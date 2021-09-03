---
- GuiCommand:/fr
   Name:Draft Layer
   Name/fr:Draft Calque
   MenuLocation:Utilitaires → Calque
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Draft Groupement automatique](Draft_AutoGroup/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Calque** crée un Draft calque. Un calque est un groupe d\'un type particulier, doté d\'un certain nombre de [propriétés visuelles](#Vue.md). Ces propriétés, et toute modification qui leur est apportée, sont propagées aux objets placés à l\'intérieur du calque. Les calques eux-mêmes sont placés dans un autre groupe spécial : le Draft LayerContainer.

Cette commande a remplacé la commande Draft Groupe visuel dans la version 0.19 de FreeCAD.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Layer.svg" width=16px> [Draft Ajouter un calque au document](Draft_Layer/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Utilitaires → <img src="images/Draft_Layer.svg" width=16px> Calque}} dans le menu.
    -   Si le conteneur de calque existe déjà : clic droit dessus dans la [Vue en arborescence](Tree_view/fr.md) et sélectionnez l\'option {{MenuCommand|<img src="images/Draft_NewLayer.svg" width=16px> Ajouter un nouveau calque}} dans le menu contextuel.
2.  S\'il n\'existe pas, le conteneur de calque est créé en premier.
3.  Un calque est créé et placé dans le conteneur de calque.
4.  Si vous le souhaitez, vous pouvez modifier les [propriétés](#Propri.C3.A9t.C3.A9s.md) du calque.
5.  Optionnellement, vous pouvez placer des objets dans le calque en les glissant et en les déposant sur le calque dans la [Vue en arborescence](Tree_view/fr.md). Les objets peuvent également être placés dans un calque en modifiant la propriété {{PropertyData/fr|Group}} du calque.
6.  Vous pouvez également [activer](#Options_du_calque.md) le calque.

## Menu contextuel {#menu_contextuel}

### Options du conteneur du calque {#options_du_conteneur_du_calque}

Pour un Draft LayerContainer, ces options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :

-    {{MenuCommand|<img src="images/Draft_Layer.svg" width=16px> Merge layer duplicates}}: cette option ne fonctionne pas actuellement.

-    {{MenuCommand|<img src="images/Draft_NewLayer.svg" width=16px> Add new layer}}: ajoute un nouveau calque au document actuel.

### Options du calque {#options_du_calque}

Pour un Draft Calque, ces options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :

-    {{MenuCommand|<img src="images/button_right.svg" width=16px> [Activer ce calque](Draft_AutoGroup/fr.md)}}: active le calque sélectionné.

-    {{MenuCommand|<img src="images/Draft_SelectGroup.svg" width=16px> [Sélectionner le contenu du calque](Draft_SelectGroup/fr.md)}}: active le calque sélectionné.

## Remarques

-   Un nouveau calque peut également être créée avec la commande [Draft Groupement automatique](Draft_AutoGroup/fr.md).
-   L\'[atelier BIM](BIM_Workbench/fr.md) offre un [outil de gestion des calques](BIM_Layers/fr.md) complet qui sera éventuellement inclus dans l\'[atelier Draft](Draft_Workbench/fr.md).

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Calque est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Layer}}

-    {{PropertyData/fr|Group|LinkList}}: spécifie les objets qui se trouvent à l\'intérieur du calque.

### Vue


{{TitleProperty|Layer}}

Les propriétés de cette section sont appliquées aux objets qui sont placés à l\'intérieur du calque. Toute modification de ces propriétés leur est propagée. Pour deux propriétés, {{PropertyView/fr|Line Color}} et {{PropertyView/fr|Shape Color}}, ce comportement est facultatif.

-    {{PropertyView/fr|Draw Style|Enumeration}}: spécifie le style de dessin du calque : {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}} ou {{value|Dashdot}}.

-    {{PropertyView/fr|Line Color|Color}}: spécifie la couleur de la ligne du calque.

-    {{PropertyView/fr|Line Width|Float}}: spécifie la largeur de ligne de la couche.

-    {{PropertyView/fr|Override Line Color Children|Bool}}: indique si les modifications apportées à {{PropertyView/fr|Line Color}} du calque sont propagées aux objets situés à l\'intérieur du calque.

-    {{PropertyView/fr|Override Shape Color Children|Bool}}: spécifie si les modifications apportées à {{PropertyView/fr|Shape Color}} du calque sont propagées aux objets situés dans le calque.

-    {{PropertyView/fr|Shape Color|Color}}: spécifie la couleur de la forme du calque.

-    {{PropertyView/fr|Transparency|Percent}}: spécifie la transparence du calque.


{{TitleProperty|Print}}

-    {{PropertyView/fr|Line Print Color|Color}}: spécifie la couleur d\'impression des lignes du calque.

-    {{PropertyView/fr|Use Print Color|Bool}}: indique si la {{PropertyView/fr|Line Print Color|}} du calque est utilisée lorsqu\'un [TechDraw Vue Draft](TechDraw_DraftView/fr.md) est créé à partir des objets contenus dans le calque.

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft calque, utilisez la méthode `make_layer` du module Draft. Pour ajouter des objets à un calque ou en supprimer, modifiez sa propriété `Group`.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

layer = Draft.make_layer(line_color=(1.0, 0.0, 0.0, 0.0),
                         shape_color=(1.0, 1.0, 0.0, 0.0))

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)
layer.Group = [polygon1, polygon2, polygon3]

doc.recompute()
```





 
