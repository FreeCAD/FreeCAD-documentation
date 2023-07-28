# Arch Window/cs
---
- GuiCommand:/cs   Name:Arch Window   Name/cs:Arch Okno   Workbenches:[MenuLocation:Arch → Window   Shortcut:W I   SeeAlso:[[Arch Wall/cs|Arch Wall](Arch_Workbench/cs___Arch]].md)---


</div>



## Popis


<div class="mw-translate-fuzzy">

Okno je základní objekt pro všechny druhy \"vestavěných\" objektů, jako jsou okna, dveře, atd\... Je konstruované tak aby bylo buď nezávislé nebo \"hostováno\" uvnitř jiné komponenty jako je zeď. Má svoji vlastní konfiguraci, která může být vytvořena z několika komponent (např. rám okna) a také definuje objem, který bude ubrán z hostitelského objektu při vytvoření otvoru.


</div>

Okna jsou založena na uzavřených 2D objektech jako jsou [Kreslení obdélníků](Draft_Rectangle.md) nebo [Náčrty](Sketcher_Workbench.md), které jsou využity k definování jejich vnitřních komponent. Základní 2D objekt proto může obsahovat několik uzavřených lomených čar, které mohou být kombinovány tak aby utvořily vyplněné křídlo (jedna lomená čára) nebo rámy (několik lomených čar). Jestliže byl 2D objekt nakreslen na podpůrném objektu a je-li tento podpůrný objekt zeď, je okno automaticky včleněno do zdi.

The Window tool features several **presets**; this allows the user to create common types of windows and doors with certain editable parameters, without the need for the user to create the base 2D objects and components manually.

All information applicable to an [Arch Window](Arch_Window.md) also applies to an [Arch Door](Arch_Door.md), as it\'s the same underlying object. The main difference between a Window and a Door is that the Door has an internal panel that is shown opaque (the door itself), while the Window has a panel that is partially transparent (the glass).

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Window_example.jpg  style="width:600px;">


</div>

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Complex window being constructed on top of a [Sketch](Sketcher_Workbench.md). When entering the window's edit mode you can create different components, set their thickness, and select and assign wires from the sketch to them.*




<div class="mw-translate-fuzzy">

## Použití


</div>



### Použití předvoleb 

1.  Press the **<img src="images/Arch_Window.svg" width=16px> [Arch Window](Arch_Window.md)** button, or press **W** then **I** keys.
2.  Select one of the presets in the list.
3.  Fill out the desired parameters.
4.  In the [3D view](3D_view.md), move the window to the location where you wish to place it. If you move the pointer over an [Arch Wall](Arch_Wall.md), the outline of the window should align itself with the face of that object.
5.  Click on the [3D view](3D_view.md) with the mouse, or press the **Enter** key three times to confirm the X, Y, Z coordinates of the placement.

#### Additional presets 

If you install the [Parts Library](Parts_Library_Workbench.md) from the [Addon Manager](Std_AddonMgr.md), the window tool will search this library for additional presets. These presets are FreeCAD files containing a single window based on a parametric sketch that has named constrains. You may place additional presets in the **parts_library** directory so that they are found by the window tool.


**$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/**

**$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/**

-   The **$ROOT_DIR** is the user directory where FreeCAD configuration files, macros, and external workbenches are stored. It can be found be entering `FreeCAD.getUserAppDataDir()` in the [Python console](Python_console.md).
    -   On Linux it is usually **/home/username/.local/share/FreeCAD/** (<small>(v0.20)</small> ) or **/home/username/.FreeCAD/** ({{VersionMinus|0.19}})
    -   On Windows it is usually **C:\Users\username\Application Data\FreeCAD\**
    -   On Mac OSX it is usually **/Users/username/Library/Preferences/FreeCAD/**
-   The subdirectory name **Custom** is just a suggestion, any name can be used. But the files must be placed in one or more subdirectories inside the **Doors** or **Windows** directories.

### Creating from scratch 

1.  Optionally, select a face on the Arch object where you want the window to be included.
2.  Switch to the [Sketcher Workbench](Sketcher_Workbench.md).
3.  Create a new sketch.
4.  Draw one or more closed wires (loops). Pay close attention to the creation order of these loops, the numbering of the \"wires\" in the [task panel](task_panel.md) (\"Window elements\") depends on this.
5.  Close the sketch.
6.  Switch back to the [Arch Workbench](Arch_Workbench.md).
7.  Press the **<img src="images/Arch_Window.svg" width=16px> [Arch Window](Arch_Window.md)** button, or press **W** then **I** keys.
8.  To adjust the window components and various properties, enter the window [task panel](task_panel.md) by double-clicking on the created object in the [tree view](tree_view.md).
9.  Note that since components following a hinged component will also hinge, all fixed components must be created first.

## Presets

The following presets are available:

Image:ParametersWindowFixed.svg\|Fixed Image:ParametersWindowSimple.svg\|Open 1-pane Image:ParametersWindowDouble.svg\|Open 2-pane Image:ParametersWindowStash.svg\|Sash 2-pane Image:ParametersWindowDouble.svg\|Sliding 2-pane Image:ParametersDoorSimple.svg\|Simple door Image:ParametersDoorGlass.svg\|Glass door Image:ParametersWindowDouble.svg\|Sliding 4-pane Image:ParametersWindowSimple.svg\|Awning



## Konstrukce komponent 


<div class="mw-translate-fuzzy">

Okna mohou obsahovat 2 typy komponent: křídla a rámy. Křídla jsou vytvořena z jedné uzavřené lomené čáry, která se vysune, zatímco rámy jsou udělány ze 2 nebo více uzavřených lomených čar, z nichž každá je samostatně vysunuta, potom ty menší jsou odebrány z těch větších. Na komponenty okna můžete přistupovat, měnit a mazat je v editačním módu (dvojklikem na okno v pohledu stromu). Komponenty mají následující vlastnosti:


</div>


<div class="mw-translate-fuzzy">

-   **Jméno**: Jméno komponenty
-   **Typ**: Typ komponenty. Může být \"Frame\" (Rám), \"Glass panel\" (Skleněný panel) nebo \"Solid panel\"(Pevný panel)
-   **Dráty**: Čárkami oddělený seznam drátů, na kterých je komponenta založena
-   **Tloušťka**: Tloušťka vysunutí komponenty
-   **Odsazení**: Vzdálenost mezi komponentou a její základovou 2D lomenou čárou(čárami)


</div>

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">



## Volby


<div class="mw-translate-fuzzy">

-   Můžete teké vytvořit uzavřený 2D profil (např. pomocí [Kreslicí plochy](Draft_Workbench.md) nebo [Náčrtové plochy](Sketcher_Workbench.md)), potom s tímto vybraným 2D profilem stisknete tlačítko **<img src="images/Arch_Window.png" width=16px> [Okno](Arch_Window.md)**.
-   Přidejte vybrané okno do [zdi](Arch_Wall.md) vybráním obou (zdi i okna), potom stisknutím tlačítka **<img src="images/Arch_Add.png" width=16px> [Přidat](Arch_Add.md)**.
-   Odebrání vybraného okna ze [zdi](Arch_Wall.md) vybráním okna a potom stisknutím tlačítka **<img src="images/Arch_Remove.png" width=16px> [Odebrat](Arch_Remove.md)**.
-   Při využití předvoleb je často výhodné zapnout \"Blízký\" [Kreslení Přichytit](Draft_Snap.md), takže můžete přichytit okno na existující plochu.


</div>

## Openings


**See also:**

[Tutorial for open windows](Tutorial_for_open_windows.md)

Doors and windows can appear partially or fully open in the 3D model, or can display opening symbols both in plan and/or elevation. Consequently, these will also appear in extracted 2D views generated by [Draft Shape2DView](Draft_Shape2DView.md) or [TechDraw Workbench](TechDraw_Workbench.md). To obtain this, at least one of the window components must have a hinge and an opening mode defined (see the [Building components](#Building_components.md) above). Then, using the **Opening**, **Symbol Plan** or **Symbol Elevation** properties, you can configure the appearance of the window:

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*A door showing the symbol plan, symbol elevation and opening properties at work*

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



## Vlastnosti


<div class="mw-translate-fuzzy">

-    **Části okna**: Seznam textových řetězců (5 řetězců na každou komponentu, nastavuje vlastnosti komponent jak jsou uvedeny výše)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Okno může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```


<div class="mw-translate-fuzzy">


:   vytvoří okno založené na zadaném objektu


</div>

Příklad: 
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Window/cs
