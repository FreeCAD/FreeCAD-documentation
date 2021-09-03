 {{TutorialInfo/de
|Topic=Programmierung
|Level=Mittelmäßiger Programmierer
|Time=15 Minuten
|FCVersion=Alle
|Author=[r-frank](User:R-Frank.md)
|Files=keine
}}

## Beschreibung

Intensivnutzer haben FreeCAD um verschiedene kundenspezifische [externe Arbeitsbereiche](external_workbenches/de.md) erweitert, die nicht in den FreeCAD Quellcodekern integriert sind, sind aber leicht auf einer bestehenden FreeCAD Installation zu installieren. Hier werden wir die Installationsmethoden für die verschiedenen Betriebssysteme behandeln.


**Hinweis:**

Ab Version 0.17 verfügt FreeCAD über einen <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Erweiterungsverwalter](Addon_Manager/de.md) im **Werkzeuge → Erweiterungsverwalter** Menü, das die Installation sowohl von Makros als auch von Workbenches erlaubt. Die folgenden Anweisungen sind nur erforderlich, wenn du einen Arbeitsbereich manuell installieren möchtest. Dies könnte notwendig sein, wenn aus irgendeinem Grund der Erweiterungsverwalter nicht funktioniert, du aber Zugriff auf den als {{FileName|.zip}} Paket heruntergeladenen Arbeitsbereich hast.


<div class="mw-collapsible mw-collapsed toccolours">

## Installation unter Windows 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen unter Windows installiert


<div class="mw-collapsible-content">

### Veraltet


**Hinweis:**

Die Verwendung des \"Erweiteruns-Installierers\" wird nicht mehr empfohlen. Die Verwendung des [Erweiterungsverwalters](Addon_Manager/de.md) in allen Systemen ist der empfohlene Weg.

Benutze den [addons-installer von Github](https://github.com/FreeCAD/FreeCAD-addons).

Während des Google Summer of Code 2016 begann der Student Mandeep Singh mit der Arbeit an einer verbesserten Version ([hier verfügbar](https://github.com/mandeeps708/PluginManager)), die jedoch noch weitere Bearbeitung benötigt, bevor sie vollständig in FreeCAD integriert werden kann.

### Manuelle Installation 


**Hinweis:**

Diese Methode ist mit der Einführung des [Erweiterungsverwalters](Addon_Manager/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

-   Lade den Arbeitsbereich von github herunter, durch anklicken auf die Schaltfläche **Clone** oder **Download** auf der github Seite (obere rechte Ecke) klickest und \"Download ZIP\" wählst
-   Entpacke das heruntergeladene Archiv auf deiner lokalen Festplatte
-   Suche innerhalb von FreeCAD den Makropfad, durch Wahl von **Bearbeiten → Einstellungen → Allgemein→ Makro** und nach dem \"Makropfad\" suchen.
-   Angenommen, dein Windows-Login ist \"*Benutzername*\", dann ist der Standard Makropfad {{FileName|%APPDATA%\FreeCAD\}}, der normalerweise {{FileName|C:\Users\''username''\Appdata\Roaming\FreeCAD}} ist.
-   Erstelle innerhalb des Makro-Verzeichnisses einen Ordner (falls nicht bereits vorhanden) namens \"{{FileName|Mod}}\"
-   Lege innerhalb des Ordners Mod einen Ordner mit dem Namen des Arbeitsbereichs an, z.B. \"Curves\".
-   Verschiebe nun die entpackten Dateien und Unterordner des Arbeitsbereichs in den soeben erstellten Arbeitsbereichs-Ordner
-   Nach dem Neustart von FreeCAD solltest du nun einen Eintrag im [Arbeitsbereichsanwähler](Std_Workbench/de.md) haben

**Zusätzliche Empfehlung zur Aktualisierung von Arbeitsbereichen**

Unter Windows behält Windows beim Aktualisieren eines bereits installierten Arbeitsbereichs die alten .py Dateien als .pyc. Da dies zu Problemen führen kann, wird empfohlen, den Arbeitsbereich zu deinstallieren, FreeCAD neu zu starten und die neue Version des Arbeitsbereichs zu installieren.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installation unter Linux 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen unter Linux installiert


<div class="mw-collapsible-content">

### Benutzung von git 

Hinzufügen der [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) innerhalb des ppa-manager.
Installation der Arbeitsbereiche über synaptische Paketmanager.


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

Diese Methode ist mit der Einführung des [Erweiterungsverwalters](Addon_Manager/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

-   Lade den Arbeitsbereich von github durch Klicken auf die Schaltfläche **Clone** oder **Download** auf der github Seite (obere rechte Ecke) und Auswahl von \"Download ZIP\"
-   Entpacke das heruntergeladene Archiv auf deiner lokalen Festplatte
-   Ermittle innerhalb von FreeCAD den Makropfad,durch wählen von **Bearbeiten→ Einstellungen → Allgemein → Makro** und schau nach dem "Makropfad"
-   Standardmäßig ist das Makro Verzeichnis das (versteckte) **./.FreeCAD/** Verzeichnis in deinem Home-Verzeichnis
-   Erstelle innerhalb des Makro-Verzeichnisses (falls nicht bereits vorhanden) einen Ordner namens \"{{FileName|Mod}}\"
-   Erstelle innerhalb des Mod/ Ordners einen Ordner mit dem Namen des Arbeitsbereichs, zum Beispiel \"Curves\"
-   Verschiebe nun die entpackten Dateien und Unterordner des Arbeitsbereichs in den soeben erstellten Arbeitsbereichs-Ordner
-   Nach dem Neustart von FreeCAD solltest du nun einen Eintrag im [Arbeitsbereichswähler](Std_Workbench/de.md) haben


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installation auf Mac 

Wie man zusätzliche Arbeitsbereiche und Erweiterungen auf MacOS installiert


<div class="mw-collapsible-content">

### Manuelle Installation 


**Hinweis:**

Diese Methode ist mit der Einführung des [Erweiterungsverwalters](Addon_Manager/de.md) möglich, aber nicht notwendig. Nichtsdestotrotz können die Informationen hier für einige noch nützlich sein.

Der Einfachheit halber für dieses Beispiel, sage du hast die [Arbeitsbereich Kurven](Curves_Workbench/de.md) als den externen Arbeitsbereich gewählt, den du installieren möchtest:

-   Wähle das git Repositorium des von dir gewählten externen Arbeitsbereichs aus und lade es als ZIP Datei herunter

-   Es gibt zwei mögliche Speicherorte für deinen Erweiterungs Arbeitsbereich \'Mods\':

1.  Alle Benutzer: {{FileName|/Applications/FreeCAD.app/Contents/Resources/Mod}}
2.  Nur aktueller Anwender: {{FileName|/Users/myusername/Library/Preferences/FreeCAD/Mod}}

-   Wenn du den Finder verwendest, um manuell zum Speicherort \"Alle Benutzer\" in Anwendungen zu navigieren, musst du
    -   zu {{FileName|/Applications}}\" gehen und FreeCAD.app wählen
    -   Klicke mit der rechten Maustaste und wähle \"Paketinhalt anzeigen\", es erscheint ein neues Fenster mit einem Ordner namens \"Inhalt\"
    -   Einfachklick auf den Ordner \"Contents\", dann auf \"Resources\" und Doppelklick, um den Ordner \"Mod\" zu öffnen
-   Sobald du dich in dem gewünschten \"Mod\" Ordner befindest, erstelle einen neuen Ordner namens \"Curves\"
-   Entpacke das heruntergeladene Repositorium in den Ordner \"Mod/Curves\"


</div>


</div>

## Allgemeine Fehlerbehebung 

-   Verwende keine Sonderzeichen (z.B. deutsche Umlaute) in deinem Windows Benutzernamen, da FreeCAD sonst Dateien und Ordner im Makropfad nicht erkennt.
-   Wenn Du bereits einen Benutzernamen mit Sonderzeichen eingerichtet hast, erstelle entweder einen neuen Benutzernamen oder zeige den Makropfad auf ein Verzeichnis ohne Sonderzeichen.
-   Gehe zu **Werkzeuge → Anpassen → Arbeitsbereiche** und stelle sicher, dass der Arbeitsbereich nicht auf ausgeblendet gesetzt ist.
-   Mit 32-Bit System und FreeCAD 0.16.6706, nach dem Versuch der Installation sind die zusätzlichen Arbeitsbereiche möglicherweise nicht verfügbar. In diesem Fall
    -   Halte beim Start von FreeCAD das [Berichtsfenster](report_view/de.md) geöffnet und lies den Fehler.
    -   siehe diesen Forumsbeitrag: [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)


 {{Powerdocnavi}}

[Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md) [Category:Addons{{\#translation:}}](Category:Addons.md)
