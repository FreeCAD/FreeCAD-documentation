---
- GuiCommand:
   Name: Spreadsheet SetAlias
   Name/pl: Arkusz Kalkulacyjny: Definiuj alias
   MenuLocation: -
   Workbenches: [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md)
   Version: 0.17
---

# Spreadsheet SetAlias/pl



## Opis

Narzędzie **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Definiuj alias](Spreadsheet_SetAlias/pl.md)** otwiera okno dialogowe, w którym można ustawić alias dla komórki. Zamiast używać przypisanej nazwy komórki, takiej jak A2, B3 lub C4, można użyć nazwy niestandardowej.



## Użycie

Upewnij się, że jest aktywny jest otwarty **[<img src=images/Spreadsheet_CreateSheet.svg style="width:16px"> [arkusz kalkulacyjny](Spreadsheet_CreateSheet/pl.md)**, aby przycisk był dostępny.

1.  Wybierz komórkę.
2.  Naciśnij przycisk **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Definiuj alias](Spreadsheet_SetAlias/pl.md)**.
3.  Wprowadź nazwę:
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
