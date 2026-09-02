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
           
          stage('TESTING') {
              steps{
                       echo 'TESTING THE APPLICATION'
              }
          }
       
          stage('DEPLOYING') {
              steps{
                       echo 'DEPLOYING THE APPLICATION'
              }
          }

      }
  }
                     

                        


