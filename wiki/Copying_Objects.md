# Copying Objects
## Overview

Like many other computer programs FreeCAD has the ability to cut, copy and paste objects. [Document](Document_structure.md) objects may be freely copied within a document or between documents using the <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Std Copy](Std_Copy.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Std Paste](Std_Paste.md) and [Std DuplicateSelection](Std_DuplicateSelection.md) commands.

![](images/Copy_past_duplicate.png )

Please consider that the copy-pasted objects are not dependent on the original. If you want dependent clones please use <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Draft Workbench\'s Clone](Draft_Clone.md) or <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [Part Design Workbench\'s Clone](PartDesign_Clone.md). If you need neither a dependent clone nor a parametric replica, you may also use <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [ Part Workbench\'s Simple Copy](Part_SimpleCopy.md). For patterned clones, please look into the [ Other Methods section](Copying_Objects#Other_Methods.md) of this page.

## Copying Linked Objects 

If an object to be copied has links to object(s) not in the selection, FreeCAD will ask if the unselected objects should be included in the copy operation.

## Finding and Positioning Pasted Object(s) 

After a copy-paste operation, it may not be obvious where the new objects are located in the [3D view](3D_view.md). That is because the new objects have the same [Placement](Placement.md) property as their originals. Toggle the Visibility property (**Spacebar**) to hide the originals and then move the copies to their correct position, for example using <img alt="" src=images/Std_TransformManip.svg  style="width:24px;"> [Std TransformManip](Std_TransformManip.md) or <img alt="" src=images/Std_Placement.svg  style="width:24px;"> [Std Placement](Std_Placement.md).

## Other Methods 

Like most things in FreeCAD, there are many ways of making a copy. For more ideas, look at:

-   PartDesign: [Mirror](PartDesign_Mirrored.md), [Linear Pattern](PartDesign_LinearPattern.md), [Polar Pattern](PartDesign_PolarPattern.md), [MultiTransform](PartDesign_MultiTransform.md)
-   Part: [Mirror](Part_Mirror.md), [Create simple copy](Part_SimpleCopy.md)
-   Draft: [Offset](Draft_Offset.md), [Scale](Draft_Scale.md), [Array](Draft_OrthoArray.md), [PathArray](Draft_PathArray.md), [Clone](Draft_Clone.md), [Mirror](Draft_Mirror.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > Copying Objects
