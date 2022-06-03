---
- GuiCommand   */de
   Name   *PartDesign Thickness
   Name/de   *PartDesign Dicke
   MenuLocation   *Part Design → Modifikationen → Dicke
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   Version   *0.17
   SeeAlso   *[Part Dicke](Part_Thickness/de.md)
---

# PartDesign Thickness/de

## Beschreibung

Das Werkzeug *Dicke* bearbeitet einen Festkörper und wandelt ihn in einen dickwandigen hohlen Gegenstand mit mindestens einer offenen Fläche um, der jeder seiner verbleibenden Flächen eine gleichmäßige Dicke verleiht. Bei einigen Volumenkörpern kann es die Bearbeitung erheblich beschleunigen und vermeidet die Erstellung von Extrusionen und Taschen.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;"> 
*Das Werkzeug Dicke angewendet auf die Fläche (B) eines Volumenkörpers (A) ergibt das hohle Objekt (C).*

## Anwendung

1.  Eine oder mehrere Flächen des aktiven Körpers auswählen.

2.  Die Schaltfläche **<img src="images/PartDesign_Thickness.png" width=24px> ''Dicke''** drücken.

3.  Die **Dicke- (Thickness) Parameter** festlegen (siehe [Optionen](#Optionen.md)).

4.  Um weitere Flächen zum Öffnen hinzuzufügen, drückt man die Schaltfläche **Fläche hinzufügen** und wählt eine oder mehrere Flächen in der 3D-Ansicht aus.

5.  Um eine zuvor ausgewählte Fläche zu entfernen, drückt man ** Fläche entfernen** und wählt eine Fläche in der 3D-Ansicht, oder klickt mit der rechten Maustaste auf die Fläche in der Liste und wählt *Entfernen*.

6.  
    **OK**drücken.

## Optionen

-   **Dicke**   * Wanddicke des resultierenden Objekts. Stellen Sie den gewünschten Wert ein.
-   **Modus**
    -   *Skin*   * Wählen Sie diese Option, wenn Sie ein Objekt wie eine Vase, kopflos, aber mit dem Boden bekommen wollen
    -   *Rohr*   * Wählen Sie diese Option, wenn Sie ein Objekt wie ein Rohr bekommen möchten, ohne Boden und Deckel. In diesem Fall kann es nützlich sein, die zu löschenden Flächen auszuwählen, bevor Sie das Werkzeug starten. Nutzen Sie dazu die vordefinierten Ansichten Schaltflächen oder verwenden Sie die numerischen Tasten.
    -   *Recto Verso*   *

-   **Verbindungstyp**
    -   *KreisBogen(Arc)*   * entfernt die äußeren Kanten und erstellt eine Leiste mit einem Radius, der der definierten Stärke entspricht.
    -   *Schnitt(Intersection)*   * Wenn Flächen nach außen versetzt sind, werden scharfe Kanten zwischen den Flächen beibehalten.
-   **Erzeugen einer Hülle mit innen liegendem Volumen**   * Wenn diese Option aktiviert ist, werden die Flächen nach innen versetzt.

## Einschränkungen

-   Es muss mindestens eine zu öffnende Fläche ausgewählt sein.
-   Wenn die Dicke nach innen geht, muss der Wert für die Dicke kleiner sein als die kleinste Höhe des Körpers.
-   Der Befehl kann bei komplexen Formen fehlschlagen. In diesem Zusammenhang muss auch eine Fläche wie die eines Kegels bereits als komplex angesehen werden.
    -   [PartDesign Additives Rohr](PartDesign_AdditivePipe/de.md) oder [PartDesign Additive Loft](PartDesign_AdditiveLoft/de.md) kann zur Erzeugung von komplexeren Formen geeigneter sein.

## Beispiele

1.  Einen Block(Aufpolsterung/Pad) aus der Skizze erstellen
2.  Eine zweite Skizze auf der XY-Ebene anlegen
3.  Ein zweiten Block aus der zweiten Skizze erstellen

Wie in den folgenden Bildern   *

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )

Dann

1.  Eine kreisförmige Fläche auswählen

2.  
    **<img src="images/_PartDesign_Thickness.png" width=24px>Dicke**auswählen

3.  Die anderen kreisförmigen Flächen zur Auswahl hinzufügen

Ergebnis   * ![](images/Brga-spessore.png )

## Bekannte Fehler 

-   BRep\_API   * command not done (Befehl nicht ausgeführt)
-   BRep\_Tool   * no parameter on edge
-   Fehlschlag ohne weitere Fehlermeldung





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/de
