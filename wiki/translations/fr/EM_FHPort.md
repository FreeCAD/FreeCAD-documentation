---
- GuiCommand   */fr
   Name   *EM FHPort
   Name/fr   *EM Port FH
   MenuLocation   *EM → FHPort
   Workbenches   *[EM](EM_Workbench/fr.md)
   Shortcut   ***E** **P**
   Version   *0.17
   SeeAlso   *[EM Noeud FH](EM_FHNode/fr.md), [EM Segment FH](EM_FHSegment/fr.md), [EM Chemin Fh](EM_FHPath/fr.md), [EM Plan FH](EM_FHPlane/fr.md), [EM Equivalence FH](EM_FHEquiv/fr.md)
---

# EM FHPort/fr

## Description

L\'outil Port FH crée un port FastHenry entre deux objets Noeud FH.

![](images/EM_FHPort_Example.png )



*Port FH FastHenry*

## Utilisation

L\'objet Port FH est basé sur les deux Noeuds FH existants entre lesquels il créera un port FastHenry.

1.  Sélectionnez deux <img alt="" src=images/EM_FHNode.svg  style="width   *16px;"> [Noeud FH](EM_FHNode/fr.md) objets
2.  Appuyez sur le bouton **<img src="images/EM_FHPort.svg" width=16px> [EM FHPort](EM_FHPort/fr.md)** ou appuyez sur les touches **E** puis **P**.

### Remarques

-   Le premier nœud que vous sélectionnez est le nœud positif du port et la flèche qui est la forme de l\'objet Port FH, pointera dans cette direction.

## Propriétés

-    **NodePos**   * le [Noeud FH](EM_FHNode/fr.md) positif du port FastHenry

-    **NodeNeg**   * le [Noeud FH](EM_FHNode/fr.md) négatif du port FastHenry

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Port FH peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante   *


```python
port = makeFHPort(nodePos=None,nodeNeg=None,name='FHPort')
```

-   Crée un objet `FHPort`.

-    `nodePos`est l\'objet [Noeud FH](EM_FHNode/fr.md) positif du port FastHenry.

-    `nodeNeg`est l\'objet [Noeud FH](EM_FHNode/fr.md) négatif objet du port FastHenry.

-    `name`est le nom de l\'objet.

Exemple   *


```python
import FreeCAD, EM

fhnode_p = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode_n = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhport = EM.makeFHPort(fhnode_p, fhnode_n)
```





{{EM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [EM](Category_EM.md) > EM FHPort/fr
