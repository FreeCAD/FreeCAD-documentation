---
- GuiCommand   */de
   Name   *PartDesign Chamfer
   Name/de   *PartDesign Fase
   MenuLocation   *Part Design → Apply a dress up feature (Verschönerung) → Fase
   Workbenches   *[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   SeeAlso   *[Verrundung](PartDesign_Fillet/de.md), [Part Fase](Part_Chamfer/de.md)
---

# PartDesign Chamfer/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug erzeugt Fasen an den ausgewählten Kanten eines Objekts. Im Projektbaum wird ein neuer separater Faseneintrag (gefolgt von einer fortlaufenden Nummer, wenn bereits Fasen im Dokument vorhanden sind) angelegt.


</div>

## Anwendung

### Add a chamfer 


<div class="mw-translate-fuzzy">

-   Wähle eine einzelne Kante, mehrere Kanten oder eine Fläche auf einem Objekt und starte dann das Werkzeug entweder durch Klicken auf die Schaltfläche **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Fase'''** oder über das Menü **PartDesign → Fase**. Im Fall das du eine Fläche ausgewählt hast, werden alle ihre Kanten zum Anfasen berücksichtigt.
-   Im erscheinenden [Aufgabenpaneel](Task_panel/de.md) kannst du die Fase auf 3 Arten definieren   *
    -   **Gleicher Abstand**   * Die Fasenkanten sind gleich weit von der Körperkante entfernt.
    -   **Zwei Abstände**   * Die Abstände der Fasenkante zur Körperkante werden angegeben. Die Abstandsrichtung kann umgedreht werden. <small>(v0.19)</small> 
    -   **Abstand und Winkel**   * Es wird ein Abstand von der Fasenkante zur Körperkante angegeben. Die zweite Fasenkante wird durch den Winkel der Fase definiert. Die Abstandsrichtung kann umgedreht werden. <small>(v0.19)</small> 
-   Wenn du weitere Kanten oder Flächen hinzufügen möchtest, klicke auf die **Hinzufügen** Schaltfläche und wähle Kanten und/oder Flächen aus.
-   Wenn du Kanten oder Flächen entfernen möchtest
    -   wähle entweder die Kante/Fläche in der Liste des Dialogs und drücke die **DEL** Taste. *Hinweis*   * Da es mindestens eine Kante für das Formelement geben muss, kann die letzte verbleibende Kante oder Fläche in der Liste nicht entfernt werden.
    -   oder klicke auf die **Entfernen** Schaltfläche. Alle Kanten und Flächen, die zuvor ausgewählt wurden, werden violett hervorgehoben. Wähle die zu entfernende Kante oder Fläche aus.
-   Klicke auf **OK**, um zu bestätigen.
-   Bei einer Kette von Kanten, die tangential zueinander verlaufen, kann eine einzelne Kante gewählt werden; die Fase breitet sich entlang der Kette aus.
-   Um die Fase nach der Validierung der Funktion zu bearbeiten, doppelklicke entweder auf die Fasenbeschriftung im Projektbaum oder klicke mit der rechten Maustaste darauf und wähle **Fase bearbeiten**.


</div>

### Edit a chamfer 

1.  Do one of the following   *
    -   Double-click the Chamfer object in the [Tree view](Tree_view.md)
    -   Right-click the Chamfer object in the [Tree view](Tree_view.md) and select **Edit Chamfer** from the context menu.
2.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following   *
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following   *
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following   *
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Specify a chamfer **Type**   *
    -   
        **Equal distance**
        
           * One distance is used to place both chamfer edges.

    -   
        **Two distances**
        
           * Two distances are used to place the chamfer edges. <small>(v0.19)</small> 

    -   
        **Distance and angle**
        
           * A distance is used to place one chamfer edge, the placement of the other chamfer edge is defined by the angle of the chamfer. <small>(v0.19)</small> 
-   Press the **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Flip direction** button to flip the direction of the chamfer (deactivated for **Equal distance**). <small>(v0.19)</small> 
-   Set the **Size** of the chamfer.
-   Set the **Size2** of the chamfer (only available if **Two distances** is selected).
-   Set the **Angle** of the chamfer (only available if **Distance and angle** is selected).
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes


<div class="mw-translate-fuzzy">

## PartDesign Fase vs. Part Fase 

**Die PartDesign Fase ist nicht zu verwechseln mit ihrem [Part Arbeitsbereich Gegenstück](Part_Chamfer/de.md)**. Obwohl sie das gleiche Symbol haben, sind sie nicht identisch und werden nicht auf die gleiche Weise verwendet. Der Hauptunterschied besteht darin, dass PartDesign Fase einen separaten Faseneintrag (gefolgt von einer fortlaufenden Nummer, falls bereits Fasen vorhanden sind) im Projektbaum für den aktuellen Körper erstellt. Die Part Fase wird zum Elternobjekt des Objekts, auf das sie angewendet wurde.


</div>

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Chamfer object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**   * If `True` the chamfered shape of the additive/subtractive parent feature will be used when the chamfer object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the chamfer itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Chamfer}}

-    **Camfer Type|Enumeration**   * The chamfer type   * {{value|Equal distance}} (default), {{value|Two distances}} or {{value|Distance and Angle}}.

-    **Size|QuantityConstraint**   * The first chamfer distance. The default is {{value|1 mm}}.

-    **Size2|QuantityConstraint**   * The second chamfer distance. Only used if **Camfer Type** is {{Value|Two distances}}. The default is {{value|1 mm}}.

-    **Angle|Angle**   * The chamfer angle. Only used if **Camfer Type** is {{Value|Distance and Angle}}. The default is {{value|45 °}}.

-    **Flip Direction|Bool**   * If `True` the direction of the chamfer is flipped. Not used if **Camfer Type** is {{Value|Equal distance}}. The default is `False`.

-    **Use All Edges|Bool**   * If `True` all edges of the feature are chamfered, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Known issues 

See [PartDesign Fillet](PartDesign_Fillet#Known_issues.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/de
