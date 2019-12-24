String cron_string = BRANCH_NAME == "master" ? "@hourly" : ""
//Required Plugins: Pipeline, HTML Publisher(https://plugins.jenkins.io/htmlpublisher)
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
                sh "newman run ./newman/postman_collection.json -r html || true"
            }
            
        }

        stage("Deploy") {
            steps{
                sh "cat "
            }
        }

        stage("Results") {
            steps {
                sh "pwd"
                sh "cp newman/`ls -Art newman | tail -n 1` newman/newman_latest.html"
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: 'newman',
                    reportFiles: 'newman_latest.html',
                    reportName: "Newman Report"
                ])
            }
        }
    }
}