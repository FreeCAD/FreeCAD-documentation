---
- GuiCommand:
   Name:Draft Trimex
   Name/fr:Draft Ajuster ou prolonger
   MenuLocation:Modification → Ajuster ou Prolonger
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**T** **R**
   SeeAlso:[Part Extrusion](Part_Extrude/fr.md)
---

# Draft Trimex/fr

## Description

La commande <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> **Draft Ajuster ou prolonger** [ajuste ou prolonge](#Ajuste_ou_prolonge.md) un objet sélectionné. Les intersections avec le bord d\'un autre objet peuvent être utilisées pour déterminer de nouveaux points d\'extrémité. La commande peut également être utilisée pour une [extrusion](#Extrusion.md) d\'une face, auquel cas elle crée un objet [Part Extrusion](Part_Extrude/fr.md).

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*En haut : une Draft polyligne étendue puis ajustée.<br>En bas : une face extrudée dans un corps solide.*



## Ajuste ou prolonge 



### Utilisation

1.  Sélectionnez un objet. L\'objet doit être une [Draft Ligne](Draft_Line/fr.md), une [Draft Polyligne](Draft_Wire/fr.md), un [Draft Arc](Draft_Arc/fr.md) ou un [Draft Cercle](Draft_Circle/fr.md) (qui ne peuvent être que ajustés). Si l\'objet sélectionné est fermé, sa propriété **Make Face** doit être définie sur `False`.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Trimex.svg" width=16px> [Ajuster ou Prolonger](Draft_Trimex/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Trimex.svg" width=16px> Ajuster ou Prolonger** dans le menu.
    -   Utilisez le raccourci clavier : **T** puis **R**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [vue 3D](3D_view/fr.md).
4.  Le panneau de tâches **Ajuster ou Prolonger** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  Déplacez le pointeur dans la [vue 3D](3D_view/fr.md) de sorte que l\'aperçu corresponde au résultat souhaité. Si nécessaire, utilisez les touches de modification comme expliqué dans la section [Options](#Options.md).
6.  Effectuez l\'une des opérations suivantes :
    -   Choisissez un point dans la [vue 3D](3D_view/fr.md).
    -   Saisissez une **Distance** ou un **Angle**. La distance est une distance relative. Cette option ne fonctionne pas si des touches modificatrices sont utilisées.
    -   Déplacez le pointeur sur une arête appartenant à un autre objet, et cliquez lorsque cette arête est mise en surbrillance, pour couper ou étendre l\'objet sélectionné en utilisant une intersection avec l\'arête mise en surbrillance comme nouveau point d\'arrivée. Lors de l\'ajustement, la projection du point où l\'arête de coupe est sélectionnée sur l\'objet à ajuster, détermine le résultat par défaut. Notez que les [Draft Aimantations](Draft_Snap/fr.md) peuvent avoir un impact indésirable ici. Dans certains cas, il peut être utile de les désactiver temporairement.

### Options

Le raccourci clavier à caractère unique et les touches de modification mentionnées ici peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md).

-   Maintenez la touche **Alt** enfoncée pour inverser le résultat par défaut de la commande.
-   Maintenez la touche **Shift** enfoncée pour limiter l\'opération au segment en cours d\'une [Draft Polyligne](Draft_Wire/fr.md).
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).

Voici un exemple pour expliquer les touches de modification. Le bord gauche ou le bord inférieur du polyligne en U a été prolongé. Toutes les [Draft Aimantations](Draft_Snap/fr.md) ont été désactivées.

![](images/Draft_Trimex_example2.png )

1.  L\'arc a été cliqué près du coin inférieur gauche de la polyligne. C\'est le résultat par défaut.

2.  
    **Alt**a été maintenu enfoncé pendant que l\'arc était cliqué près du coin inférieur gauche de la polyligne.

3.  
    **Y**est appuyée, et en survolant le bord gauche, vous maintenez la touche **Shift** enfoncée, puis vous cliquez sur l\'arc. Il n\'est nécessaire d\'appuyer sur **Y** que pour les arêtes qui sont plus ou moins parallèles à l\'axe des Y.



## Extrusion



### Utilisation 

Voir aussi : [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il peut être utile de modifier d\'abord le [Draft Plan de travail](Draft_SelectPlane/fr.md) pour qu\'il ne soit pas coplanaire avec la face que vous voulez extruder.
2.  Vous pouvez sélectionner une seule face ou un objet avec une seule face.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Trimex.svg" width=16px> [Ajuster ou Prolonger](Draft_Trimex/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Trimex.svg" width=16px> Ajuster ou Prolonger** dans le menu.
    -   Utilisez le raccourci clavier : **T** puis **R**.
4.  Si vous n\'avez pas encore sélectionné un objet ou une face : sélectionnez un objet avec une seule face dans la [Vue 3D](3D_view/fr.md).
5.  Le panneau de tâches **Ajuster ou Prolonger** s\'ouvre. Voir [Options](#Options_2.md) pour plus d\'informations.
6.  Pour définir la direction et la distance d\'extrusion, effectuez l\'une des opérations suivantes :
    -   Choisissez un point dans la [Vue 3D](3D_view/fr.md) qui ne se trouve pas sur le même plan que la face.
    -   Assurez-vous que le pointeur se trouve du bon côté de la face dans la [Vue 3D](3D_view/fr.md) et entrez une **Distance**.

### Options 

Les touches de modification mentionnées ici peuvent être modifiées. Voir [Draft Préférences](Draft_Preferences/fr.md).

-   Maintenez **Shift** pour extruder dans une direction qui n\'est pas parallèle à la normale de la face.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie de la distance : **Édition → Préférences... → Général → Unités → Réglage des unités → Nombre de décimales**.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Il n\'existe pas de méthode Python pour extruder des objets. Pour extruder des objets, utilisez la méthode `extrude` du module Draft.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`est l\'objet à extruder.

-    `vector`est la direction et la distance d\'extrusion.

-   Si `solid` est `True`, un solide est créé au lieu d\'une coquille.

-    `extrusion`est retourné avec l\'objet créé.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/fr
