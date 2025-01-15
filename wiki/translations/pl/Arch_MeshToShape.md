---
 GuiCommand:
   Name: Arch MeshToShape
   Name/pl: Architektura: Kształt z siatki
   MenuLocation: Narzędzia , Kształt z siatki
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_SplitMesh/pl,  Arch_RemoveShape/pl
---

# Arch MeshToShape/pl



## Opis

Narzędzie **Kształt z siatki** konwertuje wybrany obiekt [siatki](Mesh/pl.md) *([cechy siatki](Mesh_Feature/pl.md))* na obiekt [kształtu](Shape/pl.md) *([cechę Części](Part_Feature/pl.md))*.

Narzędzie to jest zoptymalizowane dla obiektów o płaskich powierzchniach *(bez krzywych)*. Odpowiednie narzędzie **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Utwórz kształt z siatki](Part_ShapeFromMesh/pl.md)** ze środowiska <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md) może być bardziej odpowiednie dla obiektów zawierających zakrzywione powierzchnie.



## Użycie

1.  Wybierz obiekt siatki.
2.  Naciśnij przycisk w menu **Narzędzia → <img src="images/Arch_MeshToShape.svg" width=16px> Kształt z siatki**.



## Właściwości



## Ograniczenia



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

Powyższy fragment kodu konwertuje podaną `obj` (siatkę) w kształt łączący współpłaszczyznowe elementy.

-   Jeśli właściwość `mark` ma wartość `True`, obiekty nie będące bryłami zostaną wyróżnione kolorem czerwonym.

-   Jeśli ma wartość`fast` ma wartość `True`, używa szybszego algorytmu, budując powłokę z elementów, a następnie usuwając rozdzielacz.

-    `tol`jest tolerancją używaną podczas konwersji segmentów siatki na druty.

-   Jeśli ma wartość`flat` ma wartość `True`, wymusi to, że polilinie będą idealnie płaskie, aby upewnić się, że można je przekonwertować na ściany, ale może to pozostawić luki w końcowej powłoce.

-   Jeśli ma wartość`cut` ma wartość `True`, otwory w ścianach są tworzone przez odejmowanie.

Przykład:


```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh::Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch MeshToShape/pl
