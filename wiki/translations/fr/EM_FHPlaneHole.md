---
- GuiCommand:/fr
   Name:EM FHPlaneHole
   Name/fr:EM FHPlaneHole
   MenuLocation:EM → FHPlaneHole
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:**E** **H**
   SeeAlso:[EM FHPlane](EM_FHPlane/fr.md), [EM FHNode](EM_FHNode/fr.md), [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md)
   Version:0.17
---

# EM FHPlaneHole/fr

## Description

L\'outil FHPlaneHole insère un objet de trou plan qui représente un trou plan conducteur uniforme FastHenry.

![](images/EM_point_FHPlaneHole_Example.png ) 
*FastHenry Point FHPlaneHole* ![](images/EM_rect_FHPlaneHole_Example.png ) 
*FastHenry Rectangle FHPlaneHole* ![](images/EM_circle_FHPlaneHole_Example.png ) 
*FastHenry Cercle FHPlaneHole*

## Utilisation

L\'objet FHPlaneHole peut être basé sur la position d\'un objet [Draft Point](Draft_Point/fr.md) ou vous pouvez sélectionner l\'emplacement 3D du FHNode.

1.  Appuyez sur la touche **<img src="images/EM_FHPlaneHole.svg" width=16px> [EM FHPlaneHole](EM_FHPlaneHole/fr.md)** ou appuyez sur la touche **E** puis **H**.
2.  Cliquez sur un point de la vue 3D ou tapez les coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> [Draft Ajouter un point](Draft_AddPoint/fr.md)**.

Alternativement, vous pouvez également:

1.  Sélectionnez un ou plusieurs [Draft Point](Draft_Point/fr.md) objet(s)
2.  Appuyez sur le bouton **<img src="images/EM_FHPlaneHole.svg" width=16px> [/fr|EM FHPlaneHole](EM_FHPlaneHole.md)** ou appuyez sur les touches **E** puis **H**. Autant de FHPlaneHole seront créés que les objets Draft Point, aux mêmes coordonnées que les Draft Points.

### Remarques

-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:16px;"> Les objets FHPlaneHole n\'ont aucune signification s\'ils ne font pas partie d\'un <img alt="" src=images/EM_FHPlane.svg  style="width:16px;"> _ ou sélectionnez le FHPlaneHole lors de la création de [FHPlane](EM_FHPlane/fr.md). Pour supprimer un FHPlaneHole d\'un FHPlane, vous pouvez utiliser la commande [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md).

-   Les objets FHPlaneHole représentent des trous plans FastHenry et suivent donc les mêmes règles que les trous plans conducteurs uniformes. En particulier, des trous sont créés en supprimant les nœuds plans internes du réseau de nœuds plans, avant de construire le maillage de segment. Vous pouvez activer la vue des nœuds FHPlane internes en activant la propriété [FHPlane](EM_FHPlane/fr.md) **ShowNodes**. Il existe trois types de FHPlaneHoles et peuvent être sélectionnés en modifiant la propriété **Type** FHPlaneNode.

1.  Trou de point: supprime le nœud interne FHPlane unique plus près de la position du FHPlaneHole. Le point FHPlaneHole est représenté comme un seul sommet (petit point), pour aider à visualiser sa position; voir l\'image FastHenry Point FHPlaneHole ci-dessus.
2.  Trou rectangle: supprime tous les nœuds internes FHPlane qui se trouvent à l\'intérieur ainsi qu\'à proximité de la zone définie par le point de base du FHPlaneNode et les propriétés **Length** et **Width**. Cela signifie que non seulement les nœuds internes strictement dans la zone rectangulaire définie par le FHPlaneHole sont supprimés, mais aussi les nœuds internes à l\'extérieur du rectangle, mais à l\'intérieur de la moitié de la distance nœud interne - nœud. Le Rectangle FHPlaneHole est montré comme un rectangle 2D, pour aider à visualiser sa position et sa zone; voir l\'image FastHenry Rect FHPlaneHole ci-dessus.
3.  Trou de cercle: supprime tous les nœuds internes FHPlane qui se trouvent à l\'intérieur ainsi qu\'à proximité de la zone définie par le point de base du FHPlaneNode et la propriété **Radius**. Cela signifie que non seulement les nœuds internes strictement dans la zone circulaire définie par le FHPlaneHole sont supprimés, mais également les nœuds internes à l\'extérieur du cercle, mais à moins de la moitié de la distance nœud interne - nœud. Le Circle FHPlaneHole est montré comme un cercle 2D, pour aider à visualiser sa position et sa zone; voir l\'image FastHenry Circle FHPlaneHole ci-dessus. Notez que si la discrétisation FHPlane spécifiée par les propriétés FHPlane **seg1** et **seg1** est grossière, la forme du trou circulaire ne peut pas ressembler à un cercle. C\'est normal, et c\'est ainsi que FastHenry gère les trous circulaires, et non un défaut de l\'établi électromagnétique pour FastHenry.

## Options

-   Pour saisir les coordonnées manuellement, entrez simplement les chiffres, puis appuyez sur **Enter** entre chaque composante X, Y et Z. Vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Ajouter un point** lorsque vous avez les valeurs souhaitées pour insérer le point.
-   Appuyez sur **Esc** ou sur le bouton **Close** pour abandonner la commande en cours.

## Propriétés

-    {{PropertyData/fr|X}}: coordonnée X du FHPlaneHole

-    {{PropertyData/fr|Y}}: coordonnée Y du FHPlaneHole

-    {{PropertyData/fr|Z}}: coordonnée Z du FHPlaneHole

-    {{PropertyData/fr|Length}}: longueur du trou rectangulaire (le long de x à partir du point de base FHPlaneHole)

-    {{PropertyData/fr|Width}}: largeur du trou rectangulaire (le long de y à partir du point de base FHPlaneHole)

-    {{PropertyData/fr|Radius}}: rayon du trou circulaire

-    {{PropertyData/fr|Type}}: type de trou plan FastHenry. Peut être \"Point\", \"Rect\" ou \"Circle\".

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHPlaneHole peut-être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
hole = makeFHPlaneHole(baseobj=None, X=0.0, Y=0.0, Z=0.0, holetype=None, length=None, width=None, radius=None, name='FHPlaneHole')
```

-   Crée un objet `FHPlaneHole`.

-    `baseobj`est l\'objet Draft Point dont la position peut être utilisée comme base pour le FHPlaneHole. Il a la priorité sur `X`, `Y`, `Z`. Si aucun `baseobj` n\'est donné, `X`, `Y`, `Z` sont utilisés comme coordonnées.

-    `X`coordonnée x du trou, dans le système de coordonnées absolu.

-    `Y`coordonnée y du trou, dans le système de coordonnées absolu.

-    `Z`coordonnée z du trou, dans le système de coordonnées absolu.

-    `holetype`est le type de trou. Les valeurs autorisées sont: \"Point\", \"Rect\", \"Circle\"

-    `length`est la longueur du trou (le long de la dimension x), dans le cas d\'un trou rectangulaire \"Rect\".

-    `width`est la largeur du trou (le long de la dimension y), dans le cas d\'un trou rectangulaire \"Rect\".

-    `radius`est le rayon du trou, dans le cas d\'un trou circulaire \"Circle\".

-    `name`est le nom de l\'objet

Le placement du FHPlaneHole peut être modifié en modifiant sa propriété `Placement` ou en modifiant individuellement les propriétés `X`,`Y`,`Z`. La modification de `X`,`Y`,`Z` modifie la position du nœud dans le système de coordonnées relatif du `Placement`.

En outre, la classe \_FHPlaneHole expose ces méthodes. La classe \_FHPlaneHole est accessible via l\'objet FHPlaneHole Proxy (par exemple fhhole.Proxy). 
```python
pos = getAbsCoord()
```

-   Obtenez un `FreeCAD.Vector` contenant les coordonnées du trou dans le système de référence absolu


```python
pos = getRelCoord()
```

-   Obtenez un `FreeCAD.Vector` contenant les coordonnées du trou par rapport au placement FHPlaneHole


```python
pos = setRelCoord(rel_coord, placement=None)
```

-   Définit la position du trou par rapport au placement

-    `rel_coord`est un FreeCAD.Vector contenant les coordonnées du trou par rapport au placement FHPlaneHole

-    `placement`est un nouveau placement FHPlaneHole. Si `None`, l\'emplacement n\'est pas modifié


```python
pos = setAbsCoord(abs_coord, placement=None)
```

-   Définit la position absolue du trou, en tenant compte du placement de l\'objet et en cas de forçage d\'un nouveau placement

-    `abs_coord`est un FreeCAD.Vector contenant les coordonnées des trous dans le système de référence absolu

-    `placement`est un nouveau placement FHPlaneHole. Si `None`, l\'emplacement n\'est pas modifié

Exemple: 
```python
import FreeCAD, EM

fhhole = EM.makeFHPlaneHole(X=1.0,Y=1.0,Z=0.0,holetype="Rect",length=1.0,width=2.0)
```


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHPlaneHole/fr
