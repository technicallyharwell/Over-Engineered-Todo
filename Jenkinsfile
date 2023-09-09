pipeline {
    parameters {
        gitParameter branchFilter: 'origin/(.*)', defaultValue: 'main', name: 'BRANCH', type: 'PT_BRANCH'
    }
    environment {
        GIT_REPO_URL = 'https://github.com/technicallyharwell/fastapi-templates.git'
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out...'
                git branch: "${params.BRANCH}", url: "${GIT_REPO_URL}"
            }
        }
        stage('Build CI deps') {
            steps {
                echo 'Building..'
                sh 'pip install -r config/build/ci-requirements.txt'
                echo 'Installed all CI dependencies'
            }
        }
        stage('Lint') {
            steps {
                echo 'Linting..'
                sh 'ruff check .'
                echo 'Linting complete'
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
