---
- GuiCommand:/cs   Name:Draft_ShapeString   Name/cs:Draft ShapeString   Workbenches:[MenuLocation:Draft -> ShapeString   Shortcut:S S   SeeAlso:[[Draft Text/cs|Draft Text](Draft_Workbench/cs___Kreslení]].md), [Part Extrude](Part_Extrude/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj ShapeString vkládá složený tvar, který reprezentuje textový řetězec na daný bod v aktuálním dokumentu. Výška textu, mezery a font mohou být specifikovány.


</div>

The Draft ShapeString command is not intended for standard text annotations. The [Draft Text](Draft_Text.md) command or the [Draft Label](Draft_Label.md) command should be used for that purpose.

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">

![](images/Draft_ShapeString_Example400.png )


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** button.
    -   Select the {{MenuCommand|Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text}} option from the menu.
    -   Use the keyboard shortcut: **S** then **S**.
2.  The {{MenuCommand|ShapeString}} task panel opens.
3.  Click a point in the [3D view](3D_view.md), or type coordinates.
4.  Optionally press the **Reset Point** button to reset the point to the origin.
5.  Enter a {{MenuCommand|String}}.
6.  Specify the {{MenuCommand|Height}}.
7.  To select a font do one of the following:
    -   Enter a file path in the {{MenuCommand|Font file}} input box.
    -   Press the **...** button and select a file.
8.  Press the **OK** button to finish the command.

## Volby


<div class="mw-translate-fuzzy">

-   Pro zadání souřadnic ručně, jednoduše zadejte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **ESC** pro ukončení aktuálního příkazu.
-   Defaultní soubor s fontem můžete přednastavit v Kreslení/Předvolby.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Omezení

-   Tento nástroj není dosud obecně dostupný. Bude zahrnut v budoucí verzi. (post v0.13)
-   Jsou podporovány soubory s fonty TrueType(\*.ttf), OpenType(\*.otf) a Type1(\*.pfb).
-   Velmi malé výšky textu mohou zapříčinit deformaci znaků kvůli ztrátě detailů.
-   Aktuální verze je omezena na zarovnání zleva doprava na horizontální základně.


</div>

## Tutorials

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default font file can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file}}. See [Draft Preferences](Draft_Preferences.md).

## Vlastnosti

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Pozice**: Základní bod složeného písma

-    **String**: Text řetězce

-    **Velikost**: Výška textu v jednotkách FC

-    **Mezery**: Šířka mezer mezi písmeny v jednotkách FC

-    **Font File**: Soubor s definicí fontu pro kreslený text


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj ShapeString může být použit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Změní textový řetězec na složené písmo s použitím specifikovaného fontu.


</div>

The placement of the ShapeString can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```





 
