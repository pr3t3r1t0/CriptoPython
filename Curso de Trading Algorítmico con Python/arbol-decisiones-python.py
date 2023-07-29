from sklearn import tree
from os import system
#Se crea la instancia del árbol de decisión.
clf = tree.DecisionTreeClassifier()
#[sp500, Gold, eth]
X = [[-0.74, 0.67, 7.30], [-0.61, -0.25, -3.32], [2.46, -0.93, 2.66], 
     [-0.75, -0.25, 4.20]]
#La salida donde se dice si es data1 o data2
Y = ['baja', 'sube', 'sube', 'baja']
#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)
#Datos nuevos para predecir
#Se definen los datos 1 y 2
dato1 = [1.36, 0.02, 2.91]
#dato2 = [185, 62, 37]
prediction = clf.predict([dato1])
#representacion
text_representation = tree.export_text(clf)
print(text_representation)
################
print(prediction)
if prediction == 'sube':
    print("Estas caraterísticas son de bitcoin sube")
    def comprar():
        print("Lanzando operación de compra...")
    comprar()

else:
    print("Estas características son de bitcoin baja")
    msg()