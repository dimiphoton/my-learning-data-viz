# Tutoriel 3 : Création d’une carte géographique à partir de données GeoJSON

## Objectif
Dans ce tutoriel, vous apprendrez à importer des données géospatiales depuis un fichier GeoJSON et à les visualiser sur une carte dans Power BI.

## Étapes

### 1. Téléchargez les données GeoJSON
Téléchargez le fichier GeoJSON pour afficher des données géographiques sur les villes dans le monde :  
[world-cities.geojson](https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/world-cities.geojson).

### 2. Importer le fichier GeoJSON dans Power BI
- Ouvrez Power BI Desktop.
- Cliquez sur **Obtenir des données** > **Web**.
- Entrez l'URL du fichier GeoJSON :  
  `https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/world-cities.geojson`
- Cliquez sur **OK** pour charger les données.

### 3. Créer une carte géographique
- Dans le panneau **Visualisations**, sélectionnez l'option **Carte**.
- Faites glisser **Latitude** et **Longitude** dans les champs appropriés de la carte.
- Ajoutez des informations comme la population des villes dans les **Valeurs** pour afficher des cercles de tailles variées en fonction de la population.

### 4. Personnaliser la carte
- Dans le panneau **Format**, vous pouvez personnaliser les couleurs, les tailles des cercles, et d'autres paramètres pour rendre la carte plus lisible.

## Attendus
À la fin de ce tutoriel, vous devriez avoir une carte géographique affichant les villes du monde avec des cercles de taille ajustée en fonction de la population, le tout avec un design personnalisé.
