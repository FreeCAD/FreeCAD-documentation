---
- GuiCommand   */de
   Name   *PartDesign ShapeBinder
   Name/de   *PartDesign FormBinder
   MenuLocation   *Part Design → Formbinder erstellen
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   Version   *0.17
   SeeAlso   *[PartDesign UnterFormBinder](PartDesign_SubShapeBinder/de.md),[PartDesign Klon](PartDesign_Clone/de.md)
---

# PartDesign ShapeBinder/de

## Beschreibung


<div class="mw-translate-fuzzy">

Erzeugt einen **Formbinder**-Bezug innerhalb des aktiven Körpers. Ein Formbinder ist ein Bezugsobjekt, das mit Kanten oder Flächen eines anderen Körpers verknüpft ist. Es kann auch verwendet werden, um eine Skizze von einem Körper zu einem anderen Körper zu verknüpfen. Das Formbinderobjekt wird in der 3D Ansicht als durchscheinendes Gelb in der [3D-Ansicht](3D_view/de.md) dargestellt.


</div>

A ShapeBinder will track the relative placement of the referenced geometry, which is useful in the context of creating [assemblies](Assembly.md), if its **Trace Support** property is set to {{True}}. See the [Example](#Example.md) below to understand how this works.

The referenced geometry can either be a single object (for example a [Part Box](Part_Box.md), a [PartDesign Body](PartDesign_Body.md), or a [sketch](PartDesign_NewSketch.md) or [Feature](PartDesign_Feature.md) inside a Body), or one or more subelements (faces, edges or vertices) belonging to the same parent object. Which geometry should be selected depends on the intended purpose of the ShapeBinder. For a Boolean operation you would need to select a solid. For a Pad operation a face or a sketch can be used. And for the external geometry in a sketch, or to attach a sketch, any combination of subelements may be appropriate. The referenced geometry can also belong to the Body the ShapeBinder is nested in.

<img alt="" src=images/Shapebinder_flow.png  style="width   *600px;">


<div class="mw-translate-fuzzy">



*Zwei Formen aus Body.Pad004 werden ausgewählt und ihre Bezugsobjekte sind nun in Body001.Sketch005 als Außengeometrie über Body001.ShapeBinder verfügbar.*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  [Aktiviere den Körper](PartDesign_Body/de#Active_status.md), der das Formbinderobjekt bekommen soll.
2.  Klicke auf die **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Formbinder erstellen](PartDesign_ShapeBinder/de.md)** Schaltfläche.
3.  Klicke entweder auf die **Objekt**-Schaltfläche oder die **Geometrie hinzufügen**-Schaltfläche.
4.  Wähle in der [3D Ansicht](3D_view/de.md) das zu kopierende Objekt oder die Geometrie aus. *Objekt* wählt den ganze Körper aus;*Geometrie hinzufügen* wählt das hervorgehobene, geometrische Element, z.B. Knoten, Kante oder Fläche aus.
5.  Um eine Geometrie zu entfernen, klicke auf die **Geometrie entfernen**-Schaltfläche und wähle die Geometrie in der [3D Ansicht](3D_view/de.md) aus.
6.  Alternativ können geometrische Elemente in der [3D Ansicht](3D_view/de.md) ausgewählt werden, bevor die Formbinderfunktion gestartet wird.
7.  Klicke auf die **OK**-Schaltfläche.

Um die Durchführung, die mit einem Klick auf eine Schaltfläche gestartet wurde zu stoppen, muss noch einmal auf die Schaltfläche geklickt werden.


</div>

## Optionen


<div class="mw-translate-fuzzy">

Doppelklicke auf die FormBinder Beschriftung im [Modellbaum](Tree_view/de.md) oder rechtsklicke und wähle **FormBinder bearbeiten** im Kontextmenü, um die Parameter zu bearbeiten.


</div>

## Notes

-   A ShapeBinder can be dragged out of the Body it is nested in, and dropped onto the <img alt="" src=images/Document.svg  style="width   *16px;"> document node in the [Tree view](Tree_view.md). Such an unnested ShapeBinder can be used as the [Base Feature](PartDesign_Body#Base_Feature.md) for a new Body.
-   A ShapeBinder created from a sketch can have an opposite \"tool direction\". For example a [Pad](PartDesign_Pad.md) created from the sketch may extend in the +Y direction, while a [Pad](PartDesign_Pad.md), with the same properties, created from the ShapeBinder extends in the -Y direction. Toggling the **Reversed** property (or checkbox) will solve this.

## PartDesign SubShapeBinder vs. PartDesign ShapeBinder 

See [PartDesign SubShapeBinder](PartDesign_SubShapeBinder#PartDesign_SubShapeBinder_vs._PartDesign_ShapeBinder.md).

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Label}}   * Name, der dem Objekt gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    {{PropertyData/de|Trace Support}}   * Der vorgegebene Wert ist false. Wenn diese Option auf true gesetzt ist, überwacht der Formbinder die relative Positionierung der Teile und Körper durch Änderung der Werte seiner {{PropertyData/de|Placement}}-Eigenschaften. Siehe das obige Beispiel, wie dies verwendet wird und funktioniert.


</div>

## Example


<div class="mw-translate-fuzzy">

**Beispiel**

   *   Das Beispiel verwendet die FormBinder Funktion, um ein Loch (mit oder ohne Gewinde) durch mehr als einen Körper zu bohren. Normalerweise ist die Lochfunktion des Arbeitsbereichs Part Design auf einen einzigen Körper beschränkt. Das Beispiel verwendet zwei Würfel, die sich gegenüberliegen, aber willkürlich versetzt ausgerichtet sind. Die Löcher werden mit Skizzen erstellt, die für jedes Loch einen Kreis enthalten. Der Durchmesser wird von der Lochfunktion ignoriert. Wenn du die Skizze in den anderen Würfel kopierst, befindet sie sich an der gleichen Position im lokalen Würfelkoordinatensystem. Im Bild ist dies durch den weißen Kreis auf dem rückwärtigen Würfel dargestellt. Das ist nicht das, was wir wollen, denn das Loch an dieser Stelle würde nicht auf das Loch im vorderen Würfel ausgerichtet sein.


</div>

![](images/ShapeBinderThroughHole.png )


<div class="mw-translate-fuzzy">


   *   

       *   ![](images/ShapeBinderThroughHole.png )
       *   *Beispiel Aufbau für die Darstellung von wie man Löcher durch verschiedene Körper erstellt. Der weiße Kreis zeigt, dass das Kopieren von Skizzen nicht ausreicht*.


</div>


<div class="mw-translate-fuzzy">

So nutzt Du die Formbinder Funktion, um dies zu erreichen   *

1.  Bereite ein Szenario gemäß dem obigen Bild vor. Wenn du die Würfel aus der [Part Arbeitsbereich](Part_Workbench/de.md) verwendest, denk daran, dass du sie in einen \"Körper\" Behälter (Body) stecken musst. Jeden einzelnen in einen eigenen. Andernfalls würden die Funktionen [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) nicht funktionieren. Wenn du sie nach Skizzen erstellst, sollte das System standardmäßig einen Körper erstellen.
2.  Im Reiter Eigenschaften im Diaglog den zweiten Würfel mit einer Seitwärtsverschiebung so bewegen, dass er den ersten Würfel berührt.
3.  Wähle den PartDesign Arbeitsbereich aus.
4.  Erstelle eine Skizze auf der Vorderseite des ersten Würfels und erstelle einen Kreis an beliebiger Stelle darauf und schließe die Skizze.
5.  Vergewissere dich zuerst, dass der erste Körper der [Aktive Körper](PartDesign_Body#Active_status.md) ist (Doppelklick). Wähle die Skizze in der Baumansicht und klicke auf die [Bohrung](PartDesign_Hole/de.md)-Schaltfläche.
6.  Wähle eine Bohrung in passenden Größe aus. Im Bild oben war auch eine Senkbohrung ausgewählt. Schließe die Funktion [Bohrung](PartDesign_Hole/de.md).

       *   Jetzt sollte das Bild wie oben aussehen. Wenn Du den ersten Würfel wählst und mit der Leertaste ausblendest, kannst Du sehen, dass die Bohrung den zweiten Würfel nicht erreicht. Das wird es auch dann nicht, wenn Du \"Durch Alles\" wählst oder einen wirklich großen Abstand im Dialogfenster [Bohrung](PartDesign_Hole/de.md) wählst. Der Bohrung-Dialog ist immer auf einen einzigen Körper beschränkt.
       *   Hier kommt nun unser Formbinder ins Spiel.
7.  Wähle zuerst den hinteren Würfel mit einem Doppelklick aus. Dies ist das Ziel, an das der Formbinder angefügt wird. Er muss vorher [aktiviert](PartDesign_Body#Active_status.md) sein. Vergewissere Dich, dass er doppelt angeklickt wurde.
8.  Wähle in der Baumansicht die Skizze aus, die wir für die Bohrung verwendet haben. Es ist wichtig, den ersten Körper nicht zu aktivieren.
9.  Wähle die Formbinder Funktion.

       *   Ein Dialog sollte sich öffnen. In der Zeile \"Objekt\" sollte der Name unserer Skizze sichtbar sein. Wenn du die Funktion ohne Auswahl der Skizze ausgewählt hattest, könntest du \"Objekt\" anklicken und dann die Skizze aus der Liste auswählen. Es empfielt sich, das erste in der Reihenfolge auszuwählen, um das richtige zu erhalten, besonders wenn du viele Skizzen mit automatisch generierten Namen hast Sketch001,.. \"Geometrie hinzufügen\" ist für uns nicht sinnvoll, da wir die ganze Skizze auswählen wollen. \"Geometrie hinzufügen\" wird verwendet, wenn nur Teile ausgewählt werden sollen.
10. Klicke auf die **OK**-Schaltfläche, um den Dialog zu schließen und überprüfe, ob ein neues Element zum Baum des zweiten Würfels hinzugefügt wurde.

       *   Wenn du die Sichtbarkeit des Formbinders umschaltest, wird er in der [3D-Ansicht](3D_view/de.md) gelb dargestellt. Allerdings ist er an der falschen Position, so wie der weiße Kreis im Bild oben. Dies liegt an der Standardeinstellung für den Trace Parameter.
11. Setze in der Eigenschaftsansicht des Formbinders im Datenreiter den Parameter **Trace Support** auf true. Die Voreinstellung war false.

       *   Mit **Trace Support**\' true wird der Formbinder nicht von lokalen Transformationen des Zielkörpers beeinflusst, z.B. unseren Übersetzungen. Die Form bleibt genau dort, wo die ursprüngliche vordere Objektform gewesen ist. Versuche, das vordere Objekt zu bewegen, und Du siehst, dass der Formbinder immer an die neue Position folgt.
       *   Leider können wir den Formbinder nicht für eine [Bohrung](PartDesign_Hole/de.md) auswählen. Dazu erstellen wir eine lokale Skizze und verwenden diese für unsere Bohrung im zweiten Würfel.
12. Wähle die Vorderseite des hinteren Würfels aus und erstelle eine neue Skizze. Klicke auf die **OK**-Schaltfläche für den Vorschlag im Dialog.
13. Mache die gesamte Geometrie unsichtbar und den Formbinder sichtbar. Nun kannst Du die äußere Geometriefunktion verwenden und den Kreis im Formbinder auswählen. Wir benötigen den Mittelpunkt dieses Kreises.
14. Erstelle einen neuen Kreis und setze ihn in den Mittelpunkt des Formbinderkreises. Der Radius ist nicht wichtig. Die Funktion [Bohrung](PartDesign_Hole/de.md) verwendet nur die Mittelpunkte der Kreise (Hinweis   * Einzelpunkte werden von der Bohrungsfunktion ignoriert, wir müssen Kreise verwenden).
15. Schließe die Skizze und klicke auf [Bohrung](PartDesign_Hole/de.md). Stelle den Dialog auf die gleichen Werte wie bei der ersten Bohrung und drücke OK.


</div>





{{PartDesign_Tools_ navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/de
