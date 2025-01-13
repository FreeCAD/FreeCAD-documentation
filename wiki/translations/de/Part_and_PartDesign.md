# Part and PartDesign/de
## Übersicht

Im Laufe der Jahre gab es viele Diskussionen über die Unterschiede und Auswirkungen der Verwendung des <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und des <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) Arbeitsbereichs.

Es ist eine gute Idee, den einen oder den anderen zu verwenden, bis der Benutzer mit dem einen vertraut ist, und dann das andere zu lernen. In der Regel wird auch empfohlen, dass neue Benutzer die beiden nicht mischen, bis sie die Auswirkungen verstanden haben.

Lass uns über diese Auswirkungen sprechen.



## Part Arbeitsbereich Konzepte 

Part Arbeitsbereich ist im Wesentlichen [CSG style modeling](Constructive_solid_geometry/de.md). Der Bediener kombiniert verschiedene Grundelemente, um am Ende eine Darstellung der gewünschten Form zu erhalten. (Tatsächlich geht Part Arbeitsbereich einen Schritt weiter als nur Grundelemente und erlaubt dem Anwender, eine Skizze+Extrudieren Ausführung (oder Skizze+Drehen, Austragen, Ausformen \...) zu verwenden, um auch zufällige Formen zu erstellen.) Wenn ein Grundelement oder eine Form erstellt wird, hat es keine Beziehung zu anderen erstellten Objekten (mit Ausnahme von Skizzen und deren Anhängen), es ist ein einzelner solitärer Körper.

![Rahmen\|Mitte\|Einzelne Festkörper](images/Part_CSG_Prims.png )

Dieser Zustand bleibt so, bis der Operator eine Operation verwendet, um sie zu kombinieren (normalerweise einen Booleschen Wert, der sie addiert oder subtrahiert). Jeder Ausgangskörper bleibt separat zugänglich und die Operation erstellt ein neues Objekt.

Das Wesentliche ist das einzelne solide Stück und das Zusammenfügen dieser Teile.



## PartDesign Arbeitsbereich Konzepte 

Im PartDesign Arbeitsbereich wird das Körperobjekt direkt als einzelner, kumulativer Festkörper konstruiert.

Der 1. Schritt in einem Körper muss ein Materialblock sein, entweder aus einem additiven Grundelement oder einer Extrusion aus einer Skizze, oder eine importierte Form (dann Basis Formelement genannt).

Dieser anfängliche Materialblock wird nach und nach verändert, bis die gewünschte Endform (Festkörper) erreicht ist.

Es ist kumulativ in dem Sinne, dass bei jedem Vorgang Material hinzugefügt oder entfernt wird.

Standardmäßig ist die „Spitze" des Körpers -- sofern keine bewusste Änderung der Visualisierung einer bestimmten Funktion erfolgt -- die letzte am Körper durchgeführte Operation. Dies ist der aktuelle und sichtbare Zustand des Körpers, der durch eine neue Funktion erneut geändert werden kann.

Jede Funktion unter dem Körper stellt die kumulative Form des Festkörpers vom 1. Merkmal bis zum betrachteten Merkmal dar.

Um also **den vollständigen Festkörper zu erhalten**, muss das Spitzen-Feature einerseits die letzte Phase der Konstruktion dieses Festkörpers sein und andererseits **muss der Körper ausgewählt werden** und nicht eine Phase seiner Konstruktion.

Dadurch ist es möglich, im Falle einer Änderung **immer die letzte Version des Solids dargestellt zu haben.**

**Hinweise und Ergänzungen:** Bei jedem Konstruktionsvorgang ist die letzte verwendete Funktion die „Spitze", die auch als „aktive Phase bei der Konstruktion des Objekts" oder „Phase vor der nächsten Aktion bei der Konstruktion des Objekts" definiert werden kann. Wenn die Zeichnung des Objekts abgeschlossen ist, ist die Spitze natürlich die letzte Phase oder Funktion der Konstruktion. Falls jedoch etwas vergessen wird, kann jede Funktion der Konstruktion vorläufig als Spitze deklariert werden: Sie wird dann zum Schritt vor der nächsten Aktion bei der Konstruktion des Objekts, was bedeutet, dass neue Funktionen überall in die Konstruktion eingefügt werden können, **unter der Voraussetzung, dass keine Inkompatibilitäten mit der Folge entstehen**.

Wenn alles fertig ist, muss das letzte Feature noch als Spitze umdeklariert werden, was dem fertigen Objekt entspricht.

![Rahmen\|Zentrum\|Kumulativer Körper Festkörper](images/Part_Design_Cumulativ.png )

Dieses Bild zeigt einen Körper. Es handelt sich um einen kumulativen Festkörper, der aus einer gepolsterten Skizze und einem Kegelprimitiv besteht. Dies ist ein einzelner Festkörper.

Wenn die Spitze auf einem **Pad** liegt, kann das Pad separat existieren. Wenn die Spitze jedoch auf einem **Kegel** liegt, kann der Kegel nicht separat existieren (Spitze auf Kegel = Pad + Kegel).

(Eine andere oft erwähnte Sache ist, dass ein Körper ein einzelner zusammenhängender Festkörper sein ***MUSS***. Dies bedeutet, dass die gesamte von einem Feature im Körper erstellte Geometrie ihren Vorgänger *berühren muss*.)



## Die Auswirkungen 

Obwohl es für Neulinge nicht empfohlen wird, ist es möglich, Tools aus Part Workbench und PartDesign Workbench zu kombinieren, vorausgesetzt, du weißt, was du tust. Zum Beispiel:

Benutzer geraten ins Stocken, wenn sie versuchen, ein Feature unter dem Körper (anstatt den Körper selbst) als eine Auswahl einer booleschen Operation der Part Workbench zu verwenden. Dies ist ein Problem, da das ausgewählte Feature nicht **DEN** vollständigen Festkörper darstellt.

In gewisser Weise stellt der Body aus Sicht des Part Workbench ein weiteres Primitiv dar. Die Verwendung eines Bodys (denke daran, dass es sich um einen Proxy für die Spitze handelt) und eines Part Workbench-Objekts zur Ausführung eines Booleschen Werts ist also zulässig. Das resultierende Objekt ist jedoch ein Part Workbench-Objekt. Daher können PartDesign Workbench-Tools nicht mehr darauf verwendet werden.

Und es kann noch komplizierter werden. Wenn du einen neuen Body erstellst und das Ergebnis aus dem vorherigen Absatz hineinziehst, wird ein BaseObject erstellt. Und du kannst die PartDesign Workbench-Tools darauf anwenden.



## Die Vorbehalte 

Es gibt einen Vorbehalt bezüglich der Spitze und ihrer Darstellung des einzelnen Festkörpers im Körper. „Wenn" die Spitze ein subtraktives Merkmal ist und in einer Aufbereitungsoperation verwendet wird, beispielsweise einer Spiegelung, dann wirkt der Spiegel auf das darunterliegende Merkmal (beispielsweise eine Tasche). Der kumulative Festkörper wird also nicht gespiegelt, das subtraktive Merkmal jedoch schon. Das Ergebnis davon muss ein einzelner Festkörper sein.

In diesem Beispiel erzeugt eine Spiegelung der Spitze (die die Tasche des Schlitzes ist) um eine der Basisebenen oder sogar eine Fläche des Volumenkörpers keinen gespiegelten Volumenkörper des gesamten Modells. (Tatsächlich erzeugt es ein gespiegeltes Feature im Baum, das im Wesentlichen leer ist.)

![centre\|Einzelne Festkörper](images/PhantomMirror.png )

In diesem Beispiel wird eine Spiegelung der Spitze (die die Tasche des Schlitzes darstellt) um die Bezugsebene herum durchgeführt und ein gespiegelter Schlitz erzeugt:

![centre\|Einzelne Körper](images/MirroredSlot.png )

Weitere Informationen findest du auf der Wiki-Seite zum Tool <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [PartDesign Mirrored](PartDesign_Mirrored/de.md).



## Vergleich

Unten siehst du dasselbe Beispiel, das mit jeder der beiden Workbenches erstellt wurde. Natürlich gibt es mit jedem Workbench immer mehrere mögliche Konstruktionsmöglichkeiten. ![Konstruktionen mit Part-Werkbank und PartDesign-Werkbank vergleichen](images/PartWBvsPartDesignWBexample.jpg )

+++
| Im <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> PartDesign-Workbench                                                                                | Im <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> Part-Workbench                                                                                                         |
+=============================================================================================================================================================================+====================================================================================================================================================================================+
| 01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> Neuer Körper \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Neue Skizze in der XZ-Ebene | 01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher-Workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Skizze in der XZ-Ebene |
+++
| ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                            | ![Mitte](images/01Psketch_PartWBvsPartDesignWBn.jpg )                                                                                                                              |
+++
|                                                                                                                                                                             |                                                                                                                                                                                    |
+++

+++
| 02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Drehkörper / Z | 02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Drehen / Z              |
+++
| ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )    | ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg ) |
+++
|                                                                                           |                                                                                  |
+++

+++
| 03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Neue Skizze in der XY-Ebene | 03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher-Workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Neue Skizze in der XY-Ebene |
+++
| ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                 | ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                                                                                                        |
+++
|                                                                                                  |                                                                                                                                                                                         |
+++

+++
| 04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Tasche    | 04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrudieren          |
+++
| ![](images/04pocket_PartWBvsPartDesignWBn.jpg ) | ![](images/04aExtrude_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                                |
+++

+++
|                                                                              | 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Schnitt              |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/04bCut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                        |
+++

+++
| 05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Neue Skizze in der XZ-Ebene | 05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher-Workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Neue Skizze in der XZ-Ebene |
+++
| ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                   | ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                        |
+++
|                                                                                                  |                                                                                                                                                                                         |
+++

+++
| 06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> Pad sym/XZ        | 06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrude sym/XZ       |
+++
| ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg ) | ![](images/06aExtrude_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                |                                                                                |
+++

+++
|                                                                              | 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Entwurf <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Polares Muster |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                  |
+++
|                                                                              |                                                                                                                                                     |
+++

+++
|                                                      | 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> Fusion |
+++
| ![Mitte](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![Mitte](images/06cFusion_PartWBvsPartDesignWB.jpg )       |
+++
|                                                      |                                                            |
+++

+++
| 07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Neue Skizze auf planarer Basisfläche | 07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher-Workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Neue Skizze in der XZ-Ebene |
+++
| ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )          | ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                        |
+++
|                                                                                                           |                                                                                                                                                                                         |
+++

+++
| 08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> Loch - Senkbohrung              | 08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Drehen               |
+++
| ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg ) | ![](images/08aRevolve_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                |                                                                                |
+++

+++
|                                                                              | 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Entwurf <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Polares Muster |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                  |
+++
|                                                                              |                                                                                                                                                     |
+++

+++
| 09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> Polares Muster von Loch und Pad | 09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Schnitt             |
+++
| ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )     | ![](images/09Cut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                                |                                                                      |
+++

Vergleiche die Konstruktionsbäume in den beiden Workbenches sowie deren Organisation und Lesezeitleiste:

+++
| 10- Konstruktionsbaum im PartDesign-Workbench                                      | 10- Konstruktionsbaum im Part-Workbench                                |
+++
| ![](images/PartvsPartDesign_TreePartDesignWB.jpg ) | ![](images/PartvsPartDesign_TreePartWB.jpg ) |
+++
|                                                                                    |                                                                        |
+++



## Schlussfolgerung

Die Arbeitsbereiche Part und PartDesign können mit etwas Vorsicht zusammen verwendet werden, um recht komplexe Modelle zu erstellen.

[Anfang](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/de
