---
- GuiCommand   */de
   Name   *PartDesign Thickness
   Name/de   *PartDesign Dicke
   MenuLocation   *Part Design → Modifikationen → Dicke
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   Version   *0.17
   SeeAlso   *[Part Dicke](Part_Thickness/de.md)
---

# PartDesign Thickness/de

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug *Dicke* bearbeitet einen Festkörper und wandelt ihn in einen dickwandigen hohlen Gegenstand mit mindestens einer offenen Fläche um, der jeder seiner verbleibenden Flächen eine gleichmäßige Dicke verleiht. Bei einigen Volumenkörpern kann es die Bearbeitung erheblich beschleunigen und vermeidet die Erstellung von Extrusionen und Taschen.


</div>

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;">


<div class="mw-translate-fuzzy">



*Das Werkzeug Dicke angewendet auf die Fläche (B) eines Volumenkörpers (A) ergibt das hohle Objekt (C).*


</div>

## Anwendung

### Add a thickness 


<div class="mw-translate-fuzzy">

1.  Eine oder mehrere Flächen des aktiven Körpers auswählen.

2.  Die Schaltfläche **<img src="images/PartDesign_Thickness.png" width=24px> ''Dicke''** drücken.

3.  Die **Dicke- (Thickness) Parameter** festlegen (siehe [Optionen](#Optionen.md)).

4.  Um weitere Flächen zum Öffnen hinzuzufügen, drückt man die Schaltfläche **Fläche hinzufügen** und wählt eine oder mehrere Flächen in der 3D-Ansicht aus.

5.  Um eine zuvor ausgewählte Fläche zu entfernen, drückt man ** Fläche entfernen** und wählt eine Fläche in der 3D-Ansicht, oder klickt mit der rechten Maustaste auf die Fläche in der Liste und wählt *Entfernen*.

6.  
    **OK**drücken.


</div>


   *   *Remember*   *
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Edit a thickness 

1.  Do one of the following   *
    -   Double-click the Thickness object in the [Tree view](Tree_view.md)
    -   Right-click the Thickness object in the [Tree view](Tree_view.md) and select **Edit Thickness** from the context menu.
2.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Optionen


<div class="mw-translate-fuzzy">

-   **Dicke**   * Wanddicke des resultierenden Objekts. Stellen Sie den gewünschten Wert ein.
-   **Modus**
    -   *Skin*   * Wählen Sie diese Option, wenn Sie ein Objekt wie eine Vase, kopflos, aber mit dem Boden bekommen wollen
    -   *Rohr*   * Wählen Sie diese Option, wenn Sie ein Objekt wie ein Rohr bekommen möchten, ohne Boden und Deckel. In diesem Fall kann es nützlich sein, die zu löschenden Flächen auszuwählen, bevor Sie das Werkzeug starten. Nutzen Sie dazu die vordefinierten Ansichten Schaltflächen oder verwenden Sie die numerischen Tasten.
    -   *Recto Verso*   *

-   **Verbindungstyp**
    -   *KreisBogen(Arc)*   * entfernt die äußeren Kanten und erstellt eine Leiste mit einem Radius, der der definierten Stärke entspricht.
    -   *Schnitt(Intersection)*   * Wenn Flächen nach außen versetzt sind, werden scharfe Kanten zwischen den Flächen beibehalten.
-   **Erzeugen einer Hülle mit innen liegendem Volumen**   * Wenn diese Option aktiviert ist, werden die Flächen nach innen versetzt.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Es muss mindestens eine zu öffnende Fläche ausgewählt sein.
-   Wenn die Dicke nach innen geht, muss der Wert für die Dicke kleiner sein als die kleinste Höhe des Körpers.
-   Der Befehl kann bei komplexen Formen fehlschlagen. In diesem Zusammenhang muss auch eine Fläche wie die eines Kegels bereits als komplex angesehen werden.
    -   [PartDesign Additives Rohr](PartDesign_AdditivePipe/de.md) oder [PartDesign Additive Loft](PartDesign_AdditiveLoft/de.md) kann zur Erzeugung von komplexeren Formen geeigneter sein.


</div>

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Thickness object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**   * \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Default   * `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * \"Refine shape (clean up redundant edges) after adding/subtracting\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Thickness}}

-    **Value|Length**   * \"Thickness value\". Default   * {{value|1 mm}}.

-    **Mode|Enumeration**   * \"Mode\". {{value|Skin}} (default), {{value|Pipe}} or {{Value|Recto verso}}. Only {{value|Skin}} is implemented.

-    **Join|Enumeration**   * \"Join type\". {{value|Arc}} (default) or {{Value|Intersection}}.

-    **Reversed|Bool**   * \"Apply the thickness towards the solids interior\". Default   * `False`.

-    **Intersection|Bool**   * \"Enable intersection-handling\". Default   * `False`.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/de
