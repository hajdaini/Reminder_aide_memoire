# Acronyme

```
HW : Hardware
US : User Space
K  : Kernel
```

# NATIF

![natif](imgs/natif.jpg)

# EMULATION

![emulation](imgs/emulation.jpg)

**Avantages :**

- Emulation du hardward
- Plus simple aux devs d'avoir accès au noyau (debug/coder...)

**Inconvénients :**

- Perte de 50% de performances car on passe 2 fois par API+Kernel+HW

***Exemples de logiciels :***
- VirtualBox (sans Hardware)
- VirtualPC
- VMware (sans ESX)

# TRANSLATION

![translation](imgs/translation.jpg)

**Avantages :**

- Très peu de perte de performance ( ≈2% )
- On peut éxécuter des apps windows sur un Linux

***Exemples de logiciels :***

- Wine

# ISOLATION

![isolation](imgs/isolation.jpg)

**Avantages :**

- Très peu de perte de performance ( ≈1% )
- Conteneurs (Hardware)

***Exemples de logiciels :***

- VServer
- virtuozzo
- Jail

# HyperV Type1 (Hyperviseur)

![hyperv-type1](imgs/hyperv-type1.jpg)

**Avantages :**

- De très bonne performance par rapport à l'émulation ( ≈7% )

***Exemples de logiciels :***

- Xen
- VmWare (ESX)

# HyperV Type2 (Hyperviseur)

![hyperv-type2](imgs/hyperv-type2.jpg)

***Exemples de logiciels :***

- Kvm

# Conteneur

![conteneur](imgs/conteneur.jpg)


**Avantages :**

- Très peu de perte de performance ( ≈1% )

***Exemples de logiciels :***

- Docker
- Rocket
