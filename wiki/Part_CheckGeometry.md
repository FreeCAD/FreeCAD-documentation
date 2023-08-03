---
 GuiCommand:
   Name: Part CheckGeometry‏‎
   MenuLocation: Part , Check geometry
   Workbenches: Part_Workbench
---

# Part CheckGeometry

## Description

The **<img src="images/Part_CheckGeometry.svg" width=16px> [Part CheckGeometry](Part_CheckGeometry.md)** tool runs a verification and reports if geometry is a valid solid. The tool checks if the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep or [B-rep](Glossary#B.md)) of the model is valid.

## Usage

1.  Select a part (beware to select the whole part and not just a face to check for valid solid)
2.  Invoke the tool by either:
    -   Clicking on the **<img src="images/Part_CheckGeometry.svg" width=16px> [CheckGeometry](Part_CheckGeometry.md)** button available in the Part workbench toolbar.
    -   Using the **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Check geometry** entry from the top menu.
3.  The **Settings** task panel opens, unless **Skip settings page** is enabled. See [Options](#Options.md) for more information. Click **Run check**.

Results will be reported in the [Task panel](Task_panel.md). If the check produced errors: click in the report on a specific error message and the corresponding geometric object (edge, face, etc.) will be highlighted in the [3D view](3D_view.md).

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 

If ticked, additionally a Boolean OPerations (BOP) check is performed.

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md).

## Shape Content 

In addition to detecting potential geometry errors, this tool shows a range of properties regarding the selected object:

-   Checked object
-   Shape type
-   Number of geometric entities: vertices, edges, wires, faces, shells, solids, compsolids, compounds, total shapes
-   Geometric and mass properties:
    -   Area
    -   Volume
    -   Mass
    -   Length
    -   Center of mass
    -   Orientation
    -   Symmetry axis
    -   Symmetry point
    -   Moments
    -   First axis of inertia
    -   Second axis of inertia
    -   Third axis of inertia
    -   Radius of gyration
    -   Global placement

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be checked using this tool. For [App Links](App_Link.md) the shape of the linked object is checked. For [App Part](App_Part.md) containers the visible objects within are checked as compounds. <small>(v0.20)</small> 
-   FreeCAD has no methods to automatically repair geometry. If faults are detected the steps involved to create the model need to be examined and fixed manually.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry
