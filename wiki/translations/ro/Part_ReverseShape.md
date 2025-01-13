---
 GuiCommand:
   Name: Part ReverseShape‏‎
   MenuLocation: Part , Reverse Shapes
   Workbenches: Part Workbench
---

# Part ReverseShape/ro


</div>




<div class="mw-translate-fuzzy">

## Introducere

Flips the normals of all faces of the selected object.


</div>

The <img alt="" src=images/Part_ReverseShape.svg  style="width:24px;"> **Part ReverseShape** command creates parametric copies with reversed face normals from selected objects.




<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați forma.
2.  Selectați ** Part** → **Reverse shapes** din meniul principal.
3.  O formă inversată este creată ca un nou obiect separat.


</div>

1.  Select one or more objects.
2.  Select the **Part → <img src="images/Part_ReverseShape.svg" width=16px> Reverse shapes** option from the menu.
3.  For each selected object a reversed shape is created.




<div class="mw-translate-fuzzy">

## Note

Prin executarea acestei comenzi, FreeCAD inversează(cu susul în jos) normalele tuturor fețetelor formei / solidului.
Puteți verifica prin :

1.  ascundeți toate celelalte obiecte, cu excepția formei/solidului inversat(ă)
2.  selectați forma/solidul inversat(ă)
3.  schimbați tab-ul \"iluminarea\" în \"Vizualizare\" din \"Două laturi\" în \"O singură parte\"
4.  forma/solidul va deveni negru → vă uitați la partea din spate a fațetelor


</div>

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 
-   To see the effect of the command change the **Lighting** property of the reversed shape to {{Value|On side}} and if required change **Edit → Preferences... → Display → 3D View → Rendering → Backlight color**.

## Properties

See also: [Property editor](Property_editor.md).

A Part ReverseShape object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional property:

### Data


{{TitleProperty|Reverse}}

-    **Source|Link**: specifies the linked source shape.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/ro
