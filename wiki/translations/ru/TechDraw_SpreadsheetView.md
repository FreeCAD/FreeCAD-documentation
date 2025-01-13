---
 GuiCommand:
   Name/ru: Вставить электронную таблицу
   Name: TechDraw_SpreadsheetView
   MenuLocation: TechDraw , Вставить электронную таблицу
   Workbenches: TechDraw_Workbench/ru, Spreadsheet_Workbench/ru
---

# TechDraw SpreadsheetView/ru


</div>



## Описание

The **TechDraw SpreadsheetView** tool allows you to place a view of a selected [spreadsheet](Spreadsheet_Workbench.md) on a [Page](TechDraw_Workbench.md).


<small>(v1.0)</small> 

: The [TechDraw View](TechDraw_View.md) tool can also create a Spreadsheet View.

![](images/TechDraw_Spreadsheetview.png ) 
*Spreadsheet element inserted in the TechDraw drawing page*



## Применение

1.  Select a spreadsheet in the [Tree view](Tree_view.md).
2.  If there are multiple drawing pages in the document: optionally add the desired page to the selection by selecting it in the [Tree view](Tree_view.md).
3.  Select the **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Insert Spreadsheet View** option from the menu.
4.  If there are multiple drawing pages in the document, and if no page is displayed in the [Main view area](Main_view_area.md) and you have not yet selected a page, the **Page Chooser** dialog box opens:
    1.  Select the desired page.
    2.  Press the **OK** button.
5.  A Spreadsheet View is inserted.
6.  Adjust the cell range of the view by changing its **Cell Start** and **Cell End** properties.



## Свойства

See also: [Property editor](Property_editor.md).

A Spreadsheet View, formally a {{Incode|TechDraw::DrawViewSpreadsheet}} object, has the [properties](TechDraw_View#Properties_Part_View.md) that are common to all View types. It also has the following additional properties:

### Data


{{TitleProperty|Drawing view}}

-    **Symbol|String|Hidden**: The SVG code defining this symbol.

-    **Editable Texts|StringList|Hidden**: Substitution values for the editable strings in this symbol. Not used.

-    **Owner|Link**: Feature to which this symbol is attached. <small>(v1.0)</small> 


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


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/ru
