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
| N = 100 000 |	spark	| numpy |
| : ----: | : ---: | : ---: |
| Estimation de pi |	3.147640	| 3.144960 |
| Ecart % Math.pi	| 0.006047	|0.003367 |
| Total time en secondes	| 0.145487 | 0.202782 |

<br />
| N = 1 000 000 |	spark	| numpy |
| :----- | :----: | ----: |
| Estimation de pi |	3.145560	| 3.143464 |
| Ecart % Math.pi	| 0.003967	| 0.001871 |
| Total time en secondes	| 0.191222 | 0.567063 |

Nous avons constaté que lorsqu'on passe de n = 100.000 à n = 1.000.000 <br />
les valeurs estimées de pi se rapprochent plus de Math.pi. <br />
Donc l'estimation devient plus précise.
