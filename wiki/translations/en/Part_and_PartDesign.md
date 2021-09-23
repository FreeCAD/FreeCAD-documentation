# Part and PartDesign/en
 {{TOCright}}

## Overview

There has been much discussion over the years about the differences and ramifications of using the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) and the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md) workbenches.

It is a good idea to use one or the other until the user is comfortable with one, then learn the other. It is also typically recommended that new users not mix them until the ramifications of doing so are understood.

Let\'s talk about those ramifications.

## Part Workbench Concepts 

Part Workbench is essentially [CSG style modeling](Constructive_solid_geometry.md). The operator combines various primitives to end up with a representation of the desired shape. (In fact, Part Workbench goes one step further than just primitives and allows the operator to use a sketch+extrude operation (or sketch+revolve, loft, sweep \...) to create random shapes as well.) When each primitive or shape is created, it has no relationship to other objects created (except sketches and their attachments), it is a single solitary solid.

![centre\|Solitary solids](images/Part_CSG_Prims.png )

This condition remains so, until, the operator uses some operation to combine them (typically a Boolean that adds or subtracts them). Each starting solid remains accessible separately and the operation creates a new object.

The take away is the single solitary solid bit and the combining them bit.

## PartDesign Workbench Concepts 

In the PartDesign Workbench the Body object is constructed directly as a single solitary cumulative solid.

The 1st step in a body must be a block of material, either from an additive primitive or an extrusion from a sketch, or an imported shape (then called Base Feature).

This initial block of material will be changed sequentially until the desired final shape (solid) is obtained.

It is cumulative in the sense that each operation adds or removes material.

By default, the \"tip\" of the body - unless there is a voluntary change in the visualization of a particular feature - is the last operation performed on the body. This is the current and visible state of the body, ready to be changed again by new feature.

Any function under the body represents the cumulative shape of the solid from the 1st feature to the feature considered.

So **to have the complete solid**, on the one hand the Tip feature must be the last stage of the construction of this solid, and on the other hand **it is the body which must be selected** and not a stage of its construction.

This will make it possible, in the event of a modification, **to always have the last version of the solid represented.**

**Note and additions :** At each time of the construction, the last function used is the \"Tip\", which can be defined too as \"active stage in the construction of the object\" or \"stage preceding the next action in the construction of the object\". When the object\'s drawing is complete, Tip is naturally the last stage or feature of the construction. But if desired, in case of forgetting, any feature of the construction can be provisionally declared as Tip: it then becomes the step preceding the next action in the construction of the object, which means that new feature(s) can be inserted anywhere in the construction, **on condition not to create any incompatible with the suite**.

When everything is finished, you have to redeclare the last feature as Tip, which corresponds to the finished object.

![centre\|Cumulative Body Solid](images/Part_Design_Cumulativ.png )

This image shows a Body. It is a cumulative solid that consists of a padded sketch and a cone primitive. This is a single solid.

If Tip on **Pad**, the pad can exist separately, but if Tip on **Cone**, the cone cannot exist separately (Tip on cone = pad + cone).

(Another thing mentioned often is a Body ***MUST*** be a single contiguous solid. This means all geometry created by a feature in the Body *must* touch it\'s predecessor.)

## The Ramifications 

Although not recommended for newcomers, it is possible to combine tools from Part WB and PartDesign WB, provided you know what you are doing. For example :

People get caught when they attempt to use some feature under the Body (rather than the Body itself) as one selection of a Part Workbench Boolean operation. This is a problem, because the selected feature does not represent **THE** complete solid.

In a sense, from a Part Workbench standpoint, the Body represents another primitive. So, using a Body (remember it is a proxy for the tip) and a Part Workbench object to do a Boolean is valid. But the resulting object is a Part WWorkbench object. And, thus PartDesign Workbench tools can\'t be used on it any longer.

And, it can get even more complicated. If you create a new Body and drag the result from the previous paragraph into it, a BaseObject is created. And you can go off an use the PartDesign Workbench tools on it.

## The Caveats 

There is a caveat with the Tip and it\'s representation of the single solid in the Body. *If* the tip is a subtractive feature and is used in a dress up operation, for instance a Mirror, the Mirror is operating on the underlying feature (a pocket for example). Thus the cumulative solid is not mirrored, but the subtractive feature is. The result of this must create a single solid.

In this example, a mirror of the tip (which is the pocket of the slot) around any of the base planes, or even a face of the solid will not produce a mirrored solid of the entire model. (In fact, it will produce a Mirrored feature in the tree that is essentially empty.)

![centre\|Solitary solids](images/PhantomMirror.png )

In this example, a mirror of the tip (which is the pocket of the slot) is performed around the datum plane and produces a mirrored slot:

![centre\|Solitary solids](images/MirroredSlot.png )

See the <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [PartDesign Mirrored](PartDesign_Mirrored.md) tool wiki page for more information.

## Comparison

You can see below the same example built with each of the two workbenches. Of course, there are always several possible construction timelines with each workbench. ![Compare constructions with Part WB and PartDesign WB](images/PartWBvsPartDesignWBexample.jpg )

  In <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> PartDesign WB                                                                                    In <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> Part WB
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> New body \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> New Sketch in XZ plane   01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Sketch in XZ plane
  ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                             ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                                               

  ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Revolution / Z   02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Revolve / Z
  ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )          ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg )
                                                                                                  
  ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> New Sketch in XY plane   03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> New Sketch in XY plane
  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )
                                                                                                    
  ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------- --------------------------------------------------------------------------------
  04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Pocket   04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrude
  ![](images/04pocket_PartWBvsPartDesignWBn.jpg )    ![](images/04aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                  
  ------------------------------------------------------------------------------- --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ------------------------------------------------------------------------
                                                                                 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Cut
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/04bCut_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> New Sketch in XZ plane   05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> New Sketch in XZ plane
  ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                    ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                    
  ------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------- --------------------------------------------------------------------------------
  06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> Pad sym/XZ      06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Extrude sym/XZ
  ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )   ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                   
  -------------------------------------------------------------------------------- --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ------------------------------------------------------------------------------
                                                                                 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> Fusion
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06cFusion_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> New Sketch on base planar face   07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketcher WB \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> New Sketch in XZ plane
  ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )          ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                            
  --------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------
  08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> Hole - counterbore            08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Revolve
  ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg )   ![](images/08aRevolve_PartWBvsPartDesignWB.jpg )
                                                                                                   
  ------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------
  09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> Polar Pattern of Hole and Pad   09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Cut
  ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )         ![](images/09Cut_PartWBvsPartDesignWB.jpg )
                                                                                                                     
  ------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------

Compare the construction trees in the two workbenches as well as their organization and reading timeline :

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------
  10- Construction tree in PartDesign WB                                               10- Construction tree in Part WB
  ![](images/PartvsPartDesign_TreePartDesignWB.jpg )   ![](images/PartvsPartDesign_TreePartWB.jpg )
                                                                                       
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------

## Conclusion

Part and PartDesign workbenches can be used together with some care, creating quite complex models.

[Top](#Top.md)


{{Tutorials navi

}}  {{PartDesign Tools navi}} {{Sketcher Tools navi}} 
