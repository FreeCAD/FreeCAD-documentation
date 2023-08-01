# FreeCAD and DXF Import/en
{{TOCright}}

## Background

DXF is a proprietary CAD data format for 2D drawings that originated with AutoCAD. More details can be found on the [DXF](DXF.md) wiki page.

## Introduction

Since FreeCAD version 0.18 there is a new C++ DXF importer, and since version 0.19 also a new C++ DXF exporter. These new components are installed with FreeCAD.

To use the older, legacy, DXF importer and exporter you need to install several files. These files cannot be included with FreeCAD since they use libraries published under a license that is not compatible with FreeCAD.

## How to install the legacy DXF importer and exporter 

### Automatically

If the files are not already installed, go to the menu **Edit → Preferences → Import-Export → DXF** and enable the option **Allow FreeCAD to automatically download and update the DXF libraries** to make FreeCAD automatically download and install them.

For FreeCAD 0.14 or older you have to install manually:

### Manually

1.  Go to [Yorik\'s Github account](https://github.com/yorikvanhavre/Draft-dxf-importer) and download these files (on the right side you can choose \"download as ZIP\").
2.  Put the files in your macro folder.
3.  If you are unsure where this folder is, go to **Edit → Preferences → General → Macro** and check the field named **Macro Path**.

-   In Ubuntu your macro folder is normally (the folder is hidden, you may need to unhide it):

/home/your_user_name/.FreeCAD 

-   In Windows your macro folder is normally:

C:\Users\your_user_name\AppData\Roaming\FreeCAD

See also: [Dxf Importer Install](Dxf_Importer_Install.md)

## Tips and Tricks 

Sometimes DXF Files don\'t import although they open in other CAD-Programs without problems.

You can try:

1.  Go to **Edit → Preferences → Import-Export → DXF** and untick the option **Join geometry** and try again.
2.  Remember that maybe now you won\'t have coincident endpoints. You can make them coincident with [Sketcher ValidateSketch](Sketcher_ValidateSketch.md)

You can also try:

1.  Go to **Edit → Preferences → Draft → General settings** and adjust the value of **Tolerance** (default: 0,05) and try again.

For an overview of all DXF related preferences see [Import Export Preferences](Import_Export_Preferences#DXF.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/en
