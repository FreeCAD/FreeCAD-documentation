---
 GuiCommand:
   Name: Arch CutPlane
   Name/pl: Architektura: Przetnij płaszczyzną
   MenuLocation: Modyfikacja , Przetnij płaszczyzną
   Workbenches: BIM_Workbench/pl
---

# Arch CutPlane/pl



## Opis

Narzędzie **Przytnij płaszczyzną** tnie bryłę obiektu Architektury, taką jak [ścianę](Arch_Wall/pl.md) lub [konstrukcję](Arch_Structure/pl.md) za pomocą płaskiej płaszczyzny.

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:400px;"> 
*Po lewej: Przed zastosowaniem narzędzia Przetnij płaszczyzną. Środek: wynikowa ściana po zakończeniu cięcia. Po prawej: kolejny opcjonalny wynik.*



## Użycie

1.  Jeśli płaszczyzna cięcia ma być wyprowadzona z krawędzi prostej ({{Version/pl|1.0}}) opcjonalnie wyrównaj [płaszczyznę roboczą](Draft_SelectPlane/pl.md):
    -   Wybrana krawędź nie może być równoległa do normalnej płaszczyzny roboczej.
    -   Wygenerowana powierzchnia cięcia będzie prostopadła do płaszczyzny roboczej.
2.  Wybierz obiekt do wycięcia.
3.  Wykonaj jedną z następujących czynności:
    -   Wybierz obiekt z pojedynczą płaską powierzchnią. {{Version/pl|1.0}}
    -   Wybierz płaską powierzchnię w [widoku 3D](3D_view/pl.md).
    -   Wybierz obiekt z pojedynczą prostą krawędzią. {{Version/pl|1.0}}
    -   Wybierz prostą krawędź w [widoku 3D](3D_view/pl.md). {{Version/pl|1.0}}
4.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Arch_CutPlane.svg" width=16px> '''Przetnij płaszczyzną'''**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Arch_CutPlane.svg" width=16px> Przetnij płaszczyzną**.
5.  Wybierz **Za** lub **Przed**, aby wskazać, po której stronie powierzchni cięcia materiał ma zostać usunięty.
6.  Naciśnij przycisk **OK**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Przetnij płaszczyzną może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Tworzy obiekt `cutObj` z podanego `archObject`, który jest przecinany przez `cutPlane`, która jest powierzchnią innego obiektu.
    -   
        `archObject`
        
        powinien być `SelectionObject` uzyskanym z `FreeCADGui.Selection.SelectionEx()[0]`.

    -   
        `cutPlane`
        
        powinien być `FaceObject` uzyskanym z `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]`.

-    `sideFace`określa, po której stronie `FaceObject` zostanie utworzona objętość; objętość ta zostanie następnie użyta do odjęcia od `archObject`. Jeśli `sideFace` to `0`, zostanie utworzona objętość z tyłu obiektu, w przeciwnym razie zostanie ona utworzona z przodu obiektu.

Przykład:


```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch CutPlane/pl
