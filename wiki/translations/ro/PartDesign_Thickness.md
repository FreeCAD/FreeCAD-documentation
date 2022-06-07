# PartDesign Thickness/ro
---
- GuiCommand   *   Name   *PartDesign Thickness   Workbenches   *[MenuLocation   *Part Design → Thickness   Shortcut   *None   SeeAlso   *[[Part_Thickness|Part Thickness](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **Thickness** lucrează pe un corp solid și îl transformă într-un obiect gol cu pereți groși cu cel puțin o față deschisă, dând fiecărei fațete rămase o grosime uniformă. La unele solide, acest lucru vă permite să accelerați considerabil lucrarea și să evitați extrudările și buzunarele.


</div>

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;"> 
*Base solid (A) →  Solid with selected face to be opened (B) →  Resulting hollow object (C)*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

### Add a thickness 


<div class="mw-translate-fuzzy">

1.  Selectași una sau mai multe fațete pe corpul (Body) activ.
2.  Apăsați butonul **<img src="images/PartDesign_Thickness.png" width=24px> '''Thickness'''** .
3.  Definiți **Thickness parameters** (see [Options](#Options.md)).
4.  Pentru a adăuga mai multe fațete pentru a deschide, apăsați butonul **Add face** și selectați o fațetă în vizualizarea 3D.
5.  Pentru a șterge fațete selectată anterior, apăsați butonul **Remove face** și selctați fațeta în vizualizarea 3D view, sau clic dreapta pe eticheta Face în listă și selectați *Remove*.
6.  Apăsați **OK**.


</div>


   *   *Remember*   *
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Edit a thickness 

1.  Do one of the following   *
    -   Double-click the Thickness object in the [Tree view](Tree_view.md)
    -   Right-click the Thickness object in the [Tree view](Tree_view.md) and select **Edit Thickness** from the context menu.
2.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Opţiuni


<div class="mw-translate-fuzzy">

-   **Thickness**   * Grosimea peretelui obiectului rezultat. Definiți valoarea dorită.
-   **Mode**
    -   *Skin*   * Selectați această opțiune dacă doriți pentru a obține un articol ca o vază, fără capac, dar cu fund
    -   *Pipe*   * Selectați această opțiune dacă doriți să obțineți un obiect ca o țeavă, fără cap și fără fund. În acest caz, poate fi convenabil să selectați fațele care trebuie șterse înainte de a porni instrumentul. Ajutați-vă cu vizualizări predefinite sau utilizați tastele numerice.
    -   *Recto Verso*   *
-   **Join Type**
    -   *Arc*   * îndepărtează marginile exterioare și creează o curbă cu o rază egală cu grosimea definită.
    -   *Intersection*   *când fațele sunt decalate spre exterior, marginile ascuțite sunt păstrate între faațete.
-   **Make thickness inwards**   * când sunt bifate, fațetșe sunt deplasate spre interior.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Cel puțin o fațetă care va fi deschisă trebuie selectată.
-   Valoarea grosimii nu trebuie să depășească înălțimea celei mai mici fațete a Body.
-   Comanda poate eșua cu formele complexe.


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
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/ro
