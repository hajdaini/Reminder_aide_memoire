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

**la database n'est pas encore crée** pour la créer il faut :

Il faut analyser la bdd et vérifier les differences (si la table existe sur la bdd par exemple) avec la commande :

```shell
php bin/console make:migration

```
et cree donc un fichier dans  de migration ***"./src/Migration/version.php"*** ou on peut trouver le la requette qu'il va éxécuter

on peut éxécuter notre code SQL généré par symfony avec à la commande suivate :

```shell
php bin/console doctrine:migrations:migrate
```


Pour simuler des volumes de donnees :

```shell
php bin/console make:fixtures
> ArticleFixtures
```

Il crée alors un fichier dans ***"./src/DataFixtures/ArticleFixtures.php"***

le fichier ArticleFixtures.php ressemble à ça :

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
        // create 20 s! Bam!
        for ($i = 0; $i < 20; $i++) {
            $article = new Article();
            $article->setTitle('Article '.$i);
                    ->setContent("Contenu de l'article ".$i)
                    ->setImage("http://placehold.it/35x150")
                    ->setCreatedAt(new \Datetime()); // le "\" permet de dire que la classe Datetime appartient au namespace global de php
            
            $manager->persist($article); //ici les données sont prêtes à être exportées
        }

        $manager->flush(); //ici les données sont prêtes à être envoyées à la bdd
    }
}
```

et on tape la commande suivante pour envoyer nos données (**ATTENTION CA SUPPRIMME LES ANCIENNES DONNEES** :

```shell
php bin/console doctrine:fixtures:load
```

## Exploitation des données:


```php
// src/DataFixtures/AppFixtures.php
namespace App\DataFixtures;

use App\Entity\;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Common\Persistence\ObjectManager;

use App\Entity\Article; // A IMPORTER

class BlogController extends Controller
{
    /**
    * @Route("/blog", name="blog")
    */
    public function index()
    {
        $repo = $this->getDoctrine()->getRepository(Article::class);

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
    public function show($id){
        $repo = $this->getDoctrine()->getRepository(Article::class);
        $article = $repo->find($id);
        return $this->render('blog/index.html.twig',[
            'article' => $article;
        ])
    }

}
```


Dans mon twig pour récupérer les articles :

```html
{% for article in articles %}
<article>
    <h2> {{ article.title }} </h2>
    <i>{{ article.createdAt | date('d/m/Y') }} à {{ article.createdAt | date('H:i') }}</i> <!-- pipe l'output avec un filter -->
    <p>{{ article.content }}</p>
    <a href="{{ path('blog_show', {'id': article.id}) }}" class="btn btn-primary">
        Lire la suite
    </a>
</article>

{% endfor %}
```
