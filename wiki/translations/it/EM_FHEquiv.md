---
- GuiCommand:/it
   Name:EM FHEquiv
   Name/it:EM FHEquiv
   MenuLocation:EM → FHEquiv
   Workbenches:[EM](EM_Workbench/it.md) (add-on)
   Shortcut:**E** **E**
   SeeAlso:[EM FHNode](EM_FHNode/it.md), [EM FHSegment](EM_FHSegment/it.md), [EM FHPath](EM_FHPath/it.md), [EM FHPlane](EM_FHPlane/it.md), [EM FHPort](EM_FHPort/it.md),
   Version:0.17
---

## Descrizione

The FHEquiv tool short-circuits two FHNode objects.

![](images/EM_FHEquiv_Example.png ) *FastHenry FHEquiv*

## Usage

The FHEquiv object is based on the two existing FHNodes that it will short-circuit.

1.  Select two <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [FHNode](EM_FHNode.md) objects
2.  Press the **<img src="images/EM_FHEquiv.svg" width=16px> [EM FHEquiv](EM_FHEquiv.md)** button, or press **E** then **E** keys.

### Remarks:

-   If you need to short-circuit multiple nodes, just create multiple FHEquiv nodes. You don\'t need a full mesh of FHEquiv nodes, as of course if node1 is shorted with node2, and node2 is shorted with node3, also node1 will result shorted with node3.

## Properties

-    **Node1**: the first [FHNode](EM_FHNode.md) to short-circuit

-    **Node2**: the second [FHNode](EM_FHNode.md) to short-circuit

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The FHEquiv object can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
equiv = makeFHEquiv(node1=None,node2=None,name='FHEquiv')
```

-   Creates a `FHEquiv` object.

-    `node1`is the first node [FHNode](EM_FHNode.md) object to short-circuit.

-    `node2`is the second node [FHNode](EM_FHNode.md) object to short-circuit.

-    `name`is the name of the object

Esempio: 
```python
import FreeCAD, EM

fhnode1 = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode2 = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhequiv = EM.makeFHEquiv(fhnode1, fhnode2)
```


{{EM Tools navi

}}  
