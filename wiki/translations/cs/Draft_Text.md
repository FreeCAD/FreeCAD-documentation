# Draft Text/cs
---
 GuiCommand:   Name: Draft_Text   Name/cs: Draft Text   Workbenches: Draft_Workbench/cs   Kreslení, Arch_Workbench/cs|MenuLocation: Draft , Text   Shortcut: T E---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Text vkládá text k zadanému bodu v aktuálnímu dokumentu. Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů.


</div>

To create a text element with an arrow use the [Draft Label](Draft_Label.md) command instead.


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Text.png" width=16px> [Text](Draft_Text.md)
** nebo klávesy **T** a potom **E**
2.  Klikněte na bod ve 3D pohledu nebo zadejte jeho souřadnice
3.  Vložte požadovaný text, mezi každým řádkem stiskněte **ENTER**
4.  Klávesu **ENTER** stiskněte 2x pro ukončení operace.


</div>



## Volby

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Stisknutí klávesy **CTRL** [přichytí](Draft_Snap/cs.md) Váš bod k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Pro zadání souřadnic ručně, jednoduše zadejte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu
-   Stisknutím **ENTER** nebo **Šipka dolu** při úpravě textu můžete vložit nebo editovat další řádek textu.
-   Stisknutím klávesy **Šipka nahoru** můžete editovat předcházející řádek textu.
-   **Dvojím** stisknutím **ENTER** (t.j. nevyplnění posledního řádku) přidáte text do dokumentu a ukončíte editor.


</div>

## Notes

-   A Draft Text can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Draft Texts created or saved with [FreeCAD version 0.21](Release_notes_0.21.md) are not backward compatible.




<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Pozice**: Základní bod textového bloku

-    **Štítek textu**: Obsah textového bloku

-    **Mód zobrazení**: Specifikuje jestli je text zarovnán podle os nebo vždy míří směrem ke kameře

-    **Velikost fontu**: Velikost písmen

-    **Zarovnání**: Specifikuje zda je text zarovnán vlevo, vpravo nebo na střed od základního bodu.

-    **Mezera mezi řádky**: Specifikuje mezeru mezi řádky textu.

-    **Rotace**: Specifikuje rotaci, která bude aplikována na text.

-    **Osa rotace**: Specifikuje osu, která bude použita pro rotaci.

-    **Název fontu**: Font použitý pro kreslení textu. Může to být název fontu, jako např. \"Arial\", default styl jako je \"sans\", \"serif\" nebo \"mono\" nebo rodina jako je \"Arial,Helvetica,sans\" nebo jméno se stylem jako je \"Arial:Bold\". Není-li zadaný font nalezen v systému, je místo něj použit obecný font.


</div>

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifies the position of the text in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Text|StringList**: specifies the contents of the text. Each item in the list represents a new text line.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by its **Placement**. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Justification|Enumeration**: specifies if the alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Text Color|Color**: specifies the color of the text.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Text může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Text use the `make_text` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeText` method.


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt Text na zadaném bodě, je-li poskytnut vektor, s textem obsahujícím řetězec nebo řetězce v seznamu list, jeden řetězec na jeden řádek. \* Je použita aktuální barva a výška textu a font specifikovaný v přednastaveních.
-   Je-li screenmode True, text se vždy zobrazuje ve směru pohledu, jinak leží v rovině XY.
-   Vrací nově vytvořený objekt.


</div>

The view properties of `text` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/cs
