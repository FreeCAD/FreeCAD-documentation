---
 GuiCommand:
   Name: PartDesign Point
   Name/de: PartDesign Bezugspunkt erstellen
   MenuLocation: Part Design , Bezugselement erstellen , Bezugspunkt erstellen
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_Line/de, PartDesign_Plane/de
---

# PartDesign Point/de

## Beschreibung

Erstellt einen Bezugspunkt. Dieser kann innerhalb des aktuellen Körpers referenziert werden. Dies gilt ebenfalls für weitere Referenzobjekte.

![](images/DatumPoint.png ) 
*Ein Referenzpunkt, der mit einem Offset von {{Value|2* in Z Richtung die Kugel am Z Scheitelpunkt referenziert.}}

## Anwendung

1.  Schaltfläche **<img src="images/PartDesign_Point.svg" width=24px> '''Bezugspunkt erstellent'''** drücken.

2.  Die Parameter des Punktes definieren. Eine erste Referenz in der 3D-Ansicht auswählen, um die verfügbaren Verbindungsarten zu filtern.

3.  Abhängig von der ausgewählten Referenz, können eine oder mehrere Verbindungsarten in der Liste vorhanden sein. Die wahrscheinlichste wird automatisch ausgewählt und in der Liste fett dargestellt. Der Text *Angehängt im Modus:* zusammen mit dem Namen der Verbindungsart erscheint in grün über der Liste der Referenzen.

4.  Um eine weitere Referenz hinzuzufügen, drückt man die nächste **Referenz**-Schaltfläche. Sobald sie gerückt wurde ändert sich die Beschriftung zu *Auswählen\...*, bis etwas ausgewählt wurde.

5.  Einen Befestigungsmodus aus der Liste Wählen.

6.  Versatzwerte für die Verbindung festlegen.

7.  
    **OK**drücken.

## Optionen

Doppel-Klicke das Referenzpunkt Label im Modellbaum oder klicke dies einfach und selektiere \"Bezug ändern\" oder wähle ein Referenzobjekt mit der rechten Maustaste im Kontextmenu. Details findet man bei Referenzmodus und Offsets , siehe: [Part AnhangBearbeiten](Part_EditAttachment/de.md).

## Eigenschaften

-    {{PropertyData/de|MapMode}}: Listet die benutzten Referenzmodi.

-    {{PropertyData/de|Attachment Offset}}: Transformiert ( Verschiebung und Rotation ) das Objekt in Bezug auf seinen Referenzpunkt und seine Richtung.

-    {{PropertyData/de|Label}}: änderbarer Name des Objekts

## Einschränkungen

-   Der Bezugspunkt kann nicht als Referenz für Rohr und Loft Features benutzt werden.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/de
