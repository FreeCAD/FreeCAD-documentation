---
- GuiCommand:/fr
   Name:Std LinkMakeRelative
   Name/fr:Std Créer un sous-lien
   MenuLocation:Aucun
   Workbenches:Tous
   Version:0.19
   SeeAlso:[Std Part](Std_Part/fr.md), [Std Groupe](Std_Group/fr.md), [Std Créer un lien](Std_LinkMake/fr.md)
---

# Std LinkMakeRelative/fr

## Description


**[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std Créer un sous-lien](Std_LinkMakeRelative/fr.md)**

crée un [App Link](App_Link/fr.md) (classe `App::Link`), tout comme **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)** mais il fonctionne d\'abord sur les sous-éléments sélectionnés et définit {{PropertyData/fr|Link Transform}} sur {{TRUE }}.

## Utilisation

Avec sélection :

1.  Sélectionnez un sous-élément dans la [Vue 3D](3D_view/fr.md), cela signifie un sommet, une arête ou une face, ou toute combinaison de ceux-ci. Ces sous-éléments doivent appartenir à un seul objet.
2.  Appuyez sur le bouton **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Std Créer un sous-lien](Std_LinkMakeRelative/fr.md)**. L\'objet crée a la même icône que l\'objet d\'origine mais a deux flèches superposées indiquant qu\'il s\'agit d\'un lien relatif.

Sans sélection :

-   Si aucun objet n\'est sélectionné, cette commande ne fait rien.
-   Si un objet est sélectionné uniquement dans la [Vue en arborescence](Tree_view/fr.md), mais qu\'aucun sous-élément n\'est sélectionné dans la [Vue 3D](3D_view/fr.md), la commande ne fait rien non plus.

<img alt="" src=images/Std_Link_tree_sublink_example.png ) ![](images/Std_Link_sublink_example.png  style="width:500px;">



*Corps d'origine et trois liens créés à partir de ses sous-éléments, y compris les arêtes et les faces.*

## Propriétés

Cette commande crée un nouveau [App Link](App_Link/fr.md). Ses propriétés sont décrites dans **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std Créer un lien](Std_LinkMake/fr.md)**.

En particulier, {{PropertyData/fr|Link Transform}} est défini sur `True`, donc {{PropertyData/fr|Placement}} devient masqué et à la place {{PropertyData/fr|Link Placement}} contrôle la position du lien par rapport à la position de {{PropertyData/fr|Linked Object}}.

## Script

Voir [Std Créer un lien](Std_LinkMake/fr.md) pour les informations générales.

Un App Link est créé avec la méthode `addObject()` du document. Pour définir un lien relatif, sa méthode `setLink` est utilisée pour sélectionner l\'objet source et un ou plusieurs de ses sous-éléments. Ensuite, l\'attribut `LinkTransform` est défini sur `True`.


```python
import FreeCAD as App

doc = App.newDocument()
body = App.ActiveDocument.addObject("Part::Box", "Box")

obj = App.ActiveDocument.addObject("App::Link", "Link")
obj.setLink(body, '', ['Edge1', 'Edge6', 'Edge7', 'Edge10', 'Face2', 'Face3'])
obj.LinkTransform = True
obj.LinkPlacement.Base = App.Vector(20, 20, 0)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkMakeRelative/fr
