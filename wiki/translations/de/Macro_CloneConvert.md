# Macro CloneConvert/de
{{Macro/de
|Name=Macro CloneConvert
|Translate=Macro CloneConvert
|Icon=Macro_CloneConvert.png
|Description=Erstellt einen Klon, eine Kopie oder einen Verbund des bzw. der Objekte und konvertiert in die gewünschte Position und Größe (inch, mm, m, µm...) oder frei. Das Basisobjekt wird in mm erkannt (FreeCAD-Basis).
|Author=mario52
|Version=00.16
|Date=2025-01-06
|FCVersion=ab 0.18
|Download=[https://www.freecadweb.org/wiki/images/0/0a/Macro_CloneConvert.png ToolBar Icon]
}}

## Beschreibung

Erzeugt einen Klon oder eine Kopie des Objekts und konvertiert es an der gewählten Position und Größe (Zoll, mm, m, µm \...) oder frei. Das Basisobjekt wird in mm (FreeCAD-Basis) erkannt.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/fb76b3c728c1c7cd085e87f5d6d223d9f79bb574/Macro_CloneConvert.FCMacro}}

## Verwendung

1.  Führen Sie das Makro aus
2.  Setze die XYZ-Einstellungen
3.  Wählen Sie \"Klonen\" oder \"Kopieren\"
4.  Wählen Sie eine Einheit oder einen Wert
5.  Wählen Sie Ihr Objekt aus
6.  klicken Sie auf die Schaltfläche **Ok**.

## Hinweise

-   Wenn kein Wert eingegeben wird, wird eine Kopie oder ein Klon ohne Änderung erstellt.
-   Wenn kein Objekt ausgewählt ist, wird die Schaltfläche **Ok** rot angezeigt.

Der Wert von **Bounding Box**, **Volume** und **Surface** wird in der Berichtansicht angezeigt, im Falle von **Copy** mehreren Objekten zeigt die Anzeige BoundingBox 0.0.

Die Basis ist das mm-Beispiel mit einem Würfel der Seitenlänge **1 mm**:

Wählen Sie in der ComboBox **inch**, **1 inch = 25,4 mm** die Felder **Scale free** automatisch auf 25,4 (die Werte in**Scale-free**kann separat geändert werden). Klicken Sie auf die Schaltfläche **Ok**. Der erstellte Klon enthält **25, 4 mm x 25,4 mm x 25,4 mm**.

**150%** = **1,50** in the **\"Scale free\"** fields
**104%** = **1,04** in the **\"Scale free\"** fields

Inverse Operation:

Wenn Sie ein Objekt verkleinern möchten, z. B. einen Würfel von 25,4 mm (1 Zoll) in den Würfeln von 1 mm, verwenden Sie die Formel **1 / 25.4 = 0.0393700** und geben Sie den Wert **0,0393700** (mit Komma) im Skalierungsfeld XY und Z ein.

In einem Würfel von 5 mm, **5 / 25.4 = 0.1968503** eingeben und den Wert **0,1968503** (mit Komma) in das Skalierungsfeld XY und Z eingeben.

**50%** = **0,50** in dem **\"Scale free\"** Felder
**4%** = **0,04** in dem **\"Scale free\"** Felder
Vordefinierte Einheiten sind: km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
<img alt="CloneConvert" src=images/Macro_CloneConvert_01.png  style="width:350px;">

-   **Mode**
-   **Clone :** Die Klone der Objekte werden erstellt
-   **Copy :** Es wird eine Kopie des Objekts erstellt
-   **Comp :** Eine Kombination des Objekts ist create
-   **Increm. :**Inkrementieren der Koordinatendaten auf die ursprünglichen Koordinaten des Objekts (Platzierung, Drehung \...)
    Wenn diese Option nicht aktiviert ist, beginnt die Platzierung in den Koordinaten 0,0,0 von FreeCAD.
    In diesem Fall Eine zusammengesetzte Platzierungsinformation ist \[0,0,0\]. Die Platzierung beginnt an der Position des Objekts.
    Wenn der tatsächliche Standort von den Basiskoordinaten abweicht, verwenden Sie 0,0 **ValueAt ()**. Schaltfläche für die tatsächliche Platzierung des ausgewählten Unterobjekts Fläche, Draht, Linie \....
-   **Unique:** Wenn dieses Kontrollkästchen markiert ist und mehrere Objekte ausgewählt sind, ist der erstellte Klon ein eindeutiges Objekt

-   **Coordinates**
-   ****...**:** Diese Schaltfläche bringt die YZ-Werte auf den Wert von X an, um dieselben Werte wie XYZ (oder manuell) zu erhalten. Mit zwei Klicks setzen Sie die Koordinaten auf 0,0 zurück
-   **Coordinate X:** Verschiebt die Kopie auf die ausgewählte Koordinate X (Basis 0,0,0, wenn Increm nicht aktiviert ist)
-   **Coordinate Y:** Verschiebt die Kopie in die ausgewählte Koordinate Y (Basis 0,0,0, wenn Increm nicht aktiviert ist)
-   **Coordinate Z:** Verschiebt die Kopie in die ausgewählte Koordinate Z (Basis 0,0,0, wenn Increm nicht aktiviert ist)

-   **Rotation**
-   ****...**:** Diese Schaltfläche passt die Pitch- und Roll-Werte an dem Wert von Yaw an, um dieselben Werte zu erhalten. Rotation (oder manuell)
    Mit einem zwei Klick setzen Sie das zurück Drehzahlwerte auf 0,0
-   **Yaw (Z):** Die Kopie auf die Achse Z (Yaw) drehen (0 beginnen, wenn Increm nicht aktiviert ist)
-   **Pitch (Y):** Die Kopie auf die Achse Y (Pitch) drehen (Start 0, wenn Increm nicht aktiviert ist)
-   **Roll (X):** Die Kopie auf die Achse X (Roll) drehen (Start 0, wenn Increm nicht aktiviert ist)

-   **Scale predefined**
-   **Scale predefined :** vordefinierte Skalen in Einheiten, km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique or choose a free value in the Scale free field.

-   **Number copy**
-   **Number copy :** Anzahl der Kopien

-   **Scale free**
-   **{{KEY | ...}}:** Diese Schaltfläche bringt die Skalenwerte auf den Wert von Skalierung X an, um dieselben Werte XYZ (oder manuell) zu haben.
    Mit einem Klick können Sie die Skalen zurücksetzen Werte bis 1,0
-   **Scale X:** freier Maßstab, wenn der Wert negativ **(-10)** ist, wird das Objekt *\'x 10\'* skaliert und in der X-Achse umgekehrt. Um die Form zu reduzieren, geben Sie einen Dezimalwert ein (0,5).
-   **Scale Y:** freier Maßstab, wenn der Wert negativ **(-10)** ist, wird das Objekt **x 10** skaliert und in der Y-Achse umgekehrt. Um die Form zu reduzieren, geben Sie einen Dezimalwert ein (0,5).
-   **Scale Z:** freier Maßstab, wenn der Wert negativ **(-10)** ist, wird das Objekt **x 10** skaliert und in der Z-Achse umgekehrt. Um die Form zu reduzieren, geben Sie einen Dezimalwert ein (0,5).

-   ****ValueAt ()**:** Geben Sie dem valueAt () das ausgewählte Unterobjekt an Face, Wire, Line \...
    Diese Option ist nützlich, wenn zusammengesetzte Platzierungsinformationen \[0, 0,0\] und seine tatsächliche Position ist von den Basiskoordinaten 0,0,0 entfernt (gibt keine Informationen über die Drehung des Objekts an)
-   ****Ok**:** Die OK-Schaltfläche bestätigt und startet den Befehl. Wenn kein Objekt ausgewählt ist, wird die **Ok** -Schaltfläche rot gefärbt
-   ****Reset**:** Der Reset-Button setzt alle Werte auf Null
-   ****Quit**:** die Schaltfläche Quit beendet das Makro




## Skript

Das Symbol ![](images/Macro_CloneConvert.png )

**Macro_CloneConvert.FCMacro**

Laden Sie das Makro in herunter Gist [Macro_CloneConvert.FCMacro](https://gist.github.com/mario52a/9f2f2f6144e1307a048f1840ef99300c)

## Revision

06/01/2025 ver 00.16 remplace PySide2 to PySide augmente mini et maxi efface toutes les reference a PySide, PySide2 et QtWidgets et correction clone, compound

06/06/2020 ver 0.15 = icon

20/05/2020 ver 0.14 = grid layout PySide2 Qt5

15/09/2019 ver 0.13 = replace the grec sign micro to \"um\", replace all \"\_translate(\"MainWindow\", \"mm\", None)\" to \"mm\" and comment line \"text.encode(\'utf-8\')\" cause not work with FC 0.19 18.213

01/06/2019 ver 0.12 = adapted for 0.19 et correction \"Copy:legacy=True\" and ShapeColor \.....

30/03/2018 ver 0.11 = odd checkBox, if multi selection the clone are object unique or object separate

07/06/2017 ver 0.10 = replace Draft\...Copy to Part..Shape cause section Copy : not draw copy scaled of object but copy not scaled ??

14/06/2016 ver 0.9 = adding the choice of number of copies and labels optimization

31/01/2016 ver 0.8 = modify the buttons reset section for two click for reset (in case modification the value)

30/01/2016 ver 0.7 = rewriting code with Placement and Increment and adding buttons Compound, Increment, ValueAt(),

26/01/2016 ver 0.6 = correction placement with many objets Copy

26/07/2015 ver 0.5 = correction rotate many objects Function Copy

25/07/2015 ver 0.4 = adding rotation

11/08/2014 replace \"AttributeError\" to \"Exception\"

02/07/2014 ver. 0.3 = modified to operate PyQt4 and PySide

09/05/2014 ver. 0.2 = adding function \"Copy\"



---
⏵ [documentation index](../README.md) > Macro CloneConvert/de
