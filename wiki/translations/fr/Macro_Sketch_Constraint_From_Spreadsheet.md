# Macro Sketch Constraint From Spreadsheet/fr
{{Macro/fr
|Name=Macro Sketch Constraint From Spreadsheet
|Name/fr=Macro Sketch Constraint From Spreadsheet
|Description=Macro qui, par un simple clic sur une cellule du tableur, ajoute une contrainte de longueur à une ligne, un cercle ou entre 2 points en utilisant un alias ou une adresse de cellule du tableur (ex. C2). Les modifications futures de la feuille de calcul mettront à jour la contrainte. La macro peut créer des alias pour vous.<br>Il suffit de sélectionner une ligne, deux points ou une contrainte, de cliquer sur une cellule de la feuille de calcul et d'exécuter la macro. Vous pouvez sélectionner des lignes, des points aux extrémités d'une ligne, des points, des cercles ou des arcs de cercle.
|Author=2cv001
|Download=[https://wiki.freecad.org/images/d/dc/Macro_Sketch_Constraint_From_Spreadsheet.svg Icône de la barre d'outils]
|Version=01.04
|Date=2024-11-25
|FCVersion=Toutes
}}

## Description

**Contactez-moi si quelque chose ne va pas.**

Macro qui, par un simple clic sur une cellule du tableur, ajoute une contrainte de longueur à une ligne ou entre 2 points en utilisant un alias ou une adresse de cellule du tableur (ex. C2). Les modifications ultérieures de la feuille de calcul mettront à jour la contrainte. La macro peut créer des alias pour vous.

Il suffit de sélectionner 1 ligne, 2 points ou une contrainte, de cliquer sur une cellule du tableur et d\'exécuter la macro. Vous pouvez sélectionner des polylignes, des points aux extrémités d\'une ligne, des points, des cercles ou des arcs de cercle.

![](images/SketchConstraintFromSpreadsheet1.gif )


{{Codeextralink|https://raw.githubusercontent.com/2cv001/FreeCAD-macros/master/Spreadsheet/Sketch_Constraint_From_Spreadsheet.FCMacro}}



## Utilisation



### Création automatique d\'objets 

Si vous exécutez la macro et que vous n\'avez pas encore créé de feuille de calcul, de corps ou d\'esquisse, la macro vous propose de les créer et ouvre ensuite l\'esquisse en mode édition et la feuille de calcul afin que vous puissiez commencer à la remplir.

![](images/SketchConstraintFromSpreadsheet7.gif )



### Création automatique d\'alias 

Ce n\'est pas obligatoire, mais il est préférable d\'utiliser des alias dans votre feuille de calcul. La macro peut créer des alias à partir des textes contenus dans les cellules.
Deux modes :

-   un mode manuel où vous sélectionnez vous-même les cellules contenant du texte pour l\'alias et un mode automatique.
-   et un mode automatique :



#### Mode automatique 

Un mode automatique où les alias sont automatiquement créés en utilisant une zone de texte définie par une cellule. La zone comprend la cellule et celles qui se trouvent en dessous. Ces textes correspondent au nom de l\'alias. L\'alias est créé à droite de son texte.\" La cellule désignée (ici A3) est éditable dans ces boîtes de dialogue :

![Alias automatic creation](images/SketchConstraintFromSpreadsheet2302.png )

![Alias automatic creation](images/SketchConstraintFromSpreadsheet2303.png ) ![Alias automatic creation](images/SketchConstraintFromSpreadsheet2304.gif )



#### Mode manuel 

Pour utiliser le mode manuel, ne cochez pas l\'option \"Automatic alias\".

![Alias creation](images/SketchConstraintFromSpreadsheet2301.png )

![Alias creation](images/SketchConstraintFromSpreadsheet8.gif )



### Création de contraintes 

1\) Sélectionnez :

-   une ligne,
-   deux points (extrémité d\'une ligne, centre d\'un cercle, etc.)
-   ou une contrainte de longueur.

![](images/SelectPoints.png )

2\) Cliquez sur une cellule de la feuille de calcul, avec ou sans alias, qui contient une valeur numérique :

![](images/Capture1.png )

3\) Lancez la macro.

4\) Sélectionnez le type de contrainte souhaité :

![](images/Choose_type_of_constraint.png )

Si la cellule a un alias, la propriété de longueur de la contrainte sera quelque chose comme \"Spreadsheet.alias\". Dans le cas contraire, il s\'agira de quelque chose comme \"Spreadsheet.D4\".

![](images/If_the_spreadsheet_has_an_alias.png )

5\) Si la contrainte provoque un conflit dans l\'esquisse et que la case \"conflict detection\" est cochée, la macro propose de supprimer la nouvelle contrainte :

![](images/SketchConstraintFromSpreadsheet3.gif )

Si vous sélectionnez une contrainte existante, vous pouvez remplacer sa valeur par une valeur provenant d\'une feuille de calcul :

![](images/SketchConstraintFromSpreadsheet2.gif ) ![](images/SketchConstraintFromSpreadsheet4.gif )

La macro peut également gérer une géométrie externe provenant d\'une autre esquisse : ![](images/SketchConstraintFromSpreadsheet9.gif )

Pour être encore plus précis, si, par exemple, une ligne est horizontale plutôt que verticale, à l\'ouverture de la boîte de dialogue, le focus sera sur le bouton permettant d\'appliquer une contrainte horizontale. Si la ligne est verticale et non horizontale, le focus sera sur le bouton permettant d\'appliquer une contrainte verticale. Dans les deux cas, il vous suffit d\'appuyer sur la touche Entrée si vous êtes satisfait de votre choix.

![](images/SketchConstraintFromSpreadsheet5.gif )

La macro fonctionne également pour les protusions (propriété Length), les poches (propriété Length), les filets (propriété Radius), les chanfreins (propriété Size) et les épaisseurs (propriété Value). Si vous cliquez sur un protusion, par exemple, puis sur une cellule avec la valeur souhaitée, la propriété Length de la protusion est automatiquement modifiée.
![](images/SketchConstraintFromSpreadsheet20240801.gif )



## Liens

-   [Forum de discussion (français)](https://forum.freecad.org/viewtopic.php?t=75972)
-   [Forum discussion (English)](https://forum.freecad.org/viewtopic.php?style=5&t=76990)
-   [Liste des macros](Macros_recipes/fr.md)
-   [Comment installer des macros](How_to_install_macros/fr.md)
-   [Personnaliser la barre d\'outils](Customize_Toolbars/fr.md)



## Crédits

Merci à openBrain, mario52 et onekk pour leur aide sur le code!
Merci à Syres pour les tests et pour l\'aide sur le format dans le code.
Merci à Roy043 et David69 pour les diverses révisions et améliorations du wiki.
Merci à L\'ami René pour les tests et les idées.

## Script

Icône de la barre d\'outils ![](images/Macro_Sketch_Constraint_From_Spreadsheet.svg )

### Code

ver 01.04 2024/11/25 by 2cv001 **Macro_Sketch_Constraint_From_Spreadsheet.FCMacro** 

#### Téléchargement

{{CodeDownload|https://raw.githubusercontent.com/2cv001/FreeCAD-macros/master/Spreadsheet/Sketch_Constraint_From_Spreadsheet.FCMacro| Download latest version of the macro}}



---
⏵ [documentation index](../README.md) > Macro Sketch Constraint From Spreadsheet/fr
