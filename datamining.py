import sklearn
import scipy
import numpy
import sys
import math
import random
import subprocess
import numpy as np

A = list()
B = list()
C = list()
D = list()
E = list()
F = list()
G = list()
H = list()
I = list()
J = list()
K = list()
L = list()
M = list()
N = list()
O = list()

A_test = list()
B_test = list()
C_test = list()
D_test = list()
E_test = list()
F_test = list()
G_test = list()
H_test = list()
I_test = list()
J_test = list()
K_test = list()
L_test = list()
M_test = list()
N_test = list()
O_test = list()

import csv

ftrain = open("adultdata.csv")
ftest = open("adulttest.csv")

reader = csv.DictReader(ftrain)
reader_test = csv.DictReader(ftest)

for row in reader:
	A.append(row['col_1'].strip())
	B.append(row['col_2'].strip())
	C.append(row['col_3'].strip())
	D.append(row['col_4'].strip())
	E.append(row['col_5'].strip())
	F.append(row['col_6'].strip())
	G.append(row['col_7'].strip())
	H.append(row['col_8'].strip())
	I.append(row['col_9'].strip())
	J.append(row['col_10'].strip())
	K.append(row['col_11'].strip())
	L.append(row['col_12'].strip())
	M.append(row['col_13'].strip())
	N.append(row['col_14'].strip())
	O.append(row['result'].strip())

for row in reader_test:
	A_test.append(row['col_1'].strip())
	B_test.append(row['col_2'].strip())
	C_test.append(row['col_3'].strip())
	D_test.append(row['col_4'].strip())
	E_test.append(row['col_5'].strip())
	F_test.append(row['col_6'].strip())
	G_test.append(row['col_7'].strip())
	H_test.append(row['col_8'].strip())
	I_test.append(row['col_9'].strip())
	J_test.append(row['col_10'].strip())
	K_test.append(row['col_11'].strip())
	L_test.append(row['col_12'].strip())
	M_test.append(row['col_13'].strip())
	N_test.append(row['col_14'].strip())
	O_test.append(row['result'].strip())	

d=dict()
d["?"]=0
d["State-gov"]=1
d["Self-emp-not-inc"]=2
d["Private"]=3
d["Federal-gov"]=4
d["Local-gov"]=5
d["Self-emp-inc"]=6
d["Without-pay"]=7
d["Never-worked"]=8

d["Bachelors"]=1
d["HS-grad"]=12
d["11th"]=3
d["Masters"]=4
d["9th"]=5
d["Some-college"]=6
d["Assoc-acdm"]=7
d["Assoc-voc"]=8
d["7th-8th"]=9
d["Doctorate"]=10
d["Prof-school"]=11
d["5th-6th"]=12
d["10th"]=13
d["1st-4th"]=14
d["Preschool"]=15
d["12th"]=16

d["Never-married"]=1	
d["Married-civ-spouse"]=2
d["Divorced"]=3
d["Married-spouse-absent"]=4
d["Separated"]=5
d["Married-AF-spouse"]=6
d["Widowed"]=7
d["Adm-clerical"]=8
d["Exec-managerial"]=9
d["Handlers-cleaners"]=10
d["Prof-specialty"]=11
d["Other-service"]=12
d["Sales"]=13
d["Craft-repair"]=14
d["Transport-moving"]=15
d["Farming-fishing"]=16
d["Machine-op-inspct"]=17
d["Tech-support"]=18
d["Protective-serv"]=19
d["Armed-Forces"]=20
d["Priv-house-serv"]=21

d["Not-in-family"]=1
d["Husband"]=2
d["Wife"]=3
d["Own-child"]=4
d["Unmarried"]=5
d["Other-relative"]=6

d["White"]=1
d["Black"]=2
d["Asian-Pac-Islander"]=3
d["Amer-Indian-Eskimo"]=4
d["Other"]=5

d["Male"]=1
d["Female"]=2

d["United-States"]=1
d["Cuba"]=2
d["Jamaica"]=3
d["India"]=4
d["Mexico"]=5
d["South"]=6
d["Puerto-Rico"]=7
d["Honduras"]=8
d["England"]=9
d["Canada"]=10
d["Germany"]=11
d["Iran"]=12
d["Philippines"]=13
d["Italy"]=14
d["Poland"]=15
d["Columbia"]=16
d["Cambodia"]=17
d["Thailand"]=18
d["Ecuador"]=19
d["Laos"]=20
d["Taiwan"]=21
d["Haiti"]=22
d["Portugal"]=23
d["Dominican-Republic"]=24
d["El-Salvador"]=25
d["France"]=26
d["Guatemala"]=27
d["China"]=28
d["Japan"]=29
d["Yugoslavia"]=30
d["Peru"]=31
d["Outlying-US(Guam-USVI-etc)"]=32
d["Scotland"]=33
d["Trinadad&Tobago"]=34
d["Greece"]=35
d["Nicaragua"]=36
d["Vietnam"]=37
d["Hong"]=38
d["Ireland"]=39
d["Hungary"]=40
d["Holand-Netherlands"]=41
d["48"]=42
d["<=50K"]=000
d["<=50K."]=000
d[">50K"]=001
d[">50K."]=001
#001=true, 000=false
i=0
for asd in A:
	B[i]=d[B[i]]
	D[i]=d[D[i]]
	F[i]=d[F[i]]
	G[i]=d[G[i]]
	H[i]=d[H[i]]
	I[i]=d[I[i]]	
	J[i]=d[J[i]]
	N[i]=d[N[i]]
	O[i]=d[O[i]]
	i += 1

i = 0

for asd in A_test:
	B_test[i]=d[B_test[i]]
	D_test[i]=d[D_test[i]]
	F_test[i]=d[F_test[i]]
	G_test[i]=d[G_test[i]]
	H_test[i]=d[H_test[i]]
	I_test[i]=d[I_test[i]]
	J_test[i]=d[J_test[i]]
	N_test[i]=d[N_test[i]]
	O_test[i]=d[O_test[i]]
	i += 1
	
ftrain.close()	
X = list()	
help = tuple()
X_test = list()
j=0
for asd in A:
	help=(A[j],B[j],C[j],D[j],E[j],F[j],G[j],H[j],I[j],J[j],K[j],L[j],M[j],N[j])
	X.append(help)
	j += 1

j=0
for asd in A_test:
	help=(A_test[j],B_test[j],C_test[j],D_test[j],E_test[j],F_test[j],G_test[j],H_test[j],I_test[j],J_test[j],K_test[j],L_test[j],M_test[j],N_test[j])
	X_test.append(help)
	j += 1

size=len(O_test)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, O)
P=clf.predict(X_test)
count=0
TP=0
FP=0
FN=0
TN=0
for i in range(0,size):
	if(P[i]==000 and O_test[i]==000):
		TP += 1
	else:
		if(P[i]==000 and O_test[i]==001):
			FN += 1
		else:
			if(P[i]==001 and O_test[i]==001):
				TN += 1
			else:
					FP +=1	
precision = float(TP+TN)/float(TP+TN+FP+FN)	
print ("Decision tree:")
print ("TP",TP,"FN",FN)
print ("FP",FP,"TN",TN)
print ("Accuracy",precision*100)
#print P

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf = clf.fit(X, O)
P = clf.predict(X_test)
count = 0
TP=0
FP=0
FN=0
TN=0
for i in range(0,size):
	if(P[i]==000 and O_test[i]==000):
		TP += 1
	else:
		if(P[i]==000 and O_test[i]==001):
			FN += 1
		else:
			if(P[i]==001 and O_test[i]==001):
				TN += 1
			else:
					FP +=1	

precision = float(TP+TN)/float(TP+TN+FP+FN)	
print ("Random forest:")
print ("TP",TP,"FN",FN)
print ("FP",FP,"TN",TN)
print ("Accuracy",precision*100)
#print P

from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier()
clf = clf.fit(X, O)
P = clf.predict(X_test)
count = 0
TP=0
FP=0
FN=0
TN=0
for i in range(0,size):
	if(P[i]==000 and O_test[i]==000):
		TP += 1
	else:
		if(P[i]==000 and O_test[i]==001):
			FN += 1
		else:
			if(P[i]==001 and O_test[i]==001):
				TN += 1
			else:
					FP +=1	
precision = float(TP+TN)/float(TP+TN+FP+FN)	
print ("Boosting:")
print ("TP",TP,"FN",FN)
print ("FP",FP,"TN",TN)
print ("Accuracy",precision*100)
#print P
from sklearn import svm
clf = svm.SVC()
clf=clf.fit(X, O)
P = clf.predict(X_test)
#print P
count = 0
TP=0
FP=0
FN=0
TN=0
for i in range(0,size):
	if(P[i]==000 and O_test[i]==000):
		TP += 1
	else:
		if(P[i]==000 and O_test[i]==001):
			FN += 1
		else:
			if(P[i]==001 and O_test[i]==001):
				TN += 1
			else:
					FP +=1	
precision = float(TP+TN)/float(TP+TN+FP+FN)	
print ("SVM:")
print ("TP",TP,"FN",FN)
print ("FP",FP,"TN",TN)
print ("Accuracy:",precision*100)
