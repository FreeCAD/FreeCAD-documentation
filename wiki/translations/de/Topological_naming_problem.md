# Topological naming problem/de
## Einleitung




Das [Problem der topologischen Benennung](topological_naming_problem/de.md) in FreeCAD bezieht sich auf die Frage, ob eine Form ihren internen Namen nach einer Modellierungsoperation (Polstern, Schnitt, Vereinigung, Fase, Verrundung, usw.) ändert. Dies führt dazu, dass andere parametrische Merkmale, die von dieser Form abhängen, brechen oder falsch berechnet werden. Dieser Sachverhalt betrifft alle Objekte in FreeCAD, ist aber besonders bemerkenswert, wenn Festkörper mit dem Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) erstellt und diese mit dem Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) bemaßt werden.

-   Wenn in <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) ein Merkmal auf einer Fläche (oder Kante oder Scheitelpunkt) unterstützt wird, kann das Merkmal brechen, wenn der zugrunde liegende Festkörper seine Größe oder Ausrichtung ändert, da die ursprüngliche Fläche (oder Kante oder Knoten) intern umbenannt werden kann.
-   Wenn in <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) ein Maß die Länge einer projizierten Kante anzeigt, kann das Maß brechen, wenn das 3D-Modell geändert wird, da die Knoten umbenannt werden können, wodurch die gemessene Kante geändert wird.

Das Problem der topologischen Benennung ist ein komplexes Problem bei der CAD-Modellierung, das daraus herrührt, wie die internen FreeCAD-Routinen Aktualisierungen der mit dem [OCCT-Kernel](OpenCASCADE/de.md) erstellten geometrischen Formen handhaben. Dieses Problem betrifft nicht nur FreeCAD. Es tritt in allen CAD-Anwendungen auf, aber die meisten anderen CAD-Anwendungen enthalten heuristische Methoden, die den Einfluss des Problems auf den Anwender reduzieren.

Seit FreeCAD 0.19 gibt es noch andauernde Entwicklungsanstrengungen, um den Kern im Umgang mit Formen zu verbessern, indem Methoden hinzugefügt werden, die den Einfluss dieser Probleme zu verringern. Der [Benennunngsalgorithmus](#Topological_naming_algorithm/de.md) ist ausgelegt, den manuellen Aufwand zu reduzieren, manchmal durch automatisches Beheben von Problemen, in andern Fällen durch Vorstellen einer wahrscheinlichen Lösung oder andernfalls wenigstens durch Aufzeigen, was das Problem verursachte. Die erste stabile Veröffentlichung von FreeCAD, die den neuen Benennungsalgorithmus beinhaltet ist die Version 1.0. Nach und nach wird dieser Algorithmus auf weitere Teile von FreeCAD übertragen und weitere Funktionen zum automatischen und angeleiteten Reparieren werden in späteren Versionen hinzugefügt.

Das Problem der topologischen Benennung betrifft und verwirrt neue Anwender von FreeCAD am häufigsten. In PartDesign wird dem Anwender empfohlen, die auf der Seite [Funktionsbearbeitung](feature_editing/de.md) beschriebenen optimalen Vorgehensweisen zu befolgen. Die Verwendung von unterstützenden Bezugsobjekten wie [Ebenen](PartDesign_Plane/de.md) und [lokalen Koordinatensystemen](PartDesign_CoordinateSystem/de.md) wird dringend empfohlen, um Modelle zu erstellen, die nicht leicht solchen topologischen Fehlern ausgesetzt sind. In TechDraw wird dem Anwender empfohlen, Maße nur dann hinzuzufügen, wenn das 3D-Modell vollständig ist und nicht mehr geändert wird.



## Beispiel

1\. Erstelle in der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Arbeitsbereich PartDesign](PartDesign_Workbench/de.md) einen <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Körper](PartDesign_Body/de.md), verwende dann <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign Neue Skizze](PartDesign_NewSketch/de.md) und wählen die XY-Ebene, um die Basisskizze zu zeichnen; führe dann ein <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Polster](PartDesign_Pad/de.md) aus, um einen ersten Volumenkörper zu erstellen.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Wählen Sie die Oberseite des vorherigen Volumenkörpers aus und verwende dann <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign NewSketch](PartDesign_NewSketch/de.md), um eine weitere Skizze zu zeichnen; führe dann ein zweites Polster aus.

+++
| <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;"> |
+++

3\. Wähle die Oberseite der vorherigen Extrusion aus und erstelle erneut eine Skizze und ein Polster.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Doppelklicke nun auf die zweite Skizze und ändere sie so, dass ihre Länge entlang der X-Richtung liegt; dadurch wird das zweite Pad neu erstellt. Die dritte Skizze und das Polster bleiben an der gleichen Stelle.

+++
| <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;"> |
+++

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Doppelklicke nun erneut auf die zweite Skizze und passe Deine Punkte so an, dass ein Teil davon außerhalb der durch das erste Pad definierten Grenzen liegt. Dadurch wird das zweite Pad korrekt neu berechnet, aber beim Betrachten der [Baumansicht](tree_view/de.md) wird im dritten Pad ein Fehler angezeigt.

+++
| <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;"> |
+++

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Indem man die dritte Skizze und das Polster sichtbar macht, wird deutlich, dass die Berechnung des neuen Solids nicht korrekt durchgeführt wurde. Die dritte Skizze, anstatt von der Oberseite des zweiten Pads getragen zu werden, erscheint an einer seltsamen Stelle, mit ihrer Normalen, die in X Richtung ausgerichtet ist. Dies führt zu einem ungültigen Polster, da dieses Polster vom Rest des <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Körper](PartDesign_Body/de.md) getrennt wird, was nicht erlaubt ist.

Das Problem scheint darin zu bestehen, dass bei der Änderung der zweiten Skizze die Oberseite des zweiten Polsters von `Face13` in `Face14` umbenannt wurde. Die dritte Skizze ist wie ursprünglich an `Face13` angehängt, aber da sich diese Fläche nun auf der Seite befindet (nicht oben), folgt die Skizze ihrer Ausrichtung und ist nun falsch positioniert.

+++
| <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;"> |
+++

7\. Um das Problem zu beheben, sollte die dritte Skizze wieder auf die Oberseite abgebildet werden. Wähle die Skizze aus, klicke auf die Ellipse (drei Punkte) neben der Eigenschaft {{PropertyData/de|Map Mode}}, und wähle erneut die Oberseite des zweiten Polsters. Dann geht die Skizze an die Spitze des vorhandenen Volumenkörpers, und das dritte Pad wird ohne Probleme erzeugt.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

+++
| <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;"> |
+++

Die Umschlüsselung einer Skizze auf diese Weise kann bei jedem topologischen Benennungsfehler erfolgen, dies kann jedoch mühsam sein, wenn das Modell kompliziert ist und es viele solcher Skizzen gibt, die angepasst werden müssen.



## Lösung

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

Der [Abhängigkeitsgraph](Std_DependencyGraph/de.md) ist ein Werkzeug, das hilfreich ist, um die Beziehungen zwischen den verschiedenen Körpern im Dokument zu beobachten. Die Verwendung des ursprünglichen Modellierungs Arbeitsablaufs zeigt die direkte Beziehung, die zwischen den Skizzen und den Polstern besteht. Wie eine Kette ist es leicht zu erkennen, dass diese direkte Abhängigkeit mit topologischen Benennungsproblemen behaftet sein wird, wenn sich eines der Glieder in der Reihenfolge ändert.

Wie auf der Seite [Formelemente bearbeiten](Feature_editing/de.md) erläutert, besteht eine Lösung für dieses Problem darin, Skizzen nicht an Flächen zu befestigen, sondern an die Hauptebenen des Ursprungs eines [PartDesign-Körpers](PartDesign_Body/de.md) oder an Bezugsebenen, die an diesen Hauptebenen befestigt sind. Es ist nicht nötig einzelne Skizzen, wie unten beschrieben, an Bezugsebenen zu befestigen, da die Skizze selbst direkt an einer Hauptebene befestigt werden kann und dieselben Versatzoptionen besitzt wie eine Bezugsebene. Bezugsebenen sind aber durchaus sinnvoll, wenn mehrere Skizzen positioniert werden.

1\. Wähle den Ursprung des [PartDesign Body](PartDesign_Body/de.md) und stelle sicher, dass er sichtbar ist. Wähle dann die XY-Ebene aus und klicke auf [PartDesign Fläche](PartDesign_Plane/de.md). Gib im Anhang des Dialogfelds für den Versatz einen Versatz in Z-Richtung an, so dass die Bezugsebene koplanar mit der Oberseite des ersten Polsters ist.

2\. Wiederhole den Vorgang, füge aber diesmal einen größeren Versatz hinzu, so dass die zweite Bezugsebene koplanar mit der Oberseite der zweiten Auflage ist.




+++
| <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;"> | <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;"> |
+++

3\. Wähle die zweite Skizze aus, klicke auf die Ellipse nahe der {{PropertyData/de|Map Mode}} Eigenschaft und wähle dann die erste Bezugsebene. Die Bezugsebene ist bereits von der XY-Ebene des Körpers versetzt, so dass für die Skizze kein weiterer Z-Versatz erforderlich ist.

4\. Wiederhole den Vorgang mit der dritten Skizze und wähle die zweite Bezugsebene als Auflage. Auch hier ist kein weiterer Z-Offset erforderlich.

5\. Das Abhängigkeitsdiagramm zeigt nun, dass die Skizzen und Polster von den Bezugsebenen unterstützt werden. Dieses Modell ist stabiler, da jede Skizze im Wesentlichen unabhängig voneinander modifiziert werden kann.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Doppelklicke auf die zweite Skizze und ändere die Form. Das zweite Polster sollte sofort aktualisiert werden, ohne topologische Probleme mit der dritten Skizze und dem dritten Polster zu verursachen.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. Tatsächlich kann jede Skizze geändert werden, ohne die Polster der anderen zu beeinträchtigen. Solange die Polster eine ausreichende Extrusionslänge haben, so dass sie sich berühren und einen zusammenhängenden Körper bilden, ist der gesamte Körper gültig.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Tradeoffs

Das Hinzufügen von Bezugsobjekten ist mehr Arbeit für den Anwender, erzeugt aber letztlich stabilere Modelle, die weniger dem topologischen Benennungsproblem unterliegen.

Natürlich können Bezugsobjekte erstellt werden, bevor Skizzen gezeichnet werden, und es werden Polster erstellt. Dies kann hilfreich sein, um die ungefähre Form und Dimension des Endkörpers zu visualisieren.

Bezugsflächen können auch auf anderen Bezugsflächen basieren. Dies schafft eine Kette von Abhängigkeiten, die auch zu topologischen Problemen führen können; da es sich bei Bezugsebenen jedoch um sehr einfache Objekte handelt, ist das Risiko, dass diese Probleme auftreten, geringer, als wenn die Fläche eines festen Objekts als Träger verwendet wird.

Bezugsobjekte, [Punkte](PartDesign_Point/de.md), [Linien](PartDesign_Line/de.md), [Flächen](PartDesign_Plane/de.md) und [Koordinatensysteme](PartDesign_CoordinateSystem/de.md), können auch als Referenzgeometrie, d.h. als visuelle Hilfsmittel zur Darstellung der wichtigen Merkmale im Modell nützlich sein, auch wenn keine Skizze direkt an ihnen angebracht ist.

## Topological naming algorithm 

Realthunder\'s topological naming algorithm, described in forum thread [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278), which was selected to reduce the impact of this problem, has been widely described as \"fixing the topological naming problem.\" This has unintentionally misled many users into thinking that it will no longer be helpful to use techniques like datums, explicit sketch placement, and [Feature editing](Feature_editing#Advice_for_creating_stable_models.md) to make models more stable. The algorithm is not intended to fix every failure introduced by topological naming ambiguity. Rather, it has three purposes.

1.  The first and most important purpose is, whenever possible, to **identify** broken references from topological changes and display an error to the user. Instead of having to work through a series of operations to find the first operation that diverges from the design intent, the operation that changes the names will normally be flagged with an error, making it much easier to manually fix model problems introduced by changes to operations or parameters.
2.  Sometimes, FreeCAD will be able to identify a **likely** fix for a broken reference, so that when the user is manually fixing up the flagged broken reference, a candidate will be presented for them to accept or change. A common example of this is dress-up operations like fillets and chamfers, where user might have to to edit the operation and either accept the proposed replacement feature selection or change it to correct it.
3.  In some cases, FreeCAD will be able to **automatically** resolve the broken reference, because enough information about the reference is stored to have high confidence that the replacement is correct. For example, when sketching directly on a face, the algorithm will frequently (but not always) correctly repair the reference to the face when the underlying geometry is changed parametrically. (When changing the structure, such as by adding or deleting operations in the middle of a Part Design Body, this kind of automatic repair will be less likely.) However, FreeCAD will do this only with high confidence in the correctness of the repair, because an incorrect automatic repair may re-introduce the problem of having to hunt for where a problem was introduced in order to repair a model after a modification. *First, do no harm.*

In FreeCAD 1.0, the implementation of this algorithm in the official FreeCAD release reached feature parity with Realthunder\'s \"Linkstage 3\" fork, where he originally developed the algorithm, as of the time the integration work started. There are new FreeCAD features that could use the algorithm but do not yet, and there will always be more opportunities to add candidate fixes and automatic repair. The initial work has provided a *framework* to use for these additional improvements over time, both in core FreeCAD and in Addons.



## Verweise

-   [PartDesign Verrundung - Topologische Benennung](PartDesign_Fillet/de#Topologische_Benennung.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278) , eine mögliche Lösung, von realthunder.
-   [Topological Naming Project](Topological_Naming_Project.md): Idee um das Problem zu lösen, von ickby.
-   [Topologische Daten skripten](Topological_data_scripting/de.md)
-   [Formelemente bearbeiten](Feature_editing/de.md): enthält alternative Hinweise für stabile Modellierungstechniken.
-   [Clarifying and expanding \"Topological Naming Problem\" documentation](https://forum.freecad.org/viewtopic.php?p=770360): Verdeutlicht die Erwartungen an Realthunders Algorithmus zum topologischen Benennen, der für FreeCAD 1.0 ausgewählt wurde.

## Videos

-   [Warum brechen meine FreeCAD Modelle? - \"Topologisches Benennungsproblem\"](https://youtu.be/6p2vqEEmWq4): Eine Videoerklärung der zugrunde liegenden Probleme des [Topologisches Benennungsproblem](Topological_naming_problem/de.md)
-   [FreeCAD Is Fundamentally Broken! - Now what\... Help Me Decide\...](https://www.youtube.com/watch?v=QSsVFu929jo): A Maker Tales Video


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/de
