---
- GuiCommand   */pl
   Name   *TechDraw  ActiveView
   Name/pl   *Rysunek Techniczny  Aktywny widok
   MenuLocation   *Rysunek Techniczny → Wstaw aktywny widok (widok 3D)
   Workbenches   *[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version   *0.19
   SeeAlso   *[Obraz](TechDraw_Image/pl.md)
---

# TechDraw ActiveView/pl

## Opis

Narzędzie **Aktywny widok** wstawia obraz w postaci bitmapy aktywnego widoku okna 3D, na stronie rysunku.

![](images/TechDraw_ActiveView_example.png ) 
*Prosty widok modelu przestrzennego.*

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

-    **Przytnij**   * Przytnij wygenerowaną bitmapę.

-    **Szerokość**   * Szerokość *(w mm)* do przycięcia wygenerowanego widoku.

-    **Wysokość**   * Wysokość *(w mm)* do przycięcia wygenerowanego widoku.

-    **Bez tła**   * Jeżeli opcja ta jest zaznaczona, to wygenerowana bitmapa będzie miała przezroczyste tło.

-    **Jednolite tło**   * Jeżeli opcja ta jest zaznaczona, to tworzony obiekt będzie miał tło w wybranym kolorze.

-    **Użyj tła widoku 3D**   * Jeżeli opcja ta jest zaznaczona, to wygenerowana bitmapa będzie wykorzystywać tło z okna widoku 3D.

## Uwagi

-   Aktywny widok jest statyczny po wygenerowaniu, nigdy nie jest aktualizowany przy zmianach w modelu 3D.
-   Aktywny widok z założenia jest [obrazem](TechDraw_Image/pl.md). Dlatego jego **Typ skali** jest zawsze inicjalizowany jako {{Value|Użytkownika}}.
-   W {{VersionMinus/pl|0.20}} funkcjonalność tą realizowało narzędzie [Symbol](TechDraw_Symbol/pl.md).

## Właściwości

Zobacz również stronę [Obraz](TechDraw_Image/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md) środowiska Rysunek Techniczny.

## Tworzenie skryptów 

Zobacz również stronę   * [Dokumentacja API generowana automatycznie](https   *//freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Aktywny widok nie jest dostępne dla [makrodefinicji](macros/pl.md) i z konsoli [Python](Python/pl.md). Zamiast tego użyj funkcji [Zapisz zrzut ekranu](Std_ViewScreenShot/pl.md).





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/pl
