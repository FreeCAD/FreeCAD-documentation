---
- GuiCommand:/fr
   Name:EM FHPort
   Name:EM FHPort
   MenuLocation:EM → FHPort
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:**E** **P**
   SeeAlso:[EM FHNode](EM_FHNode/fr.md), [EM FHSegment](EM_FHSegment/fr.md), [EM FHPath](EM_FHPath/fr.md), [EM FHPlane](EM_FHPlane/fr.md), [EM FHEquiv](EM_FHEquiv/fr.md),
   Version:0.17
---

# EM FHPort/fr

## Description

L\'outil FHPort crée un port FastHenry entre deux objets FHNode.

![](images/EM_FHPort_Example.png ) *FastHenry FHPort*

## Utilisation

L\'objet FHPort est basé sur les deux FHNodes existants entre lesquels il créera un port FastHenry.

1.  Sélectionnez deux <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [FHNode](EM_FHNode/fr.md) objets
2.  Appuyez sur le bouton **<img src="images/EM_FHPort.svg" width=16px> [EM FHPort](EM_FHPort/fr.md)** ou appuyez sur les touches **E** puis **P**.

### Remarques

-   Le premier nœud que vous sélectionnez est le nœud positif du port et la flèche, qui est la forme de l\'objet FHPort, pointera dans cette direction.

## Propriétés

-    {{PropertyData/fr|NodePos}}: le positif [FHNode](EM_FHNode/fr.md) du port FastHenry

-    {{PropertyData/fr|NodeNeg}}: le négatif [FHNode](EM_FHNode/fr.md) du port FastHenry

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHPort peut-être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
port = makeFHPort(nodePos=None,nodeNeg=None,name='FHPort')
```

-   Crée un objet `FHPort`.

-    `nodePos`est l\'objet nœud positif [FHNode](EM_FHNode/fr.md) du port FastHenry.

-    `nodeNeg`est le nœud négatif [FHNode](EM_FHNode/fr.md) objet du port FastHenry.

-    `name`est le nom de l\'objet.

Exemple: 
```python
import FreeCAD, EM

fhnode_p = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode_n = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhport = EM.makeFHPort(fhnode_p, fhnode_n)
```


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHPort/fr
