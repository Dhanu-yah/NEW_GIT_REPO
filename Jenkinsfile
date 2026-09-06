pipeline{
     agent any
     stages{
         stage('CHECKOUT') {
             steps {
                         sh 'ls -la'
             }
         }
            
         stage('PYTHON_VERSION') {
             steps{
                       sh 'python3 --version'
             }
         }
           
          stage('INSTALL PYTHON3 DEPENDENCIES') {
              steps{
                       sh '''
                            python3 -m venv .venv
                            .venv/bin/pip install -r requirements.txt
                          '''
              }
          }

          
          stage('TESTING PHASE') {
              steps{
                    sh '.venv/bin/python -c "import requests; print(requests.__version__)"'
              }
         }


          stage('DOCKER BUILD STAGES') {
              steps{
                    sh 'docker build -t hello-python:1.0 .'
              }
          }

       
          stage('DEPLOYED') {
              steps{
                       echo 'DEPLOYING THE APPLICATION'
              }
          }

      }
  }
                     

                        


