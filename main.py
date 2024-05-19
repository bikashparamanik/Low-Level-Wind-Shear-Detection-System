from flask import Flask, Response
from flask_restful import Api, Resource
import json
import datetime
import random
import time

app = Flask(__name__)
api = Api(app)

class ReturnJSON(Resource):
    def get(self):
        def generate_original_entries():
            runways = ['18-TDZ', '34', '27-L-TDZ', '9-L-TDZ']
            while True:
                for runway in runways:
                    wind_direction = {
                        "instantaneous": random.randint(0, 360),
                        "oneMinuteAvg": random.randint(0, 360),
                        "twoMinuteAvg": random.randint(0, 360),
                        "tenMinuteAvg": random.randint(0, 360),
                        "atMaxWindSpeed": random.randint(0, 360) if random.random() < 0.5 else "--"
                    }
                    wind_speed = {
                        "instantaneous": random.randint(0, 50) if random.random() < 0.5 else "--",
                        "oneMinuteAvg": random.randint(0, 50),
                        "twoMinuteAvg": random.randint(0, 50),
                        "tenMinuteAvg": random.randint(0, 50),
                        "maxWindSpeed": random.randint(0, 50) if random.random() < 0.5 else "--"
                    }
                    now = datetime.datetime.now()
                    entry = {
                        "date": now.strftime("%Y-%m-%d"),
                        "time": now.strftime("%H:%M:%S"),
                        "runway": runway,
                        "windDirection": wind_direction,
                        "windSpeed": wind_speed
                    }
                    yield f"{json.dumps(entry)}\n"
                    time.sleep(1)  # Pause for 1 second before yielding the next entry

        def generate_new_entries():
            stations = ['MENAMBAKKAM_ISRO', 'ENNORE_PORT']
            while True:
                for station in stations:
                    wind_dir = random.randint(0, 360)
                    wind_speed = random.randint(0, 50)
                    now = datetime.datetime.now()
                    entry = {
                        "date": now.strftime("%d-%m-%Y"),
                        "time": now.strftime("%H:%M:%S"),
                        "station": station,
                        "wind_dir": wind_dir,
                        "wind_speed": wind_speed
                    }
                    yield f"{json.dumps(entry)}\n"
                    time.sleep(1)  # Pause for 1 second before yielding the next entry

        return Response(generate_original_entries(), mimetype='text/event-stream')

class ReturnNewJSON(Resource):
    def get(self):
        def generate_new_entries():
            stations = ['MENAMBAKKAM_ISRO', 'ENNORE_PORT']
            while True:
                for station in stations:
                    wind_dir = random.randint(0, 360)
                    wind_speed = random.randint(0, 50)
                    now = datetime.datetime.now()
                    entry = {
                        "date": now.strftime("%d-%m-%Y"),
                        "time": now.strftime("%H:%M:%S"),
                        "station": station,
                        "wind_dir": wind_dir,
                        "wind_speed": wind_speed
                    }
                    yield f"{json.dumps(entry)}\n"
                    time.sleep(1)  # Pause for 1 second before yielding the next entry

        return Response(generate_new_entries(), mimetype='text/event-stream')

api.add_resource(ReturnJSON, '/returnjson')
api.add_resource(ReturnNewJSON, '/newjson')

if __name__ == '__main__':
    app.run(debug=True)