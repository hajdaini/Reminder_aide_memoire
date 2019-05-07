# Base

- **Constante :**

  ```js
  const PI = 3.14159265
  ```

- **Variable :**

  ```js
  let name = "Hatim"
  ```

- **Condition :**

  ```js
  else if et non elif
  ```

- **concaténation:**

  ```js
  console.log(`My variable : ${ma_var} | maths` + " ou  cette   variable : " + autre_var)
  ```

- **== vs ===**

  ```js
  console.log(1 == '1') // true
  console.log(1 === '1') // false
  ```

# Foreach

```js
let names = ['Hatim', 'Alex', 'Hamza', 'Mathilde']

names.forEach(function(value, index)
{
    console.log(value)
})
```

# Fonction

```js
// fonction dans une variable
let test = function (name="Hamza") {
    console.log(name)
}

//fonction seule
function name(){
    // qlq chose
}

// arrow fonction peut tenir sur 1 seule ligne
let getName = (name) => "Your name is " + name
```

# Les objets

On peut mettre toutes sortes de variables dans un objet

```js
let Player = {
    name: 'Kore',
    life: 200,
    being_attacked : function (adversary_attack)
    {
        this.life -= adversary_attack
        console.log(`${this.name} life : ${this.life}`)
    }
}

Player.being_attacked(50)
```

# Les Maps

```
let john = {
    name: "John",
    age: 25,
    email: "john@gmail.com",
    phone: "06 25 25 25"
}

let david = {
    name: "David",
    age: 30,
    email: "david@gmail.com",
    phone: "06 12 12 12"
}

let users = new Map()

users.set("john", john)
users.set("david", david)

console.log(users.get("john") + "\n")
```

# Les classes et héritages :

```js
class Player{

    constructor(name, posX, posY){
        this.name = name
        this.posX = posX
        this.posY = posY
    }

    description() {
        console.log("My name is " + this.name + ` and my position is (${this.posX},${this.posY})`)
    }

}

class Mage extends Player{
    constructor(name, posX, posY, attack){
        super(name, posX, posY)
        this.attack = attack
    }
}

const mage = new Mage("Medusa", 300, 50, 100)
mage.description()
```
