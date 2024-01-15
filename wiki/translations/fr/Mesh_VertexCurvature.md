---
 GuiCommand:
   Name: Mesh VertexCurvature
   Name/fr: Mesh Courbure
   MenuLocation: Maillages , Tracer la courbure
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_CurvatureInfo/fr
---

# Mesh VertexCurvature/fr

## Description

La commande **Courbure** crée des objets de courbure pour les objets maillés. Un objet de courbure affiche la courbure d\'un maillage en utilisant différentes couleurs pour les parties convexes, plates et concaves.

![](images/Mesh_VertexCurvature_example.png ) 
*Exemple d'un objet Mesh Courbure*



## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs manières de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_VertexCurvature.svg" width=16px> [Tracer la courbure](Mesh_VertexCurvature/fr.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/_Mesh_VertexCurvature.svg" width=16px> Tracer la courbure** du menu.
    -   Sélectionnez l\'option **<img src="images/_Mesh_VertexCurvature.svg" width=16px> Tracer la courbure** depuis le menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou depuis le menu contextuel de la [vue 3D](3D_view/fr.md).



## Propriétés

Pour un objet Courbure, les propriétés suivantes sont disponibles dans l\'[éditeur de propriétés](Property_editor/fr.md). Sélectionnez l\'option **Tout afficher** dans le menu contextuel de l\'éditeur de propriétés pour afficher les propriétés masquées.



### Données


{{TitleProperty|Base}}

-    **Label|String**: nom modifiable par l\'utilisateur pour l\'objet, une chaîne UTF8 arbitraire.

-    **Source|Link**: lien vers l\'objet maillé.



#### Données cachées 


{{TitleProperty|Base}}

-    **Curv Info|CurvatureList**: liste d\'informations sur la courbure.

-    **Expression Engine|ExpressionEngine**: liste d\'expressions.

-    **Label2|String**: description modifiable par l\'utilisateur pour l\'objet, une chaîne UTF8 arbitraire pouvant inclure des sauts de ligne.

-    **Visibility|Bool**: mis à `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md).



### Vue


{{TitleProperty|Base}}

-    **Display Mode|Enumeration**: {{value|Absolute Curvature}} (par défaut), {{value|Mean Curvature}}, {{value|Gaussian Curvature}}, {{value|Maximum Curvature}}, {{value|Courbure minimale}}.

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (par défaut), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}}, {{value|BoundBox}} (par défaut).

-    **Show In Tree|Bool**: si mis à `True`, l\'objet apparaît dans la [vue en arborescence](Tree_view/fr.md).

-    **Visibility|Bool**: si mis à `True`, l\'objet apparaît dans la [vue 3D](3D_view/fr.md).



#### Vue cachée 


{{TitleProperty|Base}}

-    **Texture Material|Material**: un [App Material](App_Material/fr.md) associé à l\'objet.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh VertexCurvature/fr
