# PartDesign project/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}


<div class="mw-translate-fuzzy">

Hier der Projektplan für die **TeileKonstruktion** als Teil des [Entwicklungsfahrplans](Development_roadmap/de.md).


</div>


<div class="mw-translate-fuzzy">

## Zweck und Grundsätze 

Dies ist ein Softwareentwicklungsprojekt, das darauf abzielt, die Teilekonstruktionsfähigkeiten zu implementieren. Es geht um Implementierung einiger **Kernfuktionen** in die CAD Module von FreeCAD, **Teil, TeileKonstruktion und Zusammenbau**.


</div>


<div class="mw-translate-fuzzy">

Die Entwicklungsschritte werden hier geplant und im Problemverfolgungssystem verfolgt, um eine gut gebildetes Änderungsprotokoll zu erhalten: [Problemverfolger](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)


</div>

## Ergebnis

Ziel des Projekts ist es, FreeCAD in die Lage zu versetzen, eine Konstruktionsaufgabe wie die rechte auszuführen.

<img alt="" src=images/Gripper.jpg  style="width:300px;">


<div class="mw-translate-fuzzy">

Dies wird durch die Verwendung des **Skizzierers** und der **PartDesign** zur Konstruktion eines Sonderteils erreicht und **Part**, um ein Normteil als STEP (wie das Linearlager) zu laden. Die **Baugruppe** setzt das Ganze mit Beschränkungen zusammen.


</div>


<div class="mw-translate-fuzzy">

Ein wichtiges Ergebnis ist auch die **Funktions Bearbeitungs Methodik**. Dadurch erhält der Benutzer einen intuitiven Ansatz zur Instanziierung und Bearbeitung von Funktionen. Dies ist wichtig für alle weiteren Module und Arbeitsbereiche, die noch kommen werden, um einer einheitlichen Benutzeroberfläche zu entsprechen!


</div>

<img alt="" src=images/TaskPanel.jpg  style="width:400px;">

![](images/CAD_Modeling.gif‎ )


<div class="mw-translate-fuzzy">

### Skizzierer

Ein parametrischer Skizzierer mit einem geometrischen Beschränkungslöser, für weitere Details siehe **[Skizzierer Projekt](Sketcher_project/de.md)**.


</div>

### TeileKonstruktion


<div class="mw-translate-fuzzy">

#### Körper Funktion 

Da eine historienbasierte Modellierung viele Schritte haben kann, die zu einer um die endgültige Form zu erreichen, wird eine Klammer benötigt. Das ist der Körper, der das Endergebnis der Modellierung darstellt und als Gruppe für alle Funktionen des Verlaufsbaums fungiert .


</div>


<div class="mw-translate-fuzzy">

#### Polsterfunktion

Eine Polsterfunktion extrudiert eine Skizze (oder ein beliebiges Part2D Objekt) in die normale Richtung. Garantiere immer einen Körper oder scheitere.

#### Taschenfunktion

Drucke eine Skizze in einen Basisvolumenkörper, entweder definiert durch die Tiefe oder \"Bis zum letzten \| Bis zum ersten\". Garantiere auch einen Volumenkörper-


</div>

#### Bohrungsfunktiom

Sehr gute Bohrungsparameterdefinition aus der NaroCad Spezifikation:

    
  <img alt="" src=images/Counterbore_settings.png  style="width:300px;">   <img alt="" src=images/Counterbore_settings2.png  style="width:300px;">   <img alt="" src=images/Countersink_settings.png  style="width:300px;">
    

  : **NaroCAD Bore definitions**

#### Muster

Wiederholen einer der oben genannten Funktionen

##### **RechteckMuster**

Wiederholen eines der oben genannten Merkmale entlang eines x,y Musters.

##### **KreisförmigesMuster**

Wiederholen eines der oben genannten Funktionen entlang eines Musters in Polarkoordinaten.

##### **Skripterzeugtes Muster** 

Wiederholen eines der oben genannten Funktionen gemäß einer allgemeinen Regel, die in Form eines Skripts zur Verfügung gestellt wird.

## Ideenfindung

### Was andere tun 

-   [SolidWorks Beispiele](http://www.youtube.com/watch?v=cVXQmDStHus)

### Muster Implementierung 

Die Muster Funktionsklasse kann als tabellarisches Muster implementiert werden und als Basisklasse für die Funktionen \"Rechteckig\", \"Kreisförmig\" und \"programmerstelltes\" Muster dienen. Diese abgeleiteten Klassen müssen nur die Wiederholungstabelle der Basisklasse ausfüllen.

Jede Zeile der Wiederholungstabelle der Basis Musterklasse muss mindestens eine Transformationsmatrix enthalten, die auf die Platzierung des zu replizierenden Originalmerkmals anzuwenden ist. Zusätzlich könnten wir optionale Transformationsregeln haben, wie z.B. die Manipulation eines Parameterwertes des zu replizierenden Merkmals (z.B. um ein Muster von Löchern mit unterschiedlichem Radius zu erzeugen).

## Organisieren

### Modellieren der Objekthierarchie 

Dieses [UML](http://en.wikipedia.org/wiki/Unified_Modeling_Language) Diagramm zeigt die geplante Objekthierarchie und ihre Beziehungen. Gelb ist eine abstrakte Basisklasse, blau ist implementiert und grau ist geplant.

<img alt="" src=images/PartDesign_ModlingObjectsHirachy.png  style="width:1000px;">

## Tutorien


<div class="mw-translate-fuzzy">

[PartDesign Lagergehäuse Tutorium I](PartDesign_Bearingholder_Tutorial_I/de.md)


</div>


<div class="mw-translate-fuzzy">

[PartDesign Lagergehäuse Tutorium II](PartDesign_Bearingholder_Tutorial_II/de.md)


</div>

## Nächste Maßnahmen 

Die nächsten Maßnahmen sind im Eintrag [Fahrplan](http://www.freecadweb.org/tracker/roadmap_page.php) für PartDesign definiert:


<div class="mw-translate-fuzzy">

### Körper

Aufgrund der parametrischen/assoziativen Natur des PartDesigns benötigen wir schließlich einen \"Körper\", der gruppiert und organisiert eine Baugeschichte. Der Körper selbst hält das Endergebnis als Form und hat als Kinder die PartDesign Formelemente gruppiert. Es definiert auch den tatsächlichen Kopf der Modellierungshistorie. Es ist auch mit dem [Zusammenbauprojekt](Assembly_project/de.md) verwandt, da es der Baustein für Produkte und Verbünde ist.


</div>


<div class="mw-translate-fuzzy">

### Zusätzliche Funktionen 

Die Polster und Taschen Funktionen sind der erste Köder für das PartDesign. Insbesondere an der Sichtbarkeitskontrolle und den visuellen Bearbeitungsgeräten muss noch gearbeitet werden. Aber dann sind zusätzliche Funktionen erforderlich.


</div>

#### Muster 

Muster Funktion, die wiederholt ein Block- oder Taschen Formelement gemäß einem kreisförmigen oder rechteckigen Muster anwendet. Ein [Beispiel in IronCAD](http://www.ironcad.com/index.php/support/learning-center). **Erledigt \[jrheinlaender\]**


<div class="mw-translate-fuzzy">

#### BohrLoch

Klassische Bohrung mit allen Parametern für Gewindeschneiden und Senkbohrung\....


</div>

#### Austragen

Trägt eine Skizze entlang einer Kurve aus und erzeugt einen Volumenkörper.

#### Drehen

Drehe eine Skizze entlang einer ihrer Achsen und um einen bestimmten Winkel. **Erledigt \[jrheinlaender et al.\]**


<div class="mw-translate-fuzzy">

## AUFGABEN Liste 

1.  **Verrundung/Fase Formteil**
    1.  Anwenden von Verrundung/Fase Arbeitsgang auf verschiedene Auswahltypen (Flächen/Flächenpaar/ganzer Körper)\*
2.  **Polster Werkzeug**
    1.  Erstellen \'bis zum nächsten\' Modus **DONE** (*mrlukeparry*\')
    2.  Erstellen \'bis zur Oberfläche / Fläche\' Modus \[**\'mrlukeparry**\'\]
    3.  Erstellen Entwurfseigenschaft für Polster **DONE** erstellen (*mrlukeparry*\')
    4.  Wenn Pad auf Fläche ausgewählt ist, automatisch eine Skizze erstellen?
    5.  Erstellen \'Mittelebene\' Modus **DONE** (*jrheinlander*\')
3.  **Taschen Werkzeug**
    1.  Erstellen \'bis zum ersten\', \'bis zum letzten\', \'durch alles\', \'bis zur Oberfläche / Fläche\' Modi **DONE** (*jrheinlander*\')
    2.  Wenn Tasche auf Fläche ausgewählt ist, automatisch eine Skizze erstellen?
    3.  **Drehung Formteil**
    4.  Zulassen, dass ein generisches Liniensegment/Achse als Referenz verwendet wird
    5.  Erstellen \'Mittelebene\' Modus **DONE** (*jrheinlander*\')
4.  **Loch Funktion**
5.  **Muster Funktion** **DONE** (*jrheinlander*\')
6.  **Austragung Funktion**
7.  **Körper Funktion**
8.  **Referenzgeometrie**
    1.  Ebene
9.  **Spiegelwerkzeug** **DONE** (*jrheinlander*\')
10. **Kopieren Funktionswerkzeug**


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign project/de
