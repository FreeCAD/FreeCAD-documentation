---
 GuiCommand:
   Name: Std Paste
   Name/pl: Std: Wklej
   MenuLocation: Edycja , Wklej
   Workbenches: wszystkie
   Shortcut: **Ctrl** + **V**
   SeeAlso: Std_Cut/pl, Std_Copy/pl, Std_DuplicateSelection/pl
---

# Std Paste/pl



## Opis

Polecenie **Wklej** powoduje wklejenie obiektów ze Schowka do aktywnego dokumentu.



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Paste.svg" width=16px> [Wklej](Std_Paste/pl.md)**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Paste.svg" width=16px> Wklej**.
    -   Wybierz opcję **<img src="images/Std_Paste.svg" width=16px> Wklej** z menu kontekstowego [Widoku drzewa](Tree_view/pl.md). Zauważ, że ta opcja jest dostępna tylko wtedy, gdy zaznaczony jest istniejący obiekt.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **V**.



## Uwagi

-   FreeCAD automatycznie zmieni wewnętrzne nazwy oraz, w zależności od preferencji, etykiety obiektów, aby uniknąć konfliktów nazw.
-   Alias komórki arkusza kalkulacyjnego, który już istnieje w arkuszu kalkulacyjnym, nie zostanie wklejony.
-   Podczas pracy w oknie tekstowym programu FreeCAD, w polu wprowadzania danych lub arkuszu kalkulacyjnym standardowy skrót klawiaturowy **Ctrl** + **V** w prawie wszystkich przypadkach nie wywołuje polecenia **Std Wklej**, ale zamiast tego używa funkcji Wklej z systemu operacyjnego.
-   Nie jest możliwe kopiowanie i wklejanie natywnych obiektów między programem FreeCAD a innymi aplikacjami.



## Ustawienia

Zobacz też: [Edytor preferencji](Preferences_Editor/pl.md).

-   Aby pozwolić na zduplikowane etykiety, zaznacz opcję **Edycja → Preferencje... → Ogólne → Dokument → Pozwalaj na zduplikowane etykiety obiektów w jednym dokumencie**. Nie jest to jednak zalecane.



---
⏵ [documentation index](../README.md) > Std Paste/pl
