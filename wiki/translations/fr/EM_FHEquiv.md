---
 GuiCommand:
   Name: EM FHEquiv
   Name/fr: EM Equivalence FH
   MenuLocation: EM , FHEquiv
   Workbenches: EM_Workbench/fr
   Shortcut: **E** **E**
   Version: 0.17
   SeeAlso: EM_FHNode/fr, EM_FHSegment/fr, EM_FHPath/fr, EM_FHPlane/fr, EM_FHPort/fr
---

# EM FHEquiv/fr

## Description

L\'outil Equivalence FH court-circuite deux objets Noeud FH.

![](images/EM_FHEquiv_Example.png )



*Equivalence FH FastHenry*

## Utilisation

L\'objet Equivalence FH est basé sur les deux Noeuds FH existants qu\'il court-circuitera.

1.  Sélectionnez deux <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [Noeud FH](EM_FHNode/fr.md) objets
2.  Appuyez sur le bouton **<img src="images/EM_FHEquiv.svg" width=16px> [EM FHEquiv](EM_FHEquiv/fr.md)** ou appuyez sur les touches **E** puis **E**.

### Remarques

-   Si vous devez court-circuiter plusieurs nœuds, créez simplement plusieurs nœuds FHEquiv. Vous n\'avez pas besoin d\'un maillage complet de nœuds FHEquiv, car bien sûr, si nœud1 est court-circuité avec nœud2, et nœud2 est court-circuité avec nœud3, le nœud1 sera en court-circuit avec nœud3.

## Propriétés

-    **Node1**: le premier [Noeud FH](EM_FHNode/fr.md) à court-circuiter

-    **Node2**: le deuxième [Noeud FH](EM_FHNode/fr.md) à court-circuiter

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Equivalence FH peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
equiv = makeFHEquiv(node1=None,node2=None,name='FHEquiv')
```

-   Crée un objet `FHEquiv`.

-    `node1`est le premier objet [Noeud FH](EM_FHNode/fr.md) à court-circuiter.

-    `node2`est le deuxième objet [Noeud FH](EM_FHNode/fr.md) à court-circuiter.

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
⏵ [documentation index](../README.md) > [EM](Category_EM.md) > EM FHEquiv/fr
