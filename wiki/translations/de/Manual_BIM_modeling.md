# Manual:BIM modeling/de
{{Manual:TOC}}

[Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) oder engl. [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling), kurz BIM, ist ein Prozess, der im Bauwesen verwendet wird, um Digitale Darstellungen von realen Strukturen zu erstellen und zu verwalten. Er integriert nicht nur 3D-Geometrie, sonder auch wichtige Daten, wie Werkstoffe, Kosten und Zeitpläne und ermöglicht so umfangreiche Analysen und Zusammenarbeit während des gesamten Produktlebenszyklus eines Projekts.

In FreeCAD hat sich die Funktionalität von BIM erheblich weiterentwickelt, besonders mit der Veröffentlichung der Version 1.0, in der die vorher getrennten Arbeitsbereiche Arch und BIM in einen integrierten Arbeitsbereich BIM zusammengeführt wurden. Diese Zusammenlegung rationalisiert Arbeitsabläufe, die dem Anwender ermöglichen Gebäudeprojekte in einer einzigen Umgebung zu erstellen, zu dokumentieren und zu verwalten.

Ein wesentlicher Fortschritt, der in der FreeCAD-Versio 1.0 vorgestellt wurde, ist die Aufnahme des Native-IFC-Konzepts. Vorher hat FreeCAD Daten, wie die meisten BIM-Anwendungen, hin und her übersetzt zwischen seinen internen Datenmodell und dem IFC- (Industry Foundation Classes) Dateiformat, was während der Lade- und Speicherabläufe zu Datenverlust führen kann. Mit Native-IFC können FreeCAD-Anwender jetzt IFC-Dateien direkt öffnen, bearbeiten und speichern, wobei die IFC-Datei selbst als Datenstruktur dient. Diese Herangehensweise beseitigt unnötige Datenübersetzung und stellt sicher, dass Änderungen gespeichert werden, ohne die gesamte Datei umzuschreiben, macht es kompatibel zu Systemen zur Versionssteuerung wie Git und stellt transparentere, präzise Arbeitsabläufe zum Umgang mit IFC-Dateien bereit.

In diesem Kapitel werden wir sehen, wie dieses kleine Gebäude modelliert wird:

![](images/FreeCAD_BIMHouse.png )

-   Ein neues Dokument erstellen und zum Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM](BIM_Workbench/de.md) wechseln.
-   In den Voreinstellungen unter **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten** folgende Einstellungen anpassen:
    -   **Hauptlinien alle** `10 Quadrate`.
    -   **Rasterabstand** `1000 mm`, um ein auf einem Meter basierendes Raster zu haben, das für die Größe unseres Gebäudes geeignet ist.
    -   **Rastergröße** `100 Quadrate`.
-   In der Symbolleiste **Draft-Einrasten** sicherstellen, dass <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Einrasten auf Raster](Draft_Snap_Grid/de.md) aktiviert ist, damit wir das Raster so weit wie möglich nutzen können.
-   Wenn die Achsen nicht zu sehen sind, die Schaltfläche <img alt="" src=images/Draft_ToggleGrid.svg  style="width:16px;"> [Raster umschalten](Draft_ToggleGrid/de.md) anklicken.
-   Die [Arbeitsebene](Draft_SelectPlane/de.md) auf **Draufsicht (XY)** einstellen.
-   Vier Linien mit dem Werkzeug <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Linie](Draft_Line/de.md) zeichnen. Die Koordinaten können manuell eingeben oder die Punkte einfach mit der Maus auf dem Raster angewählt werden. Wir verwenden Meter für unsere Abmaße:
    -   Vom Punkt (0,0) zum Punkt (0,3)
    -   Vom Punkt (0,3) zum Punkt (4,3)
    -   Vom Punkt (4,3) zum Punkt (4,0)
    -   Vom Punkt (4,0) zum Punkt (0,0)

![](images/Exercise_arch_03.jpg )

Man beachte, dass wir die Linien einheitlich in derselben Richtung gezeichnet haben (im Uhrzeigersinn). Obwohl dies ist nicht erforderlich ist, hilft es sicherzustellen, dass die Wände, die wir als nächstes erstellen, alle dieselbe Ausrichtung bezüglich links und rechts besitzen. Man könnte sich fragen, ob wir nicht einfach ein Rechteck hätten zeichnen können, was einfacher gewesen wäre. Vier einzelne Linien geben uns aber die Möglichkeit, zusätzliche BIM-Funktionalität vorzustellen, wie das Kombinieren mehrerer Objekte zu einem, was einen entscheidenden Anteil am Arbeitsablauf darstellt.

-   Wenn die Linien erstellt wurden, sollten deren Start- und Endpunkte überprüft und gegebenenfalls angepasst werden, damit sie genau stimmen.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   alle vier Linien auswählen, dann die Schaltfläche <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Wand](Arch_Wall/de.md) drücken.
-   Die **Höhe** der Wand auf 3 m (Standardwert) setzen.
-   Die Eigenschaft **Ausrichtung** auf **links** setzen; dies stellt sicher, dass die Wände, die wir erstellen, auf der linken Seite der Linien, die wir erstellt haben, positioniert werden. In FreeCADs Arbeitsbereich BIM werden Wände üblicherweise auf einer Referenzlinie basierend erstellt und ihre Ausrichtung bezüglich links und rechts bestimmt, auf welcher Seite der Linie die Wand positioniert wird.

Wurde die Wand nicht in derselben Reihenfolge wie beschrieben (im Uhrzeigersinn) gezeichnet, kann sich die Ausrichtung einiger Wände umkehren, das heißt, dass sie auf der gegenüberliegenden Seite der Linie positioniert sein können (auf der rechten, anstatt auf der linken). In so einem Falle muss die Ausrichtung nach rechts für diese Wände angepasst werden, um sicherzustellen, das alle einheitlich ausgerichtet sind. Einmal richtig ausgerichtet, befinden sich alle Wände innerhalb des Grundrisses und ergeben die gewünschte Form.

![](images/Exercise_arch_04.jpg )

Nach dem Erstellen der Wände, müssen sie im nächsten Schritt so miteinander verbunden werden, dass sie sich sauber (über-) schneiden. Das ist nötig, wenn die Wände an ihren Schnittkanten nicht sauber verbunden sind. Um dies durchzuführen, zuerst eine Wand als \"Basiskomponente\" auswählen und die anderen Wände als \"Ergänzungen\", die ihre Geometrie mit der Basiskomponente zusammenfügen. Alle Objekte im Arbeitsbereich BIM können mehrere Ergänzungen (die Geometrie hinzufügen) und auch \"Subtraktionen\" (die Geometrie entfernen) enthalten. Diese Zusammenhänge können jederzeit verwaltet werden, indem das Objekt in der Baumansicht doppelt angeklickt wird; dies ermöglicht flexible Anpassungen, die sicherstellen, dass Wände und andere Strukturelemente sauber eingebunden werden.

-   Die vier Wände mit gedrückter **Strg**-Taste auswählen, die letzte wird dann zur Basiskomponente.
-   Die Schaltfläche <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Komponente hinzufügen](Arch_Add/de.md) drücken. Die vier Wände sind nun zu einer geworden:

![](images/Exercise_arch_05.jpg )

Die einzelnen Wände sind nach wie vor zugänglich, wenn die Wand in der Baumansicht expandiert wird.

-   Lasst uns nun eine Tür positionieren; dafür das Werkzeug <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Tür](BIM_Door/de.md) anklicken.
-   Zu Beginn die Wand auswählen. Auch wenn dieser Schritt nicht nötig ist, ist er eine nützliche Angewohnheit, die man sich antrainieren sollte. Wenn ein Objekt ausgewählt wurde, bevor der Vorgang gestartet wird, wird der Vorgang standardmäßig automatisch an diesem Element durchgeführt.
-   Die <img alt="" src=images/View-axonometric.svg  style="width:16px;"> [Arbeitsebene](Draft_SelectPlane/de.md) auf **Automatisch** einstellen, damit wir nicht nur auf die Bodenebene eingeschränkt sind.
-   Die Schaltfläche <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Tür](BIM_Door/de.md) drücken.
-   Im Aufgaben-Fenster der Tür die Einstellung **Glass door** auswählen und ihre **Breite** auf 1 m setzen und ihre **Höhe** auf 2.1 m. Wir sehen hier, dass wir verschiedenen Arten von Türen auswählen und ihre Parameter wie gewünscht einstellen können. In FreeCAD ist eine Tür von einem [Fenster](Arch_Window/de.md)-Objekt abgeleitet.
-   Sicherstellen, dass die Option <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [In der Nähe einrasten](Draft_Snap_Near/de.md) aktiviert ist, damit wir auf Flächen einrasten können.
-   Die Tür ungefähr in der Mitte der Vorderfläche der Wand positionieren:

![](images/FreeCAD_BIMDoor.png )

-   Durch Erweitern der Wand- und Fensterobjekte in der Baumansicht, können wir nun die genaue Position festlegen. Dafür wird die Eigenschaft **Placement** der Basisskizze unserer Tür geändert. Die Position wird auf **x = 0.5 m, y = 0, z = 0** gesetzt. Unsere Tür ist nun genau dort, wo wir sie haben wollen:

![](images/FreeCAD_BIMDoorPos.png )

-   Lasst uns ein Fenster neben unserer Tür einbauen; dafür die Wand auswählen, das Werkzeug <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Fenster](Arch_Window/de.md) anklicken, die Einstelllung **Open 2-pane** auswählen und ein **1 m x 1 m** großes Fenster in dieselbe Fläche einfügen, wie die Tür. Die Eigenschaft Placement der Basisskizze unseres Fensters auf die Position **x = 0, y = 0, z = 1,1 m** setzen, damit die Oberkante des Fensters mit der Oberkante der Tür fluchtet (kollinear ausgerichtet ist).

![](images/FreeCAD_BIMWindow.png )

Fenster basieren immer auf Skizzen. Es ist einfach, maßgeschneiderte Fenster zu erstellen, indem zuerst eine Skizze auf einer Fläche erzeugt wird, die dann zu einem Fenster wird, wenn man die Wand auswählt und die Schaltfläche Fenster drückt. Danach können die Fenster-Parameter festgelegt werden (welcher Teil der Skizze extrudiert werden soll und wie weit); dafür in der Baumansicht doppelt auf das Fenster klicken. Lasst uns jetzt mit dem Erstellen einer Platte fortfahren:

-   Die [Arbeitsebene](Draft_SelectPlane/de.md) auf **Draufsicht (XY)** einstellen.
-   Ein <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rechteck](Draft_Rectangle/de.md) erstellen, mit einer **Länge** von 5 m, einer **Höhe** von **4 m** und eingesetzt an der Position x: -0,5 m, y: -0,7 m, z: 0.
-   Das Rechteck auswählen.
-   Das Werkzeug <img alt="" src=images/BIM_Slab.svg  style="width:16px;"> [Platte](BIM_Slab/de.md) anklicken, um aus dem Rechteck eine (Boden-) Platte zu erstellen.
-   Die Eigenschaft **Höhe** der Platte auf 0,2 m und die Richtung **Normal** auf (0,0,-1) setzen, damit sie nach unten extrudiert wird. Wir hätten das Objekt stattdessen auch 20 cm nach unten versetzen können, aber es immer gute Vorgehensweise, das extrudierte Objekt am gleichen Platz wie das Basisprofil zu belassen, um Einheitlichkeit und Genauigkeit zu erhalten.
-   Die Eigenschaft **Ifc Type** der Platte auf **slab** setzen. Das ist in FreeCAD nicht nötig, aber für den IFC-Export ist das wichtig, weil es dafür sorgt, dass das Objekt mit dem richtigen IFC-Typ exportiert wird.

![](images/FreeCAD_BIMSlab.png )

-   Lasst uns jetzt ein Dach über unsere Köpfe bauen. Wir können dies einfach erreichen, indem wir das Werkzeug <img alt="" src=images/Arch_Roof.svg  style="width:16px;"> [Dach](Arch_Roof/de.md) verwenden.
-   Die Option <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Einrasten auf Arbeitsebene](Draft_Snap_WorkingPlane/de.md) anklicken, um das Zeichnen auf allen Ebenen zu aktivieren.
-   Eine der obersten Flächen unseres Hauses auswählen und die Schaltfläche <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Ebene wählen](Draft_SelectPlane/de.md) drücken. Die Arbeitsebene wird jetzt auf diese Fläche ausgerichtet.
-   Ein <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rechteck](Draft_Rectangle/de.md) erstellen, durch Einrasten auf zwei gegenüberliegende Punkte der Wände:
-   Unter dem Reiter **Daten** des Daches die Eigenschaft **Runs** auf 1600 setzen.
-   Soll die Farbe des Daches geändert werden, kann dies unter dem Reiter Ansicht erfolgen.

![](images/FreeCAD_BIMHouseg.png )

Damit ist unser Model jetzt komplett. Der nächste Schritt ist, das Modell so ordentlich aufzuräumen, dass sichergestellt ist, dass es sich korrekt in das IFC-Format exportieren lässt. IFC-Dateien erfordern, dass alle Gebäudeelemente in einem **Gebäude**-Objekt (building object) gruppiert sind und wahlweise innerhalb einer bestimmten **Geschichte** (story). Zusätzlich müssen sich alle Gebäude auf einem **Grundstück** (site) befinden. FreeCADs IFC-Exportfunktion erstellt automatisch ein Standard-Grundstück, wenn noch keins vorhanden ist, sodass wir es nicht von Hand einfügen müssen. E ist wichtig, dass Modell richtig zu strukturieren, damit es den IFC-Norme entspricht, und so eine reibungslose Zusammenarbeit mit anderen BIM-Programmen gewährleistet. Eine vernünftige Organisation hilft auch dabei, Datenverlust während des Exportprozesses zu vermeiden.

-   Die Wände, die Platte und das Dach auswählen.
-   Die Schaltfläche <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Stockwerk](Arch_Floor/de.md) drücken.
-   Das gerade angelegte Stockwerk auswählen.
-   Die Schaltfläche <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Gebäude](Arch_Building/de.md) drücken.

Unser Modell ist nun bereit für den Export:

![](images/FreeCAD_BIMExport.png )

Das [IFC-Format](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) ist einer der wertvollsten Vorzüge in einer freien BIM-Welt, denn es erlaubt den Datenaustausch zwischen jeder Anwendung und jedem Akteur in der Welt des Baugewerbes in einer offenen Weise (das Format ist offen, frei und wird von einem unabhängigen Konsortium gepflegt). Der Export Deines Modells im IFC-Format gewährleistet, dass jeder es ansehen und untersuchen kann, unabhängig von der verwendeten Anwendung.

-   Wähle das oberste zu exportierende Objekt, das Gebäude-Objekt.
-   Wähle aus dem Menü **Datei -\> Export -\> IFC** und speichere Deine Datei.
-   Die resultierende IFC-Datei kann nun mit einer Vielzahl von Anwendungen und Betrachtern (das folgende Bild zeigt die geöffnete Datei im [IfcPlusPlus](http://www.ifcquery.com/)-Betrachter). Die Überprüfung der exportierten Datei in solch einer Betrachtungsanwendung ist wichtig, um sicherzustellen, dass die enthaltenen Daten korrekt sind, bevor die Datei an andere Personen weitergegeben wird. FreeCAD kann ebenfalls verwendet werden, um die IFC-Datei zu öffnen.

![](images/FreeCAD_BIMIFC.png )

Wir können den Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw](TechDraw_Workbench/de.md) zum Erstellen einer Zeichnung unseres Gebäudes verwenden. Der Prozess ist ähnlich dem, was im vorherigen Abschnitt dargestellt wurde, daher gehen wir hier nicht zu sehr ins Detail. Wir erstellen einfach eine neue Ansicht, indem wir zuerst die Schaltfläche <img alt="" src=images/TechDraw_PageDefault.svg  style="width:16px;"> [Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md) anklicken, dann die Ansicht auswählen, die wir auf der Zeichnung darstellen wollen und schließlich Maße hinzufügen, wo erforderlich. Dies ermöglicht, eine professionelle 2D-Darstellung des 3D-Modells für Dokumentation und Präsentation zu erstellen.

![](images/FreeCAD_BIMHouseDrawing.png )

Unsere Seite ist nun fertig und wir können sie im SVG- oder DXF-Format ausgeben oder sie drucken. Das SVG-Format erlaubt Dir, die Datei in Illustrationsanwendungen wie [Inkscape](http://www.inkscape.org) zu öffnen, mit denen Du technische Zeichnungen schnell aufwerten und sie in schönere Präsentationszeichnungen verwandeln kannst. Es bietet viel mehr Möglichkeiten als das DXF-Format.



## Herunterladen

-   Die in dieser Übung erstellte Datei <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd>
-   Die aus der obigen Datei exportierte IFC Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.ifc>
-   Die aus der obigen Datei exportierte SVG Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.svg>



## Verwandtes

-   [BIM Arbeitsbereich](BIM_Workbench/de.md)
-   [Der Arch Arbeitsbereich](Arch_Workbench/de.md)
-   [Die Entwurf Arbeitsebene](Draft_SelectPlane/de.md)
-   [Die Entwurf Fang Einstellungen](Draft_Snap/de.md)
-   [Das Ausdrücke System](Expressions/de.md)
-   [Das IFC Format](https://de.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org)
-   [IfcPlusPlus](http://www.ifcquery.com)
-   [Inkscape](http://www.inkscape.org)





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Manual:BIM modeling/de
