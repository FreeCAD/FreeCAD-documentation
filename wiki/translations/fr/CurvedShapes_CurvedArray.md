---
- GuiCommand:/fr
   Name:CurvedShapes CurvedArray
   Name/fr:CurvedShapes CurvedArray
   MenuLocation:
   Workbenches:[CurvedShapes](CurvedShapes_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# CurvedShapes CurvedArray/fr

## Description

Crée un réseau et redimensionne les objets dans les limites d\'une ou plusieurs courbes de la coque. Dans cet exemple, la forme de base orange est redimensionnée dans les limites des courbes de coque rouge et violette. Il n\'est pas nécessaire de relier les courbes entre elles. Les courbes de coque doivent se trouver sur le plan XY- XZ- ou YZ- ou être parallèles à celui-ci.

<https://github.com/chbergmann/CurvedShapesWorkbench/blob/master/Examples/WingExample.png> [Image:](Image:.md)

## Utilisation

1.  Étape 1
2.  Étape 2: appelez la commande de plusieurs manières:
    -   Utilisation de <img alt="" src=images/WorkbenchName_Command.svg  style="width:24px;"> [Commande WorkbenchName](WorkbenchName_Command/fr.md)
    -   Utilisation du raccourci clavier {{KEY}} {{KEY}}
    -   Utilisation de **Menu → Command** dans la liste déroulante Menu
3.  Étape 3

## Remarques

-   La première courbe que vous sélectionnez pour la création de CurvedArray sera l\'élément balayé et redimensionné dans les limites des autres courbes sélectionnées.

## Propriétés


{{Properties_Title|Base}}

-    {{PropertyData/fr|Base}}: objet pour créer un tableau à partir de

-    {{PropertyData/fr|Hullcurves}}: liste d\'une ou plusieurs courbes limites

-    {{PropertyData/fr|Axis}}: axe de direction de la forme de base

-    {{PropertyData/fr|Items}}: nombre d\'éléments du tableau

-    {{PropertyData/fr|OffsetStart}}: décalage de la première partie dans la direction de l\'axe

-    {{PropertyData/fr|OffsetEnd}}: décalage de la dernière partie de la fin dans la direction opposée de l\'axe

-    {{PropertyData/fr|Twist}}: applique une rotation autour de l\'axe aux éléments du tableau.

-    {{PropertyData/fr|Surface}}: fait une surface sur les éléments du tableau

-    {{PropertyData/fr|Solid}}: fait un solide si la base est une forme fermée



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Name](Category_Name.md) > [External Command Reference](Category_External Command Reference.md) > CurvedShapes CurvedArray/fr
