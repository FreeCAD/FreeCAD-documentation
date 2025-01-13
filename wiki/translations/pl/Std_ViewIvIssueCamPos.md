---
 GuiCommand:
   Name: Std ViewIvIssueCamPos
   Name/pl: Std: Parametry ujęcia widoku
   MenuLocation: Widok , Widok trójwymiarowy , Parametry ujęcia widoku
   Workbenches: wszystkie
   SeeAlso: Std_FreezeViews/pl
---

# Std ViewIvIssueCamPos/pl



## Opis

Polecenie **Std ViewIvIssueCamPos** wyświetla ustawienia ujęcia aktywnego [widoku 3D](3D_view/pl.md) w oknie [Widoku raportu](Report_view/pl.md) i [konsoli Python](Python_console/pl.md).


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```



*Przykładowe wyświetlone dane: ustawienia ujęcia widoku po zmianie widoku na [izometryczny](Std_ViewIsometric/pl.md) w nowym dokumencie*



## Użycie

1.  Wybierz z menu opcję **Widok → Widok trójwymiarowy → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Parametry ujęcia widoku**.



## Uwagi

-   Ustawienia kamery można wykorzystać do dodania zamrożenia widoków do pliku ***.cam**. Zobacz stronę [Zamroź widok](Std_FreezeViews/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Metoda `getCamera` obiektu View zwraca te same parametry ustawienia ujęcia widoku w postaci pojedynczego ciągu znaków.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.getCamera()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvIssueCamPos/pl
