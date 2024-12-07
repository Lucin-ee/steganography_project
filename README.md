# Steganography Project

Un outil Python simple pour cacher et extraire des messages dans des images en utilisant la méthode de stéganographie LSB (Least Significant Bit). Ce projet inclut des fonctionnalités pour encoder et décoder des messages, analyser les histogrammes d'images pour détecter des données potentiellement cachées, et effectuer une stéganalyse de base.

## Fonctionnalités

- **Message Encoding**: Cache un message texte dans une image en utilisant un nombre spécifié de LSB
- **Message Decoding**: Extrait un message caché d'une image
- **LSB Histogram Analysis**: Génère des histogrammes des motifs LSB dans les images pour détecter d'éventuelles données cachées

## Prérequis

- Python 3.8+
- Poetry : Utilisé pour la gestion des dépendances, le versioning et le packaging. Installez Poetry depuis [le guide d'installation de Poetry](https://python-poetry.org/docs/#installation).

## Installation

### Cloner le repository

```bash
git clone https://github.com/yourusername/steganography_project.git
cd steganography_project
```

### Installer les dépendances avec Poetry

```bash
poetry install
```

## Utilisation

### Encoder et Décoder des Messages

Vous pouvez encoder un message dans une image, le décoder, et analyser les histogrammes LSB de l'image.

#### Encoder un Message

Pour encoder un message, utilisez la commande suivante :

```bash
poetry run encode <input_image_path> "<message>" <output_image_path> <lsb_count>
```

Exemple :
```bash
poetry run encode img.png "Hello, World!" encoded_img.png 2
```

#### Décoder un Message

Pour décoder un message depuis une image, utilisez :

```bash
poetry run decode <encoded_image_path> <lsb_count>
```

Exemple :
```bash
poetry run decode encoded_img.png 2
```

### Analyse d'Histogramme pour la Stéganalyse

Générez des histogrammes LSB pour chaque canal de couleur dans une image :

```bash
poetry run histogram <image_path> <lsb_count>
```

Exemple :
```bash
poetry run histogram encoded_img.png 2
```

Cela sauvegardera un graphique d'histogramme au format PNG dans le répertoire courant.

## Tests

Pour exécuter la suite de tests, utilisez :

```bash
poetry run pytest
```

## Structure du Projet

```
steganography_project/
├── steganography_project/
│   ├── __init__.py        # Initialise le package
│   ├── encode_decode.py   # Fonctions d'encodage et décodage
│   └── histogram_analysis.py  # Fonction d'analyse d'histogramme LSB
├── tests/                 # Suite de tests pour les fonctions
├── README.md             # Documentation du projet
└── pyproject.toml        # Fichier de configuration Poetry
```

## Configuration

Tous les paramètres, y compris le nombre de LSB (jusqu'à 4), peuvent être configurés directement via la ligne de commande lors de l'exécution des commandes d'encodage, de décodage et d'analyse d'histogramme.

### Static Code Analysis
Ce projet utilise `flake8` pour la static code analysis. A installer via 
```bash
pip install flake8
```
et à run avec 
```bash
flake8 path/to/your/code
```

#### Pre-Commit Hook for Static Code Analysis
Pre-commit hooks automatically run static code analysis. To set it up:
```bash
pip install pre-commit
pre-commit install




