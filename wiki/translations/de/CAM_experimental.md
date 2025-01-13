# CAM experimental/de
## Beschreibung

The CAM Workbench contains a set of hidden commands. They are hidden by default because they are experimental. A command can be considered experimental for any of the following reasons:

-   It is incomplete.
-   It is bug-ridden.
-   It is unstable.
-   It does not produce correct, stable, safe, paths.
-   It is not a standard, regularly used command in the traditional CAM workflow.
-   It is mature but has not yet been moved to the standard tool list.
-   \... other reasons.



## Experimentelle Befehle aktivieren 

To access the hidden experimental commands of the CAM Workbench, the user must enable them in the [Parameter Editor](Std_DlgParameter.md).

1.  Open the [Parameter Editor](Std_DlgParameter.md) via **Tools → Edit Parameters...**
2.  Once in the editor the path is **BaseApp → Preferences → Mod → CAM**
3.  To enable the [CAM Area](CAM_Area.md) and [CAM Area Workplane](CAM_Area_Workplane.md) commands:
    -   Right-click in the parameter list area and select **New → New Boolean item** from the context menu.
    -   Name the new parameter: `EnableAdvancedOCLFeatures` (case-sensitive).
    -   Set it to: `True`.
4.  To enable the other experimental commands:
    -   Again select **New → New Boolean item** from the context menu.
    -   Name the new parameter: `EnableExperimentalFeatures` (case-sensitive).
    -   Set it to: `True`.
5.  Save the settings.
6.  Restart FreeCAD.

## Additional Information 

Read more about the specific experimental commands on the [wiki pages that link to this one](https://www.freecadweb.org/wiki/Special:WhatLinksHere/CAM_experimental).


 {{CAM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [CAM](CAM_Workbench.md) > CAM experimental/de
