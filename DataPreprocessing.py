import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the updated CSV file
df = pd.read_csv('merged.csv')

# One-hot encode the categorical columns: Type, City, and Area
df = pd.get_dummies(df, columns=['Type', 'City', 'Area'], drop_first=False)

# Separate features and target
X = df.drop(columns=['Price'])
y = df['Price']

# Normalize numeric columns
scaler = StandardScaler()
X[['Area_sqft', 'Bedrooms', 'Bathrooms']] = scaler.fit_transform(X[['Area_sqft', 'Bedrooms', 'Bathrooms']])

# Merge the final data
final_df = pd.concat([X, y], axis=1)

# Save to CSV
final_df.to_csv('merged_preprocessed.csv', index=False)

print(" Preprocessing complete! File saved as 'merged_preprocessed.csv'")
