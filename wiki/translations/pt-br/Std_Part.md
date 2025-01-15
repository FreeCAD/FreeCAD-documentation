---
 GuiCommand:  
   Name: Std Part  
   MenuLocation: Nenhum  
   Workbenches: Todas  
   Version: 0.17  
   SeeAlso: Std_Group/pt-br, PartDesign_Body/pt-br  
---

# Std Part/pt-br



## Descrição


**[<img src=images/Std_Part.svg style="width:16px"> [Parte Std](Std_Part/pt-br.md)**

(também chamada internamente de [Parte App](App_Part/pt-br.md)) é um contêiner usado para organizar e agrupar objetos. Ele permite que esses objetos sejam movimentados juntos como uma única unidade na [vista 3D](3D_view/pt-br.md).

O elemento \*\*Parte Std\*\* foi desenvolvido como um bloco básico para criar [montagens](assembly/pt-br.md) mecânicas. Ele é especialmente útil para organizar objetos que possuem uma [Forma Topológica (TopoShape) de Parte](Part_TopoShape/pt-br.md), como [Primitivas de Parte](Part_Primitives/pt-br.md), [Corpos PartDesign](PartDesign_Body/pt-br.md) e outras [Funcionalidades de Parte](Part_Feature/pt-br.md).

A \*\*Parte Std\*\* inclui um [Objeto de Origem](#Origin/pt-br.md) com eixos locais X, Y e Z, além de planos padrão, que podem ser usados como referência para posicionar os objetos contidos. Além disso, é possível aninhar \*\*Partes Std\*\* dentro de outras \*\*Partes Std\*\*, permitindo criar uma montagem maior a partir de submontagens menores.

Embora seja principalmente destinado a corpos sólidos, a \*\*Parte Std\*\* pode ser usada para gerenciar qualquer objeto que possua a propriedade de [Posicionamento](Placement/pt-br.md). Isso significa que ela também pode conter [Elementos de Malha](Mesh_Feature/pt-br.md), [Esboços](Sketch/pt-br.md) e outros objetos derivados da classe [App GeoFeature](App_GeoFeature/pt-br.md).

Não confunda o **[<img src=images/PartDesign_Body.svg style="width:16px"> [Corpo PartDesign](PartDesign_Body/pt-br.md)** com o **[<img src=images/Std_Part.svg style="width:16px"> [Parte Std](Std_Part/pt-br.md)**.

O primeiro é um objeto específico usado na <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Bancada PartDesign](PartDesign_Workbench/pt-br.md), destinado a modelar um [sólido único e contínuo](PartDesign_Body#Single_contiguous_solid/pt-br.md) por meio de [Recursos PartDesign](PartDesign_Feature/pt-br.md). Por outro lado, a \*\*Parte Std\*\* não é utilizada para modelagem, mas sim para organizar diferentes objetos no espaço, com o objetivo de criar [montagens](assembly/pt-br.md).

A ferramenta **[<img src=images/Std_Part.svg style="width:16px"> [Parte Std](Std_Part/pt-br.md)** não é definida por uma bancada específica, mas sim pelo sistema base, portanto, ela está disponível na **barra de ferramentas de estrutura**, que pode ser encontrada em todas as [bancadas de trabalho](Workbenches/pt-br.md).

Para agrupar objetos de forma arbitrária, sem considerar sua posição, use **[<img src=images/Std_Group.svg style="width:16px"> [Grupo Std](Std_Group/pt-br.md)**; este objeto não afeta o posicionamento dos elementos que contém, sendo essencialmente apenas uma pasta usada para manter a [Vista em Árvore](Tree_view/pt-br.md) organizada.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Esquerda: elementos dentro de uma Parte Std na [Vista em Árvore](Tree_view/pt-br.md). Direita: objetos posicionados no espaço, referenciados à Origem da Parte Std.*

## Usage

1.  Press the **[<img src=images/Std_Part.svg style="width:16px"> [Create part](Std_Part.md)** button.
2.  An empty Part is created and automatically becomes *[active](Std_Part#Active_status.md)*.
3.  To add objects to the Part, select them in [Tree view](Tree_view.md), and drag and drop them onto the Part.
4.  To remove objects from the Part, drag them out of the Part, and onto the document label at the top of the [Tree view](Tree_view.md).
5.  Objects can also be added and removed by editing the **Group** property of the Part.

## Notes

-   An object can only belong to a single Part.
-   3D operations like [Part Boolean](Part_Boolean.md) cannot be applied to Parts. For example, you cannot select two Parts, and perform a [Part Fuse](Part_Fuse.md) or [Part Cut](Part_Cut.md).

## Properties

The [Std Part](Std_Part.md), internally called [App Part](App_Part.md) (`App::Part` class), is derived from the [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class) and inherits all its properties. It also has several additional properties. Notably properties that help it manage information in the context of an assembly, for example, **Type**, **Id**, **License**, **LicenseURL** and **Group**.

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Type|String**: a description for this object. By default, it is an empty string {{value|""}}.

-    **Material|Link**: the material for this object.

-    **Meta|Map|Hidden**: map with additional meta information. By default, it is empty {}.

-    **Id|String**: an identification or part number for this object. By default, it is an empty string {{value|""}}.

-    **Uid|UUID|Hidden**: the [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID) (128-bit number) of the object. This is assigned at creation time.

-    **License|String**: a field to specify the license for this object. By default, it is an empty string {{value|""}}.

-    **LicenseURL|String**: a field to specify the web address to the license or contract for this object. By default, it is an empty string {{value|""}}.

-    **Color|Color**: a tuple of four floating point RGBA values white color.

-    **Placement|Placement**: the position of the object in the [3D view](3D_view.md). The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

    -   
        **Angle**
        
        : the angle of rotation around the **Axis**. By default, it is {{value|0°}} (zero degrees).

    -   
        **Axis**
        
        : the unit vector that defines the axis of rotation for the placement. Each component is a floating point value between {{value|0}} and {{value|1}}. If any value is above {{value|1}}, the vector is normalized so that the magnitude of the vector is {{value|1}}. By default, it is the positive Z axis, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : a vector with the 3D coordinates of the base point. By default, it is the origin {{value|(0, 0, 0)}}.

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

-    **Origin|Link|Hidden**: the [App Origin](App_OriginGroupExtension.md) object that is the positional reference for all elements listed in **Group**.

-    **Group|LinkList**: a list of referenced objects. By default, it is empty {{value|[]}}.

-    **_ Group Touched|Bool|Hidden**: whether the group is touched or not.

### View


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

## Detailed explanation 

### Active status 

An open document can contain multiple Parts. But only one Part can be active. The active Part is displayed in the [tree view](Tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). It will also be shown with bold text.

To activate or de-activate a Part:

-   Double click on it on the [Tree view](Tree_view.md), or
-   Open the context menu (right click) and select **Active object**.

![](images/Std_Part_active.png )



*Document with two Std Parts, of which the second one is active.*

### Origin

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Left: Part Origin in the [Tree view](Tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


**Note:**

the Origin is an [App Origin](App_OriginGroupExtension.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Part are referenced to the Part\'s Origin which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.

### Visibility Management 

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`. If the Part is visible, then each object\'s **Visibility** determines whether the object is shown or not.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*The visibility of the Std Part determines whether the objects grouped under it are shown in the [3D view](3D_view.md) or not. Left: the Part is hidden, so none of the objects will be shown in the [3D view](3D_view.md). Right: the Part is visible, so each object controls its own visibility.*

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Part ([App Part](App_Part.md)) is created with the `addObject()` method of the document. Once a Part exists, other objects can be added to it with the `addObject()` or `addObjects()` methods.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

You cannot create a scripted `App::Part`. However, you can add `App::Part` behavior to a scripted `Part::FeaturePython` object by using the following code:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def dumps(self):
        return

    def loads(self, _state):
        return

    def attach(self, obj):
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

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
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def dumps(self):
        return None

    def loads(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             MyGroup(),
                             ViewProviderMyGroup(),
                             True)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std Part/pt-br
