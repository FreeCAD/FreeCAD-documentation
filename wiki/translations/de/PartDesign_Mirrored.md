---
- GuiCommand:
   Name:PartDesign Mirrored
   Name/de:PartDesign Spiegeln
   MenuLocation:Part Design → Muster anwenden → Spiegeln
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign MehrfachTransformation](PartDesign_MultiTransform/de.md)
---

# PartDesign Mirrored/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> **PartDesign Spiegeln** spiegelt ein oder mehrere Formelemente über eine Ebene.

![](images/PartDesign_Mirrored_example.svg ) 
*Ein Formelement Tasche, das aus einer Skizze erstellt wurde, die einen Kreis (A) enthält, wird verwendet, um ein gespiegeltes Formelement zu erstellen. Die vertikale Achse der Skizze (B) wird als Symmetrieachse verwendet, um die Spiegelebene festzulegen. Das Ergebnis (C) wird rechts angezeigt.*



## Anwendung



### Erstellen

1.  Optional [aktiviere](PartDesign_Body#Active_status.md) den gewünschten Körper.
2.  Optional wähle eine oder mehrere Features.
3.  Es gibt mehrere Möglichkeiten um das Werkzeug zu starten:
    -   Drücke die **<img src="images/PartDesign_Mirrored.svg" width=16px> [Mirrored](PartDesign_Mirrored.md)** Schaltfläche.
    -   Wähle die **Part Design → Apply a pattern → <img src="images/PartDesign_Mirrored.svg" width=16px> Mirrored** Option aus dem Menü.
4.  Wenn es keinen aktiven Körper gibt, oder mehr als zwei Körper im Dokument vorhanden sind, dann öffnet der **Active Body Required** Dialog und zeigt an, dass einer aktiviert werden muss. Wenn es einen einzelnen Körper gibt, dann wird dieser automatisch aktiviert.
5.  Wenn keine Features ausgewählt wurden, dann öffnet das **Select feature** [Eingabefenster](Task_panel.md): wähle eine oder mehrere (drücke die **Ctrl** Taste) aus der Liste und wähle die **OK** Schaltfläche.
6.  Das **Mirrored parameters** [Eingabefenster](Task_panel.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
7.  Wähle die **OK** Schaltfläche um zu beenden.



### Bearbeiten

1.  Mache eines aus dem Folgenden:
    -   Doppel-Klicke das Spiegeln Objekt im [Modellbaum](Tree_view.md).
    -   Rechts-Klicke das Spiegeln Objekt im [Modellbaum](Tree_view.md) und wähle **Edit Mirrored** aus dem Kontextmenü.
2.  Das **Mirrored parameters** [Eingabefenster](Task_panel.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
3.  Drücke die **OK** Schaltfläche um zu beenden..



## Optionen

-   Um Features hinzuzufügen:
    1.  Betätige die **Add feature** Schaltfläche.
    2.  Wähle ein Feature im [Modellbaum](Tree_view.md) oder in der [3D Ansicht](3D_view.md).
    3.  Wieder hole alles um weitere Features hinzuzufügen.
-   Um Features zu entfernen:
    1.  Betätige die **Remove feature** Schaltfläche.
    2.  Mache eines der Folgenden:
        -   Wähle eine Feature im [Modellbaum](Tree_view.md) oder in der [3D Ansicht](3D_view.md).
        -   Wähle eine Feature in der Liste und betätige die **Del** Taste.
        -   Rechts-Klicke eine Feature in der Liste und wähle **Remove** aus dem Kontextmenü.
    3.  Wieder hole alles um weitere Features zu entfernen.
-   Falls es im Muster mehrere Features gibt, kann ihre Reihenfolge wichtig sein. Siehe [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   Lege die **Spiegelebene** fest:
    -   
        **Vertikale Skizzenachse**
        
        : Die Y Achse der Skizze (Die Spiegelebene verläuft durch diese Referenz und die Z Achse der Skizze, nur möglich für skizzenbasierte Features).

    -   
        **Horizontale Skizzenachse**
        
        : Die X Achse der Skizze (idem).

    -   
        **Konstruktionslinie**
        
        : Ein eigener Zugang für jede Konstruktionslinie in der Skizze (idem).

    -   
        **Basis XY Ebene**
        
        : Die XY Ebene des Körpers.

    -   
        **Basis YZ Ebene**
        
        : Die YZ Ebene des Körpers.

    -   
        **Basis XZ Ebene**
        
        : Die XZ Ebene des Körpers.

    -   
        **Wähle Referenz...**
        
        : Wähle eine ebene Körperfläche in der [3D Ansicht](3D_view.md).
-   Wenn die **Update Ansicht** Checkbox gewählt ist, dann wird die Ansicht in Echtzeit nachgebildet.



## Einschränkungen

Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Einschränkungen.md).





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/de
