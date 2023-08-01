---
- GuiCommand:/de
   Name:Std MergeProjects
   Name/de:Std ProjekteZusammenführen
   MenuLocation:Datei → Projekte zusammenführen...
   Workbenches:All
---

# Std MergeProjects/de



## Beschreibung

Der Befehl **Std ProjekteZusammenführen** fügt den Inhalt einer FreeCAD-Datei in das aktive Dokument ein.



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

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To merge a project use the {{Incode|mergeProject}} method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std MergeProjects/de
