Requirements :

1. **install php , curl and composer**

2. **In your php.ini enable :**

```php.ini
extension=curl
extension=pdo_mysql
```

3. run the commande :

```sh
composer create-project symfony/website-skeleton [PROJECT-NAME]
```

4. install php webserver plugin :

```sh
composer require server --dev
```

4. run your php server :

```sh
php bin/console server:run
```
