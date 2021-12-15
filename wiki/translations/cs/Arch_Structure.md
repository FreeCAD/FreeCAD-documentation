# Arch Structure/cs
---
- GuiCommand:/cs   Name:Arch_Structure   Name/cs:Struktury   Workbenches:[MenuLocation:Arch → Struktura   Shortcut:S T   SeeAlso:[[Arch Wall/cs|Zed'](Arch_Workbench/cs___Arch]].md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj Vám umožní stavět strukturované prvky jako jsou sloupy nebo příčníky specifikováním jejich šířky, délky a výšky nebo jejich založením na 2D profilu.


</div>

If no profile is given, a set of presets are available to quickly build a structural element from a predefined standard profile.

![](images/Arch_Structure_example.jpg )


<div class="mw-translate-fuzzy">

Obrázek nahoře zobrazuje sloup založený na 2D profilu, sloup a příčník založený na ne-profilu (definovaný rozměry výšky, délky a šířky) a kovový profil založený na 2D obrysu (plocha, lomená čára nebo náčrt)


</div>

## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte 2D tvar (nakreslený objekt, povrch nebo náčrt) (volitelné)
2.  Stiskněte tlačítko **<img src="images/Arch_Structure.png" width=16px> '''Arch Struktura'''
** nebo stiskněte klávesy **S** a **T**
3.  Nastavte požadované vlastnosti


</div>

## Volby


<div class="mw-translate-fuzzy">

-   Není-li vybrán žádný objekt, je vytvořen 3-rozměrný blok
-   Výška, šířka a délka struktury může být nastavena po vytvoření
-   Stiskněte klávesu **ESC** nebo **'''Cancel'''** pro ukončení aktuálního příkazu.
-   Dvojkliknutí na strukturu v pohledu stromu po jejím vytvoření Vám umožní přejít do editovacího režimu a upravovat vlastnosti
-   V editovacím módu je také možné přidat [osový systém](Arch_Axis.md) do strukturálního prvku. Pokud je přidán osový systém, strukturální prvek bude kopírován jednou na každou osu systému. Budou-li přídány 2 osové systémy, strukturální prvek bude kopírován na každý průsečík těchto dvou osových systémů.


</div>

## Vlastnosti

### Data


<div class="mw-translate-fuzzy">

-    **Délka**: Délka struktury (použito pouze v případě, že struktura není založena na profilu)

-    **Šířka**: Šířka struktury (použito pouze v případě, že struktura není založena na profilu)

-    **Výška**: Výška struktury (nebo vysunutí pokud je struktura založena na profilu)


</div>

### View

-    **Nodes Type**: The type of structural nodes of this object, linear or area.

-    **Show Nodes**: Shows or hides the structural nodes.

## Presets

The Structure tool also features a series of presets that allow to quickly build standard metallic profiles or precast concrete elements.

![](images/Arch_presets_example.jpg ) 
*Some presets for steel structures*

The presets are obtained by choosing a **Category** from the structure options panel. Available categories are **Precast concrete** or any of the industry-standard metallic profiles such as **HEA**, **HEB** or **INP**. For each of these categories, a number of presets are available. Once a preset is chosen, its individual parameters such as **Length**, **Width** or **Height** can be adjusted. However, for metallic profiles, the profile size is set by the preset and cannot be changed.

The **Switch L/H** button can be used to switch Length and Height values, and therefore building a horizontal beam rather than a vertical column.

<img alt="" src=images/Arch_precast_example.jpg  style="width:960px;"> 
*Some presets for precast concrete structures*

## Structural nodes 

Structural objects also have the ability to display structural nodes. Structural nodes are a sequence of 3D points stored in a \"Nodes\" property. By switching the \"Show Nodes\" view property on/off, one can see the structural nodes of a structural element:

<img alt="" src=images/Arch_structural_nodes.jpg  style="width:960px;"> 
*Structural nodes made visible for a set of structures*

-   Nodes are calculated and updated automatically, as long as you don\'t modify them manually. If you did, they won\'t be updated if the shape of the structural object changes, unless you use the \"Reset nodes\" tool below.
-   Arch structures can have not only linear nodes, but also planar nodes. For this, 1- There must be at least 3 vectors in the \"Nodes\" property of the object, 2- the \"NodesType\" property of their ViewObject must be set to \"Area\".
-   When the nodes calculation is automatic (that is, if you never touched them manually), when setting the Role property of a structure to \"Slab\", it will automatically become a planar node (there will be more than 3 vectors and the NodesType will be set to \"Area\").
-   When editing a structure object (double-click), a couple of node tools are available in the task view:
    -   Reset the nodes to automatic calculation, in case you modified them manually
    -   Edit the nodes graphically, works the same way as [Draft Edit](Draft_Edit.md)
    -   Extend the nodes of the edited object until it touches the node of another object
    -   Make the node of this object and another one coincident
    -   Toggle the display of all nodes of all structural objects of the document on/off

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Struktura může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Structure = makeStructure(baseobj=None, height=None)
Structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```


<div class="mw-translate-fuzzy">


:   vytvoří strukturální prvek založený na daném profilu a daném vysunutí do výšky. Není-li zadán žádný profil, můžete specifikovat délku a šířku trojrozměrného objektu.


</div>

Příklad: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(200, 300)
Structure1 = Arch.makeStructure(Rect, height=2000)
FreeCAD.ActiveDocument.recompute()

Structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(Structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/cs|[Wall/cs](Arch_Wall/cs.md)|[Arch CompRebarStraight/cs](Arch_CompRebarStraight/cs.md)|[Arch](Arch_Workbench/cs.md)|IconC=Workbench_Arch.svg|IconL=Arch_Wall.png|IconR=Arch CompRebarStraight.png}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Structure/cs
