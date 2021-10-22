# Installing on Linux/de
{{TOCright}}

## Übersicht

Die Installation von FreeCAD auf den bekanntesten Linux Systemen wurde nun von der Gemeinschaft befürwortet, und FreeCAD sollte direkt über den in Ihrer Distribution verfügbaren Paketmanager verfügbar sein. Die FreeCAD Mannschaft stellt auch einige zur Verfügung:

-   \"Offizielle\" Pakete, wenn neue Versionen erstellt werden
-   Experimentelle _ und [Ubuntu Snaps](Ubuntu_Snap.md) zum Testen nicht ausgereifter Funktionen.


<div class="mw-collapsible mw-collapsed toccolours">

## Ubuntu und Ubuntu-basierte Systeme 

Viele Linuxdistributionen basieren auf Ubuntu und teilen Ihre Repositorien. Neben den offiziellen Varianten (Kubuntu, Lubuntu und Xubuntu) gibt es nicht offizielle Ableitungen wie etwa Linux Mint, Voyager und andere. Die nachfolgenden Installationsoptionen sollten kompatibel zu allen diesen Systemen sein.


<div class="mw-collapsible-content">

### Offizielle Version 

FreeCAD ist in den Ubuntu Universum Repositorien verfügbar und kann über das {{MenuCommand/de|Software Center}} oder im Terminal installiert werden:


```python
sudo apt install freecad
```


**Hinweis:**

Das Ubuntu Universe Paket kann veraltet sein, da die Packung hinter dem neuesten stabilen Quellcode zurückbleiben kann. In diesem Fall wird empfohlen, das Paket aus dem `-stable` zu installieren. PPA unten. Darüber hinaus kann die Installation des Pakets `-daily` durchgeführt werden, um den Entwicklungszweig zu testen.

### Stabile PPA Version 

Persönliches Paket Archiv (PPA) für die stabile FreeCAD Version wird von der FreeCAD Gemeinschaft auf Launchpad gepflegt. Das Launchpad Repositorium heißt [FreeCAD Stable Releases](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable).

#### GUI

Installiere das stabile PPA über die grafische Benutzeroberfläche (GUI):

:   1\. Navigiere zu {{MenuCommand/de|Ubuntu Software → Software & Aktualisierungen → Softwarequellen → Andere Software}}
:   2\. Klicke auf **Hinzufügen**, dann kopiere und füge die folgende Zeile ein

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Füge die Quelle hinzu, schließe den Dialog und lade deine Softwarequellen neu, falls du dazu aufgefordert wirst.

Jetzt kannst Du die letzte stabile FreeCAD Version über das {{MenuCommand/de|Ubuntu Software Center}} finden und installieren.

#### CLI

Installiere das stabile PPA über die Befehlszeilenoberfläche (CLI):

:   1\. Füge das PPA zu deinen Softwarequellen hinzu:

    :   
        
```python
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        
```
        





:   2\. Rufe die aktualisierten Paketlisten ab:

    :   
        
```python
        sudo apt update
        
```
        





:   3\. Installiere dann FreeCAD zusammen mit der Offline Dokumentation:

    :   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Hinweis:**

Aufgrund von Packungsproblemen ist das Paket `freecad-doc` in bestimmten Versionen von Ubuntu mit der Installation von FreeCAD oder einer seiner Abhängigkeiten kollidiert; wenn dies der Fall ist, entferne das Paket `freecad-doc`, und installiere nur das Paket `freecad`. Wenn das Paket `freecad-doc` nicht existiert, dann ignoriere es.

#### Installation prüfen 

:   4\. Sobald du das stabile PPA zu deinen Quellen hinzugefügt hast, das `freecad` Paket wird diese PPA-Version installieren über derjenigen, die vom Ubuntu Universe Repository bereitgestellt wird. Die verfügbaren Versionen kannst Du mit `apt-cache` sehen.
:   
    
```python
    apt-cache policy freecad
    
```
    





:   Die Ausgabe sollte ähnlich wie die folgende aussehen (natürlich werden die Versionsangaben variieren):


```python
freecad:
  Installed: (none)
  Candidate: 2:0.18.4+dfsg1~201911060029~ubuntu18.04.1
  Version table:
     2:0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
        500 http://ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
     0.16.6712+dfsg1-1ubuntu2 500
        500 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
ubuntu@ubuntu:~$ apt-cache policy freecad-doc
```


:   5\. Rufe die stabile (PPA) Version von FreeCAD über die GUI oder CLI auf. Die letztere Methode ist wie folgt:
:   
    
```python
    ./freecad
    
```
    

### Entwicklungs PPA (Täglich) 

Da sich FreeCAD in ständiger Entwicklung befindet, kannst Du das **Tägliche** installieren, um mit den neuesten Verbesserungen und Fehlerkorrekturen Schritt zu halten. Das Repositorium wird auch auf Launchpad bereitgestellt und heißt [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

Diese Version wird täglich aus dem offiziellen Haupt Repositorium erstellt. Bitte beachte, dass es zwar neue Funktionen und Fehlerbehebungen enthält, aber auch neuere Fehler aufweisen und instabil sein kann.

Füge das tägliche PPA zu Deinen Softwarequellen hinzu, aktualisiere die Paketlisten und installiere das tägliche Paket: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Jeden Tag kannst Du täglich auf den neuesten Stand aktualisieren: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Hinweis:**

In einigen Fällen führt neuer Code oder führen Abhängigkeiten, die zu FreeCAD hinzugefügt werden, zu Packungsfehlern; in diesem Fall kann es vorkommen, dass kein tägliches Paket generiert wird, bis die Verantwortlichen die Probleme manuell beheben. Wenn du den neuesten Code weiter testen möchtest, solltest du den Quellcode holen und FreeCAD direkt kompilieren; Anweisungen dazu findest Du unter [Kompilieren](compiling/de.md).

Führe die tägliche (PPA) Version von FreeCAD aus:

:   
    
```python
    freecad-daily
    
```
    


**Hinweis:**

es ist möglich, sowohl die `-stable` als auch `-daily` Pakete im gleichen System zu installieren. Dies ist nützlich, wenn du mit einer stabilen Version arbeiten und trotzdem die neuesten Funktionen in der Entwicklung testen möchtest. Beachte, dass die ausführbare Datei für die tägliche Version `freecad-daily` ist, aber für die stabile Version ist es nur `freecad`.


</div>


</div>

## Debian und andere Debian-basierte Systeme 

Seit Debian Lenny ist FreeCAD direkt aus den Debian Software Repositorien verfügbar und kann über Synaptic oder einfach installiert werden mit:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD wird typischerweise mit YAST (Abk. Yet another Setup Tool)(deutsch: Noch ein anderes Einrichtungswerkzeug), dem Einrichtungs- und Konfigurationswerkzeug für das Linux Betriebssystem, oder in jedem Terminal/Konsole (root Rechte erforderlich) mit:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Hinweis:**

Dieses Verfahren bezieht sich nur auf die Installation offiziell freigegebener **stabiler** FreeCAD Programmversionen, abhängig von den installierten Verknüpfungen zu den Programmpaket Repositorien deiner Betriebssystemversion. Das openSUSE Paket kann *veraltet* sein, da das Paket hinter dem neuesten stabilen Quellcode zurückbleiben kann. In diesem Fall wird empfohlen, das Paket manuell aus den unten angegebenen (Expand) Quellcode Repositorien zu installieren.


<div class="mw-collapsible-content">

Ein umfassendes Versionsprogramm mit erstellten FreeCAD-Paketen wird angeboten.

[Übersicht über stabile Repositorien auf openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)

Im Allgemeinen ist es für die Auswahl der richtigen openSUSE Distribution erforderlich, auf die jeweilige **View** Schaltfläche zu klicken.

### Stabil

Die stabile Paketversion: [Stabile Repositorien unter openSUSE](https://software.opensuse.org/package/FreeCAD). Die richtige openSUSE Distributionsversion muss im unteren Teil der Webseite ausgewählt werden.

Hinweis: openSUSE hat mehrere Optionen zur Auswahl, wenn du FreeCAD herunterlädst. Um diese Optionen zu sehen, besuche [Übersicht über stabile Repositorien unter openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Entwicklung

Die neueste Entwicklungsversionen auch bekannt als **instabil**: [Auflistung instabiler Repositorien auf openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

Empfohlen wird, die Binärpakete direkt zu beziehen. Wähle dann die richtige Distribution für Dein installiertes openSUSE Betriebssystem aus.


</div>


</div>

## Gentoo

FreeCAD kann einfach erstellt bzw. installiert werden durch Herausgabe:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD ist seit Fedora 20 in den offiziellen Fedora Paketen enthalten. Es kann über die Befehlszeile installiert werden mit:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

Bei älteren Fedora-Versionen war das so:


```python
sudo yum install freecad
```

Der gui Paketmanager kann ebenfalls verwendet werden. Suche nach \"freecad\". Die offizielle Versionspaketversion liegt tendenziell weit hinter den FreeCAD Versionen zurück. [Packet: Freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) zeigt die Versionen, die in den Fedora Repositorien nach Zeit und den Versionen enthalten sind.

Weitere aktuelle Versionen können durch Herunterladen einer der folgenden Versionen bezogen werden [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)Versionen aus dem github Repositorium. Diese funktionieren auf Fedora gut.

Wenn du mit den absolut neuesten täglichen Bauten auf dem Laufenden bleiben möchtest, ist FreeCAD auch verfügbar unter [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). Um den Bau von dort aus zu installieren, gib in einer Terminalsitzung ein:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

Damit bleibt das copr Repositorium aktiv, also


```python
sudo dnf upgrade
```

oder gleichwertig, wird auf den neuesten FreeCAD Bau aktualisiert, zusammen mit Aktualisierungen von jedem der anderen aktiven Repositorien. Wenn du etwas Stabileres willst, kannst du es deaktivieren. \@freecad/nightly erneut nach der Erstinstallation. Die copr Repositorien halten nur Bauten der letzten 2 Wochen. Dies ist keine Lösung, wenn du eine bestimmte ältere Version heraussuchen möchtest.

Anweisungen sind auch auf [Kompiliere FreeCAD selbst](Compile_on_Linux/de.md) einschließlich eines Skripts speziell für Fedora, verfügbar. Mit einer kleinen Änderung, um die spezifische Festlegung von git auszutesten, kann jede Version seit etwa FreeCAD 0.15 auf jeder Distribution seit Fedora 21 aufgebaut werden.


</div>


</div>

## Arch

Installation von FreeCAD auf Arch Linux und Derivaten (z.B. Manjaro):


```python
pacman -S freecad
```

## Andere

Wenn du feststellst, dass dein System FreeCAD unterstützt, aber nicht auf dieser Seite dokumentiert ist, informiere uns bitte im [Forum](http://forum.freecadweb.org/viewforum.php?f=21)!

Viele alternative, nicht-offizielle FreeCAD Pakete sind im Netz verfügbar, z.B. für Systeme wie Slackware oder Fedora. Eine Suche im Netz kann schnell einige Ergebnisse liefern.

### Manuelle Installation auf .deb basierten Systemen 

Wenn aus irgendeinem Grund eine der oben genannten Methoden nicht verwendet werden können, kannst Du immer eines der .deb Pakete herunterladen, die auf der Seite [Download](Download/de.md) verfügbar sind.
{{DownloadUnixStable}}

Wenn du die entsprechende .deb Datei für dein System heruntergeladen und das _ Paket installiert hast (was meistens der Fall ist), navigiere einfach zum Verzeichnis, wo du die Datei heruntergeladen hast und doppelklicke darauf. Die notwendigen Abhängigkeiten werden automatisch von deinem Systempaketmanager erledigt. Alternativ kannst du sie auch vom Terminal aus installieren, indem du zu der Stelle gehst, an der du die Datei heruntergeladen hast, und dann tippst:


```python
sudo dpkg -i Name_of_your_FreeCAD_package.deb
```

Ändern des Name\_of\_your\_FreeCAD\_package.deb durch den Namen der heruntergeladenen Datei.

Nachdem du FreeCAD installiert hast, wird ein Startsymbol im \"Grafik\" Bereich zum Startmenü hinzugefügt.

### Installation auf anderen Linux/Unix Systemen 

Viele gängige Linux Distributionen enthalten nun ein vorkompiliertes FreeCAD als Teil der Standardpakete. Dies ist oft veraltet, aber ein guter Ausgangspunkt. Überprüfe die Standardpaketmanager für Dein System. Eine der folgenden (Teil-) Befehlslisten könnte die offizielle FreeCAD Version aus dem Terminal installieren. Dafür werden wahrscheinlich Administratorrechte benötigt.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
```

Beim Paketnamen ist fallabhängig, also versuche \FreeCAD\ sowie \freecad\. Wenn das nicht funktioniert, entweder weil der Paketmanager keine vorkompilierte FreeCAD-Version zur Verfügung hat, oder weil die verfügbare Version für Deine Zwecke zu alt ist, kann versucht werden, eine der folgenden Dateien herunterzuladen. [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) Veröffentlichungen aus den github Repositorien. Diese funktionieren in der Regel auf den meisten 64 Bit Linux Distributionen, ohne spezielle Installation. Stelle einfach sicher, dass die heruntergeladene Datei als ausführbar markiert ist, und führe sie dann aus.

Wenn das immer noch nicht gut genug ist und keine andere Quelle eines vorkompilierten Pakets für Deine Umstände finden kannst, wirst Du [FreeCAD selbst kompilieren](Compile_on_Linux/de.md) müssen.

### Installation der Windowsversion unter Linux 

Siehe die [Installieren unter Windows](Installing_on_Windows/de.md) Seite.

## Nächster Schritt 

Wenn Du FreeCAD installiert hast, ist es Zeit für die [ersten Schritte](Getting_started/de.md)!







_ _

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Installing on Linux/de
