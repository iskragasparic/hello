pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Hello World'
            }
        }    
        stage('proba'){
            steps{
                sh 'docker build service1'
                sh 'docker run service1'
            }
        }
    }
}
