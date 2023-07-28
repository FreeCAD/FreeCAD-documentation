---
- GuiCommand:/de
   Name:Part Thickness
   Name/de:Part Dicke
   MenuLocation:Formteil → Dicke...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Versatz](Part_Offset/de.md)
---

# Part Thickness/de



## Beschreibung

Das <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Dicke](Part_Thickness/de.md) Werkzeug bearbeitet eine massive Form und wandelt sie in einen hohlen Gegenstand um, indem es jeder seiner Flächen eine definierte Dicke verleiht. Bei einigen Volumenkörpern erlaubt es dir, die Arbeit erheblich zu beschleunigen und vermeidet die Herstellung von Extrusionen und Taschen.



## Verwendung

1.  Erstelle einen Festkörper
2.  Wähle eine oder mehrere Oberflächen
3.  Klicke auf das **<img src="images/Part_Thickness.svg" width=16px> '''Part Dicke'''**-Werkzeug
4.  Setze die Parameter (siehe [Optionen](#Options/de.md))
5.  Klicke **OK** zur Bestätigung, führe die Operation aus und verlasse die Funktion
6.  Passe die Parameter in der Eigenschaftentabelle bei Bedarf an



## Optionen

-   Dicke: Wanddicke des resultierenden Objekts
    -   Ein positiver Wert versetzt die Oberflächen nach außen
    -   Ein negativer Wert versetzt die Oberflächen nach innen

-   Modus
    -   Oberfläche: Wähle diese Option, wenn Du einen Gegenstand ähnlich einer Vase haben möchtest, oben offen, aber mit einem Boden.
    -   Rohr: Wähle diese Option, wenn Du ein Objekt ähnlich einem Rohr haben möchtest, oben und unten offen. In diesem Fall kann es einfacher sein, die zu löschenden Flächen vor dem Aufruf des Werkzeugs auszuwählen. Helfen können die Buttons für die vordefinierten Ansichten oder die numerischen Tasten.
    -   Recto Verso:

-   Verknüpfungstyp
    -   Kreisbogen: Entfernt die äußeren Kanten und erstellt eine Verrundung mit einem Radius gleich der definierten Dicke
    -   Tangente:
    -   Schnitt:

-   Schnitt:

-   Selbstdurchdringung: Aktiviert Selbstdurchdringung

-    **Flächen**: Wählt die zu entfernenden Flächen, klicke dann **Fertig**

-   Ansicht akutalisieren: Automatisches Aktualisieren in Echtzeit



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die auf die richtige Objektart verweisen, können auch als Quellobjekte verwendet werden. {{Version/de|0.20}}
-   Komplexe Formen können bizarre, schwer vorherzusagende Ergebnisse produzieren. Prüfe sorgfältig die entstandene Form und speichere Deine Arbeit vor dem Anwenden der Operation.



## Verweise

Ein gutes Beispiel zur Benutzung dieses Werkzeuges gibt es im Forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)



## Beispiele

**Hollow cylinder**

1.  Create **<img src="images/Part_Cylinder.svg" width=16px> [Cylinder](Part_Cylinder.md)** with radius 10mm and height 20mm
2.  Select the top and bottom surface of the cylinder
3.  Click on the **<img src="images/Part_Thickness.svg" width=16px> Thickness
** button (no need to change default settings) and press **OK**

Notes:

-   For this shape, consider using **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube.md)** instead.
-   Select the cylinder\'s top surface only to create a receptacle.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Box-Enclosure**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/de
