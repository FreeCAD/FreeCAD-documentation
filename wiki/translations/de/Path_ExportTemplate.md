---
 GuiCommand:
   Name: Path ExportTemplate
   Name/de: Pfad ExportVorlage
   MenuLocation: Pfad , Export Vorlage
   Workbenches: Path_Workbench/de
   SeeAlso: Path_SetupSheet
---

# Path ExportTemplate/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Path_ExportTemplate.svg  style="width:24px;"> [Path VorlageExportieren](Path_ExportTemplate/de.md) enthält einen bequemen Mechanismus zum Speichern häufig verwendeter Auftragsdefinitionen aus einem bestehenden Auftrag heraus. Dies erleichtert die Einrichtung zukünftiger Aufträge, die weitgehend ähnlich sind, indem der Import von Auftragsvorlagen während des Prozesses der Auftragserstellung ermöglicht wird.

Der **Bearbeiten → Voreinstellungen... → Pfad →  Auftragseinstellungen → Standardwerte → Vorlage** legt die Standardvorlage fest.



## Anwendung

1.  Select the **Path → <img src="images/Path_ExportTemplate.svg" width=16px> Export Template** option from the menu.
2.  Select elements for inclusion from the **Export Template** configuration dialog.
3.  The template must be saved in the Macro directory or the Path directory, as configured in the [Path Preferences](Path_Preferences.md).
4.  The template name must follow the pattern of **job_<template name>.json**. When shown in the selection combobox, the **job_** prefix and the extension are left out.
5.  Press the **OK** button and save the template.



## Optionen

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





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ExportTemplate/de
