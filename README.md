# Low-Level Wind Shear Detection System - Django Web Application

The Django web application is a key component of the Low-Level Wind Shear Detection System project. It provides a user-friendly interface for visualizing and interacting with wind shear data obtained from the Flask APIs.

## Features

- Real-time wind shear data visualization on an interactive dashboard
- Wind direction and speed display using a wind compass
- Runway-specific wind shear monitoring and alerting
- Wind shear magnitude and direction indicators
- Integration with Flask APIs for fetching wind data
- Visual representation of wind shear history using a wind rose chart
- Responsive and user-friendly interface

## Installation

1. Clone the repository:
git clone https://github.com/bikashparamanik/Low-Level-Wind-Shear-Detection-System.git
2. Navigate to the project directory:
cd Low-Level-Wind-Shear-Detection-System/django-project
3. Install the required dependencies:
The project dependencies are listed in the `requirements.txt` file. To install them, run the following command:
pip install -r requirements.txt
4. Apply database migrations:
The Django project uses a database to store wind shear data. To apply the necessary database migrations, run the following command:
python manage.py migrate
5. Start the Django development server:
To start the Django development server and run the web application, use the following command:
python manage.py runserver
6. Access the web application:
Open your web browser and visit `http://localhost:8000` to access the Low-Level Wind Shear Detection System web application.

## Usage

1. Upon accessing the web application, you will be presented with the wind shear dashboard.

2. The dashboard displays real-time wind shear data, including wind direction, wind speed, head wind, and cross wind.

3. Use the dropdown menus to select the desired runway and data options (instant, 1min avg, 2min avg, 10min avg) for viewing specific wind shear information.

4. The wind compass visualizes the wind direction, and the data boxes provide numerical values for wind speed, head wind, and cross wind.

5. Wind shear warnings are displayed when the wind speed exceeds a specified threshold.

6. The wind rose chart represents the wind shear history, with dots indicating wind shear events.

7. Runway markers indicate the wind speed at different altitudes along the runway.

8. The dashboard automatically updates in real-time to provide the latest wind shear data.

## Project Structure

The Django project follows a standard structure:
django-project/
├── low_level_wind_shear_detection_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── wind_shear_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── wind_shear_app/
│       └── dashboard.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py
└── requirements.txt

- The `low_level_wind_shear_detection_system` directory contains the project-level configuration files.
- The `wind_shear_app` directory contains the application-specific files, including views, models, and URLs.
- The `templates` directory contains HTML templates used for rendering the web pages.
- The `static` directory stores static files such as CSS, JavaScript, and images.
- The `manage.py` file is the command-line utility for managing the Django project.
- The `requirements.txt` file lists the project dependencies.

## Integration with Flask APIs

The Django web application integrates with the Flask APIs to fetch wind shear data. The integration is handled in the `views.py` file of the `wind_shear_app` application.

- The `fetch_wind_data_from_flask_returnjson()` function retrieves wind shear data from the `/returnjson` endpoint of the Flask API.
- The `fetch_wind_data_from_flask_newjson()` function retrieves wind shear data from the `/newjson` endpoint of the Flask API.

The fetched data is processed and stored in the `latest_wind_data` dictionary, which is then passed to the dashboard template for rendering.

## Contributing

Contributions to the Low-Level Wind Shear Detection System project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/bikashparamanik/Low-Level-Wind-Shear-Detection-System).

## Acknowledgements

- The Low-Level Wind Shear Detection System project utilizes data from the Flask APIs and local weather stations.
- The project is developed as part of the collaboration between Christ University Lavasa and the Indian Meteorological Department (IMD).
