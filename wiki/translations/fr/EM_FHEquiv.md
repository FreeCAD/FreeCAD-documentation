---
- GuiCommand:/fr
   Name:EM FHEquiv
   Name/fr:EM FHEquiv
   MenuLocation:EM → FHEquiv
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:**E** **E**
   SeeAlso:[EM FHNode](EM_FHNode/fr.md), [EM FHSegment](EM_FHSegment/fr.md), [EM FHPath](EM_FHPath/fr.md), [EM FHPlane](EM_FHPlane/fr.md), [EM FHPort](EM_FHPort/fr.md),
   Version:0.17
---

# EM FHEquiv/fr

## Description

L\'outil FHEquiv court-circuite deux objets FHNode.

![](images/EM_FHEquiv_Example.png ) *FastHenry FHEquiv*

## Utilisation

L\'objet FHEquiv est basé sur les deux FHNodes existants qu\'il court-circuitera.

1.  Sélectionnez deux <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [FHNode](EM_FHNode/fr.md) objets
2.  Appuyez sur le bouton **<img src="images/EM_FHEquiv.svg" width=16px> [EM FHEquiv](EM_FHEquiv/fr.md)** ou appuyez sur les touches **E** puis **E**.

### Remarques

-   Si vous devez court-circuiter plusieurs nœuds, créez simplement plusieurs nœuds FHEquiv. Vous n\'avez pas besoin d\'un maillage complet de nœuds FHEquiv, car bien sûr, si nœud1 est court-circuité avec nœud2, et nœud2 est court-circuité avec nœud3, également nœud1 résultera en court-circuit avec nœud3.

## Propriétés

-    {{PropertyData/fr|Node1}}: le premier [FHNode](EM_FHNode/fr.md) à court-circuiter

-    {{PropertyData/fr|Node2}}: le deuxième [FHNode](EM_FHNode/fr.md) à court-circuiter

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHEquiv peut-être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
equiv = makeFHEquiv(node1=None,node2=None,name='FHEquiv')
```

-   Crée un objet `FHEquiv`.

-    `node1`est le premier objet de noeud [FHNode](EM_FHNode/fr.md) à court-circuiter.

-    `node2`est le deuxième objet de noeud [FHNode](EM_FHNode/fr.md) à court-circuiter.

    -   
        `name`
        
        est le nom de l\'objet

Exemple: 
```python
import FreeCAD, EM

fhnode1 = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode2 = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhequiv = EM.makeFHEquiv(fhnode1, fhnode2)
```


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHEquiv/fr
