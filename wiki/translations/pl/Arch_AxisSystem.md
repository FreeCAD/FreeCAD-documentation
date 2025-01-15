---
 GuiCommand:
   Name: Arch AxisSystem
   Name/pl: Architektura: Układ osi
   MenuLocation: Opisy , Układ osi
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_Axis/pl, Arch_Grid/pl
---

# Arch AxisSystem/pl



## Opis

Narzędzie Układ osi pozwala na połączenie dwóch lub trzech obiektów [Osiami](Arch_Axis/pl.md) środowiska pracy Architektura.

Jest to przydatne do definiowania punktów przecięcia między różnymi osiami. Obiekty Architektury mogą następnie użyć tego systemu do powielenia swojego kształtu na różnych punktach przecięcia.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;"> 
*Trzy obiekty [osi](Arch_Axis/pl.md) połączone w jeden [układ osi](Arch_AxisSystem/pl.md). Obiekt [konstrukcji](Arch_Structure/pl.md) używa tego systemu jako swojej właściwości **Axis*, aby jego kształt był powielany w każdym punkcie przecięcia.**



## Użycie

1.  Opcjonalnie wybierz obiekty [osi](Arch_Axis/pl.md), które chcesz włączyć do tego systemu.
2.  Naciśnij przycisk **<img src="images/Arch_AxisSystem.svg" width=16px> '''Układ osi'''**.
3.  Kliknij prawym przyciskiem myszy nowo utworzony obiekt systemu osi w widoku drzewa, aby dodać / edytować obiekty [osi](Arch_Axis/pl.md) zawarte w tym systemie.
4.  Wybierz dowolną istniejącą [oś](Arch_Axis/pl.md) i naciśnij **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)** lub **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**, aby dodać lub usunąć ją do / z tego systemu.
5.  Ustaw właściwość **Axis** dowolnego obiektu Architektury na ten system, aby jego kształt został zduplikowany w punktach przecięcia tego systemu.



## Opcje

-   Ten sam obiekt [osi](Arch_Axis/pl.md) może być częścią więcej niż jednego systemu.
-   Dowolny obiekt oparty na kształcie może być również użyty jako właściwość **Axis** obiektów Architektury. W takim przypadku kształt obiektu zostanie zduplikowany wzdłuż wierzchołków obiektu Oś.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Układ osi** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Tworzy obiekt {{Incode|AxisSystem}} z podanego {{Incode|axes}}, który jest pojedynczą [osią](Arch_Axis/pl.md) lub ich listą.

Przykład: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch AxisSystem/pl
