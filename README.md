# Pi_estimator
#Python

Pour pouvoir tester cet exemple, veuillez ouvrir un terminal et suivre les étapes ci-dessous:\
pip install pyspark\
git clone https://github.com/sing0019/pi_estimator \
cd pi_estimator\
python script/estimator_pi.py\

# Tableau recaputilatif 
## Comparaison de performances

| N = 100000 |	spark	| numpy |
| : ---- : | : --- : | : --- : |
| Estimation de pi |	3.147640	| 3.144960 |
| Ecart % Math.pi	| 0.006047	|0.003367 |
| Total time en secondes	| 0.145487 | 0.202782 |

<br />
| N = 1000000 |	spark	| numpy |
| : ---- : | : --- : | : --- : |
| Estimation de pi |	3.145560	| 3.143464 |
| Ecart % Math.pi	| 0.003967	| 0.001871 |
| Total time en secondes	| 0.191222 | 0.567063 |
