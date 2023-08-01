---
- GuiCommand:
   Name: Design456 MultiPointsToWireClose
   MenuLocation: Design456_2Ddrawing - MultiPointsToWireClose
   Workbenches: [Design456](Design456_Workbench.md)
   Shortcut: None
   SeeAlso: 
---

# Design456 MultiPointsToWireClose

## Description

The <img alt="" src=images/Design456_MultiPointsToWireClose.svg  style="width:24px;"> **Design456 Multi Points To Wire - Close** lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at felis ut urna auctor pharetra id at nulla. This tool is part of the [external workbench](external_workbenches.md) called [Design456](Design456_Workbench.md).

## Usage

1.  Switch to the <img alt="" src=images/Design456_workbench_icon.svg  style="width:24px;"> [Design456](Design456_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed)
2.  You need to select at least 2 vertices before pressing the command. Order of selecting the points is important. First point selected will be the start of the wire and the last point selected will be the end. This tool is similar to the another tool: <img alt="" src=images/Design456_MultiPointsToWireOpen.svg  style="width:24px;">[MultiPointsToWireOpen](Design456_MultiPointsToWireOpen.md), but this one is closing the wire and making a shape/surface of the wire which can be then extruded or used as a part of Loft.

## Limitations

When you select the points in the object lists, the points aren\'t green. That causes a problem for the tool at the moment. It is strange that selecting the points in the object list are not equal to select them by clicking the points with the mouse. To avoid this problem you have to select the points by the mouse and clicking them so they are green when you use the command.

## Properties


{{Properties_Title|Base}}

## Scripting



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > Design456 MultiPointsToWireClose
