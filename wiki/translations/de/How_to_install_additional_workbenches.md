---
 TutorialInfo:e
   Topic: Programmierung
   Level: Mittelmäßiger Programmierer
   Time: 15 Minuten
   FCVersion: Alle
   Author: User:R-Frank
   Files: keine
---

# How to install additional workbenches/de







## Beschreibung

Intensivnutzer haben FreeCAD um verschiedene kundenspezifische [externe Arbeitsbereiche](external_workbenches/de.md) erweitert, die nicht in den FreeCAD Quellcodekern integriert sind, sind aber leicht auf einer bestehenden FreeCAD Installation zu installieren. Hier werden wir die Installationsmethoden für die verschiedenen Betriebssysteme behandeln.


**Hinweis:**

Seit Version 0.17 verfügt FreeCAD über einen <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) im Menü **Werkzeuge → Addon-Manager**, das die Installation sowohl von Makros als auch von Arbeitsbereichen erlaubt. Die folgenden Anweisungen sind nur erforderlich, wenn ein Arbeitsbereich manuell installiert werden soll. Dies könnte notwendig sein, wenn aus irgendeinem Grund der Addon-Manager nicht funktioniert, du aber Zugriff auf den als **.zip**-Paket heruntergeladenen Arbeitsbereich hast.


<div class="mw-collapsible mw-collapsed toccolours">



## Installation unter Windows 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen unter Windows installiert


<div class="mw-collapsible-content">



### Manuelle Installation 


**Hinweis:**

Diese Methode ist mit der Einführung des [Addon-Manager](Std_AddonMgr/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

-   Den Arbeitsbereich von github herunterladen, indem die Schaltfläche **Clone** oder **Download** auf der github-Seite (rechte obere Ecke) gedrückt und \"Download ZIP\" ausgewählt wird.
-   Das heruntergeladene Archiv auf deiner lokalen Festplatte entpacken.
-   Innerhalb von FreeCAD den Makropfad finden, indem unter **Bearbeiten → Einstellungen → Python→ Makro** nach dem \"Makropfad\" gesucht wird.
-   Angenommen, dein Windows-Login ist \"*Benutzername*\", dann wird der Standard-Makropfad **%APPDATA%\FreeCAD\** normalerweise zu **C:\Users\''Benutzername''\Appdata\Roaming\FreeCAD**.
-   Innerhalb des Makro-Verzeichnisses einen Ordner namens \"**Mod**\" erstellen (falls nicht bereits vorhanden).
-   Innerhalb des Ordners Mod einen Ordner mit dem Namen des Arbeitsbereichs anlegen, z.B. \"Curves\".
-   Nun die entpackten Dateien und Unterordner des Arbeitsbereichs in den soeben erstellten Arbeitsbereichs-Ordner verschieben.
-   Nach einem Neustart von FreeCAD solltest du nun einen Eintrag in der [Auswahlliste der Arbeitsbereiche](Std_Workbench/de.md) haben

**Zusätzliche Empfehlung zur Aktualisierung von Arbeitsbereichen**

Unter Windows behält Windows beim Aktualisieren eines bereits installierten Arbeitsbereichs die alten .py Dateien als .pyc. Da dies zu Problemen führen kann, wird empfohlen, den Arbeitsbereich zu deinstallieren, FreeCAD neu zu starten und die neue Version des Arbeitsbereichs zu installieren.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Installation unter Linux 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen unter Linux installiert


<div class="mw-collapsible-content">



### git verwenden 

Hinzufügen der [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) innerhalb des ppa-Managers.
Installation der Arbeitsbereiche über den Synaptic-Packet-Manager.


```python
$ sudo apt-get install git python-numpy python-pyside
$ mkdir ~/.FreeCAD/Mod
$ cd ~/.FreeCAD/Mod
$ git clone  https://github.com/tomate44/CurvesWB.git
```

In FreeCAD hast du nun einen neuen Arbeitsbereichs-Eintrag namens \"CurvesWB\". Nach der Installation kannst du git verwenden, um auf die neueste Version zu aktualisieren:


```python
$ cd ~/.FreeCAD/Mod/CurvesWB
$ git pull
$ rm *.pyc
```



### Manuelle Installation 


**Hinweis:**

Diese Methode ist mit der Einführung des [Addon-Manager](Std_AddonMgr/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

-   Den Arbeitsbereich von github herunterladen, indem die Schaltfläche **Clone** oder **Download** auf der github-Seite (rechte obere Ecke) gedrückt und \"Download ZIP\" ausgewählt wird.
-   Das heruntergeladene Archiv auf deiner lokalen Festplatte entpacken.
-   Innerhalb von FreeCAD den Makropfad finden, indem unter **Bearbeiten → Einstellungen → Python→ Makro** nach dem \"Makropfad\" gesucht wird.
-   Standardmäßig ist das Makro-Verzeichnis das (versteckte) Verzeichnis **./.FreeCAD/** in deinem Home-Verzeichnis.
-   Innerhalb des Makro-Verzeichnisses einen Ordner namens \"**Mod**\" erstellen (falls nicht bereits vorhanden).
-   Innerhalb des Ordners Mod einen Ordner mit dem Namen des Arbeitsbereichs anlegen, z.B. \"Curves\".
-   Nun die entpackten Dateien und Unterordner des Arbeitsbereichs in den soeben erstellten Arbeitsbereichs-Ordner verschieben.
-   Nach einem Neustart von FreeCAD solltest du nun einen Eintrag in der [Auswahlliste der Arbeitsbereiche](Std_Workbench/de.md) haben.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installation auf Mac 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen auf macOS installiert


<div class="mw-collapsible-content">



### Manuelle Installation 


**Hinweis:**

Diese Methode ist mit der Einführung des [Addon-Manager](Std_AddonMgr/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

Der Einfachheit halber für dieses Beispiel, sage du hast die [Arbeitsbereich Kurven](Curves_Workbench/de.md) als den externen Arbeitsbereich gewählt, den du installieren möchtest:

-   Wähle das git Repositorium des von dir gewählten externen Arbeitsbereichs aus und lade es als ZIP Datei herunter
-   Es gibt zwei mögliche Speicherorte für deinen Erweiterungs Arbeitsbereich \'Mods\':

1.  Alle Benutzer: **/Applications/FreeCAD.app/Contents/Resources/Mod**
2.  Nur aktueller Anwender: **/Users/myusername/Library/Application Support/FreeCAD/Mod**

-   Wenn du den Finder verwendest, um manuell zum Speicherort \"Alle Benutzer\" in Anwendungen zu navigieren, musst du
    -   zu **/Applications**\" gehen und FreeCAD.app wählen
    -   Klicke mit der rechten Maustaste und wähle \"Paketinhalt anzeigen\", es erscheint ein neues Fenster mit einem Ordner namens \"Inhalt\"
    -   Einfachklick auf den Ordner \"Contents\", dann auf \"Resources\" und Doppelklick, um den Ordner \"Mod\" zu öffnen
-   Sobald du dich in dem gewünschten \"Mod\" Ordner befindest, erstelle einen neuen Ordner namens \"Curves\"
-   Entpacke das heruntergeladene Repositorium in den Ordner \"Mod/Curves\"


</div>


</div>



## Allgemeine Fehlerbehebung 

-   Verwende keine Sonderzeichen (z.B. deutsche Umlaute) in deinem Windows-Benutzernamen, da FreeCAD sonst Dateien und Ordner im Makropfad nicht erkennt.
-   Wenn Du bereits einen Benutzernamen mit Sonderzeichen eingerichtet hast, erstelle entweder einen neuen Benutzernamen oder verweise mit dem Makropfad auf ein Verzeichnis ohne Sonderzeichen.
-   Zu **Bearbeiten → Einstellungen → Arbeitsbereiche** wechseln und sicherstellen, dass der Arbeitsbereich nicht auf ausgeblendet gesetzt ist.
-   Auf einem 32-Bit-System mit FreeCAD 0.16.6706 sind nach einem Installationsversuch die zusätzlichen Arbeitsbereiche möglicherweise nicht verfügbar. In diesem Falle
    -   Beim Start von FreeCAD das [Ausgabefenster](report_view/de.md) geöffnet lassen und den Fehler ansehen.
    -   siehe diesen Forumsbeitrag: [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)



---
⏵ [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > How to install additional workbenches/de
