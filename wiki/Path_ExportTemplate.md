---
- GuiCommand:
   Name:Path ExportTemplate
   MenuLocation:Path → Export Template
   Workbenches:[Path](Path_Workbench.md)
   SeeAlso:[Path SetupSheet](Path_SetupSheet.md)
---

## Description

Exporting Job templates provides a convenient mechanism to save commonly used Job definitions from within an existing Job. This facilitates the setup of future Jobs, that are largely similar, by allowing Job template import during the Job creation process.

The {{MenuCommand|Edit → Preferences... → Path → Job Preferences tab, Defaults → Template}} sets the default template.

## Usage

1.  Select the {{MenuCommand|Path → <img src="images/Path_ExportTemplate.svg" width=16px> Export Template}} option from the menu.
2.  Select elements for inclusion from the {{MenuCommand|Export Template}} configuration dialog.
3.  The template must be saved in the Macro directory or the Path directory, as configured in the [Path Preferences](Path_Preferences.md).
4.  The template name must follow the pattern of {{FileName|job_<template name>.json}}. When shown in the selection combobox, the {{FileName|job_}} prefix and the extension are left out.
5.  Press the **OK** button and save the template.

## Options

## Post Processing {#post_processing}

-   Postprocessor selection
-   Postprocessor arguments
-   Output file name

## Stock

-   Extent: Stock Size
-   Placement: Stock Location

## Setup Sheet {#setup_sheet}

-   Operation Heights
-   Operation Depths
-   Tool Rapid Speeds

## Tool controllers {#tool_controllers}

-   Selected Tool controllers.




 {{Path_Tools_navi}} 
