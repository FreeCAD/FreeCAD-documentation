---
- GuiCommand:
   Name:Base ExampleCommandModel
   Icon: 
   MenuLocation:Menu → Submenu → Menu text for the command
   Workbenches:[Workbench](Workbench_Name.md)
   Shortcut:**F** **C**
   Version:0.19
   SeeAlso: 
---

# GuiCommand model/pt-br

## Description

While the page is under construction, add the _ template at the top of the page by simply typing: ****

In this first paragraph give a short description of what the command does. The description can refer to other workbenches such as the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md). (*Editor note:* The image is 24px, not 16px)

Remember to use _, _, _ and _ when applicable.

For example: The feature to utilize `App::Link` <small>(v0.19)</small>  allows linking between sub-assemblies etc\...

Add an image if possible, and please follow the guidelines in [WikiPages\#Graphics](WikiPages#Graphics.md). Example taken from [Part Sweep](Part_Sweep.md): ![](images/Part_Sweep_simple.png ) 
*Optional: add a caption below the image to explain what the tool does*

Closing and opening translate tags should surround images, and other fixed elements, if they don\'t need to be translated. The caption should always be translated.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Open.svg" width=16px> _ template, it is necessary to link to the command as shown in this example)
    -   Select the **Menu → Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the menu. (*Editor note:* This uses the _ template)
    -   Select the **Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the _ template, not all commands can be accessed from a context menu)
    -   Use the keyboard shortcut **F** then **C** or **Ctrl**+**Z**. (*Editor note:* This uses the _ template, not all commands have a keyboard shortcut)
2.  Detailed steps as needed. Some steps may need **Keyboard** presses while others may require using the mouse to click on a **Button**.
3.  Other commands may need to be referenced/used. Consider linking to their wiki pages along with their icons **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** or **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.
4.  Set options and press **OK**.

## Options

-   Optional. List the command options here. Check out two examples, **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** and **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.

## Example

Optional.

## Notes

-   Optional. Use a bullet list if there are multiple items. You can also mention limitations here.

## Properties

### Data


{{TitleProperty|Property Group}}

-    **Property Name 1**: Description of the property

### View


{{TitleProperty|Property Group}}

-    **Property Name 2**: Description of the property

## Scripting

See also: _ and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ExampleCommandModel tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Object = makeExampleCommandModel(Data1, Data2)
```

-   Creates an `Object` using `Data1` and `Data2`.

Example:


```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```

## Other

Optional.

## Selectable block 


<languages/>

<translate>



{{GuiCommand
|Name=Base ExampleCommandModel
|Icon= 
|MenuLocation=Menu → Submenu → Menu text for the command
|Workbenches=[Workbench](Workbench_Name.md)
|Shortcut=**F** **C**
|Version=0.19
|SeeAlso= 
}}

== Description ==

While the page is under construction, add the [[Template:UnfinishedDocu]] template at the top of the page by simply typing: ''''''

In this first paragraph give a short description of what the command does. The description can refer to other workbenches such as the <img src="images/Workbench_Sketcher.svg" width=24px> [Sketcher Workbench](Sketcher_Workbench.md). (''Editor note:'' The image is 24px, not 16px)

Remember to use [[Template:Version]], [[Template:VersionMinus]], [[Template:VersionPlus]] and [[Template:Obsolete]] when applicable.

For example: The feature to utilize `App::Link` <small>(v0.19)</small>  allows linking between sub-assemblies etc...

Add an image if possible, and please follow the guidelines in [Part Sweep](WikiPages#Graphics]]. Example taken from [[Part_Sweep.md):
</translate>
![](images/)
<translate>

*Optional: add a caption below the image to explain what the tool does*

Closing and opening translate tags should surround images, and other fixed elements, if they don't need to be translated. The caption should always be translated.

== Usage ==

# There are several ways to invoke the command: 
#* Press the **<img src="images/Std_Open.svg" width=16px> [Base ExampleCommandModel](GuiCommand_model.md)** button. (''Editor note:'' This uses the [[Template:Button]] template, it is necessary to link to the command as shown in this example)
#* Select the **Menu → Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the menu. (''Editor note:'' This uses the [[Template:MenuCommand]] template)
#* Select the **Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu. (''Editor note:'' This also uses the [[Template:MenuCommand]] template, not all commands can be accessed from a context menu)
#* Use the keyboard shortcut **F** then **C** or **Ctrl**+**Z**. (''Editor note:'' This uses the [[Template:KEY]] template, not all commands have a keyboard shortcut)
# Detailed steps as needed. Some steps may need **Keyboard** presses while others may require using the mouse to click on a **Button**.
# Other commands may need to be referenced/used. Consider linking to their wiki pages along with their icons **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** or **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.
# Set options and press **OK**.

== Options ==

* Optional. List the command options here. Check out two examples, **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** and **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.

== Example ==

Optional.

== Notes ==

* Optional. Use a bullet list if there are multiple items. You can also mention limitations here.

== Properties ==

=== Data ===

{{TitleProperty|Property Group}}

* **Property Name 1**: Description of the property

=== View ===

{{TitleProperty|Property Group}}

* **Property Name 2**: Description of the property

== Scripting ==

See also: _.

The ExampleCommandModel tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

</translate>
```python
Object = makeExampleCommandModel(Data1, Data2)
```
<translate>

* Creates an `Object` using `Data1` and `Data2`.

Example:

</translate>
```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```
<translate>

== Other ==

Optional.




</translate>
{{Workbench Tools navi}} 






{{Workbench Tools navi

}} 

_

---
[documentation index](../README.md) > [API]] and ](Category_API]] and .md) > GuiCommand model/pt-br
