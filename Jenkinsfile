pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Hello World'
                //sh 'python /home/hello/service1/entrypoint.py'
            }
        }
        stage('unit_test') {
            steps {
                echo 'Unit test step'
            }
        }
        stage('integration_test') {
            steps {
                echo 'Integration test step'
            }
        }
        stage('publish_artifact') {
            steps {
                junit 'build/reports/**/*.xml'
            }
        }
        stage('deploy_to_staging') {
            steps {
                echo 'will be'
            }
        }
        stage('smoke_test') {
            steps {
                echo 'will be'
            }
        }
        stage('end_to_end_test') {
            steps {
                echo 'End to end test step'
            }
        }
        stage('deploy_to_production') {
            steps {
                echo 'will be'
            }
        }    
    }
}
