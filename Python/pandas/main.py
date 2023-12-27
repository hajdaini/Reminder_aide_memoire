import pandas as pd

# Créer un DataFrame d'exemple
data = {'Sector': ['Private for-profit, 2-year', 'Private for-profit, less-than 2-year', 'Private for-profit, less-than 2-year', 'Private for-profit, less-than 2-year', 'Public, 4-year or above'],
        'University': ['Pima Medical Institute-Las Vegas', 'Healthcare Preparatory Institute', 'Milan Institute-Las Vegas', 'Utah College of Massage Therapy-Vegas', 'Western Nevada College'],
        'Year': [2016, 2016, 2016, 2016, 2016],
        'Completions': [591, 28, 408, 240, 960],
        'Geography': ['Nevada', 'Nevada', 'Nevada', 'Nevada', 'Nevada']}

df = pd.DataFrame(data)

# Utiliser groupby pour regrouper par année et sum pour obtenir la somme des complétions
sum_by_year = df.groupby('Year')['Completions'].sum().reset_index()

# Utiliser set_index pour définir la colonne 'Year' comme index
sum_by_year = sum_by_year.set_index('Year')

print(sum_by_year)
