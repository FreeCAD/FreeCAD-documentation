---
- GuiCommand:
   Name: PartDesign CoordinateSystem
   Name/de: PartDesign Koordinatensystem
   MenuLocation: Part Design -> Lokales Koordinatensystem erstellen
   Workbenches: PartDesign Workbench/de
   Version: 0.18
   SeeAlso: PartDesign_Point/de, PartDesign_Line/de, PartDesign_Plane/de
---

# PartDesign CoordinateSystem/de

## Beschreibung

Erzeugt ein **lokales Koordinatensystem**, welches als Referenz für andere Bezugsgeometrie verwendet werden kann. Es hilft auch, die Orientierung der referenzierten Bezugsgeometrie im 3D Raum zu ermitteln. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) {{Caption | Lokales Koordinatensystem, das aus dem Ursprung einer Bezugsebene entspring.}}

## Anwendung

1.  Schaltfläche **[<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> [Lokales Koordinatensystem erstellen](PartDesign_CoordinateSystem/de.md)** drücken.

2.  Die Parameter des Koordinatensystems definieren. Eine erste Referenz in der 3D-Ansicht auswählen, um die verfügbaren Verbindungsarten zu filtern.

3.  Abhängig von der ausgewählten Referenz, können eine oder mehrere Verbindungsarten in der Liste vorhanden sein. Die wahrscheinlichste wird automatisch ausgewählt und in der Liste fett dargestellt. Der Text *Angehängt im Modus:* zusammen mit dem Namen der Verbindungsart erscheint in grün über der Liste der Referenzen.

4.  Um eine weitere Referenz hinzuzufügen, drückt man die nächste Schaltfläche **Referenz2**. Sobald sie gerückt wurde ändert sich die Beschriftung zu *Auswählen\...*, bis etwas ausgewählt wurde.

5.  Einen Befestigungsmodus aus der Liste Wählen.

6.  Versatzwerte für die Verbindung festlegen.

7.  
    **OK**drücken.

## Optionen

Mit einem Doppelklick auf (Lokales KS) **Local_CS** in der Baumstruktur oder durch einen Rechtsklick und Auswählen von **Bezug ändern** im Kontextmenü können die Werte geändert werden. Mehr Details zum Befestigungsmodus und dem Befestigungsversatz gibt es in [Part AnhangBearbeiten](Part_EditAttachment/de.md).

## Eigenschaften

### Daten

-    **MapMode**: listet den verwendeten Anhängemodus auf.

-    **Attachment Reversed**: Gibt an, ob das Koordinatensystem in seiner Ausrichtung umgekehrt ist.

-    **Attachment Offset**: Wendet eine Transformation (Übersetzung und Drehung) in Bezug auf die Platzierung von Anhängen an.

-    **Placement**: Gibt die Koordinaten und Ausrichtung des Ursprungs des Koordinatensystems an .

-    **Label**: Name des Objekts. Dieser Name kann beliebig geändert werden.

## Skripten


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/de
