---
- GuiCommand:
   Name: EM FHPlane
   Name/it: EM FHPlane
   MenuLocation: EM -> FHPlane
   Workbenches: EM Workbench/it 
   Shortcut: **E** **P**
   SeeAlso: EM_FHNode/it, EM_FHPlaneHole/it, EM_FHPlaneAddRemoveNodeHole/it
   Version: 0.17
---

# EM FHPlane/it


</div>

## Descrizione

The FHPlane tool inserts a FastHenry uniform conductive plane object.

![](images/EM_FHPlane_Example.png )



*FastHenry FHPlane*

## Utilizzo

The FHPlane object must be based on another object, that can be either a [Draft Rectangle](Draft_Rectangle.md) or a [Part Box](Part_Box.md) object. In case you based your FHPlane on a [Part Box](Part_Box.md) object, the Thickness parameter will be inherited from the Box Height value.

1.  Create and select a <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle.md) or a <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Box](Part_Box.md) object
2.  Press the **<img src="images/EM_FHPlane.svg" width=16px> [EM FHPlane](EM_FHPlane.md)** button, or press **E** then **P** keys.

In addition, you can also select together with the base object (the [Draft Rectangle](Draft_Rectangle.md) or the [Part Box](Part_Box.md)) also one or more [EM FHNode](EM_FHNode.md) and / or one or more [EM FHPlaneHole](EM_FHPlaneHole.md) objects, that will be adopted by the FHPlane:

1.  Create a [Draft Rectangle](Draft_Rectangle.md) or a [Part Box](Part_Box.md) object
2.  Create one or more <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [EM FHNode](EM_FHNode.md) objects
3.  Create one or more <img alt="" src=images/EM_FHPlaneHole.svg  style="width:16px;"> [EM FHPlaneHole](EM_FHPlaneHole.md) objects
4.  Select the base object, the FHNode objects and the FHPlaneHole objects (for this multiple selection, you can point and click the objects in the [tree view](Tree_view.md) or in the [3D view](3D_view.md), and to perform a multiple selection just keep the **CTRL** key pressed while selecting).
5.  Press the **<img src="images/EM_FHPlane.svg" width=16px> [EM FHPlane](EM_FHPlane.md)** button, or press **E** then **P** keys.

### Remarks:

A FastHenry uniform conductive plane object is formed by laying down a gird of nodes (hereafter called \'internal nodes\') and connecting the nodes with a 2D mesh of segments in the (relative) X and Y directions. Holes are formed in the plane by removing some internal nodes, and hence also the segments that connects to those nodes. For more details on FastHenry uniform conductive planes, you should review the [FastHenry user\'s guide](https://www.fastfieldsolvers.com/documentation.htm).

-   As the FHPlane object is based on a Draft Rectangle or Part Box object, you can NOT freely move the FHPlane. The FHPlane will always be constrained to the base object. To change the position of the FHPlane, apply the change to the underlying base object (the base object is hidden by default, you can show it again by selecting the object in the tree and pressing **Space**. The origin of the FHPlane is the origin of the base object.

-   When the FHNode objects are adopted by the FHPlane, their (X, Y, Z) coordinates will be made relative to the FHPlane origin (so while the FHNode will retain the same position in space, the relative coordinates (X, Y, Z) of the FHNode will be modified to be relative to the FHPlane origin). Also, once adopted, the Z coordinate of the FHNode will be reset to zero (as the coordinates are relative to the FHPlane, the Z coordinate is the height of the object from the plane). For this reason, the node will be visible only from the bottom of the FHPlane, or changing the transparency of the FHPlane to see the FHNodes through, or hiding the FHPlane altogether. Moreover, to show that the FHNode now belongs to the FHPlane, the color of the FHNode is changed.

-   When the FHPlaneHole objects are adopted by the FHPlane, their (X, Y, Z) coordinates will be made relative to the FHPlane origin (so while the FHPlaneHole will retain the same position in space, the relative coordinates (X, Y, Z) of the FHPlaneHole will be modified to be relative to the FHPlane origin). Also, once adopted, the Z coordinate of the FHPlaneHole will be reset to zero (as the coordinates are relative to the FHPlane, the Z coordinate is the height of the object from the plane). For this reason, the node will be visible only from the bottom of the FHPlane, or changing the transparency of the FHPlane to see the FHNodes through, or hiding the FHPlane altogether. Moreover, to show that the FHNode now belongs to the FHPlane, the color of the FHNode is changed.

-   If you want to remove the FHNodes or the FHPlaneHoles from the FHPlane later on, you can use the [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole.md) command.

## Properties

-    **Base**: The base object this component is built upon (a [Draft Rectangle](Draft_Rectangle.md) or a [Part Box](Part_Box.md))

-    **Thickness**: the FHPlane thickness (\'thick\' plane parameter in FastHenry). If the FHPlane is based on a [Part Box](Part_Box.md), this value is inherited from the Part Box Height parameter

-    **seg1**: the Number of segments along the length direction (\'seg1\' plane parameter in FastHenry)

-    **seg2**: the Number of segments along the width direction (\'seg2\' plane parameter in FastHenry)

-    **nhinc**: the Number of filaments the plane thickness (\'nhinc\' plane parameter in FastHenry)

-    **rh**: the ratio of adjacent filaments along the thickness (\'rh\' plane parameter in FastHenry)

-    **Sigma**: the FHPlane conductivity (\'sigma\' plane parameter in FastHenry)

-    **segwid1**: the Width of segments along the plane length direction (\'segwid1\' plane parameter in FastHenry)

-    **segwid2**: the Width of segments along the plane width direction (\'segwid2\' plane parameter in FastHenry)

-    **Nodes**: the list of FHNode objects for connections to the plane

-    **Holes**: the list of FHPlaneHoles in the plane

-    **FineMesh**: specifies if this the plane fine mesh is shown (i.e. composing segments)

-    **ShowNodes**: show the internal node grid supporting the plane (i.e. internal nodes)

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The FHPlane object can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
plane = makeFHPlane(baseobj=None, thickness=None, seg1=None, seg2=None, nodes=[], holes=[], name='FHPlane')
```

-   Creates a `FHPlane` object.

-    `baseobj`is the Draft Rectangle object or Part Box object that can be used as base for the FHPlane. If no `baseobj` is given, the user must assign a base object later on, to be able to use this object.

-    `thickness`is the plane thickness. If the `baseobj` is a Part Box, this parameter is ignored, and the Part Box height is used instead. Defaults to `EMFHPLANE_DEF_THICKNESS`.

-    `seg1`is an integer defining the number of segments along the x dimension of the plane (\'seg1\' parameter in FastHenry)

-    `seg2`is an integer defining the number of segments along the y dimension of the plane (\'seg2\' parameter in FastHenry)

-    `nodes`is an array of FHNode objects, specifying the nodes that will be adopted by the plane.

-    `holes`is an array of FHPlaneHole objects, specifying the holes that will be adopted by the plane.

-    `name`is the name of the object

Example:


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
⏵ [documentation index](../README.md) > [EM](Category_EM.md) > EM FHPlane/it
