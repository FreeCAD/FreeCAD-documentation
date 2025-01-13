---
 GuiCommand:
   Name: CAM DressupPathBoundary
   MenuLocation: CAM , Path Dressup , Boundary
   Workbenches: CAM_Workbench
   SeeAlso: CAM_DressupTag, CAM_DressupRampEntry
---

# CAM DressupPathBoundary/de



## Beschreibung

The tool <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:24px;"> [DressupPathBoundary](CAM_DressupPathBoundary.md) allows restricting the extent of a path to a smaller part of the object. For example, restricting a profile path to just one face or part of the model.



## Anwendung

1.  Select a path such as contour, profile or pocket operation.
2.  Select the **CAM → Path Dressup → <img src="images/CAM_DressupPathBoundary.svg" width=16px> Boundary** option from the menu.



## Optionen

-   **Create Box**
-   **Create Cylinder**
-   **Extend Model\'s Boundary Box**: A very convenient way to limit a path is to select this option and use negative values.
-   **Use Existing Solid**



## Einschränkungen

-   The *Create Box* option only sets the dimensions of the box, not its origin. To alter its origin it is necessary to adjust its *Placement* in the [tree view](Tree_view.md).





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupPathBoundary/de
