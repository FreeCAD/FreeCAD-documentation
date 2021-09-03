---
- GuiCommand:/de
   Name/de:WebTools Git‏‎
   MenuLocation:WebTools → Dienstprogramme → Commit mit Git
   Workbenches:[Arbeitsbereich Web-Werkzeuge](WebTools_Workbench/de.md)
   Version:0.17
---


{{VeryImportantMessage|Beginnend mit FreeCAD v0.17 wurde dieses Werkzeug aus dem Arch-Arbeitsbereich entfernt und ist nun Teil des externen [WebTools-Arbeitsbereich](WebTools_Workbench/de.md)s, der über das Menü Werkzeuge → <img src="images/AddonManager.svg" width=24px> [ErweiterungVerw (Erweiterungsverwalter)](Std_AddonMgr/de.md) installiert werden kann.
}}

## Beschreibung

Dieser Befehl erlaubt die Verwaltung des aktuellen Dokuments mit [Git](https://de.wikipedia.org/wiki/Git). Git ist ein mächtiges System zur Dateiversionskontrolle, welches verschiedene Versionen von Dateien verwalten kann und den Überblick über die Änderungen behält.

Git ist ein komplexes Werkzeug, so dass es sinnvoll ist, die Grundlagen vor der Benutzung zu erlernen, um falsche Operationen zu vermieden, die zu Datenverlust führen können. Reichlich Literatur über Git ist verfügbar und einfach im Internet zu finden.

**Voraussetzung:** Um diesen Befehl nutzen zu können, muss das [gitpython](https://github.com/gitpython-developers/GitPython)-Paket auf Deinem System installiert sein. In den meisten Linux-Distributionen ist gitpython in den Standard-Software-Repositories als *gitpython* oder *python-git* verfügbar.

## Anwendung

1.  Stelle sicher, dass der [Berichtsansicht](Report_view/de.md) geöffnet ist, denn Git-meldungen werden dort angezeigt.
2.  Speichere das aktuelle aktive Dokument und stelle sicher, dass sich die gespeicherte Datei innerhalb eines existierenden Git-Repository befindet. Es kann ein Unterverzeichnis sein.
3.  Wähle das Menü **WebTools → <img src="images/WebTools_Git.svg" width=16px> [Commit mit Git](WebTools_Git/de.md)
**
4.  Dies öffnet ein [Aufgabenpaneel](Task_panel/de.md) in der [Combo Ansicht](Combo_view/de.md).

## Optionen

![Tasks-Reiter zeigt Git-Interface](images/Arch_Git_panel.jpg )

-   Stelle sicher, dass das **Ausgabefenster** geöffnet ist, denn Git-Meldungen werden dort ausgegeben
-   Das Git-Werkzeug wird nur geöffnet, wenn die aktuelle Datei in einem Git-Repository gespeichert ist. Die Datei kann in einem Unterverzeichnis sein.
-   Der **Log**-Button wird einen Dialog öffnen, in dem die aktuellsten Log-Einträge angezeigt werden. Die Ausgabe entspricht git log
-   Der **Refresh**-Button wird das Repository auf geänderte Dateien durchsuchen. Nach dem Speichern deiner Arbeit musst du einen manuellen Refresh durchführen.
-   Der **Diff**-Button wird die Unterschiede zwischen der aktuellen Version einer ausgewählten Datei und der aktuellsten im Repository gespeicherten Vorversion anzeigen. Die Ausgabe entspricht git diff
    -   Als Standardvorgabe wird ein \"binary diff\" ausgeführt, du musst das fcinfo einrichten, um ein \"texutal diffing\" durchzuführen.
-   Der **Select all**-Button wird alle Dateien auswählen, um sie an das Repository zu übergeben (commit)
-   Der **Commit**-Button wird die ausgewählten Dateien an das Repository übergeben (commit). Stelle sicher, eine Commit-Meldung zu erfassen, die die zu übergebenden Änderungen beschreiben
-   Der **Pull**-Button wird jegliche neuen Änderungen aus dem ausgewählten entfernten (remote) Repository in das lokale **herunterladen**. Wenn die aktuell in FreeCAD geöffnete Datei durch einen Pull verändert wird, informiert eine Warnmeldung darüber, so dass die Datei entweder erneut gespeichert oder an einer anderen Stelle gespeichert werden kann
-   Der **Push**-Button wird den/die letzten Commit/s in das entfernte Repository **hochladen**.

## Einschränkungen

-   Das Werkzeug kann bisher keine neuen Repositories anlegen. Ein existierendes lokales Repository muss bereits verfügbar sein (FreeCAD wird prüfen, ob die aktuelle Dokumentendatei in einem Repository ist).
-   Das Werkzeug kann kein Branches ändern oder anlegen. Das muss manuell mit den Standard-Git-Werkzeugen getan werden.

## Aktivieren eines \'lesbaren\' Diffs für FCStd-Dateien mit dem fcinfo-Utility 

FreeCADs [Fcstd-Dateiformat](File_Format_FCStd/de.md) ist ein Zip-basiertes Binärformat, für das Git keine sauber lesbaren Diffs (Unterschiede) erstellen kann. Das bedeutet, dass Du nicht sehen kannst, was sich zwischen der einen und der anderen Version geändert hat und dass jede neue im Git-Repository gespeicherte Version eine vollständige Kopie der Datei ist.

Auch wenn es für das zweite Problem bisher keine Lösung gibt, kann das erste mit einem kleinen Werkzeug aus dem FreeCAD-Quellcode gelöst werden, das [fcinfo](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo) heißt. Git kann angewiesen werden, mit dem fcinfo-Dienstprogramm einen menschlich-lesbaren Bericht einer FCStd-Datei zu drucken und beim Vergleich (diff) von zwei FCStd-Dateien stattdessen einen Vergleich der beiden fcinfo-Berichte zu erzeugen. Bitte beachte, dass dies lediglich eine visuelle \'Rückmeldung\' ist, denn intern wird eine vollständige Version der Datei gespeichert.

Beispiel eines mit fcinfo erstellten diff:


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document: /tmp/43un09_testhouse.FcStd (442K)
-   SHA1: 67c1985a45d93cba57d5bf44490897aba460100d
+Document: /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1: db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment : This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company : uncreated.net
    CreatedBy : Yorik van Havre
    CreationDate : Fri May  9 12:05:54 2014 
    FileVersion : 1
    Id : 
-   Label : testhouse
-   LastModifiedBy : Yorik van Havre
-   LastModifiedDate : 2016-06-28T17:05:57-03:00
+   Label : testhouse2
+   LastModifiedBy : Yorik van Havre
+   LastModifiedDate : Sat Sep 13 20:46:36 2014
+
    License : CC-BY 3.0
    LicenseURL : http://creativecommons.org/licenses/by/3.0/
-   ProgramVersion : 0.17R7800 (Git)
-   TipName : 
+   ProgramVersion : 0.15R3989 (Git)
    Uid : 67e62d8a-6674-4358-92fe-615443be887a
-   Objects: (231)
+   Objects: (221)
        Annotation : Drawing::FeatureViewAnnotation
        Annotation001 : Drawing::FeatureViewAnnotation
        Annotation002 : Drawing::FeatureViewAnnotation
        Annotation003 : Drawing::FeatureViewAnnotation
-       Annotation004 : Drawing::FeatureViewAnnotation
-       Annotation005 : Drawing::FeatureViewAnnotation
        Array : Part::FeaturePython (9K)
        Box : Part::Box (2K)
        Building : App::DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document: /tmp/43un09_testhouse.FcStd (442K)
        Floor : App::DocumentObjectGroupPython
        Floor001 : App::DocumentObjectGroupPython
        Floor002 : App::DocumentObjectGroupPython
-       Frame : Part::FeaturePython (89K)
```

Jede FreeCAD-Datei enthält eine SHA1-Prüfsumme, die sich jedes Mal beim Speichern der Datei ändert, selbst wenn der Inhalt nicht verändert wurde. Deshalb wird fcinfo immer etwas ausgeben, unabhängig davon, ob sich der Inhalt ändert.

Zur Aktivierung der Nutzung von fcinfo (nur Linux und Mac - ToDo: Windows-Anweisungen hinzufügen)

1.  Speichere die fcinfo-Datei irgendwo in deinem System-Pfad
2.  Mache sie ausführbar
3.  Erstelle eine .gitattributes-Datei in deinem Git-Repository und füge die folgende Zeile hinzu:

 *.FCStd diff=fcinfo

Füge die folgenden Zeilen zur .gitconfig-Datei in deinem home-Verzeichnis hinzu: \[diff \"fcinfo\"\] textconv = /Pfad/zu/fcinfo Alternativ kannst du fcinfo mit Argumenten ausführen (z.B. --gui), benutze diesen Herangehensweise \[<https://stackoverflow.com/questions/55601430/how-to-pass-a-filename-> argument-gitconfig-diff-textconv\]: \[diff \"fcinfo\"\] textconv = sh -c \'/path/to/fcinfo \--gui \"\$0\"\'
