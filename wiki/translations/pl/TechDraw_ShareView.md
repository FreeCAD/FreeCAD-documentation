---
- GuiCommand:
   Name:TechDraw ShareView
   Name/pl:Rysunek Techniczny: Udostępnij widok
   MenuLocation:Rysunek Techniczny → Widoki → Udostępnij widok
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.20
   SeeAlso:[Przesuń widok](TechDraw_MoveView/pl.md)
---

# TechDraw ShareView/pl



## Opis

Narzędzie **Udostępnij widok** udostępnia widok i wszystkie jego elementy zależne *(dymki, wymiary itp.)* na inną stronę.



## Użycie

1.  Opcjonalnie wybierz widok, stronę początkową i stronę docelową. Strony muszą być wybrane w tej kolejności.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ShareView.svg" width=16px> '''Udostępnij widok'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ShareView.svg" width=16px> Udostępnij widok**.
3.  Otworzy się okno dialogowe umożliwiające wybór widoku, strony źródłowej i strony docelowej.
4.  Naciśnij przycisk **OK**.



## Uwagi

Po operacji udostępniania istnieje tylko jeden obiekt widoku. Wszelkie zmiany wprowadzone w widoku zostaną odzwierciedlone na obu stronach. Jeśli widok zostanie usunięty z jednej strony, zostanie również usunięty z drugiej strony.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Udostępnij widok** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShareView/pl
