# Selection view/fr
## Introduction




La [Fenêtre de sélection](selection_view/fr.md) est un panneau dans l\'[interface](interface/fr.md) par défaut situé sous la [Vue combinée](combo_view/fr.md). Tout comme l\'[Éditeur de propriétés](property_editor/fr.md), il affiche plus d\'informations sur les objets actuellement sélectionnés.

Une sélection peut être effectuée en choisissant un objet dans la [Vue 3D](3D_view/fr.md) ou dans la [Vue d\'arborescence](tree_view/fr.md). Plusieurs corps peuvent être sélectionnés en maintenant **Ctrl**.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Vue de sélection indiquée par le numéro 5 dans l'[interface](interface/fr.md) standard.*

## Sélection d\'objets 

L\'arborescence de cet exemple comporte deux [PartDesign Corps](PartDesign_Body/fr.md), avec plusieurs fonctionnalités chacune, et un simple [Part Cône](Part_Cone/fr.md). L\'arbre est comme suit.

![](images/FreeCAD_Selection_Tree_view.png )

La vue de sélection est vide si aucun objet n\'est sélectionné dans la [Vue 3D](3D_view/fr.md) ou dans la [Vue en arborescence](tree_view/fr.md).

<img alt="" src=images/FreeCAD_Selection_view_empty.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_empty_3D.png  style="width:" height="286px;">

Si vous sélectionnez un objet, il apparaîtra dans la liste d\'objets, avec le document auquel il appartient. Le `Name` interne en lecture seule et le `Label` modifiable par l\'utilisateur seront affichés.


`Name`

ne peut contenir que des caractères alphanumériques de base `[_0-9a-zA-Z]`, tandis que `Label` peut contenir n'importe quel symbole, y compris les espaces et les caractères accentués. 
```python
Document#Name (Label)
```

<img alt="" src=images/FreeCAD_Selection_view_one_object.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_one_object_3D.png  style="width:" height="286px;">

Si vous sélectionnez différents objets, ils seront listés dans la vue. Si ces objets sont situés dans un type de conteneur, par exemple, un [PartDesign Corps](PartDesign_Body/fr.md), le nom affiché sera attribué de manière hiérarchique, à savoir, `Document#Parent.Child` . Dans ce cas, non seulement l\'enfant, mais tout le parent apparaîtra en surbrillance dans la vue 3D. 
```python
Document#Body.Feature. (Feature_label)
```

<img alt="" src=images/FreeCAD_Selection_view_many_objects.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_many_objects_3D.png  style="width:" height="286px;">

Vous pouvez sélectionner des éléments de corps individuels, c\'est-à-dire des sommets, des arêtes et des faces, qui seront également affichés de manière hiérarchique. 
```python
Document#Body.Feature.Vertex (Feature_label)
Document#Body.Feature.Edge (Feature_label)
Document#Body.Feature.Face (Feature_label)
```

<img alt="" src=images/FreeCAD_Selection_view_many_objects_subelements.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_many_objects_subelements_3D.png  style="width:" height="286px;">

## Barre de recherche 

Si votre document contient de nombreux objets et que vous ne pouvez pas choisir celui que vous souhaitez dans la [Vue 3D](3D_view/fr.md) ou dans la [Vue en arborescence](tree_view/fr.md), vous pouvez écrire le nom partiel de l\'objet dans le champ de recherche. Il recherchera tous les noms dans le document et affichera une liste de ceux qui correspondent partiellement au texte que vous avez entré. Lorsque vous trouvez l\'objet que vous recherchez, vous pouvez cliquer dessus pour le sélectionner.

## Actions

Un clic droit sur un élément de la liste appelle diverses commandes.

-    **Select only**: désélectionne tout et sélectionne uniquement l\'objet parent qui contient l\'élément donné.

-    **Deselect**: supprime complètement la sélection de tous les objets.

-    **Zoom to fit**: désélectionne tout et ne sélectionne que l\'objet parent qui contient l\'élément donné. De plus, la [vue 3D](3D_view/fr.md) est panoramique et zoomée de sorte que l\'objet parent soit centré sur l\'écran. Ceci est utile lorsque vous sélectionnez un objet dans la vue arborescente, puis faites une mise au point rapide de la caméra sur la vue 3D.

-    **Go to selection**: désélectionne tout et ne sélectionne que l\'objet parent qui contient l\'élément sélectionné. Dans ce cas, la [vue en arborescence](tree_view/fr.md) est ajustée et développée pour montrer exactement où se trouve l\'objet sélectionné dans l\'arborescence. Ceci est utile lorsque les objets de la vue 3D sont contenus dans de nombreux objets conteneurs de la vue arborescente, par exemple, [Std Parts](Std_Part/fr.md), [Std Groupes](Std_Group/fr.md), [PartDesign Corps](PartDesign_Body/fr.md), [Arch Partie de bâtiment](Arch_BuildingPart/fr.md) et semblables. Lorsque vous avez des centaines de corps, il est plus facile de sélectionner l\'objet dans la vue 3D, puis de choisir {{MenuCommand | Aller à la sélection}} pour localiser immédiatement l\'objet dans la vue arborescente, puis de modifier ses propriétés dans le [Editeur de propriétés](Property_editor/fr.md).

-    **Mark to recompute**: marque l\'objet sélectionné comme \"touché\", ce qui signifie que ses propriétés seront mises à jour lors de la prochaine opération sur le document [recalculé](Std_Refresh/fr.md).

-    **To Python console**: ceci crée une variable `obj` qui contient une référence à l\'objet parent. Cela est utile pour écrire des scripts et tester des commandes dans la [console Python](Python_console/fr.md). Au lieu d\'utiliser le nom complet de l\'objet, il est plus facile d\'utiliser le nom plus court et plus compact `obj`.

## Objet sélectionné 

Depuis la v0.19, la case **picked object list** est disponible. Si cette case est cochée, une liste secondaire apparaîtra montrant tous les sous-éléments (sommets, arêtes et faces) qui pourraient être sélectionnés en un seul clic, même ceux qui sont derrière (masqués par) d\'autres objets.

<img alt="" src=images/FreeCAD_Selection_view_pick_hidden.png  style="width:" height="300px;"> <img alt="" src=images/FreeCAD_Selection_view_pick_hidden_3D.png  style="width:" height="300px;">


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Selection view/fr
