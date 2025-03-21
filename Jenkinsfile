pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/xpyre-ub/CID.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python setup.py install'  
            }
        }
        stage('Test') {
            steps {
                sh 'unittest tests/'  
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'  
                // Add deployment scripts here
            }
        }
    }
}
