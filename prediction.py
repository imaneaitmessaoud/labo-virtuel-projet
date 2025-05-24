import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#donnees : tailles (cm) et poids (kg)
taille = np.array([150,160,170,180,190])
poids = np.array([50,55,65,72,80])

#Gegression lineaire 

pente,intercept = np.polyfit(taille,poids, 1)

#predictions
x_pred = np.array([160, 175, 185])
y_pred = pente * x_pred + intercept

#addichage du graphique 
plt.scatter(taille,poids,label="Donnees")
plt.plot(x_pred,y_pred,color='red',label="Prediction lineaire")
plt.xlabel("Taille (cm)")
plt.ylabel("poids (kg)")
plt.title("Relation Taille /Poids")
plt.legend()
plt.grid()
plt.show()