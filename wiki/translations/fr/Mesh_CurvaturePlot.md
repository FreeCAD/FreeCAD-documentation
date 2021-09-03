---
- GuiCommand:/fr
   Name:Mesh VertexCurvature
   Name/fr:Mesh Tracé de courbure
   MenuLocation:Maillages → Tracé de courbure
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Info de courbures](Mesh_CurvatureInfo/fr.md)
---

## Description

La commande **Mesh Tracé de courbure** crée des objets maillés de courbure pour les objets maillés. Un objet de courbure affiche la courbure d\'un maillage en utilisant différentes couleurs pour les parties convexes, plates et concaves.

![](images/Mesh_VertexCurvature_example.png ) *Exemple d'un objet maillé de courbure*

## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs manières d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_VertexCurvature.svg" width=16px> [Mesh Tracé de courbure](Mesh_VertexCurvature/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Meshes → <img src="images/_Mesh_VertexCurvature.svg" width=16px> Tracé de courbure}} dans le menu.
    -   Sélectionnez l\'option {{MenuCommand|<img src="images/_Mesh_VertexCurvature.svg" width=16px> Tracé de courbure}} dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou dans le menu contextuel [vue 3D](3D_view/fr.md).

## Propriétés

Pour un objet maillé de courbure, les propriétés suivantes sont disponibles dans l\'[Éditeur de propriétés](Property_editor/fr.md). Sélectionnez l\'option {{MenuCommand|Show all}} dans le menu contextuel de l\'éditeur de propriétés pour afficher les propriétés masquées.

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Label|String}}: nom modifiable par l\'utilisateur pour l\'objet, une chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Source|Link}}: lien vers l\'objet mesh.

#### Données cachées {#données_cachées}


{{TitleProperty|Base}}

-    {{PropertyData/fr|Curv Info|CurvatureList}}: liste d\'informations sur la courbure.

-    {{PropertyData/fr|Expression Engine|ExpressionEngine}}: liste d\'expressions.

-    {{PropertyData/fr|Label2|String}}: description modifiable par l\'utilisateur pour l\'objet, une chaîne UTF8 arbitraire pouvant inclure des sauts de ligne.

-    {{PropertyData/fr|Visibility|Bool}}: mis à `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md).

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Display Mode|Enumeration}}: {{value|Absolute Curvature}} (par défaut), {{value|Mean Curvature}}, {{value|Gaussian Curvature}}, {{value|Maximum Curvature}}, {{value|Courbure minimale}}.

-    {{PropertyView/fr|On Top When Selected|Enumeration}}: {{value|Disabled}} (par défaut), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    {{PropertyView/fr|Selection Style|Enumeration}}: {{value|Shape}}, {{value|BoundBox}} (par défaut).

-    {{PropertyView/fr|Show In Tree|Bool}}: si mis à `True`, l\'objet apparaît dans la [vue en arborescence](tree_view/fr.md).

-    {{PropertyView/fr|Visibility|Bool}}: si mis à `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md).

#### Vue cachée {#vue_cachée}


{{TitleProperty|Base}}

-    {{PropertyView/fr|Texture Material|Material}}: un [App Material](App_Material/fr.md) associé à l\'objet.





{{Mesh Tools navi

}}  
