pipeline {
  agent any
  environment {
      IMAGE_NAME = "welcome-container:v1_03102025"
      KUBE_CONFIG = "/var/lib/jenkins/.kube/config"
  }
  stages {
    stage('Clone Repository') {
      steps {
        git credentialsId: '4641b99e-5f67-4515-a8ea-a89ce282213e', url: 'git@github.com:aaraskumar-git/jenkins-pipeline.git', branch: 'main'
      }
    }
    stage('List Files') {
      steps {
        sh 'ls -l'
      }
    }
    stage('Check Dockerfile') {
      steps {
        script {
          if (fileExists('Dockerfile')) {
            echo "✅ Dockerfile found!"
            sh 'head -n 10 Dockerfile'
          } else {
            error "❌ Dockerfile not found in repo root!"
          }
        }
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          def dockerImage = docker.build(IMAGE_NAME)
          echo "✅ Docker image '${IMAGE_NAME}' built and available locally."
        }
      }
    }
    stage('Deploy to Kubernetes Pod') {
      steps {
        kubectl kubeconfig: KUBE_CONFIG, command: 'apply -f deployment.yaml'
        kubectl kubeconfig: KUBE_CONFIG, command: 'apply -f service.yaml'
      }
    }
    stage('Verify Deployment and URL') {
      steps {
        sleep(15)
        echo "Checking Kubernetes resources..."
        kubectl kubeconfig: KUBE_CONFIG, command: 'get deployments'
        kubectl kubeconfig: KUBE_CONFIG, command: 'get services'
        echo "Testing Flask application URL..."
        sh 'curl --fail http://localhost:30080'
      }
    }
  }
}
