---
 GuiCommand:
   Name: Part Attachment
   Name/de: Part Befestigen
   MenuLocation: Part , Befestigung...
   Workbenches: Part_Workbench/de, PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: Placement/de,
Basic_Attachment_Tutorial
---

# Part EditAttachment/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_EditAttachment.svg  style="width:24px;"> **Part Befestigen** befestigt ein Objekt an einem oder mehreren anderen Objekten. Das befestigte Objekt ist mit den referenzierten Objekten verknüpft, d.h. wenn sich die [Positionierung](Std_Placement/de.md) oder die Geometrie der referenzierten Objekte ändert, wird die Positionierung des befestigten Objekts entsprechend aktualisiert.



## Befestigungswerkzeuge

Das Befestigen eines Objekts wird durch eins von vier Befestigungswerkzeugen (attach engines) gesteuert. Welches Werkzeug für ein Objekt voreingestellt ist, hängt von seiner Art ab. Das Befestigungswerkzeug eines Objekts kann über seine {{PropertyData/de|Attacher Engine}} geändert werden ({{Version/de|1.0}}) oder durch seine [ausgeblendete](Property_editor/de#Kontextmenü.md) (hidden) {{PropertyData/de|Attacher Type}}.

Die vorhandenen Befestigungswerkzeuge sind in der nachfolgenden Tabelle aufgelistet. Befestigungswerkzeuge kontrollieren die {{PropertyData/de|Placement}} (Positionierung) von Objekten. Alle Befestigungswerkzeuge können für alle Objekte, die diese Eigenschaft besitzen, verwendet werden. Aber die Ergebnisse der letzten drei sind am sinnvollsten, wenn die Form der Objekte mit der erwähnten \"Logischen Form\" zusammenpassen.

  Befestigungswerkzeug                       Befestigungstyp               Logische Form
    
  [3D-Engine](#3D-Engine.md)         Attacher::AttachEngine3D      
  [Plane-Engine](#Plane-Engine.md)   Attacher::AttachEnginePlane   Ebene Fläche die mit der XY-Ebene der Positionierung übereinstimmt
  [Line-Engine](#Line-Engine.md)     Attacher::AttachEngineLine    Gerade Kante die mit der Z-Achse der Positionierung kolliniear ist
  [Point-Engine](#Point-Engine.md)   Attacher::AttachEnginePoint   Knotenpunkt der mit dem Ursprung der Positionierung übereinstimmt

Der Rest dieser Seite hat den Fokus auf dem Werkzeug 3D-Engine. Die Verfahren der anderen Werkzeuge werden hier nur aufgelistet. Man beachte, dass die Verfahren der Plane-Engine in Wirklichkeit identisch sind mit denen der 3D-Engine.



## Anwendung

1.  Das Objekt auswählen, das befestigt werden soll.

2.  Eine der folgenden Möglichkeiten ausführen:
    -   Wenn das Objekt schon eine {{PropertyData/de|Map Mode}} besitzt: Im [Eigenschafteneditor](Property_editor/de.md) in dieses Feld klicken und die Schaltfläche **...** drücken, die dann erscheint.
    -   Den Menüeintrag **Part → <img src="images/Part_EditAttachment.svg" width=16px> Befestigung...** auswählen.

3.  Das Aufgaben-Fenster **Befestigen** wird geöffnet.

4.  Oben im Aufgaben-Fenster steht *Nicht befestigt*. Die erste Schaltfläche **Auswählen...** wird hervorgehoben, um anzuzeigen, dass eine Auswahl in der [3D-Ansicht](3D_view/de.md) erwartet wird.

5.  Einen Knoten, eine Kante oder eine Fläche bzw. Ebene auswählen, der/die zu einem anderen Objekt gehört.

6.  Im Eingabefeld rechts der Schaltfläche wird das referenzierte Objekt mit Subelement angezeigt. Wenn zum Beispiel eine Fläche eines [Part-Quaders](Part_Box/de.md) ausgewählt ist, kann das Feld {{Value|Box:Face6}} anzeigen. Die Bezeichnung (Label) der Schaltfläche zeigt jetzt die Art des Unterelements an.

7.  Die zur Verfügung stehenden Verfahren werden auf Basis der ausgewählten Bezugselemente und deren Reihenfolge gefiltert. Beispielsweise muss für die Verfahren [Ausrichtung O-Z-X](#Ausrichtung_O-Z-X.md) bis [Ausrichtung O-Y-X](#Ausrichtung_O-Y-X.md) das erste Bezugselement ein Knoten sein. Ist das erste Bezugselement ein Subelement einer anderen Art, werden sie von der Liste gelöscht.

8.  *Befestigungsverfahren: * wird jetzt oben im Aufgaben-Fenster angezeigt.

9.  Wahlweise einen anderen [Befestigungsmodus](#Attachment_mode/de.md) in der Liste auswählen. Für Informationen zu den Befestigungsverfahren fährt man mit dem Mauszeiger darüber, um einen QuickTip zum jeweiligen Verfahren anzuzeigen.

10. Abhängig vom ausgewählten Verfahren werden bis zu drei weitere Bezugselemente hinzugefügt, indem die Schaltflächen **Bezugselement2**, **Bezugselement3**, und **Bezugselement4** gedrückt und jeweils der Schritt 5 wiederholt werden. Es ist auch möglich, alle Bezugselemente vor der Auswahl eines Befestigungsverfahrens festzulegen.

11. Wahlweise einen [Befestigungsversatz](#Befestigungsversatz.md) eingeben.

12. 
    **OK**drücken.

13. Wo möglich, kann wahlweise die {{PropertyData/de|Map Path Parameter}} im [Eigenschafteneditor](Property_editor/de.md) geändert werden.



## Befestigungsverfahren



### 3D-Engine 

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">



#### Deaktiviert

Befestigen ist deaktiviert. Das Objekt kann durch Bearbeiten seiner Eigenschaft [Placement](Placement/de.md) (Positionierung) bewegt werden.



#### Ursprung versetzen 

Der Ursprung wird auf einen Knoten gesetzt. Die Ausrichtung wird weiterhin durch die Eigenschaft Placement des befestigten Objekts gesteuert.

:;Kombinationen der Bezugselemente:

:   Knoten.



#### X Y Z des Objekts 

Die Positionierung wird der Positionierung eines verknüpften Objekts angeglichen.

:;Kombinationen der Bezugselemente:

:   Alle
:   Kegelschnitt (Elipse, Parabel,Hyperbel).



#### X Z Y des Objekts 

Die X-, Y- und Z- Achsen werden entsprechend den lokalen X-, Z- und -Y- Achsen eines verknüpften Objekts angeglichen.

:;Kombinationen der Bezugselemente:

:   Alle
:   Kegelschnitt.



#### Y Z X des Objekts 

Die X-, Y- und Z- Achsen werden entsprechend den lokalen Y-, Z- und X- Achsen eines verknüpften Objekts angeglichen.

:;Kombinationen der Bezugselemente:

:   Alle
:   Kegelschnitt.



#### XY auf Ebene 

Die XY-Ebene wird zu einer ebenen Fläche deckungsgleich ausgerichtet.

:;Kombinationen der Bezugselemente:

:   Ebene



#### XY tangential zur Oberfläche 

Die XY-Ebene wird an einem Knoten tangential zu einer Oberfläche ausgerichtet.

:;Kombinationen der Bezugselemente:

:   Fläche, Knoten
:   Knoten, Fläche



#### Z tangential zur Kante 

Die Z-Achse wird tangential zu einer Kante ausgerichtet. Ein optionaler Knoten legt fest, an welcher Stelle.

Ist kein Knoten verknüpft, legt die {{PropertyData/de|Map Path Parameter}} den Punkt fest.

:;Kombinationen der Bezugselemente:

:   Kante
:   Kante, Knoten
:   Knoten, Kante



#### Frenet NBT 

<img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

Die X- und Y-Achsen werden an der normalen (N) und der binormalen (B) Achse des [Frenet-Serret-Koordinatensystems](https://de.wikipedia.org/wiki/Frenetsche_Formeln) ([Frenet-Serret coordinate system](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)) in einem Punkt auf einer gekrümmten Kante ausgerichtet. Ein optionaler Knoten legt fest, an welcher Stelle.

Ist kein Knoten verknüpft, legt die {{PropertyData/de|Map Path Parameter}} den Punkt fest. Der Ursprung des Objekts wird auf den Knoten verschoben, wenn dieser zuerst ausgewählt wurde oder er wird an der Kurve belassen, wenn die Kurve zuerst ausgewählt wurde.

*Frenet NBT* entspricht *Z tangential zur Kante*, außer dass die X-Achse eindeutig festgelegt ist.

:;Kombinationen der Bezugselemente:

:   Kurve
:   Kurve, Knoten
:   Knoten, Kurve



#### Frenet TNB 

<img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

Die X- und Y-Achsen werden an der tangentialen (T) und der normalen (N) Achse des Frenet-Serret-Koordinatensystems in einem Punkt auf einer gekrümmten Kante ausgerichtet. Ein optionaler Knoten legt fest, an welcher Stelle.

Siehe [Frenet NBT](#Frenet_NBT.md).



#### Frenet TBN 

<img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

Die X- und Y-Achsen werden an die tangentiale (T) und die binormale Achse des Frenet-Serret Koordinatensystems in einem Punkt auf einer gekrümmten Kante angeglichen. Ein optionaler Knoten legt fest, an welcher Stelle.

Siehe [Frenet NBT](#Frenet_NBT.md).



#### Konzentrisch

Die XY-Ebene wird an dem [Krümmungskreis](https://de.wikipedia.org/wiki/Krümmungskreis) ([osculating circle](https://en.wikipedia.org/wiki/Osculating_circle)) in einem Punkt auf einer Kante ausgerichtet. Ein optionaler Knoten legt fest, an welcher Stelle.

Ist kein Knoten verknüpft, legt die {{PropertyData/de|Map Path Parameter}} den Punkt fest.

:;Kombinationen der Bezugselemente:

:   Kurve
:   Kreis
:   Kurve, Knoten
:   Kreis, Knoten
:   Knoten, Kurve
:   Knoten, Kreis



#### Drehung Abschnitt 

Die Y-Achse wird an der Achse des Krümmungskreises in einem Punkt auf einer Kante ausgerichtet. Ein optionaler Knoten legt fest, an welcher Stelle.

Siehe [Konzentrisch](#Konzentrisch.md).



#### XY-Ebene durch 3 Punkte 

Die XY-Ebene wird so ausgerichtet, dass sie durch drei Knoten verläuft. Die X-Achse verläuft durch die ersten zwei Knoten.

:;Kombinationen der Bezugselemente:

:   Knoten, Knoten, Knoten
:   Linie, Knoten
:   Knoten, Linie
:   Linie, Linie



#### XZ-Ebene durch 3 Punkte 

Die XZ-Ebene wird so ausgerichtet, dass sie durch drei Knoten verläuft. Die X-Achse verläuft durch die ersten zwei Knoten.

Siehe [XY-Ebene durch 3 Punkte](#XY-Ebene_durch_3_Punkte.md).



#### Faltung

<img alt="" src=images/Attacher_mode_Folding.png  style="width:250px;">

Dies ist ein spezieller Modus zum Falten von Polyedern. Vier Linien mit einem gemeinsamen Punkt in dieser Reihenfolge auswählen: erste Verbindungslinie (1), erste Faltlinie (2), zweite Faltlinie (3), zweite Verbindungslinie (4). Zum ableiten des Koordinatensystems werden die Verbindungslinien deckungsgleich ausgerichtet, indem Linie 1 um Linie 2 geschwenkt wird und Linie 4 um Linie 3. Der Ursprung wird auf den gemeinsamen Punkt gesetzt, die X-Achse der Linie 2 angeglichen und die Y-Achse2 der Richtung der deckungsgleichen Verbindungslinien angeglichen.

:;Kombinationen der Bezugselemente:

:   Linie, Linie, Linie, Linie



#### Inertial-Koordinatensystem 

Die X-, Y-, und Z-Achsen werden an denen eines Inertial-Koordinatensystems (Trägheitskoordinatensystem) ausgerichtet, das aus den Hauptachsen der Massenträgheit und dem Masseschwerpunkt abgeleitet wird.

:;Kombinationen der Bezugselemente:

:   Alle
:   Alle,Alle
:   Alle, Alle, Alle
:   Alle, Alle, Alle, Alle



#### Ausrichten O-Z-X 

Der Ursprung wird auf den ersten Knoten gesetzt. Die X- und Z-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Befestigungsverfahren der Art O-X-Y](O-X-Y_Type_Attachment_Modes/de.md) für weitere Eizelheiten.

:;Kombinationen der Bezugselemente:

:   Knoten, Knoten, Knoten
:   Knoten, Knoten, Linie
:   Knoten, Linie, Knoten
:   Knoten, Linie, Linie
:   Knoten, Knoten
:   Knoten, Linie



#### Ausrichten O-Z-Y 

Der Ursprung wird auf den ersten Knoten gesetzt. Die Z-, und Y-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Ausrichten O-Z-X](#Ausrichten_O-Z-X.md).



#### Ausrichten O-X-Y 

Der Ursprung wird auf den ersten Knoten gesetzt. Die X- und Y-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Ausrichten O-Z-X](#Ausrichten_O-Z-X.md).



#### Ausrichten O-X-Z 

Der Ursprung wird auf den ersten Knoten gesetzt. Die X- und Z-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Ausrichten O-Z-X](#Ausrichten_O-Z-X.md).



#### Ausrichten O-Y-Z 

Der Ursprung wird auf den ersten Knoten gesetzt. Die Y- und Z-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Ausrichten O-Z-X](#Ausrichten_O-Z-X.md).



#### Ausrichten O-Y-X 

Der Ursprung wird auf den ersten Knoten gesetzt. Die Y- und X-Achsen werden in Richtung auf einen Knoten zu oder entlang einer Linie ausgerichtet.

Siehe [Ausrichten O-Z-X](#Ausrichten_O-Z-X.md).



#### XY parallel zur Ebene 


{{Version/de|1.0}}

Die XY-Ebene wird parallel zur XY-Ebene der Positionierung eines verknüpften Objekts ausgerichtet und verlauft durch einen Knoten. Der Ursprung wird auf den auf die XY-Ebene projizierten Ursprung des verknüpften Objekts gesetzt.

Man beachte, dass das gesamte Objekt ausgewählt werden muss und nicht nur ein Teilelement, wie eine Fläche oder Ebene.

:;Kombinationen der Bezugselemente:

:   Ein beliebiges komplettes Objekt (mit einer {{PropertyData/de|Placement}}), Knoten


<div class="toccolours mw-collapsible mw-collapsed">



### Plane-Engine 


<div class="mw-collapsible-content">

-   Deactivated
-   Translate origin
-   Object\'s XY
-   Object\'s XZ
-   Object\'s YZ
-   Plane face
-   Tangent to surface
-   Normal to edge
-   Frenet NB
-   Frenet TN
-   Frenet TB
-   Concentric
-   Revolution Section
-   Plane by 3 points
-   Normal to 3 points
-   Folding
-   Inertia 2-3
-   Align O-N-X
-   Align O-N-Y
-   Align O-X-Y
-   Align O-X-N
-   Align O-Y-N
-   Align O-Y-X
-   XY parallel to plane <small>(v1.0)</small> 


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Line-Engine 


<div class="mw-collapsible-content">

-   Deactivated
-   Object\'s X
-   Object\'s Y
-   Object\'s Z
-   Axis of curvature
-   Directrix1
-   Directrix2
-   Asymptote1
-   Asymptote2
-   Tangent
-   Normal to edge
-   Binormal
-   Through two points
-   Intersection <small>(v1.0)</small> 
-   Proximity line
-   1st principal axis
-   2nd principal axis
-   3rd principal axis
-   Normal to surface


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Point-Engine 


<div class="mw-collapsible-content">

-   Deactivated (Deaktiviert)
-   Object\'s origin (Objektursprung)
-   Focus1 (Fokus1)
-   Focus2 (Fokus2)
-   On edge (Auf Kante)
-   Center of curvature (Krümmungsmittelpunkt)
-   Center of mass (Schwerpunkt)
-   Vertex (Knoten)
-   Proximity point 1 (Näherungspunkt 1)
-   Proximity point 2 (Näherungspunkt 2)


</div>


</div>



## Befestigungsversatz

Befestigungsversatz wird aktiviert, wenn ein anderes Befestigungsverfahren als *Deaktiviert* ausgewählt wurde. Er wird eingesetzt, um einen linearen oder einen Winkelversatz innerhalb des Koordinatensystems der Befestigung (attachment coordinate system, ACS) anzuwenden, der durch das Befestigungsverfahren und die referenzierten Objekte festgelegt wird.

-   **In X-Richtung**: legt einen Versatzabstand entlang der X-Achse des ACS fest.

-   **In Y-Richtung**: legt einen Versatzabstand entlang der Y-Achse des ACS fest.

-   **In Z-Richtung**: legt einen Versatzabstand entlang der Z-Achse des ACS fest.

-   **Um die X-Achse**: dreht das befestigte Element um die X-Achse des ACS.

-   **Um die Y-Achse**: dreht das befestigte Element um die Y-Achse des ACS.

-   **Um die Z-Achse**: dreht das befestigte Element um die Z-Achse des ACS.

-   **Seiten umdrehen**: Wenn aktiviert, wird die Befestigung umgekehrt. Dies entspricht der Drehung des Objekts um 180° um die Y-Achse des ACS.



## Einschränkungen

-   Falls die Auswahl zweier Linien den Fehler ergibt \"points are collinear. Can\'t make a plane\" endet, Kann man versuchen stattdessen drei Knoten auszuwählen [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594) (engl.).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/de
