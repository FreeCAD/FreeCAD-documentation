---
 GuiCommand:
   Name: Arch Building
   Name/pl: Architektura: Budynek
   MenuLocation: 3d / BIM , Budynek
   Workbenches: BIM_Workbench/pl
   Shortcut: **B** **U**
   SeeAlso: 
---

# Arch Building/pl



## Opis

**Budynek** środowiska Architektura jest specjalnym typem obiektu grupy FreeCAD, szczególnie odpowiednim do reprezentowania całej jednostki budynku. Są one najczęściej używane do organizowania modelu, zawierając obiekty [kondygnacji](Arch_Floor/pl.md).



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów, które mają być zawarte w nowym budynku.
2.  Naciśnij przycisk **<img src="images/Arch_Building.svg" width=16px> '''Budynek'''** lub naciśnij klawisze **B**, a następnie **U**.



## Opcje

-   Począwszy od wersji FreeCAD 0.18, obiekt Budynku jest w rzeczywistości obiektem [Część budynku](Arch_BuildingPart/pl.md) z jego właściwością **Typ IFC** ustawioną na \"Building\". Możesz przekonwertować dowolną Część budynku na budynek, po prostu zmieniając jej typ IFC.
-   Po utworzeniu budynku można dodać do niego więcej obiektów, przeciągając je i upuszczając w widoku drzewa lub używając przycisku **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.
-   Możesz usunąć obiekty z budynku przeciągając i upuszczając je w widoku drzewa lub używając narzędzia **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.



## Właściwości

-    **Typ Budynku**: Typ tego budynku, do wyboru z listy.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Budynek** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji: 
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Tworzy obiekt `Building` z `objectslist`, który jest listą obiektów, lub `baseobj`, który jest obiektem `Shape`.

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

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Building/pl
