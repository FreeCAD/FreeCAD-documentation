---
 GuiCommand:
   Name: Std Delete
   Name/pl: Std: Usuń
   MenuLocation: Edycja , Usuń
   Workbenches: wszystkie
   Shortcut: **Del**
---

# Std Delete/pl



## Opis

Polecenie **Usuń** usuwa wybrane obiekty.



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz opcję z menu **Edycja → <img src="images/Std_Delete.svg" width=16px> Usuń**.
    -   Wybierz opcję **<img src="images/Std_Delete.svg" width=16px> Usuń** z menu kontekstowego [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **Del**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby usunąć obiekt, należy użyć metody `removeObject` obiektu *document*.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Delete/pl
