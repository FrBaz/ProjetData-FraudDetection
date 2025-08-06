# Source de données

Via kaggle. Trop lourde pour Github, facile à télécharger soi même (voir notebook)

# Build et utilisation de l'image docker :

## Build de l'image
docker build -t fraud-api ./api

## Lancement de l’API (sur le port 5000)
docker run -p 5000:5000 fraud-api
