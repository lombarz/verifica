import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Carica il dataset MNIST (diviso in set di addestramento e test)
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# Pre-elaborazione dei dati
#normalizzazione
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train = X_train.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Utilizzo di flatten() per appiattire i dati PROVATO MA NON FUNZIONA
#X_train = X_train.flatten()
#X_test = X_test.flatten()


y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Creazione del modello
model = Sequential()
model.add(Dense(units=128, activation='relu', input_shape=(784,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
# Compilazione del modello
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error',metrics=['accuracy'])

# Addestramento del modello
model.fit(X_train, y_train, epochs=10, batch_size=32)
predictions = model.predict(X_test)
#accuracy=accuracy_score(y_test,predictions) non funzionava????
print("Accuracy: ",accuracy)
cm = confusion_matrix(y_test, predictions)#matrice di confusione
print("Matrice di confusione\n",cm)
#Grafico matrice di confusione (molto bello)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Classe Predetta')#non mi ricordo come recuperare i nomi delle vere etichette
plt.ylabel('Classe Reale')
plt.title('Matrice di Confusione')
plt.show()
#ESERCIZIO NON FINITO, NON E' STATO TESTATTO IL FUNZIONAMENTO