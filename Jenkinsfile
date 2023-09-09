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
        stage('Build CI deps') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pwd'
                    echo 'Building..'
                    sh 'pip install --user -r config/build/ci-requirements.txt'
                    echo 'Installed all CI dependencies'
                }
            }
        }
        stage('Lint') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pwd'
                    echo 'Linting..'
                    sh 'ruff check .'
                    echo 'Linting complete'
                }
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
