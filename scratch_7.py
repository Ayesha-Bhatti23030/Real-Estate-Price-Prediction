
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

import pandas as pd
df=pd.read_csv('../merged_preprocessed.csv')
print(df)

import matplotlib.pyplot as plt
plt.scatter(df['Bedrooms'],df['Price'])
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.show()

# The columns 'Type', 'City', and 'Area' were one-hot encoded in a previous cell,
# so there is no need to map them here.
df.columns = df.columns.str.strip()


#print(df.dtypes)
#print("Missing values after mapping:")
#print(df[['Type', 'City']].isna().sum())

correlation=df.corr(numeric_only=True)
print(correlation['Price'])

plt.scatter(df['Area_sqft'],df['Price'])
plt.xlabel('Area_sqft')
plt.ylabel('Price')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
X=df[['Area_sqft','Bedrooms','Bathrooms','Type_Flat','Type_House',
      'Type_Plot'	,'Type_Shop','Type_Warehouse','City_Faisalabad','City_Gujranwala',
      'City_Hyderabad','City_Islamabad','City_Karachi','City_Lahore',
      'City_Multan','City_Peshawar','City_Quetta','City_Rawalpindi',
      'City_Sialkot',	'City_Sukkur','Area_Askari 11','Area_Bahria Town',
      'Area_Bosan Road','Area_Cantt','Area_Clifton','Area_D Ground','Area_DHA','Area_E11',
      'Area_F10','Area_F7','Area_F8','Area_FB Area','Area_Faisal Town','Area_G11',
      'Area_G13','Area_G14','Area_G6','Area_G7','Area_G8','Area_G9','Area_Garden Town',
      'Area_Gulberg','Area_Gulgasht','Area_Gulshan','Area_H13','Area_H9','Area_Hall Road',
      'Area_Hayatabad','Area_Hazar Ganji','Area_I8','Area_I9','Area_Jinnah Town','Area_Johar Town',
      'Area_Karkhano','Area_Khadim Ali Road','Area_Korangi','Area_Kutchery','Area_Latifabad','Area_Malir',
      'Area_Millat Town','Area_Minar Road','Area_Model Town','Area_Moon Market','Area_Nazimabad',
      'Area_New Multan','Area_New Sukkur','Area_North Nazimabad','Area_Phase 3',
      'Area_Qasimabad','Area_Raiwind','Area_SITE','Area_Saddar','Area_Saddar Bazaar',
      'Area_Samungli Road','Area_Satellitetown','Area_Sattelite Town','Area_Shah Rukn-e-Alam','Area_Sundar','Area_Wapda Town']]
y=df['Price']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
mse=mean_squared_error(y_test,y_pred)
print("Mean Squared Error:",mse)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

import numpy as np

errors = y_test - y_pred
print("Mean absolute error:", np.mean(abs(errors)))

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color='red', linewidth=2)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.show()

mae = 1630297.2230630661
avg_price = y_test.mean()

percent_error = (mae / avg_price) * 100
print("Mean Absolute Percentage Error:", percent_error, "%")

r2 = model.score(x_test, y_test)
print("R² Score:", r2)

