# Part Loft Technical Details/de
Diese Seite erklärt die Details, wie die [Ausformungsoberfläche](Part_Loft/de.md) des Werkzeugs erzeugt wird. Dies ist ebenfalls relevant für [Part Austragung](Part_Sweep.md), die entlang eines geraden Pfades erfolgen, auch wenn es Unterschiede gibt.

Die angegebenen Informationen sind implementierungsspezifisch und können sich ändern. Der aktuelle Stand ist relevant für FreeCAD 0.15.4119, OCC Version: 6.7.0.

## Stufen der Ausformungserstellung 

Um den Vorgang der Ausformung zu erklären, ist es sinnvoll, ihn in Stufen zu unterteilen:

1.  die Anzahl der Segmente in den Profilen gleich machen (wenn sie es nicht schon gleich sind)
2.  Übereinstimmung zwischen den Segmenten herstellen
3.  erstellen der Austragungsoberfläche

### Schritt 1. Erstellen der Segmentanzahl mit Profilübereinstimmung 

Die Ausformung benötigt die Anzahl der Segmente, um Flächen zwischen den entsprechenden Segmenten zu erzeugen. Wenn die Anzahl der Segmente in allen Profilen übereinstimmt, wird dieser Schritt übersprungen.

Wenn mindestens eines der Profile eine unterschiedliche Anzahl von Segmenten hat, wird das folgende Verfahren angewendet. Die Vorgehensweise wird hier der Einfachheit halber für den Fall von nur zwei Profilen erläutert.

1.  die Profile werden vorübergehend so ausgerichtet, dass sie koplanar sind und ihre Massenschwerpunkte\* übereinstimmen.
2.  (siehe Bild) für jeden Knoten in einem Profil wird das zweite Profil unter dem gleichen Polarwinkel geschnitten (der Polmittelpunkt ist der Massenschwerpunkt). Wenn mehr als ein Scheibe möglich ist oder gar keine Scheibe möglich ist (das kann bei sehr konvexen Profilen passieren), schlägt die Ausformung typischerweise fehl.
3.  dasselbe wird in der entgegengesetzten Richtung gemacht.

Der Vorgang wird auf alle Profile ausgedehnt, um die gleiche Anzahl von Segmenten zu erhalten. Die Gesamtanzahl der Segmente in jedem Profil wäre gleich der Summe aller Segmentanzahlen aller Profile (vorausgesetzt, dass keiner der Knoten zufällig im gleichen Polarwinkel liegt).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="Der Vorgang des Schneidens von Profil2 (weiße sichelförmige Form), um Verbindungen zu erzeugen, die den Eckpunkten von Profil1 (violettes Fünfeck) entsprechen. Die eingefügten Verbindungen werden durch gelbe Pfeile markiert." src=images/Loft-vertex-insertion.png  style="width:300px;">   <img alt="Das Ergebnis der Ausformung entsprechend dem Bild links." src=images/Loft_crescent_pentagon.png  style="width:300px;">
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------

### Schritt 2. Übereinstimmung zwischen den Segmenten herstellen 

= <img alt="Veranschaulichung der Ausformung, wobei die Anzahl der Segmente in den Profilen beibehalten wird, wenn sie übereinstimmen. Beachte wie 3 Kanten des oberen Quadrats in ein kleines polygonales Stück des unteren Profils \"kollabieren\"." src=images/Loft_Number_of_verts_match.png  style="width:300px;"> Falls die Anzahl der Segmente in allen Profilen nicht gleich war, wurde in Schritt 1 das Schneiden durchgeführt, und die Übereinstimmung ist trivial. Falls die Anzahl der Segmente in allen Profilen gleich war, werden vorhandene Segmente verwendet (siehe Bild), und dann muss die Übereinstimmung festgestellt werden.

Der genaue Algorithmus zum Auffinden der entsprechenden Segmente ist komplex, aber im Allgemeinen neigt er dazu, die Verdrehung der resultierenden Ausformung zu minimieren. Das bedeutet, dass wenn man einen Loft zwischen zwei Quadraten macht, die maximal mögliche Verdrehung \<45° ist. Eine weitere Drehung eines der Quadrate führt dazu, dass die Ausformung zu anderen Knoten springt.

Die Übereinstimmung zwischen benachbarten Profilen wird unabhängig voneinander hergestellt. Das bedeutet, dass durch das Hinzufügen weiterer Profile eine zusätzliche Verdrehung erreicht werden kann.

Zu beachten ist auch, dass bei gleicher Segmentanzahl in Profilen der resultierende Ausformung gegenüber komplexen Profilen, insbesondere bei nicht konvexen Profilen, wesentlich robuster ist. 

### Schritt 3. Die Ausformungsoberfläche herstellen. 

<img alt="Eine Spline Interpolationskurve (rot), die der Ausformungsoberfläche folgt. Die Punkte, durch die interpoliert werden soll, sind als rote Quadrate dargestellt." src=images/Loft_B-spline.png  style="width:400px;"> Wenn es nur zwei Profile gibt, sind die erzeugten Flächen Regelflächen zwischen den entsprechenden Segmenten der Profile. Gerade Kanten werden erzeugt, um die entsprechenden Eckpunkte der Profile zu verbinden.

Wenn mehr als zwei Profile vorhanden sind, werden die Flächen aus Splines in der gleichen Weise wie Geraden aus Regelflächen gebildet. Die gedachten Splines, aus denen die Oberfläche \"besteht\", werden durch entsprechende Punkte der entsprechenden Segmente der Profile gezeichnet.

Die Splines sind B-Spline Interpolation.

-   Wenn die Anzahl der Profile unter 10 liegt, wird die Interpolation mit einem B Spline mit einem maximal möglichen Grad (d.h. Grad = Anzahl\_der\_Profile - 1) durchgeführt.
-   Ist die Anzahl der Profile größer als 10, wird die Interpolation auf B Splines 3. Grades umgeschaltet.

Die verwendete Knüpfmethode ist \"ungefähre Sehnenlänge\". Näherung steht für die Tatsache, dass der Knotenvektor für jeden Spline in einer Ausformung genau gleich ist. Weitere Informationen über die B Spline Interpolation, den Knotenvektor und die Methode der Sehnenlänge findest du z.B. unter [cs.mtu.edu Curve Global Interpolation](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/INT-APP/CURVE-INT-global.html).

Beachte, dass Ausformung eine \"Ruled\"-Eigenschaft hat. Wenn sie auf \"true\" gesetzt ist, werden Regelflächen zwischen benachbarten Profilen erstellt, auch wenn es mehr als ein Profil gibt. Das heißt, die B Spline Interpolation wird durch stückweise lineare Interpolation ersetzt. 

## Das Wesentliche 

-   Die Ausformung führt eine B-Spline Interpolation zwischen den bereitgestellten Profilen durch. Die Interpolation wird auf stückweise linear geschaltet, wenn die \"Ruled\"-Eigenschaft auf true gesetzt wird.
-   Wenn die Anzahl der Profile 9 übersteigt, wird der Interpolationsgrad auf 3 reduziert, wodurch das Wackeln erheblich reduziert werden kann.
-   Die Anpassung der Anzahl der Segmente (auch bekannt als Anzahl der Knoten) in den Profilen erlaubt es, der Ausformung eine leichte Verdrehung zu geben und erlaubt typischerweise die Verwendung komplexerer Profile.
-   Wenn die Anzahl der Segmente nicht übereinstimmt, ist es am besten, die Profile durch eine richtige r(phi) Funktion in Polarkoordinaten darstellbar zu halten.

## Zusätzliche Anmerkungen 

-   Es ist nicht erforderlich, dass die Profile parallel sind (siehe Bild unten).
-   Bei Ausformngu ist es nicht erforderlich, dass die Profile getrennt sind (siehe Bild unten). Sie können koplanar sein, aber sie sollten sich nicht schneiden.
-   Wenn die Eigenschaft \"geschlossen\" der Ausformung \"wahr\" ist, gibt es eine Eckverbindung in allen Splines, die die Ausformung bilden (siehe Bild unten). Es gibt jetzt keine zuverlässige Möglichkeit, die Ausformung sanft zu schließen.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="Es ist nicht erforderlich, dass die Profile parallel sind." src=images/Loft_nonparallel.png  style="width:300px;">   <img alt="In Ausformung können die Profile koplanar sein. In diesem Beispiel sind zwei von drei Profilen koplanar." src=images/Loft_Coplanar.png  style="width:300px;">   <img alt="Ein Beispiel für eine geschlossene Ausformung zwischen drei fünfeckigen Profilen (weiß). Beachte die nicht glatte Verbindung am äußersten Profil. Dies ist das erste Profil im geschlossenen Loft." src=images/Loft-closed.png  style="width:300px;">
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

_

---
[documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Part_Workbench.md) > Part Loft Technical Details/de
