import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load the breast cancer dataset
breast_cancer = load_breast_cancer()
X = breast_cancer.data  # Features
y = breast_cancer.target  # Labels (target classes)

# Display dataset information
print("Dataset Information:")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Feature names: {breast_cancer.feature_names}")
print(f"Target classes: {breast_cancer.target_names}")
print(f"Class distribution: {np.bincount(y)}\n")  # Shows how many samples per class

# Converting the breast cancer dataset to a DataFrame for better visualization
cancer_df = pd.DataFrame(data=np.c_[breast_cancer['data'], breast_cancer['target']],
                         columns=list(breast_cancer['feature_names']) + ['target'])

# Mapping target values to class names (0 -> malignant, 1 -> benign)
cancer_df['target'] = cancer_df['target'].map({0: 'malignant', 1: 'benign'})

# Display the first few rows of the dataset
display(cancer_df.head())

# Visualizing the data before classification (using first two features for 2D plot)
plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=100)
plt.title('Breast Cancer Dataset Visualization (Before Classification)')
plt.xlabel(breast_cancer.feature_names[0])  # Feature 1
plt.ylabel(breast_cancer.feature_names[1])  # Feature 2
colorbar = plt.colorbar(label='Classes')
colorbar.set_ticks([0, 1])
colorbar.set_ticklabels(breast_cancer.target_names)  # Adding class labels to colorbar
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Implementing k-Nearest Neighbors with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)  # Train the k-NN model on the training data

# Making predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, target_names=breast_cancer.target_names)

# Print accuracy and classification report
print(f"Accuracy of k-NN: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_rep)

# Visualizing the data after classification (using first two features for 2D plot)
plt.figure(figsize=(8,6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolor='k', s=100)
plt.title('Breast Cancer Dataset Classification Visualization (After Classification)')
plt.xlabel(breast_cancer.feature_names[0])  # Feature 1
plt.ylabel(breast_cancer.feature_names[1])  # Feature 2
colorbar = plt.colorbar(label='Predicted Classes')
colorbar.set_ticks([0, 1])
colorbar.set_ticklabels(breast_cancer.target_names)  # Adding class labels to colorbar
plt.show()
