# Pi_estimator
#Python

Pour pouvoir tester cet exemple, veuillez ouvrir un terminal et suivre les étapes ci-dessous:\
pip install pyspark\
git clone https://github.com/sing0019/pi_estimator \
cd pi_estimator\
python script/estimator_pi.py\

# Ce projet a pour but de faire une comparaison entre les valeurs estimées de PI d'une par Spark et d'autre par Numpy.

# Tableau recaputilatif 
## Comparaison de performances
<br />

/Users/singaresekou/Desktop/Capture d’écran 2021-01-13 à 22.21.png

<br />
/Users/singaresekou/Desktop/Capture d’écran 2021-01-13 à 22.24.55.png

Nous avons constaté que lorsqu'on passe de n = 100.000 à n = 1.000.000 <br />
les valeurs estimées de pi se rapprochent plus de Math.pi. <br />
L'estimation devient plus précise.
