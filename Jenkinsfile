pipeline {
    parameters {
        gitParameter branchFilter: 'origin/(.*)', name: 'BRANCH', type: 'PT_BRANCH'
    }
    environment {
        GIT_REPO_URL = 'https://github.com/technicallyharwell/fastapi-templates.git'
        PATH = '/var/lib/jenkins/:${PATH}'
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out...'
                checkout scm
            }
        }
        stage('Create virtualenv') {
            steps {
                echo 'Creating virtualenv..'
                sh 'python3 -m venv venv'
                echo 'Created virtualenv'
                echo 'Activating virtualenv..'
                sh 'source venv/bin/activate'
                echo 'Activated virtualenv'
                sh 'which pip'
                sh 'which python'
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
