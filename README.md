# geekStuff




#CCSP Cloud Security Operations 


Physical Hardware : 


          Cloud environment requires physical hardware Security controls 
   Operating system : 
  BIOS (Perform test and load the hardware)  stored in hardware chip(firmware) 
                                       Protecting Bios is crucial point 
                                          UEFI : Test and validate the BIOS by signature 
                                          
                                          
                                          
                                          
TPM : cryptographic chip for device security - serving as the UEFI of root of trust,Protecting encryption key, verifying hypervisor integrity 

drive&firmware updates 


#Virtualization security requirement 
                      CPU complete cycle 
                      Memory managment 
                      Maintenaing securiy over hypervisor 
                      Apply hypervior updates 
                                       
                                     
                                       Guest operating system : to monitor other OS system and also to enforce security policies 
                                       
                                       
#Local and Remote access 
   datacentre : KVM technology physical access to hardware 
                  
                  
                  Remote access 
                        KVM technology allow access to remotely (RDP)over TCP 3389
                                       
                                                
