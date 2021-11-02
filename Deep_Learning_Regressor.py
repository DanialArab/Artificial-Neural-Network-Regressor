"""
Created on Mon Nov  1 19:09:12 2021

@author: Danial Arab
"""
# Step_1: Importing required libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error as MAE

# Step_2: Data importing and preparation 

filelist = glob(r'USROP*.csv', recursive=False)

df = []

for i in filelist:
    df.append(pd.read_csv(i))

data = df[0:7]

well_0 = data[0]
well_1 = data[1]
well_2 = data[2]
well_3 = data[3]
well_4 = data[4]
well_5 = data[5]
well_6 = data[6]


dataset = pd.concat([well_0 , well_1, well_2, well_3, well_4, well_5, well_6])

y = dataset['Rate of Penetration m/h'].to_numpy()

X = dataset.drop(labels=['Rate of Penetration m/h'],axis=1).to_numpy()
       
# Step_3: Splitting the dataset into training and testing datasets 
     
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)

# Step_4: Scaling the data

scaler=StandardScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
         
   
# Step_5: Building the deep learning model 
           
model = Sequential()
model.add(Dense(128, input_dim=12, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
model.summary()

# Step_6: Training the model 

history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs =1000)

# Step_7: Making some predictions

predictions = model.predict(X_test_scaled[:5])
print("Predicted values are: ", predictions)
print("Real values are: ", y_test[:5])


# Step_8: Plotting the loss and accuracy

from matplotlib import pyplot as plt
#plot the training and validation accuracy and loss at each epoch
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'y', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
          
  
acc = history.history['mae']
val_acc = history.history['val_mae']
plt.plot(epochs, acc, 'y', label='Training MAE')
plt.plot(epochs, val_acc, 'r', label='Validation MAE')
plt.title('Training and validation MAE')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()          
