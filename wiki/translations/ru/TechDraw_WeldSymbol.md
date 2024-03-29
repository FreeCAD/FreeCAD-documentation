---
 GuiCommand:
   Name/ru: Добавить информацию о сварке в линию-выноску
   Name: TechDraw_WeldSymbol
   MenuLocation: TechDraw , Добавить информацию о сварке в линию-выноску
   Workbenches: TechDraw_Workbench/ru
   Version: 0.19
   SeeAlso: TechDraw_LeaderLine/ru
---

# TechDraw WeldSymbol/ru


</div>



## Описание

The **TechDraw WeldingSymbol** tool adds welding specifications to an existing leader line.

<img alt="" src=images/TechDraw_WeldingSymbol_example.png  style="width:330px;"> 
*Welding specification added to a leader line*



## Применение

1.  Select an existing [leaderline](TechDraw_LeaderLine.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_WeldSymbol.svg" width=16px> [Add Welding Information to Leaderline](TechDraw_WeldSymbol.md)** button.
    -   Select the **TechDraw → Symbols → <img src="images/TechDraw_WeldSymbol.svg" width=16px> Add Welding Information to Leaderline** option from the menu.
3.  A task panel opens.
4.  Specify the welding symbols and accompanying text to be added to the leader line.
5.  Press the **OK** button.

## Notes

-   After creation a welding symbol can be edited by double clicking it in the [Tree view](Tree_view.md).
-   There is a [preference parameter](TechDraw_Preferences.md) for the default welding symbol directory. You can add your own symbols in a personal directory.



## Свойства

### Weld Symbol 

-    **All Around**: Shows the *All Around* symbol (circle) at the kink in the leader line.

-    **Field Weld**: Show the *Field Weld* symbol (flag) at the kink in the leader line.

-    **Alternate Weld**: Offsets the lower symbol to indicate alternating welds.

-    **Tail Text**: Text to be shown at the end of the leader line.



### Заголовок

Each individual symbol (\"arrow side\" and \"other side\") is represented by a \"tile\" object. A Welding Symbol has 1 or 2 tiles associated with it. Each of it has the following properties:

-    **Tile Parent**: The parent Weld Symbol

-    **Tile Row**: Row of the tile. 0 means above the line, -1 below the line. **Note:** If you change the row of one tile, you must also change the tile for the second side! This way you can flip the sides.

-    **Tile Column**: Column of the tile. At the moment it is always 0, therefore the property is not editable.

-    **Symbol File**: Directory and file name of the symbol\'s SVG file.

-    **Symbol Included**: Directory and file name of the actual included symbol SVG file. (It is a temporary directory.)

-    **Left Text**: Text to be displayed to the left of the SVG symbol.

-    **Center Text**: Text to be displayed above/below the SVG symbol.

-    **Right Text**: Text to be displayed to the right of the SVG symbol.



## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The WeldingSymbol tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
symbolName = "DrawWeldSymbol001")
symbolType = "TechDraw::DrawWeldSymbol"
App.activeDocument().addObject(symbolType, symbolName)
App.activeDocument().Page.addView(App.activeDocument().DrawWeldSymbol001)
App.activeDocument().DrawWeldSymbol001.Leader = myLeader
App.activeDocument().DrawWeldSymbol001.AllAround = True
App.activeDocument().DrawWeldSymbol001.FieldWeld = True
App.activeDocument().DrawWeldSymbol001.AlternatingWeld = True
App.activeDocument().DrawWeldSymbol001.TailText = "process text"

tileName = "DrawTileWeld001"
tileType = "TechDraw::DrawTileWeld"
App.activeDocument().addObject(tileType, tileName)
App.activeDocument().DrawTileWeld001.TileParent = App.activeDocument().DrawWeldSymbol001
App.activeDocument().DrawTileWeld001.TileRow = 0
App.activeDocument().DrawTileWeld001.TileColumn = 0
App.activeDocument().DrawTileWeld001.SymbolFile = fullPathToMySvgFile
App.activeDocument().DrawTileWeld001.LeftText = "left text"
App.activeDocument().DrawTileWeld001.RightText = "right text"
App.activeDocument().DrawTileWeld001.CenterText = "center text"
```

## Svg Symbol Tiles 

Individual symbols are formed by 64x64 pixel SVG files. Additional symbols can be created in an SVG program like [Inkscape](https://en.wikipedia.org/wiki/Inkscape) using one of the symbols supplied by FreeCAD as a template.

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">

-   Individual symbols are formed by 64x64 (nominal) pixel SVG files. The tiles actually have a \"border\" of 4px. The border ensures that the leader line and symbol meet nicely.
-   The symbol is drawn in black on a transparent background. The stroke width is 0.5mm.
-   The leader passes below symbols for the arrow side (see image on the left) and above symbols for the \"other\" side (see image on the right).
-   There is no particular naming standard other than to append \"Up/Down\" to the arrow/other side symbols.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw WeldSymbol/ru
