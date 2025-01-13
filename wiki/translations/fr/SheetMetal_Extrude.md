---
 GuiCommand:
   Name: SheetMetal Extrude
   Name/fr: SheetMetal Prolonger une face
   MenuLocation: SheetMetal , Prolonger une face
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **E**
---

# SheetMetal Extrude/fr

## Description

La commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Prolonger une face** prolonge une tôle à partir d\'une face de bord sélectionnée.

Elle crée une **extension simple** le long de la normale du bord sélectionné :

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

Si une esquisse de contour est ajoutée, elle crée une **géométrie de connexion** pour fermer un profil :

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Trois profils avec des esquisses à ajouter → trois résultats*



## Utilisation



### Extension simple 

1.  Sélectionnez une ou plusieurs faces d\'arêtes à étendre.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_Extrude.svg" width=16px> [Prolonger une face](SheetMetal_Extrude/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Prolonger une face** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Prolonger une face** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **E**.
3.  Le [panneau des tâches](Task_panel/fr.md) **Paramètres d\'extension** s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres faces.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les changements.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **Extend** sera créé et consistera en une nouvelle extension de face sur chaque face sélectionnée.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



### Extension de connexion 

:   (Préparez une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) pour l\'emboîtement des profils)

1.  Sélectionnez la face de l\'arête à prolonger.
2.  Lancez la commande comme décrit ci-dessus.
3.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
4.  Dans l\'éditeur de propriétés, appuyez sur le bouton **...** de la propriété **Sketch**.
5.  La fenêtre de dialogue Lien s\'ouvre.
    -   Sélectionnez l\'esquisse préparée dans la liste
    -   Appuyez sur le bouton **OK** pour fermer la boîte de dialogue.
6.  Définissez la propriété **Use Subtraction** sur `True` pour créer des découpes afin de faire de la place pour les extensions.
7.  Définissez la propriété **Offset** pour ajuster le dégagement autour de l\'extension.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Trois profils → position des esquisses → résultats sans découpes → résultats finaux*



### Remarques

-   Une esquisse peut contenir plus d\'un contour.

:   Après avoir inséré une esquisse, l\'un de ses contours au moins doit toucher une face opposée, sinon l\'outil ne parviendra pas à créer une extension ou une découpe.





:   Un seul contour touchant une face opposée suffit à créer une géométrie d\'extension à partir de tous les contours de l\'esquisse.

-   Chaque découpe aura une forme cuboïde, quelle que soit la forme de l\'esquisse du contour correspondant.

-   Les formes autres que les rectangles peuvent se comporter de manière un peu étrange et même si l\'objet peut être déplié, le résultat ne sera pas celui escompté.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Trois esquisses et leurs extensions résultantes : plaque triangulaire séparée avec une découpe rectangulaire, cercle sans dégagement → le solide non plié est divisé à une position inattendue*

-   Dans une opération d\'extension, il est recommandé de laisser la propriété **Refine** définie sur `True` (par défaut).

-   L\'opération d\'extension avec une esquisse liée peut échouer en raison de problèmes de coplanarité si la face du côté de l\'esquisse et la face du côté opposé sont coplanaires, mais avec des orientations opposées. Un petit décalage peut aider dans un tel cas.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Extend est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: objet de base. Lien vers la face plane à étendre.

-    **gap1|Distance**: espace par rapport au côté gauche. Valeur par défaut : {{value|0,00 mm}}.

-    **gap2|Distance**: espace par rapport au côté droit. Valeur par défaut : {{value|0,00 mm}}.

-    **length|Length**: longueur de la paroi. Valeur par défaut : {{value|10,00 mm}}.


{{Properties_Title|Parameters Ext.}}

-    **Offset|Distance**: décaler la soustraction. Valeur par défaut : {{value|20,00 µm}}.

-    **Refine|Bool**: utiliser l\'amélioration. Valeur par défaut : `True`.

-    **Sketch|Link**: esquisse de la paroi.

-    **Use Subtraction|Bool**: utiliser la soustraction. Valeur par défaut : `False`.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Extrude/fr
