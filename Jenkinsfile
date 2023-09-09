pipeline {
    environment {
        CI = 'true'
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
    }
    agent none
    stages {
        stage('Checkout') {
            agent any
            steps {
                echo 'Checking out...'
                checkout scm
            }
        }
        stage('Build CI deps') {
            agent any
            steps {
                echo 'Building..'
                sh 'pip install -r config/build/ci-requirements.txt'
                echo 'Installed all CI dependencies'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
