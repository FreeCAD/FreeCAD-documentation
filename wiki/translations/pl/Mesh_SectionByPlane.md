---
- GuiCommand:
   Name: Mesh SectionByPlane
   Name/pl: Siatka: Utwórz przekrój siatki płaszczyzną
   MenuLocation: Siatki -> Cięcie -> Utwórz przekrój siatki płaszczyzną
   Workbenches: Mesh_Workbench/pl
   SeeAlso: Mesh_CrossSections/pl
---

# Mesh SectionByPlane/pl



## Opis

Polecenie **Utwórz przekrój siatki płaszczyzną** tworzy przekrój przez obiekt siatki. Przekrój jest [cechą Części](Part_Feature/pl.md).



## Użycie

1.  Wybierz pojedynczy obiekt siatki i pojedynczą [Płaszczyznę](Part_Primitives/pl.md) środowiska Część. Płaszczyzna *(jej przedłużenie)* powinna przecinać obiekt siatki.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Mesh_SectionByPlane.svg" width=16px> '''Utwórz przekrój siatki płaszczyzną'''**.
    -   Wybierz z menu opcję **Siatki → Cięcie → <img src="images/Mesh_SectionByPlane.svg" width=16px> Utwórz przekrój siatki płaszczyzną**.



## Właściwości

Zapoznaj się z informacjami na stronie: [cecha](Part_Feature/pl.md) środowiska Część.



## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby podzielić siatkę użyj jej metody `section`. Metoda wymaga drugiego obiektu siatki, który nie musi być planarny.


```python
import FreeCAD as App
import Mesh
import Part

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(30, 40, 50)
msh.ViewObject.DisplayMode = "Flat Lines"

# Create a planar mesh from 3 points:
p1 = App.Vector(-20, -60, 0)
p2 = App.Vector(65, 25, 0)
p3 = App.Vector(-20, 25, 0)
msh_plane = Mesh.Mesh([p1, p2, p3])

# Find the section loops (each loop is a list of points):
loops = msh.Mesh.section(msh_plane)

# Show the loop polygon:
Part.show(Part.makePolygon(loops[0]))
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SectionByPlane/pl
