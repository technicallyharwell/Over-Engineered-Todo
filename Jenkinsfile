pipeline {
    parameters {
        gitParameter branchFilter: 'origin/(.*)', name: 'BRANCH', type: 'PT_BRANCH'
    }
    environment {
        GIT_REPO_URL = 'https://github.com/technicallyharwell/fastapi-templates.git'
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out...'
                checkout scm
                sh 'which python'
                sh 'which pip'
                sh 'whoami'
            }
        }
        stage('Create virtualenv') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pwd'
                }
            }
        }
        stage('Lint') {
            steps {
                sh """
                    echo "installing linting dependencies..."
                    pip install --user -r config/build/lint-requirements.txt
                    echo "linting..."
                    ruff .
                    echo "finished linting"
                """
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
