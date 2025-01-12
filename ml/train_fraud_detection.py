
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Generate synthetic financial transaction data
def generate_transaction_data():
    np.random.seed(42)
    data = {
        "transaction_id": np.arange(1, 10001),
        "user_id": np.random.randint(1, 1001, size=10000),
        "amount": np.random.uniform(10.0, 1000.0, size=10000),
        "currency": np.random.choice(["USD", "EUR", "JPY", "GBP"], size=10000),
        "is_fraud": np.random.choice([0, 1], size=10000, p=[0.98, 0.02])
    }
    return pd.DataFrame(data)

# Save the generated data to a file
data = generate_transaction_data()
data.to_csv("transactions.csv", index=False)

# Preprocess the transaction data
def preprocess_data(data):
    data = pd.get_dummies(data, columns=["currency"], drop_first=True)
    X = data.drop(columns=["transaction_id", "user_id", "is_fraud"])
    y = data["is_fraud"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y

X, y = preprocess_data(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train a neural network for fraud detection
model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.2),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, validation_split=0.2, epochs=10, batch_size=32, verbose=2)

# Save the trained model for deployment
model.save("fraud_detection_model")
