### Créer une image :

```py 
Image.new(mode, size, color)
```

```textile
@mode :
    - 1 : monochrome ( 1 bit par pixel)
    - L : Grayscale ( 8 bits par pixel)
    - RGB : Couleur
    - RGBA : Couleur avec transparence

@size : tuple(width, height)

@color :
    - 'yellow' (caseSensitive)
    - #fffff
    - rgb(100, 200, 200)
    - hsl(100, 50%, 30%)
```

### Ouvrir une image :

```py 
Image.open('mon_image.jpg')
```

### Mélanger deux images : 

```py 
Image.blend(image1, image2, alpha)
```

**Prérequis :** même size et même mode !

```textile
@alpha :
    compris entre 0 à 1 (0 = 100% image1 et 1 = 100% image2)
```

### Transformer le mode d'une image :

```py 
image = Image.open('01.jpg')
image.convert(mode).show()
```

```textile
@mode : 
    - vu sur "Créer une image"
```

### Rogner une image :

```py 
image = Image.open('01.jpg')
image.crop( (x, y, width, height) ).show()
```

### Rajouter des filtres :

***Prérequis :*** from PIL import ImageFilter

```py 
image = Image.open('01.jpg')
image.filter(ImageFilter.LES_FILTRES).show()
```

### Supprimer une image de la mémoire : 

```py 
del variable_de_limage
```

### Variables : 

- Taille de l'image :

  ```py 
  image = Image.open('01.jpg')
  print(image.size)
  ```

- Mode de l'image :

  ```py 
  image = Image.open('01.jpg')
  print(image.mode)
  ```

### Connaître toutes les couleurs et leurs occurrences :

```py 
width, height = image.size
colors = image.getcolors(width * height)
```

```textile
@return (occurence, couleur)
```

### Connaître la couleur d'un pixel (pas opti si trop de pixels) :

```py 
image = Image.open('01.jpg')
print(image.getpixel((posX, posY)))
```

```textile
@return (couleur)
```

### Retourner la couleur de chaque pixel (plus opti) :

```py 
image = Image.open('01.jpg')
print(list(image.getdata()))
```

```textile
@return [couleur]
```

### Changer la couleur d'un pixel (pas opti si trop de pixels) :

```py 
image = Image.open('01.jpg')
print(image.putpixel((posX, posY), (color)))
```

```textile
@return (couleur)
```

### Changer les pixels d'une image (plus opti) :

```py 
image = Image.open('01.jpg')
pixels = image.load()  # create the pixel map
pixels[width, height] = (color)
```

### Sauvegarder une image :

```py 
image = Image.open('01.jpg')
image.save('filename')
```

### Modifier la taille d'une image :

- Garder le ratio de l'image :

  ```py 
  image = Image.open('01.jpg')        
  image.thumbnail((width, height))
  ```

- Ignorer du ratio de l'image :

  ```py 
  image = Image.open('01.jpg')    
  image.resize((width, height))
  ```

### Rotation d'une image :

```py 
image = Image.open('01.jpg')        
image.rotate(45)
```

***Exemple :*** 

```py
image = Image.open('test.jpg')
size = width, height = image.size
pixel_data = image.load()

for w in range(width):
    for y in range(height):
        pixel_data[x, y] = (255, 0, 255)

image.save() 
```
