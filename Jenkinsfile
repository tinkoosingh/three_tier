pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app"
        DOCKER_CONTAINER = "flask-application"
    }

    stages{
    stage('Build') {
        steps{
            echo 'Building..'
            sh 'docker build -t flask-app .'
        }
    }

    stage('Test'){
        steps{
            echo 'Testing..'
            sh 'docker stop $DOCKER_CONTAINER  || true'
            sh 'docker rm $DOCKER_CONTAINER  || true'
            sh 'docker run --name $DOCKER_CONTAINER -d $DOCKER_IMAGE '  
        }
    }

    

    stage('Deploy'){
        steps{
            echo 'Deploying....'
            sh 'kubectl -- apply -f mysql_dep/secret.yml'
            sh 'kubectl -- apply -f mysql_dep/storage.yml'
            sh 'kubectl -- apply -f mysql_dep/deployment.yml'
            sh 'kubectl -- apply -f configmap.yml'
            sh 'kubectl -- apply -f app_deployment.yml'
        }
    }
}
}
