import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

df_space = pd.read_csv('space.csv', delimiter = ';')

missoes = df_space[df_space["Company Name"] == "Roscosmos"]

status = missoes["Status Mission"].value_counts()

plt.pie(status, labels=status.index, autopct = '%1.1f%%', colors = ['green', 'red'])

plt.title("Missoes da Roscosmos (% Sucesso e Falha)")
plt.tight_layout()

plt.show()