---
 TutorialInfo:
   Topic: Placement
   Level: Beginner
   Author: Simbioz
   Time: 5 minutes
   FCVersion: 0.19 or above
   Files: none
---

# Sandbox:Simbioz


**Warning: This is my sandbox where I test things<br>
To not edit**



## How to change the origin of a part 

This brief tutorial will teach you how to change the origin coordinates of a part to a given location.

## Pre-requisites 

1.  FreeCAD 0.19 or later
2.  Lattice 2 WB
3.  Basic FreeCAD Gui understanditg

## Changing Placement 

Assuming you have already created a [Part](Glossary#Part.md) with the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), you now want to change it\'s origin coordinates to somewhere else on/within the part.

Go to the <img alt="" src=images/Lattice2_workbench_icon.svg  style="width:24px;"> [Lattice2 Workbench](Lattice2_Workbench.md) and create an <img alt="" src=images/Lattice2_AttachablePlacement.svg  style="width:24px;"> [Attachable Placement](Lattice2_AttachablePlacement.md), select where you want the new origin to be located, the <img alt="" src=images/Part_EditAttachment.svg  style="width:24px;"> [Part EditAttachment](Part_EditAttachment.md) utility will appear.

object and select an attachment mode in the attachment tab.

1\. create an attached placement. attach it to your object, so that it is the origin you want. 2. create a new placement, \"XY plane\" 3. select the object, the attached placement, and \"XY plane\" placement, and apply \"Populate with copies: moved object\" command. -\> done, a moved copy of the object is created.

## Run a python script 


`exec(open("/path/foo.py").read()) `


```pythonexec(open("/path/foo.py").read())```

## Useful links 

[Mediawiki Links](https://www.mediawiki.org/wiki/Help:Links)
[Formatting](https://www.mediawiki.org/wiki/Help:Formatting)
[Collapsible elements](https://www.mediawiki.org/wiki/Manual:Collapsible_elements)

## collabsed


<div class="toccolours mw-collapsible mw-collapsed" style="width:400px; overflow:auto;">


<div style="font-weight:bold;line-height:1.6;">

Collapsed text:


</div>


<div class="mw-collapsible-content">

This text is collapsed.


</div>


</div>



---
⏵ [documentation index](../README.md) > Sandbox:Simbioz
