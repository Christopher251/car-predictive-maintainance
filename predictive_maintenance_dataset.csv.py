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


print(f"Predicted Next Maintenance Event: {prediction[0]}")
