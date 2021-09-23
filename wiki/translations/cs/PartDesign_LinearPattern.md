# PartDesign LinearPattern/cs
---
- GuiCommand:/cs   Name:PartDesign_LinearPattern   Name/cs:PartDesign LinearPattern   Workbenches:[[PartDesign Workbench/cs   Návrh dílu]], Complete|MenuLocation:PartDesign -> LinearPattern---


</div>


<div class="mw-translate-fuzzy">

## Úvod

\'Vytvořte lineární vzorek nějakého prvku\' - Tento nástroj vezme sadu jednoho nebo více vybraných prvků jako vstup (\'originály\') a vytvoří z nich druhou sadu prvků přenesených v daném směru. Například: <img alt="" src=images/linearpattern_example.png  style="width:600px;"> 

## Volby

+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
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
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





</div>

The **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''LinearPattern'''** tool creates evenly spaced copies of a feature in a linear direction. As of <small>(v0.17)</small>  the Linear pattern tool can pattern multiple features.

![](images/PartDesign_LinearPattern_example.svg )

\'\'Above: An L-shaped pad (B) made on top of a base pad (A, also referred to as *support*) is used for a linear pattern. The result (C) is shown on the right.\'\'

## Usage

To create a pattern:

1.  Select the feature (<small>(v0.19)</small>  or several features) to be patterned.
2.  Press the **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''LinearPattern'''** button.
3.  Define the **Direction**. See [Options](#Options.md).
4.  Define the **Length** (distance) between the last copied occurrence and the original feature.
5.  Set the number of **Occurrences**.
6.  If you have several features in the pattern, their order can be important, see for example the image in the [PolarPattern feature](PartDesign_PolarPattern#Usage.md). <small>(v0.19)</small>  You can change the order by dragging the feature in the list and you will see the result immediately as preview.
7.  Press **OK**.

To add or remove features from an existing pattern:

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **Space** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select **Remove**

## Options

![LinearPattern parameters in v0.16 and below.](images/Linearpattern_parameters.png ) ![LinearPattern parameters in v0.17 and above.](images/Linearpattern_parameters_v017.png )

### Direction

When creating a linear pattern feature, the **LinearPattern parameters** dialogue offers different ways of specifying the pattern direction.

#### Horizontal sketch axis 

Uses the horizontal axis of the sketch for direction.

#### Vertical sketch axis 

Uses the vertical axis of the sketch for direction.

#### Normal sketch axis 


<small>(v0.17)</small> 

Uses the normal axis of the sketch for direction.

#### Select reference\... 

Allows you to select either a DatumLine or an edge of an object or a line of a sketch to use for direction.

#### Custom Sketch Axis 

If the sketch which defines the feature to be patterned also contains a construction line (or lines), then the drop down list will contain one custom sketch axis for each construction line. The first construction line will be labelled *Sketch axis 0*.

#### Base (X/Y/Z) axis 


<small>(v0.17)</small> 

Select one of the Body Origin\'s standard axis (X, Y or Z) as direction. 


<div class="mw-translate-fuzzy">

## Omezení

-   Tvary vzorků se nesmějí vzájemně překrývat, kromě speciálního případu, kdy se jedná pouze o dva výskyty (originál plus jedna kopie)
-   Jakýkoliv tvar vzorku, který nepokrývá původní podklad (přečnívá) bude vyloučen. To zajistí, že díl v Návrhu dílu vždy obsahuje jedno spojené těleso
-   Na další omezení se podívejte na [zrcadlené prvky](PartDesign_Mirrored/cs.md)





</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/cs
