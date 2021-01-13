#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:41:39 2021

@author: singaresekou & gueyelamine
"""
import math
import pandas as pd
from time import time
from random import random, seed
from pyspark.sql import SparkSession
spark = SparkSession.builder\
                    .master("local[*]")\
                    .appName('Estimate_Pi')\
                    .getOrCreate()
sc = spark.sparkContext

n_points = 100000

def is_point_inside_unit_circle(p):
    
     x, y = random(), random()
     return 1 if x*x + y*y < 1 else 0


def pi_estimator_spark(n) :
       t_0= time()
       count = sc.parallelize(range(0, n))\
                 .map(is_point_inside_unit_circle)\
                 .reduce(lambda a, b : a + b)
       spark_pi = 4.0*count/n
       time_spark = time() - t_0
       return spark_pi, time_spark
       sc.stop()

seed(135)      
spark_pi, time_spark = pi_estimator_spark(n_points)
print("Pi avec spark est sensiblement égal à {}" .format(spark_pi))
print("Le temps de calcul est : %s" % time_spark)

def pi_estimator_numpy(n):
    N = 0
    t_1 = time()
    for i in range(n):
        N += is_point_inside_unit_circle(1)
    numpy_pi = 4 * N / n
    time_numpy = time() - t_1
    return numpy_pi, time_numpy
    
seed(135)
numpy_pi, time_numpy = pi_estimator_numpy(n_points)
print("Pi avec numpy est sensiblement égal à {}" .format(numpy_pi))
print("Le temps de calcul est : %s" % time_numpy)

def affichage_tab(n):

    #spark
    spark_pi, time_spark = pi_estimator_spark(n_points)
    # numpy
    numpy_pi, time_numpy = pi_estimator_numpy(n)
    
    # Affichage dans un tableau

    aff={"N = "+str(n):["estimation pi","Ecart % Math.pi","Total time in seconds"],"spark":[spark_pi,spark_pi-math.pi,time_spark], "numpy":[numpy_pi,numpy_pi-math.pi,time_numpy]}
    aff=pd.DataFrame(aff)
    display(aff)

# Appel de la fonction 
n=100000
seed(130)
affichage_tab(n)

################

n=1000000
seed(130)
affichage_tab(n)