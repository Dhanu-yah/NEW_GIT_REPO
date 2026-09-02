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
           
          stage('INSTALL DEPENDENCIES') {
              steps{
                       sh 'pip3 install -r requirements.txt'
              }
          }
       
          stage('DEPLOYING') {
              steps{
                       echo 'DEPLOYING THE APPLICATION'
              }
          }

      }
  }
                     

                        


