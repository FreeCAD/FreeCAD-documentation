---
- GuiCommand:
   Name:Std BoxSelection
   Name/pl:Std: Zaznacz obszar
   MenuLocation:Edycja → Zaznacz obszar
   Workbenches:wszystkie
   Shortcut:**Shift** + **B**
   SeeAlso:[Wybór elementów ramką zaznaczenia](Std_BoxElementSelection/pl.md), [Zaznacz wszystko](Std_SelectAll/pl.md)
---

# Std BoxSelection/pl

## Opis

Polecenie **Zaznacz obszar** wybiera obiekty z prostokątnego obszaru zdefiniowanego przez użytkownika za pomocą ramki zaznaczenia, w oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_BoxSelection.svg" width=16px> Zaznacz obszar**.
    -   Użyj skrótu klawiaturowego: **Shift** + **B**.
2.  Wykonaj jedną z poniższych czynności:
    -   Przeciągnij ramkę zaznaczenia od lewej do prawej, aby zaznaczyć obiekty, których środek geometryczny leży wewnątrz tego pola.
    -   Przeciągnij ramkę zaznaczenia od prawej do lewej, aby zaznaczyć obiekty, których ramka otaczająca znajduje się *(częściowo)* wewnątrz tego pola lub go dotyka.

## Uwagi

-   Użyj polecenia [Wybór elementów ramką zaznaczenia](Std_BoxElementSelection/pl.md), aby wybrać powierzchnie zamiast obiektów.
-   Tego polecenia nie można użyć do wybrania elementów w [szkicu](Sketch/pl.md). Aby \"zaznaczyć ramką\", gdy otwarte jest okno dialogowe [Szkicownika](Sketcher_Dialog/pl.md):
    1.  Upewnij się, że żadne polecenie nie jest aktywne.
    2.  Wykonaj jedną z następujących czynności:
        -   Kliknij w pustym obszarze i przeciągnij prostokąt od lewej do prawej, aby zaznaczyć obiekty, które znajdują się całkowicie wewnątrz prostokąta.
        -   Kliknij w pustym obszarze i przeciągnij prostokąt od prawej do lewej, aby zaznaczyć także obiekty, które dotykają lub przecinają prostokąt.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std BoxSelection/pl
