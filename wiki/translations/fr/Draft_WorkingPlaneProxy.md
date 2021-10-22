---
- GuiCommand:/fr
   Name:Draft WorkingPlaneProxy
   Name/fr:Draft Proxy de plan de travail
   MenuLocation:Utilitaires → Créer un proxy de plan de travail
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[Draft Plan de travail](Draft_SelectPlane/fr.md)
---

# Draft WorkingPlaneProxy/fr

## Description

La commande <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:24px;"> **Draft Proxy de plan de travail** crée un proxy de plan de travail pour sauvegarder le [Draft Plan de travail](Draft_SelectPlane/fr.md) en cours. Un proxy proxy de plan de travail peut être utilisé pour restaurer rapidement un plan de travail. La position de la caméra et la visibilité des objets dans la [Vue 3D](3D_view/fr.md) sont également enregistrées dans le proxy de plan de travail et peuvent, [optionnellement](#Propri.C3.A9t.C3.A9s.md), être restaurées également.

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Trois proxy de plan de travail montrant différentes orientations et décalages*

## Utilisation

1.  Optionnellement, changer de [plan de travail](Draft_SelectPlane/fr.md).
2.  Optionnellement, changer de [Vue 3D](3D_view/fr.md).
3.  Optionnellement, changer l\'état de visibilité des objets dans le document.
4.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_WorkingPlaneProxy.svg" width=16px> [Créer un proxy de plan de travail](Draft_WorkingPlaneProxy.md)** bouton.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Créer un proxy de plan de travail** dans le menu.
5.  Un proxy de plan de travail est créé.
6.  Pour aligner le [plan de travail](Draft_SelectPlane/fr.md) avec un proxy de plan de travail, double-cliquez sur le proxy de plan de travail dans la [Vue en arborescence](Tree_view/fr.md) ou utilisez-le avec la commande [Draft Plan de travail](Draft_SelectPlane/fr.md).

## Menu contextuel 

Pour un Draft Proxy de plan de travail, ces options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**: met à jour la propriété {{PropertyView/fr|View Data}} du proxy de plan de travail avec les paramètres actuels de la caméra [3D view](3D_view.md).

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**: met à jour la propriété {{PropertyView/fr|Visibility Map}} du proxy de plan de travail avec l\'état de visibilité actuel des objets dans le document.

## Remarques

-   Les proxies de plan de travail peuvent être _ pour s\'aimanter à leur point de {{PropertyData/fr|Placement}}.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Proxy de plan de travail est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Placement|Placement}}: spécifie la position du proxy de plan de travail dans la [Vue 3D](3D_view/fr.md). Voir [Placement](Placement/fr.md).

-    {{PropertyData/fr|Shape|Shape|Hidden}}: spécifie la forme du proxy de plan de travail.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Line Color|Color}}: spécifie la couleur de tous les éléments du proxy de plan de travail.

-    {{PropertyView/fr|Line Width|Float}}: spécifie la largeur de ligne des axes et des symboles de flèches.

-    {{PropertyView/fr|Restore State|Bool}}: spécifie si la {{PropertyView/fr|Visibility Map}} est restaurée lorsque le [plan de travail](Draft_SelectPlane/fr.md) est aligné avec le proxy de plan de travail.

-    {{PropertyView/fr|Restore View|Bool}}: spécifie si la {{PropertyView/fr|View Data}} est restaurée lorsque le [plan de travail](Draft_SelectPlane.md) est aligné sur le proxy de plan de travail.

-    {{PropertyView/fr|Transparency|Percent}}: spécifie la transparence de la face du proxy de plan de travail.

-    {{PropertyView/fr|View Data|FloatList}}: spécifie la position et les paramètres de la caméra.

-    {{PropertyView/fr|Visibility Map|Map|Hidden}}: spécifie l\'état de visibilité des objets.


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Arrow Size|Length}}: spécifie la taille des symboles de flèche affichés à l\'extrémité des trois axes.

-    {{PropertyView/fr|Display Size|Length}}: spécifie la longueur et la largeur du proxy de plan de travail.

## Script

Voir aussi: _.

Pour créer un Draft Proxy de plan de travail, utilisez la méthode `make_workingplaneproxy` du module Draft.

Si l\'[atelier Draft](Draft_Workbench/fr.md) est actif, l\'objet de l\'application FreeCAD possède une propriété `DraftWorkingPlane` qui stocke le plan de travail en cours. Le {{Incode|Placement}} de la méthode {{Incode|getPlacement}} de l\'objet `DraftWorkingPlane` peut être utilisé pour créer un proxy de plan de travail aligné. Le {{Incode|Placement}} d\'un proxy de plan de travail peut à son tour être utilisé pour réaligner le plan de travail.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

workplane = App.DraftWorkingPlane
place = workplane.getPlacement()

proxy = Draft.make_workingplaneproxy(place)
proxy.ViewObject.DisplaySize = 3000
proxy.ViewObject.ArrowSize = 200

axis2 = App.Vector(1, 1, 1)
point2 = App.Vector(3000, 0, 0)
place2 = App.Placement(point2, App.Rotation(axis2, 90))

proxy2 = Draft.make_workingplaneproxy(place2)
proxy2.ViewObject.DisplaySize = 3000
proxy2.ViewObject.ArrowSize = 200

workplane.setFromPlacement(proxy2.Placement, rebase=True)
Gui.Snapper.setGrid()

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/fr
