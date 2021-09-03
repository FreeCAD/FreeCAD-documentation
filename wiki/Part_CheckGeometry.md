---
- GuiCommand:
   Name:Part CheckGeometry‏‎
   MenuLocation:Part → Check geometry
   Workbenches:[Part](Part_Workbench.md)
---

## Description

The **<img src="images/Part_CheckGeometry.svg" width=16px> [Part CheckGeometry](Part_CheckGeometry.md)** tool runs a verification and reports if geometry is a valid solid. The tool checks if the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep or [B-rep](Glossary#B.md)) of the model is valid.

## Usage

1.  Select a part (beware to select the whole part and not just a face to check for valid solid)
2.  Invoke the tool by either:
    -   Clicking on the **<img src="images/Part_CheckGeometry.svg" width=16px> [CheckGeometry](Part_CheckGeometry.md)** button available in the Part workbench toolbar.
    -   Using the {{MenuCommand|Part → <img src="images/Part_CheckGeometry.svg" width=16px> Check geometry}} entry from the top menu.
3.  The {{MenuCommand|Settings}} task panel opens, unless {{MenuCommand|Skip settings page}} is enabled. See [Options](#Options.md) for more information. Click **Run check**.

Results will be reported in the [Task panel](Task_panel.md). If the check produced errors: click in the report on a specific error message and the corresponding geometric object (edge, face, etc.) will be highlighted in the [3D view](3D_view.md).

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page {#skip_settings_page}

If ticked, subsequent invocations of the tool skip showing the {{MenuCommand|Settings}} task panel.

### Run BOP check {#run_bop_check}

If ticked, additionally a Boolean OPerations (BOP) check is performed. <small>(v0.19)</small> 

### Log errors {#log_errors}

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 




  
