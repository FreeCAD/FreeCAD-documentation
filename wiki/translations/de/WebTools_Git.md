---
- GuiCommand   */de
   Name   *WebTools Git‏‎
   Name/de   *WebWerkzeuge Git‏‎
   MenuLocation   *WebWerkzeuge → Git
   Workbenches   *[Arbeitsbereich WebWerkzeuge](WebTools_Workbench/de.md)
   Version   *0.17
---

# WebTools Git/de


**Beginnend mit FreeCAD v0.17 wurde dieses Werkzeug aus dem Arbeitsbereich Arch entfernt und ist nun Teil des externen Arbeitsbereichs [WebTools](WebTools_Workbench/de.md), der über das Menü Werkzeuge → <img src="images/AddonManager.svg" width=24px> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.
**

## Beschreibung

Dieser Befehl erlaubt die Verwaltung des aktuellen Dokuments mit [Git](https   *//de.wikipedia.org/wiki/Git). GIT ist ein leistungsfähiges Dateiversionskontrollsystem, das verschiedene Dateiversionen verwalten und die Änderungen verfolgen kann.

Git ist ein komplexes Werkzeug, daher solltest du dich mit den Grundlagen vertraut machen, bevor du dieses Werkzeug verwendest, um Fehlbedienungen zu vermeiden, die zu Datenverlusten führen können. Im Internet gibt es eine Fülle von Literatur über GIT, die leicht zu finden ist.

**Voraussetzung   *** Um diesen Befehl verwenden zu können, muss das [gitpython](https   *//github.com/gitpython-developers/GitPython) Paket auf deinem System installiert sein. Auf den meisten Linux Distributionen ist gitpython in den Standard Software Repositorien als *gitpython* oder *python-git* verfügbar.

## Anwendung

1.  Stelle sicher, dass die [Berichtsansicht](Report_view/de.md) geöffnet ist, da die Git Meldungen dort ausgegeben werden.
2.  Speichere das aktuell aktive Dokument und stelle sicher, dass sich die gespeicherte Datei in einem bestehenden Git Repositorium befindet. Es kann sich in einem Unterverzeichnis befinden.
3.  Menü auswählen **Web Werkzeuge → <img src="images/WebTools_Git.svg" width=16px> [Git](WebTools_Git/de.md)
**
4.  Dies öffnet ein [Aufgabenfeld](Task_panel/de.md) in der [Combo Ansicht](Combo_view/de.md).

## Optionen

![Aufgabenreiter zeigt Git Oberfläche](images/Arch_Git_panel.jpg )

-   Die **Protokoll** Schaltfläche klappt einen Dialog auf, in dem die aktuellsten Protokolleinträge angezeigt werden. Die Ausgabe entspricht git log.
-   Die **Aktualisieren** Schaltfläche wird das Repository auf geänderte Dateien durchsuchen. Nach dem Speichern deiner Arbeit musst du einen manuellen Refresh durchführen.
-   Der **Diff** Schaltfläche wird die Unterschiede zwischen der aktuellen Version einer ausgewählten Datei und der aktuellsten im Repository gespeicherten Vorversion anzeigen. Die Ausgabe entspricht git diff
    -   Als Standardvorgabe wird ein \"binary diff\" ausgeführt, du musst das fcinfo einrichten, um ein \"texutal diffing\" durchzuführen.
-   Der **Select all** Schaltfläche wird alle Dateien auswählen, um sie an das Repository zu übergeben (commit)
-   Der **Commit** Schaltfläche wird die ausgewählten Dateien an das Repository übergeben (commit). Stelle sicher, eine Commit-Meldung zu erfassen, die die zu übergebenden Änderungen beschreiben
-   Der **Pull** Schaltfläche wird jegliche neuen Änderungen aus dem ausgewählten entfernten (remote) Repositorium in das lokale **herunterladen**. Wenn die aktuell in FreeCAD geöffnete Datei durch einen Pull verändert wird, informiert eine Warnmeldung darüber, so dass die Datei entweder erneut gespeichert oder an einer anderen Stelle gespeichert werden kann
-   Der **Push** Schaltfläche wird den/die letzten Commit/s in das entfernte Repositorium **hochladen**.

## Begrenzungen

-   Das Werkzeug kann noch keine neuen Repositorien erstellen. Du musst bereits ein lokales Repositorium angelegt haben. (FreeCAD prüft, ob sich die aktuelle Dokumentendatei in einem Git Repositorium befindet.)
-   Das Werkzeug kann keine Zweige ändern oder erstellen. Dies musst du manuell mit Standard Git Werkzeugen machen.

## Aktivieren von menschenlesbaren diffs für FCStd Dateien mit dem Dienstprogramm fcinfo 

FreeCADs [FCStd Dateiformat](File_Format_FCStd/de.md) ist ein Zip-basiertes Binärformat, für das Git keine sauber lesbaren diffs (Unterschiede) erstellen kann. Das bedeutet, dass Du nicht sehen kannst, was sich zwischen der einen und der anderen Version geändert hat und dass jede neue im Git Repositorium gespeicherte Version eine vollständige Kopie der Datei ist.

Auch wenn es für das zweite Problem bisher keine Lösung gibt, kann das erste mit einem kleinen Werkzeug aus dem FreeCAD Quellcode gelöst werden, das [fcinfo](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo) heißt. Git kann angewiesen werden, das fcinfo Dienstprogramm zu verwenden, um einen menschengerechten Bericht einer FCStd Datei auszudrucken, und wenn es aufgefordert wird, einen Vergleich zwischen zwei FCStd Dateien zu erstellen, wird es stattdessen einen Vergleich zwischen den beiden fcinfo Berichten erstellen. Bitte beachte, dass dies nur eine visuelle Rückmeldung ist, eine vollständige Kopie der Datei wird weiterhin intern gespeichert.

Beispiel eines mit fcinfo erstellten diff   *


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document   * /tmp/43un09_testhouse.FcStd (442K)
-   SHA1   * 67c1985a45d93cba57d5bf44490897aba460100d
+Document   * /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1   * db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment    * This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company    * uncreated.net
    CreatedBy    * Yorik van Havre
    CreationDate    * Fri May  9 12   *05   *54 2014 
    FileVersion    * 1
    Id    * 
-   Label    * testhouse
-   LastModifiedBy    * Yorik van Havre
-   LastModifiedDate    * 2016-06-28T17   *05   *57-03   *00
+   Label    * testhouse2
+   LastModifiedBy    * Yorik van Havre
+   LastModifiedDate    * Sat Sep 13 20   *46   *36 2014
+
    License    * CC-BY 3.0
    LicenseURL    * http   *//creativecommons.org/licenses/by/3.0/
-   ProgramVersion    * 0.17R7800 (Git)
-   TipName    * 
+   ProgramVersion    * 0.15R3989 (Git)
    Uid    * 67e62d8a-6674-4358-92fe-615443be887a
-   Objects   * (231)
+   Objects   * (221)
        Annotation    * Drawing   *   *FeatureViewAnnotation
        Annotation001    * Drawing   *   *FeatureViewAnnotation
        Annotation002    * Drawing   *   *FeatureViewAnnotation
        Annotation003    * Drawing   *   *FeatureViewAnnotation
-       Annotation004    * Drawing   *   *FeatureViewAnnotation
-       Annotation005    * Drawing   *   *FeatureViewAnnotation
        Array    * Part   *   *FeaturePython (9K)
        Box    * Part   *   *Box (2K)
        Building    * App   *   *DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document   * /tmp/43un09_testhouse.FcStd (442K)
        Floor    * App   *   *DocumentObjectGroupPython
        Floor001    * App   *   *DocumentObjectGroupPython
        Floor002    * App   *   *DocumentObjectGroupPython
-       Frame    * Part   *   *FeaturePython (89K)
```

Jede FreeCAD Datei enthält eine SHA1 Prüfsumme, die sich jedes Mal beim Speichern der Datei ändert, selbst wenn der Inhalt nicht verändert wurde. Deshalb wird fcinfo immer etwas ausgeben, unabhängig davon, ob sich der Inhalt ändert.

Zur Aktivierung der Nutzung von fcinfo (nur Linux und Mac - ToDo   * Windows Anweisungen hinzufügen)

1.  Speichere die fcinfo Datei irgendwo in deinem Systempfad
2.  Mache sie ausführbar
3.  Erstelle eine .gitattributes-Datei in deinem Git Repositorium und füge die folgende Zeile hinzu   *

 *.FCStd diff=fcinfo

Füge die folgenden Zeilen zur .gitconfig-Datei in deinem home Verzeichnis hinzu   * \[diff \"fcinfo\"\] textconv = /Pfad/zu/fcinfo Alternativ kannst du fcinfo mit Argumenten ausführen (z.B. --gui), benutze diesen Herangehensweise \[<https   *//stackoverflow.com/questions/55601430/how-to-pass-a-filename-> argument-gitconfig-diff-textconv\]   * \[diff \"fcinfo\"\] textconv = sh -c \'/path/to/fcinfo \--gui \"\$0\"\'



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools Git/de
