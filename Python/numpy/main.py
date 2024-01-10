# Plus rapide et consomme moins de mémoire qu'une liste python

import numpy as np

# start (inclus), stop (non inclus), step (default = 1)
print(f"Génération d'array: \n{np.arange(0, 10, 2)}")

# rows, columns
print(f"Génération d'array de zero: \n{np.zeros((3, 4))}")
print(f"Génération d'array de zero: \n{np.ones((3, 4))}")

# start (inclus), stop (non inclus), num voulu (incluant la valeur stop)
print(f"Génération d'array par valeur fixe: \n{np.linspace(0, 10, 4)}")

# rows, columns
print(f"Génération d'array random: \n{np.random.rand(2)}")
print(f"Génération d'array random: \n{np.random.rand(3, 4)}")
print(f"Génération d'array random avec des valeurs négatives: \n{np.random.randn(3, 4)}")

# start (inclus), stop (non inclus), num
print(f"Génération d'array random integers avec valeurs fix: \n{np.random.randint(1, 100, 10)}")

# définitions d'un seed pour avoir le meme random sur n'importe quel appareil utilisant le meme seed que moi
np.random.seed(42)
print(np.random.rand(4)) 

