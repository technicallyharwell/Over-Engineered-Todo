pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
        ansicolor('xterm')
    }
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
        stage('Lint') {
            steps {
                sh """
                    echo "installing linting dependencies..."
                    pip install --user -r config/build/lint-requirements.txt
                    echo "linting..."
                    python -m ruff .
                    echo "uninstalling linting dependencies..."
                    pip uninstall --yes -r config/build/lint-requirements.txt
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
