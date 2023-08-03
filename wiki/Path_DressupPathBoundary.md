---
 GuiCommand:
   Name: Path DressupPathBoundary
   MenuLocation: Path , Path Dressup , Boundary
   Workbenches: Path_Workbench
   SeeAlso: Path_DressupTag, Path_DressupRampEntry
---

# Path DressupPathBoundary

## Description

The tool <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:24px;"> [DressupPathBoundary](Path_DressupPathBoundary.md) allows restricting the extent of a path to a smaller part of the object. For example, restricting a profile path to just one face or part of the model.

## Usage

1.  Select a path such as contour, profile or pocket operation.
2.  Select the **Path → Path Dressup → <img src="images/Path_DressupPathBoundary.svg" width=16px> Boundary** option from the menu.

## Options

-   **Create Box**
-   **Create Cylinder**
-   **Extend Model\'s Boundary Box**: A very convenient way to limit a path is to select this option and use negative values.
-   **Use Existing Solid**

## Limitations

-   The *Create Box* option only sets the dimensions of the box, not its origin. To alter its origin it is necessary to adjust its *Placement* in the [tree view](Tree_view.md).




 {{Path_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupPathBoundary
