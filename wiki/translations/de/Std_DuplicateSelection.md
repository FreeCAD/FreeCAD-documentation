---
- GuiCommand:/de
   Name:Std DuplicateSelection
   Name/de:Std AuswahlDuplizieren
   MenuLocation:Bearbeiten → Auswahl duplizieren
   Workbenches:Alle
   SeeAlso:[Std Ausschneiden](Std_Cut/de.md), [Std Kopieren](Std_Copy/de.md), [Std Einfügen](Std_Paste/de.md)
---

# Std DuplicateSelection/de

## Beschreibung

Der Befehl **Std AuswahlDuplizieren** dupliziert Objekte innerhalb des aktiven Dokuments.

## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Menüeintrag **Bearbeiten → Auswahl duplizieren** auswählen.
3.  Wenn die Objekte Abhängigkeiten besitzen, die nicht ausgewählt wurden, wird ein Dialogfeld zur Angabe der zu berücksichtigenden Abhängigkeiten auffordern.

## Hinweise

-   FreeCAD wird automatisch die internen Namen und, abhängig von den Einstellungen, die Label der Objekte ändern, um Namenskonflikte zu vermeiden.

## Einstellungen

-   Duplizierte Label sind erlaubt, wenn **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → DuplicateLabels** auf `True` gesetzt ist. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Dokument.md) geändert werden.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std DuplicateSelection/de
