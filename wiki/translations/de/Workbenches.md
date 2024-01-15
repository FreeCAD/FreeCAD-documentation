# Workbenches/de
FreeCAD basiert, wie viele moderne Konstruktionsanwendungen wie [Revit](https://de.wikipedia.org/wiki/Autodesk_Revit) oder [CATIA](https://de.wikipedia.org/wiki/CATIA) auf dem Konzept von Arbeitsbereichen ([Workbenches](https://en.wikipedia.org/wiki/Workbench)). Ein Arbeitsbereich kann als ein Satz von Werkzeugen betrachtet werden, die speziell für eine bestimmte Aufgabe gruppiert sind. In einer traditionellen Möbelwerkstatt hättest du einen Arbeitstisch für die Person, die mit Holz arbeitet, einen anderen für die Person, die mit Metallteilen arbeitet, und vielleicht einen dritten für den Mann, der alle Teile zusammen montiert.

In FreeCAD wird das gleiche Konzept angewendet. Werkzeuge werden entsprechend den Aufgaben, mit denen sie verbunden sind, in Arbeitsbereichen zusammengefasst.

Wenn Du von einem Arbeitsbereich zum anderen wechselst, ändern sich die auf der Oberfläche verfügbaren Werkzeuge. Werkzeugleisten, Befehlsleisten und eventuell andere Teile der Oberfläche wechseln auf den neuen Arbeitsbereich, aber der Inhalt Deiner Szene ändert sich nicht. Du kannst z.B. mit dem Arbeitsbereich Entwurf beginnen, 2D Formen zu zeichnen und diese dann mit dem Part Arbeitsbereich weiterzubearbeiten.

Beachte, dass ein Arbeitsbereich manchmal als *Modul* bezeichnet wird. Allerdings sind Arbeitsbereiche und Module unterschiedliche Gebilde. Ein Modul ist eine beliebige Erweiterung von FreeCAD, während ein Arbeitsbereich ein besonderer Typ von Modul mit einer GUI Konfiguration (Werkzeugleisten und Menüs) ist.



## Eingebaute Arbeitsbereiche 



### Aktuell

Die folgenden Arbeitsbereiche sind mit jeder FreeCAD Installation zusammengepackt:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Basis](Std_Base/de.md). Dies ist eigentlich kein Arbeitsbereich, sondern eher eine Kategorie von \'Standard\' Befehlen und Werkzeugen, die in allen Arbeitsbereichen verwendet werden können.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> Der Arbeitsbereich [Arch](Arch_Workbench/de.md) (Architektur) für die Arbeit mit architektonischen Elementen.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> Der Arbeitsbereich [Draft](Draft_Workbench/de.md) (Entwurf) enthält 2D-Werkzeuge und grundlegende 2D- und 3D-CAD-Einsatzmöglichkeiten.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> Der Arbeitsbereich [FEM](FEM_Workbench/de.md) bietet einen Arbeitsablauf für die Finite Elemente Analyse (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> Der Arbeitsbereich [Inspection](Inspection_Workbench/de.md) wurde geschaffen, um dir spezielle Werkzeuge für die Untersuchung von Formen zu bieten. Er befindet sich noch in einer frühen Phase der Entwicklung.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> Der Arbeitsbereich [Mesh](Mesh_Workbench/de.md) (Netz) für die Arbeit mit triangulierten Polygonnetzen.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> Der Arbeitsbereich [OpenSCAD](OpenSCAD_Workbench/de.md) für das Zusammenspiel mit OpenSCAD und die Reparatur der Modellhistorie von [konstruktiver Festkörpergeometrie](constructive_solid_geometry/de.md) (Constructive-Solid-Geometry - CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> Der Arbeitsbereich [Part](Part_Workbench/de.md) für die Arbeit mit geometrischen Grundkörpern und booleschen Verknüpfungen.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> Der Arbeitsbereich [Part Design](PartDesign_Workbench/de.md) zur Erstelllung von Part-Formen aus Skizzen.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> Der Arbeitsbereich [Path](Path_Workbench/de.md) (Pfad) wird zur Erstellung von G-Code Anweisungen verwendet.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> Der Arbeitsbereich [Points](Points_Workbench/de.md) (Punkte) für die Arbeit mit Punktwolken.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> Der Arbeitsbereich [Reverse Engineering](Reverse_Engineering_Workbench/de.md) soll spezielle Werkzeuge zur Konvertierung von Formen, Festkörpern oder (Polygon-)Netzen in parametrische zu FreeCAD kompatible Formelemente bereitstellen.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> Der Arbeitsbereich [Robot](Robot_Workbench/de.md) (Roboter) zur Untersuchung von Roboterbewegungen. Wird zur Zeit nicht gewartet.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> Der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) (Skizzierer) für die Arbeit mit durch geometrische Beziehungen bestimmten Skizzen.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> Der Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) (Tabellenkalkulation) zur Erstellung und Bearbeitung von Daten in Kalkulations- bzw. Konstruktionstabellen.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> Der Arbeitsbereich [Start](Start_Workbench/de.md) ermöglicht es dir, schnell zu einem der gängigsten Arbeitsbereiche zu wechseln.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Der Arbeitsbereich [Surface](Surface_Workbench/de.md) (Oberfläche) bietet Werkzeuge zum Erstellen und Ändern von Oberflächen. Er ähnelt der Option *Fläche aus Kanten* des [Part FormGenerators](Part_Builder/de.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> Der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) zur Erstellung technischer Zeichnungen aus 3D-Modellen. Er ist der Nachfolger des Arbeitsbereichs [Drawing](Drawing_Workbench/de.md) (Zeichnung).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> Der Arbeitsbereich [Testing](Testing/de.md) (Test Rahmenwerk) ist für die FreeCAD-Fehlersuche.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> Der Arbeitsbereich [Web](Web_Workbench/de.md) öffnet ein Browserfenster in FreeCAD anstelle der [3D-Ansicht](3D_view/de.md) .



### Veraltet

Die folgenden Arbeitsbereiche sind nach der Version 0.20 nicht mehr Bestandteil von FreeCAD:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> Der Arbeitsbereich [Drawing](Drawing_Workbench/de.md) (Zeichnen) wurde für die Darstellung von 3D-Arbeiten auf einer 2D-Zeichnung verwendet. Der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) ist ein weiterentwickelte Ersatz.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> Der Arbeitsbereich [Image](Image_Workbench/de.md) (Bild) stand für die Arbeit mit Bitmap-Bildern zur Verfügung. Seine Funktionalität wurde in [Std Basis](Std_Base/de.md) integriert. Siehe [Std Import](Std_Import/de.md) und [Std AnsichtBildLaden](Std_ViewLoadImage/de.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> Der Arbeitsbereich [Raytracing](Raytracing_Workbench/de.md) wurde für die Bildsynthese durch Strahlenverfolgung (ray-tracing) verwendet. Der externe Arbeitsbereich [Render](https://github.com/FreeCAD/FreeCAD-render) sollte stattdessen verwendet werden.



## Externe Arbeitsbereiche 

FreeCAD-Arbeitsbereiche lassen sich einfach in [Python](Python/de.md) programmieren, es gibt daher viele Menschen, die zusätzliche Arbeitsbereiche außerhalb von FreeCADs Hauptentwicklungsbereich entwickeln.

Die Seite [Externe Arbeitsbereiche](External_workbenches/de.md) listet alle, die dieser Gemeinschaft bekannt sind. Die meisten sind einfach aus FreeCAD heraus zu installieren, indem man den [Addon-Mannager](Std_AddonMgr/de.md) verwendet, der unter **Werkzeuge → <img src="images/Std_AddonMgr.svg" width=24px> Addon-Manager** zu finden ist.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/de
