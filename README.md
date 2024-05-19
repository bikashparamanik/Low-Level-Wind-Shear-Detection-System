# Low-Level Wind Shear Detection System

The Low-Level Wind Shear Detection System is a web-based application that provides real-time monitoring and alerting for low-level wind shear phenomena. It combines data from multiple sources, including flask APIs and local weather stations, to provide a comprehensive view of wind shear conditions.
## Dashboard![Screenshot (109)](https://github.com/bikashparamanik/Low-Level-Wind-Shear-Detection-System/assets/118504748/68526cd7-1ebd-432e-ae5c-61cd35d597e9)

The dashboard provides an intuitive and interactive interface for monitoring wind shear conditions. It includes the following components:

- Wind direction and speed display using a wind compass
- Runway-specific wind shear monitoring and alerting
- Wind shear magnitude and direction indicators
- Visual representation of wind shear history using a wind rose chart
- Responsive and user-friendly interface

## Features

- Real-time wind shear data visualization on an interactive dashboard
- Wind direction and speed display using a wind compass
- Runway-specific wind shear monitoring and alerting
- Wind shear magnitude and direction indicators
- Integration with flask APIs for fetching wind data
- Visual representation of wind shear history using a wind rose chart
- Responsive and user-friendly interface

## System Architecture

The Low-Level Wind Shear Detection System consists of the following components:

1. Flask APIs:
   - `returnjson` API: Provides real-time wind data from various runways
   - `newjson` API: Provides wind data from local weather stations (MENAMBAKKAM_ISRO and ENNORE_PORT)

2. Django Web Application:
   - Fetches wind data from the flask APIs using background threads
   - Processes and analyzes the wind data to calculate wind shear magnitude and direction
   - Renders the dashboard template with the latest wind data
   - Updates the dashboard in real-time using AJAX requests

3. Dashboard:
   - Displays wind direction, wind speed, head wind, and cross wind data
   - Visualizes wind direction using a wind compass
   - Shows wind shear warnings based on wind speed thresholds
   - Plots wind shear history on a wind rose chart
   - Indicates wind speed at different altitudes using runway markers

## Installation

1. Clone the repository:
git clone https://github.com/your-username/Low-Level-Wind-Shear-Detection-System.git
2. Navigate to the project directory:
cd Low-Level-Wind-Shear-Detection-System
3. Install the required dependencies:
pip install -r requirements.txt
4. Configure the flask APIs:
- Update the `main.py` file with the appropriate host and port settings
- Start the flask APIs by running `python main.py`

5. Configure the Django web application:
- Update the `settings.py` file with the necessary database and other settings
- Apply database migrations by running `python manage.py migrate`
- Start the Django development server by running `python manage.py runserver`

6. Access the Low-Level Wind Shear Detection System by navigating to `http://localhost:8000` in your web browser.

## Usage

1. Select the desired runway from the dropdown menu to view wind data specific to that runway.
2. Choose the data options (instant, 1min avg, 2min avg, 10min avg) to display the corresponding wind data.
3. Monitor the wind direction and speed using the wind compass and data boxes.
4. Pay attention to the wind shear warnings displayed when the wind speed exceeds the specified threshold.
5. Analyze the wind shear history using the wind rose chart, where dots represent wind shear events.
6. View the wind speed at different altitudes using the runway markers.

## Contributing

Contributions to the Low-Level Wind Shear Detection System are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## Acknowledgements

- The Low-Level Wind Shear Detection System utilizes data from the flask APIs and local weather stations.
- The project is developed as part of the collaboration between Christ University Lavasa and the Indian Meteorological Department (IMD).
