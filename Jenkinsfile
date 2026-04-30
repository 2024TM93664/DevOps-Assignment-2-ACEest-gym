pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "aceest-gym:latest"
    SONAR_HOST_URL = "${SONAR_HOST_URL}"
    SONAR_TOKEN = "${SONAR_TOKEN}"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Run tests') {
      steps {
        sh 'python3 -m pytest -q'
      }
    }

    stage('SonarQube analysis') {
      steps {
        sh '''
          sonar-scanner \
            -Dsonar.projectKey=aceest-gym \
            -Dsonar.sources=. \
            -Dsonar.host.url=${SONAR_HOST_URL} \
            -Dsonar.login=${SONAR_TOKEN}
        '''
      }
    }

    stage('Build Docker image') {
      steps {
        sh 'docker build -t ${DOCKER_IMAGE} .'
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
          kubectl apply -f k8s/service.yaml
          kubectl apply -f k8s/deployment.yaml
          kubectl rollout status deployment/aceest-gym-deployment
        '''
      }
    }
  }

  post {
    always {
      echo 'Pipeline finished.'
    }
  }
}
