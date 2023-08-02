---
- GuiCommand:
   Name: Part Sweep
   Name/de: Part Austragung
   MenuLocation: Formteil -> Sweep...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Loft/de
---

# Part Sweep/de



## Beschreibung

Das <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Austragung](Part_Sweep/de.md) Werkzeug wird verwendet, um eine Fläche, eine Schale oder eine Volumenkörperform aus einem oder mehreren Profilen (Querschnitten) zu erzeugen, die entlang einer Bahn projiziert werden.

Das Teil Austragungswerkzeug ähnelt dem <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Teil Ausformung](Part_Loft/de.md) mit dem Hinzufügen eines Pfades, um die Projektion zwischen Profilen zu definieren.

![](images/Part_Sweep_simple.png ) *Eine Volumenkörperaustragung, die aus einem einzelnen Profil (A) erzeugt wird, das entlang eines Pfades (B) projiziert wird.*



## Anwendung

1.  Drücke die **<img src="images/Part_Sweep.svg" width=16px> '''Austragung'''** Taste. Dadurch werden die Austragungsparameter in der [Aufgabenpaneel](Task_panel/de.md) geöffnet.
2.  Klicke in der linken Spalte *Verfügbare Profile* (vormals *Knoten/Kante/Draht/Fläche* in v0.16) auf das Element, das als Austragungsprofil verwendet werden soll, und klicke dann auf den rechten Pfeil, um es in der rechten Spalte *Ausgewählte Profile* zu platzieren (vormals *Austragen* in v0.16). Wiederhole dies, wenn mehr als ein Profil gewünscht wird. Verwende die Pfeiltasten nach oben und unten, um die ausgewählten Profile neu zu ordnen.
3.  Klicke auf die **Pfad Austragen** Schaltfläche und wähle dann einen der beiden Auswahlmodi:
    -   *Einzelsegmentauswahl*: Wähle eine oder mehrere zusammenhängende Kanten in der 3D Ansicht aus (drücke **CTRL** für Mehrfachauswahl) und klicke auf **Done**. Die Austragung wird nur entlang der ausgewählten Kanten erzeugt.
    -   *Komplette Pfadauswahl*: Wechsle zum Reiter Modell, wähle das 2D Objekt, das als Pfad im Baum verwendet werden soll, wechsle zurück zum Aufgabenbereich und klicke auf **Done**. Die Austragung wird entlang aller angrenzenden Kanten des 2D Objekts erzeugt.
4.  Definiere die Optionen [Volumenkörper](#Solid/de.md) und [Frenet](#Frenet/de.md).
5.  Klicke **OK**



### Anerkannte Geometrie 

-   **Profile**: können ein Punkt (Knoten), eine Linie (Kante), ein Draht oder eine Fläche sein. Kanten und Drähte können entweder offen oder geschlossen sein. Es gibt verschiedene [Profileinschränkungen und Komplikationen](Part_Sweep/de#Profileinschränkungen_und_Komplikationen.md), siehe unten, die Profile können auch aus Grundelementen (primitives) des Arbeitsbereiches Part, und aus Objekten und Skizzen des Arbeitsbereiches Draft stammen.

-   **Pfad**: kann eine Linie (Kante) oder eine Reihe von Verbindungslinien, Draht oder verschiedene Grundelemente des Arbeitsbereiches Part, Formelemente des Arbeitsbereiches Draft oder eine Skizze sein. Der Pfad wird oft direkt aus dem Hauptmodellfenster ausgewählt, kann aber auch in der [Baumansicht](Tree_view/de.md) ausgewählt werden. (Reiter Modell der [Combo-Ansicht](Combo_View.md)). Der Pfad kann entweder eine ganze geeignete Form oder eine geeignete Unterkomponente einer weiter fortgeschrittenen Form sein (z. B. eine Kante einer <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Würfel](Part_Box/de.md) ausgewählt werden als Pfad). Der Pfad kann entweder offen oder geschlossen sein und erzeugt somit entweder eine offene oder geschlossene Austragung. Ein geschlossener Pfad, wie z.B. ein Teilkreis, führt zu einer geschlossenen Austragung. Beispielsweise erzeugt die Austragung eines kleineren Kreises um eine Bahn mit einem größeren Kreis einen Torus.

-   [App-Link](App_Link/de.md)-Objekte, die zu geeigneten Objektarten verlinkt sind und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Profile und Pfade verwendet werden. <small>(v0.20)</small> 



## Eigenschaften



### Volumenkörper

Wenn \" Volumenkörper \" auf \" wahr \" gesetzt ist, erstellt FreeCAD einen Volumenkörper, vorausgesetzt, die Profile haben eine geschlossene Geometrie; wenn sie auf \" falsch \" gesetzt sind, erzeugt FreeCAD eine Fläche oder (wenn mehr als eine Fläche vorhanden ist) eine Hülle für offene oder geschlossene Profile.

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

Die Eigenschaft \"Frenet\" steuert, wie sich die Profilausrichtung ändert, wenn sie entlang des Suchpfades folgt. Wenn \"Frenet\" \"falsch\" ist, wird die Ausrichtung des Profils von Punkt zu Punkt konsistent gehalten. Die resultierende Form weist eine minimale Verdrehung auf. Wenn ein Profil entlang einer Spirale gefegt wird, führt dies unwillkürlich dazu, dass das Profil langsam kriecht (rotiert), während es der Spirale folgt. Wenn Du \"Frenet\" auf true setzst, wird ein solches Kriechen verhindert.

Wenn \"Frenet\" \"wahr\" ist, wird die Ausrichtung des Profils basierend auf lokalen Krümmungs- und Tangentialvektoren des Pfades berechnet. Dadurch bleibt die Ausrichtung des Profils beim Austragen entlang einer Helix konstant (da der Krümmungsvektor einer geraden Helix immer auf ihre Achse zeigt). Wenn der Weg jedoch keine Helix ist, kann die resultierende Form manchmal seltsam aussehende Verdrehungen aufweisen. Weitere Informationen findest Du unter[Frenet Serret Formeln](http://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).



### Übergang

\"Übergang\" setzt den Übergangsstil der Austragung an einer Verbindung im Pfad, wenn der Pfad den Eckübergang nicht definiert (z.B. wenn der Pfad ein Draht ist). Die Eigenschaft wird im [Aufgabenpaneel](Task_panel/de.md) nicht angezeigt und befindet sich nach der Erstellung der Austragung in den Eigenschaften.



## Profileinschränkungen und Komplikationen 

-   Ein Knoten oder Punkt
    -   Knoten oder Punkt darf nur als erstes und/oder letztes Profil in der Liste der Profile verwendet werden.
        -   Zum Beispiel
            -   Du kannst nicht von einem Kreis zu einem Punkt, zu einer Ellipse schwenken.
            -   Wie auch immer Du von einem Punkt zu einem Kreis zu einer Ellipse zu einem anderen Punkt austragen könntest.
-   Offene oder geschlossene Geometrieprofile können nicht in einer einzigen Austragung gemischt werden.
    -   In einem Durchlauf müssen alle Profile (Linien, Drähte usw.) entweder offen oder geschlossen sein.
        -   Zum Beispiel
            -   FreeCAD kann nicht zwischen einem Teilkreis und einer Standard-Bauteillinie wechseln.
-   Funktionen des Draft Arbeitsbereichs können in FreeCAD 0.14 oder höher direkt als Profil verwendet werden.
    -   -   Beispielsweise können die folgenden Draft Funktionen als Profile in einer Part Austragung verwendet werden.
            -   Entwurf Polygon.
            -   Entwurf Punkt, Linie, Draht,
            -   Entwurf B-Spline, Bezierkurve
            -   Entwurf Kreis, Ellipse, Rechteck,
-   PartDesign Skizzen
    -   Das Profil kann mit einer Skizze erstellt werden. Es wird jedoch nur eine gültige Skizze in der Liste angezeigt, die zur Auswahl steht.
    -   Die Skizze darf nur einen offenen oder geschlossenen Draht oder eine Linie enthalten (kann mehrere Linien sein, wenn diese Linien alle verbunden sind, wie sie dann ein einziger Draht sind).
-   Teile Arbeitsbereich
    -   das Profil kann ein gültiger geometrischer Bauteil Grundkörper sein, das mit dem [Part Grundelemente](Part_Primitives/de.md) Werkzeug erstellt werden kann.
        -   Zum Beispiel können die folgenden geometrischen Teile Grundkörper ein gültiges Profil sein.
            -   Punkt (Knoten), Linie (Kante)
            -   Helix, Spirale
            -   Kreis, Ellipse,
            -   Regelmäßiges Polygon
            -   Ebene (Fläche)



## Verweise

-   Da Austragung häufig zum Erstellen von Gewinden für Schrauben verwendet wird, solltest Du [Gewinde für Schrauben Tutorium](Thread_for_Screw_Tutorial/de.md) anschauen.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/de
