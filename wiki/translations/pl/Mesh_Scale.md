---
- GuiCommand:
   Name: Mesh Scale
   Name/pl: Siatka Skaluj
   MenuLocation: Siatki -> Skaluj ...
   Workbenches: Mesh_Workbench/pl
---

# Mesh Scale/pl



## Opis

Polecenie **Skaluj** skaluje obiekty siatkowe.



## Użycie

1.  Wybierz jeden lub więcej obiektów siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_Scale.svg" width=16px> [Skaluj](Mesh_Scale.md)**.
    -   Wybierz z menu opcję**Siatki → <img src="images/Mesh_Scale.svg" width=16px> Skaluj ...**.
3.  Otworzy się okno dialogowe **Skaluj**.
4.  Określ współczynnik skalowania, wartość musi być większa niż {{Value|0}}.
5.  Naciśnij przycisk {{button|OK}}, aby zakończyć polecenie.



## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby skalować siatkę użyj jej metody `transformGeometry`.


```python
import FreeCAD as App
import Mesh

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(10, 10, 10)
msh.ViewObject.DisplayMode = "Flat Lines"

# Create and scale a matrix:
mat = App.Matrix()
mat.scale(2.0, 3.0, 4.0) # Unequal scaling.

# We need to work on a copy of the msh.Mesh object:
new_msh = msh.Mesh.copy()

# Transform that copy:
new_msh.transformGeometry(mat)

# Update msh.Mesh:
msh.Mesh = new_msh
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Scale/pl
