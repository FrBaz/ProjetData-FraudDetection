# Source de données

Via kaggle. Trop lourde pour Github, facile à télécharger soi même (voir notebook)

# Build et utilisation de l'image docker :

## Build de l'image
docker build -t fraud-api ./api

## Lancement de l’API (sur le port 5000)
docker run -p 5000:5000 fraud-api

**Attention** : il est impératif de rentrer les colonnes dans l'ordre, et d'ajouter Amount_Scaled et Hour_Scaled.

DATA_Scaled = (DATA - mean)/std ; 
 - amount_mean = 88.34961925093133 ; amount_std = 250.11967013523534
 - hour_mean = 14.537950752614933 ; hour_std 5.847050982336524
