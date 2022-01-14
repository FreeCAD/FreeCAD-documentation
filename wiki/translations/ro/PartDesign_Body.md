---
- GuiCommand:/ro
   Name:PartDesign Body
   Name/ro:PartDesign Body
   Icon:PartDesign_Body_Create_New.svg
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Create body
   Version:0.17
   SeeAlso:[Std Piesă](Std_Part/ro.md)
---

# PartDesign Body/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**PartDesign Body** conține o serie de schițe, date și PartDesign [features](Glossary#Feature.md) care formează un solid unic contiguu. Acesta oferă o Origine (cu planuri și axe standard) care pot fi utilizate de către funcții ca referințe. În plus, poate fi mișcat liber ca un întreg fără a face necesară mutarea funcțiilor individuale.


</div>

The Body provides an **Origin** object which includes local X, Y, and Z axes, and standard planes. These elements can be used as references to attach [sketches](Sketch.md) and [primitive objects](PartDesign_CompPrimitiveAdditive.md).

Do not confuse the <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) with the <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part.md). The first one is a specific object used in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), intended to model a [single contiguous solid](PartDesign_Body#Single_contiguous_solid.md) by means of [PartDesign Features](PartDesign_Feature.md). The [Std Part](Std_Part.md) is a grouping object intended to create [assemblies](assembly.md); it is not used for modelling, just to arrange different objects in space. Multiple bodies, and other [Std Parts](Std_Part.md), can be placed inside a single [Std Part](Std_Part.md) to create a complex assembly.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*Left: the tree view showing the features that sequentially produce the final shape of the object. Right: the final object visible in the [3D view](3D_view.md).*

## Cum se folosește 

If no previous solid is selected:

1.  Press the **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)** button. An empty Body is created and automatically becomes **[active](PartDesign_Body#Active_status.md)**.
2.  Now you can press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)** to create a [sketch](Sketch.md) in the Body that can be used with **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Pad](PartDesign_Pad.md)**.
3.  Alternatively, add a primitive [PartDesign Feature](PartDesign_Feature.md), for example, **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Additive box](PartDesign_AdditiveBox.md)**.

If a solid object is selected:

1.  Press the **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)** button. A new Body is created containing a single **Base Feature**. This Base Feature element is a simple reference to another object previously created or imported into the document. See [Base Feature](PartDesign_Body#Base_Feature.md) for more information. An existing Body or [PartDesign Feature](PartDesign_Feature.md) cannot be selected when pressing **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)**.

### Notes

-   If no Body currently exists when **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)** is pressed, a new Body will be automatically created. If a Body already exists, it has to be made active before using **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**.
-   Double-click the Body in the [tree view](tree_view.md) or open the context menu (right-click) and select **Toggle active body** to activate or deactivate the Body. If another Body is active, it will be deactivated. See [active status](PartDesign_Body#Active_status.md) for more information.

## Proprietăți

A [PartDesign Body](PartDesign_Body.md) (`PartDesign::Body` class) is derived from a [Part Feature](Part_Feature.md) (`Part::Feature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the PartDesign Body has the following properties in the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Tip|Link**: the [PartDesign Feature](PartDesign_Feature.md) defined as \"Tip\", which is usually the last feature created in the Body. The Tip indicates the final shape of the Body, which is shown in the [3D view](3D_view.md) when **Display Mode Body** is set to `Tip`. See [Tip](PartDesign_Body#Tip.md) for more information.

-    **Base Feature|Link**: an external shape used as the first [PartDesign Feature](PartDesign_Feature.md) in the Body. It is usually set when dragging a solid object into an empty Body. If no solid is imported in this way, this property will be empty. See [Base Feature](PartDesign_Body#Base_Feature.md) for more information.

-    **Placement|Placement**: the position of the object in the [3D view](3D_view.md). The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

-    **Group|LinkList**: a list with the [PartDesign Features](PartDesign_Feature.md) in the Body.

#### Hidden properties Data 

-    **Origin|Link**: the [App Origin](App_Origin.md) object that is the positional reference for all elements listed in **Group**.

-    **_ Group Touched|Bool**: whether the group is touched or not.

Also the hidden properties described in [Part Feature](Part_Feature.md).

### View


<div class="mw-translate-fuzzy">

-    **Display Mode Body**: definește afișarea între două modalități:

    -   *Through* (implicit) expune orice în interiorul corpului (features, datums, sketches, etc.). este mocalitatea utilizată în funcții aditive și editarea funcțiilor aflate în interiorul corpului .
    -   *Tip* expune numai forma corpului în sine, conform Funcției Rezultante/Tip stabilite; orice altceva, inclusiv schițele, sunt ascunse vederii și nu pot fi afișate. Utilizare practică: \"Tip\" permite selectarea muchiilor și a fețelor corpului pentru a crea operațiuni de la alte Ateliere de lucru/Workbenches.

-    **Tip**: afișează/setează funcția definită ca tip.

-    **Base Feature**: afișează/setează forma externă utilizată ca funcție de bază. Nu se aplică dacă funcția PartDesign este funcția de bază.

-    **Placement**: specifică orientarea și poziția corpului în spațiul 3D. A se vedea [Placement](Placement.md).

-    **Label**: eticheta este numele dat de operație. Acest nume poate fi schimbat dacă vă este la îndemână.

-    **Group**: listează obiectele referențiate în interiorul Corpului .


</div>

-    **Display Mode Body|Enumeration**: sets the display mode specifically for the Body with one of two types.

    -   
        `Through`
        
        (default) exposes all objects inside the Body, that is, [sketches](Sketch.md), [PartDesign Features](PartDesign_Feature.md), datum objects, etc. This mode allows visualizing partial operations done inside the Body, and thus it is the recommended mode when adding and editing features. Select the specific feature, and the set **Visibility** to `True` or press the **Space** bar on the keyboard.

    -   
        `Tip`
        
        exposes only the final shape of the Body, which is defined by the **Tip** property. Everything else, including [sketches](Sketch.md), [partial features](PartDesign_Feature.md), datums, etc., is not displayed, even if they are visible in the [tree view](tree_view.md). This mode is recommended when the Body does not need to be modified further, so a fixed shape is shown. This mode is also recommended when you wish to select the sub-elements (vertices, edges, and faces) of the final shape to use with other workbenches\' tools.

## Body concept 

### Single contiguous solid 

A PartDesign Body is intended to model a single contiguous solid. The meaning of \"contiguous\" is an element made in one piece, with no moving parts, or disconnected solids. Examples of contiguous solids are those that are manufactured from a single piece of raw material by a process of casting, cutting, or milling. For example, a nut, a washer, and a bolt each consists of a single solid piece of steel with no moving parts, so each can be modelled by a PartDesign Body. Objects that are created by welding two pieces can also be modelled by a single Body as long as the weld joint is not intended to break apart.

Once these contiguous solids are put together in some type of arrangement, then they become an \"assembly\". In an assembly, the objects are not fused together, but they are simply \"stacked\" or placed next to each other, and remain individual parts.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Left: three individual contiguous solids, each of them modelled by a PartDesign Body. Right: the individual Bodies put together in an assembly.*

### Feature editing 

A PartDesign Body is intended to work by creating an initial solid, either from a [sketch](Sketch.md) or from a [primitive shape](PartDesign_CompPrimitiveAdditive.md), and then modifying it through [\"features\"](PartDesign_Feature.md) to add or remove material from the previous shape. For a full explanation go to [feature editing](feature_editing.md).

A PartDesign Body will perform an automatic [fusion](Part_Fuse.md) (union) of the solid elements inside of it. This means that (1) partial solids should be touching when created, and (2) disconnected solids are not allowed.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*Left: two individual solids that intersect each other. Right: a single PartDesign Body with two [additive features](PartDesign_Feature.md); they are automatically fused together, so instead of intersecting, they form a single contiguous solid.*

![](images/PartDesign_Body_non-contiguous.png ) 
*Left: two disconnected solids; this isn't a valid PartDesign Body. Right: two touching solids; this results in a valid PartDesign Body. The newer [feature](PartDesign_Feature.md) should always contact or intersect the previous feature so that it is fused to it, and becomes a single contiguous solid.*


**Note:**

other CAD programs like Catia allow discontiguous solids in the same \"Body\". As of v0.19, FreeCAD does not allow this. There has been discussions in the [FreeCAD forum](https://forum.freecadweb.org/index.php) about lifting this restriction but no concrete decision has been made. If you\'d like to know more or present different points of view, please discuss in the [forum](https://forum.freecadweb.org/index.php).

## Detailed explanation of the properties 


<div class="mw-translate-fuzzy">

### Active Status 

Un document FreeCAD poate conține mai multe entități. Prin urmare, pentru a adăuga o funcție nouă unui anumit Corp, trebuie făcută activ. Un corp activ va fi afișat în arborescență cu o culoare de fundal albastru deschis. În v0.18, este numit ca fiind arborescența Model și va fi afișat și cu caractere aldine.


</div>

An open document can contain multiple Bodies. To add a new feature to a specific Body, it needs to be made **active**. An active body will be displayed in the [tree view](tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). An active body will also be shown in bold text.

To activate or de-activate a Body:

-   Double click on it on the [tree view](tree_view.md), or
-   Open the context menu (right click) and select **Toggle active body**.


<div class="mw-translate-fuzzy">

Activarea unui Corp, de asemenea, comută automat interfața la Atelierul de lucru PartDesign, dacă nu era deja Atelierul de lucru activ.


</div>

![](images/PartDesign_Body_active.png )



*Document with two PartDesign Bodies, of which the second one is active.*


<div class="mw-translate-fuzzy">

### Originea

Originea este formată din cele trei axe standard (X, Y, Z) și trei planuri standard (XY, XZ și YZ). Sketches can be attached to these planes, and planes along with axes can be used to create other datum (reference) geometry. Toate elementele din interiorul Corpului se referă la Originea Corpului; ceea ce înseamnă că corpul poate fi mișcat și rotit în raport cu sistemul global de coordonate fără a afecta amplasarea elementelor în interiorul corpului.


</div>

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

1.  Create the Body.
2.  If the Body is selected in the [tree view](tree_view.md), press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**; the [task panel](task_panel.md) will open to allow selecting one of the planes.
3.  If the Body is not selected, select the Origin instead and make it visible in the [3D view](3D_view.md) by pressing the **Space** bar in the keyboard. Also expand the Origin object to see the axes and planes.
4.  Select one of the planes, either in the [tree view](tree_view.md) or in the [3D view](3D_view.md), then press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**. The sketch will be created on the chosen plane.

The same process can be used when creating auxiliary datum geometry like [PartDesign Lines](PartDesign_Line.md), [PartDesign Planes](PartDesign_Plane.md), and [PartDesign CoordinateSystems](PartDesign_CoordinateSystem.md).


**Note:**

the Origin is an [App Origin](App_Origin.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Body are referenced to the Body\'s Origin which means that the Body can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*Left: PartDesign Body Origin in the [tree view](tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


<div class="mw-translate-fuzzy">

### Funcție de bază 

Funcția de bază este prima funcție a PartDesign creată în Corp. Dar este posibil să se utilizeze o formă solidă, fie importată, fie modelată în alte Ateliere de lucru, ca element de bază la care se pot adăuga schițe și alte funcții(onalități).


</div>

The Base Feature is the first [PartDesign Feature](PartDesign_Feature.md) in the Body when the Body is based on another solid shape. This solid can be created by any workbench, or imported from an external file, for example, a STEP file.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*PartDesign Bodies, each of them with a single Base Feature, which are taken from previously created solids.*

To create the Base Feature:

1.  select a solid shape external to any Body, and
2.  press **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**; this will create a new Body with a single Base Feature.


**Note:**

you can\'t select an existing Body, or any of its [features](PartDesign_Feature.md), when pressing **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**.

If you already have a Body, you can create the Base Feature in this way:

-   in the [tree view](tree_view.md), pick an object, and drag and drop it inside the Body, or
-   in the [property editor](property_editor.md), edit the value of **Base Feature** by pressing the ellipsis **...**, and choosing an object from the list. In this case you can choose an existing Body to be the Base Feature.


**Note:**

dragging and dropping only works for Bodies which don\'t have a Base Feature already.


**Note 2:**

if the Body already has several features, when you drag and drop the external solid, the Base Feature will be created at the beginning of the list of features, that is, it will be added to the beginning of the **Group** property.

The Base Feature is entirely optional; it is only present when including an object from outside the Body. If no external solid is included, you can still build your shape using [sketches](Sketch.md), [pads](PartDesign_Pad.md), [primitive objects](PartDesign_CompPrimitiveAdditive.md), and other [PartDesign Features](PartDesign_Feature.md). In this case the **Base Feature** property remains empty.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*Left: PartDesign Body with a Base Feature that is taken from an external solid object, and many subsequent [PartDesign Features](PartDesign_Feature.md) on top. Right: Body which doesn't have an explicit Base Feature.*


<div class="mw-translate-fuzzy">

### Funcția Rezultantă/Vărf 

Funcția rezultată este cea care este expusă în afara modelului(ceea ce se vede). Aceasta este automat ultima funcție din partea de jos a arborescenței. Dar, uneori, ar putea fi util să o înlocuiți cu o funcție anterioară în arborescența Corpului, cu efectul de a reveni în istoria sa; este posibil să adăugați funcții care ar fi trebuit adăugate anterior. În arborescența corpului Corpului, funcția rezultată poartă un punct verde cu o săgeată albă pe interior.


</div>

The Tip is the [PartDesign Feature](PartDesign_Feature.md) that is exposed outside the Body; that is, if another tool from any workbench (for example, **[<img src=images/Part_SimpleCopy.svg style="width:16px"> [Part SimpleCopy](Part_SimpleCopy.md)** or **[<img src=images/Part_Cut.svg style="width:16px"> [Part Cut](Part_Cut.md)**) needs to use the shape of the Body, it will use the shape of the Tip. Said in another way, the Tip is the final representation of the Body as if the parametric history didn\'t exist.

![](images/PartDesign_Body_Tip_final.svg )



*Left: PartDesign Body with full parametric history including intermediate features. Right: the Tip is the final shape that can be exported from the Body, while omitting the model's history.*

The Tip is automatically set to the last feature created in the Body. Nevertheless, it can also be set to any of the intermediate features by opening the [tree view](tree_view.md) context menu (right-click) and choosing **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Set tip](PartDesign_MoveTip.md)**, or by changing the Body\'s **Tip** value in the [property editor](property_editor.md).

Changing the Tip in effect rolls back its history, making it possible to add features that should have been added earlier. It also exposes a different shape to external tools.


<div class="mw-translate-fuzzy">

For more details, see the <img alt="" src=images/PartDesign_MoveTip.png  style="width:24px;"> [Move Tip](PartDesign_MoveTip.md) page.


</div>

![](images/PartDesign_Body_Tip_tree.png ) 
*Two PartDesign Bodies, each of them with [PartDesign Features](PartDesign_Feature.md). The Tip is the last feature in them, and is marked with an overlay symbol.*


<div class="mw-translate-fuzzy">

### Interacțiunea cu alte Ateliere 

În mod implicit, obiectele aflate sub un corp pot fi selectate și, desigur, este necesar să editați și să adăugați caracteristici în PartDesign. Dar selectarea caracteristicilor unui Organism pentru a crea operațiuni de la alte Aeliere de lucru (cum ar fi [Part](Part_Workbench.md) or [Draft](Draft_Workbench.md)) nu este recomandată, deoarece rezultatele pot fi neașteptate; în toate cazurile, va apărea o eroare cu mențiunea \"Linkurile ies din domeniul de aplicare permis\" în vizualizarea Raport.


</div>

By default, [PartDesign Features](PartDesign_Feature.md) inside a Body are selectable, as this is required to edit and add more features with the [PartDesign Workbench](PartDesign_Workbench.md) tools. Nevertheless, selecting the individual features to use them with tools from other workbenches, like [Part](Part_Workbench.md) and [Draft](Draft_Workbench.md), is not advised, as the results may be unexpected; if this is done, in the [report view](Report_view.md) an error message may appear, **Links go out of the allowed scope**.


<div class="mw-translate-fuzzy">

Prin urmare, pentru interacțiunile cu alte bannere de lucru, numai corpul însuși ar trebui selectat din arborele Model. În cazurile în care este necesar să se selecteze topologia specifică pe corp (vârf, muchie, față), atunci proprietatea de vizualizare **Display Mode Body** poate fi comutată de la \'\'Through \'\' (implicit) la *Tip*. Această proprietate este accesibilă din panoul Vizualizare. În modul \"Tip\", accesul la obiectele din corp (funcții, date, schițe) este dezactivat; totul, dar caracteristica vârf va fi ascuns în vizualizarea 3D, indiferent de obiectul care este setat ca vizibil.


</div>


<div class="mw-translate-fuzzy">

Odată ce operațiile din alte Ateliere de lucru au fost finalizate, nu uitați să resetați proprietatea **Display Mode Body** la *Through* pentru a putea edita corpul.


</div>

![](images/PartDesign_Body_Tip_Display_mode.svg )



*Left: when "Display Mode Body" is set to `Through* it is possible to select and perform operations with the individual [PartDesign Features](PartDesign_Feature.md); in general, this is not recommended. Right: when "Display Mode Body" is set to {{incode|Tip` all selections and operations done on the Body will be done on the Tip, making sure only the final shape of the Body is exposed.}}


<div class="mw-translate-fuzzy">

### Managementul Vizibilității 

Vizibilitatea Corpului înlătură vizibilitatea oricărui obiect pe care îl conține. Dacă corpul este ascuns, obiectele pe care le conține vor fi ascunse, chiar dacă vizibilitatea lor este setată la adevărat. Doar o funcție poate fi vizibilă la un moment dat. Selectarea unei funcții ascunse și apăsarea butonului {{KEY | space}} va face vizibilă și va ascunde automat funcția vizibilă anterior.


</div>

The Body\'s visibility supersedes the visibility of any object it contains. If the Body is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`.

Multiple [Sketches](Sketch.md) may be visible at one time, but only one [PartDesign Feature](PartDesign_Feature.md) (solid result) can be visible at a time. Selecting a hidden feature and pressing the **Space** bar in the keyboard will make it visible, and automatically hide the previously visible feature.

![](images/PartDesign_Body_Visibility.png ) 
*PartDesign Body: multiple [Sketches](Sketch.md) may be visible simultaneously, but only one solid [PartDesign Feature](PartDesign_Feature.md) may be visible at one time, whether it is the Tip or not.*

### Attachment

[PartDesign Features](PartDesign_Feature.md), just like [planar objects](Part_Part2DObject.md), can be attached to different planes, usually the standard planes defined by the Body\'s [Origin](PartDesign_Body#Origin.md), or to custom [PartDesign Planes](PartDesign_Plane.md).

[Sketches](Sketch.md) are normally attached to a plane when they are created. In similar way, [primitive features](PartDesign_CompPrimitiveAdditive.md) can also be attached. Attaching these objects to a plane allows them to be moved within the Body by changing their **Attachment Offset** property. For more information on the attachment modes see [Part EditAttachment](Part_EditAttachment.md).

A [PartDesign Feature](PartDesign_Feature.md) that is not attached will be shown with a red overlay symbol next to their icon in the [tree view](tree_view.md).

![](images/PartDesign_Body_Feature_attachment.png ) 
*PartDesign Body: [PartDesign Features](PartDesign_Feature.md) that are not attached to a plane or coordinate system will be shown with an overlay symbol next to their icon in the [tree view](tree_view.md).*

### Inheritance

A [PartDesign Body](PartDesign_Body.md) is formally an instance of the class `PartDesign::Body`, whose parent is [Part Feature](Part_Feature.md) (`Part::Feature` class) through the intermediate `Part::BodyBase` class, and is augmented with an Origin extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `PartDesign::Body* object is intended to build parametric 3D solids, and thus is derived from the basic {{incode|Part::Feature` object, and has an Origin to control the placement of the features used inside of it.}}

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document

A PartDesign Body is created with the `addObject()` method of the document. Once a Body exists, [PartDesign Features](PartDesign_Feature.md) can be added to it with the `addObject()` or `addObjects()` methods of this Body.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

In a document that has many Bodies, the [active Body](PartDesign_Body#Active_status.md) can be set using the `setActiveObject` method of the `ActiveView`. The first argument is the fixed string `"pdbody"`, and the second argument is the Body object that should be made active. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/ro
