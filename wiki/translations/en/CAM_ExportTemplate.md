---
 GuiCommand:
   Name: CAM ExportTemplate
   MenuLocation: CAM , Export Template
   Workbenches: CAM_Workbench
   SeeAlso: CAM_SetupSheet
---

# CAM ExportTemplate/en

## Description

The <img alt="" src=images/CAM_ExportTemplate.svg  style="width:24px;"> [Export Template](CAM_ExportTemplate.md) tool provides a convenient mechanism to save commonly used Job definitions from within an existing Job. This facilitates the setup of future Jobs, that are largely similar, by allowing Job template import during the Job creation process.

The **Edit → Preferences... → CAM → Job Preferences → Defaults → Template** sets the default template.

## Usage

1.  Select the **CAM → <img src="images/CAM_ExportTemplate.svg" width=16px> Export Template** option from the menu.
2.  Select elements for inclusion from the **Export Template** configuration dialog.
3.  The template must be saved in the Macro directory or the CAM directory, as configured in the [CAM Preferences](CAM_Preferences.md).
4.  The template name must follow the pattern of **job_<template name>.json**. When shown in the selection combobox, the **job_** prefix and the extension are left out.
5.  Press the **OK** button and save the template.

## Options

## Post Processing 

-   Postprocessor selection
-   Postprocessor arguments
-   Output file name

## Stock

-   Extent: Stock Size
-   Placement: Stock Location

## Setup Sheet 

-   Operation Heights
-   Operation Depths
-   Tool Rapid Speeds

## Tool controllers 

-   Selected Tool controllers.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM ExportTemplate/en
