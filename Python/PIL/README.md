"""
Créer une image : 
    Image.new(mode, size, ?color)
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
    
Ouvrir une image : 
    Image.open('mon_image.jpg')

Mélangeer deux images : 
    Image.blend(image1, image2, alpha)
    Prérequis : même size et même mode !
    @alpha :
        compris entre 0 à 1 (0 = 100% image1 et 1 = 100% image2)

Transformer le mode d'une image :
    image = Image.open('01.jpg')
    image.convert(mode).show()
    @mode : 
        - vu sur "Créer une image"

Rogner une image :
    image = Image.open('01.jpg')
    image.crop( (x, y, width, height) ).show()

Rajouter des filtres : 
    Prérequis : from PIL import ImageFilter
    image = Image.open('01.jpg')
    image.filter(ImageFilter.LES_FILTRES).show()
    
Supprimer une image de la mémoire : 
    del variable_de_limage

Variables : 
    Taille de l'image :
        image = Image.open('01.jpg')
        print(image.size)
    Mode de l'image :
        image = Image.open('01.jpg')
        print(image.mode)

Connaitre toutes les couleurs et leur occurences
    width, height = image.size
    colors = image.getcolors(width * height)
    @return (occurence, couleur)

Retourner la couleur de chaque pixel (méthode rapide)
    image = Image.open('01.jpg')
    print(list(image.getdata()))
    @return [couleur]


Connaitre la couleur d'un pixel (pas opti si trop de pixels):
    image = Image.open('01.jpg')
    print(image.getpixel((posX, posY)))
    @return (couleur)

Changer la couleur d'un pixel (pas opti si trop de pixels):
    image = Image.open('01.jpg')
    print(image.putpixel((posX, posY), (color)))
    @return (couleur)

Changer les pixels d'une image (Plus opti):
    image = Image.open('01.jpg')
    pixels = image.load()  # create the pixel map
    pixels[width, height] = (color)

Sauvegarder une image :
    image = Image.open('01.jpg')
    image.save('filename')
"""

"""
Modifier la taille d'une image:
    Garder le ratio de l'image:
        image = Image.open('01.jpg')        
        image.thumbnail((width, height))
    Osef du ratio de l'image:
        image = Image.open('01.jpg')    
        image.resize((width, height))

Rotation d'une image :
    image = Image.open('01.jpg')        
    image.rotate(45)
"""


image = Image.open('test.jpg')
size = width, height = image.size
pixel_data = image.load()

for w in range(width):
    for y in range(height):
        pixel_data[x, y] = (255, 0, 255)

image.save() 