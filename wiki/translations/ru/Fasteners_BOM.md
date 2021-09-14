---
- GuiCommand:
   Name:Fasteners BOM
   MenuLocation:Fasteners → BOM
   Workbenches:[Fasteners](Fasteners_Workbench.md)
   Shortcut:None
   SeeAlso:
---

## Описание

The <img alt="" src=images/Fasteners_BOM.svg  style="width:24px;"> [Fasteners BOM](Fasteners_BOM.md) generates a Bill of Materials. This tool is part of the [external workbench](external_workbenches.md) called [Fasteners](Fasteners_Workbench.md).

## Использование

1.  Switch to the <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners](Fasteners_Workbench.md) workbench (install from <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) is necessary, if not previously installed)
2.  Invoke the Fasteners BOM tool several ways:
    -   Press the <img alt="" src=images/Fasteners_BOM.svg  style="width:24px;"> button
    -   Use the **Fasteners → BOM** entry in the Fasteners menu
3.  When invoked the Fasteners BOM tool adds a spreadsheet to the FreeCAD document.
    -   The spreadsheet represents the BOM of fasteners used in the model feature tree.

<img alt="" src=images/BOM_example-1.FCStd.png  style="width:1000px;">

## Примечания

1.  Use the <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Spreadsheet Workbench](Spreadsheet_Workbench.md) to export the BOM to the csv format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc.

## Ограничения

## Свойства


{{Properties_Title|Base}}

-    **Label**: User name of the spreadsheet object in the [Tree view](Tree_view.md).

-    **View**: Display Mode

-    **View**: On Top When Selected, Disabled, Enabled, Object, Element, default: Disabled

-    **View**: Selection Style, Shape or BoundBox, default: Shape

-    **View**: Show In Tree, boolean, default: true

-    **View**: Visibility, boolean, default: true

## Составление скриптов 





{{Fasteners Tools navi

}} 

[Category:External Command Reference](Category:External_Command_Reference.md)
