---
 GuiCommand:
   Name: FEM FemMesh2Mesh
   Name/pl: Siatka MES do siatki
   MenuLocation: Siatka , Siatka MES do siatki
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM FemMesh2Mesh/pl



## Opis

To narzędzie przekształca powierzchnie elementów 3D lub całe elementy 2D wybranej siatki MES na [obiekt środowiska Siatka](Mesh_MeshObject/pl.md). Wewnętrznie, wybiera ono ścianki elementów siatki MES, które są unikatowe *(nie są dzielone przez dwa elementy)* i używa ich do stworzenia ścianek siatki powierzchniowej. Opcjonalnie, może być użyte do zapisania zdeformowanej siatki. Robi się to poprzez dodanie przemieszczenia z wyników analizy MES do węzłów siatki *(skala przemieszczenia może być ustawiona przy pomocy skryptu w Python)*.


{{Version/pl|1.0}}

: To narzędzie tworzy też obiekt *Mesh2Fem*, który jest trójkątną siatką MES wygenerowaną z siatki powierzchniowej.



## Użycie

1.  Zaznacz obiekt siatki MES.
2.  Opcjonalnie, zaznacz też wyniki analizy MES.
3.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [Siatka MES do siatki](FEM_FemMesh2Mesh/pl.md)**.
    -   Wybierz opcję **Siatka → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> Siatka MES do siatki** z menu.



## Tworzenie skryptów 

**Uwaga**: Parametr *scale* - {{Version/pl|0.21}}. W przypadku starszych wersji programu należy go pominąć.

Przykład belki wspornikowej, w programie FreeCAD w wersji 1.0:


```python
from os.path import join
import FreeCAD as App
import Mesh
from femmesh import femmesh2mesh

path = join(App.getResourceDir(), "examples", "FEMExample.FCStd")
doc = App.openDocument(path)
fem_mesh = doc.FEMMeshGmsh.FemMesh
result = doc.CCX_Results
scale = 10  # displacement scale factor
out_mesh = femmesh2mesh.femmesh_2_mesh(fem_mesh, result, scale)
Mesh.show(Mesh.Mesh(out_mesh))
```





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM FemMesh2Mesh/pl
