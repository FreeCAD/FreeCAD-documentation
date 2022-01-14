---
- GuiCommand:
   Name:EM FHSegment
   MenuLocation:EM → FHSegment
   Workbenches:[EM](EM_Workbench.md)
   Shortcut:**E** **S**
   Version:0.17
   SeeAlso:[EM FHNode](EM_FHNode.md), [EM FHPath](EM_FHPath.md)
---

# EM FHSegment/en

## Description

The FHSegment tool inserts a FastHenry segment object.

![](images/EM_FHSegment_Example.png )



*FastHenry FHSegment*

## Usage

The FHSegment object can be based on the position of a <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Line](Draft_Line.md) object, or on two existing <img alt="" src=images/EM_FHNode.svg  style="width:16px;"> [FHNodes](EM_FHNode.md) that will be the FHSegment end points, or you can select the 3D location of the two end points, where two additional FHNodes will be created.

1.  Press the **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment.md)** button, or press **E** then **S** keys.
2.  Click a first point on the 3D view, or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> add point** button.
3.  Click a second point on the 3D view, or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> add point** button.

Alternatively, you can also:

1.  Select two [FHNode](EM_FHNode.md) objects
2.  Press the **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment.md)** button, or press **E** then **S** keys.

Or:

1.  Select one or multiple [Draft Line](Draft_Line.md) object(s)
2.  Press the **<img src="images/EM_FHSegment.svg" width=16px> [EM FHSegment](EM_FHSegment.md)** button, or press **E** then **S** keys. As many FHSegment objects will be created as the Draft Line objects.

### Remarks:

-   If you create a FHSegment object based on a Draft Line object, you can NOT freely move the FHSegment or the end point FHNodes. The FHSegment will always be constrained to the base object. To change the position of the FHSegment, or of its end point, apply the change to the underlying Draft Line object (the base object is hidden by default, you can show it again by selecting the object in the tree and pressing **Space**.

-   If the FHSegment object has no base object `baseobj`, its position is controlled by the starting and ending FHNodes. You cannot change a FHSegment position by changing its Placement.

## Options

-   To enter coordinates manually, simply enter the numbers, then press **Enter** between each X, Y and Z component. You can press the **<img src="images/Draft_AddPoint.svg" width=16px> add point** button when you have the desired values to insert the point.
-   Press **Esc** or the **Close** button to abort the current command.

## Properties

-    **Base**: The base object this component is built upon (a [Draft Line](Draft_Line.md))

-    **NodeStart**: the starting [FHNode](EM_FHNode.md)

-    **NodeEnd**: the ending [FHNode](EM_FHNode.md)

-    **Width**: the FHSegment width (\'w\' segment parameter in FastHenry)

-    **Height**: the FHSegment height (\'h\' segment parameter in FastHenry)

-    **Sigma**: the FHSegment conductivity (\'sigma\' segment parameter in FastHenry)

-    **ww**: the FHSegment cross-section direction along the width (\'wx\', \'wy\', \'wz\' segment parameter in FastHenry)

-    **nhinc**: the Number of filaments in the height direction (\'nhinc\' segment parameter in FastHenry)

-    **nwinc**: the Number of filaments in the width direction (\'nwinc\' segment parameter in FastHenry)

-    **rh**: the ratio of adjacent filaments in the height direction (\'rh\' segment parameter in FastHenry)

-    **rw**: the ratio of adjacent filaments in the width direction (\'rw\' segment parameter in FastHenry)

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The FHSegment object can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
segment = makeFHSegment(baseobj=None, nodeStart=None, nodeEnd=None, width=None, height=None, name='FHSegment')
```

-   Creates a `FHSegment` object.

-    `baseobj`is the Draft Line object that can be used as base for the FHSegment. If `nodeStart` and `nodeEnd` are specified, they have priority over the `baseobj`, and `baseobj` is ignored.

-    `nodeStart`is the segment starting node [FHNode](EM_FHNode.md) object.

-    `nodeEnd`is the segment ending node [FHNode](EM_FHNode.md) object.

-    `width`is the segment width. Defaults to `EMFHSEGMENT_DEF_SEGWIDTH`.

-    `height`is the segment height. Defaults to `EMFHSEGMENT_DEF_SEGHEIGHT`.

-    `name`is the name of the object

Example:


```python
import FreeCAD, EM

fhnode1 = EM.makeFHNode(X=1.0,Y=0,Z=0)
fhnode2 = EM.makeFHNode(X=0,Y=1.0,Z=0)

fhsegment = EM.makeFHSegment(nodeStart=fhnode1, nodeEnd=fhnode2)
```





{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHSegment/en
