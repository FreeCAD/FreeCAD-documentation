---
- GuiCommand:/de
   Name/de:Std AbhängigkeitsDiagramm
   MenuLocation:Werkzeuge → AbhängigkeitsDiagramm...
   Workbenches:Alle
---

# Std DependencyGraph/de

## Beschreibung

Der **Std AbhängigkeitsDiagramm** Befehl zeigt die Abhängigkeiten zwischen Objekten im aktiven Dokument in einem \'Abhängigkeitsdiagramm\' an. Im Gegensatz zur [Baumansicht](Tree_view/de.md) werden die Objekte in umgekehrter chronologischer Reihenfolge aufgelistet, wobei das erste erstellte Objekt unten steht.

Es kann bei der Analyse eines FreeCAD Dokuments und beim Auffinden von Verzweigungen in einem Baum nützlich sein. Das Layout des Abhängigkeitsdiagramms hängt davon ab, welcher Arbeitsbereich verwendet wurde, um die Objekte im Dokument zu erstellen. Beispielsweise kann ein Modell, das ausschließlich im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) erstellt wurde, ein lineares Abhängigkeitsdiagramm mit einem einzigen vertikalen Zweig anzeigen. Ein Modell, das mit [Part](Part_Workbench/de.md) Arbeitsgängen erstellt wurde, hat viele Zweige, aber für ein einzelnes Teil schließen sie sich nach [Booleschen](Part_Boolean/de.md) Vorgängen oben an. Wenn dies nicht der Fall ist, bedeutet dies, dass sie separate Objekte sind.

Das Abhängigkeitsdiagramm ist ein reines Visualisierungswerkzeug, daher kann er nicht bearbeitet werden. Er wird automatisch aktualisiert, wenn Änderungen am Modell vorgenommen werden.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> 
*Beispiel eines Abhängigkeitsdiagramms mit einem PartDesign Körper auf der linken Seite und einem mit Teiloperationen erzeugten Objekt auf der rechten Seite*

## Installation

Um den Befehl verwenden zu können, muss eine Drittanbieter Software namens [Graphviz](http://graphviz.org/) installiert sein. Wenn du diese nicht vorinstalliert hast oder sie an einem unkonventionellen Ort installiert ist, zeigt FreeCAD den folgenden Dialog an:

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Lade das **graphviz-2.xx** Installationsprogramm von der [Graphviz Download Seite](https://graphviz.org/download/#windows) herunter und starten es, um es zu installieren. Einige ältere Versionen scheinen Probleme bei der Anzeige des Graphen zu haben; Version 2.38 und neuer sind als zuverlässig bekannt. Du kannst alle Graphviz Versionen auf [Gitlab](https://gitlab.com/graphviz/graphviz/-/releases) finden.

### Mac/OSX

Du kannst graphviz mit [Homebrew](https://brew.sh/) installieren. (Werde bei der Installation von Homebrew nicht nervös, wenn MacOS dich auffordert, Updates zu installieren, z.B. für die Xcode Kommandozeilenprogramme. Diese Updates werden später durch den Installationsprozess durchgeführt). 
```python
brew install graphviz
``` Dadurch werden die Graphviz Binärdateien unter /usr/local/bin installiert. FreeCAD wird dort ganz von selbst suchen. Wenn das Programm dort nicht gefunden wird, wirst du aufgefordert, den Pfad einzugeben. Leider können wir vom Dateidialog aus, der aus **Werkzeuge → Abhängigkeitsdiagramm...** aufgerufen wird, nicht direkt dorthin navigieren. Wenn du den Dateiauswahldialog erhälst, hast du zwei Möglichkeiten: Du kannst die Tastenkombination Cmd+Shift+. verwenden, die dir alle ausgeblendeten Elemente anzeigt. Oder du verwendest die Tastenkombination Cmd+Shift+G, um ein Eingabefeld für den Pfad zu erhalten. Eingabe von 
```python
/usr/local/bin
``` und bestätige das Eingabefeld und den Dateiauswahldialog.

Falls die Graphviz Binärdateien an einem nicht-standardmäßigen Ort installiert sind, versuche, das Programm mit dem Befehl zu finden 
```python
type dot
``` Sie wird etwas ausgeben wie 
```python
dot is /usr/local/bin/dot
``` Und deshalb kannst du FreeCAD anweisen, in diesem Verzeichnis zu suchen.

### Linux

Auf den meisten Linux Distributionen (Debian/Ubuntu, Fedora, OpenSUSE) musst du nur das Paket graphviz aus den Repositorien installieren. Ähnlich wie bei Mac/OSX versuche jedoch, in Fällen, in denen die Graphviz Binärdateien an einem nicht standardmäßigen Ort installiert sind, das Programm mit dem Befehl zu finden: 
```python
type dot
``` Sie wird etwas ausgeben wie 
```python
dot is /usr/local/bin/dot
``` Und deshalb kannst du FreeCAD darauf hinweisen, in diesem Verzeichnis zu suchen.

## Anwendung

1.  Wähle die **Werkzeuge →  <img src="images/Std_DependencyGraph.svg" width=16px> Abhängigkeitsdiagramm...** Option aus dem Menü.
2.  Ein neuer Reiter mit dem Titel **Abhängigkeitsdiagramm** wird im [Hauptansichtsbereich](Main_view_area/de.md) geöffnet.
3.  Verwende zum Vergrößern oder Verkleinern das Scrollrad der Maus.
4.  Verwende die Schieberegler unten und rechts auf dem Bildschirm, um die Ansicht zu verschieben.

Alternativ ({{Version/de|0.19}}) halte die linke Maustaste gedrückt und bewege die Maus.

## Speichern

Du kannst ein Abhängigkeitsdiagramm speichern:

1.  Stelle sicher, dass das Register Abhängigkeitsdiagramm im Vordergrund ist.
2.  Wähle die Option {{MenuCommand/de|Datei → [Speichern](Std_Save/de.md)}} oder {{MenuCommand/de|Datei  → [Speichern als](Std_SaveAs/de.md)}} aus dem Menü.
3.  Gib einen Dateinamen ein und wähle den Dateityp (\*.png, \*.bmp, \*.gif, \*.jpg, \*.svg oder \*.pdf).
4.  Drücke die Taste **Save**.

## Allgemeine Grundsätze 

-   Die Grafik zeigt die Objekte in umgekehrter chronologischer Reihenfolge.
-   Die Richtung der Pfeile, die Abhängigkeiten anzeigen, sollte immer nach unten zeigen, vom untergeordneten Objekt zum übergeordneten Objekt. Ein Pfeil, der nach oben zeigt, weist auf eine zyklische Abhängigkeit hin, ein Problem, das gelöst werden muss.
-   Eine Skizze, die Verknüpfungen zu [externe Geometrie](Sketcher_External/de.md) enthält, hat eine Zahl mit dem Suffix \"x\", neben dem Pfeil, der sie mit seinem Vorläufer verbindet, die die Anzahl der in der Skizze verknüpften externen Geometrien anzeigt.
-   Objekte können Abhängigkeiten zu mehreren Vorläufern haben. Beispielsweise kann bei einem Modell, das in [PartDesign](PartDesign_Workbench/de.md) erstellt wurde, eine Tasche mit ihrer Skizze und mit dem Polster Formelement verknüpft sein, das ihr vorausging.
-   Unzulässige Abhängigkeiten (z.B. zwischen einem [Entwurf](Draft_Workbench/de.md)/[Part](Part_Workbench/de.md) Vorgang und einem Element innerhalb eines PartDesign Körpers) werden mit einem roten Pfeil angezeigt. Diese Verknüpfungstyp zeigt normalerweise einen \'Verknüpfungen gehen außerhalb des zulässigen Bereichs\' Fehler in der [Berichtsansicht](Report_view/de.md) an.
-   Ein [Part Container](Std_Part/de.md) und [PartDesign Körper](PartDesign_Body/de.md) umschließen ihren Inhalt innerhalb eines Rahmens mit einem zufällig gefärbten Hintergrund. Ihr Ursprung umschließt ebenfalls seinen Inhalt (Standardebenen und -achsen) in einem Rahmen.
-   Ein [Gruppen](Std_Group/de.md) wird als ein einzelnes Element angezeigt, das mit seinem Inhalt verknüpft ist.

## Begrenzungen

-   Das Abhängigkeitsdiagramm kann beim [topologischen Benennungsproblem](topological_naming_problem/de.md) nicht helfen. Wenn eine Skizze nach einer Bearbeitung die Flächen eines Formelements wechselt, ist sie immer noch mit dem Formelement verknüpft. Selbst wenn einige Formelemente gebrochen sind, bleibt das Abhängigkeitsdiagramm unverändert.





{{Std Base navi

}}  

[<img src="images/Property.png" style="width:16px"> 3rd Party](Category_3rd_Party.md)

---
[documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > Std DependencyGraph/de
