# Path ToolBit/fr
}





{{TOCright}}

## Description

Les Outils coupants sont la base du système [Path Outils](Path_Tools/fr.md). Ils représentent un outil spécifique qui peut être utilisé dans une tâche de trajectoire pour générer un parcours d\'outil. Chaque Outil coupant est enregistré dans un fichier JSON. JSON est une donnée structurée qui peut être facilement analysée par des macros ou des scripts Python mais qui reste lisible par l\'homme. La description des outils coupants avec JSON offre la possibilité de créer automatiquement de grandes collections d\'outils coupants précis ou avec un script.

Le stockage d\'un outil sous forme de fichier JSON est une bonne idée, mais il ne permet pas d\'obtenir une représentation précise de la vignette ou du corps solide. D\'autre part, si chaque outil coupant était créé en tant qu\'objet FreeCAD, l\'obtention du corps solide serait simple mais nécessiterait un stockage énorme pour les grandes collections d\'outils. De plus, la création automatique d\'outils coupants en tant qu\'objets FreeCAD serait difficile, voire impossible.

Au lieu de cela, l\'outil coupant est un hybride. Le fichier JSON contient le chemin d\'accès au fichier forme de l\'outil et les valeurs de tous les paramètres requis pour créer l\'outil coupant spécifique.

Lorsqu\'un outil est instancié dans un travail, un corps est créé à partir du modèle et les contraintes sont définies en fonction des valeurs du fichier JSON. Tous les paramètres supplémentaires sont créés en tant que propriétés de l\'objet. Cela fournit la forme et les dimensions correctes qui peuvent être utilisées pour générer un nuage de points ou un maillage pour les algorithmes avancés (et potentiellement la simulation).

## Utilisation

Dans l\'interface graphique de FreeCAD, le gestionnaire de bibliothèque Path toolbit fournit un mécanisme pour créer un nouveau outil coupant. Un même outil coupant peut exister dans plusieurs bibliothèques d\'outils coupants.

1.  Ouvrez le gestionnaire Path Outil coupant.
2.  Sélectionnez une bibliothèque.
3.  Créez un outil coupant.

## Structure JSON 


{{Code|
{
  "version": 2,
  "name": "T1",
  "shape": "endmill.fcstd",
  "attribute": {},
  "parameter": {
    "CuttingEdgeHeight": "30.000 mm",
    "Diameter": "1.000 mm",
    "Length": "50.000 mm",
    "ShankDiameter": "3.000 mm"
  }
}
}}

## Options

## En relation 

-   [Path Outils](Path_Tools/fr.md)
-   [Path Bibliothèque des outils coupants](Path_ToolBitLibraryOpen/fr.md)





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolBit/fr
