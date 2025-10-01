import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

df_space = pd.read_csv('space.csv', delimiter = ';')

emp_china = df_space[df_space['Location'].str.contains('China')]['Company Name'].drop_duplicates()
emp_eua = df_space[df_space['Location'].str.contains('USA')]['Company Name'].drop_duplicates()

num_emp = {
    'China': len(emp_china),
    'EUA': len(emp_eua)
}

plt.bar(num_emp.keys(), num_emp.values(), color = ['red', 'blue'])

plt.title('Numero de Empresas Espaciais (EUA e China)')
plt.xlabel('Pais')
plt.ylabel('Quantidade de Empresas')
plt.grid(axis='y')
plt.tight_layout()

plt.show()