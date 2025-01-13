---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/pl: Arkusz Kalkulacyjny: Definiuj alias
   MenuLocation: -
   Workbenches: Spreadsheet_Workbench/pl
   Shortcut: **Ctrl** + **Shift** + **A**
   Version: 0.17
---

# Spreadsheet SetAlias/pl



## Opis

Narzędzie <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> **Definiuj alias** otwiera okno dialogowe, w którym można ustawić alias dla komórki. Zamiast używać przypisanej nazwy komórki, takiej jak A2, B3 lub C4, można użyć nazwy niestandardowej.



## Użycie

1.  Upewnij się, że jest aktywny [arkusz kalkulacyjny](Spreadsheet_CreateSheet/pl.md).
2.  Wybierz komórkę.
3.  Istnieje kilka sposobów wywołania tego narzędzia:
    -   Naciśnij przycisk **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Definiuj alias](Spreadsheet_SetAlias/pl.md)**.
    -   Użyj skrótu klawiaturowego: **Ctrl**+**Shift**+**A**.
4.  Wprowadź alias:
    -   Dozwolone są tylko znaki alfanumeryczne i znak podkreślenia (od `A` do `Z`, od `a` do `z`, od `0` do `9` oraz `_`).
    -   Pierwszy znak musi być literą.
    -   Nie wolno używać 1 lub 2 wielkich liter, po których następuje od 1 do 5 cyfr, na przykład `AB123`, ponieważ jest to zarezerwowane dla adresu komórki.
    -   Sekwencje znaków, które są jednostkami, nie są dozwolone. Na przykład `W` jest nieprawidłowym aliasem, ponieważ jest to jednostka dla [Wata](https://en.wikipedia.org/wiki/Watt). Ponieważ FreeCAD obsługuje wiele jednostek, najlepiej jest unikać krótkich aliasów. Zobacz stronę [Wyrażenia](Expressions/pl#Jednostki.md).
    -   Używanie stałych matematycznych `pi` i `e` jako aliasów prowadzi do błędów i należy ich unikać.
    -   Nie używaj spacji w aliasach, ponieważ będą one również prowadzić do błędów.





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/pl
