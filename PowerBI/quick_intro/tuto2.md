# Tutoriel 2 : Visualisation de données depuis une API Web (JSON)

## Objectif
Dans ce tutoriel, vous apprendrez à extraire des données depuis une API publique au format JSON et à les visualiser dans Power BI.

## Étapes

### 1. Obtenez des données depuis l'API
- Ouvrez Power BI Desktop.
- Cliquez sur **Obtenir des données** > **Web**.
- Entrez l'URL suivante pour récupérer les données JSON de l'API des populations mondiales :  
  `https://api.worldpopulationreview.com/v1/countries`
- Cliquez sur **OK** pour importer les données.

### 2. Transformer les données
- Dans l'éditeur de requêtes, vous verrez les données sous forme de tableau JSON.
- Cliquez sur **To Table** pour convertir le format JSON en format tabulaire.
- Explorez les colonnes disponibles comme **Country** (Pays) et **Population**.

### 3. Créer un graphique à barres
- Une fois les données nettoyées, allez dans la vue de rapport.
- Sélectionnez le graphique à barres.
- Faites glisser **Country** sur l'axe **X** et **Population** sur l'axe **Y**.

### 4. Personnaliser la visualisation
- Vous pouvez trier les pays par ordre décroissant de population et ajuster les couleurs, titres et autres éléments visuels.

## Attendus
À la fin de ce tutoriel, vous devriez avoir un graphique à barres montrant la population des pays extraits depuis l'API avec une personnalisation de l'affichage.
