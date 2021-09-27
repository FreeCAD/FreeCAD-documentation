# Topological naming problem/de
## Einleitung


{{TOCright}}

Das _ erstellt und diese mit der <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) dimensioniert werden.

-   Wenn in <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) ein Merkmal auf einer Fläche (oder Kante oder Scheitelpunkt) unterstützt wird, kann das Merkmal brechen, wenn der zugrunde liegende Volumenkörper seine Größe oder Ausrichtung ändert, da die ursprüngliche Fläche (oder Kante oder Scheitelpunkt) intern umbenannt werden kann.
-   Wenn in <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) eine Dimension die Länge einer projizierten Kante misst, kann die Dimension brechen, wenn das 3D-Modell geändert wird, da die Knoten umbenannt werden können, wodurch die gemessene Kante geändert wird.

Der Sachverhalt der topologischen Benennung ist ein komplexes Problem bei der CAD Modellierung, das daraus herrührt, wie die internen FreeCAD Routinen Aktualisierungen der mit dem [OCCT Kernel](OpenCASCADE/de.md) erstellten geometrischen Formen handhaben. Ab FreeCAD 0.19 gibt es kontinuierliche Bemühungen, die Kernverarbeitung von Formen zu verbessern, um solche Probleme zu reduzieren oder zu beseitigen.

-   Forumsbeitrag: [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278)

Das Problem der topologischen Benennung betrifft und verwirrt neue Anwender von FreeCAD am häufigsten. In PartDesign wird dem Anwender empfohlen, die auf der Seite [Funktionsbearbeitung](feature_editing/de.md) beschriebenen optimalen Vorgehensweisen zu befolgen. Die Verwendung von unterstützenden Bezugsobjekten wie [Ebenen](PartDesign_Plane/de.md) und [local coordinate systems](PartDesign_CoordinateSystem/de.md) wird dringend empfohlen, Modelle zu erstellen, die nicht leicht solchen topologischen Fehlern ausgesetzt sind. In TechDraw wird dem Anwender empfohlen, Bemaßungen nur dann hinzuzufügen, wenn das 3D-Modell vollständig ist und nicht mehr geändert wird.

## Beispiel

1\. Erstelle in der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> _, verwende dann <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> _ aus, um einen ersten Volumenkörper zu erstellen.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Wählen Sie die Oberseite des vorherigen Volumenkörpers aus und verwende dann <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign NewSketch](PartDesign_NewSketch/de.md), um eine weitere Skizze zu zeichnen; führe dann ein zweites Polster aus.

  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;">
  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

3\. Wähle die Oberseite der vorherigen Extrusion aus und erstelle erneut eine Skizze und ein Polster.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Doppelklicke nun auf die zweite Skizze und ändere sie so, dass ihre Länge entlang der X-Richtung liegt; dadurch wird das zweite Pad neu erstellt. Die dritte Skizze und das Polster bleiben an der gleichen Stelle.

  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;">
  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Doppelklicke nun erneut auf die zweite Skizze und passe Deine Punkte so an, dass ein Teil davon außerhalb der durch das erste Pad definierten Grenzen liegt. Dadurch wird das zweite Pad korrekt neu berechnet, aber beim Betrachten der [Baumansicht](tree_view/de.md) wird im dritten Pad ein Fehler angezeigt.

  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;">
  ----------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Indem man die dritte Skizze und das Polster sichtbar macht, wird deutlich, dass die Berechnung des neuen Solids nicht korrekt durchgeführt wurde. Die dritte Skizze, anstatt von der Oberseite des zweiten Pads getragen zu werden, erscheint an einer seltsamen Stelle, mit ihrer Normalen, die in X Richtung ausgerichtet ist. Dies führt zu einem ungültigen Polster, da dieses Polster vom Rest des <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Körper](PartDesign_Body/de.md) getrennt wird, was nicht erlaubt ist.

Das Problem scheint darin zu bestehen, dass bei der Änderung der zweiten Skizze die Oberseite des zweiten Polsters von `Face13` in `Face14` umbenannt wurde. Die dritte Skizze ist wie ursprünglich an `Face13` angehängt, aber da sich diese Fläche nun auf der Seite befindet (nicht oben), folgt die Skizze ihrer Ausrichtung und ist nun falsch positioniert.

  --------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;">
  --------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------

7\. Um das Problem zu beheben, sollte die dritte Skizze wieder auf die Oberseite abgebildet werden. Wähle die Skizze aus, klicke auf die Ellipse (drei Punkte) neben der Eigenschaft {{PropertyData/de|Map Mode}}, und wähle erneut die Oberseite des zweiten Polsters. Dann geht die Skizze an die Spitze des vorhandenen Volumenkörpers, und das dritte Pad wird ohne Probleme erzeugt.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

  --------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;">
  --------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

Die Umschlüsselung einer Skizze auf diese Weise kann bei jedem topologischen Benennungsfehler erfolgen, dies kann jedoch mühsam sein, wenn das Modell kompliziert ist und es viele solcher Skizzen gibt, die angepasst werden müssen.

## Lösung

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

Der [Abhängigkeitsgraph](Std_DependencyGraph/de.md) ist ein Werkzeug, das hilfreich ist, um die Beziehungen zwischen den verschiedenen Körpern im Dokument zu beobachten. Die Verwendung des ursprünglichen Modellierungs Arbeitsablaufs zeigt die direkte Beziehung, die zwischen den Skizzen und den Polstern besteht. Wie eine Kette ist es leicht zu erkennen, dass diese direkte Abhängigkeit mit topologischen Benennungsproblemen behaftet sein wird, wenn sich eines der Glieder in der Reihenfolge ändert.

Wie auf der Seite [\|Merkmals Bearbeitung](feature_editing/de.md) erläutert, besteht eine Lösung für dieses Problem darin, Skizzen nicht auf Flächen, sondern auf Bezugsebenen zu stützen, die von den Hauptebenen der [PartDesign Körper](PartDesign_Body/de.md) Ursprungs versetzt sind.

1\. Wähle den Ursprung des [PartDesign Body](PartDesign_Body/de.md) und stelle sicher, dass er sichtbar ist. Wähle dann die XY-Ebene aus und klicke auf [PartDesign Fläche](PartDesign_Plane/de.md). Gib im Anhang des Dialogfelds für den Versatz einen Versatz in Z-Richtung an, so dass die Bezugsebene koplanar mit der Oberseite des ersten Polsters ist.

2\. Wiederhole den Vorgang, füge aber diesmal einen größeren Versatz hinzu, so dass die zweite Bezugsebene koplanar mit der Oberseite der zweiten Auflage ist.




  --------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;">
  --------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------

3\. Wähle die zweite Skizze aus, klicke auf die Ellipse nahe der {{PropertyData/de|Map Mode}} Eigenschaft und wähle dann die erste Bezugsebene. Die Bezugsebene ist bereits von der XY-Ebene des Körpers versetzt, so dass für die Skizze kein weiterer Z-Versatz erforderlich ist.

4\. Wiederhole den Vorgang mit der dritten Skizze und wähle die zweite Bezugsebene als Auflage. Auch hier ist kein weiterer Z-Offset erforderlich.

5\. Das Abhängigkeitsdiagramm zeigt nun, dass die Skizzen und Polster von den Bezugsebenen unterstützt werden. Dieses Modell ist stabiler, da jede Skizze im Wesentlichen unabhängig voneinander modifiziert werden kann.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Doppelklicke auf die zweite Skizze und ändere die Form. Das zweite Polster sollte sofort aktualisiert werden, ohne topologische Probleme mit der dritten Skizze und dem dritten Polster zu verursachen.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. Tatsächlich kann jede Skizze geändert werden, ohne die Polster der anderen zu beeinträchtigen. Solange die Polster eine ausreichende Extrusionslänge haben, so dass sie sich berühren und einen zusammenhängenden Körper bilden, ist der gesamte Körper gültig.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Schlussbemerkungen

Das Hinzufügen von Bezugsobjekten ist mehr Arbeit für den Anwender, erzeugt aber letztlich stabilere Modelle, die weniger dem topologischen Benennungsproblem unterliegen.

Natürlich können Bezugsobjekte erstellt werden, bevor Skizzen gezeichnet werden, und es werden Polster erstellt. Dies kann hilfreich sein, um die ungefähre Form und Dimension des Endkörpers zu visualisieren.

Bezugsflächen können auch auf anderen Bezugsflächen basieren. Dies schafft eine Kette von Abhängigkeiten, die auch zu topologischen Problemen führen können; da es sich bei Bezugsebenen jedoch um sehr einfache Objekte handelt, ist das Risiko, dass diese Probleme auftreten, geringer, als wenn die Fläche eines festen Objekts als Träger verwendet wird.

Bezugsobjekte, [Punkte](PartDesign_Point/de.md), [Linien](PartDesign_Line/de.md), [Flächen](PartDesign_Plane/de.md) und [Koordinatensysteme](PartDesign_CoordinateSystem/de.md), können auch als Referenzgeometrie, d.h. als visuelle Hilfsmittel zur Darstellung der wichtigen Merkmale im Modell nützlich sein, auch wenn keine Skizze direkt an ihnen angebracht ist.

## Verweise

-   [PartDesign Verrundung - Topologische Benennung](PartDesign_Fillet/de#Topological_naming.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278) , eine mögliche Lösung, von realthunder.
-   [Benennungsprojekt](Naming_project/de.md): Bemühung, eine robuste topologische Benennung in FreeCAD zu implementieren.
-   [Topologisches Benennungsprojekt](Topological_Naming_Project/de.md): Idee um das Problem zu lösen, von ickby.
-   [Topologisches Datenskripten](Topological_data_scripting/de.md)
-   [Funktionsbearbeitung](Feature_editing/de.md): enthält alternative Hinweise für stabile Modellierungstechniken.

## Videos


<div class="mw-translate-fuzzy">

-   _


</div>


 {{TechDraw Tools navi}} {{PartDesign Tools navi}} 

_

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Topological naming problem/de
