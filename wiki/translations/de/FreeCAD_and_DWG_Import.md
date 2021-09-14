# FreeCAD and DWG Import/de

 {{TOCright}}


{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}

## Warum ist es schwierig, DWG Dateien in FreeCAD zu unterstützen? 

Das **DWG Format ist ein binäres Dateiformat mit geschlossenem Quellcode**, das von FreeCAD nicht direkt unterstützt wird. Es erfordert einen externen Dateikonvertierer eines Drittanbieters, der zuerst konvertiert und dann die Konvertierung zur Verwendung in FreeCAD importiert.

Beachte, dass es zur Zeit nicht möglich ist, 3D DWG in FreeCAD zu importieren. 3D Daten sind als binäre .SAT (ACIS) Daten, ein proprietäres und undokumentiertes Format, eingebettet.

## Was benötige ich, um DWG Dateien importieren zu können? 

### ODA Konverter (früher Teigha Konverter) 

-   Homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   Lizenz: Freeware
-   Optional, wird für den Im- und Export von DWG Dateien verwendet

Der ODA Konverter ist ein kleines, frei verfügbares Dienstprogramm, das die Konvertierung zwischen verschiedenen Versionen von DWG und DXF Dateien erlaubt. FreeCAD kann es verwenden, um DWG Import und Export anzubieten, indem DWG Dateien unter der Haube in das DXF Format konvertiert werden und der Dateiinhalt dann mit seinem Standard DXF Importeur importiert wird. Es gelten die Einschränkungen des [DXF Importeurs](Draft_DXF/de.md).

#### Einrichtung

Auf allen Plattformen nur durch Installation des geeigneten Pakets von <https://www.opendesign.com/guestfiles/oda_file_converter>. Wenn das Dienstprogramm nach der Installation nicht automatisch von FreeCAD gefunden wird, musst du den Pfad zur ausführbaren Datei des Konverters eventuell manuell einstellen. Öffne Bearbeiten → Einstellungen → Import-Export → DWG und fülle \"Pfad zum Teigha Dateikonverter\" in geeigneter Weise aus.

Für eine ausführlichere Anleitung siehe \[<https://wiki.freecadweb.org/Dxf_Importer_Install/de#Dritter_Schritt>: dieses Tutoriums\].

#### Anwendung

Das Programm kann mit der Befehlszeilenschnittstelle oder der grafischen Oberfläche verwendet werden. Achte darauf, die DWG Dateien in ein ASCII-Format zu konvertieren.

Befehlszeilenformat ist:

1.  Angegebener Eingabeordner
2.  Angegebener Ausgabeordner
3.  Ausgabe\_Version {\"ACAD9\", \"ACAD10\", \"ACAD12\", \"ACAD13\", \"ACAD14\", \"ACAD2000\", \"ACAD2004\", \"ACAD2007\", \"ACAD2010\"}
4.  Ausgabe Dateityp {\"DWG\", \"DXF\", \"DXB\"}
5.  Eingabeordner miteinbeziehen {\"0\", \"1\"}
6.  Jede Datei prüfen {\"0\", \"1\"}
7.  \[optional\] Eingabedateifilter (Standard: \"\*.DWG;\*.DXF\")

**Beispiel unter Linux**
ODAFileConverter \"/home/dwg-data\" \"/home/dxf-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" Die zweite Nummer (Audit) muss 1 sein, andernfalls schlägt sie fehl

**Beispiel unter Windows**
\"C:\\Program Files\\ODA\\Teigha File Converter 3.08.2\\TeighaFileConverter.exe\" \"Path-To-Input-Directory\" \"Path-To-Output-Directory\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Name-Of-A-Test-File.dwg\"

### CADExchanger Arbeitsbereich 

Die Installation des CADExchanger Arbeitsbereichs ermöglicht das Arbeiten mit DWG Dateien durch Integration mit dem kostenpflichtigen kommerziellen Dateikonverterprodukt [CADExchanger](https://cadexchanger.com/). Folge einfach den Anweisungen im [GitHub Repositorium](https://github.com/yorikvanhavre/CADExchanger). Du kannst über diesen Arbeitsbereich im [sein Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421) diskutieren.

Im Moment ist der CADExchanger Weg der einzige, der es erlaubt, mit 3D DWG-Dateien zu arbeiten, indem er sie in andere 3D Formate konvertiert.

## FreeCAD v0.19 und LibreDWG 

Ab 0.19 benötigt FreeCAD den ODA Konverter nicht mehr und kann libreDWG direkt verwenden. Sei dir bewusst, dass, da libreDWG ein \"unfertiges Erzeugnis\" ist, die Ergebnisse je nach Datei möglicherweise nicht die gleichen sind.

-   Homepage: <https://www.gnu.org/software/libredwg/>
-   Licenz: GPLv2-or-later
-   Optional, verwendet, um den Import und Export von DWG Dateien zu aktivieren

GNU LibreDWG ist eine freie C Bibliothek zur Verarbeitung von DWG Dateien. Sie zielt darauf ab, ein freier Ersatz für die Open Design Alliance Drawings SDK Bibliotheken zu sein.

## Einrichtung 

### AppImage Ausgaben 

LibreDWG ist in v 0.19\_pre appimages[1](https://forum.freecadweb.org/viewtopic.php?f=8&t=39827&start=20#p372933) enthalten.

### Windows

LibreDWG kann für die Arbeit unter Windows konfiguriert werden, indem du das entsprechende [vorkompilierte Windows Binärdatei](https://github.com/LibreDWG/libredwg/releases) herunterladen und entpacken und [Hinzufügen des Ordners zum Systempfad deiner Windows Versionen](https://duckduckgo.com/?t=ffab&q=how+to+add+a+folder+to+your+windows+system+path).

### Linux/Unix Systeme 

git clone <https://git.savannah.gnu.org/git/libredwg.git> cd libredwg mkdir build cd build cmake .. make make install (oder verwende checkinstall, oder suche und kopiere einfach das dwg2dxf Hilfsprogramm in den Pfad deiner ausführbaren Dateien, es wird dann automatisch von FreeCAD erkannt)

### openSUSE

Um Probleme bei der Programmausführung zu vermeiden, musst du das LibreDWG Paket verwenden, das für die installierte openSUSE OS Distribution kompiliert wurde. LibreDWG wird normalerweise mit **YAST** installiert (Abk. Yet another Setup Tool) dem Einrichtungs- und Konfigurationswerkzeug des Linux Betriebssystems, installiert.

Der erfahrenere Benutzer erhält zunächst einen Überblick über mögliche bereitgestellte Pakete. **Hinweis:** openSUSE bietet beim Herunterladen von LibreDWG mehrere Optionen zur Auswahl an. Um diese Optionen zu sehen, besuchst du [Übersicht der bereitgestellten LibreDWG Pakete unter openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

Für z. B. Intel oder AMD 64-Bit Desktops, Laptops und Server ist die (x86\_64) Version die richtige Wahl. Daher sind **libredwg0** und **libredwg-tools** die richtige Wahl zur Installation.

Es wird empfohlen, die Binärpakete direkt zu holen. Wähle dann die richtige Distribution für dein installiertes openSUSE Betriebssystem.

In einem beliebigen Terminal/Konsole (root Rechte erforderlich) wird die Installation durchgeführt mit:

:   
    
```python
    zypper install libredwg0 libredwg-tools
    
```
    

Danach sollte jeder \*.dwg Dateiimport korrekt funktionieren.

## Was sind die Alternativen? 

### DoubleCAD XT 

Es gibt auch DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). Das Programm ist für die persönliche und kommerzielle Nutzung kostenlos. Es erfordert eine kostenlose Anmeldung, um einen Aktivierungscode per E-Mail zu bekommen. Dieses Programm ist nur für Windows. Hinweis: Es scheint seit Jahren nicht mehr aktualisiert worden zu sein.

### NanoCAD 5.0 

Es gibt auch nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). Das Programm ist für die private und kommerzielle Nutzung kostenlos. Es erfordert eine kostenlose Anmeldung, um einen Aktivierungscode per E-Mail zu erhalten. Dieses Programm ist nur für Windows.

### Exportiere Deine AutoCAD Dateien in freundliches Format 

Exportiere deine AutoCAD Dateien in ein FreeCAD freundlicheres Format, wie DXF R12 oder R14, SVG und, falls die Version dies unterstützt, IGES. Alle sind bessere Alternativen zum DWG Format, wenn du FreeCAD verwendest.

Es ist wichtig zu wissen, dass es entgegen der landläufigen Meinung keinen Unterschied zwischen dem Inhalt einer Datei gibt, die im DWG oder DXF Format gespeichert ist, sofern es sich um die gleiche Version handelt (z. B. DWG 2014 vs. DXF 2014). Beide Formate werden von Autodesk verwaltet, und beide unterstützen genau dieselben Funktionen. Der Unterschied besteht darin, dass DWG geschlossen (maschinenkodiert) ist, während DXF offen ist.

## Was kann ich tun, um zu helfen? 

### Fördere die Verwendung alternativer Formate 

Einfach genommen, höre auf, im DWG Format geleistete Arbeit zu akzeptieren. In der Praxis ist dies oft leichter gesagt als getan. Dennoch wäre es keine schlechte Praxis für Benutzer und Unterstützer von FreeCAD, das DWG Format zu vermeiden und abzulehnen, wann immer es möglich ist.

### Benutze die LibreDWG Bibliothek und schreibe Fehlerberichte 

In der Entwicklungsversion kannst du, wie oben erwähnt, vom proprietären ODA Konverter auf die freie Software Bibliothek LibreDWG für DWG (und DXF) Dateien umsteigen. Bitte tue dies und melde etwaige Probleme, die dabei auftreten.


 

[Category:File\_Formats](Category:File_Formats.md) [Category:Common Questions](Category:Common_Questions.md)
