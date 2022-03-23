---
- GuiCommand:/de
   Name:PartDesign Thickness
   Name/de:PartDesign Dicke
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Modifikationen → Dicke
   Version:0.17
   SeeAlso:[Part Dicke](Part_Thickness/de.md)
---

# PartDesign Thickness/de

## Beschreibung

Das Werkzeug *Dicke* bearbeitet einen Festkörper und wandelt ihn in einen dickwandigen hohlen Gegenstand mit mindestens einer offenen Fläche um, der jeder seiner verbleibenden Flächen eine gleichmäßige Dicke verleiht. Bei einigen Volumenkörpern können Sie die Arbeit erheblich beschleunigen und vermeiden, dass Extrusionen und Taschen entstehen.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*Das Werkzeug Dicke angewendet auf die Fläche (B) eines Volumenkörpers (A) ergibt das hohle Objekt (C).*

## Anwendung

1.  Wählen Sie eine oder Flächen auf dem aktiven Körper aus.
2.  Drücke die **<img src="images/PartDesign_Thickness.png" width=24px> ''Dicke''**.
3.  Definiere die **Dicke(Thickness) Parameter** (siehe [Optionen](#Optionen.md)).
4.  Um weitere Flächen zum Öffnen hinzuzufügen, drücke **Fläche hinzufügen** und wähle eine oder mehrere Flächen in der 3D-Ansicht.
5.  Um eine zuvor ausgewählte Fläche zu entfernen, drücke {{KEY | Fläche entfernen}} und wähle eine Fläche in der 3D-Ansicht, oder klicke mit der rechten Maustaste auf die Fläche in der Liste und wähle *Entfernen*.
6.  Drücke **OK**.

## Optionen

-   **Dicke**: Wanddicke des resultierenden Objekts. Stellen Sie den gewünschten Wert ein.
-   **Modus**
    -   *Skin*: Wählen Sie diese Option, wenn Sie ein Objekt wie eine Vase, kopflos, aber mit dem Boden bekommen wollen
    -   *Rohr*: Wählen Sie diese Option, wenn Sie ein Objekt wie ein Rohr bekommen möchten, ohne Boden und Deckel. In diesem Fall kann es nützlich sein, die zu löschenden Flächen auszuwählen, bevor Sie das Werkzeug starten. Nutzen Sie dazu die vordefinierten Ansichten Schaltflächen oder verwenden Sie die numerischen Tasten.
    -   *Recto Verso*:

-   **Verbindungstyp**
    -   *KreisBogen(Arc)*: entfernt die äußeren Kanten und erstellt eine Leiste mit einem Radius, der der definierten Stärke entspricht.
    -   *Schnitt(Intersection)*: Wenn Flächen nach außen versetzt sind, werden scharfe Kanten zwischen den Flächen beibehalten.
-   **Erzeugen einer Hülle mit innen liegendem Volumen**: Wenn diese Option aktiviert ist, werden die Flächen nach innen versetzt.

## Einschränkungen

-   Es muss mindestens eine zu öffnende Fläche ausgewählt sein.
-   Wenn die Dicke nach innen geht, muss der Wert für die Dicke kleiner sein als die kleinste Höhe des Körpers.
-   Der Befehl kann bei komplexen Formen fehlschlagen. In diesem Zusammenhang muss auch eine Fläche wie die eines Kegels bereits als komplex angesehen werden.
    -   [PartDesign Additives Rohr](PartDesign_AdditivePipe/de.md) oder [PartDesign Additive Loft](PartDesign_AdditiveLoft/de.md) kann zur Erzeugung von komplexeren Formen geeigneter sein.

## Beispiele

1.  Erstellen Sie einen Block(Aufpolsterung/Pad) aus der Skizze
2.  Erstellen Sie eine zweite Skizze auf der XY-Ebene
3.  Erstellen Sie ein zweites Pad aus der zweiten Skizze

Wie in den folgenden Bildern:

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )

Dann

1.  Wählen Sie eine kreisförmige Fläche
2.  Wählen Sie **<img src="images/_PartDesign_Thickness.png" width=24px>Dicke
**
3.  Fügen Sie der Auswahl die anderen kreisförmigen Flächen hinzu

Resultat: ![](images/Brga-spessore.png )

## Bekannte Probleme 

-   BRep\_API: command not done (Befehl nicht ausgeführt)
-   BRep\_Tool: no parameter on edge
-   Fehlschlag ohne weitere Fehlermeldung





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/de
