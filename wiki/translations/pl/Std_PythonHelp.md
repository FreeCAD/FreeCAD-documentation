---
- GuiCommand:
   Name: Std PythonHelp
   Name/pl: Std: Pomoc dla środowiska Python
   MenuLocation: Pomoc - Dokumentacja automatyczna modułów Python
   Workbenches: wszystkie
   SeeAlso: [Dokumentacja skryptów środowiska Python](Std_FreeCADPowerUserHub/pl.md)
---

# Std PythonHelp/pl



## Opis

Polecenie **Dokumentacja skryptów środowiska Python** uruchamia serwer WWW, który komunikuje się z domyślną przeglądarką internetową systemu przez *local socket*. Serwer WWW wyświetla informacje o dostępnych modułach środowiska [Python](Python/pl.md), klasach i funkcjach programu FreeCAD. Żądane strony są generowane automatycznie.

Serwer internetowy jest oparty na module Python [pydoc](https://docs.python.org/3.8/library/pydoc.html#module-pydoc), dzięki czemu wydobywa \"docstringi\" plików Pythona (`.py`) oraz dokumentację tekstową zdefiniowaną w \"wrapperach\" Pythona (`.xml`), które odsłaniają leżący u ich podstaw kod C++.



## Użycie

1.  Wybierz z menu opcję **Pomoc → <img src="images/Std_PythonHelp.svg" width=16px> Dokumentacja automatycznych modułów Python**.
2.  Kliknij dowolny z linków, aby przejść do dokumentacji konkretnej klasy lub funkcji.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std PythonHelp/pl
