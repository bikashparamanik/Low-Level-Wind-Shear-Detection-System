# Flask API for Wind Shear Data

This Flask API generates and streams wind shear data in JSON format for various runways and weather stations. It provides two endpoints: `/returnjson` and `/newjson`.

## Features

- Generates random wind direction and wind speed data for multiple runways
- Provides wind direction data in various formats: instantaneous, 1-minute average, 2-minute average, 10-minute average, and at max wind speed
- Provides wind speed data in various formats: instantaneous, 1-minute average, 2-minute average, 10-minute average, and max wind speed
- Generates wind direction and wind speed data for two weather stations: MENAMBAKKAM_ISRO and ENNORE_PORT
- Streams data in real-time using Server-Sent Events (SSE)

## Endpoints

### `/returnjson`

- Method: GET
- Description: Generates and streams original wind shear data entries for multiple runways
- Response: Server-Sent Events (SSE) stream of JSON objects, where each object represents a wind shear data entry for a specific runway
- Example Response:
  ```json
  {
    "date": "2023-06-01",
    "time": "10:30:00",
    "runway": "18-TDZ",
    "windDirection": {
      "instantaneous": 180,
      "oneMinuteAvg": 190,
      "twoMinuteAvg": 185,
      "tenMinuteAvg": 195,
      "atMaxWindSpeed": "--"
    },
    "windSpeed": {
      "instantaneous": 25,
      "oneMinuteAvg": 22,
      "twoMinuteAvg": 20,
      "tenMinuteAvg": 18,
      "maxWindSpeed": "--"
    }
  }
  
### `/returnjson`

The `/newjson` endpoint is part of the Flask API component of the Low-Level Wind Shear Detection System project. It generates and streams new wind shear data entries for two weather stations: MENAMBAKKAM_ISRO and ENNORE_PORT.

## Endpoint Details

- Method: GET
- URL: `/newjson`
- Description: Generates and streams new wind shear data entries for two weather stations
- Response: Server-Sent Events (SSE) stream of JSON objects, where each object represents a wind shear data entry for a specific weather station

## Example Response

```json
{
  "date": "01-06-2023",
  "time": "10:31:00",
  "station": "MENAMBAKKAM_ISRO",
  "wind_dir": 270,
  "wind_speed": 30
}

## Usage

To retrieve new wind shear data from the `/newjson` endpoint, follow these steps:

1. Make sure the Flask API is running. If not, navigate to the project directory and run the following command:
python main.py
2. Send a GET request to `http://localhost:5000/newjson` using an SSE client or by making an HTTP request with the appropriate headers.

3. The API will start streaming wind shear data entries for the two weather stations in real-time.

4. Each data entry will be in JSON format and will contain the following fields:
- `date`: The date of the wind shear measurement (format: "DD-MM-YYYY")
- `time`: The time of the wind shear measurement (format: "HH:MM:SS")
- `station`: The name of the weather station (either "MENAMBAKKAM_ISRO" or "ENNORE_PORT")
- `wind_dir`: The wind direction in degrees (0-360)
- `wind_speed`: The wind speed in knots (0-50)

5. Process and utilize the received wind shear data entries as needed in your application.
