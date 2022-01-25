---
- GuiCommand:/ro
   Name:PartDesign Pad
   Name/ro:PartDesign Pad
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Pad
---

# PartDesign Pad/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **Pad** extrude o schiță într-un solid în direcția normală la planul schiței. Începând cu versiunea v0.17, fațete pe solid pot de de asemenea utilizate.


</div>

![](images/PartDesign_Pad_example.svg )

*Sketch (A) shown on the left; end result after pad operation (B) on the right.*

## Cum se utilizează 


<div class="mw-translate-fuzzy">

1.  Select the sketch to be padded. In v0.17 and above, a face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_Pad.png" width=24px> '''Pad'''** button.
3.  Set the Pad parameters (see next section).
4.  Click **OK**.


</div>

## Opțiuni


<div class="mw-translate-fuzzy">

Când se creează o protuberanță(Pad), vizualizarea Combo se comută automat în panoul Activități, afișând dialogul \'\'\' Parametri pad \'\'\'.


</div>

![](images/pad_parameters_cropped.png )

### Type


<div class="mw-translate-fuzzy">

Tipul oferă cinci modalități diferite de a specifica lungimea la care va fi extrudat tamponul.


</div>

#### Dimension


<div class="mw-translate-fuzzy">

Enter a numeric value for the length of the pad. The default direction for extrusion is away (outside of) the support, but it can be changed by ticking the **Reversed** option. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. With the option **Symmetric to plane** the pad will extend half of the given length to either side of the sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.


</div>

#### Two dimensions 

This allows to enter a second length in which the pad should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

#### To last 

The pad will extrude up to the last face of the support in the extrusion direction. If there is no support, an error message will appear.

#### To first 

The pad will extrude up to the first face of the support in the extrusion direction. If there is no support, an error message will appear.

#### Up to face 

The pad will extrude up to a face in the model that can be chosen by clicking on it.

### Length


<div class="mw-translate-fuzzy">

Definește lungimea protuberanței. Unitățile multiple pot fi utilizate independent de preferințele unităților utilizatorului(m, cm, mm, nm, ft or \', in or \").


</div>

### Offset to face 

Offset from face at which the pad will end. This option is only available when **Type** is either **To last**, **To first** or **Up to face**.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion. <small>(v0.20)</small> 
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values. <small>(v0.19)</small> 

#### Show direction 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed. <small>(v0.20)</small> 

#### Length along sketch normal 

If checked, the pad length is measured along the sketch normal, otherwise along the custom direction. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

### Symmetric to plane 


</div>


<div class="mw-translate-fuzzy">

Bifați caseta de selectare pentru a extinde jumătate din lungimea dată la fiecare parte a planului de schiță.


</div>

### Reversed

Reverses the direction of the pad.

## Proprietăți


<div class="mw-translate-fuzzy">

-    {{PropertyData/ro|Refine}}: <small>(v0.17)</small>  true or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in *Preferences → Part design → General → Model settings*). It can be manually changed afterwards. This property will be saved with the FreeCAD document.


</div>

## Limitări

-   Like all Part Design features, Pad creates a solid, thus the sketch must include a closed profile or it will fail with a *Failed to validate broken face* error. There can be multiple enclosed profiles inside a larger one, provided none intersect each other (for example, a rectangle with two circles inside it).
-   The algorithm used for **To First** and **To Last** is:
    -   Create a line through the center of gravity of the sketch
    -   Find all faces of the support cut by this line
    -   Choose the face where the intersection point is nearest/furthest from the sketch

:   This means that the face that is found might not always be what you expected. If you run into this problem, use the **Up to face** type instead, and pick the face you want.
:   For the very special case of extrusion to a concave surface, where the sketch is larger than this surface, extrusion will fail. This is a unresolved bug.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/ro
