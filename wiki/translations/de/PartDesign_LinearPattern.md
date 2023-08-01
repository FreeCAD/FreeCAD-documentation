---
- GuiCommand:
   Name: PartDesign LinearPattern
   Name/de: PartDesign LinearesMuster
   MenuLocation: Part Design - Muster anwenden - Lineares Muster
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
   SeeAlso: [PartDesign MehrfachTransformation](PartDesign_MultiTransform/de.md)
---

# PartDesign LinearPattern/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **PartDesign LinearesMuster** erstellt ein lineares Muster eines oder mehrerer Formelemente

![](images/PartDesign_LinearPattern_example.svg ) 
*Ein L-förmiger Block (B), der auf einer Grundplatte (A, auch als ''Träger'' bezeichnet) angebracht ist, wird für ein lineares Muster verwendet. Das Ergebnis (C) ist rechts dargestellt.''*



## Anwendung



### Erstellen

1.  Optional [aktiviere](PartDesign_Body#Active_status.md) den gewünschten Körper.
2.  Optional wähle eines oder mehrere Features im [Modellbaum](Tree_view/de.md) oder in der [3D Ansicht](3D_view.md).
3.  Es gibt mehrere Möglichkeiten um das Werkzeug zu starten:
    -   Drücke die **<img src="images/PartDesign_LinearPattern.svg" width=16px> [LinearPattern](PartDesign_LinearPattern.md)** Schaltfläche.
    -   Wähle die **Part Design → Apply a pattern → <img src="images/PartDesign_LinearPattern.svg" width=16px> LinearPattern** Option aus dem Menü.
4.  Wenn es keinen aktiven Körper gibt, oder mehr als zwei Körper im Dokument vorhanden sind, dann öffnet der **Active Body Required** Dialog und zeigt an, dass einer aktiviert werden muss. Wenn es einen einzelnen Körper gibt, dann wird dieser automatisch aktiviert.
5.  Wenn keine Features ausgewählt wurden, dann öffnet das **Select feature** [Eingabefenster](Task_panel.md): wähle eine oder mehrere (drücke die **Ctrl** Taste) aus der Liste und wähle die **OK** Schaltfläche.
6.  Das **LinearPattern parameters** [Eingabefenster](Task_panel.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
7.  Wähle die **OK** Schaltfläche um zu beenden.



### Bearbeiten

1.  Mache eines aus dem Folgenden:
    -   Doppel-Klicke das LinearPattern Objekt im [Modellbaum](Tree_view/de.md).
    -   Rechts-Klicke das LinearPattern Objekt im [Modellbaum](Tree_view/de.md) und wähle **Edit LinearPattern** aus dem Kontextmenü.
2.  Das **LinearPattern parameters** [Eingabefenster](Task_panel/de.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
3.  Drücke die **OK** Schaltfläche um zu beenden.



## Optionen

-   Um Features hinzuzufügen:
    1.  Betätige die **Add feature** Schaltfläche.
    2.  Wähle ein Feature im [Modellbaum](Tree_view/de.md) oder in der [3D Ansicht](3D_view.md).
    3.  Wieder hole alles um weitere Features hinzuzufügen.
-   Um Features zu entfernen:
    1.  Betätige die **Remove feature** Schaltfläche.
    2.  Mache eines der Folgenden:
        -   Wähle eine Feature im [Modellbaum](Tree_view/de.md) oder in der [3D Ansicht](3D_view.md).
        -   Wähle eine Feature in der Liste und betätige die **Del** Taste.
        -   Rechts-Klicke eine Feature in der Liste und wähle **Remove** aus dem Kontextmenü.
    3.  Wieder hole alles um weitere Features zu entfernen.
-   Falls es im Muster mehrere Features gibt, kann ihre Reihenfolge wichtig sein. Siehe [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   Lege die **Richtung** des Musters fest:
    -   
        **Normal zur Skizzenachse**
        
        : Die Z Achse der Skizze (nur bei skizzenbasierten Features möglich).

    -   
        **Vertikale Skizzenachse**
        
        : Die Y Achse der Skizze (idem).

    -   
        **Horizontale Skizzenachse**
        
        : Die X Achse der Skizze (idem).

    -   
        **Konstruktionslinie**
        
        : Ein eigener Zugang für jede Konstruktionslinie in der Skizze (idem).

    -   
        **Basis X Achse**
        
        : Die X Achse des Körpers.

    -   
        **Basis Y Achse**
        
        : Die Y Achse des Körpers.

    -   
        **Basis Z Achse**
        
        : Die Z Achse des Körpers.

    -   
        **Wähle Referenz...**
        
        : Wähle eine [Datum Linie](PartDesign_Line.md) im [Modellbaum](Tree_view.md) oder eine [Datum Linie](PartDesign_Line.md) oder Kante in der [3D Ansicht](3D_view.md).
-   Überprüfe die **Richtung umkehren** Checkbox um das Muster umzukehren.
-   Bestimme die **Länge** die vom Muster überdeckt wird.
-   Bestimme die Anzahl **Anzahl** (inclusive der original Feature).
-   Wenn die **Update Ansicht** Checkbox gewählt ist, dann wird die Ansicht in Echtzeit nachgebildet.



## Einschränkungen

Siehe [PartDesign PolarPattern](PartDesign_PolarPattern#Limitations.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/de
