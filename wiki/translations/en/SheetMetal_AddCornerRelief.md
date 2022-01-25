---
- GuiCommand:
   Name:SheetMetal AddCornerRelief
   MenuLocation:SheetMetal → Add Corner Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**C** **R**
---

# SheetMetal AddCornerRelief/en

## Description

The <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> **SheetMetal AddCornerRelief** command adds a corner relief to a corner.

## Usage

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal CornerRelief object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


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
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/en
