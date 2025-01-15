---
 GuiCommand:
   Name: BIM IfcQuantities
   Name/fr: BIM Quantités IFC
   Workbenches: BIM Workbench/fr
   MenuLocation: Gestion , Gérer les quantités IFC...
---

# BIM IfcQuantities/fr

## Description

L\'outil **Quantités IFC** vous permet de vérifier les **quantités explicites** attachées aux objets à exporter au format IFC.

<img alt="" src=images/BIM_ifcquantities_screenshot.png  style="width:600px;"> 
*Gestionnaire de quantités IFC*

Le format IFC permet d\'inclure, pour tout objet, des quantités explicites, qui peuvent être des choses comme \"Width\" ou \"Height\" ou \"Area\" (\"Largeur\" ou \"Hauteur\" ou \"Surface\"). Il n\'y a pas de norme qui définit quel type d\'objet doit inclure quel type de quantité et il n\'y a également aucune garantie que ces quantités explicites reflètent réellement la géométrie de l\'objet. En d\'autres termes, ces quantités peuvent avoir des valeurs erronées ou même mentir. Un mur pourrait avoir sa géométrie comme un cube d\'une longueur de 10 mètres mais avoir une quantité \"Length\" attachée de 8 mètres.

L\'idée derrière des quantités explicites est de les mettre à la disposition des applications qui ne peuvent pas lire la géométrie, comme une application de feuille de calcul. Une telle application, lors de la lecture d\'un fichier IFC avec des quantités explicites, pourrait tout de même se faire une idée des dimensions d\'un objet et les utiliser par exemple pour des calculs de quantités.

Par défaut, lors de l\'exportation d\'un fichier IFC depuis FreeCAD, aucune quantité explicite n\'est exportée. Avec le gestionnaire de quantités IFC, vous pouvez marquer les quantités à exporter et vérifier leurs valeurs. Des messages d\'avertissement seront affichés à côté des valeurs nulles, vous informant des problèmes potentiels que vous pourriez vouloir résoudre avant d\'exporter.

Vous pouvez également utiliser le gestionnaire de quantités pour modifier ou fixer les valeurs réelles **Height**, **Width** et **Length** des objets. Mais cela affectera la géométrie de l\'objet dans FreeCAD.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM IfcQuantities/fr
