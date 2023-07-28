# Draft Dimension/cs
---
- GuiCommand:/cs   Name:Draft Dimension   Name/cs:Draft Dimension   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Draft → Dimension   Shortcut:D I   SeeAlso:[FlipDimension](Draft_FlipDimension/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Kóta kreslí kóty v aktuálním dokumentu podle dvou bodů definujících měřenou vzdálenost a třetího bodu, který určuje kudy bude kóta procházet.


</div>

Linear dimensions based on edges and radial dimensions are parametric. This means that they will update if the measured edge is modified. Measured edges can belong to Draft objects but also to solid bodies. Angular dimensions are not parametric.

Draft Dimensions can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) or [TechDraw ArchView](TechDraw_ArchView.md) commands. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own dimension commands. But these create dimensions that are only displayed on the drawing page and not in the [3D view](3D_view.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


</div>

## Create

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

### Usage linear dimension 


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Dimension.png" width=16px> [Kóta](Draft_Dimension/cs.md)
** nebo klávesy **D** a pak **I**
2.  Klikněte na bod ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na druhý bod ve 3D pohledu nebo zadejte souřadnice
4.  Klikněte na třetí bod ve 3D pohledu nebo zadejte souřadnice


</div>

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a first straight edge in the [3D view](3D_view.md). Repeat this to select a second straight edge.
    -   Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  The displayed angle depends on the edges and the picked point.

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Stiskněte klávesu **X**, **Y** nebo **Z** po zadání bodu pro určení osy, na které bude ležet další bod.
-   Pro ruční zadání souřadnic jednoduše vložte číslo a **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain.md) kóty vodorovně nebo svisle nebo pokud pracujete na zakřivené hraně, přepíná mezi módem průměru a poloměru.
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **'''Relativní'''**. Je-li nastaven relativní mód jsou souřadnice následujícího bodu relativní k předchozímu bodu. Je-li mód absolutní souřadnice jsou vztaženy k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, můžete kreslit pokračovací kóty jednu za druhou při sdílení stejné základny.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu.
-   Výběrem existující hrany se stisknutou klávesou **ALT**, místo vložení měřeného bodu se kóta stane **parametrickou** a bude si pamatovat ke které hraně patří. Jestli se později některý z koncových bodů hrany posune, bude jej kóta následovat.
-   Směr kóty může být změněn později úpravou vlastnosti \"Směr\".


</div>

## Convert

### Usage

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Notes

-   Linear and radial Draft Dimensions can be edited with the [Draft Edit](Draft_Edit.md) command.
-   Draft Dimensions created or saved with [FreeCAD version 0.21](Release_notes_0.21.md) are not backward compatible.




<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Začátek**: Počáteční bod měření

-    **Konec**: Konečný bod měření

-    **PřímkaKóty**: Bod, kterým musí procházet kótovací čára

-    **Mód zobrazení**: Určuje zda je text zarovnán podle kótovací čáry nebo stále natočen ke kameře

-    **Velikost fontu**: Velikost fontu textu

-    **Vynášecí čáry**: rozměr vynášecích čar (mezi měřenými body a kótovací čárou)

-    **Pozice textu**: Může být využita pro určení pozice, kde má být text zobrazen

-    **Odsazení textu**: Specifikuje mezeru mezi textem a kótovací čárou

-    **Override**: Specifikuje text, který se má zobrazit místo míry. Chcete-li aby se v textu objevil i údaj o míře, použijte v požadovaném místě textu slovo \"\$dim\"

-    **Název fontu**: Font použitý při vykreslení textu. Může to být název fontu jako je \"Arial\", defaultní styl jako je \"sans\", \"serif\" nebo \"mono\" nebo family jako je \"Arial,Helvetica,sans\" nebo jméno se stylem jako třeba \"Arial:Bold\". Není-li zadaný font nalezen v systému, je místo něj použit obecný font.

-    **Typ šipky**: Použitý typ šipky

-    **Velikost šipky**: Rozměr šipky

-    **Desetiná místa**: Zobrazovaný počet desetinných míst

-    **Obrátit šipky**: Obrátí orientaci šipek


</div>

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension line passes.

-    **Linked Geometry|LinkSubList**: specifies the object and its subelement(s) the dimension is linked to.

-    **Normal|Vector**: specifies the normal of the plane of the text.

-    **Support|Link|hidden**: specifies the measured object.


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Normal** of the measurement. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbols displayed at the ends of the dimension line or arc.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the ends of the dimension line or arc, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifies the additional length added to the dimension line. Not used for angular dimensions.

-    **Ext Lines|Distance**: specifies the length of the extension lines that go from the dimension line to the measured points. Use {{Value|0}} for full extension lines. A negative value defines the gap between the ends of the extension lines and the measured points. A positive value defines the maximum length of the extension lines. Only used for linear dimensions.

-    **Ext Overshoot|Distance**: specifies the additional length of the extension lines beyond the dimension line. Not used for angular dimensions.

-    **Flip Arrows|Bool**: specifies whether to flip the orientation of the symbols at the ends of the dimension line or arc. Only works if the symbols are arrows.

-    **Line Color|Color**: specifies the color of the dimension line or arc, and the arrows.

-    **Line Width|Float**: specifies the width of the lines or arc belonging to the dimension.

-    **Show Line|Bool**: specifies whether to display the dimension line. Does not affect the display of extension lines and overshoots. Not used for angular dimensions.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Color|Color**: specifies the color of the text. <small>(v0.21)</small> 

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Kóta může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Dimension use the `make_dimension` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeDimension` method.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

There are various ways to invoke this method, depending on the arguments passed to it:


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt kóty s kótovací čárou procházející přes p3.
-   Objekt kóty přebíráe [tloušťku čáry a barvu](Draft_Linestyle.md) nastavenou v příkazovém pruhu.
-   Je několik způsobů vytvoření kóty v závislosti na předaných argumentech:

1.  (p1,p2,p3): vytvoří standardní kótu z p1 do p2.
2.  (object,i1,i2,p3): vytvoří spojenou kótu na daný objekt, která měří vzdálenost mezi vrcholy indexovanými i1 a i2.
3.  (object,i1,mode,p3): vytvoří spojenou kótu na daný objekt, i1 je index (zakřivené) měřené hrany a mód je buď \"poloměr\" nebo \"průměr\". Vrací nově vytvořený objekt.


</div>

To create an angular dimension use the following method:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```


<div class="mw-translate-fuzzy">

-   vytvoří úhlovou kótu z daného středu se zadaným seznamem úhlů procházející bodem p3.
-   Vrací nově vytvořený objekt.


</div>

The view properties of `dimension` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/cs
