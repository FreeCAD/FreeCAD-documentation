---
 GuiCommand:
   Name: Assembly CreateSimulation
   Name/de: Assembly SimulationErstellen
   MenuLocation: Assembly , Simulation erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: **S**
   Version: 1.1
   SeeAlso: 
---

# Assembly CreateSimulation/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:24px;"> [SimulationErstellen](Assembly_CreateSimulation/de.md): Erstellt eine Bewegungssimulation der aktuellen Baugruppe.



## Anwendung

1.  Sicherstellen, dass eine Baugruppe (Assembly-Objekt) aktiv ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateSimulation.svg" width=16px> [Simulation erstellen](Assembly_CreateSimulation.md)** drücken.
    -   Den Menüeintrag **Assembly → <img src="images/Assembly_CreateSimulation.svg" width=16px> Simulation erstellen** auswählen.
    -   Das Tastaturkürzel **S**.
3.  Wenn noch keine Simulationen vorhanden sind: Ein Simulations-Behälter (Simulations-Objekt) wird dem aktiven Assembly-Objekt hinzugefügt.
4.  Eine Simulation (Simulation-Objekt) wird dem Simulations-Behälter hinzugefügt.
5.  Das [Aufgaben-Fenster](Task_panel/de.md) **Simulationerstellen** wird geöffnet.
6.  Die grüne Plus-Schaltfläche drücken, um ein Dialogfenster zu öffnen.
    -   Eine Verbindung (ein Gelenk) in der Liste auswählen.
    -   Wenn erforderlich, eine Bewegungsart auswählen
    -   Wahlweise die Formel bearbeiten.
    -   Die Schaltfläche **OK** drücken, um das Dialogfenster schließen.
7.  Wahlweise die Einstellungen der Simulation anpassen.
8.  Die Schaltfläche **Generate** drücken.
9.  Ein Abschnitt **Animation Player** wird im Aufgaben-Fenster hinuzgefügt.
    -   Die Steuerungs-Widgets verwenden, um die Baugruppe zu animieren.
10. Die Schaltfläche **OK** drücken, um das Werkzeug zu beenden und das Aufgaben-Fenster zu schließen.



## Hinweise

-   Der unbenannte Dialog hilft, einen Antrieb festzulegen:
    1.  Die gewünschte Verbindung (Gelenk) in der Liste the **Joints** auswählen.
    2.  Steht für die ausgewählte Verbindung mehr als eine Bewegungsart zur Verfügung, wird die passende in der Liste **Motion Type** ausgewählt.
    3.  Die Formel bearbeiten, die das Verhältnis zwischen der ablaufenden Zeit und der Winkel- bzw. Längenänderung beschreibt.
    4.  Wahlweise die Schaltfläche Hilfe drücken, um Beispiele für die Beschreibungen in der **Formel** anzuzeigen.
-   In der Formel scheint **time** 1 rad pro Sekunde darzustellen, und mit 360° = 6,283 Rad für eine volle Umdrehung, haben wir folgende Möglichkeiten eine volle Umdrehung auszuführen:
    -   
        {{Value|6,283 * time}}
        
        im Eingabefeld Formula eingeben und eine Dauer (End-Wert - Start-Wert) von einer Sekunde unter Simulation settings im Aufgaben-Fenster.

    -   
        {{Value|1 * time}}
        
        im Eingabefeld Formula eingeben und eine Dauer (End-Wert - Start-Wert) von 6,283 Sekunden unter Simulation settings im Aufgaben-Fenster.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

### Simulations

Ein **Simulations**-Behälter ist ein {{Incode|Assembly::SimulationGroup}}-Objekt, das von einem [App DocumentObjectGroup](App_DocumentObjectGroup/de.md)-Objekt abgeleitet wird und alle seine Eigenschaften erbt. Es besitzt keine weiteren Eigenschaften.

### Simulation

Ein **Simulation**-Objekt wird von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



#### Daten


{{Properties_Title/de|Basis}}

-    **Group|LinkList**: Die Bewegungen (Motion-Objekte) des Objekts.

-    **_ Group Touched|Bool|hidden**:


{{Properties_Title|Simulation}}

-    **a Time Start|Time**: Standardwert {{value|0.0 s}}. Startzeit der Simulation.

-    **b Time End|Time**: Standardwert {{value|1.0 s}}. Endzeit der Simulation.

-    **c Time Step Output|Time**: Standardwert {{value|0.01 s}}. Dauer eines Simulationsschrittes für die Ausgabe.

-    **f Global Error Tolerance|Float**: Standardwert s {{value|1e-06}}. Integration der globalen Fehler-Toleranz.

-    **j Frames Per Second|Integer**: Standardwert {{value|30}}. Bildrate in Bilder pro Sekunde.



### Ansicht


{{Properties_Title|Space}}

-    **Decimals|Integer**: Standardwert {{value|9}}. Die Anzahl der Nachkomma, die für berechnete Texte verwendet wird.



### Bewegung

Ein **Motion**-Objekt wird von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Außerdem besitzt es die folgenden zusätzlichen Eigenschaften:



#### Daten 


{{Properties_Title|Motion}}

-    **Formula|String**: Die Formel für die Bewegung. Zum Beispiel {{Value|1.0*time}}.

-    **Joint|XLinkSubHidden**: Die Verbindung (Gelenk), das mit der Bewegung angetrieben wird.

-    **Motion Type|Enumeration**: Die Art der Bewegung. Die Optionen sind: {{Value|Angular}} (Drehung) und {{Value|Linear}} (Verschiebung).





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateSimulation/de
