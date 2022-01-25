# Macro ForceRecompute/en
{{Macro
|Name=Macro Force Recompute
|Icon=Force_Recompute.png
|Description=This small macro forces a manual recompute of the model.<br>Sometimes the user applies changes to the model in FreeCAD.<br>But FreeCAD does not seem to recognize them.<br>(As of <small>(v0.17)</small>  the effect of this macro can be achieved through GUI. Right-click project in model tree view, and pick "Mark to recompute" from context menu. After that, press Recompute button.)
|Author=shoogen
|Version=1.0
|Date=2014-09-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/8/88/Force_Recompute.png ToolBar Icon]
}}

## Description

Sometimes when a user applies changes to the model, FreeCAD does not seem to recognize/integrate them. In addition to that, the blue **<img src="images/Std_Refresh.svg" width=24px> [Refresh/Recompute](Std_Refresh.md)** button remains greyed out. Hence this small macro was designed to force a manual recompute of the model.

**Note:** As of <small>(v0.17)</small>  the effect of this macro can be achieved through the GUI. Right-click project in [model tree view](tree_view.md), and pick **Mark to recompute** from the context menu. What this does is make the Refresh/Recompute icon active again. Now press on the <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Refresh/Recompute](Std_Refresh.md) button to trigger a recompute.

## Usage

Run the macro when necessary.

## Script

ToolBar Icon <img alt="" src=images/Force_Recompute.png  style="width:24px;">

**Macro Force\_Recompute.py**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# Force Recompute
# macro provided by shoogen

import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
 obj.touch()
FreeCAD.ActiveDocument.recompute()

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro ForceRecompute/en
