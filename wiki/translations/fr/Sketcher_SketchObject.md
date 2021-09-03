

## Introduction

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Un [Sketcher SketchObject](Sketcher_SketchObject/fr.md), ou formellement un `Sketcher::SketchObject`, est l\'élément de base pour créer des objets 2D avec l\'[Atelier Sketcher](Sketcher_Workbench/fr.md).


`Sketcher::SketchObject`

est dérivé de [Part Part2DObject](Part_Part2DObject/fr.md). Cela signifie qu\'il s\'agit d\'un objet [Part Feature](Part_Feature/fr.md) spécialisé dans la géométrie 2D. Comme Part2DObject, l\'objet SketchObject peut être attaché à des plans et à des faces. En plus de cela, SketchObject peut gérer les contraintes géométriques des lignes et des courbes qui y sont dessinées.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Schéma simplifié des relations entre les objets principaux dans FreeCAD. La classe `Sketcher::SketchObject* est spécialisée pour les formes 2D et comprend en plus une extension pour gérer les contraintes géométriques de ses éléments.`

## Utilisation

1.  Basculez vers l\'[Atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Appuyez sur **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)**.
3.  Sélectionnez une {{MenuCommand/fr|Orientation de l'esquisse}}: plan XY, plan XZ ou plan YZ. Vous pouvez également choisir d\'{{MenuCommand/fr|Inverser la direction}} et donner une valeur de {{MenuCommand/fr|Décalage}}.
4.  Appuyez sur **OK**.

Bien que SketchObject puisse être utilisé seul pour dessiner sur un plan, il est le plus souvent utilisé conjointement avec [Atelier PartDesign](PartDesign_Workbench/fr.md) pour créer des solides extrudés.

1.  Basculer vers le [Atelier PartDesign](PartDesign_Workbench/fr.md).

2.  Appuyez sur **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.

3.  Appuyez sur **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)**.

4.  
    {{MenuCommand/fr|Fonction sélectionnée}}: XY\_Plane (Plan de base), XZ\_Plane (Plan de base) ou YZ\_Plane (Plan de base).

5.  Appuyez sur **OK**.

## Propriétés

Voir [Propriétés](Property/fr.md) pour tous les types de propriétés que les objets scriptés peuvent avoir.

Un [Sketcher SketchObject](Sketcher_SketchObject/fr.md) (classe `Sketcher::SketchObject`) est dérivé de [Part Part2DObject](Part_Part2DObject/fr.md) (classe `Part::Part2DObject`) donc partage toutes les propriétés de ce dernier.

Outre les propriétés décrites dans [Part Part2DObject](Part_Part2DObject/fr.md), l\'objet de base Sketcher SketchObject possède les propriétés suivantes dans l\'[éditeur de propriétés](property_editor/fr.md). Les propriétés masquées peuvent être affichées en utilisant la commande **Show all** dans le menu contextuel de l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Attachment}}

-    {{PropertyData/fr|Map Mode}}, {{PropertyData/fr|Map Reversed}}, {{PropertyData/fr|Attachment Offset}} comme [Part Part2DObject](Part_Part2DObject/fr.md). Voir [Part Ancrage](Part_Attachment/fr.md) pour plus d\'informations sur tous les modes d\'ancrage.


{{TitleProperty|Sketch}}

-    **Constraints|**: les contraintes nommées, si elles existent sinon c\'est une liste vide `[]`.

#### Propriétés cachées de Données 

Voir [Part Part2DObject](Part_Part2DObject/fr.md) pour le reste des propriétés masquées.


{{TitleProperty|Base}}

-    {{PropertyData/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Sketcher_SketchObject/fr#Script.md).


{{TitleProperty|Sketch}}

-    {{PropertyData/fr|Geometry|GeometryList}}: liste des géométries de pièce qui existent à l\'intérieur de l\'esquisse.

-    {{PropertyData/fr|Géométrie externe|LinkSubList}}: liste des géométries de pièce en dehors de cette esquisse qui sont utilisées comme référence.

### Vue


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints|Bool**: si `True`, il essaiera de définir des contraintes lors du tracé de la géométrie.


{{TitleProperty|Visibility automation}}

-    **Editing Workbench|String**: nom du workbench à activer lors de la modification de l\'esquisse. Valeur par défaut {{value|SketcherWorkbench}}.

-    **Hide Dependent|Bool**: si `True`, tous les objets qui dépendent de l\'esquisse sont masqués lors de l\'ouverture de l\'esquisse.

-    **Restore Camera|Bool**: si `True` la position de la caméra est enregistrée avant l\'ouverture de l\'esquisse et est restaurée après sa fermeture.

-    **Show Links|Bool**: si `True`, tous les objets utilisés dans les liens vers une géométrie externe sont affichés lors de l\'ouverture de l\'esquisse.

-    **Show Support|Bool**: si `True` tous les objets auxquels cette esquisse est attachée sont affichés lors de l\'ouverture de l\'esquisse.

#### Propriétés cachées de Vue 


{{TitleProperty|Base}}

-    {{PropertyData/fr|Proxy|PythonObject}}: classe personnalisée associée à cet objet. Cela n\'existe que pour la version [Python](Python/fr.md). Voir [Script](Sketcher_SketchObject/fr#Script.md).


{{TitleProperty|Visibility automation}}

-    {{PropertyView/fr|Tempo Vis|PythonObject}}: classe personnalisée associée à cet objet qui gère le masquage et l\'affichage d\'autres objets lors de l\'ouverture et de la fermeture de l\'esquisse.

Toutes les autres propriétés de vue, y compris les propriétés masquées, sont celles de l\'objet de base [Part Feature](Part_Feature/fr.md)

## Création de scripts 


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md) et [objet scripté](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets au document.

Un SketchObject est créé avec la méthode `addObject()` du document. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObject", "Sketch")
obj.Label = "Custom label"
```

Ce `Sketcher::SketchObject` de base n\'a pas d\'objet Proxy, il ne peut donc pas être entièrement utilisé pour la sous-classification.

Par conséquent, pour la sous-classe [Python](Python/fr.md), vous devez créer l\'objet `Sketcher::SketchObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher Tools navi

}}  {{Document objects navi}} 
