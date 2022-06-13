---
- GuiCommand   */pl
   Name   *TechDraw  ActiveView
   Name/pl   *Rysunek Techniczny  Aktywny widok
   MenuLocation   *Rysunek Techniczny → Wstaw aktywny widok (widok 3D)
   Workbenches   *[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version   *0.19
   SeeAlso   *[Symbol](TechDraw_Symbol/pl.md)
---

# TechDraw ActiveView/pl

## Opis

Narzędzie **Aktywny widok** wstawia reprezentację okna 3D na stronie rysunku.

![](images/TechDraw_ActiveView_example.png ) 
*Prosty widok z modelu 3D, który nie wymaga żadnych złożonych obliczeń.*

## Użycie

1.  Przejdź do właściwego okna [Widoku 3D](3D_view/pl.md).
2.  Jeśli w dokumencie jest wiele stron z rysunkami   * opcjonalnie wybierz odpowiednią stronę w oknie [widoku drzewa](Tree_view/pl.md). Nie jest to opcjonalne dla {{VersionMinus/pl|0.19}}.
3.  Istnieje kilka sposobów na wywołanie narzędzia   *
    -   Naciśnij przycisk**<img src="images/TechDraw_ActiveView.svg" width=16px> [Wstaw aktywny widok (widok 3D)](TechDraw_ActiveView/pl.md)
**
    -   Wybierz opcję **Rysunek Techniczny → <img src="images/TechDraw_ActiveView.svg" width=16px> Wstaw widok aktywny (widok 3D)** z menu.
4.  Jeśli w dokumencie jest wiele stron z rysunkami i nie została jeszcze wybrana żadna strona, zostanie otwarte okno dialogowe **Wybór strony**   * {{Version/pl|0.20}}
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
5.  Zostanie otwarty panel zadań **Aktywny widok na stronę Rysunku Technicznego**. Aby uzyskać więcej informacji, zobacz [Opcje](#Opcje.md).
6.  Naciśnij przycisk **OK**.

## Opcje

Można określić następujące parametry   *

-    **Szerokość**   * Szerokość generowanego widoku.

-    **Wysokość**   * Wysokość generowanego widoku.

-    **Ramka**   * Ilość pustego miejsca, które ma pozostać wokół widoku *(ale w granicach Szerokość x Wysokość)*.

-    **Tło**   * Jeśli opcja ta jest zaznaczona, dodawane jest tło o określonym kolorze.

-    **Szerokość linii**   * Grubość linii w obrazie.

-    **Tryb renderowania**   * Dostępne są następujące tryby   *

    -   
        {{Value|Domyślny}}
        
           * Renderuj elementy pierwotne takimi, jakimi są.

    -   
        {{Value|Szkieletowy}}
        
           * Renderuj wielokąty jako szkielet.

    -   
        {{Value|Punkty}}
        
           * Renderuj tylko wierzchołki wielokątów i linii.

    -   
        {{Value|Nadpisanie widoku szkieletowego}}
        
           * Oprócz trybu {{Value|Domyślny}} renderuje nakładkę ze szkieletem.

    -   
        {{Value|Cieniowany z ukrytymi krawędziami}}
        
           * Podobnie jak {{Value|Szkieletowy}}, ale usuwa linie, które w przeciwnym razie nie byłyby wyświetlane ze względu na geometryczny ubytek.

    -   
        {{Value|Ramka otaczająca}}
        
           * Pokaż tylko ramkę brzegową każdego obiektu.

## Uwagi

-   Aktywny widok jest statyczny po wygenerowaniu, nigdy nie jest aktualizowany przy zmianach w modelu 3D.
-   Aktywny widok jest [Symbolem](TechDraw_Symbol/pl.md). Dlatego jego **Typ skali** jest zawsze inicjalizowany jako {{Value|Użytkownika}}.
-   To narzędzie jest wciąż w pewnym stopniu **eksperymentalne**.

## Właściwości

Zobacz również stronę [Symbol](TechDraw_Symbol/pl.md).

## Tworzenie skryptów 


**Zobacz również   ***

[TechDraw API](TechDraw_API.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Aktywny widok może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji   *


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/pl
