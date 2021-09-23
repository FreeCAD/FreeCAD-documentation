# Doxygen/de
## Über


{{TOCright}}

Doxygen ist ein beliebtes Werkzeug zur Generierung von Dokumentation aus kommentierten C++ Quellen; es unterstützt auch andere gängige Programmiersprachen wie C\#, PHP, Java und Python. Besuche die [Doxygen Website](http://www.doxygen.nl/), um mehr über das System zu erfahren, und konsultiere das [Doxygen Handbuch](http://www.doxygen.nl/manual/index.html) für die vollständigen Informationen.

## Doxygen und FreeCAD 

Dieses Dokument gibt eine kurze Einführung in Doxygen, insbesondere wie es in FreeCAD zur Dokumentation seiner Quellen verwendet wird. Auf der Seite [Quelldokumentation](source_documentation/de.md) findest Du Anweisungen zum Erstellen der FreeCAD Dokumentation, die ebenfalls online auf der [FreeCAD API Website](https://www.freecadweb.org/api/) bereitgestellt wird.

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">


*Allgemeiner Arbeitsablauf zur Erstellung von Quellcode Dokumentation mit Doxygen.*

## Doxygen mit C++ Code 

Der Abschnitt [Getting started (Step 3)](http://www.doxygen.nl/manual/starting.html) im Doxygen Handbuch erwähnt die grundlegenden Möglichkeiten der Dokumentation der Quellen.

Für Mitglieder, Klassen und Namensräume gibt es grundsätzlich zwei Möglichkeiten:

1.  Platziere einen speziellen \"Dokumentationsblock\" (einen kommentierten Absatz) vor der Deklaration oder Definition der Funktion, des Elements, der Klasse oder des Namensraums. Bei Datei-, Klassen- und Namensraumelementen (Variablen) ist es auch erlaubt, die Dokumentation direkt nach dem Element zu platzieren. Siehe Abschnitt [Spezielle Kommentarblöcke](http://www.doxygen.nl/manual/docblocks.html#specialblock) im Handbuch, um mehr über diese Blöcke zu erfahren.
2.  Platziere einen speziellen Dokumentationsblock an einer anderen Stelle (eine andere Datei oder einen anderen Ort in der gleichen Datei) und füge einen \"Strukturbefehl\" in den Dokumentationsblock ein. Ein Strukturbefehl verknüpft einen Dokumentationsblock mit einer bestimmten zu dokumentierenden Einheit (Funktion, Element, Variable, Klasse, Namensraum oder Datei). Siehe Abschnitt [Dokumentation an anderer Stelle](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) im Handbuch, um mehr über Strukturbefehle zu erfahren.

Hinweis:

-   Der Vorteil der ersten Option ist, dass du den Namen der Einheit (Funktion, Element, Variable, Klasse oder Namensraum) nicht wiederholen musst, da Doxygen den Code analysiert und die relevanten Informationen extrahiert.
-   Dateien können nur mit der zweiten Option dokumentiert werden, da es keine Möglichkeit gibt, einen Dokumentationsblock vor eine Datei zu stellen. Natürlich benötigen Dateimitglieder (Funktionen, Variablen, Typedefinitionen, Definitionen) keinen expliziten Strukturbefehl; einfach einen Dokumentationsblock vor oder nach ihnen zu setzen, wird gut funktionieren.

### Erster Stil: Dokumentationsblock vor dem Kode 

Normalerweise möchtest du den Code in der Kopfzeilendatei dokumentieren, kurz vor der Klassendeklaration oder dem Funktionsprototyp. Dadurch bleiben Deklaration und Dokumentation dicht beieinander, so dass es einfach ist, letztere zu aktualisieren, wenn sich die erste ändert.

Der spezielle Dokumentationsblock beginnt wie ein Kommentar im C-Stil `/*`, hat aber ein zusätzliches Sternchen, also `/**`; der Block endet mit einem passenden `*/`. Eine Alternative ist die Verwendung von Kommentaren im C++-Stil `//` mit einem zusätzlichen Schrägstrich, also `////`. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```

### Zweiter Stil: Dokumentationsblock an anderer Stelle 

Alternativ kann die Dokumentation auch in einer anderen Datei (oder in derselben Datei oben, unten oder wo auch immer) abgelegt werden, weg von der Klassendeklaration oder dem Funktionsprototyp. In diesem Fall hast du duplizierte Informationen, einmal in der eigentlichen Quelldatei und einmal in der Dokumentationsdatei.

Erste Datei, `source.h`: 
```python
std::string name() const;
void setName(const std::string&);
```

Zweite Datei, `source.h.dox`: 
```python
/** \file source.h
 *  \brief The documentation of source.h
 *   
 *   The details of this file go here.
 */

/** \fn std::string name() const;
 *  \brief Returns the name of the workbench object.
 */
/** \fn void setName(const std::string&);
 *  \brief Set the name to the workbench object.
 */
```

In diesem Fall wird der Strukturbefehl `\file` verwendet, um anzugeben, welche Quelldatei dokumentiert wird; ein Strukturbefehl `\fn` zeigt an, dass der folgende Code eine Funktion ist, und der Befehl `\brief` wird verwendet, um eine kleine Beschreibung dieser Funktion zu geben.

Diese Art der Dokumentation einer Quelldatei ist nützlich, wenn du nur Dokumentation zu deinem Projekt hinzufügen möchtest, ohne echten Code hinzuzufügen. Wenn du einen Kommentar-Block in eine Datei mit einer der folgenden Erweiterungen `.dox`, `.txt`, `.txt` oder `.doc` platzierst, dann wird Doxygen die Kommentare analysieren und die entsprechende Dokumentation erstellen, aber es wird diese Hilfsdatei aus der Dateiliste ausblenden.

Das FreeCAD Projekt fügt in vielen Verzeichnissen mehrere Dateien mit der Endung `.dox` hinzu, um eine Beschreibung oder Beispiele für den dortigen Code zu liefern. Es ist wichtig, dass solche Dateien korrekt in einer Gruppe oder einem Namensraum kategorisiert werden, für die Doxygen einige Hilfsbefehle wie `\defgroup`, `\ingroup`, `\ingroup`, und `\namespace` bereitstellt.


<div class="mw-collapsible mw-collapsed toccolours">

Beispiel `src/Base/core-base.dox`; diese Datei im FreeCAD Quellbaum gibt eine kurze Erklärung des Namensraums `Base`.


<div class="mw-collapsible-content">


```python
/** \defgroup BASE Base
 *  \ingroup CORE
    \brief Basic structures used by other FreeCAD componentsThe Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units

*/

/*! \namespace Base
    \ingroup BASE
    \brief Basic structures used by other FreeCAD components

    The Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units
*/
```


</div>


</div>

Ein weiteres Beispiel ist die Datei `src/Gui/Command.cpp`. Vor den Implementierungsdetails der Methoden `Gui::Command` gibt es einen Dokumentationsblock, der einige Details des Befehlsrahmens von FreeCAD erklärt. Es verfügt über verschiedene `\section` Befehle, um die Dokumentation zu strukturieren. Es beinhaltet sogar Beispielcode, der in einem Paar von `\code` und `\endcode` Schlüsselwörtern eingeschlossen ist; wenn die Datei von Doxygen verarbeitet wird, wird dieses Code-Beispiel speziell formatiert, um sich abzuheben. Das Schlüsselwort `\ref` wird an mehreren Stellen verwendet, um Links zu benannten Abschnitten, Unterabschnitten, Seiten oder Ankern an anderer Stelle in der Dokumentation zu erstellen. Ebenso drucken die Befehle `\see` oder `\sa` \"Siehe auch\" und stellen einen Link zu anderen Klassen, Funktionen, Methoden, Variablen, Dateien oder URLs dar.


<div class="mw-kollabierbare mw-kollabierte toccolours">

Beispiel `src/Gui/Command.cpp`


<div class="mw-collapsible-content">


```python
/** \defgroup commands Command Framework
    \ingroup GUI
    \brief Structure for registering commands to the FreeCAD system
 * \section Overview
 * In GUI applications many commands can be invoked via a menu item, a toolbar button or an accelerator key. The answer of Qt to master this
 * challenge is the class \a QAction. A QAction object can be added to a popup menu or a toolbar and keep the state of the menu item and
 * the toolbar button synchronized.
 *
 * For example, if the user clicks the menu item of a toggle action then the toolbar button gets also pressed
 * and vice versa. For more details refer to your Qt documentation.
 *
 * \section Drawbacks
 * Since QAction inherits QObject and emits the \a triggered() signal or \a toggled() signal for toggle actions it is very convenient to connect
 * these signals e.g. with slots of your MainWindow class. But this means that for every action an appropriate slot of MainWindow is necessary
 * and leads to an inflated MainWindow class. Furthermore, it's simply impossible to provide plugins that may also need special slots -- without
 * changing the MainWindow class.
 *
 * \section wayout Way out
 * To solve these problems we have introduced the command framework to decouple QAction and MainWindow. The base classes of the framework are
 * \a Gui::CommandBase and \a Gui::Action that represent the link between Qt's QAction world and the FreeCAD's command world. 
 *
 * The Action class holds a pointer to QAction and CommandBase and acts as a mediator and -- to save memory -- that gets created 
 * (@ref Gui::CommandBase::createAction()) not before it is added (@ref Gui::Command::addTo()) to a menu or toolbar.
 *
 * Now, the implementation of the slots of MainWindow can be done in the method \a activated() of subclasses of Command instead.
 *
 * For example, the implementation of the "Open file" command can be done as follows.
 * \code
 * class OpenCommand : public Command
 * {
 * public:
 *   OpenCommand() : Command("Std_Open")
 *   {
 *     // set up menu text, status tip, ...
 *     sMenuText     = "&Open";
 *     sToolTipText  = "Open a file";
 *     sWhatsThis    = "Open a file";
 *     sStatusTip    = "Open a file";
 *     sPixmap       = "Open"; // name of a registered pixmap
 *     sAccel        = "Shift+P"; // or "P" or "P, L" or "Ctrl+X, Ctrl+C" for a sequence
 *   }
 * protected:
 *   void activated(int)
 *   {
 *     QString filter ... // make a filter of all supported file formats
 *     QStringList FileList = QFileDialog::getOpenFileNames( filter,QString::null, getMainWindow() );
 *     for ( QStringList::Iterator it = FileList.begin(); it != FileList.end(); ++it ) {
 *       getGuiApplication()->open((*it).latin1());
 *     }
 *   }
 * };
 * \endcode
 * An instance of \a OpenCommand must be created and added to the \ref Gui::CommandManager to make the class known to FreeCAD.
 * To see how menus and toolbars can be built go to the @ref workbench.
 *
 * @see Gui::Command, Gui::CommandManager
 */
```


</div>


</div>

### Beispiel aus dem VTK Projekt 

Dies ist ein Beispiel aus [VTK](https://vtk.org/), einer 3D Visualisierungsbibliothek, die zur Darstellung wissenschaftlicher Daten wie Finite Elemente Ergebnisse und Punktwolkeninformationen verwendet wird.

Eine Klasse zum Speichern einer Sammlung von Koordinaten wird in einer C++ Kopfzeilendatei definiert. Der obere Teil der Datei wird kommentiert, und es werden einige Schlüsselwörter verwendet, wie `@class`, `@brief`, und `@sa`, um wichtige Teile zu kennzeichnen. Innerhalb der Klasse, vor den Prototypen der Klassenmethode, erklärt ein Block aus kommentiertem Text, was die Funktion tut und welche Argumente sie hat.

-   Quellcode von [vtkArrayCoordinates.h](https://github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Doxygen hat die Dokumentation für die [vtkArrayCoordinates class](http://www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html) erstellt.

### Zusammenstellung der Dokumentation 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">


*Allgemeiner Arbeitsablauf zur Erstellung von Quellcode Dokumentation mit Doxygen.*

Um die Quellcode Dokumentation zu erstellen, gibt es zwei grundlegende Schritte:

1.  Erstelle eine Konfigurationsdatei, um zu steuern, wie Doxygen die Quelldateien verarbeiten soll.
2.  Führe `doxygen` in dieser Konfiguration aus.


<div class="mw-collapsible mw-collapsed toccolours">

Der Prozess wird im Folgenden beschrieben.


<div class="mw-collapsible-content">

-   Stelle sicher, dass die Programme `doxygen` und `doxywizard` in Deinem System vorhanden sind. Es wird auch empfohlen, das Programm `dot` von [Graphviz](https://www.graphviz.org/) zu verwenden, um Diagramme mit den Beziehungen zwischen Klassen und Namensräumen zu erzeugen. Auf Linux Systemen können diese Programme über Ihren Paketmanager installiert werden.


```python
sudo apt install doxygen doxygen-gui graphviz
```

-   Stelle sicher, dass Du Dich im gleichen Ordner wie Deine Quelldateien befindest, oder im Toplevel Verzeichnis Deines Quellbaums, wenn Du viele Quelldateien in verschiedenen Unterverzeichnissen hast.


```python
cd toplevel-source
```

-   Führe `doxygen -g DoxyDoc.cfg` aus, um eine Konfigurationsdatei namens `DoxyDoc.cfg` zu erstellen. Wenn Du diesen Namen weglässt, wird er standardmäßig auf `Doxyfile` ohne Erweiterung gesetzt.
-   Dies ist eine große, einfache Textdatei, die viele Variablen mit ihren Werten enthält. Im Doxygen Handbuch werden diese Variablen als \"Tags\" bezeichnet. Die Konfigurationsdatei und alle Tags sind im Abschnitt [Konfiguration](http://www.doxygen.nl/manual/config.html) des Handbuchs ausführlich beschrieben. Du kannst die Datei mit einem beliebigen Texteditor öffnen und den Wert jedes Tags nach Bedarf bearbeiten. In der gleichen Datei kannst du Kommentare lesen, die jedes der Tags und seine Standardwerte erklären.


```python
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = "My Project"
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       =
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = NO
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
...
```

-   Anstatt einen Texteditor zu verwenden, kannst du `doxywizard` starten, um viele Tags gleichzeitig zu bearbeiten. Mit dieser Schnittstelle kannst du viele Eigenschaften definieren, wie z.B. Projektinformationen, Art der Ausgabe (HTML und LaTeX), Verwendung von Graphviz zur Erstellung von Diagrammen, Warnmeldungen zur Anzeige, Dateimuster (Erweiterungen) zum Dokumentieren oder Ausschließen, Eingabefilter, optionale Kopf- und Fußzeilen für die von HTML generierten Seiten, Optionen für LaTeX-, RTF-, XML- oder Docbook-Ausgaben und viele andere Optionen.


```python
doxywizard DoxyDoc.cfg
```

-   Eine weitere Möglichkeit besteht darin, die Konfigurationsdatei von Grund auf neu zu erstellen und nur die Tags hinzuzufügen, die du mit einem Texteditor willst.
-   Nachdem die Konfiguration gespeichert wurde, kannst du Doxygen auf dieser Konfigurationsdatei ausführen.


```python
doxygen DoxyDoc.cfg
```

-   Die erzeugte Dokumentation wird in einem Ordner namens `toplevel-source/html` erstellt. Es wird aus vielen HTML Seiten, PNG Bildern für Grafiken, Cascading Style Sheets (`.css`), Javascript Dateien (`.js`) und möglicherweise vielen Unterverzeichnissen mit mehr Dateien je nach Größe Ihres Codes bestehen. Der Einstiegspunkt in die Dokumentation ist `index.html`, den du mit einem Webbrowser öffnen kannst.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

Wenn du neue Klassen, Funktionen oder eine ganze neue Arbeitsbereiche schreibst, wird empfohlen, `doxygen` regelmäßig auszuführen, um sicherzustellen, dass die Dokumentationsblöcke [Markdown](#Markdown_support.md) und [Spezielle Befehle](#Doxygen_markup/de.md) korrekt gelesen werden und dass alle öffentlichen Funktionen vollständig dokumentiert sind. Bitte lies auch die [Dokumentationshinweise](https://github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) im Quellcode.

Bei der Generierung der kompletten FreeCAD Dokumentation führe `doxygen` nicht direkt aus. Stattdessen verwende das Projekt `cmake`, um die Build Umgebung zu konfigurieren, und löst dann `make` die Kompilierung der FreeCAD Quellen und der Doxygen Dokumentation aus; dies wird auf der Seite [Quell Dokumentation](source_documentation/de.md) erläutert.

## Doxygen Auszeichnung 

Alle Doxygen [Befehlsdokumentation](http://www.doxygen.nl/manual/commands.html) beginnt mit einem Backslash `\\` oder einem at Symbol `@`, je nach Wunsch. Normalerweise wird der Backslash `\\` verwendet, aber gelegentlich wird der `@` verwendet, um die Lesbarkeit zu verbessern.

Die Befehle können ein oder mehrere Argumente haben. Im Doxygen Handbuch werden die Argumente wie folgt beschrieben.

-   Wenn `<sharp>` Klammern verwendet werden, ist das Argument ein einzelnes Wort.
-   Wenn `(round)` Klammern verwendet werden, erstreckt sich das Argument bis zum Ende der Zeile, in der der Befehl gefunden wurde.
-   Wenn {curly} Klammern verwendet werden, verlängert sich das Argument bis zum nächsten Absatz. Absätze werden durch eine Leerzeile oder durch ein Abschnittskennzeichen begrenzt.
-   Wenn `[square]` Klammern verwendet werden, ist das Argument optional.


<div class="mw-collapsible mw-collapsed toccolours">

Einige der häufigsten Schlüsselwörter, die in der FreeCAD Dokumentation verwendet werden, sind hier aufgeführt.


<div class="mw-collapsible-content">

-    (Gruppentitel), siehe [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), und[Gruppierung](http://www.doxygen.nl/manual/grouping.html).
-   ]), siehe[\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), und[Gruppierung](http://www.doxygen.nl/manual/grouping.html).

 [(title)], siehe [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), und[Gruppierung](http://www.doxygen.nl/manual/grouping.html).

-   \author { list of authors }, siehe [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); gibt den Autor dieses Stückes Code an.
-   \brief {kurze Beschreibung }, siehe [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); beschreibt kurz die Funktion.
-   ], siehe [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); dokumentiert eine Quell- oder Header-Datei.
-    (title), siehe [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); stellt die Informationen auf eine separate Seite, nicht direkt in Bezug stehend mit einer bestimmten Klasse, Datei oder einem Mitglied.
-   , siehe[\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); zeigt die Dokumentation für ein Java Paket an (wird aber auch mit Python verwendet).
-   \fn (Funktionsdeklaration), siehe [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); dokumentiert eine Funktion.
-   \var (Variablendeklaration), siehe [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); dokumentiert eine Variable; sie entspricht `\fn`, `\property`, und `\typedef`.
-    (section title), siehe[\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); startet einen Abschnitt.

 (subection title), siehe[\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); startet einen Unterabschnitt.

-   , siehe[\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); zeigt Informationen für einen Namensraum an.
-   \cond [(section-label)], und \endcond, siehe[\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); definiert einen Block, der bedingt dokumentiert oder weggelassen werden soll.
-   , siehe[\\a](http://www.doxygen.nl/manual/commands.html#cmda); zeigt das Argument kursiv zur Hervorhebung an.
-    { parameter description }, siehe[\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); gibt den Parameter einer Funktion an.

\return { Beschreibung des Rückgabewertes }, siehe[\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); gibt den Rückgabewert an.

-   \sa { Referenzen }, siehe [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); druckt \"Siehe auch\".
-   \note { text }, siehe[\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); fügt einen Absatz hinzu, der als Notiz verwendet werden soll.


</div>


</div>

## Markdown Unterstützung 

Seit Doxygen 1.8 wird die Markdown Syntax in Dokumentationsblöcken erkannt. Markdown ist eine minimalistische Formatierungssprache, die von einfachen Text Emails inspiriert ist, die, ähnlich wie die Wiki Syntax, einfach und lesbar sein soll, ohne komplizierten Code wie den in HTML, LaTeX oder Doxygens eigenen Befehlen zu benötigen. Markdown hat bei freier Software an Popularität gewonnen, insbesondere in Online Plattformen wie Github, da es die Erstellung von Dokumentation ohne komplizierten Code ermöglicht. Weitere Informationen finden sich im Abschnitt [Markdown Support](http://www.doxygen.nl/manual/markdown.html) im Doxygen Handbuch. Besuche die [Markdown Webseite](https://daringfireball.net/projects/markdown/), um mehr über den Ursprung und die Philosophie von Markdown zu erfahren.

Doxygen unterstützt einen Standardsatz von Markdown Anweisungen sowie einige Erweiterungen wie z.B. [Github Markdown](https://github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

Im Folgenden werden einige Beispiele für die Formatierung von Markdown vorgestellt.


<div class="mw-collapsible-content">

Das Folgende ist Standard Markdown. 
```python
Hier ist der Text für einen Absatz.

Wir machen mit mehr Text in einem anderen Absatz weiter.

Dies ist eine Level 1 Kopfzeile
========================

Dies ist eine Level 2 Kopfzeile.
------------------------

# Dies ist ein Level 1 Kopfteil

### Dies ist ein Level 3 Kopfteil #######

> Dies ist ein Blockzitat
> über mehrere Linien hinweg

- Punkt 1

  Mehr Text für dieses Element.

- Punkt 2
  * Verschachtelte Listenelemente.
  * ein weiteres verschachteltes Element.
- Punkt 3

1. Erstes Element.
2. Zweites Element.

*einzelne Sternchen: Hervorhebung*

 _single underscores_

 **double asterisks: strong emphasis**

 __double underscores__

Dies ist ein normaler Abschnitt

    Dies ist ein Codeblock

Wir fahren mit einem normalen Absatz fort.

Use the printf() function. Inline code.

[The link text](http://example.net/)

![Caption text](images//path/to/img.jpg)

<http://www.example.com>
```

Die folgenden sind Markdown Erweiterungen.

    [TOC]

    Erste Kopfzeile  | Zweite Kopfzeile
    ------------- | -------------
    Zellinhalt  | Zellinhalt
    Zellinhalt  | Zellinhalt 

    <nowiki>~~~~~~~~~~~~~</nowiki>{.py}
    # Eine Klasse
    class Dummy:
        pass
    <nowiki>~~~~~~~~~~~~~</nowiki>

    <nowiki>~~~~~~~~~~~~~</nowiki>{.c}
    int func(int a, int b) { return a*b; }
    <nowiki>~~~~~~~~~~~~~</nowiki>
int func(int a, int b) { return a*b; }
    


</div>


</div>

## Zerteilen von Dokumentationsblöcken 

Der Text in einem speziellen Dokumentationsblock wird analysiert, bevor er in die HTML- und LaTeX Ausgabedateien geschrieben wird. Beim Zertilen (engl.: Parsen) finden die folgenden Schritte statt:

-   Die Markdown Formatierung wird durch entsprechendes HTML oder spezielle Befehle ersetzt.
-   Die speziellen Befehle innerhalb der Dokumentation werden ausgeführt. Siehe Abschnitt [Spezielle Befehle](http://www.doxygen.nl/manual/commands.html) im Handbuch für eine Erklärung der einzelnen Befehle.
-   Wenn eine Zeile mit einem Leerzeichen beginnt, gefolgt von einem oder mehreren Sternchen (`*`) und dann optional mehr Leerzeichen, dann werden alle Leerzeichen und Sternchen entfernt.
-   Alle resultierenden Leerzeilen werden als Absatztrennzeichen behandelt.
-   Links werden automatisch für Wörter erstellt, die den dokumentierten Klassen oder Funktionen entsprechen. Wenn dem Wort ein Prozentsymbol `%` vorangestellt ist, wird dieses Symbol entfernt und es wird keine Verknüpfung für das Wort erstellt.
-   Links werden erstellt, wenn bestimmte Muster im Text gefunden werden. Weitere Informationen finden Sie im Abschnitt [Automatische Linkerzeugung](http://www.doxygen.nl/manual/autolink.html) im Handbuch.
-   HTML-Tags, die sich in der Dokumentation befinden, werden interpretiert und für die LaTeX Ausgabe in LaTeX Äquivalente umgewandelt. Siehe den Abschnitt [HTML-Befehle](http://www.doxygen.nl/manual/htmlcmds.html) im Handbuch für eine Erklärung der einzelnen unterstützten HTML-Tags.

## Doxygen mit Python Code 

Doxygen funktioniert am besten für statisch typisierte Sprachen wie C++. Es kann aber auch eine [Dokumentation für Python-Dateien](http://www.doxygen.nl/manual/docblocks.html#pythonblocks) erstellen.

Es gibt zwei Möglichkeiten, Dokumentationsblöcke für Python zu schreiben:

1.  Der pythonische Weg, mit \"docstrings\", d.h. ein Textblock, der von '''triple quotes''' unmittelbar nach der Klassen- oder Funktionsdefinition umgeben ist.
2.  Der Doxygen Weg, bei dem Kommentare vor die Klassen- oder Funktionsdefinition gestellt werden; in diesem Fall werden doppelte Hash-Zeichen `###` verwendet, um den Dokumentationsblock zu starten, und dann kann ein einzelnes Hash Zeichen in nachfolgenden Zeilen verwendet werden.

Hinweis:

-   Die erste Option wird bevorzugt, um [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings), [PEP257](https://www.python.org/dev/peps/pep-0257/) und die meisten Stilrichtlinien für das Schreiben von Python zu erfüllen (siehe [1](https://realpython.com/python-pep8/), [2](https://realpython.com/documenting-python-code/)). Es wird empfohlen, diesen Stil zu verwenden, wenn du beabsichtigst, dokumentierte Quellen mit [Sphinx](https://www.sphinx-doc.org/en/master/) zu erzeugen, einem sehr gebräuchlichen Werkzeug zur Dokumentation von Python Code. Wenn Du diesen Stil verwendest, kann Doxygen die Kommentare wörtlich extrahieren, aber spezielle Doxygen Befehle, die mit `\\` oder `@` beginnen, funktionieren nicht.
-   Die zweite Option ist nicht der traditionelle Python Stil, aber sie erlaubt es Dir, die speziellen Befehle von Doxygen wie `\param` und `\var` zu verwenden.

### Erster Stil: Pythonische Dokumentation 

Im folgenden Beispiel steht am Anfang eine docstring, um den allgemeinen Inhalt dieses Moduls (Datei) zu erklären. Dann erscheinen docstrings innerhalb der Funktions-, Klassen- und Klassenmethodendefinitionen. Auf diese Weise extrahiert Doxygen die Kommentare und präsentiert sie so, wie sie sind, ohne Änderungen.


```python
'''@package pyexample_a
DoKumentation für dieses Modul.
Mehr Details.
'''


def func():
    '''DoKumentation für eine Funktion.
    Mehr Details.
    '''
    pass


class PyClass:
    '''DoKumentation für eine Klasse.
    Mehr Details..
    '''

    def __init__(self):
        '''Der Konstrukteur.'''
        self._memVar = 0

    def PyMethod(self):
        '''DoKumentation für eine Methode.'''
        pass
```

### Zweiter Stil: Dokumentationsblock vor dem Code 

Im folgenden Beispiel beginnen die Dokumentationsblöcke mit doppelten Hashzeichen `###`. Am Anfang erscheint eine, um den allgemeinen Inhalt dieses Moduls (Datei) zu erklären. Dann gibt es Blöcke vor den Definitionen von Funktions-, Klassen- und Klassenmethoden, und es gibt einen Block nach einer Klassenvariablen. Auf diese Weise extrahiert Doxygen die Dokumentation, erkennt die speziellen Befehle `@package`, `@param`, und `@var` und formatiert den Text entsprechend. 
```python
## @package pyexample_b
#  Documentation for this module.
#
#  More details.


## Documentation for a function.
#
#  More details.
def func():
    pass


## Documentation for a class.
#
#  More details.
class PyClass:

    ## The constructor.
    def __init__(self):
        self._memVar = 0

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self):
        pass

    ## A class variable.
    classVar = 0
    ## @var _memVar
    #  a member variable
```

### Zusammenstellung der Dokumentation 

Die Kompilierung der Dokumentation erfolgt wie bei [für C++ Quellen](#Compilierung_der_Dokumentation/de.md). Wenn sich beide Python Dateien, `pyexample_a.py` und `pyexample_b.py`, mit eigenem Kommentarstil im gleichen Verzeichnis befinden, werden beide verarbeitet. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

Die Dokumentation sollte ähnliche Informationen wie die folgenden enthalten und entsprechende Verknüpfungen zu den einzelnen Modulen und Klassen herstellen. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```

### Umwandlung des pythonischen Stils in den Doxygen Stil 

Im vorherigen Beispiel zeigt die Python Datei, die in einem [Doxygen Stil](#Second_style:_documentation_block_before_the_code/de.md) kommentiert wird, detailliertere Informationen und Formatierungen für ihre Klassen, Funktionen und Variablen. Der Grund dafür ist, dass dieser Stil es Doxygen erlaubt, die speziellen Befehle zu extrahieren, die mit `\\` oder `@` beginnen, während der [Pythonischer Stil](#First_style:_Pythonic_documentation/de.md) dies nicht tut. Daher wäre es wünschenswert, den pythonischen Stil in den Doxygen Stil zu konvertieren, bevor die Dokumentation erstellt wird. Dies ist mit einem zusätzlichen Python-Programm namens [doxypypy](https://github.com/Feneric/doxypypy) möglich. Dieses Programm ist inspiriert von einem älteren Programm namens [doxypy](https://github.com/Feneric/doxypy), das den Python '''docstrings'''' nehmen und in die Doxygen Kommentarblöcke konvertieren würde, die mit einem Doppelhash `###` beginnen. Doxypypy geht noch weiter, da es die docstrings analysiert und interessante Elemente wie Variablen und Argumente extrahiert und sogar Doktests (Beispielcode in den docstrings).

Doxypypy kann mit `pip`, dem Installationsprogramm für Python Pakete, installiert werden. 
```python
pip3 install --user doxypypy
```

Wenn der Befehl `pip` ohne die Option `--user` verwendet wird, benötigt er Superuser (root) Rechte, um das Paket zu installieren, aber das ist in den meisten Fällen nicht erforderlich; verwende root Rechte nur, wenn Du sicher bist, dass das Paket nicht mit den von der Distribution bereitgestellten Paketen kollidiert.

Wenn das Paket als Benutzer installiert wurde, kann es sich in Deinem Heimatverzeichnis befinden, z.B. in `$HOME/.local/bin`. Wenn sich dieses Verzeichnis nicht im `PATH` deines Systems befindet, wird das Programm nicht gefunden. Füge daher das Verzeichnis der Variablen `PATH` hinzu, entweder in deiner `$HOME/.bashrc` Datei oder in deiner `$HOME/.profile` Datei. 
```python
export PATH="$HOME/.local/bin:$PATH"
```

Alternativ kannst du auch einen symbolischen Link zum `doxypy` Programm erstellen und den Link in ein Verzeichnis legen, das bereits im `PATH` enthalten ist. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Sobald das Programm `doxypypy` installiert und vom Terminal aus zugänglich ist, kann eine Python Datei mit pythonischen docstrings mit den folgenden Anweisungen in den Doxygen Stil umformatiert werden. Das Programm gibt den formatierten Code als Standardausgabe aus, also leite diese Ausgabe in eine neue Datei um. 
```python
doxypypy -a -c pyexample_pythonic.py > pyexample_doxygen.py
```


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_pythonic.py`


<div class="mw-collapsible-content">


```python
'''@package pyexample_pythonic
Documentation for this module.
More details go here.
'''


def myfunction(arg1, arg2, kwarg='whatever.'):
    '''
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    '''
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`


<div class="mw-collapsible-content">


```python
##@package pyexample_pythonic
#Documentation for this module.
#More details go here.
#


## @brief     Does nothing more than demonstrate syntax.
#
#    This is an example of how a Pythonic human-readable docstring can
#    get parsed by doxypypy and marked up with Doxygen commands as a
#    regular input filter to Doxygen.
#
#
# @param        arg1    A positional argument.
# @param        arg2    Another positional argument.
#
#
# @param        kwarg   A keyword argument.
#
# @return
#        A string holding the result.
#
#
# @exception        ZeroDivisionError
# @exception        AssertionError
# @exception        ValueError.
#
# @b Examples
# @code
#        >>> myfunction(2, 3)
#        '5 - 0, whatever.'
#        >>> myfunction(5, 0, 'oops.')
#        Traceback (most recent call last):
#            ...
#        ZeroDivisionError: integer division or modulo by zero
#        >>> myfunction(4, 1, 'got it.')
#        '5 - 4, got it.'
#        >>> myfunction(23.5, 23, 'oh well.')
#        Traceback (most recent call last):
#            ...
#        AssertionError
#        >>> myfunction(5, 50, 'too big.')
#        Traceback (most recent call last):
#            ...
#        ValueError
# @endcode
#

def myfunction(arg1, arg2, kwarg='whatever.'):
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>

Die Originaldatei hat oben einen Kommentar ''''@package pyexample_pythonic, der das Modul oder den Namensraum angibt, der durch die Datei beschrieben wird. Dieses Schlüsselwort `@package` wird nicht interpretiert, wenn dreifache Anführungszeichen im Kommentarblock verwendet werden.

In der neuen Datei wird der Kommentarstil so geändert, dass die Zeile `###@package pyexample_pythonic` wird, die nun von Doxygen interpretiert wird. Um jedoch korrekt interpretiert zu werden, muss das Argument manuell bearbeitet werden, um dem neuen Modul (Datei-) Namen zu entsprechen; danach sollte die Zeile `###@package pyexample_doxygen` sein.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

(das Obere wird manuell bearbeitet, der Rest bleibt gleich)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

Um zu kompilieren, erstelle die Konfiguration und führe `doxygen` im Toplevel Verzeichnis aus, das die Dateien enthält. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

Die Dokumentation sollte ähnliche Informationen wie die folgenden enthalten und entsprechende Verknüpfungen zu den einzelnen Modulen herstellen. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```

### Fliegendes konvertieren des Kommentarstils 

Im vorherigen Beispiel wurde die Konvertierung der Dokumentationsblöcke manuell mit nur einer Quelldatei durchgeführt. Im Idealfall soll diese Konvertierung automatisch, fliegend, mit einer beliebigen Anzahl von Python Dateien erfolgen. Dazu muss die Doxygen Konfiguration entsprechend angepasst werden.

Verwende zunächst nicht direkt das Programm `doxypy`, sondern erstelle die Konfigurationsdatei mit `doxygen -g`, bearbeite dann die erstellte `Doxyfile` und ändere das folgende Tag. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

Was dies bewirkt, ist, dass Dateien, die dem Muster entsprechen, alle Dateien mit einer Erweiterung, die auf `.py` endet, das Programm `doxypypy_filter` durchlaufen. Jedes Mal, wenn Doxygen auf eine solche Datei im Quellbaum trifft, wird der Dateiname als erstes Argument an dieses Programm übergeben. 
```python
doxypypy_filter example.py
```

Das Programm `doxypy_filter` ist standardmäßig nicht vorhanden; es sollte als Shell Skript erstellt werden, um `doxypypy` mit den entsprechenden Optionen auszuführen und eine Datei als erstes Argument zu verwenden. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

Nachdem du dieses Shell Skript gespeichert hast, stelle sicher, dass es über Ausführungsrechte verfügt und sich in einem Verzeichnis befindet, das sich im `PATH` deines Systems befindet. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

Auf Windows Systemen kann eine Batch Datei auf ähnliche Weise verwendet werden. 
```python
doxypypy -a -c %1
```

Wenn diese Konfiguration abgeschlossen ist, kann der Befehl `doxygen Doxyfile` ausgeführt werden, um die Dokumentation wie gewohnt zu generieren. Jede Python Datei, die Pythonic ''''triple quotes'''' verwendet, wird spontan neu formatiert, um Kommentare im Stil von `###Doxygen` zu verwenden, und dann von Doxygen verarbeitet, das nun in der Lage ist, das [special commands](#Doxygen_markup/de.md) und [Mardown syntax](#Markdown_support/de.md) zu interpretieren. Der ursprüngliche Quellcode wird nicht geändert, und es muss keine temporäre Datei mit einem anderen Namen erstellt werden, wie in [der vorherige Abschnitt](#Converting_the_Pythonic_style_to_Doxygen_style.md); wenn also eine Anweisung `@package example` gefunden wird, muss sie nicht manuell geändert werden.

Beachte , dass bestehende Python Dateien, die bereits den Stil `###double hash` für ihre Kommentarblöcke verwenden, vom Filter `doxypypy` nicht beeinflusst werden und von Doxygen normal verarbeitet werden.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">


*Allgemeiner Arbeitsablauf zur Erstellung von Quellcodedokumentation mit Doxygen, wenn die Python Dateien gefiltert werden, um die Kommentarblöcke zu transformieren.*

### Python Code Qualitätsprüfung 

Um die automatische Konvertierung von Dokumentationsblöcken nutzen zu können, ist es wichtig, dass die originalen Python Quellen korrekt geschrieben sind und den pythonischen Richtlinien in [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings) und [PEP257](https://www.python.org/dev/peps/pep-0257/) entsprechen. Schlampig geschriebener Code führt dazu, dass `doxypypy` bei der Verarbeitung der Datei fehlschlägt, so dass Doxygen die Dokumentation nicht korrekt formatieren kann.


<div class="mw-collapsible mw-collapsed toccolours">

Die folgenden Kommentarstile erlauben kein Zerlegen der docstrings durch `doxypypypy`, daher sollten sie vermieden werden.


<div class="mw-collapsible-content">


```python
'''@package Bad
'''

def first_f(one, two):

    "Bad comment 1"

    result = one + two
    result_m = one * two
    return result, result_m

def second_f(one, two):
    "Bad comment 2"
    result = one + two
    result_m = one * two
    return result, result_m

def third_f(one, two):
    'Bad comment 3'
    result = one + two
    result_m = one * two
    return result, result_m

def fourth_f(one, two):
    #Bad comment 4
    result = one + two
    result_m = one * two
    return result, result_m
```


</div>


</div>

Verwende immer dreifache Anführungszeichen für die docstrings und stelle sicher, dass sie unmittelbar der Klassen- oder Funktionsdeklaration folgen.

Es ist auch eine gute Idee, die Qualität Ihres Python Codes mit einem Werkzeug wie[flake8](http://flake8.pycqa.org/en/latest/) ([Gitlab](https://gitlab.com/pycqa/flake8)) zu überprüfen. Flake8 kombiniert im Wesentlichen drei Werkzeuge, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle) (früher pep8) und den [McCabe complexity checker](https://github.com/PyCQA/mccabe), um den richtigen pythonischen Stil durchzusetzen.


```python
pip install --user flake8
flake8 example.py
```

Um alle Dateien innerhalb eines Quellbaums zu überprüfen, verwende `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

Wenn das Projekt es verlangt, können einige zu strenge Code Überprüfungen ignoriert werden. Die Fehlercodes können in der [Pycodestyle Dokumentation](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes) eingesehen werden. 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

In ähnlicher Weise ist ein Programm, das in erster Linie prüft, ob Kommentare mit [PEP257](https://www.python.org/dev/peps/pep-0257/) übereinstimmen, [Pydocstyle](https://github.com/PyCQA/pydocstyle). Die Fehlercodes können in der [Pydocstyle Dokumentation](http://www.pydocstyle.org/en/4.0.0/error_codes.html) eingesehen werden. 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Verwende es auch mit `find`, um docstring Überprüfungen für alle Quelldateien durchzuführen. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```

## Quelldokumentation mit Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/) ist das beliebteste System zur Dokumentation von Python Quellcode. Da die Kernfunktionen und Arbeitsbereiche von FreeCAD jedoch in C++ geschrieben sind, wurde davon ausgegangen, dass Doxygen ein besseres Dokumentationswerkzeug für dieses Projekt ist.

Während Sphinx Python docstrings nativ analysieren kann, erfordert es etwas mehr Arbeit, C++ Quelltexte zu analysieren. Das Projekt [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) ist ein Versuch, die Lücke zwischen Sphinx und Doxygen zu schließen, um sowohl Python- als auch C++ Quellcode Dokumentation in das gleiche System zu integrieren. Zuerst muss Doxygen konfiguriert werden, um eine XML Datei auszugeben; die XML Ausgabe wird dann von Breathe gelesen und in einen geeigneten Input für Sphinx umgewandelt.

Weitere Informationen zu diesem Prozess findest du in der Dokumentation von Breathe unter [Quick start guide](https://breathe.readthedocs.io/en/latest/quickstart.html).

Siehe diese Antwort in [Stackoverflow](https://stackoverflow.com/a/35377654) für andere Alternativen zur Dokumentation von C++ und Python Code zusammen im selben Projekt.

## Verwandt

-   [Quelldokumentation](Source_documentation/de.md)
-   [FreeCAD API Internetseite](https://www.freecadweb.org/api/de/)

[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md) [Category:3rd Party](Category:3rd_Party.md)

---
[documentation index](../README.md) > [Developer_Documentation](Category:Developer_Documentation.md) > Doxygen/de
