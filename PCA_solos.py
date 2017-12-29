# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:43:37 2017

@author: matto
"""

from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn

#importa a tabela de dados
df = read_csv(r'C:\Jac\Mestrado\Projeto\Campo\solo_selecionadas.csv')
df.head()

#define uma função para normalizar os dados
def z_score(x):
    """Remove a média e normaliza os pelo desvio padrão"""
    return (x - x.mean()) / x.std()

#importa a função do PCA
from sklearn.decomposition import PCA

#roda o PCA
pca = PCA(n_components=None)
pca.fit(df.apply(z_score).T)

from pandas import DataFrame

#coloca os scores do PCA em um dataframe
loadings = DataFrame(pca.components_.T)
loadings.index = ['PC %s' % pc for pc in loadings.index + 1]
loadings.columns = ['TS %s' % pc for pc in loadings.columns + 1]
loadings

PCs = np.dot(loadings.values.T, df)


#Roda o gráfico de barras com o quanto de variação é explicada por cada eixo
perc = pca.explained_variance_ratio_ * 100

perc = DataFrame(perc, columns=['Percentage explained ratio'], index=['PC %s' % pc for pc in np.arange(len(perc)) + 1])
ax = perc.plot(kind='bar')


#Plotando apenas a primeira dimensão
marker = dict(linestyle='none', marker='o', markersize=7, color='blue', alpha=0.5)

fig, ax = plt.subplots(figsize=(7, 2.75))
ax.plot(PCs[0], np.zeros_like(PCs[0]),
        label="Scores", **marker)
[ax.text(x, y, t) for x, y, t in zip(PCs[0], loadings.values[1, :], df.columns)]

ax.set_xlabel("PC1")

_ = ax.set_ylim(-1, 1)
marker = dict(linestyle='none', marker='o', markersize=7, color='blue', alpha=0.5)

#Apenas a segunda
marker = dict(linestyle='none', marker='o', markersize=7, color='blue', alpha=0.5)

fig, ax = plt.subplots(figsize=(7, 2.75))
ax.plot(PCs[0], np.zeros_like(PCs[0]),
        label="Scores", **marker)
[ax.text(x, y, t) for x, y, t in zip(PCs[0], loadings.values[1, :], df.columns)]

ax.set_xlabel("PC2")

_ = ax.set_ylim(-1, 1)
marker = dict(linestyle='none', marker='o', markersize=7, color='blue', alpha=0.5)

#grafico de barras
ax = seaborn.corrplot(df, annot=True, diag_names=False)


#Dois eixos juntos
fig, ax = plt.subplots(figsize=(10, 7.75))
ax.plot(PCs[0], PCs[1], label="Scores", **marker)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")


text = [ax.text(x, y, t) for x, y, t in
        zip(PCs[0], PCs[1]+0.5, df.columns)]

#loadings TS1
TS1 = loadings['TS 1']
TS1.index = df.index
ax = TS1.plot(kind='bar')
loadings


#PCA loading plot
marker = dict(linestyle='none', marker='o', markersize=7, color='blue', alpha=0.5)

fig, ax = plt.subplots(figsize=(10, 7.75))

ax.plot(loadings.icol(0), loadings.icol(1), label="Loadings", **marker)
ax.set_xlabel("non-projected PC1")
ax.set_ylabel("non-projected PC2")
ax.axis([-10, 10, -10, 10])
text = [ax.text(x, y, t) for
        x, y, t in zip(loadings.icol(0), loadings.icol(1), df.index)]







