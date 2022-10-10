# Sandbox:TechDraw TemplateExplained
{{TOCright}}

## Introduction

TechDraw templates are SVG files used as the basis to create Technical drawings in FreeCAD. They can be used with the Draft workbench as well.

This document lists the necessary elements while building an A3 template.

Just a text simple text editor is needed to create a simple svg file. The necessary lines could be typed or copied into the document.

Such a tidied up file could be a basis for a Python macro\...

## Structure of a simple blank page 

The SVG format is a subset of the XML format. That is why an SVG file, like any XML file, consists of two parts   *

-   Head, a format declaration
-   Body, containing the information what to show and where to place it

### Head

The head is just one line to declare which version of the XML language an interpreter should use to handle the instructions in the body.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}

### Body

The Body starts with an opening tag which contains information about name spaces and about the size of the template and where to place it. And it finishes with a closing tag.


{{Code|lang=xml|code=
<svg
  xmlns="http   *//www.w3.org/2000/svg" version="1.1"
  xmlns   *freecad="http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


   *   **xmlns=**\"<http   *//www.w3.org/2000/svg>\"   * External link to the xml name space to look up standard xml commands
   *   **version=**\"1.1\"   * used xml version is 1.1
   *   **xmlns   *freecad=**\"<http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"   * External link to FreeCAD\'s name space extension

       *   to look up special commands that are only used inside a FreeCAD environment e.g. for editable texts
   *   **width=**\"420mm\"   * Width of the drawing area
   *   **height=**\"297mm\"   * Height of the drawing area
   *   **viewBox=**\"0 0 420 297\"   * Position of the upper left corner (0;0) and the lower right corner (420;297) in the svg construction space (in svg units).
   *   Width, height, and viewBox in this combination set 1 svg-unit to 1 mm for the whole document. A dimensional unit can be omitted from now on.

### Result   * a blank page of DIN A3 format 

For a blank page size DIN A3 in landscape orientation that\'s all.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http   *//www.w3.org/2000/svg" version="1.1"
  xmlns   *freecad="http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


   *   

       *   Just copy or type these few lines and save it as e.g. *MyFirstA3Template-blank*.svg

## Frame elements 

With FreeCAD it is not (yet) possible to draw frames and title blocks onto blank pages, and so it is done in advance by placing those elements inside the svg template file.

To create frame, title block, annotations, graphical elements, and editable texts the related code segments need to be added between the svg-tags.

Similar objects are grouped with the g-tag where the opening tag could contain an ID, some style parameters, and sub-groups.

For a complete drawing frame we need the frame(s) itself, separators, and indexes, folding lines, and a center mark for puncher holes.

### Frame

The frame consists of two rectangles, one for the sheet frame and one for the drawing area.

   *   The sheet frame has an offset of 5 mm from the page edges except on the left where additional 10 mm are added.
   *   The drawing area has another 5 mm offset from the sheet frame


{{Code|lang=xml|code=
<g id="drawing-frame"
  style="fill   *none;stroke   *#000000;stroke-width   *0.5;stroke-linecap   *miter;stroke-miterlimit   *4">
    <<nowiki>!-- Drawing area 20 10 410 287 --</nowiki>>
    <rect width="390" height="277" x="20" y="10" />
    <<nowiki>!-- Sheet frame 15 5 415 292 --</nowiki>>
    <rect width="400" height="287" x="15" y="5" />
</g>
}}


   *   

       *   The group\'s ID is \"drawing-frame\"
       *   It contains two rectangles which represent the sheet (outer) frame and the outline of the drawing area.
       *   **fill   *none** means closed shapes will not be filled. If this is missing only a black rectangle representing the sheet frame area would be visible.
       *   **stroke   *#000000** means the outline of all grouped objects will be black.
       *   **Rect**angles are defined by their Width, hight, and the position of the upper left corner.

### Separators

In order to virtually split the drawing area into indexed fields index separators are placed between sheet frame and drawing area.


{{Code|lang=xml|code=
<g id="index-separators"
  style="fill   *none;stroke   *#000000;stroke-width   *0.25;stroke-linecap   *miter;stroke-miterlimit   *4">
    <path d="m 215.0,15 v -10" />
    <path d="m 215.0,282 v  10" />
    <path d="m 25,148.5 h -20" />
    <path d="m 405,148.5 h  10" />
    <path d="m 265.0,10 v  -5" />
    <path d="m 265.0,287 v   5" />
    <path d="m 165.0,10 v  -5" />
    <path d="m 165.0,287 v   5" />
    <path d="m 315.0,10 v  -5" />
    <path d="m 315.0,287 v   5" />
    <path d="m 115.0,10 v  -5" />
    <path d="m 115.0,287 v   5" />
    <path d="m 365.0,10 v  -5" />
    <path d="m 365.0,287 v   5" />
    <path d="m 65.0,10 v  -5" />
    <path d="m 65.0,287 v   5" />
    <path d="m 20,198.5 h  -5" />
    <path d="m 410,198.5 h   5" />
    <path d="m 20,98.5 h  -5" />
    <path d="m 410,98.5 h   5" />
    <path d="m 20,248.5 h  -5" />
    <path d="m 410,248.5 h   5" />
    <path d="m 20,48.5 h  -5" />
    <path d="m 410,48.5 h   5" />
</g>
}}


   *   

       *   Since no transformation is involved yet each path starts at the svg file\'s origin.
       *   At first a relative **m**ovement of a virtual pen to a certain position without drawing
       *   followed by a **h**orizontal or **v**ertical movement drawing a line.
       *   Capital letters denote movements to absolute positions otherwise the movements are relative to the last position.

### Indexes

Now the indexes are inserted.


{{Code|lang=xml|code=
<g id="indexes"
  style="font-size   *3.5;text-anchor   *middle;font-family   *osifont">
    <text x="240.0" y="9">5</text>
    <text x="240.0" y="291">5</text>
    <text x="190.0" y="9">4</text>
    <text x="190.0" y="291">4</text>
    <text x="290.0" y="9">6</text>
    <text x="290.0" y="291">6</text>
    <text x="140.0" y="9">3</text>
    <text x="140.0" y="291">3</text>
    <text x="340.0" y="9">7</text>
    <text x="340.0" y="291">7</text>
    <text x="90.0" y="9">2</text>
    <text x="90.0" y="291">2</text>
    <text x="390.0" y="9">8</text>
    <text x="390.0" y="291">8</text>
    <text x="40.0" y="9">1</text>
    <text x="40.0" y="291">1</text>
    <text x="17.5" y="173.5">D</text>
    <text x="412.5" y="173.5">D</text>
    <text x="17.5" y="123.5">C</text>
    <text x="412.5" y="123.5">C</text>
    <text x="17.5" y="223.5">E</text>
    <text x="412.5" y="223.5">E</text>
    <text x="17.5" y="73.5">B</text>
    <text x="412.5" y="73.5">B</text>
    <text x="17.5" y="273.5">F</text>
    <text x="412.5" y="273.5">F</text>
    <text x="17.5" y="23.5">A</text>
    <text x="412.5" y="23.5">A</text>
</g>
}}


   *   

       *   Since no transformation is involved yet each distance relates to the svg file\'s origin and so capital letters could be used for **x** and **y** as well.

### Folding Marks 

Folding marks show where to fold a drawing to reduce its size to DIN A4. (DIN based drawings at least)


{{Code|lang=xml|code=
<g id="folding marks"
  style="fill   *none;stroke   *#b0b0b0;stroke-width   *0.25;stroke-linecap   *miter;stroke-miterlimit   *4">
    <path d="m 125,5 v  -5" />
    <path d="m 125,292 v   5" />
    <path d="m 230,5 v -5" />
    <path d="m 230,292 v   5" />
</g>
}}

### Center mark 

The center mark shows where to put the centre of puncher to get perfectly positioned puncher holes. But a DIN A3 formatted drawing is a bad example for a center mark, because it is substituted with a longer index separator this case.

See {{Code|lang=xml|code=
<path d="m 25,148.5 h -20" />
}} above

## Title block elements 

The title block contains elements like a frame, a segmentation, non-editable texts, and editable texts. {{Code|lang=xml|code=
<g id="titleblock"
  transform="translate(230,287)">
    <<nowiki>!-- Title block origin --</nowiki>>
</g>
}}

   *   

       *   This group is used to set the title block\'s origin and to move all elements between its tags.
       *   If it is copied into another file defining a different page format then only the coordinates need to be updated and the whole title block is moved into the wanted location.
       *   **transform=\"translate(230,287)\"** defines a translation of 230 units in x direction and 287 units in y direction.
       *   Remember   * One unit was set to 1 mm within the svg-tag. And so all is moved 230 mm to the right and 287 mm down.

### Title block frame 

This group defines the outline and the coarse segmentation of the title block. The coordinates relate to the svg-file\'s origin, because relocation is done with the \"titleblock\" group.


{{Code|lang=xml|code=
<g id="titleblock-frame"
  style="fill   *none;stroke   *#000000;stroke-width   *0.35;stroke-linecap   *miter;stroke-miterlimit   *4">
    <path d="m   0,  0 l   0,-35" />
    <path d="m   0,-35 l 180,  0" />
    <path d="m   0,-14 h 180" />
    <path d="m  60,  0 v -35" />
    <path d="m 152,  0 v -35" />
</g>
}}

### Title block segmentation 

This group defines the fine segmentation of the title block. Two groups of segmentation lines are needed, because they use different stroke-width values.


{{Code|lang=xml|code=
<g id="titleblock-structure"
  style="fill   *none;stroke   *#000000;stroke-width   *0.18;stroke-linecap   *miter;stroke-miterlimit   *4">
    <path d="m   0,-21 h  60" />
    <path d="m   0,-28 h  60" />
    <path d="m 152, -7 h  28" />
    <path d="m 152,-21 h  28" />
    <path d="m 152,-28 h  28" />
    <path d="m  12,-14 v -21" />
    <path d="m  36,-14 v -21" />
</g>
}}

### Title block text non-editable 

To label the entry fields of the title block non-editable texts are used.


{{Code|lang=xml|code=
<g id="titleblock-text-non-editable"
  style="font-size   *2;text-anchor   *start;font-family   *osifont"
  xml   *space="preserve">
    <text x="  1.5" y="-31  ">Drawn   *</text>
    <text x="  1.5" y="-24  ">Approved   *</text>
    <text x=" 13.5" y="-32.5">Name   *</text>
    <text x=" 13.5" y="-25.5">Name   *</text>
    <text x=" 13.5" y="-18.5">CAD Version   *</text>
    <text x=" 37.5" y="-32.5">Datum   *</text>
    <text x=" 37.5" y="-25.5">Datum   *</text>
    <text x=" 61.5" y="-32.5">Title   *</text>
    <text x=" 61.5" y="-11.5">Part Number   *</text>
    <text x="153.5" y="-32.5">Scale   *</text>
    <text x="153.5" y="-25.5">Material   *</text>
    <text x="153.5" y="-18.5">Mass   *</text>
    <text x="153.5" y="-11.5">Format   *</text>
    <text x="153.5" y=" -4.5">Sheet   *</text>
</g>
}}


<div class="mw-collapsible mw-collapsed toccolours">

### Projection mode symbol 


<div class="mw-collapsible-content">

That symbol shows if first angle projection is used to arrange the views or third angle projection. It is drawn around the origin and the moved to its position inside the title block.


{{Code|lang=xml|code=
<g id="Projection-symbol"
  stroke="#000000"
  stroke-width="0.18"
  fill="none"
  transform="translate(52,-17.5)">
    <circle cx="0.0" cy="0.0" r="1.0"
      stroke="#0000d0" stroke-width="0.35"/>
    <circle cx="0.0" cy="0.0" r="2.0"
      stroke="#0000d0" stroke-width="0.35"/>
    <path d="m -9.0 1.0 v -2.0 l 5.0 -1.0 v 4.0 z "
      stroke="#0000d0" stroke-width="0.35"/>
    <path d="m  -2.5 , 0    h   1" />
    <path d="m  -1.15, 0    h  0.3" />
    <path d="m  -0.5 , 0    h   1" />
    <path d="m   0.85, 0    h  0.3" />
    <path d="m   1.5 , 0    h   1" />
    <path d="m   0   ,-2.5  v  1" />
    <path d="m   0   ,-1.15 v  0.3" />
    <path d="m   0   ,-0.5  v  1" />
    <path d="m   0   , 0.85 v  0.3" />
    <path d="m   0   , 1.5  v  1" />
    <path d="m  -9.5 , 0    h   1" />
    <path d="m  -4.5 , 0    h  1" />
    <path d="m  -7   , 0    h   1" />
    <path d="m  -7.9 , 0    h  0.3" />
    <path d="m  -5.4 , 0    h   0.3" />
</g>
}}


</div>


   *   

       *   Parameters can be placed inside not only in the group tag but inside the circle and path tags as well.
       *   the values defined inside the circle and path tags override the values defined in the group tag.


</div>

### FreeCAD logo 

The FreeCAD logo consists of an F symbol and a cog symbol. The shared parameters are within the group tag and the individual parameters inside the Path tag.


{{Code|lang=xml|code=
<g id="freecad-logo"
  style="display   *inline"
  stroke="#000000"
  stroke-width="0.25"
  fill="none"
  fill-rule="evenodd"
  transform="translate(4,-19.5) scale(0.5)">
    <path id="freecad-logo-F"
      d="m0.1524,0.15254 v8.8549 h1.9744 v-3.4652 h1.396 v-1.3661 h-1.396 v-1.4745 h3.4391 v-2.5441 l-5.4135 -0.005z"
      fill="rgb(255, 50, 50)"/>
    <path id="freecad-logo-Cog"
      d="m7.7927,3.4504 -0.50715,-0.176 -0.48387 -1.2366 -0.76115 0.04 -0.34718 1.2787 -0.4859 0.23269 -1.2119 -0.53015 -0.51188 0.56882 0.65892 1.1485 -0.18006 0.50567 -1.2366 0.48387 0.044064 0.76263 1.2787 0.34718 0.23269 0.4859 -0.53421 1.2104 0.56882 0.51188 1.1485 -0.65891 0.50973 0.18155 0.4798 1.2351 0.7667 -0.04258 0.34311 -1.2802 0.4859 -0.23269 1.2145 0.5357 0.51188 -0.56882 -0.65891 -1.1485 0.17748 -0.51122 1.2351 -0.4798 -0.03851 -0.76521 -1.2802 -0.34311 -0.23269 -0.4859 0.53163 -1.216 -0.56881 -0.51184z m-0.5715 1.2244 0.23576 0.13679 0.20426 0.18519 0.16353 0.22101 0.11763 0.24572 0.06916 0.26489 0.01146 0.27146 -0.03921 0.27139 -0.08948 0.25764 -0.14234 0.23834 -0.17964 0.2016 -0.22101 0.16353 -0.24572 0.11763 -0.26489 0.06916 -0.27295 0.01553 -0.2719 -0.04 -0.2576 -0.089 -0.2383 -0.143 -0.2002 -0.183 -0.165 -0.217 -0.1177 -0.246 -0.0676 -0.269 -0.0156 -0.273 0.039206 -0.2714 0.089484 -0.25764 0.14085 -0.23427 0.18113 -0.20574 0.22101 -0.16352 0.24572 -0.11763 0.26895 -0.06768 0.27147-0.01146 0.27139 0.03921 0.25764 0.08948z"
      fill="rgb(50, 50, 255)"/>
 </g>
}}


   *   

       *   The group tag contains all parameters to draw outline only symbols
       *   The colour parameters inside the Path tags override the \"none\" value of the Group tag.
       *   The logo paths are copied from an existing file and not split in single strokes like in the other sections, and so the coordinates are less clearly represented.

### Title block text editable 

The editable texts are sorted according to font size. The group tag defines the font family and the colour of the editable texts. Sub group tags add the font size and the position of the text anchor.

**Attention!** Coordinates of editable texts have to be absolute (relate to the document\'s origin)! They are not compatible with transformations!

   *   

       *   (Only the texts could be moved but the green handles would stay in place)


{{Code|lang=xml|code=
<g id="titleblock-text-editable"
  style="font-family   *osifont"
  fill="#0000d0">
    <g id="titleblock-editable-small"
      style="font-size   *3.5;text-anchor   *start">
      <text freecad   *editable="Drawn" x="244" y="258">  <tspan>Your Name</tspan>  </text>
      <text freecad   *editable="DrDate" x="269" y="258">  <tspan>YY/MM/DD</tspan>  </text>
      <text freecad   *editable="Approved" x="244" y="265">  <tspan>---</tspan>  </text>
      <text freecad   *editable="ApDate" x="269" y="265">  <tspan>YY/MM/DD</tspan>  </text>
      <text freecad   *editable="CADVersion" x="244" y="272">  <tspan>FreeCAD 0.19</tspan>  </text>
      <text freecad   *editable="Material" x="395" y="264.5">  <tspan>Mat.</tspan>  </text>
      <text freecad   *editable="Mass" x="395" y="271.5">  <tspan>-,- g</tspan>  </text>
    </g>
    <g id="titleblock-editable-medium"
      style="font-size   *5;text-anchor   *start">
      <text freecad   *editable="Title" x="293" y="260">  <tspan>Part name</tspan>  </text>
      <text freecad   *editable="SubTitle" x="293" y="267">  <tspan>-</tspan>  </text>
      <text freecad   *editable="Scale" x="395" y="258">  <tspan>1   *1</tspan>  </text>
      <text freecad   *editable="Format" x="395" y="279">  <tspan>A3</tspan>  </text>
      <text freecad   *editable="Sheets" x="395" y="286">  <tspan>1 / 1</tspan>  </text>
    </g>
    <g id="titleblock-editable-Large"
      style="font-size   *7;text-anchor   *end">
        <text freecad   *editable="DrNumber" x="377" y="285">  <tspan>Drawing number</tspan>  </text>
    </g>
    <g id="titleblock-editable-company"
      style="font-size   *2.5;text-anchor   *start">
        <text freecad   *editable="Company" x="246" y="276">  <tspan>Company name</tspan>  </text>
    </g>
    <g id="titleblock-editable-address"
      style="font-size   *1.8;text-anchor   *start">
        <text freecad   *editable="Address-1" x="246" y="279">  <tspan>Street address</tspan>  </text>
        <text freecad   *editable="Address-2" x="246" y="281.5">  <tspan>Postcode + City, Country</tspan>  </text>
        <text freecad   *editable="MailTo" x="246" y="286">  <tspan>Name@Website</tspan>  </text>
    </g>
</g>
}}


   *   

       *   The text tags are extended with **freecad   *editable=\"** *variable name* **\"** to supply The FreeCAD file with addressable variables when the template is inserted.
       *   The default texts need to be surrounded by tspan tags otherwise the displayed text within the title block will not synchronise with modified variable content.


<div class="mw-collapsible mw-collapsed toccolours">

### Complete template 

<img alt="" src=images/TechDraw_PageDefault.svg  style="width   *64px;">


<div class="mw-collapsible-content">


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http   *//www.w3.org/2000/svg" version="1.1"
  xmlns   *freecad="http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
    <g id="drawing-frame"
      style="fill   *none;stroke   *#000000;stroke-width   *0.5;stroke-linecap   *miter;stroke-miterlimit   *4">
      
      <rect width="390" height="277" x="20" y="10" />
      
      <rect width="400" height="287" x="15" y="5" />
    </g>
    <g id="index-separators"
      style="fill   *none;stroke   *#000000;stroke-width   *0.25;stroke-linecap   *miter;stroke-miterlimit   *4">
        <path d="m 215.0,15 v -10" />
        <path d="m 215.0,282 v  10" />
        <path d="m 25,148.5 h -20" />
        <path d="m 405,148.5 h  10" />
        <path d="m 265.0,10 v  -5" />
        <path d="m 265.0,287 v   5" />
        <path d="m 165.0,10 v  -5" />
        <path d="m 165.0,287 v   5" />
        <path d="m 315.0,10 v  -5" />
        <path d="m 315.0,287 v   5" />
        <path d="m 115.0,10 v  -5" />
        <path d="m 115.0,287 v   5" />
        <path d="m 365.0,10 v  -5" />
        <path d="m 365.0,287 v   5" />
        <path d="m 65.0,10 v  -5" />
        <path d="m 65.0,287 v   5" />
        <path d="m 20,198.5 h  -5" />
        <path d="m 410,198.5 h   5" />
        <path d="m 20,98.5 h  -5" />
        <path d="m 410,98.5 h   5" />
        <path d="m 20,248.5 h  -5" />
        <path d="m 410,248.5 h   5" />
        <path d="m 20,48.5 h  -5" />
        <path d="m 410,48.5 h   5" />
    </g>
    <g id="indexes"
      style="font-size   *3.5;text-anchor   *middle;font-family   *osifont">
        <text x="240.0" y="9">5</text>
        <text x="240.0" y="291">5</text>
        <text x="190.0" y="9">4</text>
        <text x="190.0" y="291">4</text>
        <text x="290.0" y="9">6</text>
        <text x="290.0" y="291">6</text>
        <text x="140.0" y="9">3</text>
        <text x="140.0" y="291">3</text>
        <text x="340.0" y="9">7</text>
        <text x="340.0" y="291">7</text>
        <text x="90.0" y="9">2</text>
        <text x="90.0" y="291">2</text>
        <text x="390.0" y="9">8</text>
        <text x="390.0" y="291">8</text>
        <text x="40.0" y="9">1</text>
        <text x="40.0" y="291">1</text>
        <text x="17.5" y="173.5">D</text>
        <text x="412.5" y="173.5">D</text>
        <text x="17.5" y="123.5">C</text>
        <text x="412.5" y="123.5">C</text>
        <text x="17.5" y="223.5">E</text>
        <text x="412.5" y="223.5">E</text>
        <text x="17.5" y="73.5">B</text>
        <text x="412.5" y="73.5">B</text>
        <text x="17.5" y="273.5">F</text>
        <text x="412.5" y="273.5">F</text>
        <text x="17.5" y="23.5">A</text>
        <text x="412.5" y="23.5">A</text>
    </g>
    <g id="folding marks"
      style="fill   *none;stroke   *#b0b0b0;stroke-width   *0.25;stroke-linecap   *miter;stroke-miterlimit   *4">
        <path d="m 125,5 v  -5" />
        <path d="m 125,292 v   5" />
        <path d="m 230,5 v -5" />
        <path d="m 230,292 v   5" />
    </g>

    <g id="titleblock"
      transform="translate(230,287)">
      

      <g id="titleblock-frame"
        style="fill   *none;stroke   *#000000;stroke-width   *0.35;stroke-linecap   *miter;stroke-miterlimit   *4">
          <path d="m   0,  0 l   0,-35" />
          <path d="m   0,-35 l 180,  0" />
          <path d="m   0,-14 h 180" />
          <path d="m  60,  0 v -35" />
          <path d="m 152,  0 v -35" />
      </g>
      <g id="titleblock-structure"
        style="fill   *none;stroke   *#000000;stroke-width   *0.18;stroke-linecap   *miter;stroke-miterlimit   *4">
          <path d="m   0,-21 h  60" />
          <path d="m   0,-28 h  60" />
          <path d="m 152, -7 h  28" />
          <path d="m 152,-21 h  28" />
          <path d="m 152,-28 h  28" />
          <path d="m  12,-14 v -21" />
          <path d="m  36,-14 v -21" />
      </g>
      <g id="titleblock-text-non-editable"
        style="font-size   *2;text-anchor   *start;font-family   *osifont">
          <text x="  1.5" y="-31  ">Drawn   *</text>
          <text x="  1.5" y="-24  ">Approved   *</text>
          <text x=" 13.5" y="-32.5">Name   *</text>
          <text x=" 13.5" y="-25.5">Name   *</text>
          <text x=" 13.5" y="-18.5">CAD Version   *</text>
          <text x=" 37.5" y="-32.5">Date   *</text>
          <text x=" 37.5" y="-25.5">Date   *</text>
          <text x=" 61.5" y="-32.5">Title   *</text>
          <text x=" 61.5" y="-11.5">Part Number   *</text>
          <text x="153.5" y="-32.5">Scale   *</text>
          <text x="153.5" y="-25.5">Material   *</text>
          <text x="153.5" y="-18.5">Mass   *</text>
          <text x="153.5" y="-11.5">Format   *</text>
          <text x="153.5" y=" -4.5">Sheet   *</text>
      </g>
      <g id="Projection-symbol"
        stroke="#000000"
        stroke-width="0.18"
        fill="none"
        transform="translate(52,-17.5)">
          <circle cx="0.0" cy="0.0" r="1.0"
            stroke="#0000d0" stroke-width="0.35"/>
          <circle cx="0.0" cy="0.0" r="2.0"
            stroke="#0000d0" stroke-width="0.35"/>
          <path d="m -9.0 1.0 v -2.0 l 5.0 -1.0 v 4.0 z "
            stroke="#0000d0" stroke-width="0.35"/>
      <path d="m  -2.5 , 0    h   1" />
      <path d="m  -1.15, 0    h  0.3" />
      <path d="m  -0.5 , 0    h   1" />
      <path d="m   0.85, 0    h  0.3" />
      <path d="m   1.5 , 0    h   1" />
      <path d="m   0   ,-2.5  v  1" />
      <path d="m   0   ,-1.15 v  0.3" />
      <path d="m   0   ,-0.5  v  1" />
      <path d="m   0   , 0.85 v  0.3" />
      <path d="m   0   , 1.5  v  1" />
      <path d="m  -9.5 , 0    h   1" />
      <path d="m  -4.5 , 0    h  1" />
      <path d="m  -7   , 0    h   1" />
      <path d="m  -7.9 , 0    h  0.3" />
      <path d="m  -5.4 , 0    h   0.3" />
      </g>
      <g id="freecad-logo"
        style="display   *inline"
        stroke="#000000"
        stroke-width="0.25"
        fill="none"
        fill-rule="evenodd"
        transform="translate(4,-19.5) scale(0.5)">
          <path id="freecad-logo-F"
            d="m0.1524,0.15254 v8.8549 h1.9744 v-3.4652 h1.396 v-1.3661 h-1.396 v-1.4745 h3.4391 v-2.5441 l-5.4135 -0.005z"
            fill="rgb(255, 50, 50)"/>
          <path id="freecad-logo-Cog"
            d="m7.7927,3.4504 -0.50715,-0.176 -0.48387 -1.2366 -0.76115 0.04 -0.34718 1.2787 -0.4859 0.23269 -1.2119 -0.53015 -0.51188 0.56882 0.65892 1.1485 -0.18006 0.50567 -1.2366 0.48387 0.044064 0.76263 1.2787 0.34718 0.23269 0.4859 -0.53421 1.2104 0.56882 0.51188 1.1485 -0.65891 0.50973 0.18155 0.4798 1.2351 0.7667 -0.04258 0.34311 -1.2802 0.4859 -0.23269 1.2145 0.5357 0.51188 -0.56882 -0.65891 -1.1485 0.17748 -0.51122 1.2351 -0.4798 -0.03851 -0.76521 -1.2802 -0.34311 -0.23269 -0.4859 0.53163 -1.216 -0.56881 -0.51184z m-0.5715 1.2244 0.23576 0.13679 0.20426 0.18519 0.16353 0.22101 0.11763 0.24572 0.06916 0.26489 0.01146 0.27146 -0.03921 0.27139 -0.08948 0.25764 -0.14234 0.23834 -0.17964 0.2016 -0.22101 0.16353 -0.24572 0.11763 -0.26489 0.06916 -0.27295 0.01553 -0.2719 -0.04 -0.2576 -0.089 -0.2383 -0.143 -0.2002 -0.183 -0.165 -0.217 -0.1177 -0.246 -0.0676 -0.269 -0.0156 -0.273 0.039206 -0.2714 0.089484 -0.25764 0.14085 -0.23427 0.18113 -0.20574 0.22101 -0.16352 0.24572 -0.11763 0.26895 -0.06768 0.27147-0.01146 0.27139 0.03921 0.25764 0.08948z"
        fill="rgb(50, 50, 255)"/>
      </g>
    </g>
    <g id="titleblock-text-editable"
      style="font-family   *osifont"
      fill="#0000d0">
        <g id="titleblock-editable-small"
          style="font-size   *3.5;text-anchor   *start">
            <text freecad   *editable="Drawn" x="244" y="258">  <tspan>Your Name</tspan>  </text>
            <text freecad   *editable="DrDate" x="269" y="258">  <tspan>YY/MM/DD</tspan>  </text>
            <text freecad   *editable="Approved" x="244" y="265">  <tspan>---</tspan>  </text>
            <text freecad   *editable="ApDate" x="269" y="265">  <tspan>YY/MM/DD</tspan>  </text>
            <text freecad   *editable="CADVersion" x="244" y="272">  <tspan>FreeCAD 0.19</tspan>  </text>
            <text freecad   *editable="Material" x="395" y="264.5">  <tspan>Mat.</tspan>  </text>
            <text freecad   *editable="Mass" x="395" y="271.5">  <tspan>-,- g</tspan>  </text>
    </g>
        <g id="titleblock-editable-medium"
          style="font-size   *5;text-anchor   *start">
            <text freecad   *editable="Title" x="293" y="260">  <tspan>Part name</tspan>  </text>
        <text freecad   *editable="SubTitle" x="293" y="267">  <tspan>-</tspan>  </text>
        <text freecad   *editable="Scale" x="395" y="258">  <tspan>1   *1</tspan>  </text>
        <text freecad   *editable="Format" x="395" y="279">  <tspan>A3</tspan>  </text>
        <text freecad   *editable="Sheets" x="395" y="286">  <tspan>1 / 1</tspan>  </text>
    </g>
    <g id="titleblock-editable-Large"
      style="font-size   *7;text-anchor   *end">
        <text freecad   *editable="DrNumber" x="377" y="285">  <tspan>Drawing number</tspan>  </text>
    </g>
    <g id="titleblock-editable-company"
      style="font-size   *2.5;text-anchor   *start">
        <text freecad   *editable="Company" x="246" y="276">  <tspan>Company name</tspan>  </text>
    </g>
        <g id="titleblock-editable-address"
          style="font-size   *1.8;text-anchor   *start">
            <text freecad   *editable="Address-1" x="246" y="279">  <tspan>Street address</tspan>  </text>
            <text freecad   *editable="Address-2" x="246" y="281.5"> <tspan>Postcode + City, Country</tspan> </text>
            <text freecad   *editable="MailTo" x="246" y="286">  <tspan>Name@Website</tspan>  </text>
        </g>
  </g>
</svg>
}}


</div>


</div>

Dies ist eine Sandbox

[Category   *Sandbox](Category_Sandbox.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Sandbox:TechDraw TemplateExplained
