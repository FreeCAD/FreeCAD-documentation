---
 GuiCommand:
   Name: PartDesign LinearPattern
   Name/de: PartDesign LinearesMuster
   MenuLocation: Part Design , Muster anwenden , Lineares Muster
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_MultiTransform/de
---

# PartDesign LinearPattern/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **PartDesign LinearesMuster** erstellt aus einem oder mehreren Formelementen ein lineares Muster.

![](images/PartDesign_LinearPattern_example.svg ) 
*Ein L-förmiger Block (B), der auf einer Grundplatte (A, auch als ''Träger'' bezeichnet) angebracht ist, wird für ein lineares Muster verwendet. Das Ergebnis (C) ist rechts dargestellt.''*



## Anwendung



### Erstellen

1.  Wahlweise den gewünschten Körper [aktivieren](PartDesign_Body/de#Aktiver_Status.md) .
2.  Wahlweise ein oder mehrere Formelemente in der [Baumansicht](Tree_view/de.md) oder in der [3D-Ansicht](3D_view.md) auswählen.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_LinearPattern.svg" width=16px> [Lineares Muster](PartDesign_LinearPattern/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_LinearPattern.svg" width=16px> Lineares Muster** auswähen.
4.  Ist kein Körper aktiv und es sind zwei oder mehr Körper im Dokument vorhanden, wird der Dialog **Aktiver Körper erforderlich** geöffnet und zeigt an, dass einer aktiviert werden muss. Gibt es nur einen einzigen Körper, wird dieser automatisch aktiviert.
5.  Wurde kein Formelement ausgewählt, wird der [Aufgaben-Bereich](Task_panel/de.md) **Element auswählen** geöffnet: Ein oder mehrere (mit gedrücker **Ctrl**-Taste) Formelemente in der Liste auswählen und die Schaltfläche **OK** drücken.
6.  Der [Aufgaben-Bereich](Task_panel/de.md) **Parameter des linearen Musters** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Die Schaltfläche **OK** drücken, um zu beenden.



### Bearbeiten

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Ein Doppelklick auf das LinearPattern-Objekt in der [Baumansicht](Tree_view/de.md).
    -   Ein Rechtsklick auf das LinearPattern-Objekt in der [Baumansicht](Tree_view/de.md) und die Menüoption **Lineares Muster bearbeiten** im Kontextmenü auswählen.
2.  Der [Aufgaben-Bereich](Task_panel/de.md) **Parameter des linearen Musters** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Die Schaltfläche **OK** drücken, um zu beenden.



## Optionen

-   Modus auswählen:
    -   
        **Körper transformieren**
        
        : Transformiert die Form des gesamten Körpers (Standardeinstellung). {{Version/de|1.0}}

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

-   Die **Richtung** des Musters festlegen:
    -   
        **Normal zur Skizzenachse**
        
        : Die Z-Achse der Skizze (steht nur für skizzenbasierte Formelemente zur Verfügung).

    -   
        **Vertikale Skizzenachse**
        
        : Die Y-Achse der Skizze (wie vorher).

    -   
        **Horizontale Skizzenachse**
        
        : Die X-Achse der Skizze (wie vorher).

    -   
        **Konstruktionslinie**
        
        : Ein eigener Eintrag für jede Hilfslinie in der Skizze (wie vorher).

    -   
        **Basis X-Achse**
        
        : Die X-Achse des Körpers.

    -   
        **Basis Y-Achse**
        
        : Die Y-Achse des Körpers.

    -   
        **Basis Z-Achse**
        
        : Die Z-Achse des Körpers.

    -   
        **Wähle Referenz auswählen...**
        
        : Eine [Bezugslinie](PartDesign_Line/de.md) in der [Baumansicht](Tree_view/de.md) bzw. eine [ Bezugslinie](PartDesign_Line/de.md) oder Kante in der [3D-Ansicht](3D_view/de.md) auswählen.

-   Die Checkbox **Richtung umkehren** aktivieren, um das Muster umzukehren.

-    {{Version/de|1.0}}: Den **Modus** der Länge eingeben:

    -   
        **Gesamtlänge**
        
        : Die **Länge** eingeben, die von einem gegebenen Punkt des Originals bis zum selben Punkt auf der letzten Instanz gemessen wird.

    -   
        {{Version/de|1.0}}
        
        : **Versetzen**: Den **Abstand** eingeben, der von einem gegebenen Punkt des Originals bis zum selben Punkt auf der folgenden Instanzen gemessen wird. Für n Objekte: Gesamtlänge = (n - 1) \* Abstand.

-   Die **Anzahl** (inklusive des originalen Formelements) eingeben.

-   Ist die Checkbox **Ansicht aktualisieren** aktiviert, wird die Ansicht in Echtzeit aktualisiert.



## Einschränkungen

Siehe [PartDesign PolarPattern](PartDesign_PolarPattern#Limitations.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/de
