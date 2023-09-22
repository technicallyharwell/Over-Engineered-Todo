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
                    filename 'CI/CI-python.Dockerfile'
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
                            poetry install --with test --no-interaction
                            """
                    }
                }
                stage('Lint') {
                    steps {
                        sh """
                            echo "linting..."
                            cp CI/ruff.toml ./ruff.toml
                            poetry run ruff .
                            echo "finished linting"
                            """
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing..'
                        sh """
                           cp CI/pretest.sh ./pretest.sh
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
                    filename 'CI/CI-sonar.Dockerfile'
                    args '--network=host'
                }
            }
            steps {
                unstash 'sources'
                sh 'cp CI/sonar-project.properties ./sonar-project.properties'
                withSonarQubeEnv('SonarQube') {
                    sh "sonar-scanner -Dsonar.branch.name=$BRANCH_NAME"
                }
                waitForQualityGate abortPipeline: true
            }
        }
    }
    post {
        always {
            node(null) {
                script {
                    if (env.BRANCH_NAME.startsWith('PR')) {
                        def buildLink = "${env.BUILD_URL}"
                        def comment = "Build: ${buildLink} finished with status ${currentBuild.currentResult}"
                        def repoOwner = "technicallyharwell"
                        def repoName = "Over-Engineered-Todo"
                        echo "Commenting on PR ${env.CHANGE_ID} with ${comment}"
                        sh """
                            curl -X POST -H "Authorization: token ${env.GITHUB_SVC_ACC_TOKEN}" -d '{"body":"${comment}"}' https://api.github.com/repos/${repoOwner}/${repoName}/issues/${env.CHANGE_ID}/comments
                            """
                    }
                }
            }
        }
    }
}