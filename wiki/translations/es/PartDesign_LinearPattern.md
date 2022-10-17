---
- GuiCommand   */es
   Name   *PartDesign LinearPattern
   Name/es   *DiseñoPieza PatrónLineal
   MenuLocation   *DiseñoPieza  →  Aplicar un patrón → PatrónLineal
   Workbenches   *[DiseñoPieza](PartDesign_Workbench/es.md)
---

# PartDesign LinearPattern/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta **[<img src=images/PartDesign_LinearPattern.svg style="width   *24px"> '''PatrónLineal'''** crea copias de una operación a una misma distancia en dirección lineal. A partir de la v0.17 la herramienta de patrón lineal puede repetir múltiples operaciones. {{VersionPlus/es|0.17}}


</div>

![](images/PartDesign_LinearPattern_example.svg )


<div class="mw-translate-fuzzy">

*Arriba   * Una forma extruida con forma de L (B) construida encima de una base extruida (A, también referida como*soporte*) es usada para crear un patrón lineal. El resultado (C) se muestra a la derecha.*


</div>

## Uso

### Create

1.  Optionally [activate](PartDesign_Body#Active_status.md) the correct Body.
2.  Optionally select one or more features in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
3.  There are several ways to invoke the tool   *
    -   Press the **<img src="images/PartDesign_LinearPattern.svg" width=16px> [LinearPattern](PartDesign_LinearPattern.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_LinearPattern.svg" width=16px> LinearPattern** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  If no features were selected the **Select feature** [task panel](Task_panel.md) opens   * select one or more (hold down the **Ctrl** key) from the list and press the **OK** button.
6.  The **LinearPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Edit

1.  Do one of the following   *
    -   Double-click the LinearPattern object in the [Tree view](Tree_view.md).
    -   Right-click the LinearPattern object in the [Tree view](Tree_view.md) and select **Edit LinearPattern** from the context menu.
2.  The **LinearPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.


<div class="mw-translate-fuzzy">

## Opciones


</div>

-   To add features   *
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features   *
    1.  Press the **Remove feature** button.
    2.  Do one of the following   *
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list and press the **Del** key.
        -   Right-click a feature in the list and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   Specify the **Direction** of the pattern   *
    -   
        **Normal sketch axis**
        
           * The Z axis of the sketch (only available for sketch-based features).

    -   
        **Vertical sketch axis**
        
           * The Y axis of the sketch (idem).

    -   
        **Horizontal sketch axis**
        
           * The X axis of the sketch (idem).

    -   
        **Construction line #**
        
           * A separate entry for each construction line in the sketch (idem).

    -   
        **Base X axis**
        
           * The X axis of the Body.

    -   
        **Base Y axis**
        
           * The Y axis of the Body.

    -   
        **Base Z axis**
        
           * The Z axis of the Body.

    -   
        **Select reference...**
        
           * Select a [Datum Line](PartDesign_Line.md) in the [Tree view](Tree_view.md) or a [Datum Line](PartDesign_Line.md) or edge in the [3D view](3D_view.md).
-   Check the **Reverse direction** checkbox to reverse the pattern.
-   Specify the **Length** to be covered by the pattern.
-   Specify the number of **Occurrences** (including the original feature).
-   If the **Update view** checkbox is checked the view will update in real time.

## Limitations

See [PartDesign PolarPattern](PartDesign_PolarPattern#Limitations.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/es
