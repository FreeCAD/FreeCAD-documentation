---
- GuiCommand:/de
   Name:Std SendeAnPythonKonsole
   MenuLocation:Bearbeiten → Sende an Python Konsole
   Workbenches:Alle
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

# Std SendToPythonConsole/de

## Beschreibung

Der **Std SendeAnPythonKonsole** Befehl erstellt eine Variable in der [Python Konsole](Python_console/de.md), die auf ein ausgewähltes Objekt verweist. Wenn eine Unterform des Objekts ausgewählt wird, werden zwei zusätzliche Variablen erstellt, von denen eine auf die Form des Objekts und die andere auf die Unterform selbst verweist. Die Variablen und der damit verbundene Code können zur Entwicklung von Python Code verwendet werden.

>>> ### Begin command Std_SendToPythonConsole
>>> obj = App.getDocument("Unnamed").getObject("Box")
>>> shp = App.getDocument("Unnamed").getObject("Box").Shape
>>> elt = App.getDocument("Unnamed").getObject("Box").Shape.Edge8
>>> ### End command Std_SendToPythonConsole



*Beispielausgabe: eine Kante eines [Part Quaders](Part_Box/de.md) wurde ausgewählt*

## Verwendung

1.  Wähle ein einzelnes Objekt aus.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Wähle die **Bearbeiten → <img src="images/Std_SendToPythonConsole.svg" width=16px> Sende an Python Konsole** Option aus dem Menü.
    -   Wähle die Option {{MenuCommand/de|<img src="images/Std_SendToPythonConsole.svg" width=16px> Sende an Python Konsole}} Option aus dem [Baumansicht](Tree_view/de.md) Kontextmenü oder [3D Ansicht](3D_view/de.md) Kontextmenü.
    -   Verwende die Tastaturkürzel: **Strg**+**Shift**+**P**.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std SendToPythonConsole/de
