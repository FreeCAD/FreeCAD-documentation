---
 GuiCommand:
   Name: Assembly CreateJointBelt
   Name/de: Assembly RiemenverbindungErstellen
   MenuLocation: Assembly , Zahnrad-/Riemenverbindung erstellen , Riemenverbindung erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBelt/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:24px;"> [Assembly RiemenverbindungErstellen](Assembly_CreateJointBelt/de.md) erstellt eine Riemenverbindung, die die Drehungen zweier Bauteile aus unterschiedlichen Drehverbindungen koppelt. In Verbindung mit den schon vorhandenen Verbindungen kann diese Kopplung zum Simulieren von Riemenantrieben, Steuerriemen- Steuerkettengetrieben usw. eingesetzt werden.



## Anwendung

1.  Wahlweise zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die vorher zum Festlegen zweier Drehverbindungen (Revolute joints) verwendet wurden.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateJointBelt.svg" width=16px> [Riemenverbindung erstellen](Assembly_CreateJointBelt/de.md)** drücken.
    -   Den Menüeintrag **Assembly →  Zahnrad-/Riemenverbindung erstellen →  <img src="images/Assembly_CreateJointBelt.svg" width=16px> Riemenverbindung erstellen** auswählen.
3.  Der Dialog **Verbindung erstellen** wird im [Aufgaben-Fenster](Task_panel/de.md) geöffnet und zeigt eine Liste der vorausgewählten Elemente.
4.  Für weiter Schritte siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Anwendung.md).



## Hinweise

-   Radius1 und Radius2 beziehen sich auf den Teilkreis von Zahnriemenscheiben oder den Außendurchmesser von Riemenscheiben. Ihre Werte werden in {{PropertyData/de|Distance}} und {{PropertyData/de|Distance2}} gespeichert und legen das Verhältnis zwischen den beiden Drehungen fest.
-   Verwendet man denselben Wert für beide Radien, können damit die beiden Enden einer flexiblen Welle verbunden werden (wenn die Drehrichtung nicht passt, kann entweder eine [Drehverbindung](Assembly_CreateJointRevolute/de.md) umgekehrt werden oder man verwendet die [Zahnradverbindung](Assembly_CreateJointGears/de.md) statt dieser).



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **Belt**-Objekt ist von einem [App-FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Eigenschaften.md) für weitere Eigenschaften.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBelt/de
