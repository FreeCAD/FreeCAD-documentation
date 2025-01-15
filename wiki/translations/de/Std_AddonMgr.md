---
 GuiCommand:
   Name: Std AddonMgr
   Name/de: Std AddonManager
   MenuLocation: Werkzeuge , Addon-Manager
   Workbenches: Alle
   Version: 0.17
   SeeAlso: External_workbenches/de, Macros/de
---

# Std AddonMgr/de



## Beschreibung

Der Befehl **Std Addon-Manager** öffnet den Addon-Manager. Mit dem Addon-Manager können [externe Arbeitsbereiche](external_workbenches/de.md), [Makros](macros/de.md), und [Voreinstellungspakete](Preference_Packs/de.md), die durch die FreeCAD-Gemeinschaft bereitgestellt werden, installiert und verwaltet werden. Standardmäßig stammen die verfügbaren Erweiterungen aus zwei Quellen, [(GitHub) FreeCAD-Addons](https://github.com/FreeCAD/FreeCAD-addons/) und von der Seite [Makrorezepte](Macros_recipes/de.md). Wenn GitPython und git auf dem eigenen System installiert sind, werden zusätzliche Makros von [(GitHub) FreeCAD-Makros](https://github.com/FreeCAD/FreeCAD-macros/) geladen. Benutzerdefinierte Quellen können in den Voreinstellungen des [Addon-Managers](Preferences_Editor/de#Addon-Manager.md) hinzugefügt werden.

Aufgrund von Änderungen an der GitHub-Plattform im Jahr 2020 funktioniert der Addon-Manager nicht mehr, wenn man die FreeCAD-Version 0.17 oder älter verwendet. Man muss auf die Version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) oder neuer aktualisieren. Alternativ könen die Erweiterungen auch manuell installiert werden, siehe [Hinweise](#Hinweise.md) unten.



## Anwendung

1.  Den Menüeintrag **Werkzeuge → <img src="images/Std_AddonMgr.svg" width=16px> Addon-Manager** auswählen.
2.  Wird der Addon-Manager zum ersten Mal verwendet, wird ein Dialogfeld geöffnet, das darauf hinweist, dass die Erweiterungen im Addon-Manager kein offizieller Bestandteil von FreeCAD sind. Es enthält auch mehrere Optionen, die mit der Verwendung von Daten durch den Addon-Manager zusammenhängen. Hat man diese Optionen den eigenen Vorlieben entsprechend eingestellt, drückt man die Schaltfläche **OK**, um zu bestätigen und fortzufahren.
3.  Das Dialogfeld Addon-Manager öffnet sich. Für weitere Informationen siehe [Optionen](#Optionen.md).
4.  Die Schaltfläche **<img src="images/Button_valid.svg" width=16px> Alles aktualisieren** funktioniert zurzeit nicht.
5.  Die Schaltfläche **<img src="images/Process-stop.svg" width=16px> Schließen** drücken, um das Dialogfeld zu schließen.
6.  Wenn ein Arbeitsbereich installiert oder aktualisiert wurde, wird ein neues Dialogfeld geöffnet, das darauf hinweist, dass FreeCAD neu gestartet werden muss, damit die Änderungen wirksam werden.



## Optionen

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  Der Addon-Manager stellt zwei Layouts zur Verfügung: \"Schmal\" and \"Erweitert\". In der \"schmalen\" Ansicht füllt eine Erweiterung eine einzelne Zeile und ihre Beschreibung wird gekürzt, um in den vorhandenen Platz zu passen. \"Erweitert\" stellt zusätzliche Einzelheiten dar, wie weiteren Beschreibungstext und auch Informationen für Bearbeiter, weitere Installationsdetails usw.
2.  Drei Arten von Erweiterungen werden unterstützt: [Arbeitsbereiche](external_workbenches/de.md), [Makros](macros/de.md), und [Voreinstellungspakete](Preference_Packs/de.md). Man kann wählen, ob nur eine Art angezeigt wird oder alle in einer einzigen Liste.
3.  Die Liste kann so eingegrenzt werden, dass sie nur installierte Pakete, nur Pakete mit erhältlichen Aktualisierungen oder nur Pakete, die noch nicht installiert wurden, enthält.
4.  Die Liste kann gefiltert werden durch die Suche nach Schlüsselwörtern in Benennung, Beschreibung und Kennzeichen (Beschreibung und Kennzeichnung müssen vom Addon-Entwickler in den Meta-Daten angegeben werden). Der Filter kann sogar ein regulärer Ausdruck sein, für eine präzise Steuerung des genauen Suchbegriffs.
5.  Die erweiterte Ansicht zeigt enthaltene Versionsinformationen, Beschreibungen, Informationen für Bearbeiter und Informationen zur Version der Installation für Pakete mit einer [Paket-Meta-Daten](Package_Metadata/de.md)-Datei (oder für Makros mit eingebetteten Meta-Daten).
6.  Die Addon-Daten werden lokal zwischengespeichert, mit einer variablen Häufigkeit der Aktualisierung des Zwischnspeichers, festgelegt in den Benutzereinstellungen.
7.  Zu jeder Zeit kann die manuelle Aktualisierung des lokalen Zwischenspeichers ausgewählt werden, um die neuesten verfügbaren Aktualisierungen für alle Erweiterungen anzuzeigen.
8.  Die Suche nach Aktualisierungen kann auf automatisch eingestellt sein oder manuell erfolgen durch einen Klick auf eine Schaltfläche (festgelegt in den Benutzereinstellungen). Wenn GitPython und git auf dem eigenen System installiert sind, werden die Aktualisierungsinformationen unter Verwendung von git abgeholt. Wenn nicht, werden Informationen zu Aktualisierungen aus allen vorhandenen Meta-Daten-Datein ausgelesen.

Klickt man in dieser Ansicht auf eine Erweiterung, wird eine Seite mit Einzelheiten zu dieser Erweiterung geöffnet:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

Diese Seite mit Einzelheiten zeigt Schaltflächen, die es erlauben Erweiterungen zu installieren, zu deinstallieren, zu aktualisieren und zeitweise zu deaktivieren. Sie listet die aktuell installierten Versionen mit dem Installationsdatum und ob es sich um die neueste verfügbare Version handelt. Darunter befindet sich ein eingebettetes Webbrowser-Fenster, das die README-Seite der Erweiterung anzeigt (für Arbeitsbereiche und Voreinstellungspakete), oder die Wiki-Seite (für Makros).



## Einstellungen

Die Einstellungen für den Addon-Manager findet man im [Voreinstellungseditor](Preferences_Editor/de#Addon-Manager.md). {{Version/de|0.20}}



## Sortieren nach Punktzahl 


{{Version/de|1.0}}

Der Addon-Manager unterstützt das Sortieren nach einer Reihe verschiedener Kriterien. Die meisten davon werden direkt von den Servern von FreeCAD heruntergeladen (die sie von GitHub und FreeCAD-Wiki zwischenspeichern), aber ein „Score" wird von FreeCAD überhaupt nicht bereitgestellt und erscheint nur als Option, wenn die Einstellung „Score-Quell-URL" in den Einstellungen angegeben ist.

Die Score-Quell-URL ist ein Pfad zu einem Remote-Dokument im JSON-Format, das Add-Ons und eine Art „Score" auflistet. Der Score kann vom Datenanbieter beliebig berechnet werden, sollte aber ein ganzzahliger Wert sein, wobei höhere Scores in gewisser Weise „besser" sind. Jedem nicht aufgeführten Add-On wird intern ein Score von 0 zugewiesen. Das Format der Datei ist ein einzelnes JSON-Wörterbuch, wobei der Schlüssel die Add-On-URL (für Workbenches und Preference Packs) oder der Name des Makros (für Makros) ist. Ein Beispiel findest du unter [diese Datenquelle](https://gist.githubusercontent.com/chennes/e8f60e80f16e6ffbd057dd47ca36ad2a/raw/7b118cca8e84444c3379919bbd744b99e6ef6711/addon_score_for_testing.json) (beachte, dass die Punktzahl dort lediglich der Länge der Add-on-Beschreibung entspricht und nur für Test- und Demonstrationszwecke vorgesehen ist).



## Hinweise

-   Die Verwendung von Erweiterungen ist nicht auf die FreeCAD-Version beschränkt, mit der sie installiert wurden. Sie können auch in jeder anderen FreeCAD-Version verwenden, die von der Erweiterung unterstützt wird, die möglicherweise auf dem eigenen System vorhanden ist.
-   Die im Addon-Manager verfügbaren Erweiterungen sind nicht Teil des offiziellen FreeCAD-Programms und werden vom FreeCAD-Kernentwicklungsteam nicht unterstützt. Man solltet die bereitgestellten Informationen sorgfältig lesen, um sicherzustellen, daß man weiß, was man installiert.
-   Fehlerberichte und Anfragen für neue Funktionen sollten direkt an den Ersteller der Erweiterung gerichtet werden, durch Besuch der angegebene Webseite. Viele Erweiterungsentwickler sind regelmäßige Nutzer des [FreeCAD-Forums](https://forum.freecadweb.org), und können dort auch kontaktiert werden.
-   Wenn das [GitPython](https://github.com/gitpython-developers/GitPython)-Paket auf dem eigenen Computer installiert ist, wird der Addon-Manager davon Gebrauch machen, was das Herunterladen beschleunigt.
-   Die Erweiterungen können auch manuell installiert werden. Siehe [Wie man zusätzliche Arbeitsbereiche installiert](How_to_install_additional_workbenches/de.md) und [Wie man Makros installiert](How_to_install_macros/de.md).



## Informationen für Addon-Entwickler 

Siehe [Erweiterung](Addon/de#Informationen_für_Entwickler.md).



## Skripten


{{Version/de|0.21}}

Einige Funktionen des Addon-Managers sind so ausgelegt, dass auf sie über FreeCADs Python-API zugegriffen werden kann. Im einzelnen kann ein Addon über die Python-Schnittstelle installiert, aktualisiert und entfernt werden. Die meisten Anwendungen dieser API erfordern, dass ein Objekt mit mindestens drei Attributen angelegt wird: {{Incode|name}}, {{Incode|branch}} und {{Incode|url}}. Zum Beispiel:


```python
class MyAddonClass:
    def __init__(self):
        self.name = "TestAddon"
        self.url = "https://github.com/Me/MyTestAddon"
        self.branch = "main"
my_addon = MyAddonClass()
```

Das Objekt {{Incode|my_addon}} ist jetzt Bereit für den Einsatz mit der Addon-Manager-API.



### Verwendung der Befehlszeile (ohne GUI) 

Wenn dein Code ein Add-on synchron installieren oder aktualisieren muss (z. B. ohne GUI), kann der Code sehr einfach sein:


```python
from addonmanager_installer import AddonInstaller
installer = AddonInstaller(my_addon)
installer.run()
```

Beachte, dass dieser Code blockiert, bis er abgeschlossen ist. Du solltest ihn daher nicht im Haupt-GUI-Thread ausführen. Für den Addon-Manager sind „Installieren" und „Aktualisieren" derselbe Aufruf: Wenn dieses Addon bereits installiert ist und Git verfügbar ist, wird es über „Git Pull" aktualisiert. Wenn es nicht installiert ist oder über eine andere Installationsmethode als Git installiert wurde, wird es von Grund auf neu heruntergeladen (mit Git, falls verfügbar).

Zum Deinstallieren verwende:


```python
from addonmanager_uninstaller import AddonUninstaller
uninstaller = AddonUninstaller(my_addon)
uninstaller.run()
```



### GUI-Verwendung 

Wenn du planst, deinen Code in einer GUI auszuführen oder die Ausführung in der Vollversion von FreeCAD zu unterstützen, ist es am besten, deine Installation in einem separaten Nicht-GUI-Thread auszuführen, damit die GUI reaktionsfähig bleibt. Überprüfe dazu zunächst, ob die GUI ausgeführt wird, und starte in diesem Fall einen {{Incode|QThread}} (versuche nicht, einen {{Incode|QThread}} zu starten, wenn die GUI nicht aktiv ist: sie benötigt eine aktive Ereignisschleife, um zu funktionieren).


```python
from PySide import QtCore
from addonmanager_installer import AddonInstaller

worker_thread = QtCore.QThread()
installer = AddonInstaller(my_addon)
installer.moveToThread(worker_thread)
installer.success.connect(installation_succeeded)
installer.failure.connect(installation_failed)
installer.finished.connect(worker_thread.quit)
worker_thread.started.connect(installer.run)
worker_thread.start() # Returns immediately
```

Definiere dann die Funktionen {{Incode|installation_succeeded}} und {{Incode|installation_failed}}, die in jedem Fall ausgeführt werden sollen. Für die Deinstallation kannst du dieselbe Technik verwenden, obwohl sie normalerweise viel schneller ist und die GUI nicht sehr lange blockiert. Daher ist es im Allgemeinen sicher, das Deinstallationsprogramm direkt zu verwenden, wie oben gezeigt.



---
⏵ [documentation index](../README.md) > Std AddonMgr/de
