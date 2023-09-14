pipeline {
    triggers {
        pollSCM('')     // build on push
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
        ansiColor('xterm')
    }
    parameters {
        gitParameter branchFilter: 'origin/(.*)', name: 'BRANCH', type: 'PT_BRANCH'
    }
    environment {
        GIT_REPO_URL = 'https://github.com/technicallyharwell/fastapi-templates.git'
    }
    agent none
    stages {
        stage('Python part') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            stages {
                stage('Checkout') {
                    steps {
                        checkout scm
                    }
                }
                stage('Install') {
                    steps {
                        sh """
                            poetry lock
                            poetry install --with test
                            """
                    }
                }
                stage('Lint') {
                    steps {
                        sh """
                            echo "linting..."
                            poetry run ruff .
                            echo "finished linting"
                            """
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing..'
                        sh """
                           chmod +x ./pretest.sh
                           ./pretest.sh
                           """
                    }
                }
            }
            post {
                success {
                    stash name: 'sources', excludes: '**/__pycache__/**'
                }
            }
        }

        stage('Code Coverage') {
            agent {
                dockerfile {
                    filename 'CI-build.Dockerfile'
                    args '--network=host'
                }
            }
            steps {
                unstash 'sources'
                withSonarQubeEnv('SonarQube') {
                    sh "sonar-scanner -Dsonar.branch.name=$BRANCH_NAME"
                }
                waitForQualityGate abortPipeline: true
            }
        }
    }
}