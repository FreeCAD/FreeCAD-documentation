# Property editor/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

## Prezentare generală 

Editorul proprietății este unul dintre cele mai importante instrumente ale FreeCAD și un element principal în timpul colaborării cu FreeCAD. Editorul proprietății permite gestionarea proprietăților obiectelor din document.


</div>

The [property editor](property_editor.md) appears when the **Model** tab of the [combo view](combo_view.md) is active in the [interface](interface.md); it allows managing the publicly exposed properties of the objects in the document.


<div class="mw-translate-fuzzy">

În general, editorul de proprietăți este destinat să se ocupe de un singur obiect la un moment dat. Valorile afișate în Editorul de proprietăți aparțin obiectului activ al documentului dvs. activ (aveți grijă ce document este activ, dacă lucrați la mai multe documente). Dacă nu ați selectat niciun element (sau nu există elemente), editorul proprietății va fi gol.


</div>


<div class="mw-translate-fuzzy">

Nu toate proprietățile pot fi modificate în orice moment. În funcție de starea specifică, unele proprietăți vor fi afișate ca fiind numai pentru citire.


</div>


{{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Empty property editor, when no object is selected.*


<div class="mw-translate-fuzzy">

## Property definition 

A **property** is a piece of information like a number or a text string that is attached to a FreeCAD document or an object in a document. Properties can be viewed and modified with the [Property editor](Property_editor.md).


</div>

A property is a piece of information like a number or a text string that is attached to a FreeCAD document or an object in the document.


<div class="mw-translate-fuzzy">

Obiecte personalizate [scripted objects](scripted_objects.md) în FreeCAD pot avea proprietăți ale următoarelor tipuri   *


</div>

Some of the most commonly used property types are   * 
```python
App   *   *PropertyBool
App   *   *PropertyFloat
App   *   *PropertyAngle
App   *   *PropertyDistance
App   *   *PropertyInteger
App   *   *PropertyString
App   *   *PropertyMatrix
App   *   *PropertyVector
App   *   *PropertyPlacement
```


<div class="mw-translate-fuzzy">

Obiectele diferite pot avea proprietăți diferite. Cu toate acestea, unele proprietăți sunt comune printre toate obiectele, de exemplu poziția și rotirea unui obiect sunt Proprietăți de date care pot fi manipulate.


</div>

## View and Data properties 


<div class="mw-translate-fuzzy">

Există două tipuri de proprietăți ale funcțiilor accesibile prin tab-urile din partea de jos a editorului de proprietăți   *    * {{PropertyView | View}}   * proprietăți legate de afișarea \"vizuală\" a unui obiect.    * {{PropertyData | Data}}   * proprietăți legate de parametrii \"fizici\" ai unui obiect.


</div>

For this reason, **Data** properties are considered to be more \"real\", as they truly define the geometry of a shape. On the other hand, **View** properties are less important because they only affect the superficial appearance of the geometry. For example, a circle of 10 mm radius is different from a circle of 5 mm radius; the color of the circle (view property) doesn\'t affect its shape, but the radius does (data property). In many instances in this documentation, the word \"property\" is understood to refer to a \"Data property\" and not to a \"View property\".

### Basic properties 


**See also   * [Object name](Object_name.md)**

The most basic [scripted object](scripted_objects.md) won\'t show any **Data** property in the property editor, except for its `Label` attribute. The `Label` is a user editable string that identifies the object in the [tree view](tree_view.md). On the other hand, the `Name` attribute of an object is assigned at the moment of its creation and cannot be changed; this attribute is read-only, and is not displayed in the property editor either.

A basic parametric object is created as follow


```python
obj = App.ActiveDocument.addObject("App   *   *FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width   *" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width   *" height="264px;">



*View and Data tabs of the property editor, for a basic "App   *   *FeaturePython" scripted object.*

Most geometrical objects that can be created and displayed in the [3D view](3D_view.md) are derived from a `Part   *   *Feature`. See [Part Feature](Part_Feature.md) for the most basic properties that these objects have.

For 2D geometry, most objects are derived from `Part   *   *Part2DObject` (itself derived from `Part   *   *Feature`) which is the base of [Sketches](Sketch.md), and most [Draft elements](Draft_Workbench.md). See [Part Part2DObject](Part_Part2DObject.md) for the most basic properties that these objects have.

## Actions


<small>(v0.19)</small> 

Right clicking in an empty space of the view, or with a property selected, shows only one command   *

-    **Show all**   * if active, in addition to the standard properties that appear already, it shows all the hidden Data and View properties in their respective tabs.

    -   Data   * \"Proxy\", \"Label2\", \"Expression Engine\", and \"Visibility\".
    -   View   * \"Proxy\".

When the **Show all** option is active, and one property is selected, more actions are available with a second right click   *

-    **Show all**   * deactivates the **Show all** command, hiding the additional Data and View properties.

-    **Add Property**   * adds a dynamic property to the object; this works with both C++ defined objects, and Python [scripted objects](scripted_objects.md).

-    **Expression...**   * brings up the formula editor, which allows using [expressions](Expressions.md) in the property value.

-    **Hidden**   * if active, sets the property as hidden, meaning that it will only be displayed in the property editor if **Show all** is active.

-    **Output**   * if active, sets the property as output.

-    **NoRecompute**   * if active, sets the property as not recomputed when the document is recomputed; this is useful when a property should be kept unaffected by other updates.

-    **ReadOnly**   * if active, sets the property to be read-only; it won\'t be editable in the property editor any more until this switch is turned off. The **Expression...** menu entry is no longer available. **Note   *** It may be still possible to change the property via a dialog that updates the property.

-    **Transient**   * if active, sets the property as transient. The value of a transient property is not saved to file. When opening a file, it is instantiated with its default value.

-    **Touched**   * if active, it becomes touched, and ready for recompute.

-    **EvalOnRestore**   * if active, it is evaluated when the document is restored.


<div class="mw-translate-fuzzy">

## Exemplu de proprietăți obiecte Piese 

### Proprietăți


</div>

In this section we show some common properties that are visible for a [PartDesign Body](PartDesign_Body.md), and one [PartDesign Feature](PartDesign_Feature.md). The specific properties of an object can found in the specific documentation page of that object.

### Vizualizare

Most of these properties are inherited from the [Part Feature](Part_Feature.md) basic object.


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Properties_View.png  style="width   *490px;"> {{TitleProperty|Base}}


</div>


<div class="mw-translate-fuzzy">

-    {{PropertyView/ro|Bounding Box}}   * Indică dacă trebuie afișată o casetă care să arate întinderea globală a obiectului. Valoare False sau True (Implicit, Fals).

-    {{PropertyView/ro|Point Control}}   * Indică dacă punctele de control ale elementelor trebuie afișate. Valoare False sau True (Implicit, Fals).

-    {{PropertyView/ro|Deviation}}   * Setează precizia reprezentării poligoanelor modelului în vederea 3D (mozaicare/tessellation). Valori mai mici = o calitate mai bună. Valoarea este în procente din mărimea obiectului (deviația în mm = (w + h + d) /3

-   valueInPercent / 100, unde w, h, d sunt dimensiunile casetei delimitate).

-    {{PropertyView/ro|Display Mode}}   * Modul de afișare al caracteristicii, **Flat lines, Shaded, Wireframe, Points** [96px](IMAGE   *_Vue_DisplayModePartDesign_fr_00.png.md). (Implicit, **Linii plate**).

-    {{PropertyView/ro|Lighting}}   * Iluminare **O parte, Două laturi** [96px](IMAGE   *Vue_Lighting_fr_00.png.md). (Default, **Two side**).

-    {{PropertyView/ro|Line Color}}   * Oferă culoarea liniei (margini) (Implicit, **25, 25, 25**).

* {{PropertyView/ro|Line Width}}   * Dă grosimea liniei (marginii) (Implicit, **2**).
* {{PropertyView/ro|Point Color}}   * Oferă culoarea punctelor (capetele caracteristicii) (Implicit, **25, 25, 25**). 

-    {{PropertyView/ro|Point Size}}   * Oferă dimensiunea punctelor (Implicit, **2**).

* {{PropertyView/ro|Selectable}}   * Permite selectarea caracteristicii. Valoare False, True (implicită, True). 

-    {{PropertyView/ro|Shape Color}}   * Dați culoarea formei (implicit, \'\' \'204, 204, 204\' \'\').

-    {{PropertyView/ro|Transparency}}   * Setează gradul de transparență în caracteristica de la **0** la \'\'\' 100 **(Implicit,** 0 \'\'\').

* {{PropertyView/ro|Visibility}}   * Determină vizibilitatea funcționalității (de exemplu, bara **SPACE**). Valoare False sau True (Implicit, True). 


</div>

### Data

In this case we observe the properties of the [PartDesign Revolution](PartDesign_Revolution.md) feature.


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_Properties_Data.png  style="width   *490px;"> {{TitleProperty|Base}}


</div>


<div class="mw-translate-fuzzy">


{{PropertyData/ro|Label}}

   * Eticheta este numele dat obiectului (funcționalității), acest nume poate fi schimbat ulterior.


</div>


{{TitleProperty|Part Design}}

-    **Refine**   * whether to refine the fusion done with other objects.


<div class="mw-translate-fuzzy">


{{PropertyData/ro|Placement}}

   * Rezumatul datelor de mai jos. Fiecare caracteristică are o destinație de plasare care poate fi controlată prin tabelul Proprietăți date. Controlează amplasarea piesei în raport cu sistemul de coordonate. NOTĂ   * Proprietățile de plasare nu afectează dimensiunile fizice ale elementului, ci doar poziția sa în spațiu!
If you select the title **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width   *256px;">, a button with **three small points** appears to the right. Clicking this button ** '''...'''**, opens the **[Tasks\_Placement](Tasks_Placement.md)** options window.


</div>


<div class="mw-translate-fuzzy">


{{PropertyData/ro|Axis}}

   * Această proprietate specifică axa/axele după care se rotește funcționalitatea/obiectul. Valoarea exactă a rotației provine de la funcția unghiului (deasupra). Această proprietate are trei argumente, care sunt trecute ca numere în casetele x, y și z din instrument. Stabilirea unei valori pentru mai multe axe va determina rotirea piesei în fiecare axă, prin valoarea unghiului înmulțită cu valoarea pentru axă. De exemplu, cu un unghi de 15 °, setarea unei valori de 1,0 pentru x și 2,0 pentru y va determina rotirea piesei finite cu 15 ° în axa x și 30 ° în axa y.


</div>


<div class="mw-translate-fuzzy">


{{PropertyData/ro|Angle}}

   * Specifică unghiul care va utilizat cu funcția [axis](#Axis.md) (de mai jos). Un unghi este setat aici, iar axa pe care unghiul acționează este stabilită cu proprietatea axei. Funcționalitatea este rotită cu unghiul specificat, în jurul axei specificate. Un exemplu de utilizare ar putea fi dacă ați creat o caracteristică de revoluție după cum este necesar, dar a trebuit apoi să rotiți întreaga caracteristică cu o anumită sumă, pentru a permite o aliniere cu o altă caracteristică pre-existentă.


</div>


{{TitleProperty|Sketch Based}}


<div class="mw-translate-fuzzy">


{{PropertyData/ro|Position}}

   * Această proprietate specifică punctul de bază la care se referă toate dimensiunile. Acest lucru necesită trei argumente, care sunt transmise ca numere în casetele x, y și z din instrument. Stabilirea unei valori pentru mai mult de una dintre casete va face ca piesa să fie translatată cu un număr de unități de-a lungul axei corespunzătoare.


</div>




## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

See [scripted objects](scripted_objects.md) for the full information on adding properties to objects defined through [Python](Python.md).

Most properties that are visible in the property editor can be accessed from the [Python console](Python_console.md). These properties are just attributes of the class that defines the selected object. For example, if the property editor shows the **Group** property, this means that the object has the `Group` attribute. 
```python
print(obj.Group)
```

These attributes (properties) are added with the `addProperty` method of the base object. At least it is necessary to specify the type of [property](property.md), and its name. 
```python
obj.addProperty("App   *   *PropertyFloat", "Custom")
print(obj.Custom)
```

Properties follow the `CapitalCamelCase` or `PascalCase` convention, meaning that each word starts with a capital letter, and there are no underscores. When the property editor displays such names, it leaves a space between each capital letter, making it easier to read.


```python
obj.addProperty("App   *   *PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Property editor showing the Data properties of a [PartDesign Body](PartDesign_Body.md), with two additional properties, "Custom" and "Custom Camel Property".*

In similar way the **View** properties are added, not to the base object, but to its `ViewObject`. Then, it follows that properties like **Angular Deflection**, **Bounding Box**, **Display Mode**, **Display Mode Body**, **Line Color**, and others, can be examined and changed from the [Python console](Python_console.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

All public properties of the object, and of its view provider, are contained in the corresponding `PropertiesList` attribute. 
```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```


<div class="mw-translate-fuzzy">


{{docnav/ro
|[Interface Customization](Interface_Customization/ro.md)
|[Workbenches](Workbenches/ro.md)
}}


</div>


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Property editor/ro
