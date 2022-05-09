# Arch SectionPlane/cs
---
- GuiCommand   */cs   Name   *Arch SectionPlane   Name/cs   *Arch SectionPlane   Workbenches   *[[Arch_Workbench/cs   Arch]]|MenuLocation   *Arch → Section Plane   Shortcut   *S P---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj umístí do aktuálního dokumentu pomůcku Rovina řezu, která definuje rovinu řezu nebo pohledu. Tato pomůcka může být přemístěna a přeorientována pomocí posunování a otáčení tak, abyste získali 2D pohled, který chcete získat. Objekt Rovina řezu bere ohled pouze na objekty, které byly vybrány v době jeho vytvoření. Objekty mohou být později přidávány do nebo odebírány z objektu Rovina řezu pomocí nástrojů [Přidat](Arch_Add.md) a [Odebrat](Arch_Remove.md).


</div>


<div class="mw-translate-fuzzy">

Po vytvoření objekt Rovina řezu také vkládá [pohled](Drawing_View.md) sama sebe do aktivní [Vykreslovací stránky](Drawing_Workbench.md) nebo vytváří novou stránku, pokud žádná neexistuje. Můžete také přidat pohled Roviny řezu přímo do dokumentu použitím nástroje [2D kreslení](Draft_Shape2DView.md) s vybranou rovinou řezu.


</div>

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width   *600px;">


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte objekty které chcete zahrnout do roviny pohledu
2.  Stiskněte tlačítko **<img src="images/Arch_SectionPlane.png" width=16px> '''Rovina řezu'''
** nebo stiskněte klávesy **S** a **P**
3.  [Posun](Draft_Move.md)/[otočení](Draft_Rotate.md) nastaví rovinu řezu do požadované pozice
4.  Stiskněte tlačítko **<img src="images/Std_Recompute.png" width=16px> '''Přepočítat'''** pro aktualizaci pohledu


</div>

## Volby

-   The Section plane object will only consider a certain set of objects, not all the objects of the document. Objects can be added or removed from a SectionPlane object by using the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view, selecting objects either in the list of in the 3D scene, and pressing the **add** or remove **buttons**.


<div class="mw-translate-fuzzy">

-   S vybraným objektem Rovina řezu použijte nástroj [2D kreslení](Draft_Shape2DView.md) k vytvoření tvaru reprezentujícího pohled řezu v dokumentu


</div>

<img alt="" src=images/Arch_Section_example2.jpg  style="width   *600px;">


<div class="mw-translate-fuzzy">

-   Vytvořit další [pohledy](Drawing_View.md) z roviny řezu lze po jeho vybrání udělat použitím nástroje [Kreslení](Draft_Drawing.md)


</div>

<img alt="" src=images/Arch_Section_example3.jpg  style="width   *600px;">

-   The Section Plane can also be used to show the entire 3D view cut by an infinite plane. This is only visual, and won\'t affect the geometry of the objects being cut.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width   *600px;">

## Vlastnosti


<div class="mw-translate-fuzzy">

-    **Rozměr zobrazení**   * Velikost pomůcky Rovina řezu ve 3D pohledu


</div>

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width   *600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App   *   *PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Rovina řezu může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce   *


</div>


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```


<div class="mw-translate-fuzzy">


   *   Vytvoří objekt Rovina řezu zahrnující zadané objekty.


</div>

Příklad   *


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>


 

[Category   *Arch/cs](Category   *Arch/cs.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane/cs
