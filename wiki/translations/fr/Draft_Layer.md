---
- GuiCommand:
   Name: Draft Layer
   Name/fr: Draft Calque
   MenuLocation: Utilitaires -> Calque
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   Version: 0.19
   SeeAlso: Draft_AutoGroup/fr, Draft_LayerManager/fr
---

# Draft Layer/fr

## Description

La commande <img alt="" src=images/Draft_Layer.svg  style="width:24px;"> **Draft Calque** crée un Draft calque. Un calque est un groupe d\'un type particulier, doté d\'un certain nombre de [propriétés visuelles](#Vue.md). Ces propriétés, et toute modification qui leur est apportée, sont propagées aux objets placés à l\'intérieur du calque. Les calques eux-mêmes sont placés dans un autre groupe spécial : le Draft LayerContainer.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Layer.svg" width=16px> [Calque](Draft_Layer/fr.md)**.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_Layer.svg" width=16px> Calque** du menu.
    -   Si le conteneur de calque existe déjà : clic droit dessus dans la [vue en arborescence](Tree_view/fr.md) et sélectionnez l\'option **<img src="images/Draft_NewLayer.svg" width=16px> Ajouter un nouveau calque** dans le menu contextuel.
2.  S\'il n\'existe pas, le conteneur de calque est créé en premier.
3.  Un calque est créé et placé dans le conteneur de calque.
4.  Si vous le souhaitez, vous pouvez modifier les [propriétés](#Propri.C3.A9t.C3.A9s.md) du calque.
5.  Optionnellement, vous pouvez placer des objets dans le calque en les glissant et en les déposant sur le calque dans la [vue en arborescence](Tree_view/fr.md). Les objets peuvent également être placés dans un calque en modifiant la propriété **Group** du calque.
6.  Vous pouvez également [activer](#Options_du_calque.md) le calque.



## Menu contextuel 



### Options du conteneur du calque 

Pour un Draft LayerContainer, ces options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :

-    **<img src="images/Draft_Layer.svg" width=16px> Fusionner les calques en double**: fusionne toutes les calques ayant la même étiquette de base.

:   L\'étiquette de base d\'un calque est son étiquette **Label** débarrassée des chiffres et des espaces de fin. Tous les calques avec la même étiquette de base sont fusionnés en un seule calque avec **Label** défini à cette étiquette de base.

-    **<img src="images/Draft_NewLayer.svg" width=16px> Ajouter un nouveau calque**: ajoute un nouveau calque au document en cours.



### Options du calque 

Pour un Draft Calque, ces options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :

-    **<img src="images/button_right.svg" width=16px> [Activer ce calque](Draft_AutoGroup/fr.md)**: active le calque sélectionné.

-    **<img src="images/Draft_SelectGroup.svg" width=16px> [Sélectionner le contenu du calque](Draft_SelectGroup/fr.md)**: active le calque sélectionné.



## Comportement du glisser-déposer 


{{Version/fr|0.21}}

Si vous déposez un objet d\'un [Std Groupe](Std_Group/fr.md), ou un objet de type groupe tel qu\'un [Arch Partie de bâtiment](Arch_BuildingPart/fr.md), sur un calque dans la [vue en arborescence](Tree_view/fr.md), il n\'est pas retiré du groupe, et vice versa. Pour retirer un objet d\'un calque, il doit être déposé sur un autre calque ou sur le nœud du document. Il n\'est pas nécessaire de maintenir la touche **Ctrl** enfoncée lorsque vous faites glisser ou déposez un objet sur un calque.



## Remarques

-   Un nouveau calque peut également être créée avec la commande [Draft Groupement automatique](Draft_AutoGroup/fr.md).
-   L\'[atelier BIM](BIM_Workbench/fr.md) offre un [outil de gestion des calques](BIM_Layers/fr.md) complet qui sera éventuellement inclus dans l\'[atelier Draft](Draft_Workbench/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Calque est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Layer}}

-    **Group|LinkList**: spécifie les objets qui se trouvent à l\'intérieur du calque.



### Vue


{{TitleProperty|Layer}}

Les propriétés de cette section sont appliquées aux objets qui sont placés à l\'intérieur du calque. Toute modification de ces propriétés leur est propagée. Pour deux propriétés, **Line Color** et **Shape Color**, ce comportement est facultatif.

-    **Draw Style|Enumeration**: spécifie le style de dessin du calque : {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}} ou {{value|Dashdot}}.

-    **Line Color|Color**: spécifie la couleur de la ligne du calque.

-    **Line Width|Float**: spécifie la largeur de ligne de la couche.

-    **Override Line Color Children|Bool**: indique si les modifications apportées à **Line Color** du calque sont propagées aux objets situés à l\'intérieur du calque.

-    **Override Shape Color Children|Bool**: spécifie si les modifications apportées à **Shape Color** du calque sont propagées aux objets situés dans le calque.

-    **Shape Color|Color**: spécifie la couleur de la forme du calque.

-    **Transparency|Percent**: spécifie la transparence du calque.


{{TitleProperty|Print}}

-    **Line Print Color|Color**: spécifie la couleur d\'impression des lignes du calque.

-    **Use Print Color|Bool**: indique si la **Line Print Color|** du calque est utilisée lorsqu\'une [TechDraw Vue d\'un objet Draft](TechDraw_DraftView/fr.md) est créée à partir des objets contenus dans le calque.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft Calque, utilisez la méthode `make_layer` du module Draft. Pour ajouter des objets à un calque ou en supprimer, modifiez sa propriété `Group`.


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Layer/fr
