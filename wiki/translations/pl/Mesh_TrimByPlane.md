---
- GuiCommand:/pl
   Name:Mesh TrimByPlane
   Name/pl:Siatka Przytnij siatkę płaszczyzną
   MenuLocation:Siatki → Cięcie → Przytnij siatkę
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Przetnij siatkę](Mesh_PolyCut/pl.md), [Przytnij siatkę](Mesh_PolyTrim/pl.md)
---

# Mesh TrimByPlane/pl



## Opis

Polecenie **Przytnij siatkę płaszczyzną** wycina z obiektu siatkowego ściany i części ścian po jednej stronie płaszczyzny.



## Użycie

1.  Wybierz pojedynczy obiekt siatki i pojedynczą [Płaszczyznę części](Part_Plane/pl.md). Płaszczyzna *(jej przedłużenie)* powinna przecinać obiekt siatki.

2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Mesh_TrimByPlane.svg" width=16px> '''Przytnij siatkę płaszczyzną'''**.
    -   Wybierz z menu polecenie **Siatki → Cięcie → <img src="images/Mesh_TrimByPlane.svg" width=16px> Przytnij siatkę płaszczyzną**.

3.  Otwiera się okno dialogowe **Przytnij płaszczyzną**.

4.  
    **Wybierz stronę, którą chcesz pozostawić**, naciskając jeden z przycisków:

    -   
        {{button|Poniżej}}
        

    -   
        {{button|Powyżej}}
        

    -   
        {{button|Rozdziel}}
        
        : usuwa ściany i części ścian nad płaszczyzną i tworzy zawierający je nowy obiekt siatki.



## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby przyciąć siatkę za pomocą płaszczyzny użyj jej metody `trimByPlane`.


```python
import FreeCAD as App
import Mesh

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(30, 40, 50)
msh.ViewObject.DisplayMode = "Flat Lines"

# Define a plane by a base point and a normal vector:
pnt = App.Vector(25, 0, 0)
nor = App.Vector(0, 0, 1)

# We need to work on a copy of the msh.Mesh object:
new_msh = msh.Mesh.copy()

# Trim that copy:
new_msh.trimByPlane(pnt, nor)

# Update msh.Mesh:
msh.Mesh = new_msh
```





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/pl
