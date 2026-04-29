# Assignment 2 - ACEest Gym Management System

## Project Overview

This is a simple Flask-based web application for ACEest Functional Fitness & Gym. The application displays different fitness program plans including workout schedules and nutrition information for Fat Loss, Muscle Gain, and Beginner programs. It demonstrates basic DevOps practices including version control, testing, containerization, and CI/CD.

## Assignment 2 – CI/CD Pipeline with Minikube

The Assignment 2 is extension of previous Assignment 1 which is available at - https://github.com/2024TM93664/ACEest-gym

### Files added for Assignment 2
- `Jenkinsfile`
- `sonar-project.properties`
- `k8s/deployment.yaml`
- `k8s/service.yaml`
- `k8s/blue-green.yaml`

### Tools used
- Jenkins
- SonarQube
- Docker
- Minikube
- kubectl

### Pipeline flow
1. Checkout source code
2. Install Python dependencies
3. Run `pytest`
4. Perform SonarQube analysis
5. Build Docker image
6. Deploy to Minikube

### How to run locally with Minikube
1. Install Minikube and start it:
   ```bash
   minikube start
   ```
2. Use Minikube Docker environment:
   ```bash
   eval $(minikube docker-env)
   ```
3. Build the app image inside Minikube:
   ```bash
   docker build -t aceest-gym:latest .
   ```
4. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/service.yaml
   kubectl apply -f k8s/deployment.yaml
   ```
5. Open the app in a browser:
   ```bash
   minikube service aceest-gym-service --url
   ```

### Useful kubectl commands
- Check deployment rollout:
  ```bash
  kubectl rollout status deployment/aceest-gym-deployment
  ```
- View pods:
  ```bash
  kubectl get pods
  ```
- View service:
  ```bash
  kubectl get svc
  ```
- Rollback deployment:
  ```bash
  kubectl rollout undo deployment/aceest-gym-deployment
  ```

### Docker and Minikube commands
- Build Docker image locally:
  ```bash
  docker build -t aceest-gym .
  ```
- Start Minikube:
  ```bash
  minikube start
  ```
- Switch Docker to Minikube environment:
  ```bash
  eval $(minikube docker-env)
  ```
- Open service in browser:
  ```bash
  minikube service aceest-gym-service
  ```
