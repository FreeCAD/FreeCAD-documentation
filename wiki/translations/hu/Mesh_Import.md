---
- GuiCommand:   Name:Mesh ImportMesh   MenuLocation:Hálók → Háló importálása   Workbenches:[SeeAlso:[[Std_Import|Std Import](Mesh_Workbench___Háló]].md)---


</div>


<div class="mw-translate-fuzzy">

## Bemutatás


</div>


<div class="mw-translate-fuzzy">

Ez az eszköz lehetővé teszi egy [\*.STL](https://en.wikipedia.org/wiki/STL_(file_format)), [\*.AST](https://en.wikipedia.org/wiki/STL_(file_format)#ASCII_STL), \*.BMS, [\*.OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file), [\*.OFF](http://en.wikipedia.org/wiki/OFF), [\*.iv](http://web.mit.edu/ivlib/www/iv/files.html), [\*.PLY](https://en.wikipedia.org/wiki/PLY_(file_format)) fájl hozzáadását a jelenlegi dokumentumhoz.


</div>


<div class="mw-translate-fuzzy">

## Használat


</div>


<div class="mw-translate-fuzzy">

1.  Kattintson a <img alt="" src=images/Mesh_ImportMesh.png  style="width:32px;"> ikonra vagy válassza a **Hálók** → **<img src="images/Mesh_ImportMesh.png" width=24px> Háló importálása…** menüpontot a felső menüből.
2.  Válassza ki az importálandó fájlt.


</div>

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Properties

See: [Mesh Feature](Mesh_Feature.md).

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To import a mesh file use the `insert` method of the Mesh module.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```





{{Mesh Tools navi

}}  
