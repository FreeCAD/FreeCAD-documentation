# Feature editing/de
## Einleitung

Diese Seite erklärt den Arbeitsablauf \"Feature-Editing\" des Arbeitsbereichs <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign](PartDesign_Workbench/de.md).



## Körper

Die Arbeit in PartDesign erfordert zunächst das Erstellen eines <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> **[Körpers](PartDesign_Body/de.md)**. Der PartDesign-Körper (Body-Objekt) ist ein Behälter, der einen einzelnen zusammenhängenden Festkörper enthalten soll. Wird ein Körper erstellt, werden ihm automatisch ein Ursprung (Origin-Objekt) und ein lokales Koordinatensystem, das die Standard-Bezugsebenen (XY, XZ, YZ) und die Achsen (X, Y, Z) enthält, hinzugefügt. Der Festkörper wird durch hinzufügen von Formelementen aufgebaut. Jedes [Formelement](PartDesign_Feature/de.md) ist kumulativ und fügt dem vorhergehenden Formelement etwas hinzu oder zieht etwas davon ab.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:400px;">



*Feature-Editing angewendet. Von links nach rechts:<br>
Körper mit einem Formelement [Quader](PartDesign_AdditiveBox/de.md).<br>
Körper mit den Formelementen Quader und [Fase](PartDesign_Chamfer/de.md).<br>
Körper mit den Formelementen Quader, Fase und [Vertiefung](PartDesign_Pocket/de.md).*

Ein Dokument kann mehrere Körper enthalten, aber nur einer kann aktiv sein. Neue Formelemente werden dem aktiven Körper hinzugefügt. Ein Körper kann durch Doppelklick in der [Baumansicht](Tree_view/de.md) aktiviert bzw. deaktiviert werden. Der aktive Körper wird in der Baumansicht farblich hervorgehoben.

![](images/PartDesign_Body_tree.png )



### Was ist ein zusammenhängender Festkörper? 

Ein einzelner zusammenhängender Festkörper ist ein Objekt wie ein Gussteil oder etwas, das maschinell aus einem einzigen Metallblock herausgearbeitet wurde. Wenn das Objekt Nägel, Schrauben oder Kleber enthält, ist es kein einzelner zusammenhängenden Festkörper. Ein praktisches Beispiel ist ein Holzstuhl, der aus mehreren Körpern zusammengestellt wird, mit einem für jede seiner Unterkomponenten (Beine, Latten, Sitz usw.).

In FreeCAD-Version 1.0 wurde eine experimentelle Eigenschaft eingeführt, die Körper ermöglicht, die nicht zusammenhängend sind. Dies kann auch in den [Einstellungen](PartDesign_Preferences/de#Allgemein.md) als Standardeinstellung für neu erstellte Körper vorgegeben werden. Dies ist nicht dafür gedacht, um einen Holzstuhl, wie in dem vorherigen Beispiel, aufzubauen. Sie soll Formelemente ermöglichen, die (vorerst) nicht verbundene Festkörper ergeben, die durch später folgende Formelemente zu einem zusammenhängenden verbunden werden.

Wenn ein Modell mehrere Körper benötigt, wie der Holzstuhl, kann der uninverselle <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Part-Container](Std_Part/de.md) verwendet werden, um sie zu gruppieren und das Ganze als Einheit zu bewegen.



### Sichtbarkeit der Körperelemente 

Standardmäßig präsentiert ein Körper (Body-Objekt) sein neuestes Formelement nach außen. Dieses Formelement ist die \"Spitze\" (von engl. tip) des Körpers. Diese \"Spitze\" markiert auch die Stelle, an der neue Formelemente hinzugefügt werden. Es ist möglich, die \"Spitze\" auf ein Formelement in der Mitte des Körpers zu versetzen, um dort neue Objekte einzufügen (Formelemente, Skizzen oder Bezugselemente). Wird eine neues Formelement in den Baum eingefügt, wird das vorherige ausgeblendet und das neue Formelement wird zur \"Spitze\".

:   (In der Baumansicht wird die \"Spitze\" mit dem passenderen Begriff Arbeitsposition bezeichnet, da sie die Position kennzeichnet an der weitergearbeitet wird, also neue Formelemente an- bzw. eingefügt werden)

Es kann immer nur ein Formelement zur Zeit sichtbar sein. Es ist möglich, die Sichtbarkeit eines beliebigen Formelements im Körper [umzuschalten](Std_ToggleVisibility/de.md), indem man es in der Baumansicht markiert und die **Leertaste** drückt, wodurch man sich in der Verlaufsgeschichte des Körpers zurück bewegt. Man beachte, dass das Ändern der Sichtbarkeit die Arbeitsposition des Körpers nicht verändert.



### Objekte verschieben und neu ordnen 

Die Formelemente eines Körpers können anders angeordnet werden oder sie können in einen anderen Körper zu verschoben werden. Das Formelement auswählen und mit einem Rechtsklick darauf ein Kontextmenü öffnen, das beide Optionen enthält. Die Operation kann abgebrochen werden, wenn das Objekt Abhängigkeiten im Quellkörper aufweist, z.B. wenn es an einer Fläche befestigt ist. Um eine Skizze in einen anderen Körper zu verschieben, sollte sie keine Verknüpfungen zu externer Geometrie enthalten.

<img alt="" src=images/PartDesign_workflow.svg  style="width:400px;">



*Schematische Darstellung des PartDesign-Arbeitsablaufes.*



## Bezugsgeometrie

Die Bezugsgeometrie besteht aus benutzerdefinierten Ebenen, Linien, Punkten oder extern verknüpften Formen. Sie können zur Verwendung als Referenz für Skizzen und Formelemente erstellt werden. Es gibt viele Möglichkeiten zum [Befestigen](Part_EditAttachment/de.md) von Bezugsobjekten.

In FreeCAD sind Bezugsebenen sinnvoll, wenn Skizzen in ungewöhnlichen Ausrichtungen positioniert werden, d.h. auf gegenüber den Hauptachsen versetze oder gedrehte Ebenen. Da Skizzen aber auch in ungewöhnlichen Ausrichtungen positioniert werden können und dieselben Befestigungsmöglichkeiten besitzen, wie Bezugsebenen, ist es oft nicht nötig, Bezugsebenen zu verwenden. Bezugsebenen sind am sinnvollsten, wenn es mehrere Skizzen mit derselben ungewöhnlichen Ausrichtung gibt. Wird die Ausrichtung der Bezugsebene angepasst, werden auch alle zugehörigen Skizzen sowie mit ihnen erstellte Formelemente entsprechend ausgerichtet.

Obwohl die FreeCAD-Version 1.0 schon Code enthält, der das [Problem der topologischen Benennung](Topological_naming_problem/de.md) abmildert, ist es immer noch am besten, Skizzen und Bezugsebenen an den Basisebenen des Ursprung-Objekts eines Körpers zu befestigen, wann immer es möglich ist. Das Referenzieren auf erzeugte Geometrie (Geometrie, die das Ergebnis eines Vorgangs zur Erstellung eines Formelements ist, z.B. ein Block oder eine Vertiefung) kann weiterhin weniger stabile Modelle ergeben. Siehe [Ratschläge zum Erstellen stabiler Modelle](#Ratschläge_zum_Erstellen_stabiler_Modelle.md) weiter unten.



## Ratschläge zur Erstellung stabiler Modelle 

Die Idee der parametrischen Modellierung beinhaltet, dass die Werte bestimmter Parameter verändert werden können und die nachfolgenden Schritte den neuen Werten entsprechend geändert werden. Bei schwerwiegenden Änderungen kann das Modell jedoch aufgrund des [Problem der topologischen Benennung](topological_naming_problem/de.md) brechen. Der Bruch kann minimiert werden, wenn die folgenden Konstruktionsprinzipien berücksichtigt werden:

-   Es sollte vermieden werden, Skizzen und eigene Bezugselementen an generierte Geometrie, d.h. jede Fläche, Kante oder Knoten des Festkörpers des Modells, anzuhängen. Stattdessen sollten sie an Hauptebenen oder -achsen befestigt werden. Skizzen oder Bezugselemente, die an diese Hauptebenen oder -achsen befestigt werden, werden nicht unerwartet an andere Referenzen befestigt; falls nötig, Befestigungsversatzwerte anpassen.
-   Eine \"Hauptskizze\" (Master-Sketch) verwenden. Da eine Hauptskizze vor dem Rest des Modells angelegt wird, kann sie sich nur auf die Hauptebenen oder -achsen beziehen.
    -   Eine Hauptskizze sollte so einfach wie möglich sein und grundlegende geometrische Elemente des Modells enthalten.
    -   Elemente der Hauptskizze können beim Modellieren nachfolgender Formelemente referenziert werden.
    -   Eine Hauptskizze kann die erste Skizze im Körper sein oder sich gänzlich außerhalb des Körpers befinden. Im ersten Fall kann sie direkt als externe Geometrie referenziert werden, im anderen Fall über einen <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [Formbinder](PartDesign_ShapeBinder/de.md) or <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [Teilformbinder](PartDesign_SubShapeBinder/de.md).
-   FormBinder nicht aus generierter Geometrie erstellen. Nicht vergessen, dass (Teil-)Formbinder ein Problem darstellen können, wenn Geometrie aus der Skizze, auf der sie basieren, gelöscht wird.
-   Es sollte immer zuerst versucht werden, auf eine Skizze oder auf Skizzenelemente zu referenzieren, anstatt auf generierte Geometrie. Ist man gezwungen auf generierte Geometrie zu referenzieren, sollte das erste Formelement verwendet werden, das das benötigte Element enthält. Änderungen durch spätere Schritte werden das Modell dann nicht zerstören.
-   *Modifikationen* wie Verrundungen und Fasen so spät wie möglich im Modellbaum einsetzen.



## Anleitungen

Die Seite [Tutorien](Tutorials/de.md) enthält einige Beispiele für die Anwendung der Feature-Editing-Methode des Arbeitsbereichs [PartDesign](PartDesign_Workbench/de.md).

-   [Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)
-   [Grundlegende PartDesign-Anleitung 0.19](Basic_Part_Design_Tutorial_019/de.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial/de.md)



## Verwandtes

-   [Konstruktive Festkörpergeometrie](Constructive_solid_geometry/de.md)


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/de
