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
                junit allowEmptyResults: true, testResults: '**/test_results/*.xml'
            }
        }
        stage('deploy_to_staging') {
            steps {
                echo 'will be'
            }
        }
        stage('smoke_test') {
            steps {
                sleep 60
                sh "./smoke_test.sh"
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
