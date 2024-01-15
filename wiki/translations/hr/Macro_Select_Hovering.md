# Macro Select Hovering/hr
{{Macro
|Name=Macro Select Hovering
|Icon=Macro_Select_Hovering.png
|Description=This macro select a choice Face, Edge, Vertex hovering by the mouse.<br/>PS: For unselected one face (or other) click the **Pause grab** and use the standard procedure : CTRL + Click 
|Author=Mario52
|Version=00.04
|Date=2024-01-11
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d8/Macro_Select_Hovering.png ToolBar Icon]
}}

## Description

this macro select a choice Face, Edge, Vertex hovering by the mouse.

![Macro Select Hovering](images/Select_Hovering00.gif )


{{Codeextralink|https://gist.githubusercontent.com/mario52a/7ebe6b3fd047441114d9d0e08ceddd63/raw/f9dea03a0327b48c76a7c3e9d7cd391b5093a8cf/Macro%2520Select%2520Hovering.FCMacro}}

![Macro Select Hovering](images/Macro_Select_Hovering_00.png )

PS: For deselect one face (or other) click the **Pause grab** and use the standard procedure : CTRL + Click

## How To Use 

Hovering element by the mouse.

#### Section Face 


{{CheckBox}}

Select Face → 3 number of face(s) {{LineEdit|300.0}} area total of selections {{LineEdit|100.0}} area of the latest selection

#### Section Edge 


{{CheckBox}}

Select Edge → 4 number of edge(s) {{LineEdit|40.0}} length total of selections {{LineEdit|10.0}} length of the latest selection

#### Section Vertex 


{{CheckBox}}

Select Vertex → 1 number of vertex(s)

#### Section Main 

Title display info of the :

-   ( Obj: 1 ) : number object(s) selected
-   ( Sub: 8 ) : number of Sub object(s) selected
-   ( Tot: 9 ) : Somme Obj + Sub


{{LineEdit|Unnamed: Box. Face6 (1.34,2.64,10.0)}}

-   display little info and info below the cursor mouse


{{ComboBox|Unnamed: 1 : (8 sel.) (Obj. 1, Fa. 3, Ed. 4, Ve. 1) }}

-   Name of document
-   8 selections
-   Obj. 1 object
-   Fa. 3 faces
-   Ed. 4 edges
-   Ve. 1 vertex
-   If you use several document the macro restores only the selection in the document open (to work)
-   The toolTip display the listing of the selected document Name and subObject

![Info objects memorized displayed](images/Macro_Select_Hovering_01.png )


**Selected by Box**

-   if you select by the Box selection this button select all objects checked of the selection
-   Other think you check the vertex option and you want selected all vertexes of the object \... click this button


**Reset Data**

-   Reset all data in the macro (not the memo)


**Reset Memo**

-   Reset the memo


**Remove selection**

-   Remove the selections in the current document

*(**PS:** if several document are open on click mouse in the 3D view remove all selection in all documents)*


**Quit**

-   Quit the macro


**Pause grab/Refresh**

-   Pause the macro for ex: deselect on of many object
-   after pause click for return on macro and upgrade al info in the macro
-   Can be use for upgrade the selections in the macro (all time)
-   Ex: many object are selected before run the macro
-   The macro adapts and detect all change of document

### Icons

The icon must be copied into the same directory as the macro

The icon ToolBar ![Macro Select Hovering](images/Macro_Select_Hovering.png )

## Script

**Macro_Select_Hovering.FCMacro**


{{CodeDownload|https://gist.github.com/mario52a/7ebe6b3fd047441114d9d0e08ceddd63| Download latest version of the macro}}

## Version

ver 00.04 (11/01/2024) : add:

-   LineEdit info,
-   ComboBox memo selection,
-   Button Memo selection,
-   Button Selected by body
-   Button Reset Data
-   Button Reset Memo
-   Button Remove Selection

ver 00.03b (28/10/2020) : add print**()** for Python 3

ver 00.03 (26/12/2017) : replace test with (FreeCAD.ActiveDocument.getObject(obj), sub) == False)

ver 00.02 (26/12/2017) :

ver 00.01 (25/12/2017) :



## Poveznica

[Multiple face selection to convert a shape to a solid](https://forum.freecadweb.org/viewtopic.php?f=3&t=26370)



---
⏵ [documentation index](../README.md) > Macro Select Hovering/hr
