---
- GuiCommand:/es
   Name:Std Part
   Name/es:Std Pieza
   MenuLocation:Ninguna
   Workbenches:Todos
   Version:0.17
   SeeAlso:[Std Grupo](Std_Group/es.md), [Cuerpo PartDesign](PartDesign_Body/es.md)
---


</div>

## Descripción


<div class="mw-translate-fuzzy">

**Parte** es un contenedor de propósito general que mantiene juntos un grupo de objetos para que puedan moverse como una unidad. La parte puede contener la mayoría de los objetos de FreeCAD, como conjuntos de PartDesign, objetos del ambiente de trabajo de Pieza, objetos de malla, etc.


</div>


<div class="mw-translate-fuzzy">

Part proporciona un sistema de coordenadas local al que se pueden adjuntar sketches y otros objetos.


</div>

Although it is primarily intended for solid bodies, the Std Part can be used to manage any object that has a [Placement](Placement.md) property, so it can also contain [Mesh Features](Mesh_Feature.md), [sketches](Sketch.md), and other objects derived from the [App GeoFeature](App_GeoFeature.md) class.


<div class="mw-translate-fuzzy">

Part se encuentra en la barra de herramientas Estructura que se muestra en todos los ambientes de trabajo.


</div>

The **<img src=images/Std_Part.svg style="width:16px"> <img src=images/Std_Group.svg style="width:Std Part](Std_Part.md)** tool is not defined by a particular workbench, but by the base system, thus it is found in the {{MenuCommand|structure toolbar}} that is available in all [workbenches](Workbenches.md). To group objects arbitrarily without considering their position, use **[16px"> [Std Group](Std_Group.md)**; this object does not affect the placements of the elements that it contains, it is essentially just a folder that is used to keep the [tree view](tree_view.md) organized.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )


*Left: elements inside a Std Part in the [tree view](tree_view.md). Right: objects positioned in space, referred to the Origin of the Std Part.*


<div class="mw-translate-fuzzy">

## Como utilizar {#como_utilizar}


</div>


<div class="mw-translate-fuzzy">

-   Presione el botón {{KEY | <img src="images/_Std_Part.png_" width= 24px> '''Create part'''}} en la barra de herramientas. La Part se activa automáticamente.
-   Haga doble clic en la Part en el árbol del Modelo para activarlo o desactivarlo.
-   Para agregar objetos a una Part, arrástrelos y suéltelos sobre la Part en el árbol del Modelo.
-   Para eliminar objetos de una Part, arrástrelos y suéltelos de la Part y en la etiqueta del documento en la parte superior del árbol del modelo.


</div>

### Notes

-   As of v0.19, a given object can only belong to a single Part.
-   Double-click the Part in the [tree view](tree_view.md) or open the context menu (right-click) and select {{MenuCommand|Toggle active part}} to activate or deactivate the Part. If another Part is active, it will be deactivated. See [active status](Std_Part#Active_status.md) for more information.


<div class="mw-translate-fuzzy">

## Limitaciones


</div>


<div class="mw-translate-fuzzy">

-   Incluso cuando una Part está activa, los objetos recién creados no se colocan dentro de la Part, sino en la parte inferior del árbol. Simplemente arrástrelos y suéltelos sobre la Part.
-   Una part no tiene forma. Por lo tanto, no es posible aplicar la mayoría de las operaciones 3D en una Part, como Part Booleans.
-   En este momento, [ Draft Snap](Draft_Snap.md) no funciona en contenedores de Part seleccionados o en objetos dentro de un contenedor de Part.
-   \'\' Nota del Redactor: en este momento, no está claro si el estado activo de la Part cumple un propósito \'\'.


</div>

## Propiedades

A [Std Part](Std_Part.md) is internally called [App Part](App_Part.md) (`App::Part` class), and is derived from an [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), therefore it shares most of the latter\'s properties.

In addition to the properties described in [App GeoFeature](App_GeoFeature.md), the App Part class has some properties that help it manage information in the context of an assembly, for example, **Type**, **Id**, **License**, **LicenseURL**, **Color**, and **Group**.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the {{MenuCommand|Show all}} command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Id}}: ID (Número de pieza) del artículo. Este campo es opcional.

-    {{PropertyData | License}}: la licencia bajo la cual se lanza la Part.

-    {{PropertyData | License URL}}: la dirección web donde se pueden encontrar los términos de licencia.

-    {{PropertyData | Placement}}: especifica la orientación y la posición de la Part en el espacio 3D. Ver [Placement](Placement.md).

-    {{PropertyData | Label}}: la label/etiqueta es el nombre dado a la operación. Este nombre se puede cambiar a su conveniencia.

-    {{PropertyData | Group}}: enumera los objetos a los que se hace referencia.


</div>

#### Hidden properties Data {#hidden_properties_data}

-    **Material|Map**: map with material properties. By default, it is empty {}.

-    **Meta|Map**: map with additional meta information. By default, it is empty {}.

-    **Uid|UUID**: the [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (128-bit number) of the object. This is assigned at creation time.

-    **Label2|String**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool**: whether to display the object or not.

-    **Origin|Link**: the [App Origin](App_Origin.md) object that is the positional reference for all elements listed in **Group**.

-    **_ Group Touched|Bool**: whether the group is touched or not.

### View

The App Part only has the five properties of the basic [App FeaturePython](App_FeaturePython.md), and it does not have hidden properties.


{{TitleProperty|Base}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [tree view](tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


<div class="mw-translate-fuzzy">

### Ejemplos de uso {#ejemplos_de_uso}

-   Como un contenedor de ensamblaje que agrupa los objetos que se fabricarán por separado, luego se pegarán o atornillarán, como una mesa de madera.
-   Al importar un STEP ensamblado en FreeCAD, el ensamblaje principal y sus subconjuntos son contenedores Part.
-   Una Part que se compone de múltiples componentes no fusionados, como un cojinete de bolas.


</div>

The Std Part is intended to be the basic building block to create assemblies. Unlike a [PartDesign Body](PartDesign_Body.md), an assembly is meant to be a collection of separate, distinguishable elements which are connected in some way in the physical world, for example, through pressure, screws, or glue.

Examples that could be Parts:

-   A wooden table that consists of individual wooden pieces (legs, top), which are put together by glue or metal screws.
-   A ball bearing that is composed of multiple steel balls, an inner ring, a retainer, a seal, and an outer ring.
-   An assembly of a screw with a washer, and a matching nut.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Left: three individual contiguous solids, each of them modelled by a [PartDesign Body](PartDesign_Body.md). Right: the individual Bodies put together inside a Std Part to create an assembly.*

In general terms, when importing a STEP file into the program, the main assembly and its sub-assemblies will be imported as Part containers, each of them containing a simple [Part Feature](Part_Feature.md).

## Detailed explanation {#detailed_explanation}


<div class="mw-translate-fuzzy">

### Estado activo {#estado_activo}

Un documento de FreeCAD puede contener varias Part. Solo una Part puede estar activa a la vez. Una Part activa se mostrará en el árbol con un color de fondo azul claro.


</div>

An open document can contain multiple Parts. An active Part will be displayed in the [tree view](Tree_view.md) with the background color specified by the {{MenuCommand|Active container}} value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). An active part will also be shown in bold text.

To activate or de-activate a Part:

-   Double click on it on the [tree view](Tree_view.md), or
-   Open the context menu (right click) and select {{MenuCommand|Toggle active part}}.


**Notes:**

-   The {{emphasis|active status}} of Parts was developed in v0.17 in parallel with the {{emphasis|active status}} of [PartDesign Bodies](PartDesign_Body.md); however, as of v0.19 this status does not serve a real purpose for Parts.
-   Even when a Part is active, newly created objects are not placed inside of it automatically. In this case, simply drag these new objects, and drop them onto the desired Part.
-   Only a single Part can be active at a time.

![](images/Std_Part_active.png )


*Document with two Std Parts, of which the second one is active.*


<div class="mw-translate-fuzzy">

### Origen

The Origin consta de los tres ejes estándar (X, Y, Z) y tres planos estándar (XY, XZ y YZ). Sketches se pueden unir a estos planos. Todos los elementos dentro de la Part están referenciados al Origen de la Part; lo que significa que la Part se puede mover y rotar en referencia al sistema de coordenadas global sin afectar la ubicación de los elementos en su interior.


</div>

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )


*Left: Part Origin in the [tree view](tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


**Note:**

the Origin is an [App Origin](App_Origin.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Part are referenced to the Part\'s Origin which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.


<div class="mw-translate-fuzzy">

### Gestión de visibilidad {#gestión_de_visibilidad}

La visibilidad de la Part reemplaza la visibilidad de cualquier objeto que contenga. Si la Part está oculta, los objetos que contiene también estarán ocultos, incluso si su visibilidad está establecida en verdadero. Múltiples objetos dentro de una Part pueden ser visibles a la vez.


</div>

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`. If the Part is visible, then each object\'s **Visibility** determines whether the object is shown or not.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) *The visibility of the Std Part determines whether the objects grouped under it are shown in the [3D view](3D_view.md) or not. Left: the Part is hidden, so none of the objects will be shown in the [3D view](3D_view.md). Right: the Part is visible, so each object controls its own visibility.*

### Inheritance

A [Std Part](Std_Part.md) is formally an instance of the class `App::Part`, whose parent is the basic [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), and is augmented with an Origin extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::Part* class is a simple container that has a position in 3D space, and has an Origin to control the placement of the objects grouped under it.`

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Part ([App Part](App_Part.md)) is created with the `addObject()` method of the document. Once a Part exists, other objects can be added to it with the `addObject()` or `addObjects()` methods of this Part.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

You cannot create a scripted `App::Part`. However, you can add `App::Part` behaviour to a scripted `Part::FeaturePython` object by using the following code:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}  
