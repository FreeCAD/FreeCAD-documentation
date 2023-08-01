---
- GuiCommand:
   Name:Part Attachment
   Name/de:Part Befestigen
   MenuLocation:Part → Befestigung...
   Workbenches:[Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Positionierung](Placement/de.md),
[Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) [Part Part2DObject](Part_Part2DObject/de.md)
---

# Part EditAttachment/de



## Beschreibung

**Part Befestigen** ist ein Hilfsmittel, um ein Objekt an ein anderes anzuhängen. Das angehängte Objekt ist an dem anderen Objekt befestigt, d.h. wenn die Platzierung des letzteren nachträglich geändert wird, wird das angehängte Objekt auf seine neue Position aktualisiert.



## Anwendung

1.  Wähle das Objekt aus, das angehängt werden soll.
2.  Gehe in das Menü **Formteil → Attachment\...**.
3.  **Hinweis**: Wenn in [PartDesign](PartDesign_Workbench/de.md) gearbeitet wird und Skizzen, Bezugsgeometrien oder Grundkörper erstellt werden, sind die Schritte 1 und 2 überflüssig: der Anhang Dialog wird automatisch aufgerufen.
4.  Unter **Anhang** Parameter kann *Nicht angehängt* gelesen werden. Die erste Schaltfläche unten ist mit **Auswahl...** beschriftet, um anzuzeigen, dass sie eine Auswahl in der 3D Ansicht erwartet.
5.  Wähle ein Topologieelement auf dem Objekt, an das angehängt werden soll: Knoten, Kante oder Fläche/Ebene. Bezugsgeometrien aus [Part Behältern](Std_Part/de.md) sind ebenfalls wählbar.
6.  Die Beschriftung der ersten Schaltfläche übernimmt nun die Art der ausgewählten Topologie. In dem weißen Feld rechts daneben wird das referenzierte Objekt und sein Element hinzugefügt. Wenn zum Beispiel eine Fläche auf einem Grundelement Würfel ausgewählt ist, zeigt das Feld Box:Face6 an.
7.  Wähle einen [Anhangsmodus](#Anhangsmodus.md) aus der Liste. Die verfügbaren Modi werden nach den ausgewählten Referenzen gefiltert. **Angefügt mit Modus ** wird unter der **Anhang**s Überschrift angezeigt.

    :   Für Live Informationen über die Anhangsmodi fahre mit der Maus über einen der Modi in der Liste damit eine Werkzeugspitze erscheint.
8.  Füge optional bis zu 3 weitere Referenzen durch drücken der Tasten **Referenz2**, **Referenz3** und **Referenz4** und wiederholen von Schritt 4 hinzu.
9.  Lege optional einen [Anhang Versatz](#Anhang_Versatz.md) fest.
10. Drücke **OK**.



## Optionen

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">



### Befestigungsmodus



#### Deaktiviert

Standard, keine Referenz gewählt.



#### Normal zur Kante 

Das Objekt wird senkrecht zur Kante gemacht. Eine optionale Knotenreferenz definiert die Position.

:; Referenzkombinationen:

:   Kante
:   Kante, Knoten
:   Knoten, Kante

Siehe [Align O-X-Y type attachment modes](O-X-Y_type_attachment_modes.md) für weitere Details zu den folgenden Modi:



#### Ausrichten O-Z-X 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet dann die Normalen und die horizontalen Achsen der Ebene am Knoten/an der Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ausrichten O-Z-Y 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet seine Normalen und vertikalen Achsen in Richtung Knoten/Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ausrichten O-X-Y 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet die horizontalen und vertikalen Achsen des Objekts am Knoten/an der Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ausrichten O-X-Z 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet seine horizontale Ebenenachse und seine Normale am Knoten bzw. entlang der Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ausrichten O-Y-Z 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet die vertikale Achse und die Normale des Objekts am Knoten/an der Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ausrichten O-Y-X 

Passt den Ursprung des Objekts an den ersten referenzierten Knoten an und richtet die vertikalen und horizontalen Achsen des Objekts am Knoten/an der Linie aus.

:; Referenz Kombinationen:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Kante
:   Knoten, Kante, Knoten
:   Knoten, Kante, Kante
:   Knoten, Knoten
:   Knoten, Kante



#### Ursprung versetzen 

Der Objektursprung wird am entsprechenden Knoten ausgerichtet. Die Ausrichtung wird durch die Eigenschaft [Platzierung](Placement/de.md) gesteuert.

:; Referenzkombinationen:

:   Knoten.



#### Objekt XY 

Die Ebene wird an der lokalen XY Fläche des verknüpften Objekts ausgerichtet.

:; Referenzkombinationen:

:   Alle, Konisch.



#### Objekt XZ 

Die Ebene wird an der lokalen XZ Fläche des verknüpften Objekts ausgerichtet.

:; Referenzkombinationen:

:   Alle, Konisch.



#### Objekt XZ 

Die Ebene wird an der lokalen YZ Ebene des verknüpften Objekts ausgerichtet.

:; Referenzkombinationen:

:   Alle, Konisch.



#### Ebene Fläche 

Die Ebene wird zur ebenen Fläche deckungsgleich ausgerichtet.

:;Referenzkombinationen:

:   Ebene



#### Tangente zur Oberfläche 

Die Ebene wird im Knoten tangential zur Oberfläche gemacht.

:; Referenzkombinationen:

:   Fläche, Knoten
:   Knoten, Fläche

#### Frenet NB 

Ebene wird auf normal-binormale (NB) Achsen von [Frenet-Serret Koordinaten](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) an den Punkt der Kantenkurve gesetzt, der dem Knoten am nächsten liegt (oder durch die MapPathParameter Eigenschaft definiert wird, wenn der Knoten nicht verknüpft ist). Der Objektursprung wird auf den Knoten übersetzt, wenn der Knoten zuerst liegt, oder auf der Kurve gehalten, wenn die Kante zuerst liegt. Dieser Modus ist ähnlich wie *Normal zur Kante*, außer dass die X Achse wohldefiniert ist.

:;Referenzkombinationen:

:   Kurve
:   Kurve, Knoten
:   Knoten, Kurve
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

#### Frenet TN 

Ebene wird auf tangentig-normale (TN) Achsen von [Frenet-Serret Koordinaten](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) an den Punkt der Kurve der Kante gesetzt, die dem Knoten am nächsten liegt (oder durch die MapPathParameter Eigenschaft definiert wird, wenn der Knoten nicht verknüpft ist). Der Ursprung der Skizze wird auf den Knoten übersetzt, wenn der Knoten zuerst liegt, oder auf der Kurve gehalten, wenn die Kante zuerst liegt. Wenn die Kurve planar ist, ist die Skizzierebene effektiv die Ebene der Kurve.

:;Referenzkombinationen:

:   Kurve
:   Kurve, Knoten
:   Knoten, Kurve
:   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

#### Frenet TB 

Ebene wird auf tangential-binormale (TB) Achsen von [Frenet-Serret Koordinaten](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) an den Punkt der Kantenkurve festgelegt, der dem Knoten am nächsten liegt (oder durch die MapPathParameter Eigenschaft definiert wird, wenn der Knoten nicht verknüpft ist). Der Ursprung der Skizze wird auf den Knoten übersetzt, wenn der Knoten zuerst liegt, oder auf der Kurve gehalten, wenn die Kante zuerst liegt.

:;Referenzkombinationen:

:   Kurve
:   Kurve, Knoten
:   Knoten, Kurve
:   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">



#### Konzentrisch

Richtet sich an der Ebene zum Schmiegungskreis einer Kante aus. Optionale Knoten Verknüpfung definiert, wo.

:; Referenzkombinationen:

:   Kurve
:   Kreis
:   Kurve, Knoten
:   Kreis, Knoten
:   Knoten, Kurve
:   Knoten, Kreis



#### Drehung Abschnitt 

Die Ebene steht senkrecht zur Kante, und die Y Achse ist mit der Achse des Schmiegungskreises abgestimmt. Optionale Knoten Verbindung definiert, wo.

:; Referenzkombinationen:

:   Kurve
:   Kreis
:   Kurve, Knoten
:   Kreis, Knoten
:   Knoten, Kurve
:   Knoten, Kreis



#### Ebene durch 3 Punkte 

Richtet die XY Ebene so aus, dass sie durch drei Knoten verläuft.

:; Referenzkombinationen:

:   Knoten, Knoten, Knoten
:   Linie, Knoten
:   Knoten, Linie
:   Linie, Linie



#### Normale zu 3 Punkten 

Richtet die Ebene so aus, dass sie durch die ersten beiden Knoten verläuft und senkrecht zu der Ebene, die durch 3 Knoten verläuft.

:; Referenzkombinationen:

:   Knoten, Knoten, Knoten
:   Linie, Knoten
:   Knoten, Linie
:   Linie, Linie



#### Faltung

Spezialmodus zum Falten von Polyedern. Wähle 4 Kanten in der Reihenfolge: Verbindungskante, Faltlinie, andere Faltlinie, andere Verbindungskante. Die Ebene wird ausgerichtet, um die erste Kante zu falten. Im folgenden Bild ist es nicht erforderlich, dass beide zu faltenden Blätter gleich sind.

:; Referenzkombinationen:

:   Linie, Linie, Linie, Linie
:   ![ 250px](images/Attacher_mode_Folding.png )



#### Trägheit 2-3 

Das Objekt wird an einer Ebene befestigt, welche durch die zweite und dritte Hauptträgheitsachse (Massenschwerpunkt) verläuft.

:; Referenzkombinationen:

:   Alle
:   Alle,Alle
:   Alle, Alle, Alle
:   Alle, Alle, Alle, Alle



### Befestigungsversatz

Attachment Versatz wird verwendet, um einen linearen oder rotatorischen Versatz vom referenzierten Objekt anzuwenden. Das heißt, die Versätze beziehen sich auf das *lokale* Koordinatensystem, nicht auf das globale. Er wird aktiv, wenn ein anderer Anbringungsmodus als *Deaktiviert* gewählt wurde.

-   **X**: legt einen Versatzabstand in der X Achse des Referenzobjekts fest.

-   **Y**: legt einen Versatzabstand in der Y Achse des Referenzobjekts fest.

-   **Z**: legt einen Versatzabstand in der Z Achse des Referenzobjekts fest. Diese Koordinate ist für den häufigen Anwendungsfall zu verwenden, dass du eine Skizze rechtwinklig zur Ebene versetzen möchtest.

-   **Gieren**: dreht das angehängte Objekt um die Z Achse des Referenzobjekts.

-   **Neigung**: dreht das angehängte Element entlang der Y Achse des Referenzobjekts.

-   **Wanken**: dreht das angehängte Element entlang der X Achse des Referenzobjekts.

-   **Seiten kippen**: Wenn angehakt, wird das angehängte Objekt aus der XY Ebene umgekehrt.



## Einschränkungen

-   [Std Teil](Std_Part/de.md) und [PartDesign Körper](PartDesign_Body/de.md) Behälter werden nicht unterstützt. Während es möglich ist, Befestigungsmodi zu verwenden, um sie auszurichten, wird die Befestigung nicht parametrisch verknüpft.
-   Falls das Auswählen zweier Linien in einem \"Traceback\" mit der Meldung \"points are collinear. Can\'t make a plane\" endet, versuche stattdessen drei Punkte auszuwählen [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594) (engl.).





{{Part_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/de
