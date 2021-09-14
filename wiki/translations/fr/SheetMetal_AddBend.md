---
- GuiCommand:/fr
   Name:SheetMetal AddBend
   Name/fr:SheetMetal Transformation en pli
   MenuLocation:SheetMetal → Make Bend
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **B**
---

## Description

La commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> **SheetMetal AddBend** plie une tôle selon une ligne choisie.

## Utilisation

## Propriétés

See also: [Property editor](Property_editor.md).

A SheetMetal SolidBend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base object\". Links to the edges to be bent.

-    **radius|Length**: \"Bend Radius\". Default: {{value|1,00 mm}}.

-    **thickness|Length**: \"Thickness of sheetmetal\". Default: {{value|1,00 mm}}.




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
