# Doctrine :

## Mots-clés
- **Entity :** représente des tables 
- **Manager :** Insertion/Maj/Suppression d'une ligne de la bdd
- **Repository :** Selection d'une ligne de la bdd

## Configuration


### Configuration de la database

- Commencer par modifier la **varible DATABASE_URL** dans fichier ***.env***

```
DATABASE_URL=mysql://user:password@127.0.0.1:3306/Blog
```

- Configuration de la database Blog

```shell
> php bin/console doctrine:database:create
```

### Configuration de la table

- Configuration de l'entity (table) Article
    
```shell
> php bin/console make:entity
```

- Il nous demande ensuite le nom de l'entity  : 
```shell
Class name of the entity to create or update (e.g. VitoriousGname) :
> Article
```

- Il nous demande ensuite le nom et type des colonnes de l'entity Article : 

```shell
New property name (press <return> to stop addigs fields) :
> title

Field type (enter ? to see all types) [string] :
> <Enter>

Field length [255]:
> <Enter>

Can this field be null in the database (nullable) (yes/no) [no]
> <Enter>

Add another property? Enter the property name (or press <return> to stop adding fields)
> createdAt
Field type (enter ? to see all types) [datetime] :
> <Enter>
```

Après la fin la commande ``php bin/console make:entity``, il crée des getters et setters de notre table dans le fichier ***"./src/Entity/<TABLE_NAME>.php"***

### Création de notre database et table

- Analyser la bdd et vérifier les differences (si la table existe déja sur la bdd par exemple) avec la commande :

```shell
php bin/console make:migration

```

Si la commande se déroule bien alors il va nous créer nos lignes SQL dans le fichier ***"./src/Migration/version.php"***

- On peut ainsi éxécuter nos lignes SQL générées par symfony avec à la commande suivante :

```shell
php bin/console doctrine:migrations:migrate
```

### Simuler des volumes de données


- **Les fixtures:** permettent de charger un "faux" jeu de données dans une base de données pouvant être utilisée pour tester nos données.
- **Faker :** Créer des données fakes (https://github.com/fzaninotto/Faker)

- Création de notre fixtures :

```shell
php bin/console make:fixtures
> ArticleFixtures
```

Il va alors nous créer un fichier dans ***"./src/DataFixtures/ArticleFixtures.php"*** qui ressemble à ça 

```php
// src/DataFixtures/AppFixtures.php
namespace App\DataFixtures;

use App\Entity\;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Common\Persistence\ObjectManager;

use App\Entity\Article; // A IMPORTER

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager)
    {
        // On configure dans quelles langues nous voulons nos données
        $faker = Faker\Factory::create('fr_FR');
        
        // create 20 s! Bam!
        for ($i = 0; $i < 20; $i++) {
            $article = new Article(); // instanciation  de notre entity Article
            $article->setTitle($faker->title); // rajouter le nom à l'entity Article
                    ->setContent($faker->text($maxNbChars = 200)) // rajouter le contenu à l'entity Article
                    ->setImage($faker->imageUrl($width = 640, $height = 480)) // rajouter un lien d'image à l'entity Article
                    ->setCreatedAt(new \Datetime()); // le "\" permet de dire à symfony que la classe Datetime appartient au namespace global de php
            
            $manager->persist($article); //ici les données sont prêtes à être exportées
        }

        $manager->flush(); //ici les données sont prêtes à être envoyées à la bdd
    }
}
```

- Envoyer nos données à notre database (**ATTENTION CA SUPPRIMME LES ANCIENNES DONNEES**) :

```shell
php bin/console doctrine:fixtures:load
```

### Exploitation des données:

- Notre Controller BlogController :

```php
// src/DataFixtures/AppFixtures.php
namespace App\DataFixtures;

use App\Entity\;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Common\Persistence\ObjectManager;

use App\Entity\Article; // A IMPORTER
use App\Repository\ArticleRepository; // A IMPORTER


class BlogController extends Controller
{
    /**
    * @Route("/blog", name="blog")
    */
    public function index(ArticleRepository $repo)
    {
        /* $repo = $this->getDoctrine()->getRepository(Article::class); 
            c'est une autre façon d'importer le repo de l'entity Article
        */

         $article = $repo->find(
             12); //trouve moi l'article avec l'id 12
        
        $articles = $repo->findByTitle(
             'article 1'); //trouve moi tous les articles avec le titre article 1

        $article = $repo->findOneByTitle(
             'article 1'); //trouve moi un seul article avec le titre article 1 (prend le 1er)
        
        $articles= $repo->findAll(); //tous les articles

        return $this->render('blog/index.html.twig',[
            'articles' => $articles;
        ])
    }


    /**
    * @Route("/article/{id}", name="blog_show")
    */
    public function show(ArticleRepository $repo, $id){
        $article = $repo->find($id);
        return $this->render('blog/index.html.twig',[
            'article' => $article;
        ])
    }

    /* AUTRE FACON DE RECUPERER L'ARTICLE (Symfony saura seul comment récupérer l'article)
    /**
    * @Route("/blog/{id}", name="blog_show")
    */
    public function show(Article $article){
        return $this->render('blog/index.html.twig',[
            'article' => $article;
        ])
    }

}
```


- Notre twig pour afficher tous les articles récupérées depuis la bdd

```html
{% for article in articles %}
<article>
    <h2> {{ article.title }} </h2>
    <i>{{ article.createdAt | date('d/m/Y') }} à {{ article.createdAt | date('H:i') }}</i> <!-- on pipe l'output avec un filter -->
    <p>{{ article.content }}</p>
    <a href="{{ path('blog_show', {'id': article.id}) }}" class="btn btn-primary"> <!-- récupération by id (voir la fonction show() -->
        Lire la suite
    </a>
</article>

{% endfor %}
```
