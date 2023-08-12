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
      sudo docker image tag httpdimg prashant/httpdimg:1.2
      sudo docker push pras001/httpdimg:1.2
      sudo docker run --name httpdimg1 -d -p 80:80 pras001/httpdimg:1.2
    }
    }
  }
}
