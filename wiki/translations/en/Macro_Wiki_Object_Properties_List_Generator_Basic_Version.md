# Macro Wiki Object Properties List Generator Basic Version/en
{{Macro
|Name=Wiki List Generator of Object Properties
|Description=This macro generate properties list of selected object. List presented in wiki format into Python report view.
|Author=Evgeniy
|Date=2021-09
|Version=0.1
|SeeAlso=[Macro Wiki Object Properties List Generator](Macro_Wiki_Object_Properties_List_Generator.md)
}}

## Description

This simple macro generate properties list of selected object. The parameters list is printed to the [Report view](Report_view.md) of FreeCAD. This example is more educational in nature and is not applicable for use without editing after generate, since it includes absolutely all the parameters of the object. The lists of properties that are published in this wiki contain, as a rule, only unique parameters. The parameters inherited from the parents objects are not published.

## Usage

-   Preparing:
    -   Copy code of Macro from this page and place it in a new \*.FCMacro file.
    -   Save FCMacro file, and place it in the FreeCAD Macros folder.
    -   Disable **Include a timecode for each entry** checkbox in Preferences -\> General -\> Output window (Tab).
-   First using:
    -   Select (or create and select) object the type of you need in tree view.
    -   Select Macro -\> Macros\... item in main menu.
    -   In opened window find \*.FCMacro file what you save letter and press **Execute** Button.
-   How to use again:
    -   To quickly run this macro again, you can use keyboard shortcut **Shift+Ctrl+1** (on Windows) it will launch the last run macro.

## Recommendations

Do not delete spaces between lines. This is necessary to simplify the translation. Each line separated by a space will be considered a separate part for translation. When creating texts, always remember that large monolithic fragments of text are difficult for translators to translate.

## Example of using 

-   For example open the Arch Workbench
-   Create a Structure object.
-   Select the created Structure object.
-   Run the macro.
-   Copy the text from the report view and paste it in a wiki page and check the result.

## Results of using 

The results may look like this:

## Properties

### View

-    **Proxy|PythonObject**:


{{TitleProperty|Component}}

-    **UseMaterialColor|Bool**: Use the material color as this object\'s shape color, if available


{{TitleProperty|Display Options}}

-    **BoundingBox|Bool**: Display object bounding box

-    **DisplayMode|Enumeration**: Set the display mode

-    **ShowInTree|Bool**: Show the object in the tree view

-    **Visibility|Bool**: Show the object in the 3d view


{{TitleProperty|Nodes}}

-    **NodeColor|Color**: The color of the nodes line

-    **NodeLine|Float**: The width of the nodes line

-    **NodeSize|Float**: The size of the node points

-    **NodeType|Enumeration**: The type of structural node

-    **ShowNodes|Bool**: If the nodes are visible or not


{{TitleProperty|Object Style}}

-    **AngularDeflection|Angle**: Specify how finely to generate the mesh for rendering on screen or when exporting.

The default value is 28.5 degrees, or 0.5 radians. The smaller the value the smoother the appearance in the 3D view, and the finer the mesh that will be exported.

-    **Deviation|FloatConstraint**: Sets the accuracy of the polygonal representation of the model

in the 3D view (tessellation). Lower values indicate better quality. The value is in percent of object\'s size.

-    **DiffuseColor|ColorList**: Object diffuse color.

-    **DrawStyle|Enumeration**: Defines the style of the edges in the 3D view.

-    **Lighting|Enumeration**: Set object lighting.

-    **LineColor|Color**: Set object line color.

-    **LineColorArray|ColorList**: Object line color array.

-    **LineMaterial|Material**: Object line material.

-    **LineWidth|FloatConstraint**: Set object line width.

-    **PointColor|Color**: Set object point color

-    **PointColorArray|ColorList**: Object point color array.

-    **PointMaterial|Material**: Object point material.

-    **PointSize|FloatConstraint**: Set object point size.

-    **ShapeColor|Color**: Set shape color

-    **ShapeMaterial|Material**: Shape material

-    **Transparency|Percent**: Set object transparency


{{TitleProperty|Selection}}

-    **OnTopWhenSelected|Enumeration**: Enabled: Display the object on top of any other object when selected

Object: On top only if the whole object is selected Element: On top only if some sub-element of the object is selected

-    **Selectable|Bool**: Set if the object is selectable in the 3d view

-    **SelectionStyle|Enumeration**: Set the object selection style

### Data

-    **Placement|Placement**:

-    **Proxy|PythonObject**:

-    **Shape|Part::PropertyPartShape**:

-    **Visibility|Bool**:


{{TitleProperty|Base}}

-    **ExpressionEngine|ExpressionEngine|Hidden**: Property expressions

-    **Label|String**: User name of the object (UTF8)

-    **Label2|String|Hidden**: User description of the object (UTF8)


{{TitleProperty|Component}}

-    **Additions|LinkList**: Other shapes that are appended to this object

-    **Axis|Link**: An optional axis or axis system on which this object should be duplicated

-    **Base|Link**: The base object this component is built upon

-    **CloneOf|Link**: The object this component is cloning

-    **HiRes|Link**: An optional higher-resolution mesh or shape for this object

-    **HorizontalArea|Area**: The area of the projection of this object onto the XY plane

-    **Material|Link**: A material for this object

-    **MoveBase|Bool**: Specifies if moving this object moves its base instead

-    **MoveWithHost|Bool**: Specifies if this object must move together when its host is moved

-    **PerimeterLength|Length**: The perimeter length of the horizontal area

-    **StandardCode|String**: An optional standard (OmniClass, etc\...) code for this component

-    **Subtractions|LinkList**: Other shapes that are subtracted from this object

-    **VerticalArea|Area**: The area of all vertical faces of this object


{{TitleProperty|IFC}}

-    **IfcData|Map**: IFC data

-    **IfcProperties|Map**: IFC properties of this object

-    **IfcType|Enumeration**: The type of this object


{{TitleProperty|IFC Attributes}}

-    **Description|String**: Description of IFC attributes are not yet implemented

-    **GlobalId|String**: Description of IFC attributes are not yet implemented

-    **ObjectType|String**: Description of IFC attributes are not yet implemented

-    **PredefinedType|Enumeration**: Description of IFC attributes are not yet implemented

-    **Tag|String**: Description of IFC attributes are not yet implemented


{{TitleProperty|Structure}}

-    **FaceMaker|Enumeration**: The facemaker type to use to build the profile of this object

-    **Height|Length**: The height or extrusion depth of this element. Keep 0 for automatic

-    **Length|Length**: The length of this element, if not based on a profile

-    **Nodes|VectorList**: The structural nodes of this element

-    **NodesOffset|Distance**: Offset distance between the centerline and the nodes line

-    **Normal|Vector**: The normal extrusion direction of this object (keep (0,0,0) for automatic normal)

-    **Profile|String**: A description of the standard profile this element is based upon

-    **Tool|Link**: An optional extrusion path for this element

-    **Width|Length**: The width of this element, if not based on a profile

## Script


{{MacroCode|code= 
#! python
# -*- coding: utf-8 -*-
# <nowiki>(c) 2021 </nowiki><<nowiki>Evgeniy</nowiki>><nowiki> LG
from FreeCAD import Qt

def print_obj_properties(obj,typ):
   prop={}
   i=1
   for pr in obj.PropertiesList:
      tp = obj.getTypeIdOfProperty(pr) or ""
      atr = obj.getTypeOfProperty(pr) or ("")
      # Wiki template supports only Hidden type of property. But it can be as: Hidden,Output,Readonly etc...
      if atr != "" and atr[0] == "Hidden":
         atr = "|"+atr[0]
      else:
         atr = ""      
      prop[str(i)] = pr,obj.getGroupOfProperty(pr),tp.replace("App::Property",""),obj.getDocumentationOfProperty(pr),atr
      i+=1
   sorted_prop = sorted(prop.items(), key=lambda x: x[1][1])

   title=""
   for pr in sorted_prop:
      if title != pr[1][1]:
         title = pr[1][1]
         print("\n"+"{{TitleProperty{"+title+"}}")
      print("\n"+"* {{Property"+typ+"{"+pr[1][0]+"{"+pr[1][2]+pr[1][4]+"}}: "+pr[1][3])

print("\n"+"==Properties==")
print("\n"+"===View===")
obj = Gui.activeDocument().ActiveObject
print_obj_properties(obj,"View")
print("\n"+"===Data===")
obj = FreeCAD.activeDocument().ActiveObject
print_obj_properties(obj,"Data")
</nowiki>
}}

## Links

The discussion on the forum: <https://forum.freecadweb.org/viewtopic.php?f=21&t=61998>



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Wiki Object Properties List Generator Basic Version/en
