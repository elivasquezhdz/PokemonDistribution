import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
type1 = []
total = []
i=0
for line in file('Pokemon.csv'):
	row = line.split(",")
	type1.append(row[2])
	i+=1
	try:
		total.append(float(row[4]))
	except ValueError,e:
		print "error",e,"on line",i
type1.remove('Type 1') #remove the first item, it is not a type!
norm_total = [float(i)/max(total) for i in total]#Normalize the values
for n,i in enumerate(type1):#Convert the string list to an int list
	if i == 'Bug':
		type1[n]=1
	if i == 'Dark':
		type1[n]=2
	if i == 'Dragon':
		type1[n]=3
	if i == 'Electric':
		type1[n]=4
	if i == 'Fairy':
		type1[n]=5
	if i == 'Fighting':
		type1[n]=6
	if i == 'Fire':
		type1[n]=7
	if i == 'Flying':
		type1[n]=8
	if i == 'Ghost':
		type1[n]=9
	if i == 'Grass':
		type1[n]=10
	if i == 'Ground':
		type1[n]=11
	if i == 'Ice':
		type1[n]=12
	if i == 'Normal':
		type1[n]=13
	if i == 'Poison':
		type1[n]=14
	if i == 'Psychic':
		type1[n]=15
	if i == 'Rock':
		type1[n]=16
	if i == 'Steel':
		type1[n]=17
	if i == 'Water':
		type1[n]=18
#Bug		1 	#Dark		2
#Dragon		3	#Electric	4
#Fairy		5	#Fighting	6
#Fire		7	#Flying		8
#Ghost		9	#Grass		10
#Ground		11	#Ice		12
#Normal  	13	#Poison		14
#Psychic	15  #Rock		16
#Steel		16  #Water		17
type1_norm = [float(i)/max(type1) for i in type1]#Normalize the values
type1_normp = np.array(type1_norm).astype(dtype=np.float32) #convert my list to a Numpy array

X = np.vstack((type1_normp,norm_total)) #concatenates the data into a Matrix

af = AffinityPropagation(preference=-50).fit(X) #computes affinity propagation
cluster_centers_indices = af.cluster_centers_indices_
n_clusters_ = len(cluster_centers_indices)
centroids = af.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=169, linewidths=3,color='r', zorder=10)
plt.scatter(type1_normp,norm_total)
plt.title('Pokemon distribution, found ' + str(n_clusters_) + " Clusters")
plt.xlabel('Type1')
plt.ylabel('Total')
plt.show()