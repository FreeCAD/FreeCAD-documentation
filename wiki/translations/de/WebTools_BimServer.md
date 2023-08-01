---
- GuiCommand:
   Name: WebTools BimServer
   Name/de: WebWerkzeuge BimServer‏‎
   MenuLocation: Web Werkzeuge - Bim Server‏‎
   Workbenches: [Arbeitsbereich WebWerkzeuge](WebTools_Workbench/de.md)
---

# WebTools BimServer/de


**Beginnend mit FreeCAD v0.17 wurde dieses Werkzeug aus dem Arbeitsbereich Arch entfernt und ist nun Teil des externen Arbeitsbereichs [WebTools](WebTools_Workbench/de.md), der über das Menü Werkzeuge → <img src="images/AddonManager.svg" width=24px> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.
**

## Beschreibung

Dieser Befehl erlaubt dir mit einer [BIMServer](http://www.bimserver.org) Instanz zu interagieren, auf dem BIM Server gespeicherte Dateien zu öffnen und neue Überarbeitungen dieser Dateien zu speichern. BIMServer ist ein freies, quelloffenes Serversystem, das für die Arbeit mit IFC Dateien gemacht wurde. In seinem aktuellen Zustand erlaubt es die Verwaltung von Projekten mit mehreren IFC Dateien und die Verwaltung von Überarbeitungen. Sein hochgradig erweiterbares Datenbanksystem und seine Einschubarchitektur erlaubt auch die Gestaltung fortschrittlicher Abfrage/Validierungswerkzeuge und intelligenter Zusammenführungsarbeitsabläufe.

Um diesen Befehl zu verwenden, müssen die folgenden Bedingungen erfüllt sein:

-   Die Python Module **json** und **requests** müssen auf deinem System installiert sein.
-   Du musst Zugang zu einer BIMServer Instanz haben (lies die [BIMServer Dokumentation](https://github.com/opensourceBIM/BIMserver/wiki), um einen BIMServer lokal zu installieren) und die Zugangsdaten (Login und Passwort) für diesen Server haben. Zum Zeitpunkt der Erstellung dieses Artikels ist die stabile Version von BIMServer 1.4, aber wir empfehlen dir, eine der verfügbaren Beta Versionen 1.5.X zu installieren, die viele Zusatzprogramme automatisch installiert (in der Version 1.4 musst du die Zusatzprogramme manuell installieren).
-   Alle Dateiübertragungen mit dem BIMServer werden mit IFC Dateien durchgeführt. Daher musst du wissen, wie man mit [IFC Dateien](Arch_IFC/de.md) arbeitet.

## Anwendung

1.  Stelle sicher, dass die oben genannten Voraussetzungen erfüllt sind und du Zugang zu einer laufenden BIMServer Instanz hast.
2.  Wähle das Menü **Web Werkzeuge → <img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](WebTools_BimServer/de.md)
**
3.  Klicke auf die Schaltfläche **Verbinden** und gib deine Anmeldedaten ein.
4.  Sobald die Verbindung zum BIMServer gemacht wurde, wähle im Aufklappfeld **Projekt** ein Projekt aus, mit dem du arbeiten möchtest.

## Optionen

![](images/Arch_Bimserver_panel.jpg )

-   Wenn dies das erste Mal ist, daß du dich von FreeCAD aus mit einem BIMServer verbindest, drücke die **Verbinden** Schaltfläche und gib die Server URL, deine Anmeldung (die immer eine E-Mail Adresse ist) und dein Passwort in den Dialogkasten ein, der aufklappen wird. Wenn du dich das nächste Mal, wenn du den BimServer Befehl verwendest, automatisch anmelden möchtest, hake die Option **Zugangsdaten speichern** an (dein Login und Passwort werden von FreeCAD nicht gespeichert, nur ein Sitzungscookie).
-   Sobald FreeCAD erfolgreich eine Verbindung zu einer BIMServer Instanz hergestellt hat, wird die Schaltfläche **Verbinden** zu **Verbunden**. Klicke erneut auf die Schaltfläche, um die Verbindung zu trennen. Dadurch wird auch der gespeicherte Sitzungscookie gelöscht, so dass du beim nächsten Mal deine Anmeldedaten erneut eingeben musst.
-   Um das Sitzungscookie manuell zu löschen und alles zurückzusetzen, kannst du einfach die BIMServer URL löschen, die in **Bearbeiten → Einstellungen → Architektur → BimServer** gespeichert ist.
-   Die **Im Browser öffnen** Schaltfläche öffnet die Weboberfläche des BIMServers entweder im FreeCAD internen Webbrowser oder, wenn du diese Option in **Bearbeiten → Voreinstellungen → Architektur → BimServer** markiert hast, in einem externen Webbrowser. So kannst du zum Beispiel neue Projekte erstellen oder die auf dem BIMServer gespeicherten Inhalte analysieren.

### Überarbeitungen Herunterladen 

-   Das Aufklappfeld **Projekt** zeigt die auf dem BIMServer gespeicherten Projekte an. Wähle eines aus, um die verfügbaren Überarbeitungen für dieses Projekt zu sehen.
-   Wähle eine Überarbeitung und klicke auf **Öffnen**, um die IFC Datei, die dieser Überarbeitung entspricht, herunterzuladen und in FreeCAD zu öffnen.
-   Wenn die Schaltfläche **Öffnen** gedrückt wird, öffnet sich ein Dialogfeld, das dir erlaubt die heruntergeladene IFC Datei an einem Ort deiner Wahl speichern zu önnen, bevor du sie öffnest. Wenn du **Abbrechen** drückst, wird die Datei stattdessen unter einem temporären Namen im temporären Verzeichnis des Systems gespeichert.

### Überarbeitungen Hochladen 

-   Wenn du eine neue Überarbeitung hochladen möchtest, vergewissere dich, dass das richtige Projekt im Aufklappfeld **Projekt** ausgewählt wurde.
-   Wähle das **Wurzelobjekt**, das du hochladen möchtest. Es muss entweder ein [Arch Site](Arch_Site/de.md) oder ein [Arch Building](Arch_Building/de.md) sein. Nur Objekte, die zu diesem Stammobjekt gehören, werden hochgeladen.
-   Schreibe einen **Kommentar**, der die Beschreibung (Name) der Überarbeitung sein wird.
-   Drücke die Schaltfläche **Hochladen**. Es öffnet sich ein Dialogfeld, das dir erlaubt die erstellte IFC Datei an einem Ort deiner Wahl speichern zu können, bevor du sie hochlädst. Wenn du auf **Abbrechen** drückst, wird die Datei stattdessen unter einem temporären Namen im temporären Verzeichnis des Systems gespeichert.



---
⏵ [documentation index](../README.md) > WebTools BimServer/de
