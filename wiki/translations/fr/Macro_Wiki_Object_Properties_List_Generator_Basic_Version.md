# Macro Wiki Object Properties List Generator Basic Version/fr
{{Macro/fr
|Name=Wiki List Generator of Object Properties
|Description=Cette macro génère la liste des propriétés de l'objet sélectionné. Liste présentée au format wiki dans la vue du rapport Python.
|Author=Evgeniy
|Date=2021-09
|Version=0.1
|SeeAlso=[Macro Wiki Object Properties List Generator](Macro_Wiki_Object_Properties_List_Generator/fr.md)
}}

## Description

Cette simple macro génère la liste des propriétés de l\'objet sélectionné. La liste des paramètres est imprimée dans la [Vue rapport](Report_view/fr.md) de FreeCAD. Cet exemple est de nature plus pédagogique et n\'est pas applicable pour une utilisation sans édition après génération, puisqu\'il inclut absolument tous les paramètres de l\'objet. Les listes de propriétés qui sont publiées dans ce wiki ne contiennent, en règle générale, que des paramètres uniques. Les paramètres hérités des objets parents ne sont pas publiés.



## Utilisation

-   Préparation :
    -   Copiez le code de la macro de cette page et placez-le dans un nouveau fichier \*.FCMacro.
    -   Enregistrez le fichier FCMacro. Et placez-le dans le dossier Macros de FreeCAD.
    -   Désactiver la case à cocher **Inclure un timecode pour chaque entrée** dans Préférences -\> Général -\> Fenêtre de sortie (onglet).
-   Première utilisation :
    -   Sélectionnez (ou créez et sélectionnez) l\'objet dont vous avez besoin dans l\'arborescence.
    -   Sélectionnez l\'élément Macro -\> Macros\... dans le menu principal.
    -   Dans la fenêtre ouverte, trouvez le fichier \*.FCMacro que vous avez sauvegardé et appuyez sur le bouton **Lancer**.
-   Comment l\'utiliser à nouveau :
    -   Pour exécuter rapidement cette macro à nouveau, vous pouvez utiliser le raccourci clavier **Shift+Ctrl+1** (sous Windows) qui lancera la dernière macro exécutée.

## Recommendations

Ne supprimez pas les espaces entre les lignes. Cela est nécessaire pour simplifier la traduction. Chaque ligne séparée par un espace sera considérée comme une partie distincte pour la traduction. Lorsque vous créez des textes, n\'oubliez jamais que les grands fragments monolithiques de texte sont difficiles à traduire pour les traducteurs.



## Exemples d\'utilisation 

-   Par exemple, ouvrez l\'atelier Arch
-   Créez un objet Structure.
-   Sélectionnez l\'objet Structure créé.
-   Exécutez la macro.
-   Copiez le texte de la vue du rapport et collez-le dans une page wiki et vérifiez le résultat.



## Résultats de l\'utilisation 

Les résultats peuvent ressembler à ceci :

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



## Liens

La discussion sur le forum : <https://forum.freecadweb.org/viewtopic.php?f=21&t=61998>



---
⏵ [documentation index](../README.md) > Macro Wiki Object Properties List Generator Basic Version/fr
