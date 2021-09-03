---
- GuiCommand:
   Name:Part Defeaturing
   MenuLocation:Part → Defeaturing
   Workbenches:[Part](Part_Workbench.md)
   Version:0.18
---

## Description

The **Defeaturing** tool is intended for removal of selected features from the model. In this context, features are meant as holes, protrusions, gaps, chamfers, fillets etc. found on the model.

The defeaturing tool can be very useful in different contexts:

-   To edit an imported solid where no history of operations is available.
-   Fixing defects in the model, e.g. filling gaps, holes etc.
-   Model simplification for numeric analysis, display on mobile devices, etc.

The removed features are filled by the extension of the adjacent faces, thus no unexpected parts should appear in the result. Please note that the result is a new shape that is not linked to the original; thus, it is non-parametric.

To be available, this tool requires FreeCAD to be based on Open Cascade 7.3.0 or greater. If it is not available in your version of FreeCAD, you may have a look at the [Defeaturing Workbench](Defeaturing_Workbench.md) add-on, which proposes similar functionality even with older versions of OCC or FreeCAD.

![](images/Part_Defeaturing_example.png )

## Usage

1.  Select the face(s) on the model to remove.
2.  Press the **<img src="images/Part_Defeaturing.svg" width=16px> [Defeaturing](Part_Defeaturing.md)** button.
3.  A new object is created labeled *Defeatured* in the Model [tree view](Tree_view.md), and the original object is hidden from view.

## Links

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), the official announcement on the Open Cascade collaborative development portal.
-   <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [Defeaturing Workbench](Defeaturing_Workbench.md)





 
