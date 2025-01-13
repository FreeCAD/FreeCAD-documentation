# Assembly/de
## Einleitung




In FreeCAD wird das Wort \"[Zusammenbau](Assembly/de.md)\" normalerweise verwendet, um sich auf ein [3D Modell](model/de.md) zu beziehen, das aus mehreren unterscheidbaren Teilen besteht, die auf irgendeine Art und Weise zusammengesetzt werden, um ein funktionales Objekt (eine Baugruppe) zu schaffen, so wie Produkte im echten Leben hergestellt werden.

Zum Beispiel sind eine Schraube, eine Beilagscheibe und eine Mutter drei separate Körper, die zusammengesetzt eine Baugruppe bilden.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*Links: drei einzelne beieinander liegende Teile, die mit [PartDesign Körper](PartDesign_Body.md) erstellt wurden. Rechts: die einzelnen Teile zu einer Einheit in [Std Part](Std_Part.md) zusammengestellt.*



## Anwendung



### Manueller Zusammenbau 

Im Allgemeinen werden keine speziellen Werkzeuge benötigt, um Baugruppen zusammenzubauen, es müssen nur viele verschiedene [Körper](Body/de.md) in irgendeiner Weise angeordnet haben.

Um die Körper wie gewünscht zu positionieren, gibt es folgende Mölichkeiten:

-   Das Werkzeug [Std TransformManip](Std_TransformManip/de.md) verwenden,
-   Den Dialog <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Std Positionierung](Std_Placement/de.md) verwenden
-   Die Eigenschaft [Platzierung](Placement/de.md) direkt im [Eigenschafteneditor](Property_editor/de.md) anpassen.

Es kann einer der [externen Pseudo-Zusammenbau-Arbeitsbereiche](external_workbenches/de.md) wie Lattice2, Manipulator, Part-o-magic oder WorkFeature verwendet werden, um Schnittpunkte zu ermitteln, Abstände zu messen und Objekte auf die gewünschte Weise zu verteilen.

Im Prinzip wurde das **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)**-Objekt so ausgelegt, dass es als Grundbaustein für die Erstellung von Baugruppen dient. Dieses Objekt wird verwendet, um mehrere [Körper](body/de.md) zu gruppieren und sie zusammen als eine Einheit, d.h. als Unterbaugruppe, zu bewegen. Anschließend kann diese Unterbaugruppe neben oder innerhalb anderer Unterbaugruppen platziert werden, um die endgültige Baugruppe zu erstellen.



### Zusammenbau mit Randbedingungen 

Es kann auch der enthaltene Arbeitsbereich [Assembly](Assembly_Workbench/de.md) verwendet werden oder entsprechende Addons wie <img alt="" src=images/A2p_workbench.svg  style="width:24px;"> [A2plus](A2plus_Workbench/de.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/de.md) oder <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench/de.md). Bitte beachten, dass [Assembly2](Assembly2_Workbench/de.md) nicht gepflegt wird und daher für neue Modelle nicht zu empfehlen ist.

Die Arbeitsbereiche zum Erstellen von Baugruppen verwenden Randbedingungen und Ausdrücke, um Beziehungen zwischen den Objekten in einem Modell festzulegen und so die Objekte mathematisch an ihren Platz zu binden, z. B. \"diese Fläche sollte an dieser anderen Fläche haften\", \"dieser Zylinder sollte konzentrisch zu diesem Kreis sein\", \"dieser Punkt sollte dieser Kante folgen\", usw.

Dies ist eine erweiterte Anwendung der Software, die normalerweise für komplexemechanischen Systeme eingesetzt wird. Wenn ein [Modell](model/de.md) nicht sehr komplex ist, ist die Verwendung eines Arbeitsbereichs zum Erstellen von Baugruppen möglicherweise nicht nötig.



## Hinweise

-   Seit FreeCAD 1.0 gibt es einen offiziellen Arbeitsbereich [Assembly](Assembly_Workbench/de.md), der standardmäßig im System enthalten ist.

-   Bitte beachten, dass Arbeitsbereiche zum Erstellen von Baugruppen im Allgemeinen nicht miteinander kompatibel sind. Wird eine Baugruppe mit einem dieser Arbeitsbereiche erstellt, sollte man bei diesem bleiben und keinen anderen Arbeitsbereich für die Arbeit an demselben Dokument verwenden.


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/de
