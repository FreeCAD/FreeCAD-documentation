---
- GuiCommand:
   Name:Part SectionCut
   MenuLocation:View → Persistent section cut
   Workbenches:All
   Version:0.20
   SeeAlso:[[Std ToggleClipPlane]]
---

# Part SectionCut/pl

## Opis

Funkcja **Wycinek przekroju** jest dostępna dla wszystkich środowisk pracy, choć działa tylko dla obiektów Część i Projekt Części oraz ich złożeń. Tworzy ona trwałe przecięcie obiektów i złożeń. Ponieważ wynik cięcia jest normalnym obiektem [wycięcia](Part_Cut/pl.md) środowiska Część, może być dalej modyfikowany lub np. drukowany na drukarce 3D. Zobacz poniżej możliwe zastosowania.

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*A cut assembly. Some cut faces were manually colored. The yellow part is not cut because it was purposely moved by one micron into another part.*

## Usage

![The Section Cut dialog.](images/Part_SectionCut_Dialog.png )

The **Section Cut** dialog is opened via the menu **View → <img src="images/Part_SectionCut.svg" width=16px> Persistent section cut**. It is independent of the current workbench and the currently opened document. It can be detached from its opening position by pressing the button at the upper right of the dialog.

The **Section Cut** feature takes all currently visible Part objects in the active document into account. Therefore you can control what will be cut, by making a part visible or not. By checking one of the **Cutting** options in the dialog the feature is activated. You can then either enter a position (in coordinates of the document) or use the sliders to set the cut position. It is also possible to combine cuts, for example to cut in X and Z direction. The buttons **Flip** flip the side that is cut.

As soon as a **Cutting** option is checked in the dialog, you get a cut object in the [tree view](Tree_view.md). Its name is e.g. *SectionCutY* when it is a cut in Y direction.

The dialog option **Keep only cuts visible when closing** hides everything in the tree view except of the cut object when the button **Close** is clicked to close the dialog.

To remove the cut object, uncheck all **Cutting** options.

By unchecking all **Cutting** options, the button **Refresh view** becomes active. When pressed, it takes a kind of a screenshot of the currently visible Part objects. This will be used when you check the next time a **Cutting** option. The refreshing is necessary when you switched the document. It is furthermore useful for assemblies, where you might want to hide some parts or later want to add them to the cut. In this case the refreshing recalculates the min/max values of the sliders and cut positions according to the currently visible object dimensions.

If the option **Auto** in the color section is checked, the color of the cut objects will be taken. This only works if all cut objects have the same color or transparency.

**Note:** For assemblies the sliders in the dialog are disabled (except the one for the transparency). The reason is that a slider movement results in many cut operations is a short time. For assemblies this quickly consumes all CPU power and the sticky slider movement is then no longer helpful.

When you select a cut object in the tree view and then open the Section Cut dialog, the cut positions will be read into the dialog.

## Applications

-   An important use case is that Section Cut creates real cuts, not hollow ones like the **[Clip Plane](Std_ToggleClipPlane.md)** feature.
-   Section Cut is useful for assemblies to visualize for example the working principle of a device. You thereby might want to color certain cut faces using the **[Face Colors](Part_FaceColors.md)** tool. To use the tool, switch to the Part or PartDesign workbench, right-click on the cut object in the tree view and select in the context menu **Set colors**.
-   The limitation that only parts can be cut that don\'t intersect each other, see below, can be used as collision test.
-   The Section Cut feature can be used for technical drawings to highlight certain areas or to be able to draw in dimensions. The image below shows an example where the [TechDraw](TechDraw_Workbench.md) features [ActiveView](TechDraw_ActiveView.md) and [View](TechDraw_View.md) are used.

<img alt="" src=images/Part_SectionCut_TD-example.png  style="width:400px;"> 
*A technical drawing where a Section Cut result is used. (Click on the image for full size.)*

## Special cut positions 

<img alt="A slant cut of an assembly." src=images/Part_SectionCut_slant-cut.png  style="width:200px;">

-   For example in the first image in this page only one quarter of the assembly is cut. This was done by creating a cut in X direction. Then in the resulting cut object **SectionCutX** the [placement](placement.md) of the subobject **SectionCutBoxX** was changed.
-   To get a cut in any direction, you can do this:

1.  Create a new [Std Part](Std_Part.md) container.
2.  Select all objects you want to cut in the tree view and move them into the container.
3.  Now set the placement of the container to a rotation of your choice. For the image at the left, the container was rotated by 45° around the X and Z axis and the section cut was performed in X direction.




## Limitations

<img alt="An assembly where two parts intersect each other and that are therefore not cut. Note the color artifacts at the cut face." src=images/Part_SectionCut_Color-artifact.png  style="width:200px;">

-   **Important:** The Section Cut feature works poorly with [OpenCASCADE](OpenCASCADE.md) 7.4 and older due to bugs. It is therefore recommended to use OpenCASCADE 7.5 or newer (all builds of FreeCAD 0.20 assure this).
-   In assemblies parts that intersect each other cannot be cut. Normally intersecting objects will not be cut while the others will. However, sometimes the cutting can produce strange results which is a bug in the OpenCASCADE libraries. To get a cut view also for intersecting objects, you can use the the macro [Cross Section](Macro_cross_section.md).
-   There can be color artifacts in the cut result. If and how depends on the OpenCASCADE library and also on the view position. In many cases the color artifacts disappear when the 3D view is slightly rotated.
-   When having cut objects with different colors, it is not possible to apply automatically their color to the corresponding cut faces. All cut faces will get the same color selected in the dialog.




## Background Info 

**Section Cut** is inspired by the macro [Cross Section](Macro_cross_section.md) and works technically this way:

All visible objects are put into a [Part Compound](Part_Compound.md) container and then the compound is cut using a [Part Box](Part_Box.md) object. The box must be as large as necessary to cover the whole volume of all visible objects. To achieve this, the bounding box of the objects is acquired. When changing the view by adding/removing objects or changing the document, the bounding box must be updated. This is done when the button **Refresh view** is clicked.

To enable the cutting of intersecting objects, instead of the Part Compound container a [Boolean Fragements](Part_BooleanFragments.md) container is needed. This feature addition is planned for the next FreeCAD version.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/pl
