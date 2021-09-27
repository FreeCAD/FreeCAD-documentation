# TechDraw TemplateHowTo/en
{{TutorialInfo
|Topic=Drafting
|Level=Intermediate
|Time=60 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:wandererfan wandererfan]
|FCVersion=0.17
}}

## Introduction

This tutorial shows you how to create an [SVG](SVG.md) file that can be used as the background [template](TechDraw_Templates.md) for the [TechDraw Workbench](TechDraw_Workbench.md) pages.

This tutorial assumes you are moderately familiar with _, as well as FreeCAD and the [TechDraw Workbench](TechDraw_Workbench.md).

We\'re going to make a simple template for US Letter size paper in landscape orientation.

A copy of the result of this tutorial is available in 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/HowToExample.svg
```

Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example 
```python
/usr/share/freecad/Mod/TechDraw/Templates/HowToExample.svg
```

## Create base document 

1\. Open a new document in Inkscape.

2\. In Document Properties

-   Select page size \"US Letter\" or \"A4\" and orientation \"landscape\".
-   Set default units to \"mm\", and the page size to width \"279.4\" and height \"215.9\". For DIN-A4 you would use \"210\" and \"297\".

<img alt="" src=images/InkDocProp.png  style="width:800px;"> *align=center|Inkscape: document with page size and orientation* 

3\. Use the XML Editor to add a \"freecad\" namespace clause to the `<svg>` item.

:   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)"

Note that your editable texts will *not* work if you use \"<https://>\...\", even though the wiki is reached via https these days. Since SVG is a human readable format you could also enter the line above into the file with a text editor. <img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> *align=center|Inkscape: XML Editor adding the "freecad" namespace clause to the <svg> item* 

## Create template drawing 

4\. Draw outlines, zone numbers, center lines, and other geometry.

5\. Draw the boxes and lines for the title block.

6\. Add and position your static text.

7\. Add and position the text that will be editable.

8\. You now have your finished artwork, that should look something like this: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> *align=center|Inkscape: tentative template layout* 

## Create editable fields 

9\. Use the XML Editor to add a `freecad:editable` tag to each editable `<text>` item.

-   Assign a meaningful field name to each editable text.

<img alt="" src=images/InkXMLeditableTag.png  style="width:800px;"> *align=center|Inkscape: XML Editor adding the "freecad:editable" property to the desired <text> item* 

## Adjust size of the SVG 

10\. Use the XML editor to adjust the `viewBox` attribute to match your page size in millimeters.

-   It is four values, in the format `"0 0 width height"`

<img alt="" src=images/InkXMLviewBox.png  style="width:800px;"> *align=center|Inkscape: XML Editor adjusting the viewbox to match the page size in millimeters* 

11\. Your template will now appear much bigger than desired. <img alt="" src=images/InkMuchTooBig.png  style="width:800px;"> *align=center|Inkscape: tentative template layout exceeding the page size* 

12\. We need to shrink it.

-    **Edit → Select All in All Layers**, or box select and select all.

-   Adjust the **W:** and **H:** spinboxes to match your artwork\'s size in millimeters.

-   Set it to the page size less any applicable margins, for example, **W: 250**, and **H: 200**.

13\. Use \"Align and Distribute\" or the **X:** and **Y:** spinboxes to position the artwork within the limits of the page if required.

14\. Your template should now look right, just like it did in the finished artwork picture above.

## Remove transformans on the SVG 

15\. Ensure that all your editable texts are \"ungrouped\" with **Shift**+**Ctrl**+**g**.

16\. Select everything on your page, **Edit → Select All**, and then **Edit → Copy** (**Ctrl**+**c**).

17\. Then delete the current layer, **Layer → Delete Current Layer**.

:   Note: if you deleted the layer already (in your layer panel is no layer listed) this step is not required. In that case you should select all (**Ctrl**+**a**), cut the selection (**Ctrl**+**x**) and paste it with the command in the next step.

18\. Then paste, **Edit → Paste in Place**.

:   **Note:** This command prevents that the text positions are stored in transform tags. It\'s important that you do not use the normal paste command!

19\. Your template should now look right and shouldn\'t have any unwanted transforms.

20\. Save your template. When you use Inkscape, save it preferably as **Plain SVG** because FreeCAD can only handle the features of the SVG 1.1 specification. **Plain SVG** will remove any Inkscape-specific XML tags.

21\. Try it in FreeCAD and [TechDraw Workbench](TechDraw_Workbench.md) with [Insert Page using Template](TechDraw_PageTemplate.md). ![](images/FCTemplateHow.png ) *align=center|FreeCAD: finished template with an editable text field being modified* 

## Notes

Don\'t use Layers in Inkscape until you\'ve mastered template creation without them. Layers and Groups can automatically insert unwanted transforms into your [SVG](SVG.md) file.

As a final step before using your new template, make sure to remove any transform clauses from the Svg code. Transform clauses **will cause problems**.

See a Stackoverflow discussion on [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

If you do not see the green boxes for your editable texts, there might be something wrong with your document scale. Open your file in Inkscape again and confirm the values of the viewBox and the sizes are matching.


{{Tutorials navi

}} {{TechDraw Tools navi}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateHowTo/en
