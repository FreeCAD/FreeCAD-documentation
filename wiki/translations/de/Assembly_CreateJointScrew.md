---
 GuiCommand:
   Name: Assembly CreateJointScrew
   Name/de: Assembly SpindelverbindungErstellen
   MenuLocation: Assembly , Schraubverbindung erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointScrew/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:24px;"> [Assembly SpindelverbindungErstellen](Assembly_CreateJointScrew/de.md) erstellt eine Spindelverbindung (wendelförmige Verbindung), die die Verschiebung eines Bauteils einer prismatischen Verbindung und die Drehung eines Bauteils einer Drehverbindung koppelt. In Verbindung mit den schon vorhandenen Verbindungen kann diese Verbindung zum Simulieren eines Spindelgetriebes eingesetzt werden.



## Anwendung

1.  Wahlweise zwei geometrische Elemente zweier unterschiedlicher Formen auswählen, die vorher zum Festlegen einer prismatischen Verbindung (Slider joint) und einer Drehverbindung (Revolute joint) verwendet wurden.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateJointScrew.svg" width=16px> [Spindelverbindung erstellen](Assembly_CreateJointScrew/de.md)** drücken.
    -   Den Menüeintrag **Assembly → <img src="images/Assembly_CreateJointScrew.svg" width=16px> Spindelverbindung erstellen** auswählen.
    -   Das Tastaturkürzel **W**.
3.  Der Dialog **Verbindung erstellen** wird im [Aufgaben-Fenster](Task_panel/de.md) geöffnet und zeigt eine Liste der vorausgewählten Elemente.
4.  Für weiter Schritte siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Anwendung.md).



## Hinweise

-   Der Wert Pitch radius entspricht der Steigung (pitch) einer Spindel (Schraube). Er wird in der {{PropertyData/de|Distance}} gespeichert und legt die Verschiebung pro eine Umdrehung der Spindel fest.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **Screw**-Objekt ist von einem [App-FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Eigenschaften.md) für weitere Eigenschaften.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointScrew/de
