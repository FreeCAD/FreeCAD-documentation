---
 GuiCommand:
   Name: PartDesign Mirrored
   Name/de: PartDesign Spiegeln
   MenuLocation: Part Design , Muster anwenden , Spiegeln
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_MultiTransform/de
---

# PartDesign Mirrored/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> **PartDesign Spiegeln** spiegelt ein oder mehrere Formelemente über eine Ebene.

![](images/PartDesign_Mirrored_example.svg ) 
*Ein Formelement Tasche, das aus einer Skizze erstellt wurde, die einen Kreis (A) enthält, wird verwendet, um ein gespiegeltes Formelement zu erstellen. Die vertikale Achse der Skizze (B) wird als Symmetrieachse verwendet, um die Spiegelebene festzulegen. Das Ergebnis (C) wird rechts angezeigt.*



## Anwendung



### Erstellen

1.  Optional den gewünschten Körper [aktivieren](PartDesign_Body/de#Aktiver_Status.md).
2.  Optional ein oder mehrere Formelemente auswählen.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_Mirrored.svg" width=16px> [Spiegeln](PartDesign_Mirrored/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_Mirrored.svg" width=16px> Spiegeln** auswählen.
4.  Ist kein Körper aktiv und es sind zwei oder mehr Körper im Dokument vorhanden, wird der Dialog **Aktiver Körper erforderlich** geöffnet und zeigt an, dass einer aktiviert werden muss. Gibt es nur einen einzigen Körper, wird dieser automatisch aktiviert.
5.  Wurde kein Formelement ausgewählt, wird der [Aufgaben-Bereich](Task_panel/de.md) **Element auswählen** geöffnet: Ein oder mehrere (mit gedrücker **Ctrl**-Taste) Formelemente in der Liste auswählen und die Schaltfläche **OK** drücken.
6.  Der [Aufgaben-Bereich](Task_panel/de.md) **Parameter der Spiegelung** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Die Schaltfläche **OK** drücken, um zu beenden.



### Bearbeiten

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Ein Doppelklick auf das PolarPattern-Objekt in der [Baumansicht](Tree_view/de.md).
    -   Ein Rechtsklick auf das PolarPattern-Objekt in der [Baumansicht](Tree_view/de.md) und die Menüoption **Spiegelung bearbeiten** im Kontextmenü auswählen.
2.  Der [Aufgaben-Bereich](Task_panel/de.md) **Parameter der Spiegelung** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Die Schaltfläche **OK** drücken, um zu beenden.



## Optionen

-   Modus auswählen:
    -   
        **Körper transformieren**
        
        : Transformiert die Form des gesamten Körpers (Standardeinstellung). {{Version/de|1.0}}

    1.  Die Schaltfläche **Add feature** drücken.

    -   
        **Werkzeugformen transformieren**
        
        : Transformiert die einzelnen Forme der ausgewählten Formelemente.

        -   Formelemente hinzufügen:
            1.  Die Schaltfläche **Element hinzufügen** drücken.
            2.  Ein Formelement in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen.
            3.  Wiederholen, um weitere Formelemente hinzuzufügen.
        -   Formelemente entfernen:
            1.  Die Schaltfläche **Element entfernen** drücken.
            2.  Eine der folgenden Möglichkeiten wählen:
                -   Ein Formelement in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view/de.md) auswählen.
                -   Ein Formelement in der oberen Liste auswählen und die **Del**-Taste drücken.
                -   Mit der rechten Maustaste ein Formelement in der oberen Liste anklicken und **Entfernen** aus dem Kontextmenü auswählen.
            3.  Wiederholen, um weitere Formelemente zu entfernen.
        -   Wenn ein Muster mehrere Formelemente enthält, kann deren Reihenfolge wichtig sein. Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Formelemente_ordnen.md).
-   Die **Spiegelebene** festlegen:
    -   
        **Vertikale Skizzenachse**
        
        : Die Y-Achse der Skizze (die Spiegelebene verläuft durch diese Referenz und die Z-Achse der Skizze; steht nur für skizzenbasierte Formelemente zur Verfügung).

    -   
        **Horizontale Skizzenachse**
        
        : Die X-Achse der Skizze (wie vorher).

    -   
        **Konstruktionslinie**
        
        : Ein eigener Eintrag für jede Hilfslinie in der Skizze (wie vorher).

    -   
        **Basis XY Ebene**
        
        : Die XY-Ebene des Körpers.

    -   
        **Basis YZ Ebene**
        
        : Die YZ-Ebene des Körpers.

    -   
        **Basis XZ Ebene**
        
        : Die XZ-Ebene des Körpers.

    -   
        **Wähle Referenz...**
        
        : Eine ebene Fläche in der [3D-Ansicht](3D_view/de.md) auswählen.
-   Ist die Checkbox **Ansicht aktualisieren** aktiviert, wird die Ansicht in Echtzeit aktualisiert.



## Einschränkungen

Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Einschränkungen.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/de
