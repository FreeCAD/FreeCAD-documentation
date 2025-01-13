# Manual:The FreeCAD Interface/de
{{Manual:TOC}}

FreeCAD basier auf dem [Qt-Rahmenwerk](https://de.wikipedia.org/wiki/Qt_(Bibliothek)) und ist durch eine einfache und geradlinige Benutzerschnittstelle gekennzeichnet. Erfahrenere CAD-Anwender können Ähnlichkeiten mit anderen Programmen erkennen, während neue Anwender einfach verschiedene neue Möglichkeiten ausprobieren, die FreeCAD bereithält. Hier ist das Standarderscheinungsbild von FreeCAD:

![](images/FreeCAD_022_Start.png )

Die Startseite dient als Begrüßungsbildschirm und soll einen schnellen und einfachen Zugriff auf die wichtigsten Bereiche von FreeCAD ermöglichen, die ein Benutzer erkunden möchte. Über sie können Benutzer mühelos neue Teile erstellen, aktuelle Dateien öffnen und mit dem 2D-Entwurf beginnen. Darüber hinaus bietet sie Verknüpfungen zu hilfreichen Ressourcen wie Tutorials und Benutzerforen, die sowohl für Anfänger als auch für erfahrene Benutzer, die Anleitungen oder Tipps suchen, von unschätzbarem Wert sind. Benutzer können das Erscheinungsbild der Startseite problemlos nach ihren Wünschen anpassen.

Wenn du mit FreeCAD besser vertraut bist, kannst du die Einstellungen unter „Einstellungen" anpassen. Dadurch kannst du FreeCAD so konfigurieren, dass es direkt in einem der Arbeitsbereiche geöffnet wird und beim Starten ein neues Dokument bereitsteht. Alternativ kannst du einfach die Registerkarte „Startseite" schließen und manuell ein neues Dokument erstellen.

![](images/FreeCAD_022_PartDesign.png )



### Arbeitsbereiche

FreeCAD verwendet ein System namens „Arbeitsbereiche" (Workbenches), das den konzeptionellen Rahmenbedingungen in fortschrittlicher Designsoftware wie Revit oder CATIA ähnelt. Die Idee eines Arbeitsbereichs ist analog zu spezialisierten Stationen in einem wissenschaftlichen Labor, wo verschiedene Arbeitsstationen für unterschiedliche Arten von Experimenten ausgestattet sind. In einem Labor gibt es möglicherweise einen Bereich für Chemie, einen anderen für Biologie und einen dritten für Physik, die jeweils mit den spezifischen Werkzeugen ausgestattet sind, die für diese Disziplinen erforderlich sind.

Im Kontext von FreeCAD ist jeder Arbeitsbereich auf einen bestimmten Aufgabentyp zugeschnitten und organisiert alle erforderlichen Werkzeuge für diese Aktivität in einer Oberfläche. Beim Wechseln zwischen Arbeitsbereichen passt sich der in der Benutzeroberfläche sichtbare Satz von Werkzeugen und Steuerelementen an die Anforderungen der ausgewählten Aufgabe an, obwohl sich der eigentliche Projektinhalt oder die „Szene", an der du arbeitest, nicht ändert. Dies ermöglicht nahtlose Übergänge im Arbeitsablauf, z. B. das Beginnen eines Entwurfs mit grundlegenden 2D-Formen im Arbeitsbereich Draft und das anschließende Ausarbeiten dieser Entwürfe mit erweiterten Modellierungswerkzeugen im Arbeitsbereich Part.

Die Begriffe „Arbeitsbereich" und „Modul" werden manchmal synonym verwendet, haben aber innerhalb von FreeCAD unterschiedliche Bedeutungen. Ein Modul ist jede Erweiterung, die FreeCAD Funktionalität hinzufügt, während ein Arbeitsbereich eine bestimmte Art von Modul ist, das mit eigenen Benutzeroberflächenkomponenten wie Symbolleisten und Menüs ausgestattet ist und bestimmte Aufgabentypen erleichtern soll. Daher ist jeder Arbeitsbereich ein Modul, aber nicht jedes Modul qualifiziert sich als Arbeitsbereich.

Die wichtigste Steuerung der FreeCAD-Oberfläche ist der Arbeitsbereichswähler, mit dem du von einem Arbeitsbereich zum anderen wechseln kannst:

![](images/FreeCAD_WB.png )

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> Der Arbeitsbereich [Assembly](Assembly_Workbench/de.md) zum Erstellen und Lösen mechanischer Baugruppen. {{Version/de|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> Der Arbeitsbereich [BIM](BIM_Workbench/de.md) zum Arbeiten mit Architekturelementen und Erstellen von [BIM](https://en.wikipedia.org/wiki/Building_information_modeling)-Modellen. Er kombiniert den Arbeitsbereich Arch und den ehemals externen Arbeitsbereich BIM, der in {{VersionMinus/de|0.21}} verfügbar ist.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> Der Arbeitsbereich [CAM](CAM_Workbench/de.md) Wird eingesetzt, um G-Code-Anweisungen zu erstellen. Dieser Arbeitsbereich wurde in {{VersionMinus/de|0.21}} \"Path\" genannt.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> Der Arbeitsbereich [Draft](Draft_Workbench/de.md) enthält 2D-Werkzeuge und grundlegende 2D- und 3D-CAD-Bearbeitungen.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> Der [Arbeitsbereich FEM](FEM_Workbench/de.md) stellt einen Arbeitsablauf für die Finite-Elemente-Analyse (FEA) zur Verfügung.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> Der Arbeitsbereich [Inspection](Inspection_Workbench/de.md) wurde entwickelt, um spezielle Werkzeuge für die Untersuchung von Formen bereitzustellen. Er befindet sich noch in einer frühen Entwicklungsphase.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> Der Arbeitsbereich [Material](Material_Workbench/de.md) kümmert sich um FreeCADs Materialsystem. {{Version/de|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> Der Arbeitsbereich [Mesh](Mesh_Workbench/de.md) (Netz) für die Arbeit mit triangulierten Polygonnetzen.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> Der Arbeitsbereich [OpenSCAD](OpenSCAD_Workbench/de.md) für das Zusammenspiel mit OpenSCAD und die Reparatur der Modellhistorie von [konstruktiver Festkörpergeometrie](constructive_solid_geometry/de.md) (Constructive-Solid-Geometry - CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> Der Arbeitsbereich [Part](Part_Workbench/de.md) für die Arbeit mit geometrischen Grundkörpern und booleschen Verknüpfungen.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> Der Arbeitsbereich [Part Design](PartDesign_Workbench/de.md) zum Erstellen von Part-Formen aus Skizzen.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> Der Arbeitsbereich [Points](Points_Workbench/de.md) (Punkte) für die Arbeit mit Punktwolken.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> Der Arbeitsbereich [Reverse Engineering](Reverse_Engineering_Workbench/de.md) soll spezielle Werkzeuge bereitstellen, um Formen, Festkörper oder Netze in parametrische, zu FreeCAD kompatible Formelemente umzuwandeln.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> Der Arbeitsbereich [Robot](Robot_Workbench/de.md) zur Untersuchung von Roboterbewegungen. Wird derzeit nicht gewartet.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> Der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) (Skizzierer) für die Arbeit mit durch geometrische Beziehungen bestimmten Skizzen.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> Der Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) (Tabellenkalkulation) zur Erstellung und Bearbeitung von Daten in Kalkulations- bzw. Konstruktionstabellen.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Der Arbeitsbereich [Surface](Surface_Workbench/de.md) (Oberfläche) stellt Werkzeuge zum Erstellen und Ändern von Oberflächen zur Verfügung. Er ähnelt der Option *Fläche aus Kanten* des [Part Form-Generators](Part_Builder/de.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> Der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) zur Erstellung technischer Zeichnungen aus 3D-Modellen. Er ist der Nachfolger des Arbeitsbereichs [Drawing](Drawing_Workbench/de.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> Der Arbeitsbereich [Test Framework](Testing/de.md) dient zum Debuggen von FreeCAD.

Neue Benutzer sind durch die Arbeitsbereiche oft verwirrt, da es nicht immer einfach ist, zu wissen, in welchem ​​Arbeitsbereich man nach einem bestimmten Werkzeug suchen soll. Sie sind jedoch schnell zu erlernen und fühlen sich nach kurzer Zeit ganz natürlich an. Neue Benutzer erkennen schnell, dass Arbeitsbereiche eine praktische Möglichkeit sind, die Vielzahl der Werkzeuge zu organisieren, die FreeCAD zu bieten hat. Darüber hinaus sind Arbeitsbereiche auch vollständig anpassbar.



### Die Oberfläche 

Lass uns einen genaueren Blick auf die verschiedenen Teile der Oberfläche werfen:

![](images/FreeCAD_022_Interface.png )

Das Hauptfenster der Anwendung lässt sich grob in 11 Abschnitte unterteilen:

1.  Der [Hauptansichtsbereich](main_view_area/de.md), der verschiedene Fenster mit Registerkarten enthalten kann.
2.  Die [3D-Ansicht](3D_view/de.md), normalerweise eingebettet in den [Hauptansichtsbereich](main_view_area/de.md). Die 3D-Ansicht ist das zentrale Element der Benutzeroberfläche. Sie zeigt die Objekte, an denen du arbeitest, und ermöglicht deren Bearbeitung. Es ist möglich, mehrere Ansichten desselben Dokuments (oder derselben Objekte) zu haben oder mehrere Dokumente gleichzeitig geöffnet zu haben. Darüber hinaus kann jede Ansicht separat vom Hauptfenster getrennt werden.
3.  Das Modell und die Registerkarte [Aufgaben](task_panel/de.md).
    1.  Die Registerkarte Modell zeigt dir den Inhalt und die Struktur deines Dokuments.
    2.  Auf der Registerkarte Aufgaben fordert FreeCAD dich zur Eingabe von Werten auf, die für den Workbench und das Werkzeug spezifisch sind, das du gerade verwendest (z. B. die Abmessungen eines Objekts).
4.  Der [Eigenschafteneditor](property_editor/de.md), der angezeigt wird, wenn die Registerkarte Modell in der Benutzeroberfläche aktiv ist. Er ermöglicht die Verwaltung der öffentlich zugänglichen Eigenschaften der Objekte im Dokument. Er besteht aus den Abschnitten Daten und Ansicht, in denen die Visualisierungseigenschaften bzw. die parametrischen Eigenschaften der Objekte angezeigt werden.
5.  Die [Auswahlansicht](selection_view/de.md), die die ausgewählten Objekte oder Unterelemente von Objekten (Knoten, Kanten, Flächen) anzeigt.
6.  Das [Ausgabefenster](report_view/de.md), in dem Nachrichten, Warnungen und Fehler angezeigt werden.
7.  Die [Python-Konsole](python_console/de.md) in der alle ausgeführten Befehle ausgegeben werden und in der du Python-Code eingeben kannst.
8.  Die [Statusleiste](status_bar/de.md), in der einige Nachrichten und Tooltips angezeigt werden.
9.  Der Symbolleistenbereich, in dem die Symbolleisten angedockt sind.
10. Die [Arbeitsbereichsauswahl](Std_Workbench/de.md), in der du den aktiven [Arbeitsbereich](Workbenches/de.md) auswählst.
11. Das [Standardmenü](Standard_Menu/de.md), das die grundlegenden Operationen des Programms enthält.

Drücke „CTRL-ENTER" zum Bestätigen und gehe zur nächsten

Die meisten der oben genannten Paneele können über das Menü **Ansicht → Bedienfelder** ausgeblendet oder angezeigt werden.



### Anpassung der Oberfläche 

Die FreeCAD-Oberfläche ist für umfassende Anpassungen konzipiert. Alle Symbolleisten und Bedienfelder können je nach Benutzerwunsch in verschiedenen Konfigurationen verschoben, gestapelt oder sogar angedockt werden. Darüber hinaus können sie bei Bedarf geschlossen und dann wieder geöffnet werden. Darüber hinaus haben Benutzer zahlreiche weitere Optionen, darunter die Möglichkeit, benutzerdefinierte Symbolleisten mit Werkzeugen aus den verfügbaren Arbeitsbereichen zu erstellen und Tastaturkürzel zuzuweisen oder zu ändern, um den Arbeitsablauf zu optimieren. Diese Flexibilität stellt sicher, dass Benutzer die Umgebung an ihre spezifischen Bedürfnisse und Vorlieben anpassen können.

Diese erweiterten Anpassungsoptionen sind über das Menü **Werkzeuge → Menü Anpassen** verfügbar:

![](images/FreeCAD_022_Customization.png )

**Weiterlesen**

-   [Erste Schritte mit FreeCAD](Getting_started/de.md)
-   [Anpassung der Oberfläche](Interface_Customization/de.md)
-   [Arbeitsbereiche](Workbenches/de.md)
-   [Mehr über Python](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/de
