# <img alt="Symbol des Arbeitsbereichs Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/de






## Einleitung

Mit dem Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) können 2D-Skizzen für den Gebrauch in anderen Arbeitsbereichen erstellt werden. 2D-Skizzen sind der Ausgangspunkt für viele CAD-Modelle. Sie legen typischerweise die Profilquerschnitte und Rückgratkurven für die Verfahren zur Erstellung von 3D-Formen fest. Die endgültige Form eines Modells kann von mehreren Skizzen abhängen.

Zusammen mit booleschen Verknüpfungen, die im Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) festgelegt werden, bildet der Arbeitsbereich Sketcher, oder kurz \"der Sketcher\", die Basis der Methode \"Konstruktive Festkörper-Geometrie\", engl.: [constructive solid geometry](constructive_solid_geometry/de.md) (CSG) zum Aufbau von Festkörpern. Zusammen mit den Verfahren des Arbeitsbereichs <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/de.md) bildet er auch die Basis der Methode [Formelemente bearbeiten](Feature_editing/de.md) zum Aufbau von Festkörpern. Aber auch viele andere Arbeitsbereiche setzen Skizzen ein.

Der Arbeitsbereich Sketcher verwendet [Randbedingungen](#Randbedingungen.md) (engl.: constraints, auch Beschränkungen, Zwangsbedingungen oder Einschränkungen genannt), die es ermöglichen, dasss 2D-Formen präzisen geometrische Festlegungen in Form von Längen, Winkeln und Lagebeziehungen (horizontal, vertikal, rechtwinklig, usw.) folgen. Ein mathematischer Gleichungslöser (kurz Löser) *Löser* (engl.: Solver) berechnet den mit Randbedingungen bestimmten Umfang der 2D-Geometrie und ermöglicht die interaktive Überwachung der Freiheitsgrade der Skizze.

Der Sketcher ist nicht für die Herstellung von technischen Zeichnungen (Blaupausen) vorgesehen. Sobald Skizzen eingesetzt wurden um ein Festkörper-Formelement zu erstellen, werden sie automatisch ausgeblendet und Randbedingungen sind nur im Skizzenbearbeitungsmodus sichtbar. Sollen nur 2D-Zeichnungen zum Ausdrucken erstellt werden, ohne dass 3D-Modelle benötigt werden, sollte der Arbeitsbereich [Draft](Draft_Workbench.md) ausprobiert werden.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Eine vollständig bestimmte Skizze‎*



## Randbedingungen

Randbedingungen (auch Beschränkungen, Einschränkungen, Zwangsbedingung genannt) werden eingesetzt, um die Freiheitsgrade eines Objektes festzulegen (zu bestimmen). Beispielsweise besitzt eine Linie ohne Randbedingung 4 nicht bestimmte Freiheitsgrade (engl.: degree(s) of freedom, abgekürzt als \"DoF\"): Sie kann horizontal oder vertikal verschoben, sie kann gestreckt, oder gedreht werden.

Durch Vorgabe einer Ausrichtung, wie horizontal, vertikal oder eines Winkels (relativ zu einer anderen Linie oder zu einer der Achsen), wird ihr die Fähigkeit zu rotieren genommen, sodass 3 Freiheitsgrade übrig bleiben. Das Festsetzen eines der Punkte relativ zum Ursprung entfernt weitere 2 Freiheitsgrade. Und das Festlegen der Länge entfernt den letzten Freiheitsgrad. Die Skizze ist dann **vollständig bestimmt**.

Objekte können relativ zueinander ausgerichtet werden. Zwei Linien können durch je einen ihrer Endpunkte mit der Randbedingung *KoinzidentFestlegen* (deckungsgleich) verbunden werden. Ein Winkel kann zwischen den beiden Linien festgelegt werden oder auch ein rechter Winkel. Eine Linie kann tangential an einem Bogen oder einem Kreis liegen, usw. Eine komplexe Skizze mit mehreren Objekten kann auf verschiedene Arten festgelegt bzw. bestimmt werden. **vollständig bestimmt** bedeutet, dass die Kombination der Randbedingungen nur noch genau eine Lösung für die Berechnung zulässt.

Es gibt zwei Arten von Randbedingungen: *geometrische* und *maßliche*. Sie sind im Abschnitt [Werkzeuge](#Werkzeuge.md) weiter unten ausführlich beschrieben.



### Randbedingungen bearbeiten 

Wenn eine [festlegende maßliche Randbedingung](Sketcher_ToggleDrivingConstraint/de.md) erstellt wird und wenn die [Einstellung](Sketcher_Preferences/de#Anzeige.md) **Wert erfragen, nach Erstellung einer maßlichen Randbedingung** aktiviert ist (Standardeinstellung), öffnet sich ein Dialog zum Bearbeiten des Wertes.

![Sketcher Randbedingungen bearbeiten](images/Sketcher_Edit_Constraint.png )

Es kann ein Zahlenwert oder ein [Ausdruck](Expressions/de.md) eingegeben werden und es ist möglich der Randbedingung einen Namen zu geben, um ihre Verwendung in anderen Ausdrücken zu ermöglichen. Man kann die Checkbox **Referenz** aktivieren, um die Randbedingung in den [anzeigenden Modus](Sketcher_ToggleDrivingConstraint/de.md) umzuschalten.

Um den Wert einer vorhandenen maßlichen Randbedingung zu ändern gibt es folgende Möglichkeiten :

-   Ein Doppelklick auf die Randbedingung in der [3D-Ansicht](3D_view/de.md).
-   Ein Doppelklick auf die Randbedingung im [Sketcher-Dialog](Sketcher_Dialog/de.md).
-   Ein Rechtsklick auf die Randbedingung im Sketcher-Dialog und die Menüoption **Wert ändern** im Kontextmenü auswählen.



### Randbedingungen verschieben 

Maßliche Randbedingungen können durch Ziehen in der 3D-Ansicht verschoben werden. MIt dem Mauszeiger über der Maßzahl die linke Maustaste gedrückt halten und die Maus bewegen. Die Symbole der geometrischen Randbedingungen werden automatisch positioniert und können nicht bewegt werden.



## Profilskizzen

Um eine Skizze zu erstellen, die sich zum Erstellen von Festkörpern eignet, müssen folgende Regeln befolgt werden:

-   Die Skizze darf nur geschlossene Konturen enthalten. Lücken zwischen den Endpunkten, egal wie klein, sind nicht erlaubt.
-   Konturen können eingebettet werden, um Hohlräume zu erstellen; sie dürfen sich aber nicht selbst kreuzen oder andere Konturen überlappen.
-   Konturen dürfen keine gemeinsamen Kanten mit anderen Konturen besitzen. Doppelte Kanten müssen vermieden werden.
-   T-Verbindungen, d.h. mehr als zwei Kanten sind mit einem gemeinsamen Punkt verbunden, oder ein Punkt der eine Kante berührt, sind nicht erlaubt.

Diese Regeln gelten nicht für Hilfsgeometrie (Standardfarbe blau), die außerhalb des Bearbeitungsmodus nicht dargestellt wird oder wenn die Skizze für einen anderen Zweck eingesetzt wird. Abhängig von dem Arbeitsbereich und dem Werkzeug, das die Skizze verwendet, können weitere Einschränkungen gelten.



## Zeichnungshilfen

Der Arbeitsbereich Sketcher besitzt einige Zeichnungshilfen und andere Funktionen, die bei der Erstellung von Geometie und beim Zuordnen von Randbedingungen helfen können.



### Fortsetzen-Modi 

Es gibt zwei Fortsetzen-Modi. Werden in den [Voreinstellungen](Sketcher_Preferences/de#Anzeige.md) die Einstellungen **Geometrie im \"Fortsetzen-Modus\" erstellen** und **Randbedingungen im \"Fortsetzen-Modus\" erstellen** aktiviert (Standardeinstellung), dann werden die zugehörigen Werkzeuge nach dem Beenden erneut gestartet. Um ein Werkzeug im Fortsetzen-Modus zu beenden, wird die **Esc**-Taste oder die rechte Maustaste gedrückt. Dies muss wiederholt werden, wenn ein Werkzeug zur Geometrieerstellung im Fortsetzen-Modus schon Eingaben erhalten hat. Ein Werkzeug im Fortsetzen-Modus kann auch verlassen werden, indem ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen gestartet wird. Man beachte, dass das Drücken der **Esc**-Taste den Skizzenbearbeitungsmodus verlässt, wenn kein Werkzeug ausgewählt ist. Das Deaktivieren der Option **Mit Esc den Bearbeitungsmodus der Skizze verlassen** in den [Voreinstellungen](Sketcher_Preferences/de#Allgemein.md) hilft, wenn man zu oft unbeabsichtig **Esc** drückttoo many times.



### Automatische Randbedingungen 

In Skizzen, für die **Automatische Randbedingungen** aktiviert ist (Standardeinstellung), werden mehrere Randbedingungen automatisch angelegt. Das Symbol der vorgesehenen automatischen Randbedingung wird neben dem Mauszeiger angezeigt, wenn er richtig positioniert ist. Ein Klick mit der linken Maustaste legt diese Randbedingung fest. Diese Einstellung gilt pro Skizze und kann im [Sketcher-Dialog](Sketcher_Dialog/de#Randbedingungen.md) geändert werden oder durch Ändern der {{PropertyView/de|Autoconstraints}} ([siehe Eigenschaften](Property_editor/de.md)) der Skizze.

Die folgenden Randedingungen werden automatisch festgelegt:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertikal festlegen](Sketcher_ConstrainVertical/de.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangential festlegen](Sketcher_ConstrainTangent/de.md)

-    {{Version/de|1.0}}: <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetrisch festlegen](Sketcher_ConstrainSymmetric/de.md) (Linienmittelpunkt)



### Einrasten


{{Version/de|0.21}}

Es ist möglich auf Rasterlinien und Rasterschnittstellen [einzurasten](Sketcher_Snap/de.md), auf Kanten von Geometrien und Mittelpunkten von Linien und Kreisbögen sowie auf bestimmte Winkel. Bitte beachten, dass Einrasten selbst keine Randbedingungen erstellt. Nur wenn [Automatische Randbedingungen](#Automatische_Randbedingungen.md) eingeschaltet ist, wird das Einrasten auf einer Kante eine Randbedingung [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) anlegen. Aber auch das einfache Auswählen eines Punktes auf der Kante hätte dann das gleiche Ergebnis.



### In-Ansicht-Parameter 


{{Version/de|1.0}}

Abhängig von der ausgewählten Option in den [Voreinstellungen](Sketcher_Preferences/de#Allgemein.md) können nur die maßlichen In-Ansicht-Parameter (On-View-Parameters) aktiviert werden oder beide, die maßlichen In-Ansicht-Parameter und die zum Festlegen von Positionen. Letztere ermöglichen die Eingabe von exakten Koordinaten, z.B. für den Mittelpunkt eines Kreises oder den Startpunkt einer Linie. Maßliche Parameter ermöglichen die Eingabe exakter Maße und Winkel z.B. für den Radius eines Kreises oder die Länge und den Winkel einer Linie. In-Ansicht-Parameter stehen nicht für alle Werkzeuge zur Verfügung.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Bestimmung des Mittelpunktes eines Kreises mit aktivierten Positionsparametern*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Bestimmung des Radius eines Kreises mit aktivierten Maßparametern*

Werden Werte eingegeben und mit **Enter** oder **Tab** bestätigt, werden die zugehörigen Randbedingungen automatisch hinzugefügt. Werden zwei Parameter gleichzeitig angezeigt, z.B. die X- und die Y-Koordinate eines Punktes, ist es möglich einen Wert einzugeben und den anderen durch Auswahl eines Punktes festzulegen. Abhängig vom Objekt können weitere Randbedingungen erforderlich sein, um es vollständig zu bestimmen. Randbedingungen, die sich aus In-Ansich-Parametern ergeben, haben Vorrang vor denen, die aus [Automatischen Randbedingungen](Sketcher_Dialog/de#Randbedingungen.md) resultieren.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Kreisbogen, für den alle In-Ansicht-Parameter eingegeben wurden, mit den resultierenden automatisch erstellten Randbedingungen*



### Koordinatenanzeige

Ist die [Voreinstellung](Sketcher_Preferences/de#Anzeige.md) **Während der Bearbeitung Koordinaten neben dem Eingabezeiger anzeigen** aktiviert (Standardeinstellung), werden die Parameter des aktuellen Werkzeugs zur Geometrieerstellung (Koordinaten, Radius oder Länge und Winkel) neben dem Mauszeiger angezeigt. Dies wird deaktiviert, während in-Ansicht-Parameter angezeigt werden.



## Auswahlmethoden

Während sich eine Skizze im Bearbeitungsmodus befindet, können folgende Methoden eingesetzt werden:



### Elemente in der 3D-Ansicht auswählen 

Wie auch anderswo in FreeCAD kann ein Element in der [3D-Ansicht](3D_view/de.md) mit einem einzelnen Klick mit der linken Maustaste ausgewählt werden. Die **Ctrl**-Taste muss aber nicht gedrückt werden, wenn mehrere Elemente ausgewählt werden; sie kann aber gedrückt werden, was den Vorteil hat, dass nicht die ganze Auswahl verloren geht, wenn man sich verklickt. Kanten, Punkte und Randbedingungen können auf diese Weise ausgewählt werden.



### Rechteckauswahl in der 3D-Ansicht 

Rechteckauswahl in der 3D-Auswahl funktioniert ohne den Einsatz von [Std RechteckAuswahl](Std_BoxSelection/de.md) oder [Std RechteckElementAuswahl](Std_BoxElementSelection/de.md):

1.  Sicherstellen, dass kein Werkzeug aktiv ist.
2.  Eine der folgenden Möglichkeiten auswählen:
    -   In einen leeren Bereich klicken und ein Rechteck von links nach rechts aufziehen, um Elemente auszuwählen, die vollständig innerhalb des Rechtecks liegen.
    -   In einen leeren Bereich klicken und ein Rechteck von rechts nach links aufziehen, um auch Elemente auszuwählen, die das Rechtecks berühren oder die sich nur teilweise darin befinden.

Es können nur Kanten und Punkte mit einer Rechteckauswahl ausgewählt werden, aber keine Randbedingungen.



### Verbundene Geometrie in der 3D-Ansicht auswählen 


{{Version/de|1.0}}

Ein Doppelklick auf eine Kante in der 3D-Ansicht wählt alle Kanten aus, die direkt oder indirekt mit dieser Kante über Endpunkte verbunden sind. Die Kanten müssen nicht mit der Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) verbunden sein, sie müssen nur die gleichen Koordinaten aufweisen.



### Auswahl im Sketcher-Dialog 

Kanten und Punkte können auch im Abschnitt Elemente des [Sketcher-Dialogs](Sketcher_Dialog/de.md) ausgewählt werden und Randbedingungen im Abschnitt Randbedingungen dieses Dialogs.



## Kopieren, Ausschneiden und Einfügen 


{{Version/de|1.0}}

Die Standard-Tastaturkürzel **Ctrl** + **C**, **Ctrl** + **X** und **Ctrl** + **V** können zum Kopieren, Ausschneiden und Einfügen ausgewählter Skizzengeometrien einschließlich der zugehörigen Randbedingungen eingesetzt werden. Diese Werkzeuge stehen aber auch im Menü unter **Skizze → Sketcher-Werkzeuge** zur Verfügung. Sie können innerhalb derselben Skizze eingesetzt werden aber auch zwischen unterschiedlichen Skizzen oder verschiedenen Instanzen von FreeCAD. Da die Daten als Python-Code in die Zwischenablage kopiert werden, können sie auch auf andere Weise verwendet werden (z.B. im Forum geteilt werden).



## Werkzeuge

Die Werkzeuge des Arbeitsbereichs Sketcher sind im Menü *Sketch* und/oder mehreren Symbolleisten zu finden. {{Version/de|0.21}}: Fast alle Sketcher-Symbolleisten werden nur dann dargestellt, wenn sich eine Skizze im Bearbeitungsmodus befindet. Die einzige Ausnahme ist die Symbolleiste [Sketcher](#Sketcher_toolbar/de.md), die nur dargestellt wird, wenn sich keine Skizze im Bearbeitungsmodus befindet.

Einige Werkzeuge stehen auch im Kontextmenü der [3D-Ansicht](3D_view/de.md) zur Verfügung, während sich eine Skizze im Bearbeitungsmodus befindet, oder in den Kontextmenüs des [Sketcher-Dialogs](Sketcher_Dialog/de.md).


{{Version/de|0.21}}

: Ist eine Skizze im Bearbeitungsmodus, ist die Werkzeugleiste Struktur ausgeblendet, da dann keins ihrer Werkzeuge verwendet werden kann.



### Allgemein



#### Symbolleiste Sketcher 

-   <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [Skizze erstellen](Sketcher_NewSketch/de.md): Erstellt eine neue Skizze und öffnet den [Sketcher-Dialog](Sketcher_Dialog/de.md), um sie zu bearbeiten.

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Skizze bearbeiten](Sketcher_EditSketch/de.md): Öffnet den [Sketcher-Dialog](Sketcher_Dialog/de.md), um eine vorhandene Skizze zu bearbeiten.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:24px;"> [Sketcher SkizzeZuordnen](Sketcher_MapSketch/de.md): Befestigt eine Skizze an ausgewählter Geometrie.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> [Sketcher SkizzeAusrichten](Sketcher_ReorientSketch/de.md): Verlegt eine Skizze auf eine der Hauptebenen, wahlweise mit einem Abstand. Es kann auch zum Ablösen der Skizze eingesetzt werden.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Skizze überprüfen](Sketcher_ValidateSketch/de.md): Kann eine Skizze analysieren und reparieren, die nicht mehr bearbeitet werden kann oder die ungültige Randbedingungen enthält oder kann fehlende Randbedingungen für Koinzidenz hinzufügen.

-   <img alt="" src=images/Sketcher_MergeSketch.svg‎  style="width:32px;"> [Skizzen zusammenführen](Sketcher_MergeSketches/de.md): Führt zwei oder mehr Skizzen zusammen.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎  style="width:32px;"> [Skizze spiegeln](Sketcher_MirrorSketch/de.md): Spiegelt eine Skizze über ihre X-Achse, Y-Achse oder über ihren Ursprung.



#### Symbolleiste Sketcher-Bearbeitungsmodus 

-   <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> [Skizze verlassen](Sketcher_LeaveSketch/de.md): Beendet den Bearbeitungsmodus des Sketchers und schließt den [Sketcher-Dialog](Sketcher_Dialog/de.md)..

-   <img alt="" src=images/Sketcher_ViewSketch.png‎  style="width:32px;"> [Skizze anzeigen](Sketcher_ViewSketch/de.md): Richtet die [3D-Ansicht](3D_view/de.md) zur Skizzenebene aus.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Schnitt anzeigen](Sketcher_ViewSection/de.md): Schaltet eine zeitweilige Schnittebene ein bzw. aus, die vorübergehend alle Anteile von Objekten ausblendet, die sich vor der Skizzenebene befinden.



#### Symbolleiste Sketcher-Werkzeuge Bearbeitung 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Raster umschalten](Sketcher_Grid/de.md): Aktiviert bzw. deaktiviert das Raster in der aktuell bearbeiteten Skizze. Die Einstellungen können im zugehörigen Menü angepasst werden. {{Version/de|0.21}}

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Einrasten umschalten](Sketcher_Snap/de.md): Aktiviert bzw. deaktiviert das Einrasten in allen Skizzen. Die Einstellungen können im zugehörigen Menü angepasst werden. {{Version/de|0.21}}

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Rendering-Reihenfolge konfigurieren](Sketcher_RenderingOrder/de.md): Die Rendering-Reihenfolge aller Skizzen kann im zugehörigen Menü angepasst werden. {{Version/de|0.21}}



#### Andere

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Vorgang beenden](Sketcher_StopOperation/de.md): Hält jedes gerade aktive Werkzeug zur Erstellung von Geometrien oder Randbedingungen an.



### Skizzengeometrien

Dies sind Werkzeuge zum Erstellen von Objekten.

-   <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Punkt erstellen](Sketcher_CreatePoint/de.md): Erstellt einen Punkt.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Linienzug erstellen](Sketcher_CreatePolyline/de.md): Erstellt eine Abfolge von Linien- und Kreisbogenabschnitten, die and ihren Enpunkten verbunden sind. Das Werkzeug besitzt mehrere Modi.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Linie erstellen](Sketcher_CreateLine/de.md): Erstellt eine Linie zwischen 2 Punkten. {{Version/de|1.0}}: Das Werkzeug besitzt drei Modi.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Bogen erstellen:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Kreisbogen um Mittelpunkt erstellen](Sketcher_CreateArc/de.md): Erstellt einen Kreisbogen durch Festlegen seines Mittelpunktes und seiner Endpunkte. {{Version/de|1.0}}: Oder durch Festlegen seiner Endpunkte und eines Punktes im Verlauf des Bogens.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Kreisbogen durch 3 Punkte erstellen](Sketcher_Create3PointArc/de.md): Erstellt einen Kreisbogen durch seine Endpunkte und eine weiteren Punkt im Verlauf des Bogens. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Kreisbogen um Miitelpunkt erstellen](Sketcher_CreateArc/de.md) aber mit einem anderen Startmodus.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Ellipsenbogen erstellen](Sketcher_CreateArcOfEllipse/de.md): Erstellt einen Ellipsenbogen.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Hyperbelbogen erstellen](Sketcher_CreateArcOfHyperbola/de.md): Erstellt einen Hyperbelbogen.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Parabelbogen erstellen](Sketcher_CreateArcOfParabola/de.md): Erstellt einen Parabelbogen.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Kreis/Ellipse erstellen:

  - <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Kreis um Mittelpunkt erstellen](Sketcher_CreateCircle/de.md): Erstellt einen Kreis durch Festlegen seines Mittelpunktes und eines Punktes im Verlauf seines Umfangs. {{Version/de|1.0}}: Oder durch Festlegen dreier Punkte im Verlauf seines Umfangs.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Kreis aus drei Punkten erstellen](Sketcher_Create3PointCircle/de.md): Erstellt einen Kreis durch Festlegen dreier Punkte im Verlauf seines Umfangs. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Kreis um Mittelpunkt erstellen](Sketcher_CreateCircle/de.md) aber mit einem anderen Startmodus.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse um Mittelpunkt erstellen](Sketcher_CreateEllipseByCenter/de.md): Erstellt eine Ellipse durch Festlegen ihres Mittelpunktes, eines Endpunktes einer ihrer Achsen und eines Punktes im Verlauf ihres Umfangs. {{Version/de|1.0}}: Oder durch Festlegen beider Endpunkte einer Achse und eines Punktes im Verlauf ihres Umfangs.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse durch 3 Punkte erstellen](Sketcher_CreateEllipseBy3Points/de.md): Erstellt eine Ellipse durch Festlegen beider Endpunkte einer ihrer Achsen und eines Punktes im Verlauf ihres Umfangs. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Ellipse um Mittelpunkt erstellen](Sketcher_CreateEllipseByCenter/de.md) aber mit einem anderen Startmodus.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Rechteck erstellen:

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rechteck erstellen](Sketcher_CreateRectangle/de.md): Erstellt ein Rechteck. {{Version/de|1.0}}: Das Werkzeug besitzt vier Modi. Zusätzlich können die Optionen Abgerundete Ecken und Rahmen aktiviert werden.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Zentriertes Rechteck erstellen](Sketcher_CreateRectangle_Center/de.md): Erstellt ein zentriertes Rechteck. <small>(v1.0)</small> : Dies ist dasselbe Werkzeug wie [Rechteck erstellen](Sketcher_CreateRectangle/de.md) aber mit einem anderen Startmodus.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Abgerundetes Rechteck erstellen](Sketcher_CreateOblong/de.md): Erstellt ein abgerundetes Rechteck. <small>(v1.0)</small> : Dies ist dasselbe Werkzeug wie [Rechteck erstellen](Sketcher_CreateRectangle/de.md) aber mit einem anderen Startmodus.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Regelmäßiges Vieleck erstellen:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Gleichseitiges Dreieck erstellen](Sketcher_CreateTriangle/de.md): Erstellt ein gleichseitiges Dreieck. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Quadrat erstellen](Sketcher_CreateSquare/de.md): Erstellt ein Quadrat. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Fünfeck erstellen](Sketcher_CreatePentagon/de.md): Erstellt ein regelmäßigen Fünfeck. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Sechseck erstellen](Sketcher_CreateHexagon/de.md): Erstellt ein regelmäßiges Sechseck. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Siebeneck erstellen](Sketcher_CreateHeptagon/de.md): Erstellt ein regelmäßiges Siebeneck. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Achteck](Sketcher_CreateOctagon/de.md): Erstellt ein regelmäßiges Achteck. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md) aber mit einem bestimmten voreingestellten Wert für die Anzahl der Seiten.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regelmäßiges Vieleck erstellen](Sketcher_CreateRegularPolygon/de.md): Erstellt ein regelmäßiges Vieleck. Die Anzahl der Seiten kann eingestellt werden.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Oval erstellen:

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Oval erstellen](Sketcher_CreateSlot/de.md): Erstellt eine \"Nut\".

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Bogennut](Sketcher_CreateArcSlot/de.md): Erstellt eine Bogennut. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-Spline erstellen:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-Spline durch Kontrollpunkte](Sketcher_CreateBSpline/de.md): Erstellt eine B-Spline-Kurve durch Setzen von Kontrollpunkten. {{Version/de|1.0}}: Oder durch Setzen von Knotenpunkten.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Geschlossener B-Spline durch Kontrollpunkte](Sketcher_CreatePeriodicBSpline/de.md): Erstellt eine periodische (geschlossene) B-Spline-Kurve durch Setzen von Kontrollpunkten. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [B-Spline durch Kontrollpunkte](Sketcher_CreateBSpline/de.md) aber mit einem anderen Startmodus.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline durch Knoten](Sketcher_CreateBSplineByInterpolation/de.md): Erstellt eine B-Spline-Kurve durch Knotenpunkte. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [B-Spline durch Kontrollpunkte](Sketcher_CreateBSpline/de.md) aber mit einem anderen Startmodus.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Geschlossener B-Spline durch Knoten](Sketcher_CreatePeriodicBSplineByInterpolation/de.md): Erstellt eine periodische (geschlossene) B-Spline-Kurve durch Knotenpunkte. {{Version/de|1.0}}: Dies ist dasselbe Werkzeug wie [B-Spline durch Kontrollpunkte](Sketcher_CreateBSpline/de.md) aber mit einem anderen Startmodus.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Hilfsgeometrie umschalten](Sketcher_ToggleConstruction/de.md): Aktiviert bzw. deaktiviert den Konstruktionsmodus für alle Werkzeuge zur Geometrieerstellung oder es wandelt ausgewählte normale Geometrie in Hilfsgeometrie und umgekehrt.



### Sketcher-Randbedingungen 

Dies sind Werkzeuge zum Erstellen von [Randbedingungen](#Randbedingungen.md). Einige Randbedingungen erfordern den Einsatz von [Hilfsrandbedingungen](Sketcher_helper_constraint/de.md).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Maßliche Randbedingungen:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Abmessung](Sketcher_Dimension/de.md): Es ist das kontextabhängige Werkzeug zum Erstellen von Randbedingungen des Arbeitsbereichs Sketcher. Basierend auf der aktuellen Auswahl stellt es passende maßliche Randbedingungen zur Verfügung aber auch geometrische Randbedingungen. {{Version/de|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md) (XAbstandFestlegen): Legt den horizontalen Abstand zwischen zwei Punkten oder Endpunkten einer Linie fest. Ist ein einzelner Punkt vorausgewählt, bezieht sich der Abstand auf den Ursprung der Skizze.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md) (YAbstandFestlegen): Legt den vertikalen Abstand zwischen zwei Punkten oder den Endpunkten einer Linie fest. Ist ein einzelner Punkt vorausgewählt, bezieht sich der Abstand auf den Ursprung der Skizze.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Abstand festlegen](Sketcher_ConstrainDistance/de.md): Legt die Länge einer Linie, den Abstand zwischen zwei Punkten, den senkrechten Abstand eines Punktes zu einer Linie fest; oder {{Version/de|0.21}} den Abstand zwischen den Kanten zweier Kreise oder Kreisbögen oder zwischen der Kante eines Kreises oder Kreisbogens und einer Linie; oder {{Version/de|1.0}} die Länge eines Kreisbogens.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Automatisch Radius oder Durchmesser festlegen](Sketcher_ConstrainRadiam/de.md): Legt den Radius für Bögen und B-Spline-Gewichtskreise und den Durchmesser für Kreise fest.

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radius](Sketcher_ConstrainRadius/de.md): Legt den Radius für Kreise, Kreisbögen oder B-Spline-Gewichtskreise fest.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Durchmesser festlegen](Sketcher_ConstrainDiameter/de.md): Legt den Durchmesser für Kreise und Kreisbögen fest.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Winkel festlegen](Sketcher_ConstrainAngle/de.md): Legt den Winkel zwischen zwei Kanten, den Winkel zur horizontalen Achse der Skizze oder den überstrichenen Winkel eines Kreisbogens fest.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Sperren](Sketcher_ConstrainLock/de.md): Ordnet Punkten die Randbedingungen [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md) und [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md) zu. Ist ein einzelner punkt ausgewählt, beziehen sich die Randbedingungen auf den Ursprung der Skizze. Sind zwei oder mehr Punkte ausgewählt, beziehen sich die Randbedingungen auf den letzten Punkt in der Auswahl.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [KoinzidentFestlegen (kombiniert)](Sketcher_ConstrainCoincidentUnified/de.md): Legt zwei Punkte koinzident (deckungsgleich) fest, legt Punkte auf Kanten oder Achsen fest oder legt Kreise oder Kreisbögen konzentrisch fest. Es kombiniert die Werkzeuge [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) und [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md). {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md): Legt Punkte koinzident (deckungsgleich) fest oder Kreise und Kreisbögen konzentrisch.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md): Legt Punkte auf Kanten oder Achsen fest.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Horizontal/vertikal:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertikal](Sketcher_ConstrainHorVer.md): Legt Linien oder Punktpaare horizontal oder vertikal fest, je nach dem, was eher der aktuellen Ausrichtung entspricht. Es kombiniert die Werkzeuge [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md) und [Vertikal festlegen](Sketcher_ConstrainVertical/de.md) .{{Version/de|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md): Legt Linien oder Punktpaare horizontal fest.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertikal festlegen](Sketcher_ConstrainVertical/de.md): Legt Linien oder Punktpaare vertikal fest.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallel festlegen](Sketcher_ConstrainParallel/de.md): Legt Linien parallel zueinander fest.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Rechtwinklig festlegen](Sketcher_ConstrainPerpendicular/de.md): Legt zwei Linien rechtwinklig zueinander fest oder zwei Kanten bzw. eine Kante und eine Achse in ihrem Schnittpunkt. Die Randbedingung kann auch zwei Kanten an ihrer Verbindungsstelle rechtwinklig zueinander festlegen.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangential oder kollinear festlegen](Sketcher_ConstrainTangent/de.md): Legt zwei Kanten oder eine Kante und eine Achse tangetial zueinander fest. Die Randbedingung kann auch zwei Kanten verbinden und an der Verbindungsstelle tangetial zueinander festlegen. Sind zwei Linien ausgewählt, werden sie kollinear festgelegt.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md): Legt fest, dass Kanten die gleiche Länge (Linien) oder die gleiche Krümmung (andere Kanten außer B-Splines) aufweisen.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symmetrie festlegen](Sketcher_ConstrainSymmetric/de.md): Legt zwei Punkte symmetrisch zu einer Linie oder Achse bzw. zu einem dritten Punkt fest.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Fixieren](Sketcher_ConstrainBlock/de.md): Setzt Kanten mit einer einzigen Randbedingung auf ihren Positionen fest. Es ist hauptsächlich für B-Spines gedacht.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md): Legt zwei Linien so fest, dass sie der Lichtbrechung entsprechen, die beim Passieren einer Grenzfläche auftritt.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Randbedingungen umschalten:

  - <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Randbedingung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleDrivingConstraint/de.md): Schaltet den Modus der Werkzeuge zum Erstellen von maßlichen Randbedingungen zwischen festlegend oder anzeigend (Referenzmodus) um oder wechselt den Modus der ausgewählten maßlichen Randbedingungen.

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Einschränkung aktivieren/deaktivieren](Sketcher_ToggleActiveConstraint/de.md) (UmschalterAktiveRandbedingung): Aktiviert bzw. deaktiviert ausgewählte Randbedingungen.



### Sketcher-Werkzeuge 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Verrundung oder Fase erstellen:

  - <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Verrundung erstellen](Sketcher_CreateFillet/de.md): Erstellt einen Bogen zwischen zwei nicht parallelen Kanten. {{Version/de|1.0}}: Das Werkzeug kann auch eine Fase erstellen

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Fase erstellen](Sketcher_CreateChamfer/de.md): Erstellt eine Fase zwischen zwei nicht parallelen Kanten. Dies ist dasselbe Werkzeug wie [Verrundung erstellen](Sketcher_CreateFillet/de.md) aber mit einem anderen voreingestellten Modus. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Kante bearbeiten:

  - <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Kante zuschneiden](Sketcher_Trimming/de.md): Stutzt eine Kante an den am nächsten liegenden Schnittpunkten mit anderen Kanten.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Kante teilen](Sketcher_Split/de.md): Teilt eine Kante in zwei und überträgt dabei die meisten Randbedingungen.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Kante verlängern](Sketcher_Extend/de.md): Verlängert oder kürzt eine Linie oder einen Kreisbogen bis zu einer beliebigen Stelle oder bis zu einer Zielkante bzw. einem Zielpunkt.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Externe Geometrie](Sketcher_External/de.md): Projiziert Kanten und/oder Knoten, die zu einem Objekt außerhalb der Skizze gehören, auf die Skizzenebene. {{VersionMinus/de|1.0}}

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Externe Geometrie:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Externe Geometrie projizieren](Sketcher_Projection/de.md): Projiziert die Kanten externer Geometrie. {{Version/de|1.1}}

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Externe Geometrie schneiden](Sketcher_Intersection/de.md): Erstellt die Schnittkanten externer Geometrie mit der Skizzenebene. {{Version/de|1.1}}

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Pause](Sketcher_CarbonCopy/de.md): Paust alle Geometrien und Randbedingungen aus einer anderen Skizze in die aktuelle Skizze durch.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Ursprung auswählen](Sketcher_SelectOrigin/de.md): Wählt den Ursprung der Skizze aus.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Horizontale Achse auswählen](Sketcher_SelectHorizontalAxis/de.md): Wählt die horizontale Achse der Skizze aus.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Vertikale Achse auswählen](Sketcher_SelectVerticalAxis/de.md): Wählt die vertikale Achse der Skizze aus.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Versetzt ausgewählte Elemente oder kopiert sie wahlweise. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate/de.md): Dreht ausgewählte Elemente oder kopiert sie wahlweise. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Skalierungs-Transformation](Sketcher_Scale/de.md): Skaliert ausgewählte Elemente oder kopiert sie wahlweise. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Versatzkontur](Sketcher_Offset/de.md): Erstellt Kanten mit konstantem Abstand um die Ausgewählten Geometrien herum. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetrie](Sketcher_Symmetry/de.md): Erstellt gespiegelte Kopien ausgewählter Elemente.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Achsenausrichtung entfernen](Sketcher_RemoveAxesAlignment/de.md): Entfernt achsparallele Ausrichtungen ausgewählter Kanten, indem die Randbedingungen [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md) und [Vertikal festlegen](Sketcher_ConstrainVertical/de.md) durch die Randbedingungen [Parallel festlegen](Sketcher_ConstrainParallel/de.md) und [Rechtwinklig festlegen](Sketcher_ConstrainPerpendicular/de.md) ersetzt werden.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Gesamte Geometrie löschen](Sketcher_DeleteAllGeometry/de.md) (AlleGeometrienLöschen): Löscht sämtliche Geometrien und Randbedingungen aus der Skizze.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Alle Einschränkungen löschen](Sketcher_DeleteAllConstraints/de.md) (AlleRandbedingungenLöschen): Löscht alle Randbedingungen aus der Skizze.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Kopieren im Sketcher: Siehe [Kopieren, Ausschneiden und Einfügen](#Kopieren,_Ausschneiden_und_Einfügen.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Ausschneiden im Sketcher: Siehe [Kopieren, Ausschneiden und Einfügen](#Kopieren,_Ausschneiden_und_Einfügen.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Einfügen im Sketcher: Siehe [Kopieren, Ausschneiden und Einfügen](#Kopieren,_Ausschneiden_und_Einfügen.md).



### Sketcher-B-Spline-Werkzeuge 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [Geometrie in B-Spline wandeln](Sketcher_BSplineConvertToNURBS/de.md): Wandelt Kanten in B-Splines um.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Grad des B-Splines erhöhen](Sketcher_BSplineIncreaseDegree/de.md): Erhöht den Grad (die Ordnung) von B-Splines.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Grad des B-Splines verringern](Sketcher_BSplineDecreaseDegree/de.md): Verringert den Grad (die Ordnung) von B-Splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Vielfachheit eines Spline-Knotens erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md): Erhöht die Vielfachheit eines B-Spline-Knotens.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Vielfachheit eines Spline-Knotens verringern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md): Verringert die Vielfachheit eines B-Spline-Knotens.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Knoten einfügen](Sketcher_BSplineInsertKnot/de.md): Fügt einen Knoten in einen B-Spline ein oder erhöht die Vielfachheit eines vorhandenen Knotens.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Kurven verbinden](Sketcher_JoinCurves.md): Erstellt einen B-Spline, indem zwei vorhandene B-Splines oder andere Kanten verbunden werden. {{Version/de|0.21}}



### Sketcher visuell 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Unterbestimmte Elemente auswählen](Sketcher_SelectElementsWithDoFs/de.md): Wählt die nicht vollständig bestimmten Elemente einer Skizze aus.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Zugehörige Randbedingungen auswählen](Sketcher_SelectConstraints/de.md): Wählt die Randbedingungen aus, die (den) Skizzenelementen zugeordnet sind.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Zugehörige Geometrie auswählen](Sketcher_SelectElementsAssociatedWithConstraints/de.md) (ZugehörigeElementeAuswählen): Wählt die Skizzenelemente aus, denen Randbedingungen zugeordnet sind.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Überflüssige Randbedingungen auswählen](Sketcher_SelectRedundantConstraints/de.md): Wählt die redundanten Randbedingungen in der Skizze aus.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Widersprüchliche Randbedingungen auswählen](Sketcher_SelectConflictingConstraints/de.md): Wählt die widersprüchlichen Randbedingungen in der Skizze aus.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Kreishelfer für Bögen ein-/ausblenden](Sketcher_ArcOverlay/de.md): Blendet Kreishelfer (zugrundeliegende virtuelle Kreiskurven) für Kreisbögen in allen Skizzen ein bzw. aus. {{Version/de|1.0}}

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-Spline-Informationsebene ein-/ausblenden:

  - <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [B-Spline-Grad ein- / ausblenden](Sketcher_BSplineDegree/de.md): Blendet den Grad der B-Splines in allen Skizzen ein bzw. aus.

  - <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [B-Spline-Kontrollpolygon ein- / ausblenden](Sketcher_BSplinePolygon/de.md): Blendet das Kontrollpolygon der B-Splines in allen Skizzen ein bzw. aus.

  - <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [B-Spline-Krümmungskamm ein- / ausblenden](Sketcher_BSplineComb/de.md): Blendet den Krümmungskamm der B-Splines in allen Skizzen ein bzw. aus.

  - <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Vielfachheit der B-Spline-Knoten ein- / ausblenden](Sketcher_BSplineKnotMultiplicity/de.md): Blendet die Knotenvielfachheit der B-Splines in allen Skizzen ein bzw. aus.

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Gewicht der B-Spline-Kontrollpunkte anzeigen / ausblenden](Sketcher_BSplinePoleWeight/de.md): Blendet die Gewichte der Kontrollpunkte der B-Splines in allen Skizzen ein bzw. aus.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Interne Geometrie anzeigen / ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md): Löscht die interne Geometrie von Elementen oder stellt fehlende interne Geometrie wieder her.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Virtuellen Bereich wechseln](Sketcher_SwitchVirtualSpace/de.md): Blendet Randbedingungen ein bzw. aus oder wechselt den sichtbaren virtuellen Bereich.



### Veraltete Werkzeuge 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Klonen](Sketcher_Clone/de.md): Klont ein Skizzenelement. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Kontur schließen](Sketcher_CloseShape/de.md): Erstellt eine geschlossene Form, durch Anwendung der Randbedingung KoinzidentFestlegen auf Endpunkte. Dieses Werkzeug ist veraltet. Steht in {{VersionPlus/de|0.21}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Eckenerhaltende Verrundung erstellen](Sketcher_CreatePointFillet/de.md): Erstellt einen Bogen zwischen zwei nicht parallelen Linien, wobei ihr Eckpunkt erhalten bleibt. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Linien verbinden](Sketcher_ConnectLines/de.md): Verbindet Skizzenelemente, durch Anwendung der Randbedingung KoinzidentFestlegen auf Endpunkte. Dieses Werkzeug ist veraltet. Steht in {{VersionPlus/de|0.21}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Kopieren](Sketcher_Copy/de.md): Kopiert ein Skizzenelement. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Verschieben](Sketcher_Move/de.md): Verschiebt die ausgewählte Geometrie mit Bezug auf den zuletzt ausgewählten Punkt. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rechteckige Anordnung](Sketcher_RectangularArray/de.md): Erstellt eine Anordnung ausgewählter Skizzenelemente. Steht in {{VersionPlus/de|1.0}} nicht mehr zur Verfügung.



## Einstellungen

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Einstellungen](Sketcher_Preferences/de.md): Einstellungen für den Arbeitsbereich **Sketcher**.



## Bewährtes Vorgehen 

Jeder CAD-Benutzer entwickelt im Laufe der Zeit seine eigene Arbeitsweise, aber es gibt einige nützliche allgemeine Grundsätze, denen man folgen kann.

-   Eine Reihe einfacher Skizzen ist einfacher handzuhaben als eine komplexe einzelne Skizze. Beispielsweise kann eine erste Skizze für die grundlegenden 3D-Funktionen (entweder ein Block oder ein Drehteil) erstellt werden, während eine zweite Skizze Löcher oder Ausschnitte (Taschen) enthalten kann. Einige Details können weggelassen werden, um später als 3D-Formelemente realisiert zu werden. Es können Verrundungen in einer Skizze vermieden werden, wenn zu viele vorhanden sind, und diese als 3D-Formelemente hinzugefügt werden.
-   Es sollte immer ein geschlossenes Profil erstellt werden, da die Skizze sonst keinen Volumenkörper, sondern eine Reihe offener Seitenflächen erzeugt. Sollen einige der Objekte nicht in die Erstellung eines Volumenkörper einbezogen werden, können sie mit dem Werkzeug Hilfsgeometrie umschalten in Konstruktionselemente umgewandelt werden.
-   Die Funktion Automatische Randbedingungen kann aktiviert werde, um die Anzahl der Randbedingungen zu begrenzen, die manuell hinzugefügt werden müssen.
-   Nach einer allgemeinen Regel sollten zuerst geometrische, danach maßliche Randbedingungen verwendet werden und Sperren als letztes. Aber nicht vergessen: Regeln sind dazu da, gebrochen zu werden. Wenn Probleme beim Bearbeiten einer Skizze auftreten, kann es hilfreich sein, zuerst einige Objekte festzulegen, bevor ein Profil vervollständigt wird.
-   Eine Skizze sollte möglichst mit der Randbedingung Sperren auf den Ursprung (0,0) ausgerichtet werden. Wenn die Skizze nicht symmetrisch ist, setzt man einen ihrer Punkte auf den Ursprung oder wählt einfache runde Zahlen für die festzulegenden abstände.
-   Hat man die Möglichkeit, zwischen den Randbedingungen Abstand festlegen und Horizontalen Abstand festlegen bzw. Vertikalen Abstand festlegen zu wählen, sollte eine der letzteren bevorzugt werden. Horizontalen Abstand festlegen und Vertikalen Abstand festlegen sind vom Berechnungsaufwand her günstiger.
-   Im Allgemeinen eignen sich die folgenden Randbedingungen am besten: Horizontal und Vertikal Festlegen, Horizontalen und Vertikalen Abstand festlegen, (Punkt-zu-Punkt) Tangential festlegen. Wenn möglich sollten die folgenden nur begrenz eingesetzt werden: Abstand festlegen, (Kante-zu-Kante) Tangential festlegen von, Punkt auf Objekt festlegen; Symmetrie festlegen.
-   Wenn Zweifel an der Gültigkeit einer Skizze bestehen, nachdem diese vervollständigt wurde (Elemente werden grün), schließt man das Sketcher-Dialogfeld und verwendet <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Skizze Überprüfen](Sketcher_ValidateSketch/de.md).



## Anleitungen

-   [Sketcher-Lehrgang](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) von chrisb. Dies ist ein über 80 Seiten langes PDF-Dokument, das als ausführliches Handbuch für den Sketcher dient. Die Grundlagen zur Verwendung des Sketchers werden erläutert und es beschreibt detailreich die Erstellung geometrischer Formen sowie die einzelnen Randbedingungen.
-   [Grundlegendes Sketcher Tutorium](Basic_Sketcher_Tutorial/de.md) für Anfänger
-   [Sketcher Mikrotutorium - Beschränkungspraktiken](Sketcher_Micro_Tutorial_-_Constraint_Practices/de.md)
-   [Sketcher Anforderungen an Skizzen](Sketcher_requirement_for_a_sketch/de.md) Mindestanforderung für eine Skizze und vollständige Festlegung einer Skizze



## Skripten

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) enthält Beispiele für die Erstellung von Randbedingungen aus Python-Skripten.



## Beispiele

Ein paar Ideen, was mit den Sketcher-Werkzeugen erstellt werden kann, findet man unter: [Sketcher Beispiele](Sketcher_Examples/de.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/de
