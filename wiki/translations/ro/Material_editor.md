---
- GuiCommand:/ro
   Name/ro:Material editor
   Icon:Arch_Material_Group.svg
   MenuLocation:Model → Material → Material editor
   Workbenches:[FEM](FEM_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# Material editor/ro


</div>

## Description


<div class="mw-translate-fuzzy">

Editorul de materiale vă permite să editați și să salvați informațiile conținute într-un material [FreeCAD](Material.md). În prezent, astfel de materiale sunt folosite de Atelierele de lucru [FEM](FEM_Workbench.md) și [Arch](Arch_Workbench.md).


</div>

![](images/Material_editor.jpg )


<div class="mw-translate-fuzzy">

Editorul de material poate fi accesat în mod curent de:


</div>

The material editor can currently be accessed by either:


<div class="mw-translate-fuzzy">

-   The **Edit material** button of the [new material](Arch_SetMaterial.md) creation panel of the [Arch Workbench](Arch_Workbench/ro.md)
-   Via python:


</div>

## Opțiuni


<div class="mw-translate-fuzzy">

-   **Browser button**: Descide conținutul proprietății URL într-un browser
-   **Material card**: Permite alegerea unei umpleri predefinite a câmpurilor
-   **Open**: Deschide un fișier .FCMat
-   **Save as**: Salvează conținutul editorului ca pe un nou fișier .FCMat
-   **Preview**: Not implemented yet
-   **Properties editor**:Permite editarea conținutului proprietăților materialelor
-   **Add property**: Permite să se adauge o npouă proprietate persoanlizată
-   **Delete property**: Permite editarea conținutului proprietăților materialelor


</div>

Note:


<div class="mw-translate-fuzzy">

-   Butoanele **OK** și **Cancel** au același efect atunci când Material editor nu este utilizat pentru editarea directă a proprietății materialului în obiectul existent.


</div>

## Scripting


```python
import MaterialEditor
MaterialEditor.openEditor()
```


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Arch](Category_Arch.md) > [Material](Material_Workbench.md) > Material editor/ro
