---
 GuiCommand:
   Name: Std ToggleSelectability
   Name/pl: Std: Przełącz możliwość zaznaczenia
   MenuLocation: Widok , Widoczność , Przełącz możliwość zaznaczenia
   Workbenches: wszystkie
---

# Std ToggleSelectability/pl



## Opis

Polecenie **Przełącz możliwość zaznaczenia** przełącza możliwość wyboru obiektów w oknie [widoku 3D](3D_view/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz z opcję menu **Widok → Widoczność → <img src="images/Std_ToggleSelectability.svg" width=16px> Przełącz możliwość zaznaczenia**.
    -   Wybierz opcję **<img src="images/Std_ToggleSelectability.svg" width=16px> Przełącz możliwość zaznaczenia** z menu kontekstowego [widoku drzewa](Tree_view/pl.md) lub widoku 3D.



## Uwagi

-   Wybieralność obiektu można również zmienić poprzez jego powiązaną właściwość **Selectable** w [Edytorze właściwości](Property_editor/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Właściwość `Selectable` obiektu określa jego możliwość zaznaczenia.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

obj.Selectable = not obj.Selectable
```



---
⏵ [documentation index](../README.md) > Std ToggleSelectability/pl
