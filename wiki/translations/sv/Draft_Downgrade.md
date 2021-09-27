# Draft Downgrade/sv
---
- GuiCommand:/sv   Name:Draft Downgrade   Name/sv:Draft Downgrade   Workbenches:_---


</div>

## Beskrivning


<div class="mw-translate-fuzzy">

Detta verktyg nedgraderar valda objekt på olika sätt. Om inget objekt är markerat, så kommer du att ombes att välja ett.


</div>

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width:400px;"> 
*Two overlapping faces are downgraded to a Part Cut object, which is downgraded to a face. That face is then downgraded to a closed wire, which is finally downgraded to separate edges.*


<div class="mw-translate-fuzzy">

## Bruk


</div>

1.  Optionally select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Downgrade.svg" width=16px> [Draft Downgrade](Draft_Downgrade.md)** button.
    -   Select the **Modification → <img src="images/Draft_Downgrade.svg" width=16px> Downgrade** option from the menu.
    -   Use the keyboard shortcut: **D** then **N**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).

## Scripting

See also: _.

To downgrade objects use the `downgrade` method of the Draft module.


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```

-    `objects`contains the objects to be downgraded. It is either a single object or a list of objects.

-   If `delete` is `True` the source objects are deleted.

-    `force`forces a certain way of downgrading by calling a specific internal function. It can be: `"explode"`, `"shapify"`, `"subtr"`, `"splitFaces"`, `"cut2"`, `"getWire"`, `"splitWires"` or `"splitCompounds"`.

-    `downgrade_list`is returned. It is a list containing two lists: a list of new objects and a list of objects to be deleted. If `delete` is `True` the second list is empty.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=True)

compound = add_list1[0]
add_list2, delete_list2 = Draft.downgrade(compound, delete=False)
face = add_list2[0]
add_list3, delete_list3 = Draft.downgrade(face, delete=False)

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/sv
