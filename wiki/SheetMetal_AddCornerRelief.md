---
 GuiCommand:
   Name: SheetMetal AddCornerRelief
   MenuLocation: SheetMetal , Add Corner Relief
   Workbenches: SheetMetal_Workbench
   Shortcut: **C** **R**
---

# SheetMetal AddCornerRelief

## Description

The <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> **SheetMetal AddCornerRelief** command adds a corner relief. A relief is usually created at corners where two bends meet, but the command can also create a relief at an open corner.

The command can only create one relief at a time.

 <img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width:300px;">  
*Default corner of two bends → Corner with added corner relief*

 <img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width:300px;">  
*Default open corner → Open corner with added corner relief*

## Usage

1.  Select two edges of a corner.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief.md)** button.
    -   Select the **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Add Corner Relief** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Add Corner Relief** option from the context menu.
    -   Use the keyboard shortcut: **C** then **R**.
3.  The **Generate Sheet Metal base shape** [Task panel](Task_panel.md) opens (introduced in version 0.5.00).
4.  Optionally press the **Select** button to reselect the edges.
    -   Press the **Preview** button to finish the selection and display the changes.
5.  Optionally adjust the parameters in the Task panel.
6.  Press the **OK** button to finish the command and close the Task panel.
7.  A **CornerRelief** object will be created consisting of one new corner relief at the selected corner.
8.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

## Relief shapes 

The shape of a corner relief can be altered by changing its property values:

The value of the property **ReliefSketch** can be chosen from a list: {{value|Circle}} (default), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{value|Circle}}and {{value|Square}} use the value of the property **Size** to scale the relief.

-    {{value|Circle-Scaled}}and {{value|Square-Scaled}} use the value of the property **Size Ratio** to scale the relief.

-    {{value|Sketch}}activates the use of the sketch listed in the property **Sketch** to define the relief shape.

 <img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width:200px;">  
*Circular relief (default settings) → Square relief (default settings) → Sketch based relief*

## A closer look at relief sizes 

To get an idea how and where the relief is placed we unfold a default corner without a relief.

 <img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width:200px;"> 



*Default corner of two bends → Corner with unfold solid → Corner in top view*

The next step is to open the unfold sketch, create a circle through 3 points and add a radius dimension.
Now we add a corner relief, create the corresponding unfold solid and open the first unfold sketch again.
Adding a concentric circle of 3 mm radius reveals that we have found out how the internal circle is positioned as the new circle fits perfectly into the cut-out of the relief\'s unfold solid.

 <img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width:300px;"> 



*Default corner with unfold sketch → Corner with default relief and the same unfold sketch*

Trying to set the property **Size** to a value below the determined 1,67 mm will result in an error; any value above should work fine.

Switching to Circle-Scaled and creating another unfold solid shows that 1,67 mm is the base for the property **Size Ratio**, too.

## Notes

-   The k factor defines where within the thickness of a sheet the neutral axis is located according to the ANSI standard.
-   The selection accepts more than two edges, but only the first two edges are taken into account.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal CornerRelief object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Parameters}}

-    **ReliefSketch|Enumeration**: \"Corner Relief Type\". {{value|Circle}} (default), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    **Size|Length**: \"Size of Shape\". Default: {{value|3,00 mm}}.

-    **Size Ratio|Float**: \"Size Ratio of Shape\". Default: {{value|1,50}}.

-    **base Object|LinkSub**: \"Base Object\". Links to the pair of edges defining the Corner Relief position.

-    **kfactor|FloatConstraint**: \"Neutral Axis Position\". Default: {{value|0,50}}.


{{Properties_Title|Parameters1}}

-    **Sketch|Link**: \"Corner Relief Sketch\".

-    **XOffset|Distance**: \"Gap from side one\". Default: {{value|0,00 mm}}.

-    **YOffset|Distance**: \"Gap from side two\". Default: {{value|0,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddCornerRelief
