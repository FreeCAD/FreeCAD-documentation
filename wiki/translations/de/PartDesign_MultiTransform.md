---
- GuiCommand:/de
   Name:PartDesign MultiTransform
   Name/de:PartDesign MultiTransform
   MenuLocation:Part Design → Muster anwenden → Mehrfach-Transformation erstellen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign Spiegeln](PartDesign_Mirrored/de.md), [PartDesign LinearesMuster](PartDesign_LinearPattern/de.md), [PartDesign PolaresMuster](PartDesign_PolarPattern/de.md), [PartDesign Skalieren](PartDesign_Scaled/de.md)
---

# PartDesign MultiTransform/de

## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:24px;"> **PartDesign MehrfachTransformation** erstellt ein Muster aus einem oder mehreren Formelementen. Das Muster kann mehrere Transformationen enthalten, wobei jede folgende Transformation auf das Ergebnis der vorherigen Transformation angewendet wird.

Folgende Transformationen stehen zur Verfügung: <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Spiegeln](PartDesign_Mirrored/de.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [LinearesMuster](PartDesign_LinearPattern/de.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:16px;"> [PolaresMuster](PartDesign_PolarPattern/de.md) und <img alt="" src=images/PartDesign_Scaled.svg  style="width:16px;"> [Skaliert](PartDesign_Scaled/de.md). Die ersten drei stehen auch als separate Werkzeuge zur Verfügung.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Ein Lochmuster, das aus einem einzelnen Loch erstellt wurde, wobei zuerst ein lineares Muster mit 2 Vorkommen und danach ein polares Muster mit 8 Vorkommen angewendet wurde.*

## Anwendung

### Erstellen

1.  Bei Bedarf den korrekten Körper [aktivieren](PartDesign_Body#Active_status/de.md).
2.  Wahlweise können ein oder mehrere Elemente in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) ausgewählt werden.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
4.  Falls kein Körper aktiviert ist und sich zwei oder mehr Körper im Dokument befinden, öffnet sich der Dialog **Aktiver Körper erforderlich** mit der Aufforderung einen zu aktivieren. Wenn nur ein einziger Körper vorhanden ist, wird dieser automatisch aktiviert.
5.  Wenn kein Formelement ausgewählt wurde, öffnet sich der [Aufgabenbereich](Task_panel/de.md) {{MenuCommand/de|Element auswählen}}: Ein oder mehrere (**Ctrl**-Taste gedrückt halten) aus der Liste auswählen und die Schaltfläche **OK** drücken.
6.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.

### Bearbeiten

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung:
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **MultiTransform bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.

### Kombinieren vorhandener Transformationen 

Es ist möglich ein MultiTransform-Objekt von vorhandenen Transformationen wie [Spiegeln](PartDesign_Mirrored/de.md), [Lineares Muster](PartDesign_LinearPattern/de.md) und [Polares Muster](PartDesign_PolarPattern/de.md) zu erstellen.

1.  Die {{PropertyData/de|Originals}} der bestehenden Transformationen überprüfen, ob sie auf dieselben Formelemente angewendet werden.
2.  Diese Formelemente in der [Baumansicht](Tree_view/de.md) auswählen.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
4.  Der [Aufgabenbereich](Task_panel/de.md) {{MenuCommand/de|Parameter der Mehrfach-Transformation}} wird geöffnet.
5.  Die Schaltfläche **OK** am oberen Rand drücken.
6.  Die {{PropertyData/de|Tranformations}} des erstellten MultiTransform-Objekts bearbeiten:
    1.  Auf das Feld klicken.
    2.  Die Schaltfläche **...**, die dann erscheint, anklicken.
    3.  Der Dialog **Link** wird geöffnet.
    4.  Mit gedrückter **Ctrl**-Taste werden die bestehenden Transformationen ausgewählt.
    5.  Die Schaltfläche **OK** drücken.
7.  Wahlweise das MultiTransform-Objekt [bearbeiten](#Bearbeiten.md), siehe oben.

## Optionen

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
-   Transformationen hinzufügen:
    1.  Wenn schon Transformationen vorhanden sind: Die Transformation auswählen, hinter der die neue Transformation eingefügt werden soll.
    2.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.
    3.  Eine der folgenden Möglichkeiten des Kontextmenüs auswählen:
        -   
            **Spiegelung hinzufügen**
            
            . Siehe [PartDesign Mirrored](PartDesign_Mirrored.md).

        -   
            **Lineares Muster hinzufügen**
            
            . Siehe [PartDesign LinearesMuster](PartDesign_LinearPattern/de.md).

        -   
            **Polares Muster hinzufügen**
            
            Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de.md).

        -   
            **Skalierte Transformation hinzufügen**
            
            . Siehe [PartDesign Skalieren](PartDesign_Scaled/de.md).
    4.  Die ausgewählte Transformation wird zur Liste hinzugefügt und die Einstellungen der Transformationen werden unterhalb der Liste angezeigt.
    5.  Die Einstellungen nach Bedarf anpassen.
    6.  Die **OK**-Leiste am unteren Rand drücken.
    7.  Wiederholen, um weitere Transformationen hinzuzufügen.
-   Transformationen bearbeiten:
    1.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.

    2.  
        **Bearbeiten**
        
        aus dem Kontextmenü auswählen.

    3.  Die Einstellungen nach Bedarf anpassen.

    4.  Die **OK**-Leiste am unteren Rand drücken.
-   Die Reihenfolge der Transformationen ändern:
    1.  Mit der rechten Maustaste in die Liste **Transformationen** klicken.

    2.  
        **Nach oben verschieben**
        
        or **Nach unten verschieben** aus dem Kontextmenü auswählen.
-   Wenn die Checkbox **Ansicht aktualisieren** aktiviert ist, erfolgt die aktualisierung in Echtzeit.

## Einschränkungen

Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Einschränkungen.md).

## Example

You can use this tool to create a fully parametric part that is symmetrical about two axes from a sketch.

This could be a 150x100x10mm large mounting plate for a motor with symmetric holes.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width:400px;">

1.  Create a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Body](PartDesign_Body.md) and add a <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [sketch](PartDesign_NewSketch.md) on one of its base planes.
2.  In the sketch create geometry for one quadrant of the part (i.e. the upper right quadrant).
    -   Note that the constraints must also only cover a quarter of the part, e.g. instead of the full dimension of {{Value|150mm}} enter {{Value|150/2mm}} or {{Value|75mm}}.
    -   Make sure the sketch is closed by adding lines along the vertical and horizontal axes.
3.  Extrude the part with <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md).
4.  Select <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> **PartDesign MultiTransform**.
5.  The task dialog opens.
6.  The last feature of the Body is already selected. Since we want to mirror that feature we can ignore the **Add feature** and **Remove feature** buttons.
7.  Right-click in the **Transformations** field and select **Add mirrored transform** from the context menu.
8.  For the **Plane** select **Vertical sketch axis**.
9.  If the **Update view** checkbox is checked, you should now see the part mirrored about one axis.
10. Again select **Add mirrored transform** from the context menu of the **Transformations** field.
11. Now for the **Plane** select **Horizontal sketch axis**.
12. Press the **OK** button to finish.
13. To remove the edges along the axes of symmetry in the final result, set the **Refine** property of the new feature to {{Value|true}} in the [Property editor](Property_editor.md).

To verify that the part is fully parametric open the initial sketch with the quarter part and change one dimension, say a hole diameter. After closing the sketch the three other holes will have changed accordingly. This works with all other dimensions as well. A sketch modelling the full part with a single extrusion and no mirroring would be a lot more complex and all later changes would be more complicated.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/de
