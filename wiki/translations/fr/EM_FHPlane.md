---
 GuiCommand:
   Name: EM FHPlane
   Name/fr: EM Plan FH
   MenuLocation: EM , FHPlane
   Workbenches: EM_Workbench/fr
   Shortcut: **E** **P**
   Version: 0.17
   SeeAlso: EM_FHNode/fr, EM_FHPlaneHole/fr, EM_FHPlaneAddRemoveNodeHole/fr
---

# EM FHPlane/fr

## Description

L\'outil Plan FH insère un objet de type plan conducteur uniforme FastHenry.

![](images/EM_FHPlane_Example.png )



*Plan FH FastHenry*



## Utilisation

L\'objet Plan FH doit être basé sur un autre objet, qui peut être un objet [Draft Rectangle](Draft_Rectangle/fr.md) ou un objet [Part Cube](Part_Box/fr.md). Si vous avez basé votre FHPlane sur un objet [Part Cube](Part_Box/fr.md), le paramètre Thickness sera hérité de la valeur Box Height.

1.  Créez et sélectionnez un objet <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou un objet <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Cube](Part_Box/fr.md).
2.  Appuyez sur le bouton **<img src="images/EM_FHPlane.svg" width=16px> [EM FHPlane](EM_FHPlane/fr.md)** ou appuyez sur les touches **E** puis **P**.

De plus, vous pouvez également sélectionner conjointement avec l\'objet de base ([Draft Rectangle](Draft_Rectangle/fr.md) ou [Part Cube](Part_Box/fr.md)) également un ou plusieurs [EM Noeud FH](EM_FHNode/fr.md) et/ou un ou plus [EM Trou FH](EM_FHPlaneHole/fr.md) qui seront adoptés par le Plan FH :

1.  Créez un objet [Draft Rectangle](Draft_Rectangle/fr.md) ou [Part Box](Part_Box/fr.md)
2.  Créez un ou plusieurs objets <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [EM Noeud FH](EM_FHNode/fr.md)
3.  Créez un ou plusieurs objets <img alt="" src=images/EM_FHPlaneHole.svg  style="width:16px;"> [EM Trou FH](EM_FHPlaneHole/fr.md)
4.  Sélectionnez l\'objet de base, les objets Noeud FH et les objets Plan FH (pour cette sélection multiple, vous pouvez pointer et cliquer sur les objets dans la [vue en arborescence](Tree_view/fr.md) ou dans la [vue 3D](3D_view/fr.md) et pour effectuer une sélection multiple maintenez simplement la touche **CTRL** enfoncée lors de la sélection).
5.  Appuyez sur le bouton **<img src="images/_EM_FHPlane.svg" width=16px> [EM Plan FH](EM_FHPlane/fr.md)** ou appuyez sur les touches **E** puis **P**.



### Remarques :

Un objet plan conducteur uniforme FastHenry est formé en posant une ceinture de nœuds (ci-après appelés « nœuds internes ») et en connectant les nœuds avec un maillage 2D de segments dans les directions (relatives) X et Y. Des trous sont formés dans le plan en supprimant certains nœuds internes, et donc également les segments qui se connectent à ces nœuds. Pour plus de détails sur les plans conducteurs uniformes FastHenry, consultez le [guide de l\'utilisateur FastHenry](https://www.fastfieldsolvers.com/documentation.htm).

-   Comme l\'objet Plan FH est basé sur un objet Draft Rectangle ou Part Cube, vous ne pouvez PAS déplacer librement le FHPlane. Le FHPlane sera toujours contraint à l\'objet de base. Pour modifier la position du FHPlane, appliquez la modification à l\'objet de base sous-jacent (l\'objet de base est masqué par défaut, vous pouvez l\'afficher à nouveau en sélectionnant l\'objet dans l\'arborescence et en appuyant sur **Espace**. L\'origine de le FHPlane est l\'origine de l\'objet de base.

-   Lorsque les objets Noeud FH sont adoptés par le Plan FH, leurs coordonnées (X, Y, Z) seront faites par rapport à l\'origine du FHPlane (ainsi, alors que le FHNode conservera la même position dans l\'espace, les coordonnées relatives (X, Y, Z ) du FHNode sera modifié pour être relatif à l\'origine du FHPlane). De plus, une fois adoptée, la coordonnée Z du FHNode sera remise à zéro (car les coordonnées sont relatives au FHPlane, la coordonnée Z est la hauteur de l\'objet par rapport au plan). Pour cette raison, le nœud ne sera visible que depuis le bas du FHPlane, ou en modifiant la transparence du FHPlane pour voir les FHNodes à travers, ou en masquant complètement le FHPlane. De plus, pour montrer que le FHNode appartient désormais au FHPlane, la couleur du FHNode est modifiée.

-   Lorsque les objets Trous FH (FHPlaneHole) sont adoptés par le Plan FH, leurs coordonnées (X, Y, Z) seront établies par rapport à l\'origine du FHPlane (ainsi, alors que le FHPlaneHole conservera la même position dans l\'espace, les coordonnées relatives (X, Y, Z ) du FHPlaneHole sera modifié pour être relatif à l\'origine du FHPlane). De plus, une fois adoptée, la coordonnée Z du FHPlaneHole sera remise à zéro (car les coordonnées sont relatives au FHPlane, la coordonnée Z est la hauteur de l\'objet par rapport au plan). Pour cette raison, le nœud ne sera visible que depuis le bas du FHPlane, ou en modifiant la transparence du FHPlane pour voir les FHNodes à travers, ou en masquant complètement le FHPlane. De plus, pour montrer que le FHNode appartient désormais au FHPlane, la couleur du FHNode est modifiée.

-   Si vous souhaitez supprimer les FHNodes ou les FHPlaneHoles du FHPlane ultérieurement, vous pouvez utiliser la commande [EM Bascule noeud trou FH](EM_FHPlaneAddRemoveNodeHole/fr.md).



## Propriétés

-    **Base**: l\'objet de base sur lequel ce composant est construit (un [Draft Rectangle](Draft_Rectangle/fr.md) ou un [Part Cube](Part_Box/fr.md))

-    **Thickness**: l\'épaisseur du Plan FH (paramètre de plan « épais » dans FastHenry). Si le Plan FH est basé sur un [Part Cube](Part_Box/fr.md), cette valeur est héritée du paramètre Part Box Height

-    **seg1**: le nombre de segments le long de la direction de la longueur (paramètre de plan \'seg1\' dans FastHenry)

-    **seg2**: le nombre de segments le long de la direction de la largeur (paramètre de plan \'seg2\' dans FastHenry)

-    **nhinc**: le nombre de filaments de l\'épaisseur du plan (paramètre plan \'nhinc\' dans FastHenry)

-    **rh**: le rapport des filaments adjacents le long de l\'épaisseur (paramètre du plan \'rh\' dans FastHenry)

-    **Sigma**: la conductivité du Plan FH (paramètre du plan \'sigma\' dans FastHenry)

-    **segwid1**: la largeur des segments le long de la direction de la longueur du plan (paramètre plan \'segwid1\' dans FastHenry)

-    **segwid2**: la largeur des segments le long de la direction de largeur du plan (paramètre plan \'segwid2\' dans FastHenry)

-    **Nodes**: la liste des objets Noeuds FH pour les connexions au plan

-    **Holes**: la liste des Trous FH dans le plan

-    **FineMesh**: spécifie si le maillage fin plan est affiché (c\'est-à-dire la composition des segments)

-    **ShowNodes**: affiche la grille de nœuds internes supportant le plan (c\'est-à-dire les nœuds internes)



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Plan FH peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
plane = makeFHPlane(baseobj=None, thickness=None, seg1=None, seg2=None, nodes=[], holes=[], name='FHPlane')
```

-   Crée un objet `FHPlane`.

-    `baseobj`est l\'objet Draft Rectangle ou l\'objet Part Cube qui peut être utilisé comme base pour le Plan FH. Si aucun `baseobj` n\'est donné, l\'utilisateur doit attribuer un objet de base ultérieurement, pour pouvoir utiliser cet objet.

-    `thickness`est l\'épaisseur du plan. Si `baseobj` est un Part Cube, ce paramètre est ignoré et la hauteur de Part Cube est utilisée à la place. La valeur par défaut est `EMFHPLANE_DEF_THICKNESS`.

-    `seg1`est un entier définissant le nombre de segments le long de la dimension x du plan (paramètre \'seg1\' dans FastHenry).

-    `seg2`est un entier définissant le nombre de segments le long de la dimension x du plan (paramètre \'seg2\' dans FastHenry).

-    `nodes`est un tableau d\'objets Noeud FH, spécifiant les nœuds qui seront adoptés par le plan.

-    `holes`est un tableau d\'objets Trous FH, spécifiant les trous qui seront adoptés par le plan.

-    `name`est le nom de l\'objet.

Exemple :


```python
import FreeCAD, Draft, EM

pl = FreeCAD.Placement()
pl.Rotation.Q = (0.0,0.0,0.0,1.0)
pl.Base = FreeCAD.Vector(1.0,1.0,0.0)
rec = Draft.makeRectangle(length=10.0,height=5.0,placement=pl,face=True,support=None)

fhnode1 = EM.makeFHNode(X=1.0,Y=3.5,Z=0)
fhnode2 = EM.makeFHNode(X=8.0,Y=3.5,Z=0)

hole = EM.makeFHPlaneHole(X=6.0,Y=3.5,Z=0.0)

fhplane = EM.makeFHPlane(rect, thickness=1.0, seg1=15, seg2=15, nodes=[fhnode1, fhnode2], holes=[hole])
```





{{EM Tools navi

}}



---
⏵ [documentation index](../README.md) > [EM](Category_EM.md) > EM FHPlane/fr
