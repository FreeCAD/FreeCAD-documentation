# Installing on Windows/de



{{docnav/de
|[Funktionalitäten](Feature_list/de.md)
|[ Installieren auf Linux](Install_on_Linux/de.md)
}}

Du kannst FreeCAD unter Windows installieren, indem du einen der folgenden Installer herunterlädst:


{{DownloadWindowsStable}}

Nachdem du die.exe-Datei (NSIS Installer) heruntergeladen hast, doppelklicke auf sie, um den Installationsprozess zu starten.

Nachfolgend sind weitere Informationen zu einigen technischen Optionen. Dennoch benötigen die meisten Benutzer nicht mehr als die oben genannten .exe Dateien. Gehe nach Abschluss der Installation auf [Erste Schritte](Getting_started/de.md).

## Einfache Installation des NSIS Installationsprogramms 

Der einfachste Weg um **FreeCAD unter Windows zu installieren**, ist durch Verwendung des herunterladbaren Installationspakets oben. Diese Seite beschreibt die Verwendung und die Funktionen des *NSIS Installierers* für weitere Installationsoptionen.

Wenn du eine Entwicklungsversion herunterladen möchtest (die möglicherweise instabil ist), lies die Seite [Download](Download/de.md).

## Chocolatey

Jedoch wird dringend empfohlen, dass du einen Paketmanager wie Chocolatey verwendest, um deine Software auf dem neuesten Stand zu halten. Du kannst Chocolatey nach [diese Anweisungen](https://chocolatey.org/install) installieren und dann ein PowerShell Terminal als Administrator öffnen und ausführen:


```python
choco install freecad
```

Von Zeit zu Zeit kannst du deine Software aktualisieren mit


```python
choco upgrade freecad
```

um die neueste Version zu erhalten, die im Chocolatey Repositorium verfügbar ist. Wenn es irgendwelche Probleme mit dem Chocolatey Paket gibt, kannst du dich an die Betreuer unter [auf dieser Seite](https://chocolatey.org/packages/freecad) wenden.

## Befehlszeileninstallation

Mit dem Befehlszeilendienstprogramm *msiexec.exe* stehen zusätzliche Funktionen wie nicht interaktive Installation und administrative Installation zur Verfügung. Siehe Beispiele unten.

### Nicht-Interaktive Installation 

Mit der Befehlszeile


```python
msiexec /i FreeCAD<version>.msi
```

Die Installation kann programmtechnisch ausgelöst werden. Zusätzliche Parameter können am Ende der Befehlszeile übergeben werden, zum Beispiel


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Begrenzte Benutzeroberfläche 

Der Umfang der vom Installationsprogramm erlaubten Benutzerkontrolle kann mit den Optionen /q gesteuert werden:

-   /qn - Keine Oberfläche
-   /qb - Basisoberfläche - zeigt nur einen kleinen Fortschrittsdialog mit Abbruch Schaltfläche
-   /qb! - wie /qb, aber blendet die Abbrechen Schaltfläche aus
-   /qr - Reduzierte Oberfläche - alle Dialoge anzeigen, die keine Benutzereingriffe erfordern (alle modalen Dialoge überspringen)
-   /qn+ - wie /qn, zeigt jedoch zum Schluss den \"Fertiggestellt\"-Dialog

### Zielverzeichnis

Die Eigenschaft TARGETDIR bestimmt das Stammverzeichnis der FreeCAD Installation. Beispielsweise kann ein anderes Installationslaufwerk mit


```python
TARGETDIR=R:\FreeCAD25
```

Das Standard Zielverzeichnis TARGETDIR ist \[Windowslaufwerk\\Programme\\\]FreeCAD.

### Installation für alle Benutzer 

Hinzufügen von


```python
ALLUSERS=1
```

bewirkt eine Installation für alle Benutzer. Standardmäßig wird bei nicht-interaktiver (/i) Installation das Paket nur für den aktuellen Benutzer installiert, während die interaktive Installation einen Dialog anbietet, der \"alle Benutzer\" vorgibt, falls der Benutzer über ausreichend Berechtigung verfügt.

### Funktionsauswahl

Eine Reihe von Eigenschaften ermöglicht die Auswahl von Funktionen, die installiert, neu installiert oder entfernt werden können. Der Satz von Eigenschaften für das FreeCAD Installationsprogramm ist

-   StandardFunktion - Installiere die richtige Software und die Kernbibliotheken.
-   Dokumentation - Installiere die Dokumentation
-   Quellcode - Installieren der Quellen
-   \... ZuTun

Darüber hinaus gibt ALL alle Merkmale an. Alle Funktionen hängen von DefaultFeature ab, so dass die Installation einer Funktion automatisch auch die Standardfunktion installiert. Die folgenden Eigenschaften steuern Funktionen, die installiert oder entfernt werden sollen

-   ADDLOCAL - Liste von Elementen zur Installation auf dem lokalen Rechner
-   REMOVE - Liste vom lokalen Rechner zu entfernender Elemente
-   ADDDEFAULT - Liste von Elementen zum hinzufügen in die Standardkonfiguration (ist lokal für alle FreeCAD-Elemente)
-   REINSTALL - Liste von Elementen zum erneuten installieren/reparieren
-   ADVERTISE - Liste von Elementen zur Durchführung einer angekündigten Installation

Es gibt noch einige weitere Eigenschaften, siehe dazu die MSDN-Dokumentation für mehr Details.

Durch hinzufügen dieser Optionen


```python
ADDLOCAL=Extensions
```

wird der Interpreter selbst installiert und die Erweiterungen registriert, sonst wird nichts installiert.

## Deinstallation

Mit


```python
msiexec /x FreeCAD<version>.msi
```

kann FreeCAD deinstalliert werden. Für die Deinstallation ist es **nicht** nötig, die .MSI-Datei zu besitzen; alternativ kann auch das Paket oder der Produkt-Code angegeben werden. Den Produkt-Code findet man beim Blick auf die Eigenschaften vom Uninstall-Kurzverweis, den FreeCAD im Start-Menu anlegt.

## Administrative Einrichtung 

Mit


```python
msiexec /a FreeCAD<version>.msi
```

kann eine \"administrative\" (Netzwerk)-Installation vorgenommen werden. Die Dateien werden in ein Zielverzeichnis entpackt (sollte ein Netzwerk-Verzeichnis sein), es werden aber keine weiteren Änderungen am lokalen Rechner durchgeführt. Zusätzlich wird eine weitere (kleinere) .MSI Datei im Zielverzeichnis erzeugt, die dann von den Nutzern aufgerufen werden kann, um eine lokale Installation vorzunehmen (zukünftige Versionen werden evtl. auch anbieten, einige Elmente auf dem Netzwerk-Verzeichnis unterzubringen).

Derzeit gibt es kein Benutzer-Interface zur administrativen Installation, somit muss das Zielverzeichnis per Befehlszeile angegeben werden.

Es gibt keine spezielle Uninstall-Prozedur für die Administrative Installation - einfach das Zielverzeichnis löschen, wenn kein Benutzer dies mehr benötigt.

## Werbung

Mit


```python
msiexec /jm FreeCAD<version>.msi
```

wäre es prinzipiell möglich, FreeCAD an einer Maschine \"zu bewerben\" (mit /ju an einen Benutzer). Dies würde dazu führen, dass die Symbole im Startmenü erscheinen und die Erweiterungen registriert werden, ohne dass die Software tatsächlich installiert wird. Die erste Verwendung einer Funktion würde dazu führen, dass dieses Funktion installiert wird.

Der FreeCAD-Installer unterstützt derzeit nur die Ankündigung von Start-Menü-Einträgen, aber keine Ankündigung von Verknüpfungen.

## Automatische Installation auf einer Gruppe von Maschinen 

Mit der Windows Gruppenrichtlinie ist es möglich, FreeCAD auf eine Gruppe von Maschinen automatisch zu installieren. Um dies zu tun, führe die folgenden Schritte durch:

1.  Anmelden auf dem Domain controller
2.  Kopieren der MSI Datei in ein gemeinsames Verzeichnis, auf das alle Zielmaschinen zugangsberechtigt sind.
3.  Öffnen des MMC Snapins \"Aktives Verzeichnis Benutzer und Computer\"
4.  Navigieren zur Gruppe von Computern, die FreeCAD benötigen
5.  Eigenschaften öffnen
6.  Gruppenrichtlinien öffnen
7.  Eine neue Richtlinie einfügen und diese bearbeiten
8.  Unter Computer Konfiguration/Software Installation, wählen Sie Neu / Paket
9.  Wähle die MSI Datei im entsprechenden Netzpfad
10. Optional wähle aus, dass du willst, dass FreeCAD deinstalliert wird, wenn der Computer den Bereich der Richtlinie verlässt.

Gruppenrichtlinien Durchsetzung nimmt üblicherweise einige Zeit in Anspruch, um das Paket zuverlässig einzusetzen, sollten alle Maschinen neu gestartet werden.

## Installation unter Linux mit Crossover Office 

Sie können die Windowsversion von FreeCAD auf einem Linuxsystem installieren, das *CXOffice 5.0.1* verwendet. Starte *msiexec* in der CXOffice Befehlszeile. Nehmen wir z.B. an, das Paket liegt im \"Software\" Verzeichnis, das sich im Laufwerk \"Y:\" befindet:


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD läuft, aber es wurde berichtet, dass die OpenGL Anzeige nicht funktioniert, wie bei anderen Programmen, die unter [Wine](https://de.wikipedia.org/wiki/Wine) laufen, u.a. Google [SketchUp](https://de.wikipedia.org/wiki/SketchUp_(Software)).


{{docnav/de
|[Funktionalitäten](Feature_list/de.md)
|[ Installieren auf Linux](Install_on_Linux/de.md)
}}



