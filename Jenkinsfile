pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //nije dovrseno
                echo 'Hello World'
                sh 'python service1/entrypoint.py "md5\n proba \n\n"'
                //sh 'docker build . -t $8080:8080/node-app:${DOCKER_TAG}'
                //sh 'docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts'
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
                echo 'to be added'
            }
        }
        stage('smoke_test') {
            steps {
                sh 'chmod +x smoke_test.sh'
                sh './smoke_test.sh || true'
                junit allowEmptyResults: true, testResults: '**/test_results/*.xml'
            }
        }
        stage('end_to_end_test') {
            steps {
                echo 'End to end test step'
            }
        }
        stage('deploy_to_production') {
            steps {
                echo 'to be added'
            }
        }    
    }
}
