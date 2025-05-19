import pandas as pd
import matplotlib as plt
# import data
data= pd.read_csv ("C:/Users/Nikita/OneDrive/Desktop/borsa_italia/listino_catalog_kaggle.csv")
#data inspaction 
print('data shape',data.shape)
print("\nfirst 5 row :")
print(data.head())
print("\nColumns:", data.columns.tolist())
print("\nData types:\n", data.dtypes)
#clean data 
data.replace("na", pd.NA, inplace=True)  
data.replace("missing",pd.NA,inplace= True)

# Convert Y/N columns to boolean
yn_columns = ['detailspresent', 'withinstudy', 'covidstudy', 'UsedForENG']
for col in yn_columns:
    data[col] = data[col].map({'Y': True, 'N': False})

#market distubution 
market_dist =data['market'].value_counts()
print("\nMarket Distribution:\n", market_dist)

# 2.Industry analysis
industry_dist = data['industry'].value_counts()
print("\nindustry analysis N top :\n",industry_dist)

#3  COVID study participation
covid_study = data['covidstudy'].value_counts(dropna=False)
print("\nCOVID Study Participation:\n", covid_study)

# 4. Accounts availability comparison
accounts_comparison = pd.DataFrame({
    '2019': data['2019accounts'].notna().value_counts(),
    '2021': data['2021accounts'].notna().value_counts()
})
print("\nAccounts Availability:\n", accounts_comparison)

# visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10)) 

# Market Distribution
plt.figure(figsize=(4, 4))
market_dist.plot(kind='bar', title='Market Distribution')
plt.xticks(rotation=45)
plt.xlabel("Market")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--')
plt.show()

# Industry Distribution
plt.figure(figsize=(10, 6))
industry_dist.plot(kind='pie', autopct='%1.1f%%', title='Top Industries')
plt.ylabel("")  # Hide y-label to make it cleaner
plt.show()

# COVID Study Participation
plt.figure(figsize=(10, 6))
covid_study.plot(kind='bar', title='COVID Study Participation')
plt.xticks(ticks=[0, 1, 2], labels=['No', 'Yes', 'Unknown'], rotation=0)
plt.xlabel("COVID Study Participation")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--')
plt.show()

# Financial Accounts Availability
plt.figure(figsize=(10, 6))
accounts_comparison.plot(kind='bar', title='Financial Accounts Availability')
plt.xticks(ticks=[0, 1], labels=['Missing', 'Available'], rotation=0)
plt.xlabel("Availability")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--')
plt.show()

# Advanced analysis: Market vs Industry
cross_tab = pd.crosstab(data['market'], data['industry'])
print("\nMarket vs Industry Cross-Tabulation:\n", cross_tab)

# Save cleaned data
data.to_csv('cleaned_financial_data.csv', index=False)