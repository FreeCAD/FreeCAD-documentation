# PartDesign Mirrored/ro
---
- GuiCommand:   Name:PartDesign Mirrored   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → Mirrored---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **Mirrored** simetrizează o funcție în plan. Începând cu v0.17, instrumentul poate simetriza multiple funcții(onalități) .


</div>

![](images/PartDesign_Mirrored_example.svg )


<div class="mw-translate-fuzzy">

\"Deasupra: o funcție Pocket a fost creată dintr-o schiță care conține un cerc (A), Pocket-ul a fost ulterior folosit pentru a crea o caracteristică Mirror. Axa verticală a schiței (B) a fost utilizată ca axă de simetrie. Rezultatul (C) este afișat în partea dreaptă. „"


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Select the feature(s) to be mirrored. Alternatively, the feature can be selected from a dialogue after step 2.

    :   v0.16 and below Only a single feature can be selected, and it must be the last one at the bottom of the feature tree.
2.  Press the **<img src=images/PartDesign_Mirrored.png style="width:24px"> '''Mirrored'''** button.
3.  v0.17 and above Press **Add feature** to add a feature to be mirrored. The feature must be visible in the 3D view:
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **spacebar** to make it visible in the 3D view;
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
4.  v0.17 and above Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select *Remove*.
5.  Define the mirror plane. See [Options](#Options.md).
6.  Press **OK**.


</div>

To add or remove features from an existing mirroring:

1.  Press **Add feature** to add a feature to be mirrored. The feature must be visible in the [3D view](3D_view.md):
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **spacebar** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select *Remove*.

## Opţiuni


<div class="mw-translate-fuzzy">

![Mirrored parameters in v0.16 and below.](images/mirrored_parameters.png ) ![Mirrored parameters in v0.17 and above.](images/Mirrored_parameters_v017.png )


</div>

### Plane


<div class="mw-translate-fuzzy">

When creating a mirrored feature, the **Mirrored parameters** dialogue offers different ways of specifying the mirror line or plane .


</div>

#### Horizontal sketch axis 

Uses the horizontal axis of the sketch as the axis of symmetry.

#### Vertical sketch axis 

Uses the vertical axis of the sketch as the axis of symmetry.

#### Select reference\... 

Allows you to select a plane (such as a face of an object) to use as a mirror plane .

#### Custom Sketch Axis 

If the sketch which defines the feature to be mirrored also contains a construction line (or lines), then the drop down list will contain one custom sketch axis for each construction line. The first construction line will be labelled \'Sketch axis 0\'. The image below is an example with the sketch in edit mode showing that it includes a construction line for use as the Mirrored axis.

![](images/PartDesign_Mirrored_axis_fromconstructionlines.jpg )

#### Base (XY/XZ/YZ) plane 


<div class="mw-translate-fuzzy">

v0.17 and above Select one of the Body Origin\'s standard planes (XY, XZ or YZ) .


</div>

### Preview


<div class="mw-translate-fuzzy">

The mirror result can be previewed in real time before clicking OK by checking \"Update view\" .


</div>




## Limite


<div class="mw-translate-fuzzy">

-   Caracteristica Mirror nu poate să oglindi un întreg corp solid. Pentru asta, a se vedea [Part Mirror](Part_Mirror.md) .


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/ro
