---
- GuiCommand   */pl
   Name   *Std AxisCross
   Name/pl   *Std   * Symbol osi
   MenuLocation   *Widok → Przełącz krzyż osi
   Workbenches   *wszystkie
   Shortcut   ***A** **C**
---

# Std AxisCross/pl

## Opis

Polecenie **Symbol osi** włącza / wyłącza krzyż osi w aktywnym oknie [Widoku 3D](3D_view/pl.md).

Krzyż osi składa się z trzech strzałek reprezentujących osie X, Y i Z globalnego układu współrzędnych w kierunku dodatnim. Ich wspólnym punktem początkowym jest początek globalnego układu współrzędnych.

![](images/Std_AxisCross_example.svg ) 
*Krzyż osi ''(litery nie są częścią krzyża osi)''.*

## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia   *
    -   Wybierz z menu opcję **Widok → <img src="images/Std_AxisCross.svg" width=16px> Przełącz krzyż osi**.
    -   Użyj skrótu klawiaturowego   * **V** kolejnie **P**.

## Uwagi

-   FreeCAD może wyświetlać mniejszy symbol układu współrzędnych w prawym dolnym rogu okna widoków 3D   * **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Pokaż w narożniku symbol układu współrzędnych**. Patrz [Edytor preferencji](Preferences_Editor/pl#Widok_3D.md)
-   [Kostka do nawigacji 3D](Navigation_Cube/pl.md) zawiera również wskaźnik układu współrzędnych.

## Ustawienia

Domyślne ustawienie krzyża osi można zmienić w preferencjach   * **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Pokaż w narożniku symbol układu współrzędnych**. Przeczytaj również informacje o [Edytorze preferencji](Preferences_Editor/pl#Widok_3D.md). {{Version/pl|0.19}}

## Tworzenie skryptów 


**Zobacz również   ***

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby przełączyć widoczność **symbolu osi**, należy użyć metody `setAxisCross` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AxisCross/pl
