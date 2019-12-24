String cron_string = BRANCH_NAME == "master" ? "@hourly" : ""

pipeline {
    agent any
    triggers { cron(cron_string) }

    stages {
        stage("Build") {
            steps {
                sh "npm install -g newman"
                echo "Building..."
            }
        }

        stage("Test") {
            sh "newman jenkins_demo.postman_collection --exitCode 1"
        }

        stage("Deploy") {
                echo 'Deploying....'
        }
    }
}