    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-ci-app:1.0 .'
            }
        }
    }
}
