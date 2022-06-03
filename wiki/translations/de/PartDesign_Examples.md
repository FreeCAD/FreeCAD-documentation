# PartDesign Examples/de
{{TOCright}}

## Einführung

Manchmal braucht man einen Hinweis darauf, wie mächtig ein Werkzeug ist, ohne zu viele Erklärungen.

Dies ist eine Sammlung von Beispielen, die mit bestimmten Werkzeugen erzielt werden können. Detaillierte Erklärungen findet man bei den Werkzeugbeschreibungen und in Tutorien, die man im Web findet.

## Pad

<img alt="" src=images/PartDesign_Pad.svg  style="width   *24px;"> [PartDesign Pad](PartDesign_Pad/de.md) Ist ein Werkzeug zum Erstellen von Pad-Objekten, die prismatische Objekte sind, wie z. B. Extrusionsobjekte, Zylinder, Kegel, Würfel, Keile\...

Jedes Objekt basiert auf einer Kontur (gelb), die die Querschnittsform definiert (vorzugsweise mit dem Arbeitsbereich [Sketcher](Sketcher_Workbench.md) erstellt).

Die Kontur wird entlang einer Richtung gezogen (ausgetragen, extrudiert), um ein Objekt mit einer Dicke oder einer Länge zu versehen.
Standardmäßig wird die Normalenrichtung der Ebene verwendet, die die Kontur enthält (Skizzenebene). Wahlweise kann die Richtung durch Bearbeiten der Parameter im Eigenschafteneditor geändert werden oder durch das Anwählen einer separaten geraden Linie (weiß).


<div class="mw-collapsible mw-collapsed">

**Galerie**


<div class="mw-collapsible-content toccolours">

### Prismatisch Grundkörper 

++++
| **Zylinder**            | <img alt="Zylinder" src=images/PartDesign_ExamplePad-01.png  style="width   *200px;">                       | -   Kontur   * **Kreis**.                                       |
++++
| **Würfel**              | <img alt="Würfel" src=images/PartDesign_ExamplePad-02.png  style="width   *200px;">                           | -   Kontur   * **Quadrat**.                                     |
|                         |                                                                                         | -   Extrusionslänge   * Ist gleich der Länge der Quadratkanten. |
++++
| **Quader**              | <img alt="Quader" src=images/PartDesign_ExamplePad-03.png  style="width   *200px;">                           | -   Kontur   * **Rechteck**.                                    |
++++
| **Regelmäßiges Prisma** | <img alt="Regelmäßiges Prisma" src=images/PartDesign_ExamplePad-04.png  style="width   *200px;"> | -   Kontur   * **Sechseck**.                                    |
++++
| **Keil**                | <img alt="Keil" src=images/PartDesign_ExamplePad-05.png  style="width   *200px;">                               | -   Kontur   * **Dreieck**.                                     |
++++

### Prismatische Profile 


</div>


</div>

## Additive Pipe 

<img alt="" src=images/PartDesign_AdditivePipe.svg  style="width   *24px;"> [PartDesign Additive pipe](PartDesign_AdditivePipe/de.md) ist ein Werkzeug zum Erstellen von AdditivePipe-Objekten, wie z. B. Sweep-Objekte, Extrusionsobjekte, Rotationsobjekte (Drehkörper), Zylinder, Kegel, Würfel, Pyramiden, Kugeln\...

Jedes Objekt basiert auf wenigstens zwei Linien (vorzugsweise mit dem Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) erstellt)   *

-   Eine Kontur (gelb), die die Querschnittsform definiert.
-   Einen Pfad (weiß), an dem entlang die Kontur ausgetragen wird.

Es ist nicht schwer zu erkennen, dass einige Objekte auch mit anderen Werkzeugen erstellt werden können, aber käme man darauf, wie vielseitig dieses Werkzeug ist, ohne diese Beispiele?


<div class="mw-collapsible mw-collapsed">

**Galerie**


<div class="mw-collapsible-content toccolours">

### Kreisförmig ausgetragene Objekte 

++++
| **Kugel**        | <img alt="Kugel" src=images/PartDesign_ExampleSphere-01.png  style="width   *200px;">                            | -   Kontur   * ein **180° Bogen** (Halbkreis) und eine **Linie**, die beide Endpunkte verbindet.                                                           |
|                  |                                                                                           | -   Pfad   * **Kreis**.                                                                                                                                    |
++++
| **Kugelsegment** | <img alt="Kugelsegment 240°" src=images/PartDesign_ExampleSphere-02.png  style="width   *200px;">    | -   Kontur   * ein **180° Bogen** und eine **Linie**, die beide Endpunkte verbindet.                                                                       |
|                  |                                                                                           | -   Pfad   * ein **240° Bogen**.                                                                                                                           |
|                  |                                                                                           |                                                                                                                                                         |
|                  |                                                                                           |    *   Diese Funktion kann Segmente mit beliebigem Winkel außer 180° erstellen, da sie ein Problem damit hat, wenn Ausgangs- und Zielebene komplanar sind. |
++++
| **Halbkugel**    | <img alt="Halbkugel" src=images/PartDesign_ExampleSphere-03.png  style="width   *200px;">                    | -   Kontur   * ein **90° Bogen** und zwei rechtwinklige **Linien**, die beide Endpunkte verbinden.                                                         |
|                  |                                                                                           | -   Pfad   * **Kreis**.                                                                                                                                    |
++++
| **Torus**        | <img alt="Torus" src=images/PartDesign_ExampleTorus-01.png  style="width   *200px;">                             | -   Kontur   * **Kreis**.                                                                                                                                  |
|                  |                                                                                           | -   Pfad   * **Kreis**.                                                                                                                                    |
++++
| **Kegel**        | <img alt="Kegel" src=images/PartDesign_ExampleTorus-04.png  style="width   *200px;">                             | -   Kontur   * **Dreieck**, wobei eine Linie auf der Mittellinie liegt.                                                                                    |
|                  |                                                                                           | -   Pfad   * **Kreis**.                                                                                                                                    |
++++
| **Zylinder**     | <img alt="Zylinder" src=images/PartDesign_ExampleTorus-02.png  style="width   *200px;">                       | -   Kontur   * **Rechteck**, wobei eine Linie auf der Mittellinie liegt.                                                                                   |
|                  |                                                                                           | -   Pfad   * full **Kreis**.                                                                                                                               |
++++
| **Rohr** (Röhre) | <img alt="Rohr (Hohlzylinder)" src=images/PartDesign_ExampleTorus-03.png  style="width   *200px;"> | -   Kontur   * **rectangle**.                                                                                                                              |
| Hohlzylinder     |                                                                                           | -   Pfad   * **Kreis**.                                                                                                                                    |
++++

### Prismatische Objekte 

Gerade ausgetragene Objekte

++++
| **Zylinder**            | <img alt="Zylinder" src=images/PartDesign_ExamplePrism-01.png  style="width   *200px;">                           | -   Kontur   * **Kreis**.                                                 |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++
| **Würfel**              | <img alt="Würfel" src=images/PartDesign_ExamplePrism-02.png  style="width   *200px;">                               | -   Kontur   * **Quadrat**.                                               |
|                         |                                                                                               | -   Pfad   * gerade **Linie**, mit gleicher Länge, wie die Quadratkanten. |
++++
| **Quader**              | <img alt="Quader" src=images/PartDesign_ExamplePrism-03.png  style="width   *200px;">                               | -   Kontur   * **Rechteck**.                                              |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++
| **Keil**                | <img alt="Keil" src=images/PartDesign_ExamplePrism-04.png  style="width   *200px;">                                   | -   Kontur   * **Dreieck**.                                               |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++
| Regelmäßiges **Prisma** | <img alt="Regelmäßiges Prisma" src=images/PartDesign_ExamplePrism-05.png  style="width   *200px;">     | -   Kontur   * regelmäßiges **Sechseck**.                                 |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++
| Sternförmiges Prisma    | <img alt=" Sternförmiges Prisma" src=images/PartDesign_ExamplePrism-06.png  style="width   *200px;"> | -   Kontur   * regelmäßige **Sternform**.                                 |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++
| Doppel-T-Träger         | <img alt="Doppel-T-Träger" src=images/PartDesign_ExamplePrism-07.png  style="width   *200px;">             | -   Kontur   * **Trägerquerschnitt**.                                     |
|                         |                                                                                               | -   Pfad   * gerade **Linie**.                                            |
++++

### Konische Objekte 

++++
| **Kegel**         | <img alt="Kegel" src=images/PartDesign_ExampleConic-01.png  style="width   *200px;">                         | -   Konturen   * Boden   * **Kreis**, Deckel   * **Punkt**.      |
|                   |                                                                                       | -   Pfad   * gerade **Linie**.                             |
|                   |                                                                                       |                                                         |
|                   |                                                                                       |    *   (Die Spitze ist ein Endpunkt einer Hilfslinie)      |
++++
| **Pyramide**      | <img alt="Pyramide" src=images/PartDesign_ExampleConic-02.png  style="width   *200px;">                   | -   Konturen   * Boden   * **Quadrat**, Deckel   * **Punkt**.    |
|                   |                                                                                       | -   Pfad   * gerade **Linie**.                             |
|                   |                                                                                       |                                                         |
|                   |                                                                                       |    *   (Die Spitze ist ein Endpunkt einer Hilfslinie)      |
++++
| Geneigte Pyramide | <img alt="Geneigte Pyramide" src=images/PartDesign_ExampleConic-03.png  style="width   *200px;"> | -   \* Konturen   * Boden   * **Quadrat**, Deckel   * **Punkt**. |
|                   |                                                                                       | -   Pfad   * gerade **Linie**.                             |
|                   |                                                                                       |                                                         |
|                   |                                                                                       |    *   (Die Spitze ist der Endpunkt des Pfades)            |
++++

### Gekrümmte ausgetragene Objekte 

++++
| **Schlauch**           | <img alt="Schlauch" src=images/PartDesign_ExampleSweep-01.png  style="width   *200px;">                       | -   Kontur   * 2 konzentrische **Kreise**.                      |
| (Rohr)                 |                                                                                           | -   Pfad   * **Kurve**.                                         |
++++
| Quadratisches **Rohr** | <img alt="Quadratisches Rohr" src=images/PartDesign_ExampleSweep-02.png  style="width   *200px;">   | -   Kontur   * 2 konzentrische **Quadrate**.                    |
|                        |                                                                                           | -   Pfad   * **Kurve**.                                         |
++++
| **Draht**              | <img alt="Draht" src=images/PartDesign_ExampleSweep-04.png  style="width   *200px;">                             | -   Kontur   * **Kreis**.                                       |
|                        |                                                                                           | -   Pfad   * **Kurve**.                                         |
++++
| Horn                   | <img alt="Horn" src=images/PartDesign_ExampleSweep-03.png  style="width   *200px;">                               | -   Kontur   * Boden   * **Kreis**, Deckel   * (kleinerer) **Kreis**. |
|                        |                                                                                           | -   Pfad   * **Kurve**.                                         |
++++
| Legendärer             | <img alt=" Sechskantschlüssel" src=images/PartDesign_ExampleSweep-05.png  style="width   *200px;"> | -   Kontur   * **Sechseck**.                                    |
| **Sechskantschlüssel** |                                                                                           | -   Pfad   * **Kurve**.                                         |
++++

### Spiral- und wendelförmige Objekte 

++++
| Schraubenfeder   | <img alt="Schraubenfeder" src=images/PartDesign_ExampleSpring-01.png  style="width   *200px;"> | -   Kontur   * **Kreis**.                                                                                               |
|                  |                                                                                  | -   Pfad   * <img alt="" src=images/Part_Helix.svg  style="width   *16px;"> [Part Helix](Part_Helix.md).                  |
++++
| Spiralfeder      | <img alt="Unruhfeder" src=images/PartDesign_ExampleSpring-03.png  style="width   *200px;">         | -   Kontur   * **Rechteck**.                                                                                            |
| Unruhfeder       |                                                                                  | -   Pfad   * <img alt="" src=images/Part_Spiral.svg  style="width   *16px;"> [Part Spirale](Part_Spiral.md).             |
++++
| **Evolutfeder**, | <img alt="Wickelfeder" src=images/PartDesign_ExampleSpring-04.png  style="width   *200px;">       | -   Kontur   * **Rechteck**.                                                                                            |
| Wickelfeder      |                                                                                  | -   Pfad   * <img alt="" src=images/Part_Helix.svg  style="width   *16px;"> [Part Helix](Part_Helix.md) mit einem Winkel. |
++++

### Übergangsobjekte

++++
| Quadrat -\> Kreis | <img alt="Gekrümmtes Übergangsobjekt" src=images/PartDesign_ExampleTrans-01.png  style="width   *200px;"> | -   Konturen   * Boden   * **Quadrat**, Deckel   * **Kreis**.     |
| mit Pfad          |                                                                                                         | -   Pfad   * Gekrümmte **Linie**.                           |
++++
| Quadrat -\> Kreis | <img alt="Gerades Übergangsobjekt" src=images/PartDesign_ExampleTrans-02.png  style="width   *200px;">       | -   Konturen   * Boden   * **Quadrat**, Deckel   * **Kreis**.     |
| gerade            |                                                                                                         | -   Pfad   * Gerade **Linie**.                              |
++++
| Vieleck -\> Stern | <img alt="Übergang Vieleck -\> Stern" src=images/PartDesign_ExampleTrans-03.png  style="width   *200px;">  | -   Konturen   * Boden   * **Fünfeck**, Deckel   * **Sternform**. |
|                   |                                                                                                         | -   Pfad   * Gerade **Linie**.                              |
++++

### Optionen

#### Eckübergang

Ein Linienzug kann als Pfad verwendet werden, wobei die Eigenschaft **Transition** (Übergang) die Form der Ecken beeinflußt.

**Transformed** braucht besondere Beachtung, da ebene Bereiche mit Ausdehnung 0 entstehen können.

++++
| Parameter        | Iso-Ansicht                                                                                              | Draufsicht                                                                                             |
+==================+==========================================================================================================+========================================================================================================+
| **Transformed**  | <img alt="Transformed, Iso-Ansicht" src=images/PartDesign_ExampleProperty-01.png  style="width   *200px;">   | <img alt="Transformed, Draufsicht" src=images/PartDesign_ExampleProperty-02.png  style="width   *200px;">   |
|                  |                                                                                                          |                                                                                                        |
|                  |    *   Innen- und Außenecken sind Kanten.                                                                   |    *   Die Grundform folgt nicht der Ausrichtung der Linie.                                               |
++++
| **Right corner** | <img alt="Right corner, Iso-Ansicht" src=images/PartDesign_ExampleProperty-03.png  style="width   *200px;"> | <img alt="Right corner, Draufsicht" src=images/PartDesign_ExampleProperty-04.png  style="width   *200px;"> |
|                  |                                                                                                          |                                                                                                        |
|                  |    *   Inner and outer corners are edges.                                                                   |    *   Die Grundform folgt der Ausrichtung der Linie.                                                     |
++++
| **Round corner** | <img alt="Round corner, Iso-Ansicht" src=images/PartDesign_ExampleProperty-05.png  style="width   *200px;"> | <img alt="Round corner, Draufsicht" src=images/PartDesign_ExampleProperty-06.png  style="width   *200px;"> |
|                  |                                                                                                          |                                                                                                        |
|                  |    *   Die Ecken, die außerhalb des Pfades liegen, werden abgerundet.                                       |    *   Die Grundform folgt der Ausrichtung der Linie.                                                     |
++++

#### Ausrichtungsmodus

++++
| Parameter     | Iso-Ansicht                                                                                           | Draufsicht                                                                                                                      |
+===============+=======================================================================================================+=================================================================================================================================+
| **Standard**  | <img alt="Standard, Iso-Ansicht" src=images/PartDesign_ExampleProperty-07.png  style="width   *200px;">      | <img alt="Standard, Draufsicht" src=images/PartDesign_ExampleProperty-08.png  style="width   *200px;">                                  |
|               |                                                                                                       |                                                                                                                                 |
|               |    *   Lage und Ausrichtung folgen dem Pfad.                                                             |    *   (Wenn das Objekt auf unerwartete Art verdreht ist, sollte man Frenet ausprobieren)                                          |
|               |    *                                                                                                     |                                                                                                                                 |
++++
| **Fixed**     | <img alt="Fixed, Iso-Ansicht" src=images/PartDesign_ExampleProperty-09.png  style="width   *200px;">            | <img alt="Fixed, Draufsicht" src=images/PartDesign_ExampleProperty-10.png  style="width   *200px;">                                        |
|               |                                                                                                       |                                                                                                                                 |
|               |    *   Die Lage folgt dem Pfad und die Ausrichtung bleibt wie die der Grundform.                         |    *   Dies hat die Tendenz, Sebstdurchdringungen zu erzeugen, die zu weiteren Fehlern führen   * In diesem Falle eine Geisterfläche. |
++++
| **Frenet**    | <img alt="Frenet, Iso-Ansicht" src=images/PartDesign_ExampleProperty-07.png  style="width   *200px;">          | <img alt="Frenet, Draufsicht" src=images/PartDesign_ExampleProperty-08.png  style="width   *200px;">                                      |
|               |                                                                                                       |                                                                                                                                 |
|               |    *   Lage und Ausrichtung folgen dem Pfad, auf einem anderen Algorithmus basierend als unter Standard. |    *   Die Grundform folgt der Ausrichtung der Linie.                                                                              |
++++
| **Auxiliary** |                                                                                                       |                                                                                                                                 |
++++
| **Binormal**  |                                                                                                       |                                                                                                                                 |
++++


</div>


</div>

[Category   *PartDesign](Category_PartDesign.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Examples/de
