---
 GuiCommand:
   Name: Part Sweep
   Name/de: Part Austragung
   MenuLocation: Formteil , Sweep...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Loft/de
---

# Part Sweep/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Austragung](Part_Sweep/de.md) (Sweep) wird verwendet, um eine Fläche, eine Schale (dünnwandiges Objekt) oder eine Festkörper-Form aus einem oder mehreren Profilen (Querschnitten) entlang eines Spines (Rückgratkurve) zu erzeugen.

Der Befehl Part Austragung ähnelt dem <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Ausformung](Part_Loft/de.md) mit einem hinzugefügten Spine.

<img alt="" src=images/Part_Sweep_simple.png  style="width:400px;"> 
*Ein Festkörper-Sweep-Objekt aus einem einzelnen Profil (A) entlang eines Spines (B) ausgetragen*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl auzurufen:
    -   Die Schaltfläche **<img src="images/Part_Sweep.svg" width=16px> [Sweep...](Part_Sweep/de.md)** drücken.
    -   Den Menüeintrag **Part → <img src="images/Part_Sweep.svg" width=16px> Sweep...** auswählen.

2.  Der [Aufgaben-Bereich](Task_panel/de.md) Sweep wird geöffnet.

3.  In der linken Liste *Verfügbare Profile* ein Profil auswählen und auf den Pfeil nach rechts klicken, um es in die rechte Liste *Ausgewählte Profile* zu verschieben.

4.  Wiederholen, wenn mehr als ein Profil verwendet werden soll.

5.  Die Pfeiltasten nach oben und nach unten ändern die Reihenfolge der Liste, aber dias hat keinen Einfluss auf das Ergebnis. Die Lage der Profile entlang des Spines bestimmt, in welcher Reihenfolge sie verwendet werden.

6.  Die Schaltfläche **Sweep-Pfad** drücken; danach hat man zwei Möglichkeiten den Spine auszuwählen:
    -   *Abschnitte auswählen*: Eine Kante oder mehrere zusammenhängende Kanten in der [3D-Ansicht](3D_view/de.md) auswählen (für Mehrfachauswahl **strg** (ctrl) drücken) und die Schaltfläche **Fertig** drücken. Das Sweep-Objekt wird nur entlang der ausgewählten Kanten ausgetragen.
    -   *Den Kompletten Pfad auswählen*: Zur [Baumansicht](Tree_view/de.md) wechseln, das Objekt auswählen, das als Spine verwendet werden soll, zum Aufgaben-Bereich zurück wechseln und die Schaltfläche **Fertig** drücken. Das Sweep-Objekt wird entlang aller aneinandergrenzenden Kanten ausgetragen, die das Objekt enthält.

7.  Wahlweise die Optionen [Festkörper erstellen](#Festkörper.md) und [Frenet](#Frenet/de.md) aktivieren.

8.  
    **OK**anklicken



### Akzeptierte Geometrie 

-   **Profile** können aus einem Punkt (Knoten), einer Linie (Kante), einem Kantenzug oder einer Fläche bestehen. Kanten und Kantenzüge können entweder offen oder geschlossen sein. Es gibt verschiedene [Einschränkungen](#Einschränkungen.md), siehe unten.

-   **Spine**: kann aus einer Linie (Kante), einer Reihe von verbundenen Linien, einem Kantenzug, verschiedenen Grundelemente des Arbeitsbereiches Part, Objekten des Arbeitsbereiches Draft oder einer Skizze bestehen. Der Spine kann offen oder gesclossen sein.

-   [App-Link](App_Link/de.md)-Objekte, die zu geeigneten Objektarten verlinkt sind und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Profile und Pfade verwendet werden. {{Version/de|0.20}}



## Optionen



#### Festkörper

Wenn \"Festkörper erstellen\" auf \"true\" gesetzt ist, erstellt FreeCAD einen Festkörper, vorausgesetzt, die Profile sind geschlossen; wenn es auf \"false\" gesetzt ist, erstellt FreeCAD stets eine Fläche oder eine Schale, sowohl aus offenen als auch aus geschlossenen Profilen.

#### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

Die Eigenschaft \"Frenet\" steuert, wie sich die Profilausrichtung ändert, Während sie dem Sweep-Spine folgt. Wenn \"Frenet\" \"falsch\" ist, wird die Ausrichtung des Profils von Punkt zu Punkt konsistent gehalten. Die resultierende Form weist die kleinstmögliche Verdrehung auf. Wenn ein Profil entlang einer Spirale ausgetragen wird, führt dies unwillkürlich dazu, dass das Profil langsam kriecht (dreht), während es der Spirale folgt. Wird \"Frenet\" auf \"true\" gesetzt, wird dies verhindert.

Wenn \"Frenet\" \"wahr\" ist, wird die Ausrichtung des Profils basierend auf lokalen Krümmungs- und Tangentialvektoren des Pfades berechnet. Dadurch bleibt die Ausrichtung des Profils beim Austragen entlang einer Helix konstant (da der Krümmungsvektor einer geraden Helix immer auf ihre Achse zeigt). Wenn der Weg jedoch keine Helix ist, kann die resultierende Form manchmal seltsam aussehende Verdrehungen aufweisen. Weitere Informationen befinden sich unter [Frenet-Serret-Formeln](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).



#### Übergang

\"Transition\" (Übergang) legt die Art des Übergangs des Sweep-Objekts an nicht-tangentialen Verbindungen (Knicken) im Spline fest. Die Eigenschaft wird im Aufgaben-Bereich nicht angezeigt und befindet sich nach der Erstellung des Sweep-Objekts in den [ Eigenschaften](Property_editor/de.md).



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Sweep-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Sweep}}

-    {{PropertyData/de|Sections|LinkList}}: listet die verwendeten Querschnitte auf.

-    {{PropertyData/de|Spine|LinkSub}}: Spine (Rückgratkurve,Pfad) an dem entlang das Sweep-Objekt ausgetragen wird.

-    {{PropertyData/de|Solid|Bool}}: true oder false (Standardwert). True bewirkt, dass ein Festkörper (Solid) erstellt wird.

-    {{PropertyData/de|Frenet|Bool}}: true oder false (Standardwert). True bewirkt, dass der Frenet-Algorithmus eingesetzt wird.

-    {{PropertyData/de|Transition|Enumeration}}: Übergangsmodus mit den Optionen *Transformed*, *Right corner* oder *Round corner*.



## Einschränkungen



### Knoten oder Punkt 

Ein Knoten oder Punkt darf nur als erstes und/oder letztes Profil eingesetzt werden.
Zum Beispiel:

-   Eine Form kann nicht von einem Kreis über einen Punkt zu einer Ellipse ausgetragen werden.
-   Es ist aber möglich eine Form von einem Punkt über einen Kreis und eine Ellipse zu einem weiteren Punkt auszutragen.



### Profile

In einem Sweep-Objekt müssen alle Profile (Linien, Linienzüge usw.) entweder offen oder geschlossen.
Zum Beispiel:

-   FreeCAD kann ein Sweep-Objekt nicht zwischen einem Part-Kreis und einer Part-Linie austragen.



### Skizzen

-   Das Profil kann mit einer Skizze erstellt werden. Es werden aber nur geeignete Skizzen werden zur Auswahl im Aufgaben-Bereich angezeigt.
-   Die Skizze darf nur einen Linienzug oder eine Linie, jeweils entweder offen oder geschlossen, enthalten (Es können mehrere Linien sein, wenn alle miteinander verbunden sind und einen einzelnen Linienzug bilden).



### Objekte des Arbeitsbereichs Draft 

Ein Profil kann ein Objekt des Arbeitsbereichs [Draft](Draft_Workbench/de.md) sein.
Die folgenden Objekte können geeignete Profile sein:

-   Punkt
-   Linie, Linienzug
-   B-Spline, Bézierkurve
-   Kreis, Ellipse
-   Rechteck, Vieleck



### Objekte des Arbeitsbereichs Part 

Eine Profilkurve kann ein Part-Objekt sein, dass mit dem Befehl [Part Grundelemente](Part_Primitives/de.md) erstellt wurde.
Die folgenden Objekte können geeignete Profile sein:

-   Punkt (Knoten)
-   Linie (Kante)
-   Wendel, Spirale
-   Kreis, Ellipse
-   Regelmäßiges Vieleck
-   Ebene (Fläche)



## Verweise

-   Ein Sweep-Objekt wird häufig zum Erstellen von Gewinden für Schrauben verwendet, siehe die Anleitung [Gewinde für Schrauben](Thread_for_Screw_Tutorial/de.md) für weitere Informationen.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/de
