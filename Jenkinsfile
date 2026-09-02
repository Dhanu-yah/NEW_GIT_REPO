pipeline{
     agent any
     stages{
         stage('CHECKOUT') {
             steps {
                         sh 'ls -la'
             }
         }
            
         stage('PYTHON VERSION') {
             steps{
                       sh 'python --version'
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
                     

                        


