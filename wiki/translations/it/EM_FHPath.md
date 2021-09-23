---
- GuiCommand:/it
   Name:EM FHPath
   Name/it:EM FHPath
   MenuLocation:EM → FHPath
   Workbenches:[EM](EM_Workbench/it.md) (add-on)
   Shortcut:**E** **T**
   SeeAlso:[EM FHNode](EM_FHNode/it.md), [EM FHSegment](EM_FHSegment/it.md)
   Version:0.17
---

# EM FHPath/it

## Descrizione

The FHPath tool inserts a FHPath object, that is a set of FastHenry segments along a path.

![](images/EM_FHPath_Example.png ) *FastHenry FHPath*

## Utilizzo

The FHPath object can be based on any shape containing edges, but the FHPath object is designed to work best with the support of a sketch or a wire.

1.  Select one or multiple object(s) containing edges.
2.  Press the **<img src="images/EM_FHPath.svg" width=16px> [EM FHPath](EM_FHPath.md)** button, or press **E** then **T** keys. As many FHPath objects will be created as the selected objects.

### Note:

-   The FHPath will create a set of FHNodes and a set of FastHenry segments following the path formed by the edges.

-   Curved edges will be discretized according to the FHPath properties settings.

-   If the resulting segments are too short with respect to the cross-section, a warning will be raised in the Report window of FreeCAD, as this can cause issues in FastHenry simulations.

-   The default orientation of the FHPath segment cross-sections is the FastHenry default one: the vector along the width is parallel to the XY plane; if the width is along the Z direction, the width vector is aligned to the X axis. You can change the orientation of the cross-section of the first segment of the FHPath specifying the **ww** vector property. This is done in the base Placement coordinate system, i.e. changes in the Placement preserve the relative cross-connection orientation without changing **ww**. Subsequent segments are automatically oriented applying the rotations corresponding to the angle between each pair of segments in turn. The first segment is identified by the first node of the FHPath object as shown in the tree (the topmost is the first node, regardless of its name / numbering), or equivalently as the first node in the **Nodes** FHPath property list.

-   A FHPath will have at least one starting FHNode and one ending FHNode, if there is at least one edge in the base object. The start FHNode object and the ending FHNode will be kept the same if you change the path, by including or removing edges from the base object, or changing the FHPath discretization. Therefore, when changing the FHPath, you don\'t need to worry about the connections to other objects already done using the FHPath endpoints, e.g. if you used the endpoints as starting point for FHSegment objects, FHPort objects, FHEquiv objects, or connections to a FHPlane object. In particular, when you modify a FHPath causing the creation of more segments, the already existing FHNode object list will be simply extended, and the old FHNode positions will be re-arranged. If instead you modify a FHPath causing the removal of segments, the FHNode object list will be shortened and the excess FHNode objects removed from the Document, unless any of the FHNode had been already used within any other object (e.g. if you used an intermediate node for creating a FHSegment). In this case the FHNode will be kept, but outside the FHPath object, and the connection will be possibly dangling; it is up to the user to guarantee the correcness of the connections.

-   You cannot freely move the FHPath object or its FHNodes. To change the position of the FHPath, move the underlying base object (the base object is hidden by default, you can show it again by selecting the object in the tree and pressing **Space**.

-   Curved edges will be discretized into a set of segments according to the **Discr** FHPath property.

## Proprietà

-    **Base**: The base object this component is built upon

-    **Nodes**: (read-only) The list of [FHNode](EM_FHNode.md) along the path. Not for direct user modification.

-    **Width**: the FHPath segments width (\'w\' segment parameter in FastHenry)

-    **Height**: the FHPath segments height (\'h\' segment parameter in FastHenry)

-    **Discr**: the max number of segments into which curved edges will be discretized

-    **Sigma**: the FHPath segments conductivity (\'sigma\' segment parameter in FastHenry)

-    **ww**: the cross-section direction along the width for the first segment of the FHPath (\'wx\', \'wy\', \'wz\' segment parameter in FastHenry)

-    **nhinc**: the number of filaments in the height direction (\'nhinc\' segment parameter in FastHenry)

-    **nwinc**: the number of filaments in the width direction (\'nwinc\' segment parameter in FastHenry)

-    **rh**: the ratio of adjacent filaments in the height direction (\'rh\' segment parameter in FastHenry)

-    **rw**: the ratio of adjacent filaments in the width direction (\'rw\' segment parameter in FastHenry)

## Script


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The FHPath object can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
path = makeFHPath(baseobj=None,name='FHPath')
```

-   Creates a `FHPath` object.

-    `baseobj`is the object that can be used as base for the FHPath. If no `baseobj` is given, the user must assign a base object later on, to be able to use this object. The `baseobj` is mandatory, and can be any shape containing edges, even if the FHPath object is designed to work best with the support of a sketch or a wire.

-    `name`is the name of the object

Esempio: 
```python
import FreeCAD, EM
from FreeCAD import Base
import Part, PartGui
spiral = App.ActiveDocument.addObject("Part::Spiral","Spiral")
spiral.Growth=1.00
spiral.Rotations=4.00
spiral.Radius=1.00
spiral.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
spiral.Label='Spiral'

fhpath = EM.makeFHPath(spiral)
fhpath.Discr = 40
App.ActiveDocument.recompute()
```


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHPath/it
