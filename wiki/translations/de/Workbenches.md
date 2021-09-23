# Workbenches/de
FreeCAD basiert, wie viele moderne Konstruktionsanwendungen wie [Revit](wikipedia:Revit.md) oder [CATIA](wikipedia:CATIA.md) auf dem Konzept von [Workbench](wikipedia:Workbench.md). Ein Arbeitsbereich kann als ein Satz von Werkzeugen betrachtet werden, die speziell für eine bestimmte Aufgabe gruppiert sind. In einer traditionellen Möbelwerkstatt hättest du einen Arbeitstisch für die Person, die mit Holz arbeitet, einen anderen für die Person, die mit Metallteilen arbeitet, und vielleicht einen dritten für den Mann, der alle Teile zusammen montiert.

In FreeCAD wird das gleiche Konzept angewendet. Werkzeuge werden entsprechend den Aufgaben, mit denen sie verbunden sind, in Arbeitsbereichen zusammengefasst.

Wenn Du von einem Arbeitsbereich zum anderen wechselst, ändern sich die auf der Oberfläche verfügbaren Werkzeuge. Werkzeugleisten, Befehlsleisten und eventuell andere Teile der Oberfläche wechseln auf den neuen Arbeitsbereich, aber der Inhalt Deiner Szene ändert sich nicht. Du kannst z.B. mit dem Arbeitsbereich Entwurf beginnen, 2D Formen zu zeichnen und diese dann mit dem Part Arbeitsbereich weiterzubearbeiten.

Beachte, dass ein Arbeitsbereich manchmal als *Modul* bezeichnet wird. Allerdings sind Arbeitsbereiche und Module unterschiedliche Gebilde. Ein Modul ist eine beliebige Erweiterung von FreeCAD, während ein Arbeitsbereich ein besonderer Typ von Modul mit einer GUI Konfiguration (Werkzeugleisten und Menüs) ist.

## Eingebaute Arbeitsbereiche 

Die folgenden Arbeitsbereiche sind mit jeder FreeCAD Installation zusammengepackt:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Basis](Std_Base/de.md). Dies ist eigentlich kein Arbeitsbereich, sondern eher eine Kategorie von \'Standard\' Befehlen und Werkzeugen, die in allen Arbeitsbereichen verwendet werden können.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> Der [Architektur Arbeitsbereich](Arch_Workbench/de.md) für die Arbeit mit architektonischen Elementen.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> Der [Entwurf Arbeitsbereich](Draft_Workbench/de.md) enthält 2D Werkzeuge und grundlegende 2D und 3D CAD Einsatzmöglichkeiten.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> Der [FEM Arbeitsbereich](FEM_Workbench/de.md) bietet einen Arbeitsablauf für die Finite Elemente Analyse (FEA).

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> Der [Bild Arbeitsbereich](Image_Workbench/de.md) für die Arbeit mit Bitmap Bildern.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> Der [Arbeitsbereich Inspektion](Inspection_Workbench/de.md) wurde geschaffen, um dir spezielle Werkzeuge für die Untersuchung von Formen zu bieten. Er befindet sich noch in der Entwicklung.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> Der [Polygonnetz Arbeitsbereich](Mesh_Workbench/de.md) für die Arbeit mit triangulierten Polygonnetzen.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> Der [OpenSCAD Arbeitsbereich](OpenSCAD_Workbench/de.md) für das Zusammenspiel mit OpenSCAD und die Reparatur von [Konstruktiver Festkörpergeometrie](constructive_solid_geometry/de.md) (CSG) Modellhistorie.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> Das [Part Modul](Part_Workbench/de.md) für die Arbeit mit CAD Teilen.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> Der [Part Design Arbeitsbereich](PartDesign_Workbench/de.md) zur Erstelllung von Teilformen aus Skizzen.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> Der [Pfad Arbeitsbereich](Path_Workbench/de.md) wird zur Erstellung von G-Code Anweisungen verwendet. Er befindet sich noch in der Entwicklung.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> Der [Punkte Arbeitsbereich](Points_Workbench/de.md) für die Arbeit mit Punktwolken.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> Der [Arbeitsbereich Strahlenverfolgung](Raytracing_Workbench/de.md) für die Arbeit mit Strahlenverfolgung (Bildsynthese).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> Der [Arbeitsbereich Rekonstruktionsingenieurwissenschaften](Reverse_Engineering_Workbench/de.md) soll spezielle Werkzeuge zur Konvertierung von Formen/Volumenkörpern/Polygonnetze in parametrische FreeCAD-kompatible Formelemente bereitstellen. Er befindet sich noch in der Entwicklung.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> Der [Roboter Arbeitsbereich](Robot_Workbench/de.md) zur Untersuchung von Roboterbewegungen.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> Der [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) für die Arbeit mit geometrie-beschränkten Skizzen.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> Der [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md) zur Erstellung und Bearbeitung von Tabellenkalkulationsdaten.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> Der [Startzentrum Arbeitsbereich](Start_Workbench/de.md) ermöglicht es dir, schnell zu einem der gängigsten Arbeitsbereiche zu wechseln.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Der [Arbeitsbereich Oberfläche](Surface_Workbench/de.md) bietet Werkzeuge zum Erstellen und Ändern von Oberflächen. Er ist ähnlich wie der Part Form Erbauer Fläche aus Kanten.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> Der [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) zur Erstellung technischer Zeichnungen aus 3D Modellen. Es ist der Nachfolger des [Zeichnung Arbeitsbereichs](Drawing_Workbench/de.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> Der [Test Rahmenwerk Arbeitsbereich](Testing/de.md) ist für die FreeCAD Fehlersuche.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> Der [Web Arbeitsbereich](Web_Workbench/de.md) bietet dir ein Browserfenster anstelle der [3D Ansicht](3D_view/de.md) in FreeCAD.

### Veraltet

Die folgenden Arbeitsbereiche sind aus Kompatibilitätsgründen noch in der Basisinstallation enthalten, sollten aber nicht mehr verwendet werden.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> Der [Vollständige Arbeitsbereich](Complete_Workbench/de.md) enthält alle Befehle und Funktionen aller Module und Arbeitsbereiche, die bestimmte Qualitätskriterien erfüllen. {{Obsolete/de|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> Der [Arbeitsbereich Zeichnen](Drawing_Workbench/de.md) wurde für die Darstellung deiner 3D Arbeiten auf einer 2D Zeichnung verwendet, ist aber inzwischen veraltet. Es ist immer noch notwendig, alte FreeCAD Dateien zu lesen, die ein Zeichenobjekt enthalten, das ursprünglich mit diesem Arbeitsbereich erstellt wurde. Siehe [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md), der ein fortgeschrittenerer Ersatz ist. {{Obsolete/de|0.17}}

## Externe Arbeitsbereiche 

FreeCAD Arbeitsbereiche lassen sich einfach in [Python](Python/de.md) programmieren, es gibt daher viele Menschen, die zusätzliche Arbeitsbereiche außerhalb des FreeCAD Hauptentwicklungsbereichs entwickeln.

Die [Externe Arbeitsbereich](external_workbenches/de.md) Seite listet alle, die dieser Gemeinschaft bekannt sind. Die meisten sind einfach aus FreeCAD heraus zu installieren, indem man die Option [Erweiterungs Manager](Addon_Manager/de.md), zu finden unter Menü {{MenuCommand/de|Werkzeuge → <img src="images/AddonManager.svg" width=24px> Erweiterungs Manager}}.

Neue Arbeitsbereiche sind immer in der Entwicklung, bleib\' dran!







[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Workbenches/de
