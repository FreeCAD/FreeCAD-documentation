---
- GuiCommand:   Name:Mesh ImportMesh‏‎   MenuLocation:Meshes → Import Mesh   Workbenches:[SeeAlso:[[Std_Import|Std Import](Mesh_Workbench___Mesh]].md)---


</div>


<div class="mw-translate-fuzzy">

## Introducere


</div>


<div class="mw-translate-fuzzy">

Acest instrument vă permite să importați un obiect mesh ca fișier [\*.STL](https://en.wikipedia.org/wiki/STL_(file_format)), [\*.AST](https://en.wikipedia.org/wiki/STL_(file_format)#ASCII_STL), \*.BMS, [\*.OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file), [\*.OFF](http://en.wikipedia.org/wiki/OFF), [\*.iv](http://web.mit.edu/ivlib/www/iv/files.html), [\*.PLY](https://en.wikipedia.org/wiki/PLY_(file_format)) from the current document.


</div>


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

1.  Faceți clic pe<img alt="" src=images/Mesh_ImportMesh.png  style="width:32px;"> or choose **Mesh** → **<img src="images/Mesh_ImportMesh.png" width=24px>  Import Mesh...** din meniul principal.
2.  Selectați fișierul de importat


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
