---
 GuiCommand:
   Name: Part Thickness
   Name/de: Part Dicke
   MenuLocation: Formteil , Dicke...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Offset/de
---

# Part Thickness/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Dicke](Part_Thickness/de.md) bearbeitet eine Festkörper-Form und wandelt sie in ein hohles Objekt um, indem es jeder seiner Flächen eine festgelegte und konstante Wandstärke verleiht. Bei einigen Festkörpern ermöglicht es, die Arbeit erheblich zu beschleunigen und vermeidet die Erstellung von Extrusionen und Taschen.



## Verwendung

1.  Erstelle einen Festkörper
2.  Wähle eine oder mehrere Oberflächen
3.  Klicke auf das **<img src="images/Part_Thickness.svg" width=16px> '''Part Dicke'''**-Werkzeug
4.  Setze die Parameter (siehe [Optionen](#Options/de.md))
5.  Klicke **OK** zur Bestätigung, führe die Operation aus und verlasse die Funktion
6.  Passe die Parameter in der Eigenschaftentabelle bei Bedarf an



## Optionen

-    **Dicke**: Wandstärke des resultierenden Objekts.

    -   Ein positiver Wert versetzt die Oberflächen nach außen.
    -   Ein negativer Wert versetzt die Oberflächen nach innen.

-    **Modus**-   
        **Oberfläche**
        
        : Diese Option auswählen, wenn ein Gegenstand ähnlich einer Vase entstehen soll, oben offen, aber mit einem Boden.

    -   
        **Rohr**
        
        : Diese Option auswählen, wenn ein Objekt ähnlich einem Rohr entstehen soll, oben und unten offen. In diesem Fall kann es einfacher sein, die zu löschenden Flächen vor dem Aufruf des Werkzeugs auszuwählen. Helfen können die Buttons für die vordefinierten Ansichten oder die numerischen Tasten.

    -   
        **Hinten-Vorne**
        
        :

-    **Verknüpfungstyp**-   
        **Kreisbogen**
        
        : Entfernt die äußeren Kanten und erstellt eine Verrundung mit einem Radius gleich der festgelegten Wandstärke.

    -   
        **Tangente**
        
        :

    -   
        **Schnitt**
        
        :

-    **Schnitt**:

-    **Selbstdurchdringung**: Aktiviert Selbstdurchdringung

-    **Flächen**: Die zu entfernenden Flächen auswählen, dann **Fertig** anklicken.

-    **Ansicht akutalisieren**: Aktualisier die Ansicht automatisch in Echtzeit.



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die auf die richtige Objektart verweisen, können auch als Quellobjekte verwendet werden. {{Version/de|0.20}}
-   Komplexe Formen können bizarre, schwer vorherzusagende Ergebnisse produzieren. Prüfe sorgfältig die entstandene Form und speichere Deine Arbeit vor dem Anwenden der Operation.



## Verweise

Ein gutes Beispiel zur Benutzung dieses Werkzeuges gibt es im Forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)



## Beispiele

**Hohlzylinder**

1.  Einen **<img src="images/Part_Cylinder.svg" width=16px> [Zylinder](Part_Cylinder/de.md)** mit 10 mm Radius und 20 mm Höhe.
2.  Deckel- und Bodenfläche des Zylinders auswählen.
3.  Die Schaltfläche **<img src="images/Part_Thickness.svg" width=16px> Dicke** drücken (es ist nicht nötig, die Voreinstellungen zu ändern) und dann **OK**.

Hinweise:

-   Für diese Form sollte man erwägen, **<img src="images/Part_Tube.svg" width=16px> [Hohlzylinder erstellen](Part_Tube/de.md)** zu verwenden.
-   Nur die Deckfläche des Zylinders auswählen, um eine Buchse zu erstellen.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Gehäuse**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/de
