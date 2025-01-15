---
 GuiCommand:
   Name: Std ViewRotateLeft
   Name/pl: Std: Odwróć widok w lewo
   MenuLocation: Widok , Widoki standardowe , Odwróć w lewo
   Workbenches: wszystkie
   Shortcut: **Shift**+**Lewo**
   SeeAlso: Std_ViewRotateRight/pl
---

# Std ViewRotateLeft/pl



## Opis

Polecenie **Odwróć widok w lewo** obraca widok w aktywnym oknie [widoku 3D](3D_view/pl.md) wokół osi normalnej *(prostopadłej do widoku)*, w 90-stopniowych przyrostach w lewo *(przeciwnie do ruchu wskazówek zegara)*.



## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz opcję **Widok → Widoki standardowe → <img src="images/Std_ViewRotateLeft.svg" width=16px> Odwróć w lewo** z menu.
    -   Wybierz opcję **Widoki standardowe → <img src="images/Std_ViewRotateLeft.svg" width=16px> Odwróć w lewo** z menu podręcznego w oknie [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **Shift** + **Lewo**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby obrócić widok w lewo, użyj metody `viewRotateLeft` obiektu *ActiveView*. Dostępna jest też metoda `viewRotateRight`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewRotateLeft()
```



---
⏵ [documentation index](../README.md) > Std ViewRotateLeft/pl
