---
- GuiCommand:/pl
   Name:TechDraw MoveView
   Name/pl:Rysunek Techniczny: Przesuń widok
   MenuLocation:Rysunek Techniczny → Widoki → Przesuń widok
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.20
   SeeAlso:[Udostępnij widok](TechDraw_ShareView/pl.md)
---

# TechDraw MoveView/pl



## Opis

Narzędzie **Przesuń widok** przenosi widok i wszystkie jego elementy zależne *(dymki, wymiary itp.)* na inną stronę.



## Użycie

1.  Opcjonalnie wybierz widok, stronę początkową i stronę docelową. Strony muszą być wybrane w tej kolejności.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_MoveView.svg" width=16px> '''Przesuń widok'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_MoveView.svg" width=16px> Przesuń widok**.
3.  Otworzy się okno dialogowe umożliwiające wybór widoku, strony źródłowej i strony docelowej.
4.  Naciśnij przycisk **OK**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Przesuń widok** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
import TechDrawTools
TechDrawTools.MoveView(viewName, fromPageName, toPageName)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw MoveView/pl
