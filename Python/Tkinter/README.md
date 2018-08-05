### Documentation Tkinter :
http://tkinter.fdex.eu/doc/uwm.html#update_idletasks

### Documentation externe : 
- Couleurs tkinter : https://www.tutorialspoint.com/python/tk_colors.htm
- combinaison de couleurs : https://coolors.co/browser/best/1
- tkinter text color : https://wiki.tcl.tk/37701
    
### Fenêtre de base :
```py
from tkinter import *

WIDTH = 500
HEIGHT = 500

def window_position(window, width, height):
    screen_width = int(window.winfo_screenwidth())
    screen_height = int(window.winfo_screenheight())
    window_width = width
    window_height = height
    window_x = (screen_width // 2) - (window_width // 2)
    window_y = (screen_height // 2) - (window_height // 2)
    return '{}x{}+{}+{}'.format(window_width, window_height, window_x, window_y)

window = Tk()
window.title('Hello world')
window.geometry(window_position(window, WIDTH, HEIGHT))


window.resizable(width=False, height=False)
window.mainloop()
```

# Widgets

### TEXT : 
```py
label = Label(window, text="hello", font='Arial 16')
label['text'] = 'change me'
print(label['text'])
```

### INPUT :
```py
input = Entry(window, font='Arial 12 normal italic', fg='gray')
input.insert(0, 'placeholder')
```

### BUTTON :
```py
button = Button(window, text='button welcome', font='Arial 12 normal', bg='#DC4C46', fg='white')
```

### CHECKBOX :
```py
checkbox = Checkbutton(window, text="Mineur ?", variable='checked', onvalue="1", offvalue="0")
```

### RADIOS :
    """
    -Les radios peuvent avoir seuelement un element check
    -@value = peut être n'importe quoi tant ça reste la même chose pour 
            les elements non check et unique sur l'element check
    """
```py
radio1 = Radiobutton(window, text="Grand ?", value='unique')
radio2 = Radiobutton(window, text="Petit ?",  value='autrevaleur')

### SCALE (sorte de scroll) :
```py
scale = Scale(window, orient='horizontal', from_=0, to=10, resolution=0.1, tickinterval=2, length=350, label='Volume (db)')
```

### Spinbox :
```py
from tkinter import StringVar
spinbox = Spinbox(window, from_=0, to=100)
```

### DROPDOWN MENU
```py
from tkinter import StringVar
variable = StringVar(window)
variable.set("one") # default value
w = OptionMenu(window, variable, "one", "two", "three")

### AFFICHAGE DES WIDGETS : equivalent d'une div en html :
```py
input.pack()
```

### MESSAGE BOX :
```py
from tkinter import messagebox

def message_test():
    #messagebox.showerror('Titre Erreur', 'Erreur')
    #messagebox.showwarning('Titre Attention', 'Attention)
    #messagebox.showinfo('Titre info', 'information')
    #messagebox.askquestion('Titre', 'es tu beau ?')
    messagebox.askyesnocancel('Sauvegarde', 'Es tu sur de vouloir quitter sans sauvegarder ?')

but = Button(window, text='ERREUR', command=message_test)
but.pack()
```

### EVENTS :
```py
def key(event):
    print("pressed {}".format(event.char))

def callback(event):
    print("clicked at", event.x, event.y)

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
window.bind('<Left>', leftKey)
window.bind('<Right>', rightKey)
window.bind("<Key>", key)
window.bind("<Button-1>", callback)
```

### Canvas :
```py
def center(LARGEUR):
    return (WIDTH/2 -LARGEUR), (HEIGHT/2 - LARGEUR), (WIDTH/2+LARGEUR), (HEIGHT/2+LARGEUR)

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
canvas.create_line(0, WIDTH, HEIGHT, 0, fill="red", width=1)
canvas.create_oval(center(100), fill="white", width=1, outline='black')
canvas.create_rectangle(center(50), fill="red", width=1, outline='black')
canvas.pack()
```

#Animation
```py
ball = canvas.create_oval(center(10), fill='orange')
speedx = 1
speedy = 1
while True:
    time.sleep(0.005)
    canvas.move(ball,speedx,speedy)
    window.update()
    playerX0, playerY0, playerX1, playerY1 = canvas.coords(ball)
    if  playerX0 <= 0 or playerX1 >= WIDTH:
        speedx = -speedx
    if  playerY0 <= 0 or playerY1 >= HEIGHT:
        speedy = -speedy
```
