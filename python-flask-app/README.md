# Weather App

This is a simple web application built using Flask that allows users to check the weather of a specific city. It fetches weather data from the OpenWeatherMap API and displays it to the user.

## Features

- **Search by City**: Users can enter the name of a city to get the current weather information.
- **Temperature and Description**: The application displays the temperature and a brief description of the weather conditions.
- **Responsive Design**: The application interface is designed to work well on various screen sizes, including mobile devices.

## Usage

1. Enter the name of the city you want to check the weather for in the input field.
2. Click on the "Get Weather" button.
3. The application will display the current weather information for the specified city, including temperature and weather description.
4. To search for weather information for another city, click on the "Search for another city" button.

## Technologies Used

- **Flask**: Flask is a micro web framework for Python used to develop web applications.
- **OpenWeatherMap API**: The application uses the OpenWeatherMap API to fetch weather data for cities.
- **HTML/CSS**: Used for structuring and styling the web pages.
- **Docker**: The application is containerized using Docker, making it easy to deploy and run in different environments.

## Running the Application

To run the application locally:

1. Make sure you have Docker installed on your system.
2. Clone this repository.
3. Navigate to the root directory of the project.
4. Build the Docker image:

```
docker build -t weather-app .
```

5. Run a container based on the built image:

```
docker run -p 3000:3000 weather-app
```

6. Access the application in your web browser at http://localhost:3000.



