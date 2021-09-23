# PartDesign Pocket/ro
---
- GuiCommand:   Name:PartDesign Pocket   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → Pocket---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul **Pocket** așchiază un solid prin extrudarea unei schițe în traiectorie dreaptă și extrăgând-o din solid.


</div>

![](images/PartDesign_Pocket_example.svg ) \'\'Sketch profile (A) was mapped to the top face of base solid (B); result after pocketing through on the right. \'\'


<div class="mw-translate-fuzzy">

## Cum se foloseșste 

1.  Select the sketch to be pocketed.

    :   v0.16 and below The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear.
2.  Press the **<img src="images/PartDesign_Pocket.png" width=16px> '''Pocket'''** button.
3.  Set the Pocket parameters (see next section).
4.  Click OK.


</div>

## Opțiuni

![](images/Pocket_options.png )


<div class="mw-translate-fuzzy">

Atunci când se creează un pocket, dialogul **Pocket parameters** oferă cinci căi diferite de specificare a lungimii(adâncimii) la care buzunarul va fi extrudat:

### Dimension

Enter a numeric value for the depth of the pocket. The default direction for extrusion is into the support. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.

### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

### Through all 

The pocket will cut through all material in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.

### Up to face 

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions 

v0.17 and above This allows to enter a second length in which the pad should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option.


</div>

### Up to face 

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option. <small>(v0.17)</small> 

## Limitări

-   Use the type **Dimension** or **Through All** wherever possible because the other types sometimes give trouble when they are being patterned
-   Otherwise, the pocket feature has the same [limitations](PartDesign_Pad#Limitations.md) as the pad feature.

## Link uri utile 

Un exemplu [example](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) are partea practică pe forum.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/ro
