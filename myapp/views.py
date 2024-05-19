import math
import json
import requests
from django.http import JsonResponse
from django.template.response import TemplateResponse
from datetime import datetime, timedelta
from django.conf import settings
import time
import threading
import numpy as np

latest_wind_data = {
    'wind_direction_instantaneous': 0,
    'wind_direction_one_minute_avg': 0,
    'wind_direction_two_minute_avg': 0,
    'wind_direction_ten_minute_avg': 0,
    'wind_direction_at_max_wind_speed': 0,
    'wind_speed_instantaneous': 0,
    'wind_speed_one_minute_avg': 0,
    'wind_speed_two_minute_avg': 0,
    'wind_speed_ten_minute_avg': 0,
    'wind_speed_max': 0,
    'shear_magnitude': 0,
    'shear_direction': 0,
    'shear_history': [],
    'menambakkam_isro_wind_speed': 0,
    'ennore_port_wind_speed': 0,
}

def handle_wind_data(request):
    try:
        return JsonResponse(latest_wind_data)
    except Exception as e:
        return JsonResponse({'error': 'Error fetching wind data.'}, status=500)

def calculate_wind_shear(top_wind_speed, top_wind_direction, bottom_wind_speed, bottom_wind_direction):
    # Convert wind directions to radians
    top_wind_direction_rad = np.deg2rad(top_wind_direction)
    bottom_wind_direction_rad = np.deg2rad(bottom_wind_direction)

    # Calculate wind vectors
    top_wind_vector = np.array([top_wind_speed * np.cos(top_wind_direction_rad),
                                top_wind_speed * np.sin(top_wind_direction_rad)])
    bottom_wind_vector = np.array([bottom_wind_speed * np.cos(bottom_wind_direction_rad),
                                   bottom_wind_speed * np.sin(bottom_wind_direction_rad)])

    # Calculate wind shear (vector subtraction)
    wind_shear_vector = top_wind_vector - bottom_wind_vector

    # Calculate magnitude and direction of wind shear vector
    shear_magnitude = np.linalg.norm(wind_shear_vector)
    shear_direction_deg = np.degrees(np.arctan2(wind_shear_vector[1], wind_shear_vector[0]))

    # Ensure the wind shear direction is within [0, 360) degrees
    if shear_direction_deg < 0:
        shear_direction_deg += 360

    return shear_magnitude, shear_direction_deg

def fetch_wind_data_from_flask_returnjson():
    global latest_wind_data
    while True:
        response_returnjson = requests.get('http://127.0.0.1:5000/returnjson', stream=True)

        if response_returnjson.status_code == 200:
            for line in response_returnjson.iter_lines(decode_unicode=True):
                if line:
                    data = json.loads(line)
                    save_latest_wind_data_returnjson(data)
                    update_station_wind_speeds(data)
        else:
            print(f"Error fetching data from /returnjson endpoint. Status code: {response_returnjson.status_code}")

        time.sleep(1)

def update_station_wind_speeds(data):
    if 'stations' in data:
        if 'MENAMBAKKAM_ISRO' in data['stations']:
            latest_wind_data['menambakkam_isro_wind_speed'] = data['stations']['MENAMBAKKAM_ISRO']['wind_speed']
        if 'ENNORE_PORT' in data['stations']:
            latest_wind_data['ennore_port_wind_speed'] = data['stations']['ENNORE_PORT']['wind_speed']

def fetch_wind_data_from_flask_newjson():
    global latest_wind_data
    while True:
        response_newjson = requests.get('http://127.0.0.1:5000/newjson', stream=True)

        if response_newjson.status_code == 200:
            top_wind_speed = None
            top_wind_direction = None
            bottom_wind_speed = None
            bottom_wind_direction = None

            for line in response_newjson.iter_lines(decode_unicode=True):
                if line:
                    data = json.loads(line)
                    if data['station'] == 'MENAMBAKKAM_ISRO':
                        top_wind_speed = data['wind_speed']
                        top_wind_direction = data['wind_dir']
                        latest_wind_data['menambakkam_isro_wind_speed'] = data['wind_speed']
                    elif data['station'] == 'ENNORE_PORT':
                        bottom_wind_speed = data['wind_speed']
                        bottom_wind_direction = data['wind_dir']
                        latest_wind_data['ennore_port_wind_speed'] = data['wind_speed']

                    if top_wind_speed is not None and top_wind_direction is not None and bottom_wind_speed is not None and bottom_wind_direction is not None:
                        shear_magnitude, shear_direction_deg = calculate_wind_shear(top_wind_speed, top_wind_direction, bottom_wind_speed, bottom_wind_direction)
                        latest_wind_data['shear_magnitude'] = shear_magnitude
                        latest_wind_data['shear_direction'] = shear_direction_deg

                        # Add wind shear data to history
                        shear_history_item = {
                            'magnitude': shear_magnitude,
                            'direction': shear_direction_deg
                        }
                        latest_wind_data['shear_history'].append(shear_history_item)

                        # Limit shear history to 100 data points
                        if len(latest_wind_data['shear_history']) > 100:
                            latest_wind_data['shear_history'].pop(0)

        time.sleep(1)

def save_latest_wind_data_returnjson(data):
    global latest_wind_data

    # Handle '--' values for windDirection
    wind_direction_at_max_wind_speed = int(data['windDirection']['atMaxWindSpeed']) if data['windDirection']['atMaxWindSpeed'] != '--' else None
    wind_direction_instantaneous = int(data['windDirection']['instantaneous']) if data['windDirection']['instantaneous'] != '--' else None
    wind_direction_one_minute_avg = int(data['windDirection']['oneMinuteAvg']) if data['windDirection']['oneMinuteAvg'] != '--' else None
    wind_direction_two_minute_avg = int(data['windDirection']['twoMinuteAvg']) if data['windDirection']['twoMinuteAvg'] != '--' else None
    wind_direction_ten_minute_avg = int(data['windDirection']['tenMinuteAvg']) if data['windDirection']['tenMinuteAvg'] != '--' else None

    # Handle '--' values for windSpeed
    wind_speed_instantaneous = float(data['windSpeed']['instantaneous']) if data['windSpeed']['instantaneous'] != '--' else None
    wind_speed_one_minute_avg = float(data['windSpeed']['oneMinuteAvg']) if data['windSpeed']['oneMinuteAvg'] != '--' else None
    wind_speed_two_minute_avg = float(data['windSpeed']['twoMinuteAvg']) if data['windSpeed']['twoMinuteAvg'] != '--' else None
    wind_speed_ten_minute_avg = float(data['windSpeed']['tenMinuteAvg']) if data['windSpeed']['tenMinuteAvg'] != '--' else None
    wind_speed_max = float(data['windSpeed']['maxWindSpeed']) if data['windSpeed']['maxWindSpeed'] != '--' else None

    # Calculate head wind and cross wind for instantaneous values
    if wind_direction_instantaneous is not None and wind_speed_instantaneous is not None:
        wind_direction_radians = math.radians(wind_direction_instantaneous)
        head_wind_instantaneous = abs(wind_speed_instantaneous * math.cos(wind_direction_radians))
        cross_wind_instantaneous = abs(wind_speed_instantaneous * math.sin(wind_direction_radians))
        if 90 <= wind_direction_instantaneous <= 270:
            cross_wind_instantaneous_label = f"{cross_wind_instantaneous:.1f}R"
        else:
            cross_wind_instantaneous_label = f"{cross_wind_instantaneous:.1f}L"
    else:
        head_wind_instantaneous = None
        cross_wind_instantaneous_label = None

    latest_wind_data['wind_direction_at_max_wind_speed'] = wind_direction_at_max_wind_speed
    latest_wind_data['wind_direction_instantaneous'] = wind_direction_instantaneous
    latest_wind_data['wind_direction_one_minute_avg'] = wind_direction_one_minute_avg
    latest_wind_data['wind_direction_two_minute_avg'] = wind_direction_two_minute_avg
    latest_wind_data['wind_direction_ten_minute_avg'] = wind_direction_ten_minute_avg
    latest_wind_data['wind_speed_instantaneous'] = wind_speed_instantaneous
    latest_wind_data['wind_speed_one_minute_avg'] = wind_speed_one_minute_avg
    latest_wind_data['wind_speed_two_minute_avg'] = wind_speed_two_minute_avg
    latest_wind_data['wind_speed_ten_minute_avg'] = wind_speed_ten_minute_avg
    latest_wind_data['wind_speed_max'] = wind_speed_max
    latest_wind_data['head_wind_instantaneous'] = head_wind_instantaneous
    latest_wind_data['cross_wind_instantaneous_label'] = cross_wind_instantaneous_label

def dashboard(request):
    # Start the background threads to fetch data from Flask server
    thread_returnjson = threading.Thread(target=fetch_wind_data_from_flask_returnjson)
    thread_newjson = threading.Thread(target=fetch_wind_data_from_flask_newjson)
    thread_returnjson.start()
    thread_newjson.start()
    return TemplateResponse(request, 'myapp/dashboard.html', {'latest_wind_data': latest_wind_data})