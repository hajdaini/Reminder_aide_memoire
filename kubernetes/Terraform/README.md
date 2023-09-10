# Concepts Terraform

- **Ressources** : Entités gérées par Terraform, ex: VM/bdd etc...
- **Providers** : Plugins permettant l'interaction avec différents fournisseurs cloud ou services.
- **Modules** : Blocs de construction réutilisables pour organiser et structurer votre code.
- **État (State)** : Fichier stockant l'état actuel de votre infrastructure Terraform.
- **Plan & Apply** : Les étapes pour prévisualiser et appliquer les changements d'infrastructure.
- **Variables** : Paramètres configurables pour rendre votre code Terraform flexible.
- **Sorties (Outputs)** : Les valeurs que vous pouvez récupérer après le déploiement de l'infrastructure.
- **Cycle de Vie** : Les phases de développement, de planification, d'application et de mise à jour de l'infrastructure.
- **Datasource** : Source de données pour importer des informations externes.
- **Backend** : Configuration pour stocker l'état Terraform de manière sécurisée, souvent dans un système de stockage distant.
- **Workspace** : Environnements isolés pour gérer plusieurs états Terraform au sein d'un même projet.


```hcl
# Configuration du provider AWS
provider "aws" {
  region = "us-east-1"
}

# Backend pour stocker l'état Terraform
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}

# Définition d'une ressource (machine virtuelle EC2)
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleInstance"
  }
}

# Variables pour flexibilité
variable "instance_count" {
  type    = number
  default = 1
}

# Sorties pour informations post-déploiement
output "instance_id" {
  value = aws_instance.example.id
}

# Utilisation d'une ressource datasource pour obtenir des infos sur une instance
data "aws_instance" "example_data" {
  instance_id = aws_instance.example.id
}

# Cycle de vie de la ressource
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  # Crée avant de détruire (pas d'arrêt)
  lifecycle {
    create_before_destroy = true

    # Permet la destruction lors de la mise à jour
    prevent_destroy      = false
  }
}
```


structure

```text
my-terraform-project/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── .gitignore
├── modules/
│   ├── module/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── prod/
│   │   ├── main.tf
│   │   ├── variables.tf
└── │   ├── outputs.tf
```

- `main.tf` : Le fichier principal où vous définissez les ressources et les configurations.
- `variables.tf` : Le fichier où vous définissez les variables utilisées dans le projet.
- `outputs.tf` : Le fichier où vous définissez les sorties pour récupérer des informations après le déploiement.
- `terraform.tfvars` : Le fichier contenant les valeurs des variables spécifiques à l'environnement.
- `environments/` : Le répertoire qui contient les configurations spécifiques à chaque environnement (par exemple, développement et production).
- `modules/` : Le répertoire qui contient des modules Terraform réutilisables.
