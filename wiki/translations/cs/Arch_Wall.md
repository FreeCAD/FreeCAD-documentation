---
- GuiCommand:/cs   Name:Arch Wall   Name/cs:Zed'   Workbenches:[MenuLocation:Arch → Zed'   Shortcut:W A   SeeAlso:[[Arch Structure/cs|Struktura](Arch_Workbench/cs___Architettura]].md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj staví objekt Zeď od začátku nebo na vrchní části jakéhokoliv objektu založeného na [tvaru](Part_Workbench.md) nebo [síti](Mesh_Workbench.md). Zeď může být postavena i bez jakéhokoliv základního objektu, v takovém případě se chová jako trojrozměrné těleso, které má vlastnosti délka, šířka a výška. Pokud je postavena na vrchní části existujícího tvaru, může být založena na:


</div>


<div class="mw-translate-fuzzy">

-   **2D lineárním objektu**, jako jsou přímky, lomené čáry, úhly nebo náčrty, v takovém případě můžete měnit tloušťku, zarovnání (vlevo, vpravo nebo na střed) a výšku. Vlastnost délka nemá žádný vliv.
-   **rovné ploše**, v takovém případě můžete měnit pouze výšku. Vlastnosti délka a šířka nemají žádný vliv. Je-li plocha svislá, bude se používat vlastnost šířka místo výšky, což umožňuje vytvořit zeď z jakoby prostorových objektů nebo hmotových studií.
-   **tělese**, kdy vlastnosti délka šířka a výška nemají žádný vliv. Zeď jednoduše přebírá tvary podkladového tělesa.
-   **síti**, v takovém případě musí být podkladová síť uzavřená bez mezer.


</div>

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Walls built from a line, a wire, a face, a solid, and a sketch*


<div class="mw-translate-fuzzy">

Zdi také mohou být přidávány nebo odebírány. Přídavky jsou další objekty jejichž tvary jsou připojeny ke tvaru zdi, zatímco odebírání jsou tvary odebírané ze zdi. Přidávání a odebírání se dělá pomocí nástrojů [Přidat](Arch_Add.md) and [Odebrat](Arch_Remove.md). Přidávání a odebírání nemá žádný vliv na parametry zdi jako jsou výška a šířka, které mohou být dále měněny. Zeď může mít také automatickou výšku, a to v případě když je včleněna do výškově daného objektu jako je [podlaží](Arch_Floor.md). Výška pak musí být nastavena na 0, zeď pak přebírá výšku specifikovanou v rodičovském objektu.


</div>

Pokud se má několik zdí protínat, musíte je umístit do [podlaží](Arch_Floor.md) aby se protínaly v jeho konstrukci.


<div class="mw-translate-fuzzy">

## Použití


</div>

### Kreslení zdi z náčrtu 


<div class="mw-translate-fuzzy">

1.  Stiskněte tlačítko **<img src="images/Arch_Wall.png" width=16px> [Zeď](Arch_Wall.md)
** nebo klávesy **W** a **A**
2.  Klikněte na první bod v 3D pohledu nebo zadejte [koordináty](Draft_Coordinates.md)
3.  Klikněte na druhý bod v 3D pohledu nebo zadejte [koordináty](Draft_Coordinates.md)


</div>

### Nakreslení zdi na vybraném objektu 


<div class="mw-translate-fuzzy">

1.  Vyberte jeden nebo více geometrických objektů(Nakreslený objekt, nákres, atd.)
2.  Stiskněte tlačítko [Zeď](Arch_Wall.md) nebo stiskněte klávesy **W** a **A**
3.  Nastavte požadované vlastnosti jako je výška nebo šířka.


</div>

## Volby


<div class="mw-translate-fuzzy">

-   Výška, šířka a zarovnání zdi může být nastavena během kreslení pomocí zadávacího panelu
-   Připojením zdi na existující zeď budou obě zdi spojeny do jedné. Způsob jakým budou obě zdi spojeny závisí na jejich vlastnostech: mají-li stejnou šířku, výšku a zarovnání a je-li povolena volba \"spojit základní náčrty\" ve volbách Architektury, výsledná zeď bude jeden objekt založený na náčrtu vytvořeného z několik segmentů. V ostatních případech bude druhá zeď přidána k první zdi jako přídavek.
-   Po prvním bodu tiskněte klávesu **X**, **Y** nebo **Z** k určení druhého bodu v požadované ose.
-   Pro zadání koordinátů ručně jednoduše vložte číslo a stiskněte klávesu **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **Relativně**. Je-li nastaven relativní mód, budou koordináty druhého bodu relativní k prvnímu bodu. Není-li nastaven, koordiánty jsou absolutní k základnímu bodu (0,0,0).
-   Stiskněte klávesu **SHIFT** při [zadávání](Draft_Constrain.md) druhého bodu horizontálně nebo vertikálně v relaci k prvnímu bodu.
-   Stiskněte klávesu **ESC** nebo **Cancel** pro zrušení probíhajícího příkazu.
-   Dvojklik na zeď v panelu stromu po jejím vytvoření Vám umožňuje přejít do editačního módu a modifikovat ji


</div>

## Uchopování


<div class="mw-translate-fuzzy">

Uchopování pracuje trochu odlišně ve Zdech než v jiných objektech Architektury nebo Kreslení. Pokud má zeď podkladový objekt, bude vázána na základový objekt místo na konstrukci zdi, což Vám umožní snadněji vyrovant zdi k jejich základně. Nicméně, pokud specifikujete, že chcete uchopovat podle konstrukce zdi stisknutím klávesy **CTRL** bude uchopování přepnuto na objekt zdi.


</div>

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;">


</div>

## Vlastnosti


<div class="mw-translate-fuzzy">

Objekt zdi dědí vlastnosti objektů [Modul Díl](Part_Workbench.md) a má ještě následující zvláštní vlastnosti:

-    **Zarovnání**: Zarovnání zdi k její základně: Vlevo, vpravo nebo na střed

-    **Základna**: Základový objekt, na kterém je postavena

-    **Plocha**: Index plochy, která je použita ze základového objektu. Není-li hodnota nastavena nebo je 0, je použit celý objekt

-    **Vynucená lomená čára**: Je-li True a zeď je založena na ploše, je využit pouze obvodová čára plochy a výsledkem je zeď ohraničující plochu

-    **Délka**: Délka zdi (není využito pokud je zeď založena na objektu)

-    **Šířka**: Šířka zdi (není využito pokud je zeď založena na ploše)

-    **Výška**: Výška zdi (není využito pokud je zeď založena na tělese)

-    **Normal**: Směr vysunutí pro zeď. Je-li nastaveno na (0,0,0) je vysunutí zdi automatické.


</div>


<small>(v0.18)</small> 

-    **Make Blocks**: Enable this to make the wall generate blocks

-    **Block Length**: The length of each block

-    **Block Height**: The height of each block

-    **Offset First**: The horizontal offset of the first line of blocks

-    **Offset Second**: The horizontal offset of the second line of blocks

-    **Joint**: The size of the joints between each block

-    **Count Entire**: The number of entire blocks (read-only)

-    **Count Broken**: The number of broken blocks (read-only)


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Zeď může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```


<div class="mw-translate-fuzzy">

-   Vytvoří zeď založenou na zadaném objektu, což může být náčrt, nakreslený objekt, plocha nebo těleso. Zarovnání může být \"Center\",\"Left\" or \"Right\". Není-li zadán žádný podkladový objekt, pak musíte použít číslené hodnoty pro délku, šířku a výšku. Face může být použito pro zadání indexu použité plochy podkladového objektu, na kterém je zeď stavěna, místo použití celého objektu.
-   Vrací vytvořenou zeď nebo None když operace skončila neúspěšně.


</div>

Příklad:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>







[Category:Arch/cs](Category:Arch/cs.md)
