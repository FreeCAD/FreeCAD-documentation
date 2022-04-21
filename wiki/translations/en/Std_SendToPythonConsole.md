---
- GuiCommand:
   Name:Std SendToPythonConsole
   MenuLocation:Edit → Send to Python Console
   Workbenches:All
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

# Std SendToPythonConsole/en

## Description

The **Std SendToPythonConsole** command creates variables in the [Python console](Python_console.md) referencing a selected object and its selected subshapes, along with some other useful references. The variables and the code involved can be used in the development of Python code.

Depending on the selected object and its selected subshapes, if any, the following variables are created:

+++
| Variable name   | Referenced object(s)                                                                                                                                    |
+=================+=========================================================================================================================================================+
|  | The document containing the selected object                                                                                                             |
| {{Incode|doc}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | The selected Link object (only created if the selected object is a Link)                                                                                |
| {{Incode|lnk}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | Depending on the selected object:                                                                                                                       |
| {{Incode|obj}}  | The selected object itself (if the selected object is not a Link)                                                                                       |
|              | The Linked object (if the selected object is a Link)                                                                                                    |
+++
|  | Depending on the type of {{Incode|obj}}:                                                                                                  |
| {{Incode|shp}}  | The {{Incode|Shape}} property of {{Incode|obj}} (for objects derived from the {{Incode|Part::Feature}} class) |
|              | The {{Incode|Mesh}} property of {{Incode|obj}} (for Mesh objects)                                                           |
|                 | The {{Incode|Points}} property of {{Incode|obj}} (for Points objects)                                                       |
+++
|  | The first selected subshape (only created if at least one subshape is selected)                                                                         |
| {{Incode|sub}}  |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++
|  | A list containing all subshapes (only created if two or more subshapes are selected)                                                                    |
| {{Incode|subs}} |                                                                                                                                                         |
|              |                                                                                                                                                         |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try:
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception:
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole



*Example output: an edge, a face, and a vertex of a [Link](Std_LinkMake.md) to a [Part Box](Part_Box.md) were selected*

## Usage

1.  Select a single object or one or more subshapes belonging to a single object.
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console** option from the menu.
    -   Select the **<img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Ctrl**+**Shift**+**P**.
3.  If required the [Python console](Python_console.md) opens.
4.  The [Python console](Python_console.md) receives the keyboard focus.

## Notes

-   All previously created variables are deleted each time the command is run.

-   If the selected object is a Link ({{Incode|App::Link}}) and the Linked object is derived from the {{Incode|Part::Feature}} class, the {{Incode|shp}} variable will be the shape of the Linked object. If the Link has been transformed or scaled and you want to access the scaled/transformed shape, you can do so with this code:

:   
    
```pythonlnk_shp = Part.getShape(lnk)```
    





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SendToPythonConsole/en
