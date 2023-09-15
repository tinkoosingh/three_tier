pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app"
        DOCKER_CONTAINER = "flask-application"
    }

    stages{

    stage('code check by sonarqube'){
        
        
        steps{
        

            withSonarQubeEnv("sonar") {
                    // sh 'chmod +x gradlew'
                    // sh './gradlew sonarqube'
                    tool name: 'sonar', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    sh "${tool("sonar")}/bin/sonar-scanner"
                   
        
        }        
    }
    }

    stage('quality check'){
        steps{
        script{

                    def qualitygate = waitForQualityGate()
                        if (qualitygate.status != "OK") {
                            error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
                        }
        }
        }        
    }
    

    stage('Build') {
        steps{
            echo 'Building..'
            //sh 'git clone https://github.com/tinkoosingh/three_tier.git'
            sh 'docker build -t flask-app .'
        }
    }

    // stage('Image Scane'){
    //     steps{
    //         sh 'trivy image flask-app'
    //     }
    // }

    // stage('Test'){
    //     steps{
    //         echo 'Testing..'
    //         sh 'docker stop $DOCKER_CONTAINER  || true'
    //         sh 'docker rm $DOCKER_CONTAINER  || true'
    //         sh 'docker run --name $DOCKER_CONTAINER -d $DOCKER_IMAGE '  
    //     }
    // }

    

    // stage('Deploy'){
    //     steps{
    //         echo 'Deploying....'
    //         sh 'minikube delete'
    //         sh 'minikube start'
    //         sh 'minikube kubectl -- apply -f mysql_dep/secret.yml'
    //         sh 'minikube kubectl -- apply -f mysql_dep/storage.yml'
    //         sh 'minikube kubectl -- apply -f mysql_dep/deployment.yml'
    //         sh 'minikube kubectl -- apply -f configmap.yml'
    //         sh 'minikube kubectl -- apply -f app_deployment.yml'
    //     }
    // }
    }
}

