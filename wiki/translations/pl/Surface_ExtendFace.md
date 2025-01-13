---
 GuiCommand:
   Name: Surface ExtendFace
   Name/pl: Powierzchnia 3D: Rozszerz powierzchnię
   MenuLocation: Surface , Extend face
   Workbenches: Surface_Workbench/pl
   Version: 0.17
---

# Surface ExtendFace/pl



## Opis

Polecenie **[<img src=images/Surface_ExtendFace.svg style="width:16px"> '''Rozszerz powierzchnię'''** ekstrapoluje istniejącą ścianę lub powierzchnię na jej granicach za pomocą lokalnych parametrów U i V.

<img alt="" src=images/Surface_ExtendFace_base_example.png  style="width:300px;"> <img alt="" src=images/Surface_ExtendFace_example.png  style="width:300px;">



*Po lewej: oryginalna powierzchnia. Po prawej: powierzchnia powiększona.*



## Użycie

1.  Upewnij się, że masz obiekt, który ma powierzchnie. Obiekt może być utworzony w środowisku pracy <img alt="" src=images/Workbench_Surface.svg  style="width:24px;">. [Powierzchnia 3D](Surface_Workbench/pl.md), ale może to być również dowolny inny obiekt, na przykład utworzony za pomocą środowisk <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) lub <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">. [Projekt Części](PartDesign_Workbench/pl.md).
2.  Wybierz ścianę do rozszerzenia, klikając ją w oknie [widoku 3D](3D_view/pl.md).
3.  Naciśnij przycisk **[<img src=images/Surface_ExtendFace.svg style="width:16px">. '''Rozszerz powierzchnię'''**.



## Opcje

To polecenie nie ma żadnych opcji. Może działać z zaznaczeniem wstępnym lub jego brakiem.



## Właściwości

Obiekt **Rozszerz powierzchnię** *(klasa `Surface::Extend`)* jest pochodną podstawowej klasy [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`, poprzez klasę podrzędną `Part::Spline`)*, dlatego też dzieli z nią wszystkie jej właściwości.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), obiekt Rozszerz powierzchnię, posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Ściana|LinkSub**: element podrzędny obiektu, który zostanie rozszerzony. Musi to być powierzchnia.

-    **Tolerancja|FloatConstraint**: wartość domyślna to {{Value|0.1}}.

-    **Extend UNeg|FloatConstraint**: Wartość domyślna to {{Value|0.05}}. Stosunek lokalnego parametru U, który zostanie rozszerzony w kierunku ujemnym.

-    **Extend UPos|FloatConstraint**: Wartość domyślna to {{Value|0.05}}. Stosunek lokalnego parametru U, który zostanie rozszerzony w kierunku dodatnim.

-    **Extend USymetric|Bool**: Wartość domyślna to {{TRUE/pl}}, w którym to przypadku **Extend UNeg** i **Extend UPos** będą miały tę samą wartość.

-    **Extend VNeg|FloatConstraint**: Wartość domyślna to {{Value|0.05}}. Stosunek lokalnego V, który zostanie rozszerzony w kierunku ujemnym.

-    **Extend VPos|FloatConstraint**: Wartość domyślna to {{Value|0.05}}. Stosunek lokalnego kierunku V, który zostanie rozszerzony w kierunku dodatnim.

-    **Extend VSymetric|Bool**: Wartość domyślna to {{TRUE/pl}}, w którym to przypadku **Extend VNeg** i **Extend VPos** będą miały tę samą wartość.

-    **SampleU|IntegerConstraint**: Wartość domyślna to {{Value|32}}.

-    **SampleV|IntegerConstraint**: Wartość domyślna to {{Value|32}}.



### Widok


{{TitleProperty|Podstawa}}

-    **Punkty kontrolne|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Surface Extend może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) poprzez dodanie obiektu `Surface::Extend`.

-   Powierzchnia do rozszerzenia musi być przypisana jako struktura danych [LinkSub](FeaturePython_Custom_Properties/pl#App:_PropertyLinkSub.md) do właściwości `Face` obiektu. Musi ona zawierać tylko jedną powierzchnię.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points = [a, App.Vector(-20, -8, 0), b, c,
          App.Vector(37, 4, 0), d,
          App.Vector(-2, -18, 0), a]
obj = Draft.make_bspline(points)
doc.recompute()

if App.GuiUp:
    obj.ViewObject.Visibility = False

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj, "Edge1")]
doc.recompute()

# 
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# 
surf_extended = doc.addObject("Surface::Extend", "Surface")
surf_extended.Face = [surf, "Face1"]
doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface ExtendFace/pl
