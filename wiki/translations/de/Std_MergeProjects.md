---
- GuiCommand:/de
   Name:Std MergeProjects
   Name/de:Std Projekte zusammenführen
   Workbenches:Alle
   MenuLocation:[Datei](Std_File_Menu/de.md) → Projekt zusammenführen
   Shortcut:
   SeeAlso:
---

# Std MergeProjects/de

## Beschreibung

Die **Std Projekt zusammenführen** fügt den Inhalt einer FreeCAD-Datei dem aktiven Dokument bei.

## Anwendung

1.  Wähle **Datei → <img src="images/Std_MergeProjects.svg" width=16px> Projekt zusammenführen...** aus dem Menü.
2.  Wähle eine FreeCAD-Datei im aufgehenden Dialog.
3.  Klicke auf die Schaltfläche **Öffnen**.

## Optionen

-   Drücke die **esc**-Taste oder klicke auf die Schaltfläche **Abbrechen** um abzubrechen.

## Hinweise

-   Ein Projekt nicht mit sich selbst zusammengeführt werden. Die Auswahl der aktuellen Datei ist nicht erlaubt.
-   FreeCAD ändert automatisch die internen Namen und die Beschriftungen der Objekte, abhängig von den Einstellungen, um Konflikte zu vermeiden.

## Einstellungen

-   Der letzte, verwendete Dateiablageort wird gespeichert: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Doppelte Beschriftungen sind erlaubt, wenn **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → DuplicateLabels** auf `True` gesetzt ist. Diese Einstellung kann auch im [Voreinstellungseditor / Dokument](Preferences_Editor/de#Dokument.md) geändert werden.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MergeProjects/de
