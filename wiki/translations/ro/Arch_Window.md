---
- GuiCommand:/ro
   Name:Arch Window
   Name/ro:Arch Window
   MenuLocation:Arch → Window
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**W** **I**
   SeeAlso:[Arch Wall](Arch_Wall/ro.md)
---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Fereastra este un obiect de bază pentru toate tipurile de obiecte \"încorporate\", cum ar fi ferestrele și ușile. Este concepută să fie independentă, sau \"găzduită\" în interiorul unei alte componente, cum ar fi [Arch Wall](Arch_Wall.md), [Arch Structure](Arch_Structure.md) sau [Arch Roof](Arch_Roof.md). Are o geometrie proprie, care poate fi făcută din mai multe componente solide (de obicei un cadru și panouri interioare) și definește de asemenea un volum care trebuie scăzut din obiectele gazdă, pentru a crea o deschidere.


</div>


<div class="mw-translate-fuzzy">

Elementele ferestrei se bazează pe obiecte 2D închise, cum ar fi [Draft Rectangles](Draft_Rectangle.md) ori [Sketches](Sketcher_Workbench.md), care sunt folosite pentru a defini componentele lor interioare. Obiectul de bază 2D trebuie să conțină, prin urmare, mai multe filamente închise, care pot fi combinate pentru a forma panouri umplute (un filament) sau rame (mai multe filamente).


</div>

Instrumentul Window are câteva funcții **presets**, acest lucru permite utilizatorului să creeze tipuri comune de ferestre și uși cu anumiți parametri editabili, fără a fi nevoie ca utilizatorul să creeze manual obiecte și componente de bază 2D.


<div class="mw-translate-fuzzy">

Toate informațiile aplicabile unui [Arch Window](Arch_Window.md) se aplică și pentru [Arch Door](Arch_Door.md), deoarece este același obiect de bază. Principala diferență dintre un Ferest și o Ușă este că Ușa are un panou interior care este arătat opac (ușa însăși), în timp ce Fereastra are un panou parțial transparent (geamul).


</div>

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;">


</div>

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Complex window being constructed on top of a [Sketch](Sketcher_Workbench.md). When entering the window's edit mode you can create different components, set their thickness, and select and assign wires from the sketch to them.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

### Utilizarea predefinitelor 


<div class="mw-translate-fuzzy">

1.  Opțional, selectați un obiect Arch. Dacă nu este selectat niciun obiect, fereastra va fi inserată în obiectul de sub mouse când plasați fereastra.
2.  Press the **<img src="images/Arch_Window.png" width=16px> [[Arch Window]]** button, or press **W** then **I** keys
3.  Select one of the presets in the list
4.  Fill out the desired parameters
5.  Press the **OK** button


</div>


**Note:**

if you install the \"Parts Library\" from the [AddonManager](AddonManager.md), the window tool will search this library for additional presets. These presets are FreeCAD files containing a single window based on a parametric sketch that has named constrains. You may place additional presets in the `parts_library` directory so that they are found by the window tool.


```python
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Doors/Custom/
$ROOT_DIR/Mod/parts_library/Architectural\ Parts/Windows/Custom/
```

The `$ROOT_DIR` is the user\'s directory where FreeCAD configuration, macros, and external workbenches are stored.

-   On Linux it is usually `/home/username/.FreeCAD/`
-   On Windows it is usually `C:\Users\username\Application Data\FreeCAD\`
-   On Mac OSX it is usually `/Users/username/Library/Preferences/FreeCAD/`

### Crearea de la zero 


<div class="mw-translate-fuzzy">

1.  Opțional, selectați o fațetă de pe Arch unde doriți să fie inclusă fereastra
2.  Switch to the [Sketcher Workbench](Sketcher_Workbench.md)
3.  Create a new sketch
4.  Draw one or more closed wires
5.  Close the sketch
6.  Switch back to the [Arch Workbench](Arch_Workbench.md)
7.  Press the **<img src="images/Arch_Window.png" width=16px> [[Arch Window]]** button, or press **W** then **I** keys
8.  Enter Edit mode by double-clicking the window in the tree view, to adjust the window components


</div>


**Note:**

when creating the sketch, pay close attention to the creation order of the loops; the numbering of the \"wires\" in the [task panel](task_panel.md) (\"Window elements\") depends on this.

## Setări prealabile 

Sunt disponibile următoarele presetări:

Image:ParametersDoorGlass.svg\|Glass door Image:ParametersDoorSimple.svg\|Simple door Image:ParametersWindowDouble.svg\|Double-opening window Image:ParametersWindowFixed.svg\|Fixed window Image:ParametersWindowSimple.svg\|Single-opening window Image:ParametersWindowStash.svg\|Sash-opening window

## Construcția de componente 

Ferestrele pot include 3 tipuri de componente: panouri, cadre și jaluzele. Panourile și jaluzele sunt realizate dintr-un fir închis, care este extrudat, în timp ce cadrele sunt realizate din 2 sau mai multe fire închise,where each one is extruded, then the smaller ones are subtracted from the biggest one. You can access, create, modify and delete components of a window in edit mode (double-click the window in the Tree view). The components have the following properties:

-   **Name**: Un nume al componentului
-   **Type**: The type of component. Can be \"Frame\", \"Glass panel\", \"Solid panel\" or \"Louvres\"
-   **Wires**: A comma-separated list of wires the component is based on
-   **Thickness**: The extrusion thickness of the component
-   **Z Offset**: The distance between the component and its base 2D wire(s)
-   **Hinge**: This allows you to select an edge from the base 2D object, then set that edge as a hinge for this component and the next ones in the list
-   **Opening mode**: If you defined a hinge in this component or any other earlier in the list, setting the opening mode will allow the window to appear open or to display 2D opening symbols in plan or elevation.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">

## Opţiuni


<div class="mw-translate-fuzzy">

-   Ferestrele partajează proprietățile și comportamentele comune ale tuturor[Arch Components](Arch_Component.md)
-   If the **Auto-include**checkbox on the Window creation task panel is unchecked, the window won\'t be inserted into any host object on creation.
-   Add a selected window to a [wall](Arch_Wall.md) by selecting both, then pressing the **<img src="images/Arch_Add.png" width=16px> [[Arch Add]]** button.
-   Remove a selected window from a [wall](Arch_Wall.md) by selecting the window, then pressing the **<img src="images/Arch_Remove.png" width=16px> [[Arch Remove]]** button.
-   When using presets, it is often convenient to turn the \"Near\" [Draft Snap](Draft_Snap.md) on, so you can snap your window to an existing face.
-   The hole created by a window in its host object is determined by two properties: **Hole Depth** and **Hole Wire** (<small>(v0.17)</small> ). The Hole Wire number can be picked in the 3D view from the window\'s task panel available when double-clicking the window in the tree view
-   Windows poate folosi [ Multi-Materials](Arch_MultiMaterial.md). Fereastra va căuta în Multi-Material -ul atașat pentru straturi de materiale cu același nume pentru fiecare componentă a ferestrei și o folosește dacă este găsită. De exemplu, o componentă numită \"OuterFrame\" va căuta în Multi-Material atașat, pentru un strat de material numit \"OuterFrame\". Dacă se găsește un astfel de strat, materialul său va fi atribuit componentei OuterFrame. Valoarea grosimii stratului de material nu este luată în considerare.


</div>

## Deschideri


<div class="mw-translate-fuzzy">

A se vedea de asemenea: [Tutorial for open windows](Tutorial_for_open_windows.md)


</div>


<div class="mw-translate-fuzzy">

Ușile și ferestrele pot apărea parțial sau complet în modelul 3D sau pot fi afișate atât în plan cât și în elevație. Consequently, these will also appear in extracted 2D views generated by [Draft Shape2DView](Draft_Shape2DView.md) or [TechDraw Workbench](TechDraw_Workbench.md) or [Drawing Workbench](Drawing_Workbench.md).Pentru a obține acest lucru, cel puțin una dintre componentele ferestrei trebuie să aibă o articulație și un mod de deschidere definit (vezi [\#Building components](#Building_components.md) de mai sus). Apoi, folosind proprietățile **Open**,\'\'\' Symbol Plan **sau** Elevation Symbol \'\'\', puteți configura aspectul ferestrei:


</div>

<img alt="" src=images/Arch_window_openings.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="A door showing from left to right the Symbol Plan, Symbol Elevation and Opening properties at work" src=images/Arch_window_openings.png  style="width:600px;">


</div>

## Defining window types 

Windows can also take advantage of other tools, specifically [PartDesign](PartDesign_Workbench.md) workflows, to define a type. A type is an object that defines the shape of the window. This is specially well suited to work with [App Parts](App_Part.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Download the example file shown above](https://github.com/FreeCAD/Examples/blob/master/Arch_Example_Files/Window_Type.FCStd)

### Example workflow 

-   Create a window frame object, a glass panel, and any other window component you need, using [Part Workbench](Part.md) or [PartDesign](PartDesign_Workbench.md) tools.
-   For example, create a base rectangular sketch for your window, then a profile sketch for the frame, and create a [Part Sweep](Part_Sweep.md) to sweep the profile around the base sketch. Create a [Part Offset2D](Part_Offset2D.md) from the base sketch, then a [Part Extrude](Part_Extrude.md) to create the glass panel
-   Make sure all these pieces have a unique, meaningful name (for example, \"Frame\" or \"Glass Panel\")
-   Create an [App Part](App_Part.md), and place all your subcomponents in it
-   Create a volume to be subtracted from the wall, for example by extruding the base sketch. Add this volume to the App Part. Make sure the volume is turned off
-   If using FreeCAD version 0.19 or later, you can add 3 properties to your App Part, by right-clicking its properties view, and check \"Show All\". Add the following properties (all of them are optional, the group doesn\'t matter):
    -   **Height** as a PropertyLength and link it, for example, to a vertical constraint of your base sketch
    -   **Width** as a PropertyLength and link it, for example, to a horizontal constraint of your base sketch
    -   **Subvolume** as a PropertyLink and link it to the volume to be subtracted that we created above
    -   **Tag** as a PropertyString

### Materials

Our window type is now ready. We can create window objects from it, simply by selecting the App Part and pressing the window button. The \"Height\", \"Width\", \"Subvolume\" and \"Tag\" properties of the window will be linked to the corresponding property of the App Part, if existing.

To build a material for type-based windows:

-   Create a [multi-material](Arch_MultiMaterial.md)
-   Create one entry in the multi-material for each component of your App Part. For example, one \"Frame\", one \"Glass panel\" as we used above. Make sure to use the exact same name.
-   Attribute that multi-material to each of the windows derived from the same type

You can use any other kind of workflow than the one described above, the important points to remember are:

-   The type object must be one object, no matter the type (App Part, PartDesign Body, Part Compound, or even another Arch Window)
-   The type object must have a \"Subvolume\" property (linked to the window\'s Subvolume property) for openings in host objects to work
-   The type object must have a \"Group\" property with different children with same names as multi-material items for multi-materials to work

## Proprietăți

-    **Height**: Înălțimea acestei ferestre

-    **Width**: The width of this window

-    **Hole Depth**: The depth of the hole created by this window in its host object

-    **Hole Wire**: The number of the wire from the base object that is used to create a hole in the host object of this window. This value can be set graphically when double-clicking the window in the tree view. Setting a value of 0 will make the window automatically pick its biggest wire for the hole.

-    **Window Parts**: A list of strings (5 strings per component, setting the component options above)

-    **Louvre Width**: If any of the components is set to \"Louvres\", this property defines the size of the louvre elements

-    **Louvre Spacing**: If any of the components is set to \"Louvres\", this property defines the spacing between the louvre elements

-    **Opening**: All components that have their opening mode set, and provided a hinge is defined in them or in an earlier component in the list, will appear open by a percentage defined by this value

-    **Symbol Plan**: Shows 2D opening symbol in plan

-    **Symbol Elevation**: Shows 2D opening symbol in elevation


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul pentru ferestre poate fi utilizat în [macro-uri](macro-uri.md) și din consola [Python](Python.md) utilizând următoarea funcție:


</div>


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```


<div class="mw-translate-fuzzy">

-   Toate argumentele sunt opționale
-   Creează un  Window \</ code\> bazat pe  baseobj \</ code\>, care ar trebui să fie un [Draft Wire](Draft_Wire.md) sau [Sketcher Sketch](Sketcher_Sketch.md)
-   Dacă este disponibil, setează  width \</ code\>,  height \</ code\> și  name \</ code\>
-   Dacă  baseobj \</ code\> nu este o formă închisă, este posibil ca instrumentul să nu creeze o figură solidă adecvată


</div>

Exempluː 
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

You can also create a Window from a preset. 
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;">


</div>

Example: 
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```


<div class="mw-translate-fuzzy">


</div>







[Category:Arch/ro](Category:Arch/ro.md)
