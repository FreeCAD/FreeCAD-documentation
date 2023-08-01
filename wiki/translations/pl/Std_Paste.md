---
- GuiCommand:
   Name: Std Paste
   Name/pl: Std: Wklej
   MenuLocation: Edycja - Wklej
   Workbenches: wszystkie
   Shortcut: **Ctrl** + **V**
   SeeAlso: [Wytnij](Std_Cut/pl.md), [Kopiuj](Std_Copy/pl.md), [Powiel zaznaczone](Std_DuplicateSelection/pl.md)
---

# Std Paste/pl



## Opis

Polecenie **Wklej** powoduje wklejenie obiektów ze Schowka do aktywnego dokumentu.



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Paste.svg" width=16px> '''Wklej'''**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Paste.svg" width=16px> Wklej**.
    -   Wybierz opcję **<img src="images/Std_Paste.svg" width=16px> Wklej** z menu kontekstowego [Widoku drzewa](Tree_view/pl.md). Zauważ, że ta opcja jest dostępna tylko wtedy, gdy zaznaczony jest istniejący obiekt.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **V**.



## Uwagi

-   FreeCAD automatycznie zmieni wewnętrzne nazwy oraz, w zależności od preferencji, etykiety obiektów, aby uniknąć konfliktów nazw.
-   Alias komórki arkusza kalkulacyjnego, który już istnieje w arkuszu kalkulacyjnym, nie zostanie wklejony.
-   Podczas pracy w oknie tekstowym programu FreeCAD, w polu wprowadzania danych lub arkuszu kalkulacyjnym standardowy skrót klawiaturowy **Ctrl** + **V** w prawie wszystkich przypadkach nie wywołuje polecenia **Std Wklej**, ale zamiast tego używa funkcji Wklej z systemu operacyjnego.
-   Nie jest możliwe kopiowanie i wklejanie natywnych obiektów między programem FreeCAD a innymi aplikacjami.



## Ustawienia

-   Duplikaty etykiet są dozwolone, gdy opcja **Przybory→ Edycja parametrów ... → BaseApp → Preferencje → Dokument → DuplicateLabels** jest ustawione na wartość {{TRUE/pl}}. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Paste/pl
