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
- **Jenkins**: Jenkins is an open-source automation server that helps automate various parts of the software development process, including building, testing, and deployment.
- **ArgoCD**: ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes. It helps in managing application deployments to Kubernetes clusters.

## Overview
![image](https://github.com/RajeevThapa/all-in-one/assets/101322664/f3985c8e-935c-4ba7-b46c-2d977ab4136c)

## Running the Application

To run the application locally:

1. Clone this repository.
2. Navigate to the root directory of the project.
3. Bash the following command in the terminal
```
python3 app.py
```
![Screenshot from 2024-05-10 23-08-59](https://github.com/RajeevThapa/all-in-one/assets/101322664/c2dbd9fb-c7d7-4f18-b3e7-ed66569482b9)
![Screenshot from 2024-05-10 23-09-13](https://github.com/RajeevThapa/all-in-one/assets/101322664/5c03fe6e-5e50-493d-9579-4516c462c775)

4. Access the application from: http://127.0.0.1:5000
5. If you want to Build the Docker image (Make sure comment the lines: 13 and 19 and uncomment lines: 11 and 18 = As the dockerfile for now is made for jenkins and due to location of directory issue while automating):

```
docker build -t weather-app .
```

6. Run a container based on the built image:

```
docker run -p 3000:3000 weather-app
```

7. Access the application in your web browser at http://localhost:3000.


## Jenkins Pipeline

This repository includes a Jenkinsfile that defines a pipeline for automating the build, push, cleanup, and deployment processes for the Dockerized Flask application. The pipeline integrates with Dockerhub for image storage and GitHub for version control of Kubernetes manifests.

### Steps to Run Jenkins Pipeline

1. **Install Jenkins**: If you have trouble installing Jenkins, you can clone and execute the installation script from the provided [Install_Jenkins](https://github.com/RajeevThapa/Install_Jenkins) repository using the following commands:
    ```
    git clone https://github.com/RajeevThapa/Install_Jenkins.git
    cd Install_Jenkins
    bash install_jenkins.sh
    ```
    This script automates the installation process of Jenkins on your server or local machine.

2. **Set up Jenkins Credentials**: In Jenkins, create a credential with the ID `docker-hub-credentials` to store Dockerhub credentials for pushing the Docker image. This credential should have access to your Dockerhub account.

3. **Create a New Pipeline Job**: In Jenkins, create a new pipeline job and configure it to use the pipeline script defined in the Jenkinsfile located in your project repository.

4. **Configure Job Parameters**: If needed, adjust the environment variables defined in the Jenkinsfile, such as `IMG_NAME`, `IMG_TAG`, `DOCKERFILE_PATH`, `K8S_MANIFEST_PATH`, and `DOCKERHUB_CREDENTIALS`, to match your project setup.

5. **Run the Pipeline**: Trigger the pipeline job in Jenkins. Jenkins will execute the pipeline stages, including building the Docker image, pushing it to Dockerhub, updating the Kubernetes manifest, and committing the changes to your GitHub repository.

6. **Verify Deployment**: Once the pipeline completes successfully, verify that the Docker image has been pushed to Dockerhub and the Kubernetes manifest has been updated in your GitHub repository.
![Screenshot from 2024-05-10 23-06-31](https://github.com/RajeevThapa/all-in-one/assets/101322664/2a53552d-d5c7-4022-b1a7-ea9d0637bf63)


## Using ArgoCD

To manage deployments with ArgoCD:

1. **Check ArgoCD Pods**:
    ```
    kubectl get pods -n argocd
    ```

2. **Check ArgoCD Services**:
    ```
    kubectl get svc -n argocd
    ```

3. **Expose ArgoCD Server using NodePort**:
    ```
    kubectl edit svc argocd-server -n argocd
    ```
    Replace `type: ClusterIP` with `type: NodePort` to expose ArgoCD to a URL.

4. **List Minikube Services and Navigate to ArgoCD URL**:
    ```
    minikube service list -n argocd
    ```
    Visit the URL associated with ArgoCD in your web browser.

5. **Retrieve ArgoCD Secret**:
    ```
    kubectl get secret -n argocd
    ```

6. **Copy ArgoCD Initial Admin Password**:
    ```
    kubectl edit secret argocd-initial-admin-secret -n argocd
    ```
    Copy the password and exit.

7. **Decode and Use Credentials**:
    ```
    echo <copied_password> | base64 --decode
    ```
    Use the username `admin` and the decoded password to log in to the ArgoCD URL. 

Username is `admin` by default for ArgoCD.
![Screenshot from 2024-05-10 23-07-30](https://github.com/RajeevThapa/all-in-one/assets/101322664/4e723f8b-3bcf-4de5-8326-e6ad90c9dcba)

## Deployment in minikube
![Screenshot from 2024-05-10 23-07-45](https://github.com/RajeevThapa/all-in-one/assets/101322664/70d0e162-492c-4edd-9a9a-8388939144eb)


