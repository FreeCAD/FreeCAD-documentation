---
 GuiCommand:
   Name: Arch Check
   Name/pl: Architektura: Sprawdź
   MenuLocation: Narzędzia , Sprawdź
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_CloseHoles/pl
---

# Arch Check/pl



## Opis

Narzędzie to sprawdza bieżący dokument lub wybrane obiekty pod kątem braku brył typu [Część](Part_Workbench/pl.md) lub [BIM](BIM_Workbench/pl.md), co może powodować problemy, ponieważ większość operacji środowiska pracy BIM wymaga obiektów bryłowych.



## Użycie

1.  Wybierz z manu opcję **<img src="images/Arch_Check.svg" width=16px> '''Sprawdź'''** lub **Narzędzia → <img src="images/Arch_Check.svg" width=16px> Sprawdź**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształt z siatki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
list_bad = check(objectslist, includehidden=False)
```

-   Sprawdza, czy podane obiekty w `objectslist` zawierają tylko bryły.
-   Jeśli `includehidden` ma wartość `True`, uwzględni wszystkie ukryte obiekty, w przeciwnym razie pominie je w wyszukiwaniu.
-   Zwraca `list_bad`, listę obiektów, które nie są pochodnymi `Part::Feature` lub komponentów, które nie są zamknięte, nieważne, nie zawierają brył lub zawierają ściany, które nie są częścią żadnej bryły. Służy do wykrywania polilinii i profili środowiska pracy [BIM](BIM_Workbench/pl.md) lub [Rysunek Roboczy](Draft_Workbench/pl.md), które nie są bryłami.
    -   Każdy element w `list_bad` jest kolejną listą `[object, message]`, gdzie `object` jest wykrytą nie-bryłą, a `message` wskazuje powód, dla którego został on włączony do tej listy.

Przykład:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```



---
⏵ [documentation index](../README.md) > Arch Check/pl
