# Part and PartDesign/de
{{TOCright}}

## Übersicht

Im Laufe der Jahre gab es viele Diskussionen über die Unterschiede und Auswirkungen der Verwendung des <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/de.md) und des <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench/de.md) Arbeitsbereichs.

Es ist eine gute Idee, den einen oder den anderen zu verwenden, bis der Benutzer mit dem einen vertraut ist, und dann das andere zu lernen. In der Regel wird auch empfohlen, dass neue Benutzer die beiden nicht mischen, bis sie die Auswirkungen verstanden haben.

Lass uns über diese Auswirkungen sprechen.

## Part Arbeitsbereich Konzepte 

Part Arbeitsbereich ist im Wesentlichen [CSG style modeling](Constructive_solid_geometry/de.md). Der Bediener kombiniert verschiedene Grundelemente, um am Ende eine Darstellung der gewünschten Form zu erhalten. (Tatsächlich geht Part Arbeitsbereich einen Schritt weiter als nur Grundelemente und erlaubt dem Anwender, eine Skizze+Extrudieren Ausführung (oder Skizze+Drehen, Austragen, Ausformen \...) zu verwenden, um auch zufällige Formen zu erstellen.) Wenn ein Grundelement oder eine Form erstellt wird, hat es keine Beziehung zu anderen erstellten Objekten (mit Ausnahme von Skizzen und deren Anhängen), es ist ein einzelner solitärer Körper.

![centre\|Solitary solids](images/Part_CSG_Prims.png )

This condition remains so, until, the operator uses some operation to combine them (typically a Boolean that adds or subtracts them). Each starting solid remains accessible separately and the operation creates a new object.

The take away is the single solitary solid bit and the combining them bit.

## PartDesign Arbeitsbereich Konzepte 

Im PartDesign Arbeitsbereich wird das Körperobjekt direkt als einzelner, kumulativer Festkörper konstruiert.

Der 1. Schritt in einem Körper muss ein Materialblock sein, entweder aus einem additiven Grundelement oder einer Extrusion aus einer Skizze, oder eine importierte Form (dann Basis Formelement genannt).

Dieser anfängliche Materialblock wird nach und nach verändert, bis die gewünschte Endform (Festkörper) erreicht ist.

Es ist kumulativ in dem Sinne, dass bei jedem Vorgang Material hinzugefügt oder entfernt wird.

By default, the \"tip\" of the body - unless there is a voluntary change in the visualization of a particular feature - is the last operation performed on the body. This is the current and visible state of the body, ready to be changed again by new feature.

Any function under the body represents the cumulative shape of the solid from the 1st feature to the feature considered.

So **to have the complete solid**, on the one hand the Tip feature must be the last stage of the construction of this solid, and on the other hand **it is the body which must be selected** and not a stage of its construction.

This will make it possible, in the event of a modification, **to always have the last version of the solid represented.**

**Note and additions    *** At each time of the construction, the last function used is the \"Tip\", which can be defined too as \"active stage in the construction of the object\" or \"stage preceding the next action in the construction of the object\". When the object\'s drawing is complete, Tip is naturally the last stage or feature of the construction. But if desired, in case of forgetting, any feature of the construction can be provisionally declared as Tip   * it then becomes the step preceding the next action in the construction of the object, which means that new feature(s) can be inserted anywhere in the construction, **on condition not to create any incompatible with the suite**.

When everything is finished, you have to redeclare the last feature as Tip, which corresponds to the finished object.

![centre\|Cumulative Body Solid](images/Part_Design_Cumulativ.png )

This image shows a Body. It is a cumulative solid that consists of a padded sketch and a cone primitive. This is a single solid.

If Tip on **Pad**, the pad can exist separately, but if Tip on **Cone**, the cone cannot exist separately (Tip on cone = pad + cone).

(Another thing mentioned often is a Body ***MUST*** be a single contiguous solid. This means all geometry created by a feature in the Body *must* touch it\'s predecessor.)

## Die Auswirkungen 

Although not recommended for newcomers, it is possible to combine tools from Part workbench and PartDesign workbench, provided you know what you are doing. For example    *

People get caught when they attempt to use some feature under the Body (rather than the Body itself) as one selection of a Part Workbench Boolean operation. This is a problem, because the selected feature does not represent **THE** complete solid.

In a sense, from a Part Workbench standpoint, the Body represents another primitive. So, using a Body (remember it is a proxy for the tip) and a Part Workbench object to do a Boolean is valid. But the resulting object is a Part Workbench object. And, thus PartDesign Workbench tools can\'t be used on it any longer.

And, it can get even more complicated. If you create a new Body and drag the result from the previous paragraph into it, a BaseObject is created. And you can go off an use the PartDesign Workbench tools on it.

## Die Vorbehalte 

There is a caveat with the Tip and it\'s representation of the single solid in the Body. *If* the tip is a subtractive feature and is used in a dress up operation, for instance a Mirror, the Mirror is operating on the underlying feature (a pocket for example). Thus the cumulative solid is not mirrored, but the subtractive feature is. The result of this must create a single solid.

In this example, a mirror of the tip (which is the pocket of the slot) around any of the base planes, or even a face of the solid will not produce a mirrored solid of the entire model. (In fact, it will produce a Mirrored feature in the tree that is essentially empty.)

![centre\|Solitary solids](images/PhantomMirror.png )

In this example, a mirror of the tip (which is the pocket of the slot) is performed around the datum plane and produces a mirrored slot   *

![centre\|Solitary solids](images/MirroredSlot.png )

See the <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *24px;"> [PartDesign Mirrored](PartDesign_Mirrored.md) tool wiki page for more information.

## Vergleich

You can see below the same example built with each of the two workbenches. Of course, there are always several possible construction timelines with each workbench. ![Compare constructions with Part workbench and PartDesign workbench](images/PartWBvsPartDesignWBexample.jpg )

  In <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> PartDesign workbench                                                                             In <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> Part workbench
   
  01- <img alt="" src=images/PartDesign_Body.svg  style="width   *32px;"> New body \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XZ plane   01- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> Sketch in XZ plane
  ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                             ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                                               

   
  02- <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> Revolution / Z   02- <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> Revolve / Z
  ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )          ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg )
                                                                                                  
   

   
  03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XY plane   03- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XY plane
  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )
                                                                                                    
   

   
  04- <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> Pocket   04a- <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> Extrude
  ![](images/04pocket_PartWBvsPartDesignWBn.jpg )    ![](images/04aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                  
   

   
                                                                                 04b- <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> Cut
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/04bCut_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XZ plane   05- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XZ plane
  ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                    ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                    
   

   
  06- <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> Pad sym/XZ      06a- <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> Extrude sym/XZ
  ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )   ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                   
   

   
                                                                                 06b- <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width   *32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
                                                                                 06c- <img alt="" src=images/Part_Fuse.svg  style="width   *32px;"> Fusion
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06cFusion_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch on base planar face   07- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XZ plane
  ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )          ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                            
   

   
  08- <img alt="" src=images/PartDesign_Hole.svg  style="width   *32px;"> Hole - counterbore            08a- <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> Revolve
  ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg )   ![](images/08aRevolve_PartWBvsPartDesignWB.jpg )
                                                                                                   
   

   
                                                                                 08b- <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width   *32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *32px;"> Polar Pattern of Hole and Pad   09- <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> Cut
  ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )         ![](images/09Cut_PartWBvsPartDesignWB.jpg )
                                                                                                                     
   

Compare the construction trees in the two workbenches as well as their organization and reading timeline    *

   
  10- Construction tree in PartDesign workbench                                        10- Construction tree in Part workbench
  ![](images/PartvsPartDesign_TreePartDesignWB.jpg )   ![](images/PartvsPartDesign_TreePartWB.jpg )
                                                                                       
   

## Schlussfolgerung

Die Arbeitsbereiche Part und PartDesign können mit etwas Vorsicht zusammen verwendet werden, um recht komplexe Modelle zu erstellen.

[Anfang](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/de
