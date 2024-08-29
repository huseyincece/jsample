pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'odinedevops/my-python-app'
        DOCKER_HUB_CREDS = credentials('DockerHub')
        GIT_BRANCH = 'main'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${env.GIT_BRANCH}", url: 'https://github.com/huseyincece/jsample.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def app = docker.build("$DOCKER_HUB_REPO:${env.BUILD_ID}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "$DOCKER_HUB_CREDS") {
                        def app = docker.image("$DOCKER_HUB_REPO:${env.BUILD_ID}")
                        app.push()
                    }
                }
            }
        }

        stage('Deploy to Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name my-python-app odinedevops/my-python-app:${env.BUILD_ID}'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    sh 'pip install selenium'
                    sh 'python test_script.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker stop my-python-app || true'
            sh 'docker rm my-python-app || true'
        }
    }
}
