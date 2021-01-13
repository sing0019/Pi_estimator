# Pi_estimator		
Ce projet a pour but de faire une comparaison entre les valeurs estimées de PI d'une par Spark et d'autre par Numpy.		

 
 Pour pouvoir tester cet exemple, veuillez ouvrir un terminal et suivre les étapes ci-dessous: <br />		
 pip install pyspark  <br />			
 git clone https://github.com/sing0019/pi_estimator  <br />	
 cd pi_estimator  <br />	
 python script/estimator_pi.py  <br />	

  
  # Tableau recaputilatif 		
 ## Comparaison de performances		
 <br />		

  <img width="420" alt="Capture d’écran 2021-01-13 à 22 24 55" src="https://user-images.githubusercontent.com/71514636/104513012-5108ad80-55ef-11eb-9a2c-ed5bb00d0aec.png">
  
<img width="412" alt="Capture d’écran 2021-01-13 à 22 21" src="https://user-images.githubusercontent.com/71514636/104513028-5534cb00-55ef-11eb-9c6c-b0271b0f1df1.png">

Nous avons constaté que lorsqu'on passe de n = 100.000 à n = 1.000.000 <br />		
les valeurs estimées de pi se rapprochent plus de Math.pi. <br />		
L'estimation devient plus précise.
