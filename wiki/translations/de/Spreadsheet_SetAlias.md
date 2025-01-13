---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/de: Spreadsheet AliasFestlegen
   MenuLocation: -
   Workbenches: Spreadsheet_Workbench/de
   Shortcut: **Ctrl**+**Shift**+**A**
   Version: 0.17
---

# Spreadsheet SetAlias/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> **Spreadsheet AliasFestlegen** öffnet ein Dialogfenster zum Festlegen eines Alias für eine Zelle. So kann anstelle des exakten Zellnamens wie A2, B3 oder C4 ein benutzerdefinierter Name verwendet werden.



## Anwendung

1.  Sicherstellen, dass eine [Kalkulationstabelle](Spreadsheet_CreateSheet/de.md) aktiviert ist.
2.  Eine Zelle auswählen.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Alias-Namen festlegen](Spreadsheet_SetAlias/de.md)** drücken.
    -   Das Tastaturkürzel **Ctrl** + **Shift** + **A**.
4.  Einen Alias eingeben:
    -   Nur alphanumerische Zeichen und Unterstriche (`A` bis `Z`, `a` bis `z`, `0` bis `9` und `_`) sind erlaubt.
    -   Das erste Zeichen muss ein Buchstabe sein.
    -   Die Verwendung von 1 oder 2 Großbuchstaben gefolgt von 1 bis 5 Ziffern, z.B. `AB123`, ist nicht erlaubt, da dies als eine Zelladresse angesehen wird.
    -   Zeichenfolgen die Maßeinheiten entsprechen sind nicht erlaubt. Zum Beispiel ist `W` ein ungültiger Alias da er der Einheit [Watt](https://de.wikipedia.org/wiki/Watt_(Einheit)) entspricht. Da FreeCAD viele Einheiten unterstützt, vermeidet man am besten kurze Alias. Siehe [Ausdrücke](Expressions/de#Einheiten.md).
    -   Die Verwendung der mathematischen Konstanten `pi` und `e` als Alias führt zu Fehlern und sollte vermieden werden.
    -   Keine Leerzeichen in Aliasen verwenden, da auch sie zu Fehlern führen.





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/de
