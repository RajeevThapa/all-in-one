# Simple Express App

This is a simple web application using Node.js and Express.js framework. The application serves as a basic API server and a web application with server-side rendering using EJS templates.

## Features

- **Home Page:** A simple home page rendered with EJS.
- **API Endpoint:** A basic API endpoint that returns a JSON response.

## Technologies Used

- **Node.js:** A JavaScript runtime built on Chrome's V8 JavaScript engine.
- **Express.js:** A minimal and flexible Node.js web application framework.
- **EJS:** A simple templating language that lets you generate HTML markup with plain JavaScript.
- **Docker**: The application is containerized using Docker, making it easy to deploy and run in different environments.

## Overview
![image](https://github.com/RajeevThapa/all-in-one/assets/101322664/8baebd2e-5acf-4dd1-8f61-1e3eead42d35)

## Running the Application

To run the application locally:

1. Clone this repository.
2. Navigate to the root directory of the project.
3. Bash the following command in the terminal
```
node app.js
```
![Screenshot from 2024-05-16 18-54-05](https://github.com/RajeevThapa/all-in-one/assets/101322664/e0c3f508-9952-4b26-a1a8-a3e43ce50c90)
![Screenshot from 2024-05-16 18-53-52](https://github.com/RajeevThapa/all-in-one/assets/101322664/4ccca11d-4c75-4047-be5b-1ee6f80b760e)

4. Access the application from: http://127.0.0.1:3000
5. If you want to Build the Docker image:

```
docker build -t node-app .
```

6. Run a container based on the built image:

```
docker run -p 3000:3000 node-app
```

7. Access the application in your web browser at http://localhost:3000.

