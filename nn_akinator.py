# -*- coding: utf-8 -*-
"""NN_Akinator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ycnoyPB0a7RiVS1p2Ras9o4CMigV_KSW
"""

import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

"""**We read the files**"""

# Load the CSV file
file_path ='DiseaseAndSymptoms.csv'
data = pd.read_csv(file_path)

"""**We look the file format**"""

print(data)

"""**We give the right format**



"""

# We identify all unique symptoms across the dataset
symptoms = pd.Series(data.iloc[:, 1:].values.ravel()).dropna().unique()

print(symptoms)
print(len(symptoms))

#We create a binary matrix for the symptoms
symptoms_matrix = pd.DataFrame(0, index=data.index, columns=symptoms)

#We populate the matrix with 1 where a symptom is present for a disease
for i, row in data.iterrows():
    present_symptoms = row[1:].dropna()
    symptoms_matrix.loc[i, present_symptoms] = 1

# We add the Disease column to the binary matrix
organized_data = pd.concat([data['Disease'], symptoms_matrix], axis=1)

"""**We look the new file format**"""

print(organized_data)

# Save the organized data to a new CSV file
organized_data.to_csv('organized_disease_symptoms.csv', index=False)

print("The dataset has been organized and saved to 'organized_disease_symptoms.csv'.")

print(organized_data.shape)

"""**Data Preprocessing**"""

# Get the list of symptoms (all columns except 'Disease')
symptoms = organized_data.columns[1:]

print(symptoms)

# Encode the 'Disease' column into numeric labels
label_encoder = LabelEncoder()

organized_data_encoded = organized_data.copy()
organized_data_encoded['Disease'] = label_encoder.fit_transform(organized_data['Disease'])

"""**We can recover the encoded data with**"""

lable_encoded0=15
predicted_disease = label_encoder.inverse_transform([lable_encoded0])[0]
print(predicted_disease )

print(organized_data_encoded['Disease'])

#We look for the number of non repeated total Disease
max(organized_data_encoded['Disease'].values)

# Separate features and labels
X = organized_data_encoded[symptoms].values
y = organized_data_encoded['Disease'].values

# We split the data into training+validation (90%) and testing (10%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9, shuffle=True, random_state=1)

"""**We build the neural network**"""

# We define the architecture
model = Sequential([
    Dense(10, input_shape=(X.shape[1],), activation='relu'),  # Input layer + hidden layer 1
    Dense(10, activation='relu'),                             # Hidden layer 2
    Dense(len(label_encoder.classes_), activation='softmax')  # Output layer
])

"""**Compile the and train the model**"""

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=2, validation_split=1-0.1/0.9)

"""**Evaluate the Model**"""

#We evaluate the Model using the validation set
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")

"""**We save the emulator**"""

model.save('Emulator_Disease.keras')