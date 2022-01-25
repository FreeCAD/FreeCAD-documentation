# Assembly project/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Hier ist der Projektplan für das **Zusammenbau** Modul als Teil des [Entwicklungsfahrplans](Development_roadmap/de.md)

## Zweck und Grundsätze 

Dies ist ein Softwareentwicklungsprojekt das auf die Implementierung von Zusammenbau- und Produkterstellungsfähigkeiten gerichtet ist. Es geht um die Implementierung einiger **Kernfunktionen** in die CAD Module von FreeCAD, **Formteil und Zusammenbau**.

Die Entwicklungsschritte werden hier geplant und im Problemverfolgungssystem verfolgt, um ein gut ausgearbeitetes Änderungsprotokoll zu erhalten: [Problem Verfolger](https://www.freecadweb.org/tracker/)

Du möchtest aktuelle Entwicklungen in [Externe Arbeitsbereichen](External_workbenches/de.md), Abschnitt [Zusammenbau](External_workbenches/de#Zusammenbau.md) herausfinden.

## Ergebnis

Ziel des Projektes ist es, FreeCAD zu befähigen, Gestaltungsaufgaben wie diese umsetzen zu können:

<img alt="" src=images/Gripper.jpg  style="width:400px;">

Dies wird durch die Verwendung des **Zusammenbau Arbeitsbereichs** erreicht, um alle verschiedenen Arten von Teilen mit Beschränkungen zusammenzustellen und so nah wie möglich an der ISO 10303 Spezifikation zu bleiben, um einen einfachen Modellaustausch zu ermöglichen.

Ein weiteres Ziel ist die Verwendung von [Offene Dynamik Maschine](https://de.wikipedia.org/wiki/Open_Dynamics_Engine) für Kinematik.

## Ideenfindung

### Multi-Modell 

<img alt="" src=images/MultiModel.png  style="width:600px;"> Ein wesentliches Merkmal von Entwürfen in der realen Welt ist die Fähigkeit, einen Entwurf in handhabbare Teile zu zerlegen. Es ist unmöglich, an allen Aspekten eines Entwurfs gleichzeitig oder allein zu arbeiten. Das gilt sowohl für die Geometrie als auch für technische Aufgaben wie FEM oder CAM. Deshalb braucht FreeCAD die Möglichkeit, Modelle aufzuteilen. Das eröffnet einige Möglichkeiten:

-   **Spätes Laden** - Benötigt nur Ressourcen wie Grafik und Hauptspeicher für das Teil, an dem du gerade arbeitest.
-   [**simultanes Konstruieren**](http://en.wikipedia.org/wiki/Concurrent_engineering) - erlaubt es mehreren Personen, am selben Entwurf zu arbeiten
-   Feinkörnige [**Versionskontrolle**](http://en.wikipedia.org/wiki/Version_control) - bessere Kontrolle über verschiedene Aspekte des Entwurfs
-   und viele mehr\....

Eine Multi-Modell Konstruktion könnte folgendermaßen aussehen:

### Projektmanagement

Multi-Modell bedeutet, dass viele Dateien zu einem Projekt gehören, wahrscheinlich in einem gemeinsamen Verzeichnis. Eine Projektdatei und ein Projektbrowser können helfen, die Dateien zu organisieren. Sie können auch zusätzliche Informationen über das Projekt oder eine Projekt Webseite speichern.

1\. Zwei Modi, der \"Einfache\" und der \"Projekt\" Modus. Einfach bedeutet nur ein Dokument und alle Baugruppen und Teile werden in einem Dokument gespeichert. Wenn ein Projekt geöffnet oder erstellt wird, befindet sich FreeCAD im Projektmodus.

2\. Projekte. Die Position der FCPrj Datei auf dem Laufwerk definiert ein Stammverzeichnis. Alle Dateien unterhalb dieses Verzeichnisses werden mit relativen Pfaden zum Stammverzeichnis definiert. Eine zusätzliche Ansicht auf der linken Seite enthält den ProjectExplorer, der den Verzeichnisbaum mit den bearbeiteten Dateien anzeigt. Dieses Wurzelverzeichnis wird auch als Wurzel für einen SVN Sandkasten verwendet, die später eine vereinfachte Freigabe und Versionskontrolle ermöglicht. Externe Verweise (auf ein Verzeichnis außerhalb des Stammverzeichnisses, eine Serverfreigabe oder eine Web Ressource) werden im ProjectExplorer separat gehandhabt und angezeigt (ein Pseudo Verzeichnis für jeden Datei oder Webserver). Dadurch ist es möglich, einen schnellen Überblick über externe Referenzen zu erhalten und diese umzuleiten.

### Urheberrecht

Das Urheberrecht für 3D Modelle ist ein interessantes Feld. 3D Modelle fallen unter das Urheberrecht. Das Urheberrecht fällt an den **Schöpfer** des Modells. Es ist nur möglich, die Form, die durch das Modell dargestellt wird, durch ein Patent oder ein Geschmacksmuster (US) zu schützen. Patente beziehen sich jedoch nur auf die Herstellung eines physischen Teils, mit dem Geld verdient werden soll. Ein Beispiel dafür ist das [Microsoft Mouse design patent](http://patft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=D464,651.PN.&OS=PN/D464,651&RS=PN/D464,651).

Wir müssen uns also den Ersteller (Urheberrechte Inhaber) und jede Art von Lizenz für jedes Modell/Produkt/Datei einer Gestaltung merken. Für die Lizenz würde ich die CC Lizenzen verwenden. <http://creativecommons.org/>

Abkürzungsschlüssel für CC Lizenzen:

-   BY = Namensnennung
-   BY-ND = Namensnennung-Keine Bearbeitung
-   BY-NC-ND = Namensnennung - Nicht-kommerziell - Keine Bearbeitung
-   BY-NC = Namensnennung-Nicht kommerziell
-   BY-NC-SA = Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen
-   BY-SA = Namensnennung - Weitergabe unter gleichen Bedingungen
-   PD = Zugeordnet oder gekennzeichnet als im Gemeingut über eines unserer gemeinfreien Werkzeuge, oder andere gemeinfreie Werke; Bearbeitungen von gemeinfreien Werken können darauf aufbauen und vom Urheber unter den gewünschten Lizenzbedingungen lizenziert werden.

Zusätzlich kann ein URL Verweis zum vollständigen Lizenzdokument verwendet werden (im Falle von kundenspezifischen Lizenzen).

### ISO 10303 

Die ISO 10303 (STEP) Norm ist in diesem Feld sehr wichtig. Es ist die einzige gute, genormte, weithin diskutierte und anerkannte Definition von Produktstrukturen, die ich kenne. <img alt="" src=images/Product_structure_modeling_Process-Data_diagram.gif  style="width:500px;">

Hier einige Verweise mit Informationen:

-   [ISO 10303](https://de.wikipedia.org/wiki/Standard_for_the_exchange_of_product_model_data) auf Wikipedia
-   [ISO 10303-11](http://en.wikipedia.org/wiki/ISO_10303-11) über die Modelliersprache (EXPRESS), engl.
-   [Ein Wikipedia-Artikel](http://en.wikipedia.org/wiki/Product_Structure_Modeling) über Produktmodellierung

### Zusammenbau Beschränkungen 

Eine wichtige Rolle beim Aufbau großer Modelle und Produkte spielen die Zusammenbau Beschränkungen, die bestimmte Regeln für den Zusammenbau von Formteilen zu einem Produkt formulieren. Hauptsächlich sind dies Fix, FlächeZuFläche, Winkel, Versatz und eine Art von Musterinstanziierung. Diese Beschränkungen benötigen einen speziellen Löser, um sie aufrechtzuerhalten, wenn sich die Teile ändern. Dieser Löser unterscheidet sich grundlegend von dem Skizzen Löser. Ich denke, wir müssen hier einen diagrammbasierten Ansatz anstreben\...

### Kinematik

Ein weiterer Schritt wäre die Verwendung von [ODE](http://ode.org/) oder ähnlichen Bibliotheken, um die Teile und Zusammenbau Beschränkungen einer kinematischen Maschinensimulation zusammenzufügen. Dies würde die Kollisionsprüfung und ERforschung des Verhaltens mechanischer Systeme ermöglichen.

### Versionskontrolle

Ein wichtiger Punkt ist die Versionskontrolle und die verteilte Entwicklung. Mit Multi-Modell Gestaltung sind wir dazu in der Lage Entwürfe in kleinere Teile aufzuteilen und die Arbeit auf ein Team verteilen. Für einen Softwareentwickler klingt \"verteilt\" und \"Version\" vertraut, warum also nicht ein [Verteilte Versionsverwaltung](https://de.wikipedia.org/wiki/Versionsverwaltung#Verteilte_Versionsverwaltung) (engl. distributed version control system DVCS) verwenden. Ein guter Vergleich ist [Vergleich von Revisionskontrollsoftware hier](http://en.wikipedia.org/wiki/Comparison_of_revision_control_software#Technical_information).

Da wir es mit großen Daten zu tun haben und mit Daten, die sich nicht einfach unterscheiden lassen, sind wir auf Systeme begrenzt, die das Schnappschuss Persistenzmodell verwenden. Jedes System, das nur Unterschiede speichert, wird gravierende Probleme mit unseren Daten haben (persönlich getestet mit Mercurial und Catia Dateien). Nachdem wir kommerzielle und unfreie Systeme aussortiert haben, bleiben im Grunde nur [Git](http://en.wikipedia.org/wiki/Git_%28software%29) und [SVN](http://subversion.apache.org/) übrig.

Die Verwendung von Git für diese Aufgabe bringt uns an zwei große Grenzen:

-   Git ist sehr kompliziert: Verzweigen, Zusammenführen und Markieren entlang eines nicht linearen Entwicklungspfads, ganz zu schweigen vom Zusammenführen mit entfernten Repositorien (push, pull), macht die Sache sehr komplex. Dies vor dem Benutzer zu verbergen wird eine herausfordernde Aufgabe sein.
-   Git erlaubt Merge und Diff Handhaber für bestimmte Dateitypen; wir brauchen einen für .fcstd. Dieser Handhaber muss zwei FreeCAD Dokumente untersuchen und Unterschiede in den Objekten, Merkmalen und Parametern anzeigen und zusammenführen. Auch nicht einfach.

Aber die Verwendung von Git würde eine Menge Möglichkeiten eröffnen, von denen selbst hochklassige PLM Systeme nur träumen können\...

## Organisieren

Hier einige Entwicklungsaufgaben, die für eine gute Zusammenbau/Produktgestaltung erforderlich sind:

### Infrastruktur

Der Zusammenbau erfordert einige Änderungen im Basissystem und der Infrastrukturschicht von FreeCAD.

#### Multi-Modell 

Multi-Modell wurde von Anfang an bei der Entwicklung von FreeCAD berücksichtigt. Deshalb haben wir eine Multi-Dokument Schnittstelle und können unbegrenzt Dokumente laden. Aber wir müssen vor allem den 3D-Betrachter aufrüsten, um mehr als ein Dokument in seiner Ansicht handhaben zu können (Teilbäume).

#### Teilbäume

Da im Zusammenbau die Zusammenstellung von Teilen und Unterbaugruppen der Hauptarbeitsablauf ist, müssen die Werkzeuge zum Stapeln (Gruppieren) von Teilen in einem Baum implementiert werden. Anders als eine DokumentObjektGruppe muss sich die Zusammenbau Gruppe mit der Sichtbarkeit und Platzierung der Kinder beschäftigen. Dies geschieht am besten durch das Stapeln von AnsichtsAnbietern übereinander. Das erfordert eine Art ClaimChildren() Schnittstelle für die AnsichtsAnbieter.

#### Einheitliche Ziehen/Ablegen/Kopieren/Einfügen Schnittstelle 

Eine Schnittstelle ermöglicht AnsichtsAnbieter und Arbeitsbereichen die volle Kontrolle über Ziehen/Ablegen/Kopieren/Einfügen Tätigkeiten im Baum oder in der 3D Ansicht.

#### Externe Ressourcen 

Handhabung von dotierten Verweisen (von internen oder externen Browsern). Bedeutet das Laden von Ressourcen über (potentiell) langsame Verbindungen (http).

### Material

Beschreibung von Materialien und deren Eigenschaften ist grundlegender Bestandteil eines CAD/CAE-Systems. Materialien haben unzählige Eigenschaften und Namensgebungen hängen stark vom Einsatzgebiet ab: FEM und Maschinenbau haben zum Beispiel verschiedene Frameworks und Standards der Materialbeschreibung.

Für die Materialbeschreibung gibt es einen eigenen Artikel: [Material](Material/de.md)

### Objektmodell

Klassenbaum für folgende Konzepte nötig: Referenzen, Interfaces, Dokumentenlinks, Ansichten, Objektgruppen, Randbedingungen, Konfigurationen u.v.m.

## STEP Prüfschleife 

Implementierung eines ersten STEP Importeurs für mehr als Geometrie und Farbe, um zu prüfen, ob das Objektmodell für eine breitere Verwendung geeignet ist.

### Zusammenbau Beschränkungslöser 

Definiere eine Schnittstelle zu einem Zusammenbau Beschränkungslöser, sehr ähnlich der Skizzierer Löser Schnittstelle.

### Physiksimulations Schnittstelle 

Schnittstelle, die es (externer) (Multi)Physiksimulationssoftware ermöglicht, die Kontrolle über die Positionierung der Teile einer Baugruppe zu übernehmen. Dies würde die Verwendung von \"Bullet\" oder \"ODE\" zur Durchführung kinematischer Tests und DMU ermöglichen.

## Nächste Aktionen 

-   Objektmodell
-   \...



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Assembly project/de
