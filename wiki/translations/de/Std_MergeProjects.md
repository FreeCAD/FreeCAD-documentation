---
 GuiCommand:
   Name: Std MergeProjects
   Name/de: Std ProjekteZusammenführen
   MenuLocation: Datei , Dokument zusammenführen...
   Workbenches: Alle
---

# Std MergeProjects/de



## Beschreibung

Der Befehl **Std ProjekteZusammenführen** fügt den Inhalt einer FreeCAD-Datei in das aktive Dokument ein.



## Anwendung

1.  Wähle **Datei → <img src="images/Std_MergeProjects.svg" width=16px> Dokument zusammenführen...** aus dem Menü.
2.  Wähle eine FreeCAD-Datei im aufgehenden Dialog.
3.  Klicke auf die Schaltfläche **Öffnen**.



## Optionen

-   Drücke die **esc**-Taste oder klicke auf die Schaltfläche **Abbrechen** um abzubrechen.



## Hinweise

-   Ein Projekt nicht mit sich selbst zusammengeführt werden. Die Auswahl der aktuellen Datei ist nicht erlaubt.
-   FreeCAD ändert automatisch die internen Namen und, abhängig von den [Einstellungen](Preferences_Editor/de#Dokument.md), die Benennungen der Objekte, um Konflikte zu vermeiden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um ein Projekt hinzuzufügen, wird die Methode `mergeProject` des Dokumentobjekts verwendet.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std MergeProjects/de
