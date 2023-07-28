# Sketcher Examples/de
{{TOCright}}



## Einleitung

Ich denke der Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) kann einige Beispiele gebrauchen, die nicht so detailliert sind wie Anleitungen oder Videos\...



## Filmscharnier

Ein Filmscharnier ist ein winziges Stück biegsamer Kunststoff, das die beiden Seiten eines Spritzgussobjekts, wie z.B. einen Kabelkanal mit einem Deckel oder die beiden Hälften einer Staubschutzkappe für einen Stecker.

Dieses Beispiel verwendet eine Art Master-Skizze, um darauf einige abhängige Skizzen aufzusetzen. Es zeigt auch, wie ein einfacher Klipp angefügt und animiert wird, der auf <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md)-Formelementen und <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md)-Randbedingungen basiert. Die Verwendung von <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [Ausdrücken](Expressions/de.md), wie unten beschrieben, erfordert FreeCAD ab **Version 0.21**.



### Basis-Skizze 

Normalerweise wird ein Objekt in geschlossenem Zustand konstruiert. Später wird der bewegliche Teil um 180° umgeklappt, um in offenem Zustand gespritzt zu werden.
Der biegsame Streifen wird im geschlossenen Zustand durch einen Kreisbogen dargestellt und im offenen Zustand durch eine gerade Linie; beide gehen vom gleichen Startpunkt aus.
Der Mittelpunkt der Linie, die beide Endpunkte verbindet, gibt die Lage der Achse an, um die geklappt wird, die normal auf der Skizzenebene steht. (Der Punkt wird im Skizzenursprung positioniert, so dass die globale Achse, die normal auf der Skizzen steht, als Achse zum Umklappen genutzt werden kann)


<div class="mw-collapsible mw-collapsed">

(Einige ausgeblendete zusätzliche Erklärungen und eine Beschreibung des Arbeitsablaufs können da drüben ausgeklappt werden \--\>

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:400px;"> 
*Master-Skizze und das animierte fertige Filmscharnier (Ein Klick auf das Bild, um die Animation anzusehen, falls sie nach einigen Wiederholungen gestoppt haben sollte)*


<div class="mw-collapsible-content toccolours">

Für einen Halbkreis ergibt sich die Bogenlänge aus dem Radius multipliziert mit Pi (**l = r \* Pi**). Der Radius wird mit NeutralerRadius benannt und die Linie mit GestreckteLänge. Ein Ausdruck (expression) für die GestreckteLänge verbindet beide Werte: `.Constraints.NeutralerRadius * pi`

:   Innerhalb derselben Skizze startet ein Ausdruck mit einem `.` gefolgt von ArtDesWertes.NameDesWertes (ValueType.ValueName), um einen weiteren Wert zu adressieren.


</div>



### Zwischenskizze

Der Bogen dieses Filmscharniers hat eine konstante Länge und einen variablen Radius. Eine Eingangsgröße ist NeutralerRadius der Basis-Skizze; um ihn in der Skizze zur Hand zu haben, wird er als <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [externe Geometrie](Sketcher_External/de.md) eingebunden und erhält das mit ReferenzRadius benannte anzeigende Maß (reference dimension).


<div class="mw-collapsible-content toccolours">

Ein Tortenstück aus Hilfsgeometrie zeigt die Verbindung zwischen dem Bogen und dem Radius für einen gegebenen Winkel.
**EingangsLänge = ReferenzRadius \* Pi**
und
**BogenLänge = DynamischerRadius \* Pi \* BogenWinkel / 180°**
mit konstanter Länge ergibt sich:
**ReferenzRadius \* Pi = DynamischerRadius \* Pi \* BogenWinkel / 180°**
Und mit herausgekürztem Pi erhalten wir:
**ReferenzRadius = DynamischerRadius \* BogenWinkel / 180°** oder **DynamischerRadius = ReferenzRadius \* 180° / BogenWinkel**

:   Der <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [Ausdruck](Expressions/de.md) für den Wert von DynamischerRadius: `.Constraints.ReferenzRadius * 180 ° / .Constraints.BogenWinkel`

Ein Filmscharnier ist meistens symmetrisch, daher wird ein weiterer Bogen mit demselben Mittelpunkt, genannt HalbBogen, als Ergebniselement verwendet und stellt eine Hälfte des Scharnierbogens dar.

:   Der <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [Ausdruck](Expressions/de.md) für den Wert von HalbBogen: `.Constraints.BogenWinkel / 2`


</div>

<img alt="" src=images/Sketcher_ExampleHinge-02.png  style="width:400px;"> 
*Die Zwischenskizze zeigt die Strecke DynamischerRadius des Filmscharniers mit 4 (mm) bei einem gegebenen Winkel von 45° (und den halben Winkel als Ausgabeelement)*



### Filmscharnierskizze

Diese Skizze legt die Wandstärke und die angrenzende Geometrie des Filmschrniers fest. Dazu laden wir den halben Bogen der Zwischenskizze als externe Geometrie hinzu, um ihn als Basis für den Filmanteil zu verwenden. (ein Bruchteil von 180° in diesem Falle)

Dieses Filmscharnier ist so ausgelegt, dass sich die damit verbundenen Teile berühren, wenn das Objekt geschlossen ist. Dies kann erreicht werden durch das Berechnen eines Kreisbogens mit der erforderlichen Länge, dann das Erstellen eines Streifens mit konstanter Wandstärke und schließlich durch das Verrunden der Übergänge zwischen dem Streifen und den beiden Objekthälften. Der letzte Schritt verkürzt zwar die entstehende Schlaufe, aber in der Realität spielt dies keine Rolle, da der Bogen nie ganz kreisförmig sein wird, so hat die Verrundung zwar einen Einfluss auf den Krümmungsverlauf der Schlaufe, aber keinen Einfluss auf ihre Funktion.

<img alt="" src=images/Sketcher_ExampleHinge-03.png  style="width:400px;"> 
*Die Scharnierskizze zeigt den Umriss des Scharniers basierend auf der externen Geometrie des halben Bogens aus der Zwischenskizze*

<img alt="" src=images/Sketcher_ExampleHinge-04.png  style="width:300px;"> <img alt="" src=images/Sketcher_ExampleHinge-05.png  style="width:300px;"> 
*Links: Das <img src="images/PartDesign_Pad.svg" width=16px> [extrudierte](PartDesign_Pad/de.md) halbe Scharnier mit sichtbarer Skizze. Rechts: Das halbe Scharnier mit hinzugefügter <img src="images/PartDesign_Fillet.svg" width=16px> [Verrundung](PartDesign_Fillet/de.md)*

<img alt="" src=images/Sketcher_ExampleHinge-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-07.png  style="width:300px;"> 
*Das halbe Scharnier mit ausgewählter Spiegelebene → <img src="images/PartDesign_Mirrored.svg" width=16px> [gespiegeltes](PartDesign_Mirrored/de.md) Filmscharnier*

Hinweis: <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Part Spiegeln](Part_Mirror/de.md) akzeptiert nur die drei Basis-Ebenen und kann dadurch in so einem Falle nicht verwendet werden.

:   (Rückblickend war es eine weise Entscheidung dieses Beispiel mit der Kombination von PartDesign und Sketcher zu beginnen.)

Letztendlich legen zwei Parameter die Größe des Filmscharniers fest:

-   NeutralerRadius in der Basis-Skizze
-   Der Wert der Wandstärke in der Filmscharnierskizze



### Biegen des Filmscharniers 

Der Biegewinkel wird durch die Randbedingung BogenWinkel der Zwischenskizze gesteuert und kann in ihrem Einstellungseditor geändert werden.
Aber wir sind ja richtige Konstrukteure und haben unsere Skizzen, Randbedingungen und Maße sinnvoll benannt und können daher den steuernden Winkel über Python ansprechen.
Einige grundlegende Codezeilen zum Einbetten in einer Benutzerschnittstelle könnten so aussehen:


```python
doc=App.ActiveDocument
sketch=doc.getObjectsByLabel('IntermediateSketch')[0]
 ...
sketch.getDatum('ArcAngle')
 ...
sketch.setDatum('ArcAngle',App.Units.Quantity('50.000000 deg'))
doc.recompute(None,True,True)
```


<div class="mw-collapsible-content toccolours">

Eine kurze Erklärung:

-    {{Incode|doc {{=}}App.ActiveDocument}}: Zum Ansprechen des aktiven Dokuments mit einem Alias namens **doc**

-    {{Incode|sketch {{=}}doc.getObjectsByLabel(\'IntermediateSketch\')\[0\]}}: Zum Ansprechen der relevanten Skizze mit dem Alias **sketch**.

    :   Die Methode **getObjectsByLabel()** gibt eine Liste von Objekten zurück und wir müssen den Index {{value|0}} anhängen, um das erste Element der Liste auszuwählen. (Wir erwarten nicht, dass ein anderes Objekt dieselbe Benennung aufweist und müssen uns daher nicht um andere Elemente in der Liste kümmern.)

-    {{Incode|sketch.getDatum('ArcAngle')}}: Gibt den aktuellen Wert der maßlichen Randbedingung **ArcAngle** (BogenWinkel) zurück (an das Ausgabefenster)

-    {{Incode|sketch.setDatum('ArcAngle', App.Units.Quantity('50.0 deg'))}}: Setzt den Wert von **ArcAngle** auf {{value|50°}}

-    {{Incode|doc.recompute(None,True,True)}}: Zum aktualisieren des ganzen Dokuments, um auch die Änderungen an den abhängigen Geometrien darzustellen.


</div>



### Geometrien verbinden 

Zwei Hälften eines Klipp-Objekts warten darauf mit dem Filmscharnier verbunden zu werden, eine an der statischen Seite und eine auf der beweglichen Seite.

<img alt="" src=images/Sketcher_ExampleHinge-08.png  style="width:300px;"> 
*Zwei Hälften eines einfachen Klipps*


<div class="mw-collapsible-content toccolours">

Die statische Seite ist einfach:

1.  Den Körper (Body) aktivieren und die Eigenschaften position und orientation properties im Eigenschafteneditor anpassen, bis er zum Filmscharnier passt.
2.  Den Scharnierkörper aktivieren.
3.  Das Werkuzeug <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Boolesche Operation](PartDesign_Boolean/de.md) mit der (Standard-) Option Vereineigung auswählen.
4.  Im Dialog die Schaltfläche **Körper hinzufügen** drücken.
5.  Den **Körper** der statischen Hälfte des Klipps auswählen.
6.  Zum Beenden und Schließen des Dialogs OK drücken.


</div>

<img alt="" src=images/Sketcher_ExampleHinge-09.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-10.png  style="width:300px;"> 
*Filmscharnier und statische Hälfte in Konstruktionslage → Filmscharnier mit versetzter und <img src="images/PartDesign_Boolean.svg" width=16px> [vereinigter](PartDesign_Boolean/de.md) statischer Hälfte*


<div class="mw-collapsible-content toccolours">

Aber die bewegliche Seite ist anders: die zugehörige Hälfte der Klippgeometrie muss in die richtige Lage bewegt werden, bevor die (Neu-) Berechnung einer Vereinigungsoperation gestartet wird.

An diesem Punkt vermisse ich eine Funktion \"Befestigen mit Abstand\" (Attachment with offset), wie die von Assembly3, zum Verknüpfen der Klippgeometrie mit einer der beweglichen Flächen. Aber nach etwas Herumprobieren und Feineinstellen habe ich herausgefunden:

-   Die Behälter <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std Teil](Std_Part/de.md) (Part) und <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Körper](PartDesign_Body/de.md) (Body) werden nicht von <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Befestigen](Part_EditAttachment/de#Einschränkungen.md) unterstützt.

:   Es ist zwar möglich, Befestigen zu verwenden, um die Behälter auszurichten, aber die Befestigung wird nicht parametrisch verknüpft.

-   Befestigen kann auf ein PartDesign-Formelement angewendet werden. Dieses und davon abhängige Formelemente werden mit Bezug zur Basisgeometrie verschoben. Aber!:
    -   Unabhängige PartDesign-Formelemente werden sich nicht bewegen und daher kann sich die Ergebnisform ändern und schließlich zerbrechen.
    -   Es wird geraten, Formelemente unabhängig zu halten, um Auswirkungen, die auf dem [Problem der Topologischen Benennung](Topological_naming_problem/de.md) basieren, zu vermeiden.
-   <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Klon](PartDesign_Clone/de.md) erstellt einen Körper mit einem einzigen Formelement, der mit Befestigen verwendet werden kann.

Mit diesem Wissen im Hinterkopf könnte ein Arbeitsablauf so aussehen:

1.  Den Körper (Body) der beweglichen Hälfte auswählen.
2.  Den Befehl <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Klon erstellen](PartDesign_Clone/de.md) aufrufen.
3.  In der Baumansicht im neuen Körper (Body-Objekt) das Clone-Objekt auswählen.
4.  Das Werkzeug <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Befestigung](Part_EditAttachment/de.md) aufrufen, um dem Clone-Objekt die Eigenschaften von Befestigung hinzuzufügen.
5.  Der Dialog Anhang wird geöffnet.
    -   Einen Knoten für den Ursprung auswählen.
    -   Eine Kante für die erste Richtung auswählen.
    -   Eine Kante für die zweite Richtung auswählen.
    -   Die Befestigungsmöglichkeiten durchprobieren, um die am besten passende herauszufinden.
    -   Die Drehungs- und Koordinatenwerte anpassen, bis sich die Geometrie wieder in Konstruktionslage befindet.
6.  OK drücken, um den Dialog zu schließen.
7.  MIt noch immer aktiviertem Scharnierkörper das Werkzeug <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Boolesch Operation](PartDesign_Boolean/de.md) auswählen.
8.  Im Dialog die Schaltfläche **Körper hinzufügen** drücken.
9.  Den Körper der beweglichen Hälfte auswählen.
10. OK drücken, um die Aktion zu beenden und den Dialog zu Schließen.


</div>


</div>

<img alt="" src=images/Sketcher_ExampleHinge-14.png  style="width:300px;"> 
*Die bewegliche Hälfte wird an einer Ecke der beweglichen Scharnierseite <img src="images/Part_EditAttachment.svg" width=16px> [befestigt](Part_EditAttachment/de.md) (Befestigungsmodus Ausrichten OXZ: Knoten, Kante, Kante)*

Rückblickend betrachtet, wäre es weiser gewesen, die Geometrie zum Befestigen in der Zwischenskizze vorzugeben, um eine weitere Quelle des [Problems der topologischen Benennung](Topological_naming_problem/de.md) zu vermeiden.

<img alt="" src=images/Sketcher_ExampleHinge-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-12.png  style="width:300px;"> 
*Der Klipp bis hier hin und die bewegliche Hälfte in Konstruktionslage → der fertige Klipp mit der <img src="images/Part_EditAttachment.svg" width=16px> [befestigten](Part_EditAttachment/de.md) und <img src="images/PartDesign_Boolean.svg" width=16px> [vereinigten](PartDesign_Boolean/de.md) beweglichen Hälfte*

Jetzt sollte das Ergebnis ein Klipp sein, der nur aus einem Einzel-Festkörper besteht und der geschlossen und geöffnet werden kann, indem der BogenWinkel des Filmscharniers geändert wird. Die erlaubten Werte liegen zwischen 0.1° und 180°; der Filmabschnitt darf nicht gerade sein und mehr als geschlossen ist nicht sinnvoll. (Bei 180° kann das Objekt an berührenden oder überlappenden Flächen verschmelzen, aber eine kleine zusätzliche Lücke kann helfen, wenn dies nicht akzeptabel ist.)

<img alt="" src=images/Sketcher_ExampleHinge-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-16.png  style="width:200px;"> 
*Klipp fast geschlossen → Klipp halb geschlossen → Klipp in Werkzeuglage*


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Examples/de
