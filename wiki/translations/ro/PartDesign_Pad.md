---
 GuiCommand:
   Name: PartDesign Pad
   Name/ro: PartDesign Pad
   Workbenches: PartDesign Workbench/ro
   MenuLocation: Part Design , Pad
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

Când se creează o protuberanță(Pad), vizualizarea Combo se comută automat în panoul Activități, afișând dialogul **Parametri pad**.


</div>


<div class="mw-translate-fuzzy">

![](images/pad_parameters_cropped.png )


</div>

### Type


<div class="mw-translate-fuzzy">

Tipul oferă cinci modalități diferite de a specifica lungimea la care va fi extrudat tamponul.


</div>

#### Dimension


<div class="mw-translate-fuzzy">

Enter a numeric value for the length of the pad. The default direction for extrusion is away (outside of) the support, but it can be changed by ticking the **Reversed** option. Extrusions occur [normal](http://en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. With the option **Symmetric to plane** the pad will extend half of the given length to either side of the sketch plane. Negative dimensions are not possible. Use the **Reversed** option instead.


</div>

#### To last 

The pad will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.

#### To first 

The pad will extend up to the first face of the support it encounters in its direction. If there is no support, an error message will appear.

#### Up to face 

The pad will extend up to a face. Press the **Select face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second length in which the pad should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

#### Up to shape 


<small>(v1.0)</small> 

: The pad will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select faces** button and select the faces up to which the pad should be created.

### Offset to face 

Offset from face at which the pad will end. This option is only available if **Type** is **To last**, **To first** or **Up to face**.

### Length


<div class="mw-translate-fuzzy">

Definește lungimea protuberanței. Unitățile multiple pot fi utilizate independent de preferințele unităților utilizatorului(m, cm, mm, nm, ft or \', in or \").


</div>

### 2nd length 

Defines the length of the pad in the opposite direction. This option is only available if **Type** is **Two dimensions**.




<div class="mw-translate-fuzzy">

### Symmetric to plane 


</div>


<div class="mw-translate-fuzzy">

Bifați caseta de selectare pentru a extinde jumătate din lungimea dată la fiecare parte a planului de schiță.


</div>

### Reversed

Reverses the direction of the pad.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.

#### Show direction 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pad length is measured along the sketch or face normal, otherwise along the custom direction.

### Taper angle 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.

### 2nd taper angle 

Tapers the pad in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.



## Proprietăți

### Data


{{TitleProperty|Pad}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/ro|Refine}}: <small>(v0.17)</small>  true or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in *Preferences → Part design → General → Model settings*). It can be manually changed afterwards. This property will be saved with the FreeCAD document.


</div>


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



## Limitări

-   Like all Part Design features, Pad creates a solid, thus the sketch must include a closed profile or it will fail with a *Failed to validate broken face* error.
-   Sketches containing [B-Splines](B-Splines.md) often cannot be tapered properly. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face would have fewer edges than the start face/sketch.
-   The algorithm used for **To First** and **To Last** is:
    -   Create a line through the center of gravity of the sketch
    -   Find all faces of the support cut by this line
    -   Choose the face where the intersection point is nearest/furthest from the sketch

:   This means that the face that is found might not always be what you expected. If you run into this problem, use the **Up to face** type instead, and pick the face you want.
:   For the very special case of extrusion to a concave surface, where the sketch is larger than this surface, extrusion will fail. This is an unresolved bug.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/ro
