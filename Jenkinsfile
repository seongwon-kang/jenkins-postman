String cron_string = BRANCH_NAME == "master" ? "@hourly" : ""
//Required Plugins: Pipeline, HTML Publisher
pipeline {
    agent any
    triggers { cron(cron_string) }

    stages {
        stage("Build") {
            steps {
                echo "Building..."
            }
        }

        stage("Test") {
            steps{
                sh "newman run ./newman/postman_collection.json -r html" --exitCode 1
            }
            
        }

        stage("Deploy") {
            steps{
                sh "cat "
            }
        }

        stage("Results") {
            steps {
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: 'newman',
                    reportFiles: 'newman/*.html',
                    reportName: "Newman Report"
                ])
            }
        }
    }
}