pipeline{
     agent any
     stages{
         stage('CHECKOUT') {
             steps {
                         sh 'ls -la'
             }
         }
            
         stage('BUILDING') {
             steps{
                       echo 'BUILDING THE APPLICATION'
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
                     

                        


