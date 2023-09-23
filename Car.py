import pandas as pd

# Create a DataFrame with the provided data
data = {
    'CarBrand': ['Toyota', 'Ford', 'Honda', 'Toyota', 'Honda'],
    'CarModel': ['Camry', 'F-150', 'Accord', 'Corolla', 'Civic'],
    'CarYear': [2015, 2018, 2017, 2016, 2019],
    'Mileage': [45000, 55000, 60000, 42000, 70000],
    'NextMaintenance': ['Oil Change', 'Tire Rotation', 'Brake Replacement', 'Oil Change', 'Tire Rotation']
}

df = pd.DataFrame(data)
df = pd.read_csv('predictive_maintenance_dataset.csv')
print(df.head())
# Define features and target variable
features = ['CarBrand', 'CarModel', 'CarYear', 'Mileage']
target = 'NextMaintenance'


new_data = {
    'CarBrand_Toyota': [1],  # One-hot encoded columns for 'Toyota' brand
    'CarBrand_Ford': [0],    # One-hot encoded columns for 'Ford' brand
    'CarBrand_Honda': [0],   # One-hot encoded columns for 'Honda' brand
    'CarModel_Camry': [1],   # One-hot encoded columns for 'Camry' model
    'CarModel_F-150': [0],   # One-hot encoded columns for 'F-150' model
    'CarModel_Accord': [0],  # One-hot encoded columns for 'Accord' model
    'CarYear': [2015],
    'Mileage': [52000]
}

# Create a DataFrame for the new data
new_data_df = pd.DataFrame(new_data)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ... Code to load and preprocess data ...

# Train a model
model = LinearRegression()
#model.fit(X_train, y_train)

# Make a prediction
#prediction = model.predict(X_test)

# Print the prediction
print(f"Predicted Next Maintenance Event: {[0]}")

