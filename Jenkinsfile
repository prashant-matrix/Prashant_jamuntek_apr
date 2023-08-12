pipeline{
  agent any
  stages{
    stage "Connect to GitHub"
    {
      steps{
      }
    }
    stage "Build"{
      steps{
      sudo docker pull httpd
      sudo docker build -t httpdimg Dockerfile
      sudo docker image tag httpdimg susigugh/httpdimg:1.2
      sudo docker push susigugh/httpdimg:1.2
      sudo docker run --name httpdimg1 -d -p 80:80 susigugh/httpdimg:1.2
    }
    }
  }
}
