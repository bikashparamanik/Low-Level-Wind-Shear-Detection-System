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
  
  /newjson

Method: GET
Description: Generates and streams new wind shear data entries for two weather stations
Response: Server-Sent Events (SSE) stream of JSON objects, where each object represents a wind shear data entry for a specific weather station
Example Response:
{
  "date": "01-06-2023",
  "time": "10:31:00",
  "station": "MENAMBAKKAM_ISRO",
  "wind_dir": 270,
  "wind_speed": 30
}

