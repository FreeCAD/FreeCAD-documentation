# Macro WireFilter/pl
{{Macro
|Name=Macro WireFilter
|Icon=Wirefilter.svg
|Description=Filter wires from sketches, 2D offsets, scales, rearranges wire order
|Author=TheMarkster
|Version=0.2022.02.09
|Date=2022-02-09
|FCVersion=python 3 versions
|Download=[https   *//wiki.freecadweb.org/File   *Wirefilter.svg ToolBar Icon]
|Links=[https   *//github.com/mwganson/wirefilter Full Documentation on Github]
}}

## Description

WireFilter is a macro that can be used to filter certain wires from a sketch. It can also be used on any object with wires, such as a solid. With WireFilter you can do a 2D offset of a wire, you can scale the wire, you can use one of 4 different facemakers (Part   *   *FaceMakerBullseye, Part   *   *FaceMakerCheese, Part   *   *FaceMakerSimple, or Part   *   *FaceMakerExtrusion) if you want to make a face. You can also reset the wire order, which can be useful where a loft is criss-crossing because the wire order is different with the 2 sketches being used.

Examples and full documentation can be found on github   * [WireFilter](https   *//github.com/mwganson/wirefilter).

In the screenshot below, WireFilter is used to make faces from a bullseye sketch (with nested holes within holes) for use with a PartDesign   *   *Pad. Normally, Pad cannot manage such sketches, but if we make the face for it (using FaceMakerBullseye) and select the faces for the Pad it will be able to pad the WireFilter.

<img alt="" src=images/Wirefilter_scr1.png  style="width   *600px;"> 
*Macro WireFilter screenshot‎*

## Known Issues 

Sometimes Pad cannot find the correct normal and the WireFilter is padded off in the wrong direction. This can be fixed by toggling the Fix Normal property of the WireFilter object, which sets the Pad\'s custom direction to the correct normal. This also works for Extrude when it fails to find the correct normal.

## Legend


{{Codeextralink|https   *//gist.github.com/mwganson/0aedd5e9057650d0a1f0483f3cc2fa6c/raw/e9d282440f8ae58817df8fad1c4995861c7cc949/wirefilter.FCMacro|wirefilter.FCMacro}}

ToolBar Icon ![](images/Wirefilter.svg )

## Script

**Macro Wirefilter.FCMacro**


{{CodeDownload|https   *//gist.github.com/mwganson/0aedd5e9057650d0a1f0483f3cc2fa6c|Wirefilter.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro WireFilter/pl
