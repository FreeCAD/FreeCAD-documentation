# PartDesign LinearPattern/cs
---
- GuiCommand:/cs   Name:PartDesign_LinearPattern   Name/cs:PartDesign LinearPattern   Workbenches:[[PartDesign Workbench/cs   Návrh dílu]], Complete|MenuLocation:PartDesign -> LinearPattern---


</div>


<div class="mw-translate-fuzzy">

## Úvod

\'Vytvořte lineární vzorek nějakého prvku\' - Tento nástroj vezme sadu jednoho nebo více vybraných prvků jako vstup (\'originály\') a vytvoří z nich druhou sadu prvků přenesených v daném směru. Například: <img alt="" src=images/linearpattern_example.png  style="width:600px;"> 

## Volby

+++
| ![](images/linearpattern_parameters.png ) | Při vytváření lineárního vzorku prvku nabízí dialogové okno \'parametry lineárního vzorku\' dva různé způsoby specifikování směru vzorku.                                                                                                                   |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | ### Standardní osy                                                                                                                                                                                                                         |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | Jedna ze standardních os **X**, **Y** nebo **Z** múže být vybrána radio tlačítkem. Směr vzorku může být obrácen zakliknutím \'Opačný směr\'.                                                                                                                |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | ### Vyběr plochy                                                                                                                                                                                                                             |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | Stisk tlačítka označeného \'Směr\' umožňuje vybrat plochu nebo hranu z existujícího tělesa k určení směru. Je-li vybrána plocha, bude směr vzorku kolmý k této ploše. Připomínám, že tlačítko musí být stisknuto pokaždé při výběru nové plochy nebo hrany. |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | ### Výběr originálů                                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | Okénko seznamu ukazuje \'originály\', prvky, které jsou vybrány ke vzorkování. Kliknutí na libovolný prvek jej přidá do seznamu.                                                                                                                            |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | ### Délka a Výskyty                                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                                                                                                                                             |
|                                                                  | Určuje délku, která má být pokryta vzorkem a celkový počet výskytů vzorků (včetně originálního prvku). Například šest výskytů v délce 150 dá šířku mezer mezi vzorky na 30 (150 děleno 5, protože mezer je 5 mezi celkovým počtem výskytů 6!).              |
+++





</div>

The <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **PartDesign LinearPattern** tool creates a linear pattern of one or more features.

![](images/PartDesign_LinearPattern_example.svg ) 
*An L-shaped pad (B) made on top of a base pad (A, also referred to as support) is used for a linear pattern. The result (C) is shown on the right.*

## Usage

### Create

1.  Optionally [activate](PartDesign_Body#Active_status.md) the correct Body.
2.  Optionally select one or more features in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_LinearPattern.svg" width=16px> [LinearPattern](PartDesign_LinearPattern.md)** button.
    -   Select the **Part Design → Apply a pattern → <img src="images/PartDesign_LinearPattern.svg" width=16px> LinearPattern** option from the menu.
4.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
5.  If no features were selected the **Select feature** [task panel](Task_panel.md) opens: select one or more (hold down the **Ctrl** key) from the list and press the **OK** button.
6.  The **LinearPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Edit

1.  Do one of the following:
    -   Double-click the LinearPattern object in the [Tree view](Tree_view.md).
    -   Right-click the LinearPattern object in the [Tree view](Tree_view.md) and select **Edit LinearPattern** from the context menu.
2.  The **LinearPattern parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add features:
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features:
    1.  Press the **Remove feature** button.
    2.  Do one of the following:
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list and press the **Del** key.
        -   Right-click a feature in the list and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [PartDesign PolarPattern](PartDesign_PolarPattern#Ordering_features.md).
-   Specify the **Direction** of the pattern:
    -   
        **Normal sketch axis**
        
        : The Z axis of the sketch (only available for sketch-based features).

    -   
        **Vertical sketch axis**
        
        : The Y axis of the sketch (idem).

    -   
        **Horizontal sketch axis**
        
        : The X axis of the sketch (idem).

    -   
        **Construction line #**
        
        : A separate entry for each construction line in the sketch (idem).

    -   
        **Base X axis**
        
        : The X axis of the Body.

    -   
        **Base Y axis**
        
        : The Y axis of the Body.

    -   
        **Base Z axis**
        
        : The Z axis of the Body.

    -   
        **Select reference...**
        
        : Select a [Datum Line](PartDesign_Line.md) in the [Tree view](Tree_view.md) or a [Datum Line](PartDesign_Line.md) or edge in the [3D view](3D_view.md).
-   Check the **Reverse direction** checkbox to reverse the pattern.
-   Specify the **Length** to be covered by the pattern.
-   Specify the number of **Occurrences** (including the original feature).
-   If the **Update view** checkbox is checked the view will update in real time.

## Limitations

See [PartDesign PolarPattern](PartDesign_PolarPattern#Limitations.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/cs
