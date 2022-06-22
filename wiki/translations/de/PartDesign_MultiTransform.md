---
- GuiCommand   */de
   Name   *PartDesign MultiTransform
   Name/de   *PartDesign MultiTransform
   MenuLocation   *Part Design → Muster anwenden → Mehrfach-Transformation erstellen
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso   *[PartDesign Spiegeln](PartDesign_Mirrored/de.md), [PartDesign LinearesMuster](PartDesign_LinearPattern/de.md), [PartDesign PolaresMuster](PartDesign_PolarPattern/de.md), [PartDesign Skalieren](PartDesign_Scaled/de.md)
---

# PartDesign MultiTransform/de

## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *24px;"> **PartDesign MehrfachTransformation** erstellt ein Muster aus einem oder mehreren Formelementen. Das Muster kann mehrere Transformationen enthalten, wobei jede folgende Transformation auf das Ergebnis der vorherigen Transformation angewendet wird.

Folgende Transformationen stehen zur Verfügung   * <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *16px;"> [Spiegeln](PartDesign_Mirrored/de.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width   *16px;"> [LinearesMuster](PartDesign_LinearPattern/de.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *16px;"> [PolaresMuster](PartDesign_PolarPattern/de.md) und <img alt="" src=images/PartDesign_Scaled.svg  style="width   *16px;"> [Skaliert](PartDesign_Scaled/de.md). Die ersten drei stehen auch als separate Werkzeuge zur Verfügung.

<img alt="" src=images/multitransform_example.png  style="width   *600px;"> 
*Ein Lochmuster, das aus einem einzelnen Loch erstellt wurde, wobei zuerst ein lineares Muster mit 2 Vorkommen und danach ein polares Muster mit 8 Vorkommen angewendet wurde.*

## Anwendung

### Erstellen

1.  Bei Bedarf den korrekten Körper [aktivieren](PartDesign_Body#Active_status/de.md).
2.  Wahlweise können ein oder mehrere Elemente in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) ausgewählt werden.
3.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen   *
    -   Die Schaltfläche **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Mehrfach-Transformation erstellen](PartDesign_MultiTransform/de.md)** drücken.
    -   Den Menüeintrag **Part Design → Muster anwenden → <img src="images/PartDesign_MultiTransform.svg" width=16px> Mehrfach-Transformation erstellen** auswählen.
4.  Falls kein Körper aktiviert ist und sich zwei oder mehr Körper im Dokument befinden, öffnet sich der Dialog **Aktiver Körper erforderlich** mit der Aufforderung einen zu aktivieren. Wenn nur ein einziger Körper vorhanden ist, wird dieser automatisch aktiviert.
5.  Wenn kein Formelement ausgewählt wurde, öffnet sich der [Aufgabenbereich](Task_panel/de.md) {{MenuCommand/de|Element auswählen}}   * Ein oder mehrere (**Ctrl**-Taste gedrückt halten) aus der Liste auswählen und die Schaltfläche **OK** drücken.
6.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
7.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.

### Bearbeiten

1.  Eine der folgenden Möglichkeiten startet die Bearbeitung   *
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
    -   Das MultiTransform-Objekt in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **MultiTransform bearbeiten** aus dem Kontextmenü auswählen.
2.  Der [Aufgabenbereich](Task_panel/de.md) **Parameter der Mehrfach-Transformation** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Zum Fertigstellen die Schaltfläche **OK** am oberen Rand drücken.

### Kombinieren vorhandener Transformationen 

Es ist möglich ein MultiTransform-Objekt von vorhandenen Transformationen wie [Spiegeln](PartDesign_Mirrored/de.md), [Lineares Muster](PartDesign_LinearPattern/de.md) und [Polares Muster](PartDesign_PolarPattern/de.md) zu erstellen.

1.  Check the **Originals** property of the existing transformations to make sure they have been applied to the same features.
2.  Select those features in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool   *
    -   Press the **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Create MultiTransform](PartDesign_MultiTransform.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_MultiTransform.svg" width=16px> Create MultiTransform** option from the menu.
4.  The **MultiTransform parameters** [task panel](Task_panel.md) opens.
5.  Press the **OK** button at the top.
6.  Edit the **Tranformations** property of the created MultiTransform object   *
    1.  Click in the field.
    2.  Press the **...** button that appears.
    3.  The **Link** dialog opens.
    4.  Hold down the **Ctrl** key and select the existing transformations.
    5.  Press the **OK** button.
7.  Optionally [edit](#Edit.md) the MultiTransform object, see above.

## Optionen

-   To add features   *
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features   *
    1.  Press the **Remove feature** button.
    2.  Do one of the following   *
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list at the top and press the **Del** key.
        -   Right-click a feature in the list at the top and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   To add transformations   *
    1.  If there are existing transformations   * select the transformation after which the new transformation should be added.
    2.  Right-click the **Transformations** list.
    3.  Select one the following options from the context menu   *
        -   
            **Add mirrored transformation**
            
            . See [PartDesign Mirrored](PartDesign_Mirrored.md).

        -   
            **Add linear pattern**
            
            . See [PartDesign LinearPattern](PartDesign_LinearPattern.md).

        -   
            **Add polar pattern**
            
            See [PartDesign PolarPattern](PartDesign_PolarPattern.md).

        -   
            **Add scaled transformation**
            
            . See [PartDesign Scaled](PartDesign_Scaled.md).
    4.  The selected transformation is added to the list and the settings for the transformation are displayed below the list.
    5.  Adjust the settings to suit.
    6.  Press the **OK** bar at the bottom.
    7.  Repeat to add more transformations.
-   To edit a transformation   *
    1.  Right-click the transformation in the **Transformations** list.
    2.  Select **Edit** from the context menu.
    3.  Adjust the settings to suit.
    4.  Press the **OK** bar at the bottom.
-   To change the order of the transformations   *
    1.  Right-click a transformation in the **Transformations** list.
    2.  Select **Move up** or **Move down** from the context menu.
-   If the **Update view** checkbox is checked the view will update in real time.

## Einschränkungen

Siehe [PartDesign PolaresMuster](PartDesign_PolarPattern/de#Einschränkungen.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/de
