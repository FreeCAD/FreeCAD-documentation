---
- GuiCommand:/de
   Name:PartDesign ShapeBinder
   Name/de:PartDesign FormBinder
   MenuLocation:Part Design → Einen Formbinder erstellen
   Workbenches:[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign UnterFormBinder](PartDesign_SubShapeBinder/de.md),[PartDesign Klon](PartDesign_Clone/de.md)
---

# PartDesign ShapeBinder/de

## Beschreibung


<div class="mw-translate-fuzzy">

Erzeugt einen Bezug **Formbinder** von einem ausgewählten Körper innerhalb des aktiven Körpers. Ein Formbinder ist ein Referenzobjekt, das mit Kanten oder Flächen eines anderen Körpers verknüpft ist. Es kann auch verwendet werden, um eine Skizze von einem Körper zu einem anderen Körper zu verknüpfen. Das Formbinderobjekt wird in der 3D Ansicht als durchscheinendes Gelb in der [3D Ansicht](3D_view/de.md) dargestellt.


</div>

Anwendungsbeispiele sind der Bau eines Gehäuses mit passendem Deckel in zwei verschiedenen Körpern oder die Fertigung von Löchern, die zwischen verschiedenen Körpern ausgerichtet sind.

<img alt="" src=images/Shapebinder_tree.png ) ![](images/Shapebinder_flow.png  style="width:600px;"> 
*Zwei Formen aus Body.Pad004 werden ausgewählt und ihre Bezugsobjekte sind nun in Body001.Sketch005 als Außengeometrie über Body001.ShapeBinder verfügbar.*

## Anwendung


<div class="mw-translate-fuzzy">

Allgemeine Anwendung:

1.  [Aktiviere den Körper](PartDesign_Body/de#Active_status.md), der das Formbinderobjekt bekommen soll.
2.  Drücke die **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Erzeuge einen Formbinder](PartDesign_ShapeBinder/de.md)** Schaltfläche
3.  Drücke entweder die **Objekt** Taste oder die **Geometrie hinzufügen** Taste.
4.  Wähle in der [3D Ansicht](3D_view/de.md) das zu kopierende Objekt oder die Geometrie aus. *Objekt* wählt den ganze Körper aus;*Geometrie hinzufügen* wählt jedes beliebige Element (Knoten, Kante, Fläche).
5.  Um die ausgewählte Geometrie zu entfernen, drücke die **Geometrie entfernen** Taste und wähle die Geometrie in der [3D Ansicht](3D_view/de.md) aus. Um den Vorgang abzubrechen, drücke die Taste erneut.
6.  Alternativ kann der zu kopierende Körper vor dem Start des Formbinder Befehls ausgewählt werden.
7.  Drücke **OK**.


</div>

**Beispiel**

:   Das Beispiel verwendet die FormBinder Funktion, um ein Loch (mit oder ohne Gewinde) durch mehr als einen Körper zu bohren. Normalerweise ist die Lochfunktion des Arbeitsbereichs Part Design auf einen einzigen Körper beschränkt. Das Beispiel verwendet zwei Würfel, die sich gegenüberliegen, aber willkürlich falsch ausgerichtet sind. Die Löcher werden mit Skizzen erstellt, die für jedes Loch einen Kreis enthalten (der Durchmesser wird von der Lochfunktion ignoriert). Wenn du die Skizze in den anderen Würfel kopierst, befindet sie sich an der gleichen Position im lokalen Würfelkoordinatensystem. Im Bild ist dies durch den weißen Kreis auf dem Rückwürfel dargestellt. Das ist nicht das, was wir wollen, denn das Loch an dieser Stelle würde nicht auf das Loch im vorderen Würfel ausgerichtet sein.





:   

    :   ![](images/ShapeBinderThroughHole.png )
    :   *Beispiel Aufbau für die Darstellung von wie man Löcher durch verschiedene Körper erstellt. Der weiße Kreis zeigt, dass das Kopieren von Skizzen nicht ausreicht*.


<div class="mw-translate-fuzzy">

So nutzt Du die Formbinder Funktion, um dies zu erreichen:

1.  Bereite ein Szenario gemäß dem obigen Bild vor. Wenn du die Würfel aus der [Part Arbeitsbereich](Part_Workbench/de.md) verwendest, denk daran, dass du sie in einen \"Körper\" Behälter (Body) stecken musst. Jeden einzelnen in einen eigenen. Andernfalls würden die Funktionen [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) nicht funktionieren. Wenn du sie nach Skizzen erstellst, sollte das System standardmäßig einen Körperbehälter erstellen.
2.  Wähle den EigenschaftenDialog/Datenreiter, um den zweiten Würfel mit einer Seitwärtsverschiebung so zu bewegen, dass er den ersten Würfel berührt.
3.  Wähle den PartDesign Arbeitsbereich aus
4.  erstelle eine Skizze auf der Vorderseite des ersten Würfels und platziere einen Kreis an beliebiger Stelle und schließe die Skizze.
5.  Vergewissere dich, dass der erste Körper der aktive Körper ist (Doppelklick). Wähle die Skizze im Baum aus und drücke die [Bohrung](PartDesign_Hole/de.md)-Funktion.
6.  Wähle eine Bohrung in passenden Größe aus. Im Bild oben war auch eine Senkbohrung ausgewählt. Schließe die Funktion [Bohrung](PartDesign_Hole/de.md).

\#:Jetzt sollte das Bild wie oben aussehen. Wenn Du den ersten Würfel ausblendest (wähle und drücke die Leertaste), kannst Du sehen, dass die Bohrung den zweiten Würfel nicht erreicht. Das wird es nicht, auch wenn Du \"Durch Alles\" oder einen wirklich großen Abstand im Dialogfenster [Hole](PartDesign_Hole/de.md) wählst. Der Lochdialog ist immer auf einen einzigen Körper beschränkt.

\#: Hier kommt nun unser Formbinder ins Spiel.

1.  Wähle zuerst den hinteren Würfel aus. Dies ist das Ziel, an das der Formbinder angefügt wird. Er muss aktiviert sein, also vergewissere Dich, dass er doppelt angeklickt wurde.
2.  Wähle die Skizze im Baum aus, die wir für die Bohrung verwendet haben. Es ist wichtig, den ersten Körper nicht zu aktivieren.
3.  Wähle die Formbinder Funktion.

#: Ein Dialog sollte sich öffnen. In der Zeile "Objekt" sollte der Name unserer Skizze sichtbar sein. Wenn du die Funktion ohne Auswahl der Skizze ausgewählt hattest, könntest du "Objekt" drücken und dann die Skizze aus der Liste auswählen. Es ist empfehlenswert, das Objekt vorher auszuwählen, um das richtige zu erhalten, besonders wenn du viele Skizzen mit automatisch generierten Namen hast Sketch001,.. Die "Geometrie hinzufügen" ist für uns nicht sinnvoll, da wir die ganze Skizze auswählen wollen.  "Geometrie hinzufügen" wird verwendet, wenn nur Teile ausgewählt werden sollen.

1.  Drücke **OK**, um die Skizzenfunktion zu schließen und überprüfe, ob ein neues Element zum Baum wenn des zweite Würfels hinzugefügt wurde.

    :   Wenn du die Sichtbarkeit des Formbinders umschaltest, wird er in der [3D Ansicht](3D_view/de.md) gelb dargestellt. Allerdings ist er an der falschen Position, so wie der weiße Kreis im Bild oben. Dies liegt an der Standardeinstellung für den Trace Parameter.
2.  Setze in der Eigenschaftsansicht des Formbinders im Datenreiter den Parameter **Trace Support** auf true. Die Voreinstellung war false.

    :   Mit **Trace Support**\' true wird der Formbinder nicht von lokalen Transformationen des Zielkörpers beeinflusst, z.B. unseren Übersetzungen. Die Form bleibt genau dort, wo die ursprüngliche vordere Objektform gewesen ist. Versuche, das vordere Objekt zu bewegen, und Du siehst, dass der Formbinder immer an die neue Position folgt.
    :   Leider können wir den Formbinder nicht für eine [Bohrung](PartDesign_Hole/de.md) auswählen. Dazu erstellen wir eine lokale Skizze und verwenden diese für unsere Bohrung im zweiten Würfel.
3.  Wähle die Vorderseite des hinteren Würfels aus und erstelle eine neue Skizze (klicke OK für den Vorschlag im Dialog).
4.  Mache die gesamte Geometrie unsichtbar und den Formbinder sichtbar. Nun kannst Du die äußere

Geometriefunktion verwenden und den Kreis im Formbinder auswählen. Wir benötigen den Mittelpunkt dieses Kreises.

1.  Erstelle einen neuen Kreis und setze ihn in den Mittelpunkt des Formbinder Kreises. Der Radius ist nicht wichtig. Die Funktion [Bohrung](PartDesign_Hole/de.md) verwendet nur die Mittelpunkte der Kreise (Hinweis: Einzelpunkte werden von der Bohrungsfunktion ignoriert, wir müssen Kreise verwenden).
2.  Schließe die Skizze und klicke [Bohrung](PartDesign_Hole/de.md). Stelle den Dialog auf die gleichen Werte wie bei ersten Bohrung und drücke OK.


</div>


<div class="mw-translate-fuzzy">

Erledigt.

:   Jetzt hast du zwei verbundene Bohrungen in zwei verschiedenen Körpern. Wenn Du die Geometrie oder die Positionen der Bohrungen änderst, werden beide Bohrungen angepasst. Nur wenn Du eine neuee Bohrung hinzufügst, musst Du die Skizze im zweiten Würfel für die zweite Bohrung aktualisieren.


</div>


<div class="mw-translate-fuzzy">


:   Anmerkungen
:   dass es eine andere Möglichkeit gibt, einen FormBinder zu erstellen: mit aktiviertem hinteren Würfel klicke auf die Vorderseite des vorderen Würfels und erstelle eine neue Skizze. Ein Dialog wird aufklappen, in dem du \"Abhängige Skizze\" auswählst. Dadurch entsteht tatsächlich ein Formbinder. Du kannst den Parameter von *\'Nachverfolgungsunterstützung* im Eigenschaftsfenster sehen. Es ist ein paar Klicks weniger als unser Verfahren.
:   Beachte auch, dass die Arbeit mit FormBinder mit Skizzen nur eine Teilmenge seiner Möglichkeiten ist. Es ist auch möglich, Teile der 3D Geometrie zu verwenden, wie im obigen Beispiel gezeigt.


</div>

## Optionen

Doppelklicke auf die FormBinder Beschriftung im [Modellbaum](Tree_view/de.md) oder rechtsklicke und wähle **FormBinder bearbeiten** im Kontextmenü, um die Parameter zu bearbeiten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Label}}: Name, der dem Objekt gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    {{PropertyData/de|Trace Support}}: Wenn diese Option auf true gesetzt ist, überwacht der Formbinder die relative Platzierung der Teile und Körper. Standardeinstellung ist false. Siehe das obige Beispiel, wie dies verwendet wird und funktioniert {{Version/de|0.18}}.


</div>

## Begrenzungen


<div class="mw-translate-fuzzy">

-   Eine Mehrfachauswahl wird nicht unterstützt. Die Geometrie hinzufügen und Geometrie entfernen Tasten müssen für jede einzelne Auswahl gedrückt werden.

Es gibt eine Übergangslösung für die Mehrfachauswahl: Wenn du alle Elemente auswählst, die du vorher beim Erstellen des FormBinders haben möchtest, erscheinen sie in der Startliste.

-   Ein Formbinder kann nicht als Basismerkmal dienen.
-   Ausgewählte Geometrie auf einem Körper muss zusammenhängend sein.
-   Wenn vor dem Start des Befehls zuerst der zu kopierende Körper ausgewählt wird oder wenn die Schaltfläche **Object** verwendet wird, ist es nicht mehr möglich, nur bestimmte Geometrieelemente auszuwählen.
-   Die relative Platzierung des Zielkörpers und des kopierten Körpers wird nicht berücksichtigt. Der Formbinder übernimmt die gleichen internen Koordinaten wie der kopierte Körper. Seit der Version 0.18 gibt es eine neue Eigenschaft \"Nachverfolgungs Unterstützung\", um dieses Verhalten so zu ändern, dass die relativen Platzierungen berücksichtigt werden.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/de
