# Getting started/de
{{TOCright}}



## Vorwort

FreeCAD ist eine [parametrische 3D Modellierungssoftware](About_FreeCAD/de.md) und hauptsächlich für mechanisches Konstruieren ausgelegt. FreeCAD unterstützt aber auch alle anderen Anwendungen, bei denen 3D Objekte präzise und kontrolliert, mit einer Historie versehen modelliert werden müssen.

FreeCAD befindet sich seit 2002 in der Entwicklung und bietet einen großen [Funktionsumfang](Feature_list/de.md). Für kommerzielle Anwendungen fehlen noch einige Funktionen. Für den Hobbygebrauch und für kleinere Betriebe ist es aber leistungsfähig genug.

Eine schnell wachsende Gemeinschaft begeisterter Anwender ist im [FreeCAD Forum](http://forum.freecadweb.org/index.php) aktiv. Dort sind \[<https://forum.freecadweb.org/viewforum.php?f=24>\| viele Beispiele\] aus Qualitätsprojekten zu finden, die mit FreeCAD erstellt wurden. Siehe auch [FreeCAD Verwendung in der Produktion](FreeCAD_used_in_production.md).

Um zu wachsen, neue Funktionen zu erhalten und Fehler zu beheben ist FreeCAD wie alle freien Software-Projekte auf seine Gemeinschaft angewiesen. Vergiss das nicht, wenn du FreeCAD nutzt! Wenn du magst, kannst du [spenden](Donate/de.md), und FreeCAD z.B. beim Schreiben von Dokumentationen und Übersetzen auf verschiedene Weise [helfen](Help_FreeCAD/de.md).

Siehe auch:

-   [Umstieg von Fusion360 auf FreeCAD](Migrating_to_FreeCAD_from_Fusion360/de.md)
-   [Welchen Arbeitsbereich soll ich auswählen?](Which_workbench_should_I_choose/de.md)
-   [Tutorien](Tutorials/de.md)
-   [Video-Anleitungen](Video_tutorials/de.md)



## Einrichtung

Beginne damit, FreeCAD herunter zu laden und zu installieren. Für Informationen zu aktuellen Versionen und Installationsanweisungen für dein Betriebssystem lese die Seiten [Herunterladen](Download/de.md), ([Windows](Installing_on_Windows/de.md), [Linux](Installing_on_Linux/de.md) oder [Mac](Installing_on_Mac/de.md)). Es gibt fertige Installationspakete für Windows (.msi), Debian und Ubuntu (.deb), openSUSE (.rpm) und Mac OSX. FreeCAD ist über die Paketmanager vieler anderer Linux Distributionen verfügbar. Eine eigenständige, ausführbare [AppImage](AppImage/de.md) Datei ist ebenfalls verfügbar, die auf den meisten aktuellen 64-Bit-Linux-Systemen läuft. Da FreeCAD Open-Source ist, kannst du den Quellcode herunterladen und [kompilieren](Compiling/de.md).



## Erkunden der Oberfläche 

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Die Standard FreeCAD Oberfläche*


**Vollständige Erklärung der  [Oberfläche](Interface/de.md).**


:   1\. Der [Hauptansichtsbereich](main_view_area.md) der verschiedene Registerkartenfenster enthalten kann, hauptsächlich die [3D Ansicht](3D_view/de.md).
:   2\. Die [3D Ansicht](3D_view/de.md), zeigt die geometrischen Objekte im Dokument an.
:   3\. Die [Baumansicht](tree_view/de.md) (Teil der [Combo Ansicht](combo_view/de.md)), die die Hierarchie und Konstruktionshistorie von Objekten im Dokument anzeigt; es kann auch das [Aufgabenfenster](task_panel/de.md) für aktive Befehle anzeigen.
:   4\. Der [Eigenschaftseditor](property_editor/de.md) (Teil der [Comboansicht](combo_view/de.md)), die das Anzeigen und Ändern von Eigenschaften der ausgewählten Objekte ermöglicht.
:   5\. Die [Auswahlansicht](selection_view/de.md), die die Objekte oder Unterelemente von Objekten (Ecken, Kanten, Flächen) anzeigt, die ausgewählt werden.
:   6\. Die [Berichtansicht](report_view/de.md) (oder Ausgabefenster), in dem Meldungen, Warnungen und Fehler ausgegeben wird.
:   7\. Die [Python Konsole](Python_console/de.md), in der alle ausgeführten Befehle ausgegeben werden und in der [Python](Python.md) Code eingegeben werden kann.
:   8\. Die [Statusleiste](status_bar/de.md), in der einige Meldungen und Werkzeugtipps erscheinen.
:   9\. Der Werkzeugleistenbereich, in dem die Werkzeugleisten angedockt sind.
:   10\. Der [Arbeitsbereichsselektor](Std_Workbench/de.md), mit dem der aktive [Arbeitsbereich](workbenches.md) ausgewählt wird.
:   11\. Das [Standardmenü](Standard_Menu/de.md), das die grundlegenden Funktionen des Programms enthält.

Das Hauptkonzept der FreeCAD Oberfläche besteht darin, dass sie in [Arbeitsbereiche](workbenches/de.md) unterteilt ist. Ein Arbeitsbereich ist eine Sammlung von Werkzeugen, die für eine bestimmte Aufgabe angepasst wurden, wie z.B. das Arbeiten mit [Polygonnetzen (mesh)](Mesh_Workbench/de.md) oder das Zeichnen von [2D Objekten](Draft_Workbench/de.md) oder das Arbeiten mit [beschränkten Skizzen](Sketcher_Workbench/de.md). Der aktuelle Arbeitsbereich kann mit dem [Arbeitsbereich Wähler](Std_Workbench/de.md) gewechselt werden. Die in jedem Arbeitsbereich enthaltenen Werkzeuge können individuell [angepasst werden](Interface_Customization/de.md). Werkzeuge von anderen Arbeitsbereichen und auch selbst erstellte [Makros](macros/de.md) können hinzugefügt werden. Meistens wird mit dem [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md) und /oder [Arbeitsbereich Part](Part_Workbench/de.md) begonnen.

Wenn du FreeCAD zum ersten Mal startest, wird dir die Startseite angezeigt. So sieht sie für die Version 0.19 aus:

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">

Die Startseite ermöglicht es dir, schnell zu einer der gebräuchlichsten Arbeitsbereiche zu springen, eine der letzten Dateien zu öffnen oder die neuesten Nachrichten aus der FreeCAD Welt zu sehen. Du kannst den Standard Arbeitsbereich in den [Einstellungen](Preferences_Editor/de.md) ändern.



## Navigieren im 3D Raum 

FreeCAD bietet verschiedene [Navigationsmodi](Mouse_navigation/de.md), die sich durch die Art und Weise, mit Objekten in der 3D Ansicht und der 3D Ansicht selbst zu interagieren, unterscheiden. Einer dieser Modi ist speziell für [Touchpads](Mouse_navigation/de#Touchpad_Navigation.md) ausgelegt, bei dem die mittlere Maustaste nicht genutzt wird. Der Standard Navigationsmodus ist [CAD Navigation](Mouse_navigation/de#CAD_navigation.md). Mit der **[<img src=images/NavigationCAD_dark.svg style="width:16px">** Schaltfläche in der [Status bar](Status_bar/de.md) oder durch rechts klicken eines lehren Bereichst der [3D Ansicht](3D_view/de.md) kann schnell zwischen verschiedenen Moden gewechselt werden.

Es stehen mehrere Ansichtsvoreinstellungen (beispielsweise Draufsicht, Frontansicht, usw.) im Ansichtsmenü, auf der Ansichtssymbolleiste und über Tastenkürzel (**1**, **2**, usw.) zur Verfügung. Mit einem Rechtsklick auf ein Objekt oder den Leerbereich der Ansicht steht ein schneller Zugriff auf allgemeine Vorgänge zur Verfügung, beispielsweise um eine bestimmte Ansicht oder ein Objekt in der Baumansicht auszuwählen.



## Erste Schritte mit FreeCAD 

Das Hauptaugenmerk von FreeCAD besteht darin, Ihnen zu ermöglichen, hochpräzise 3D-Modelle zu erstellen, deren Eigenschaften Sie weiterhin genau kontrollieren (durch die Möglichkeit, in der Modellhistorie zurück zu gehen, und Parameter anpassen zu können) und gegebenenfalls auch die Fertigung dieser Modelle (mittels 3D-Druck, CNC-Fräsen oder sogar bei Bauwerken). Es unterscheidet sich daher sehr von einigen anderen 3D-Anwendungen, die für andere Einsatzzwecke wie z.B. Erstellen von Animationsfilmen oder Spielen programmiert wurden. Die Lernkurve von FreeCAD kann sehr steil sein, besonders wenn es Ihr erster Kontakt mit dem 3D-Modellieren ist. Falls Sie an einigen Stellen nicht mehr weiterkommen, vergessen Sie nicht, dass es eine freundliche Gemeinschaft von Nutzern unter [FreeCAD forum](http://forum.freecadweb.org/index.php) gibt, welche Ihnen schnell weiterhelfen kann.

Welchen Arbeitsbereich du in FreeCAD anfängst zu verwenden, hängt von der Art der Arbeit ab, die du erledigen musst: Wenn du an mechanischen Modellen arbeitest oder ganz allgemein an Miniaturobjekten arbeitest, dann wirst du wahrscheinlich den Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) verwenden wollen. Wenn du in 2D arbeiten möchtest, dann wechsle zum [Entwurf Arbeitsbereich](Draft_Workbench/de.md) oder zum [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) wenn du Beschränkungen benötigst. Wenn du [Gebäudedatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) machen möchtest, starte den [Arch Arbeitsbereich](Arch_Workbench/de.md). Und wenn du aus der OpenSCAD Welt kommst, versuche den [OpenSCAD Arbeitsbereich](OpenSCAD_Workbench/de.md). Es gibt auch viele von der Gemeinschaft entwickelte,verfügbare [Externe Arbeitsbereiche](External_workbenches/de.md).

Sie können den Arbeitsbereich jederzeit wechseln und [modifizieren](Interface_Customization/de.md), um beispielsweise Werkzeuge anderer Arbeitsbereiche einzufügen.



## Arbeiten mit den PartDesign und Skizzierer Arbeitsbereichen 

Der Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) wurde für das Erstellen von komplexen Objekten entwickelt. Beginnend mit einfachen Grundkörpern können beliebige andere Körper hinzugefügt oder ausgeschnitten werden (\"Merkmale\" genannt), bis das Modell der eigenen Vorstellung entspricht. Alle dabei verwendeten Merkmale werden im [Modellbaum](Document_structure/de.md) angezeigt. Man kann sich das mit *PartDesign* erstellte Objekt als eine Folge von Operationen vorstellen, die sich auf das Ergebnisobjekt der jeweils letzten Operation beziehen und somit eine lange Kette bilden. Im Modellbaum ist das fertige Objekt zu sehen, doch die Hierarchie kann aufgeklappt werden, um vorherige Zustände abzurufen oder die Parameter der Merkmale und Operationen nachträglich zu verändern, wobei das Endergebnis automatisch aktualisiert wird.

Der Arbeitsbereich *PartDesign* verwendet dabei viele der Funktionen und Werkzeuge des Arbeitsbereichs [Sketcher](Sketcher_Workbench/de.md). Der *Sketcher* erlaubt es Ihnen zweidimensionale Formen zu zeichnen, die durch wählbare Beschränkungen und Maße definiert werden. Man kann beispielsweise ein Rechteck zeichnen und eine Seitenlänge mit einer *Distanzbeschränkung* festlegen. Diese Seite kann danach nur noch durch eine Modifikation der Beschränkung verändert werden.

Solche mit dem *Sketcher* erstellen 2D-Formen werden vielfach im *PartDesign* verwendet, z.B. um dreidimensionale Volumenkörper zu erstellen oder auch um Bereiche einer Oberfläche für eine geplante Vertiefung zu markieren. So sieht die übliche Vorgehensweise im Arbeitsbereich *PartDesign* aus:

1.  Erstelle eine neuen Skizze
2.  Zeichne einer geschlossenen Form (alle Punkte müssen verbunden sein)
3.  Schließe die Skizze
4.  Erweitere Skizze mit dem Werkzeug *Aufpolsterung* <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> in einen 3D-Volumenkörper
5.  Wähle eine der Seiten des Körpers aus
6.  Erstelle eine zweite Skizze auf dieser Oberfläche
7.  Zeichne eine geschlossene Form
8.  Schließe die Skizze
9.  Füge eine *Tasche* <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> der zweiten Skizze auf dem ersten Objekt ein.

Das Ergebnis dieser Prozedur könnte beispielsweise wie folgt aussehen:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

Die Skizzen können jederzeit ausgewählt und geändert werden, wobei das Endergebnis automatisch aktualisiert wird. Dasselbe gilt auch für die Einstellungen der Operationen *Aufpolsterung* und *Tasche*.



## Arbeiten mit den Arbeitsbereichen Draft und Arch 

Die Arbeitsbereiche [Draft](Draft_Workbench/de.md) und [Arch](Arch_Workbench/de.md) verhalten sich etwas anders als die zuvor beschriebenen Arbeitsbereiche, obwohl sie denselben Regeln folgen, die überall in FreeCAD gelten. Kurz gesagt: Während die Arbeitsbereiche *Sketcher* und *PartDesign* für die Konstruktion von einzelnen komplexen Objekten ausgelegt sind, wurden *Draft* und *Arch* darauf optimiert, die Arbeit mit vielen einfachen Objekten gleichzeitig zu erleichtern.

Der Arbeitsbereich [Draft](Draft_Workbench/de.md) bietet 2D-Werkzeuge, wie sie auch in klassischen CAD-Programmen (z.B. [AutoCAD](https://de.wikipedia.org/wiki/AutoCAD)) zu finden sind. Da das Erstellen von 2D-Zeichnungen jedoch nicht zum eigentlichen Aufgabenbereich von FreeCAD gehört, sollte hierbei keine solch große Auswahl an Werkzeugen wie bei kommerziellen Alternativen erwartet werden. Die meisten der dabei verfügbaren Werkzeuge funktionieren nicht nur in 2D-Ebenen, sondern auch im 3D-Raum und profitieren dabei von hilfreichen Funktionen wie [Ebene markieren](Draft_SelectPlane/de.md) und [Draft Snap](Draft_Snap/de.md).

Der Arbeitsbereich [Arch](Arch_Workbench/de.md) fügt eine Umgebung für [BIM](https://de.wikipedia.org/wiki/Building_Information_Modeling) in FreeCAD ein. Dies erlaubt das Erstellen architektonischer Modelle aus parametrischen Objekten. Der Arbeitsbereich *Arch* basiert umfangreich auf anderen Arbeitsbereichen wie *Draft* oder *Sketcher*. Alle Werkzeuge von *Draft* sind auch in *Arch* zu finden und die meisten Werkzeuge von *Arch* nutzen das Hilfssystem von *Draft*.

Eine typische Vorgehensweise mit *Arch* und *Draft* könnte sein:

1.  Zeichnen einiger Linien mit dem [Linienwerkzeug](Draft_Line/de.md) von *Draft*
2.  Auswahl der einzelnen Linien und Umwandlung in eine Wand mit dem Werkzeug [Wand](Arch_Wall/de.md)
3.  Verbinden der Wände durch Auswahl und einen Klick auf [Add](Arch_Add/de.md)
4.  Erstellen eines [Bodens](Arch_Floor/de.md) und Einfügen der Wände in dieses Boden-Objekt (im Modellbaum)
5.  Erstellen eines [Gebäudes](Arch_Building/de.md) und Einfügen des Bodens in dieses Gebäude-Objekt (im Modellbaum)
6.  Einfügen eines Fensters durch Anklicken des Werkzeugs [Fenster](Arch_Window/de.md), Auswahl der Voreinstellung und anschließende Auswahl einer Wand
7.  Bemaßen des Objekts, indem zuerst eine Arbeitsebene festgelegt wird und dann das Werkzeug [Abmessung](Draft_Dimension/de.md) verwendet wird

Das Ergebnis könnte folgendermaßen aussehen:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

Mehr dazu auf der Seite [Tutorials](Tutorials/de.md).



## Erweiterungen, Makros und externe Arbeitsbereiche 

FreeCAD bietet als Open-Source-Software die Möglichkeit, seine Arbeitsbereiche mit Erweiterungen zu ergänzen.

Das Prinzip [Erweiterungen](Addon/de.md) basiert auf der Entwicklung eines Arbeitsbereich Ergänzung. Jeder Benutzer kann eine Funktion entwickeln, die er für seine eigenen Bedürfnisse oder letztlich für die Gemeinschaft für vermisst hält. Mit dem Forum kann der Benutzer eine Meinung, Hilfe im Forum einholen. Es kann, oder auch nicht, das Objekt seiner Entwicklung nach den Regeln des Urheberrechts zu definieren. Frei für ihn/sie. Für die Entwicklung stehen dem Anwender [scripting](scripting/de.md) Funktionen zur Verfügung.

Es gibt zwei Arten von Erweiterungen:

1.  [Makros](Macros/de.md): kurze Schnipsel des Python Code, die ein neues Werkzeug oder eine neue Funktionalität bereitstellen. Makros beginnen üblicherweise als ein Weg, die Aufgabe des Zeichnens oder Bearbeitens eines bestimmten Objekts zu vereinfachen oder zu automatisieren. Wenn viele dieser Makros in einem Verzeichnis gesammelt werden, kann das gesamte Verzeichnis als neuer Arbeitsbereich verteilt werden.
2.  [Externe Arbeitsbereiche](External_workbenches/de.md): Sammlungen von Werkzeugen, die in Python oder C++ programmiert sind und FreeCAD in einer wichtigen Weise erweitern. Wenn ein Arbeitsbereich ausreichend entwickelt und gut dokumentiert ist, kann sie als eine der Basis Arbeitsbereiche in FreeCAD integriert werden. Unter [Arbeitsbereiche](External_workbenches/de.md) finden Sie das Prinzip und eine Liste der vorhandenen Bibliothek.



## Skriptsprache

Und schließlich ist eine der leistungsfähigsten Funktionen von FreeCAD die [scripting](scripting/de.md) Umgebung. Von der integrierten Python-Konsole (oder von jedem anderen externen Python Skript) aus kann auf fast jeden Teil von FreeCAD zugegriffen, Geometrien erstellt oder geändert werden, die Darstellung dieser Objekte in der 3D Szene geändert oder auf die FreeCAD Oberfläche zugegriffen und diese modifiziert werden. Python Skriptsprache kann auch in [Makros](macros/de.md) verwendet werden, die eine einfache Methode zur Erstellung benutzerdefinierter Befehle bietet.



## Was neu ist 

-   Siehe [Funktionsübersicht](Feature_list/de#Release_notes.md) für eine detaillierte Liste der Leistungsmerkmale.





{{Userdocnavi/de}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Getting started/de
