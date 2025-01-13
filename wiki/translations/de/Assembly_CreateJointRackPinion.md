---
 GuiCommand:
   Name: Assembly CreateJointRackPinion
   Name/de: Assembly ZahnstangeRitzelVerbindungErstellen
   MenuLocation: Assembly , Zahnstange-Ritzel-Verbindung erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: **Q**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointRackPinion/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:24px;"> [Assembly ZahnstangeRitzelVerbindung](Assembly_CreateJointRackPinion/de.md) erstellt eine Zahnstange-Ritzel-Verbindng, die die Verschiebung eines Bauteils einer prismatischen Verbindung und die Drehung eines Bauteils einer Drehverbindung koppelt.



## Anwendung

1.  Wahlweise zwei geometrische Elemente zweier unterschiedlicher Bauteile auswählen, die vorher zum Festlegen einer prismatischen Verbindung (Slider joint) und einer Drehverbindung (Revolute joint) verwendet wurden.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateJointRackPinion.svg" width=16px> [Zahnstange-Ritzel-Verbindung erstellen](Assembly_CreateJointRackPinion/de.md)** drücken.
    -   Den Menüeintrag **Assembly → <img src="images/Assembly_CreateJointRackPinion.svg" width=16px> Zahnstange-Ritzel-Verbindung erstellen** auswählen.
    -   Das Tastaturkürzel **Q**.
3.  Der Dialog **Verbindung erstellen** wird im [Aufgaben-Fenster](Task_panel/de.md) geöffnet und zeigt eine Liste der vorausgewählten Elemente.
4.  Für weiter Schritte siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Anwendung.md).



## Hinweise

-   Pitch radius bezieht sich auf den Teilkreis des Ritzels. Er wird in der {{PropertyData/de|Distance}} gespeichert und ist die Grundlage zum Berechnen des Verhältnisses von Drehung zu Verschiebung.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **RackPinion**-Objekt ist von einem [App-FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Siehe [Assembly StarreVerbindungErstellen](Assembly_CreateJointFixed/de#Eigenschaften.md) für weitere Eigenschaften.


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointRackPinion/de
