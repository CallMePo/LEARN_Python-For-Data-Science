import pandas as pd

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
print(df.head())

Keluarga={'Istri':['Sesa','Shadim','Shafaa'], 'Suami':['Khokho','Ahul','KhomKhom'],'Kids':['Zacrown','Zoel','Zlatan']}
Keluarga_Happy=pd.DataFrame(Keluarga)
print(Keluarga_Happy.head())

x=Keluarga_Happy[['Suami','Istri']]
print(x)

#z=Keluarga_Happy.ix[0:1]
#print(z)

print(Keluarga_Happy['Istri'].unique()) #for numbers only
print(Keluarga_Happy['Kids']>='Zoel')