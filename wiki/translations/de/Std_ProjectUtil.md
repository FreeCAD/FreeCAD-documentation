---
- GuiCommand:/de
   Name:Std ProjectUtil
   Name/de:Std ProjektHilfsprogramm
   MenuLocation:Werkzeuge → Projekt Hilfsprogramm...
   Workbenches:Alle
---

## Beschreibung

Mit dem **Std ProjectUtil** Befehl kannst du Dateien aus einer FreeCAD Projektdatei ({{FileName|*.FCStd}}), die eigentlich eine [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)) Datei ist, extrahieren und nach manueller Bearbeitung daraus eine neue Projektdatei erstellen.

![](images/Project_utility_en.png ) *Das Projekt Hilfsprogramm Dialogfeld*

## Anwendung

### Projekt extrahieren {#projekt_extrahieren}

1.  Wähle die Option {{MenuCommand/de|Werkzeuge → <img src="images/Std_ProjectUtil.svg" width=16px> Projekt Hilfsprogramm...}} aus dem Menü.
2.  Das Projekthilfsprogramm Dialogfeld wird geöffnet.
3.  Drücke die **...** Schaltfläche rechts von {{MenuCommand/de|Projekt extrahieren → Quelle}}.
4.  Wähle die {{FileName|*.FCStd}} Datei, die du bearbeiten möchtest.
5.  Drücke die **...** Schaltfläche rechts neben {{MenuCommand/de|Projekt extrahieren → Ziel}}.
6.  Wähle einen Ordner, in den die Projektdatei extrahiert werden soll. Es ist ratsam, einen leeren Ordner zu wählen.
7.  Drücke die **Extrahieren** Schaltfläche.
8.  Drücke die **Close** Schaltfläche, um das Dialogfeld zu schließen.

### Manuelle Bearbeitungen {#manuelle_bearbeitungen}

Es ist wichtig zu erkennen, dass die Dateien innerhalb einer FreeCAD-Projektdatei miteinander verknüpft sind. Nur die Bearbeitung einer einzelnen Datei führt typischerweise zu Fehlern. Um konsistente Bearbeitungen über mehrere Dateien hinweg vorzunehmen, verwenden Sie einen guten Code-Editor, wie z.B. [Notepad++](http://notepad-plus-plus.org/) (für das Windows-Betriebssystem) oder [Notepadqq](https://notepadqq.com/s/) (für Linux-Betriebssysteme).

### Projekt erstellen {#projekt_erstellen}

1.  Wähle die {{MenuCommand/de|Werkzeuge→ <img src="images/Std_ProjectUtil.svg" width=16px> 
     Projekthilfsprogramm...}} Option aus dem Menü.
2.  Das Projekthilfsprogramm Dialogfeld wird geöffnet.
3.  Drücke die **...** Schaltfläche rechts neben {{MenuCommand/de|Projekt erstellen→ Quelle}}.
4.  Wähle die {{FileName|Document.xml}} Datei. Der Befehl wird automatisch alle verknüpften Dateien finden.
5.  Drücke die **...** Schaltfläche rechts neben {{MenuCommand/de|Projekt erstellen →Ziel}}.
6.  Wähle einen Ordner, in dem die neue Projektdatei erstellt werden soll.
7.  Drücke die **Erstellen** Schaltfläche.
8.  Eine neue Projektdatei mit einem festen Namen, {{FileName|project.fcstd}}, wird im gewählten Ordner erstellt. Es erfolgt keine Warnung, wenn eine Datei mit diesem Namen bereits vorhanden ist.
9.  Aktiviere optional das {{CheckBox|TRUE|Projektdatei nach Erstellung laden}} Kontrollkästchen.
10. Drücke die **Schließen** zum Schließen des Dialogfelds.

## Hinweise

-   Für weitere Informationen über das FreeCAD Projekt Dateiformat siehe [Dateiformat FCStd](File_Format_FCStd/de.md).





{{Std Base navi

}}  
