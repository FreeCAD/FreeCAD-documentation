---
- GuiCommand:/fr
   Name:SheetMetal Extrude
   Name/fr:SheetMetal Prolonger une face
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**E**
---

# SheetMetal Extrude/fr

## Description

La commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Extrude** prolonge une plaque de tôle au niveau d\'une face de bord sélectionnée.

Elle crée une **extension simple** le long de la normale à la face de l\'arête sélectionnée :

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

Si une esquisse de contour est ajoutée, elle crée une **géométrie de connexion** pour fermer un profil :

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Trois profils avec des esquisses à ajouter → trois résultats*

## Utilisation

### Extension simple 

1.  Sélectionnez une ou plusieurs faces d\'arêtes à étendre.
2.  Lancez la commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Prolonger une face** en utilisant l\'une des méthodes suivantes :
    -   Le bouton **<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**.
    -   L\'option du menu **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Extend Face**.
    -   Le raccourci clavier : **E**.
3.  Modifiez la valeur de la propriété **length** pour ajuster la longueur de l\'extension.

### Extension de connexion 

1.  Sélectionnez une face d\'arête à étendre.
2.  Lancez la commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Prolonger une face** (voir ci-dessus).
3.  Ajoutez une esquisse de contour coplanaire à la propriété **Sketch**.
4.  Définissez la propriété **Use Subtraction** sur `True` pour créer des découpes afin de faire de la place pour les extensions.
5.  Définissez la propriété **Offset** pour ajuster le dégagement autour de l\'extension.

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

Un objet SheetMetal Prolonger une face est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face planaire à étendre.

-    {{PropertyData/fr|gap1|Distance}}: \"Ecart par rapport au côté gauche\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|gap2|Distance}}: \"Ecart depuis le côté droit\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|length|Length}}: \"Longueur de la paroi\". Valeur par défaut : {{value|10,00 mm}}.


{{Properties_Title|Parameters Ext.}}

-    {{PropertyData/fr|Offset|Distance}}: \"Décalage pour la soustraction\". Valeur par défaut : {{value|20,00 µm}}.

-    {{PropertyData/fr|Refine|Bool}}: \"Utilise le raffinage\". Valeur par défaut : `True`.

-    {{PropertyData/fr|Sketch|Link}}: \"Esquisse de la paroi\".

-    {{PropertyData/fr|Use Subtraction|Bool}}: \"Utiliser la soustraction\". Valeur par défaut : `False`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Extrude/fr
