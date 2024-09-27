import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Caricare il dataset Iris
data = load_iris()
# Crea un DataFrame di pandas per load_iris
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# esplorazione dei dati
print(df.head())
print(df.describe())
print("Classi target:", data.target_names)


#suddivisione dati
X = data.data
y = data.target  

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)#normalizzare e ridimensiore i dati prima  di applicare algoritmi di ML

# # Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

knn=KNeighborsClassifier(n_neighbors=5)#KNN
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
accuracy=accuracy_score(y_test,predictions)
print("Accuracy: ",accuracy)
cm = confusion_matrix(y_test, predictions)#matrice di confusione
print("Matrice di confusione\n",cm)
#Grafico matrice di confusione (molto bello)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)#heatmap
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Reale')
plt.title('Matrice di Confusione')
plt.show()
