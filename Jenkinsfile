pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tinkoosingh.jfrog.io/docker-local/flask-application:v2'
        DOCKER_CONTAINER = 'flask-application'
        DOCKER_USERNAME = 'singhtinkoo666@gmail.com tinkoosingh.jfrog.io'
        DOCKER_PASSWORD = credentials('jfrog_token')
        KUBE_TOKEN = credentials('kube_token')
    }

    stages{
    // stage('Pre-req'){
    //     steps{
    //         // sh 'minikube start'
    //         // sh 'eval $(minikube docker-env)'
    //         sh 'git pull https://github.com/tinkoosingh/three_tier.git'
    //         // sh 'minikube ip'
    //         //sh 'git clone https://github.com/tinkoosingh/three_tier.git'
    //     }
    // }

    // stage('code check by sonarqube'){
    //     steps{
    //         withSonarQubeEnv("sonar") {
    //                 tool name: 'sonar', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
    //                 sh "${tool("sonar")}/bin/sonar-scanner"      
    //     }        
    // }
    // }

    // stage('quality check'){
    //     steps{
    //     script{
    //                 def qualitygate = waitForQualityGate()
    //                     if (qualitygate.status != "OK") {
    //                         error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
    //                     }
    //     }
    //     }        
    // }

    // stage('Getting image from Artifactory') {
    //     steps{
    //         echo 'Fetching docker image..'
    //         sh 'docker login -u${DOCKER_USERNAME} -p=${DOCKER_PASSWORD}'
    //         sh 'docker pull ${DOCKER_IMAGE}'
    //     }
    // }

    // stage('Image Scane'){
    //     steps{
    //         sh 'trivy image ${DOCKER_IMAGE}'
    //     }
    // }

    // stage('Test'){
    //     steps{
    //         echo 'Testing..'
    //         sh 'docker stop ${DOCKER_CONTAINER}  || true'
    //         sh 'docker rm ${DOCKER_CONTAINER}  || true'
    //         sh 'docker run --name ${DOCKER_CONTAINER} -d ${DOCKER_IMAGE}'  
    //     }
    // }

    stage('Deploy'){
        steps{
            echo 'Deploying....'
            // sh 'minikube kubectl -- create secret docker-registry jfrog-secret --docker-server=tinkoosingh.jfrog.io/docker-local --docker-username=singhtinkoo666@gmail.com --docker-password=${DOCKER_PASSWORD}'
            sh 'kubectl apply -f mysql_dep --insecure-skip-tls-verify'
            sh 'kubectl apply -f configmap.yml --insecure-skip-tls-verify'
            sh 'kubectl apply -f app_deployment.yml --insecure-skip-tls-verify'
            sh 'kubectl get all --insecure-skip-tls-verify'
        }
    }
    }
}


