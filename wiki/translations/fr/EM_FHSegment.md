---
- GuiCommand:/fr
   Name:EM FHSegment
   Name/fr:EM Segment FH
   MenuLocation:EM → FHSegment
   Workbenches:[EM](EM_Workbench/fr.md)
   Shortcut:**E** **S**
   Version:0.17
   SeeAlso:[EM Noeud FH](EM_FHNode/fr.md), [EM Chemin FH](EM_FHPath/fr.md)
---

# EM FHSegment/fr

## Description

L\'outil Segment FH insère un objet FastHenry de type Segment.

![](images/EM_FHSegment_Example.png )



*Segment FH FastHenry*

## Utilisation

L\'objet Segment FH peut être basé sur la position d\'un objet <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Ligne](Draft_Line/fr.md) ou sur deux <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [Noeuds FH](EM_FHNode/fr.md) qui seront les points d\'extrémité du Segment FH, ou bien, vous pouvez sélectionner l\'emplacement 3D des deux points d\'extrémité, où deux Noeuds FH supplémentaires seront créés.

1.  Appuyez sur le bouton **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment/fr.md)** ou appuyez sur les touches **E** puis **S**.
2.  Cliquez sur un premier point de la vue 3D ou tapez une coordonnée et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
3.  Cliquez sur un deuxième point de la vue 3D ou tapez une coordonnée et appuyez sur le bouton **<img src="images/_Draft_AddPoint.svg" width=16px> Entrez le point**.

Vous pouvez également le faire :

1.  Sélectionnez deux objets <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [Noeuds FH](EM_FHNode/fr.md)
2.  Appuyez sur le bouton **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment/fr.md)** ou appuyez sur la touche **E** puis **S**.

Ou:

1.  Sélectionnez un ou plusieurs objet(s) [Draft Ligne](Draft_Line/fr.md)
2.  Appuyez sur le bouton **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment/fr.md)** ou appuyez sur les touches **E** puis **S**. Autant d\'objets Segment FH seront créés que les objets Draft Ligne.

### Remarques

-   Si vous créez un objet Segment FH basé sur un objet Draft Ligne, vous ne pouvez PAS déplacer librement le FHSegment ou les points finaux FHNodes. Le FHSegment sera toujours contraint à l\'objet de base. Pour modifier la position du FHSegment ou de son point de fin, appliquez la modification à l\'objet Draft Line sous-jacent (l\'objet de base est masqué par défaut, vous pouvez l\'afficher à nouveau en sélectionnant l\'objet dans l\'arborescence et en appuyant sur **Espace**.

-   Si l\'objet Segment FH n\'a pas d\'objet de base `baseobj`, sa position est contrôlée par les FHNodes de début et de fin. Vous ne pouvez pas modifier la position d\'un segment FHS en modifiant son placement.

## Options

-   Pour entrer les coordonnées manuellement, il suffit d\'entrer les nombres, et frapper sur la touche **Entrée** entre chaque affectation de la composante X, Y et Z. Vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées pour insérer le point.
-   Appuyez sur **Echap** ou le **Fermer** pour annuler et quitter l\'opération.

## Propriétés

-    **Base**: L\'objet de base sur lequel ce composant est construit (une [Draft Ligne](Draft_Line/fr.md))

-    **NodeStart**: le début de [Noeud FH](EM_FHNode/fr.md)

-    **NodeEnd**: la fin de [Noeud FH](EM_FHNode/fr.md)

-    **Width**: la largeur du segment FH (paramètre de segment \'w\' dans FastHenry)

-    **Height**: la hauteur du segment FH (paramètre du segment \'h\' dans FastHenry)

-    **Sigma**: la conductivité segment FH (paramètre de segment \'sigma\' dans FastHenry)

-    **ww**: la direction de la section transversale du segment FH le long de la largeur (paramètre de segment \'wx\', \'wy\', \'wz\' dans FastHenry)

-    **nhinc**: le nombre de filaments dans le sens de la hauteur (paramètre de segment \'nhinc\' dans FastHenry)

-    **nwinc**: le nombre de filaments dans le sens de la largeur (paramètre de segment \'nwinc\' dans FastHenry)

-    **rh**: le rapport des filaments adjacents dans le sens de la hauteur (paramètre de segment \'rh\' dans FastHenry)

-    **rw**: le rapport des filaments adjacents dans le sens de la largeur (paramètre de segment \'rw\' dans FastHenry)

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHSegment peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
segment = makeFHSegment(baseobj=None, nodeStart=None, nodeEnd=None, width=None, height=None, name='FHSegment')
```

-   Crée un objet `FHSegment`.

-    `baseobj`est l\'objet Draft Ligne qui peut être utilisé comme base pour le FHSegment. Si `nodeStart` et `nodeEnd` sont spécifiés, ils ont priorité sur `baseobj`, et `baseobj` est ignoré.

-    `nodeStart`est l\'objet noeud de départ du segment [FHNode](EM_FHNode/fr.md).

-    `nodeEnd`est l\'objet noeud de fin de segment [FHNode](EM_FHNode/fr.md).

-    `width`est la largeur du segment. La valeur par défaut est `EMFHSEGMENT_DEF_SEGWIDTH`.

-    `height`est la hauteur du segment. La valeur par défaut est `EMFHSEGMENT_DEF_SEGHEIGHT`.

-    `name`est le nom de l\'objet.

Exemple:


```python
import FreeCAD, EM

fhnode1 = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode2 = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhsegment = EM.makeFHSegment(nodeStart=fhnode1, nodeEnd=fhnode2)
```





{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHSegment/fr
