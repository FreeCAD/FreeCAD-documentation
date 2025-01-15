---
 GuiCommand:
   Name: Arch Floor
   Name/pl: Architektura: Kondygnacja
   MenuLocation: 3D / BIM , Budynek
   Workbenches: BIM_Workbench/pl
   Shortcut: **L** **V**
   SeeAlso: 
---

# Arch Floor/pl



## Opis

**Kondygnacje** są specjalnym typem obiektu grupy FreeCAD, który posiada kilka dodatkowych właściwości szczególnie przydatnych dla pięter budynków. W szczególności posiadają właściwość wysokości, którą mogą wykorzystać dziecięce obiekty ([ściany](Arch_Wall/pl.md) i [konstrukcje](Arch_Structure/pl.md)) do automatycznego ustawiania swojej wysokości. Są one głównie używane do organizacji modelu.

Od {{VersionPlus/pl|0.18}} obiekt **Kondygnacja** wywodzi się w całości z obiektu [Część budynku](Arch_BuildingPart/pl.md), który jest ogólnym kontenerem do organizowania modelu budynku, nie ograniczonym do pięter lub kondygnacji. Starsze obiekty Kondygnacja można przekonwertować na nowy typ, klikając je prawym przyciskiem myszy i wybierając {{Incode|Konwertuj na Część budynku}}.



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów, które mają być uwzględnione w nowym piętrze.
2.  Wywołaj polecenie Kondygnacja na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Arch_Floor.svg" width=16px> '''Kondygnacja'''** na pasku narzędziowym.
    -   Użyj klawiszy klawiatury **L**, a następnie **V**.
    -   Skorzystaj z pozycji **3D / BIM → Kondygnacja** z menu głównego.



## Opcje

-   Po utworzeniu podłogi można dodać do niej więcej obiektów, przeciągając je i upuszczając w widoku drzewa lub używając narzędzia **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.
-   Obiekty można usuwać z kondygnacji poprzez przeciąganie i upuszczanie ich w widoku drzewa lub za pomocą narzędzia **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.



## Właściwości

Obiekt Kondygnacja dzieli wszystkie właściwości z obiektem [Część budynku](Arch_BuildingPart/pl.md), przy czym **IFC Type** jest ustawione na `"Building Storey"`.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kondygnacja** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```

-   Tworzy obiekt `Floor` z `objectslist`, który jest listą obiektów.

Przykład:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > Arch Floor/pl
