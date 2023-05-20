# Twitter Sentiment Analysis Bot

Ce projet est un bot Twitter qui effectue l'analyse de sentiment sur les tweets en temps réel et génère des rapports visuels.

## Configuration

1. Créez une application Twitter sur le [portail de développement de Twitter](https://developer.twitter.com/) et obtenez vos clés API.
2. Installez les dépendances nécessaires à l'aide de pip : `pip install -r requirements.txt`

Assurez-vous de remplacer "votre clé API", "votre clé secrète d'API", "votre jeton d'accès" et "votre jeton d'accès secret" par vos propres clés et jetons d'API Twitter.

Notez que config.py est ajouté au fichier .gitignore pour éviter d'exposer vos clés API à des tiers.

Pour exécuter le projet, installez d'abord les dépendances avec pip install -r requirements.txt, puis exécutez python main.py.

Ce projet est un exemple simplifié d'analyse de sentiment. Pour une analyse plus précise, vous pourriez envisager d'utiliser un modèle d'apprentissage automatique plus sophistiqué et de prendre en compte d'autres facteurs, tels que le contexte du tweet et la fiabilité de la source.

## Usage

Exécutez le script principal : `python main.py`

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
