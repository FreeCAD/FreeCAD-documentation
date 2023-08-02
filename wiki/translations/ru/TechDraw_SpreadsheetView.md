---
- GuiCommand:
   Name/ru: Вставить электронную таблицу
   Name: TechDraw_SpreadsheetView
   MenuLocation: TechDraw -> Вставить электронную таблицу
   Workbenches: TechDraw_Workbench/ru, Spreadsheet_Workbench/ru
---

# TechDraw SpreadsheetView/ru


</div>



## Описание

The **TechDraw SpreadsheetView** tool allows you to place a view of a selected [spreadsheet](Spreadsheet_Workbench.md) on a [Page](TechDraw_Workbench.md).

![](images/TechDraw_Spreadsheetview.png ) 
*Spreadsheet element inserted in the TechDraw drawing page*



## Применение

1.  Select a single spreadsheet in the [Tree view](Tree_view.md).
2.  If there are multiple drawing pages in the document: optionally add the desired page to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> [Insert Spreadsheet View](TechDraw_SpreadsheetView.md)** button.
    -   Select the **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Insert Spreadsheet View** option from the menu.
4.  If there are multiple drawing pages in the document and you have not yet selected a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.
5.  Adjust the cell range of the view by changing its **Cell Start** and **Cell End** properties.

## Notes

-   In {{VersionMinus|0.19}} some characters in spreadsheet cells will cause errors when displayed in a Spreadsheet View. These characters have to be XML encoded. Currently known characters are: {{Incode|&}} (replace with {{Incode|&amp;amp;}}) and {{Incode|&lt;}} (replace with {{Incode|&amp;lt;}}). See also this [discussion](https://forum.freecadweb.org/viewtopic.php?p=629853#p629885) in the forum.



## Свойства

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Spreadsheet}}

-    **Source|Link**: The spreadsheet to be added to the page.

-    **Cell Start|String**: The top left cell of the cell range to be included in this view.

-    **Cell End|String**: The bottom right cell of the cell range to be included in this view.

-    **Font|Font**: The name of the font used for texts.

-    **Text Color|Color**: The color of texts and lines that have no color specified in the spreadsheet.

-    **Text Size|Float**: The font size of texts.

-    **Line Width|Float**: The width of the cell borders.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/ru
