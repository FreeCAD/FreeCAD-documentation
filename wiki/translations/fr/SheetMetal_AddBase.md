---
- GuiCommand:/fr
   Name:SheetMetal AddBase
   Name/fr:SheetMetal Tôle de base
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**C** **B**
---

# SheetMetal AddBase/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> *SheetMetal AddBase* crée un objet de base SheetMetal à partir d\'une esquisse.

A partir d\'un contour ouvert, il crée un *profil* prismatique :

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

A partir d\'un contour fermé, il crée une *plaque* de base (vierge) :

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">



## Utilisation



### Profilage

1.  Sélectionnez une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) à **contour ouvert**.
2.  Lancez <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [SheetMetal AddBase](SheetMetal_AddBase/fr.md) en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/SheetMetal_AddBase.svg" width=16px> [SheetMetal Tôle de base](SheetMetal_AddBase/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_AddBase.svg" width=16px> Faire un mur de base** option de menu.
    -   Le raccourci clavier : **C** puis **B**.
3.  Ajustez les paramètres du profil en modifiant les valeurs correspondantes dans l\'[Éditeur de propriétés](Property_editor/fr.md) :
    -   La propriété **length** pour la longueur du profil,
    -   La propriété **thickness** pour l\'épaisseur du profil,
    -   La propriété **radius** pour le rayon intérieur des plis.



### Plaque

1.  Sélectionnez une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) à **contour fermé**.
2.  Lancez la commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [SheetMetal AddBase](SheetMetal_AddBase/fr.md) (voir ci-dessus).
3.  Ajustez le paramètre de la plaque en éditant la valeur correspondante dans l\'[Éditeur de propriétés](Property_editor/fr.md) :
    -   La propriété **thickness** pour l\'épaisseur de la plaque.

:   

    :   (Les propriétés **length** et **radius** ne sont pas utilisées pour les plaques).



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Tôle de base est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Bend Side|Enumeration}}: \"Relief Type\". {{value|Outside}} (par défaut), {{value|Inside}}, {{value|Middle}}.

-    {{PropertyData/fr|Bend Sketch|Link}}: \"Objet Esquisse de mur\". Lien vers l\'esquisse de profil/de contour.

-    {{PropertyData/fr|Mid Plane|Bool}}: \"Extruder symétriquement au plan\".   `True`, le profil s\'étend symétriquement sur les deux côtés du plan d\'esquisse.

-    {{PropertyData/fr|Reverse|Bool}}: \"Inverse la direction d\'extrusion\". Valeur par défaut : `False`.

-    {{PropertyData/fr|length|Length}}: \"Longueur du mur\". Valeur par défaut : {{value|100,00 mm}}.

-    {{PropertyData/fr|radius|Length}}: \"Rayon de courbure\". Valeur par défaut : {{value|1,00 mm}}.

-    {{PropertyData/fr|thickness|Length}}: \"Epaisseur de la tôle\". Valeur par défaut : {{value|1,00 mm}}.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/fr
