---
 GuiCommand:
   Name: SheetMetal AddCornerRelief
   Name/fr: SheetMetal Grugeage
   MenuLocation: SheetMetal , Créer un grugeage à un coin
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **C** **R**
---

# SheetMetal AddCornerRelief/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> **SheetMetal Grugeage** ajoute un grugeage à un coin. Un grugeage est généralement créé dans les coins où deux pliures se rencontrent, mais la commande peut également créer un grugeage dans un coin ouvert.

La commande ne peut créer qu\'un seul grugeage à la fois.

<img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width:300px;"> 
*Coin par défaut de deux pliures → Coin avec un grugeage*

<img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width:300px;"> 
*Coin par défaut de deux pliures → Coin ouvert avec un grugeage*



## Utilisation

1.  Sélectionnez deux arêtes d\'un coin.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Créer un grugeage à un coin](SheetMetal_AddCornerRelief/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Créer un grugeage à un coin](SheetMetal_AddCornerRelief/fr.md)** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Créer un grugeage à un coin** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **C** puis **R**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Générer une forme de base de la tôle* s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres faces.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les changements.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **CornerRelief** sera créé et consistera en un grugeage au niveau du coin sélectionné.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Formes de grugeage 

La forme d\'un grugeage de coin peut être modifiée en changeant les valeurs de ses propriétés :

La valeur de la propriété **ReliefSketch** peut être choisie parmi une liste : {{value|Circle}} (par défaut), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{value|Circle}}et {{value|Square}} utilisent la valeur de la propriété **Size** pour mettre le grugeage à l\'échelle.

-    {{value|Circle-Scaled}}et {{value|Square-Scaled}} utilisent la valeur de la propriété **Size Ratio** pour mettre le grugeage à l\'échelle.

-    {{value|Sketch}}active l\'utilisation de l\'esquisse listée dans la propriété **Sketch** pour définir la forme du grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width:200px;"> 
*Grugeage circulaire (paramètres par défaut) → Grugeage carré (paramètres par défaut) → Grugeage basé sur une esquisse*



## Un regard plus attentif sur les tailles de grugeage 

Pour avoir une idée de comment et où le grugeage est placé, nous déplions un coin par défaut sans grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width:200px;">



*Coin par défaut de deux pliures → Coin du solide déplié → Coin vu de dessus.*

L\'étape suivante consiste à ouvrir l\'esquisse de dépliage, à créer un cercle à travers 3 points et à ajouter une dimension de rayon.
Maintenant, nous ajoutons un grugeage d\'angle, créons le solide de dépliage correspondant et ouvrons à nouveau la première esquisse de dépliage.
L\'ajout d\'un cercle concentrique de 3 mm de rayon révèle que nous avons trouvé comment le cercle interne est positionné car le nouveau cercle s\'insère parfaitement dans la découpe du solide de dépliage du grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width:300px;">



*Coin par défaut avec esquisse dépliée → Coin avec grugeage par défaut et la même esquisse dépliée*

Si vous essayez de définir la propriété **Size** à une valeur inférieure à la valeur déterminée de 1,67 mm, vous obtiendrez une erreur ; toute valeur supérieure devrait fonctionner correctement.

En passant à Circle-Scaled et en créant un autre solide non plié, on constate que 1,67 mm est également la base de la propriété **Size Ratio**.



## Remarques

-   Le facteur k définit l\'emplacement de l\'axe neutre dans l\'épaisseur d\'une tôle, conformément à la norme ANSI.
-   La sélection accepte plus de deux arêtes, mais seules les deux premières sont prises en compte.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal CornerRelief est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **ReliefSketch|Enumeration**: type de grugeage d\'angle. {{value|Circle}} (par défaut), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    **Size|Length**: taille de la forme. Valeur par défaut : {{value|3,00 mm}}.

-    **Size Ratio|Float**: rapport de taille de la forme. Valeur par défaut : {{value|1,50}}.

-    **base Object|LinkSub**: objet de base. Liens vers la paire d\'arêtes définissant la position de la contre-dépouille d\'angle.

-    **kfactor|FloatConstraint**: position de l\'axe neutre. Valeur par défaut : {{value|0,50}}.


{{Properties_Title|Parameters1}}

-    **Sketch|Link**: esquisse du grugeage.

-    **XOffset|Distance**: espace par rapport au premier côté. Valeur par défaut : {{value|0,00 mm}}.

-    **YOffset|Distance**: espace par rapport au deuxième côté. Valeur par défaut : {{value|0,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/fr
