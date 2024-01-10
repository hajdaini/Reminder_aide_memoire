# Documentation Numpy

## Qu'est-ce que NumPy?

NumPy est l'abréviation de "Numeric Python". C'est une bibliothèque numérique open source utilisée pour travailler avec des fonctions mathématiques, des tableaux multidimensionnels et des structures de données matricielles. Elle est largement utilisée en science des données et en apprentissage machine.

## Pourquoi Utiliser NumPy?

Bien que Python dispose d'une structure de liste intégrée, NumPy offre des avantages significatifs :

- Utilisation plus efficace de la mémoire.
- Lecture plus rapide des informations.
- Opérations pratiques de diffusion à travers les dimensions du tableau.

Apprendre NumPy sera essentiel pour exploiter les capacités avancées de bibliothèques telles que TensorFlow, que nous aborderons plus tard dans le cours.

Dans les prochaines vidéos, nous explorerons concrètement l'utilisation de tableaux et matrices avec NumPy. Préparez-vous pour une plongée approfondie!



## Génération d'Array avec NumPy

Génère un tableau d'éléments espacés régulièrement dans l'intervalle (tart, stop) avec un pas donné.

```python
print(f"Génération d'array: \n{np.arange(0, 10, 2)}")
"""
res:
[0 2 4 6 8]
""" 
```
Génère des tableaux remplis de zéros (`np.zeros`) ou de uns (`np.ones`) avec la forme spécifiée par le tuple `shape`.

```python
print(f"Génération d'array de zéros: \n{np.zeros((3, 4))}")
print(f"Génération d'array de uns: \n{np.ones((3, 4))}")
"""
res:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
--------------------
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
""" 
```

Génère un tableau de valeurs espacées linéairement sur un intervalle donné, avec un nombre spécifié de points.

```python
print(f"Génération d'array par valeur fixe: \n{np.linspace(0, 10, 4)}")
"""
res:
[ 0. 3.33333333  6.66666667 10.]
""" 
```

Génère une matrice identité de taille NxN.

```python
print(f"Génération de valeurs diagonales: \n{np.eye(5)}")
"""
res:
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
""" 
```

Génère des tableaux d'éléments aléatoires selon une distribution uniforme (`np.random.rand`) ou normale (`np.random.randn`) avec la forme spécifiée par le tuple `shape`.

```python
print(f"Génération d'array random: \n{np.random.rand(2)}")
print(f"Génération d'array random: \n{np.random.rand(3, 4)}")
print(f"Génération d'array random avec des valeurs négatives: \n{np.random.randn(3, 4)}")
"""
res:
[0.45059634 0.05360731]
--------------------
[[0.93384785 0.87763203 0.33059751 0.11879557]
 [0.42968456 0.34027911 0.40980841 0.55675974]
 [0.09872075 0.56869833 0.38390584 0.4618371 ]]
--------------------
[[ 0.53700519  2.66559706  1.03853079  0.42166115]
 [ 0.28333433  0.04241445 -0.09366026  0.01569945]
 [ 0.4530168   0.4205186  -0.07941142  0.46813533]]
""" 
```

Génère un tableau d'entiers aléatoires dans l'intervalle (low, high) avec la forme spécifiée par le tuple `size`.

```python
print(f"Génération d'array random integers avec valeurs fix: \n{np.random.randint(1, 100, 10)}")
"""
res:
[11 17 78 66 21 89 77 95 39 72]
""" 

```
Pour obtenir des résultats reproductibles sur différents appareils, il est possible de définir une graine (seed) pour le générateur de nombres aléatoires de NumPy.

```python
# Définition d'un seed
np.random.seed(42)
print(np.random.rand(4))
"""
res:
[0.37454012 0.95071431 0.73199394 0.59865848]
""" 
```

L'utilisation de np.random.seed garantit que les mêmes nombres aléatoires seront générés chaque fois que le code est exécuté avec le même seed.

np.reshape(array, newshape)

Remodèle un tableau sans changer ses données.

```python
# Définition d'un seed
arr = np.arange(12)
reshaped_arr = np.reshape(arr, (3, 4))
print(f"Tableau remodelé: \n{reshaped_arr}")
"""
res:
[ 0  1  2  3  4  5  6  7  8  9 10 11]
--------------------
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
""" 
```

**Fonctions pour Trouver les Valeurs Minimales et Maximales dans un Array**

Retourne la valeur maximale dans l'array `ranarr`:

```python
max_value = ranarr.max()
print(f"Valeur maximale dans ranarr: {max_value}")
res:
9
```

Retourne la valeur minimale dans l'array `ranarr`:

```python
min_value = ranarr.min()
print(f"Valeur minimale dans ranarr: {min_value}")
res:
1
```
Retourne l'indice de la première occurrence de la valeur maximale dans l'array.


```python
index_of_max = np.argmax(ranarr)
print(f"Indice de la valeur maximale dans ranarr: {index_of_max}")
res:
4
```

Retourne l'indice de la première occurrence de la valeur minimale dans l'array.

```python
index_of_min = np.argmin(ranarr)
print(f"Indice de la valeur minimale dans ranarr: {index_of_min}")
res:
0
```
