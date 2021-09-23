# Assembly/de
## Einführung


{{TOCright}}

In FreeCAD wird das Wort \"[Zusammenbau](Assembly/de.md)\" normalerweise verwendet, um sich auf ein [3D Modell](model/de.md) zu beziehen, das aus mehreren unterscheidbaren Teilen besteht, die auf irgendeine Art und Weise zusammengesetzt werden, um ein funktionales Objekt zu schaffen, so wie Produkte im echten Leben hergestellt werden.

Zum Beispiel sind eine Schraube, eine Beilagscheibe und eine Mutter drei separate Körper, die zusammengesetzt eine Baugruppe bilden.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">


*Links: drei einzelne beieinander liegende Teile, die mit [PartDesign Körper](PartDesign_Body.md) erstellt wurden. Rechts: die einzelnen Teile zu einer Einheit in [Std Part](Std_Part.md) zusammengestellt.*

## Anwendung

### Manueller Zusammenbau 

Im Allgemeinen brauchst du keine speziellen Werkzeuge, um Baugruppen zu erstellen, du musst nur viele verschiedene [Körper](Body/de.md) in irgendeiner Weise angeordnet haben.

Um die Körper dort zu positionieren, wo du sie haben willst, kannst du

-   das [Std TransformManip](Std_TransformManip/de.md) Werkzeug verwenden,
-   den <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Std Positionierungsdialog](Std_Placement/de.md), verwenden oder
-   ändere die [Platzierungseigenschaft](Placement/de.md) direkt im [Eigenschaftseditor](Property_editor/de.md).

Du kannst eine der Pseudo-Zusammenbau [externe Arbeitsbereiche](external_workbenches/de.md) wie Lattice2, Manipulator, Part-o-magic oder WorkFeature verwenden, um Schnittpunkte zu finden, Abstände zu messen und deine Objekte auf die gewünschte Weise zu verteilen.

Im Allgemeinen wurde das**<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** Objekt konzipiert um als Grundbaustein für die Erstellung von Baugruppen zu dienen. Dieses Objekt wird verwendet, um mehrere [Körper](body/de.md) zu gruppieren und sie als eine Einheit, d.h. als Unterbaugruppe, zusammen zu bewegen. Anschließend kann diese Unterbaugruppe neben oder innerhalb anderer Unterbaugruppen platziert werden, um die endgültige Baugruppe zu erstellen.

### Beschränkter Zusammenbau 

Du kannst auch einen anderen zugeordneten Baugruppenarbeitsbereich verwenden, wie <img alt="" src=images/A2p_workbench.svg  style="width:24px;"> [A2plus](A2plus_Workbench/de.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/de.md) oder <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench/de.md). Bitte beachte, dass [Assembly2](Assembly2_Workbench/de.md) nicht gepflegt wird und daher für neue Modelle nicht zu empfehlen ist.

Die Zusammenbau Arbeitsbereiche verwenden Beschränkungen und Ausdrücke, um Beziehungen zwischen den Objekten in deinem Modell zu erstellen, um die Objekte mathematisch an ihren Platz zu binden, z. B. \"diese Fläche sollte an dieser anderen Fläche haften\", \"dieser Zylinder sollte konzentrisch zu diesem Kreis sein\", \"dieser Punkt sollte dieser Kante folgen\", usw.

Dies ist eine erweiterte Anwendung der Software, die normalerweise bei komplexen mechanischen Systemen verwendet wird. Wenn dein [Modell](model/de.md) nicht sehr komplex ist, ist die Verwendung eines Zusammenbau Arbeitsbereichs möglicherweise nicht notwendig.

## Hinweise

Ab FreeCAD 0.19 gibt es keinen offiziellen Arbeitsbereich für Baugruppen mehr, die standardmäßig im System enthalten ist. Ein Arbeitsbereich für Baugruppen ist schwierig zu programmieren, da viele Probleme hinsichtlich der effizienten Nutzung von [Körpern](Body/de.md) und [Teilen](Part/de.md) in der Baugruppe gelöst werden müssen. Dennoch hat die Einführung des [Anwendungsverknüpfungs](App_Link/de.md)-Objekts die Situation verbessert.

Bitte beachte, dass Zusammenbau Arbeitsbereiche im Allgemeinen nicht miteinander kompatibel sind. Wenn du eine Baugruppe mit einer dieser Arbeitsbereiche erstellst, solltest du bei dieser bleiben und keinen anderen Zusammenbau Arbeitsbereich für die Arbeit mit demselben Dokument verwenden.

Die Entwicklung der Zusammenbau Arbeitsbereiche geht weiter, und es wird erwartet, dass irgendwann ein Zusammenbau Arbeitsbereich als die \"offizielle\" hervorgehen wird. Dies könnte durch die Förderung einer der aktuellen Zusammenbau Arbeitsbereiche oder durch deren Kombination zu einer umfassenderen Lösung geschehen.


{{Std Base navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category:Glossary.md) > Assembly/de
