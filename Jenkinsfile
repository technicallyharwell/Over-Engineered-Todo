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
                    args '-u root:root'
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
                    stash name: 'repo', includes: '**'
                }
            }
        }

        stage('Code Coverage') {
            agent {
                dockerfile {
                    filename 'CI-build.Dockerfile'
                    args '-u root:root'
                }
            }
//            environment {
//                SCANNER_HOME = tool 'SonarQubeScanner'
//            }
            steps {
                unstash 'repo'
                sh """
                    echo 'Running SonarQube analysis'
                    sonar-scanner --version
                    sonar-scanner \
                    -Dsonar.projectKey=$BRANCH_NAME
                    """
                waitForQualityGate abortPipeline: true
            }
        }
    }
}