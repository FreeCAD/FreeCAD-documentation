# Sketcher External/cs
---
- GuiCommand:/cs   Name:Sketcher_External   Name/cs:Skicář Povrchový Náčrt   Workbenches:[Návrh dílu](Sketcher_Workbench/cs___Skicář]],_[[PartDesign_Workbench/cs.md)|Shortcut:E   MenuLocation:Náčrt → Skicář Konstrukce → Povrchový náčrt   SeeAlso:[Konstrukční mód](Sketcher_ConstructionMode/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj přetáhne linky konstrukce do aktuálního náčrtu. Když jsou linky přetaženy, zobrazí se v náčrtu v barvě magenta a můžete na ně navázat linky v náčrtu a rozměry.


</div>

A note of caution, using this tool to link to generated (solid) geometry can lead to unexpected results due to [Topological Naming Problem](Topological_naming_problem.md). Also see [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).

<FILE:Sketcher_ExternalEsempio1.png>


<div class="mw-translate-fuzzy">

## Použití

-   Začněte náčrt na ploše tělesa (klikněte na plochu tělesa, potom klikněte na tlačítko pro vytvoření náčrtu)
-   Klikněte na tlačítko \'Povrchový náčrt\'
-   Vyberte linky tělesa, které chcete přetáhnout do náčrtu (pamatujte na to, že to musejí být linky ve stejné rovině jako je náčrt)


</div>

-   Create a new sketch, or open an existing sketch.
-   Click \'Sketcher External\' button
-   Select an edge or a vertex that you want to link to in the sketch.
-   Press Esc, or select another tool to stop importing geometry into the sketch.

### Selection rules 

-   Only edges and vertices from objects from same coordinate system are allowed.

That is, the sketch and the object must be in same Body (when in Part Design workbench), or in same Part (when in Part workbench), or both outside of any Parts and Bodies.

For example, If the open sketch is in Body, you can use another sketch from Body as external geometry, but you can\'t use a sketch from Body001, or an edge from a Part Cube in the root of the project. Use Shapebinder feature to bring in a copy of the object into the coordinate system of open sketch. Then you will be able to use edges/vertices of Shapebinder object.

-   No circular dependencies are allowed.

That means, you can\'t link to Pocket made with this sketch. You can\'t link to any object that depends on the sketch.

Sketch doesn\'t have to be on any face in order to use this tool. Links directly between sketches are possible, and encouraged, as they are more reliable.


<div class="mw-translate-fuzzy">

### Jak zjistit jestli to prošlo 

Pokud je linka úspěšně přetažena změní se její barva na magenta. Pokud přetažena nebyla zůstává její barva zelená.


</div>


<div class="mw-translate-fuzzy">

### Podobnost s Konstrukčními linkami 

Přetažené konstrukční linky v barvě magenta mohou být využity jak [Konstrukční linky](Sketcher_ConstructionMode/cs.md). Konstrukční linky jsou vnitřní linky náčrtu a používají se pouze pro vytváření konstrukce a ne pro pozdější operace s tělesem, jako je třeba vysunutí.


</div>


<div class="mw-translate-fuzzy">

### Dvě hlavní oblasti využití Přetažených linek 


</div>


<div class="mw-translate-fuzzy">

Jsou dva scénáře, kde se může hodit použití tohoto nástroje.


</div>


<div class="mw-translate-fuzzy">

Volba 1 je jednodušší volbou. Chcete-li udělat otvor na určitém místě objektu, měla by být použita tato metoda.


</div>


<div class="mw-translate-fuzzy">

### Záludné použití, Sneaky Usage, Dimension One Sketch Off Of Another 

One can use this to dimension one sketch off of another using the following order of operations:

1.  Vytvořte náčrt\#1
2.  Nástrojem Deska nebo vysunutím z něj vytvořte těleso, těleso\#1
3.  Vytvořte náčrt\#2 ve stejné rovině jako náčrt\#1
4.  Přetáhněte linky tělesa\#1 do náčrtu\#2
5.  Nástrojem Deska nebo vysunutím z náčrtu\#2 vytvořte těleso, těleso\#2
6.  Volitelné skryjte těleso\#1


</div>

You can use any Part geometry that is in coordinate system of the sketch. It is advised to link to the earliest feature possible, as it forms a more stable link.

## Příklad

Linky v barvě magenta jsou Přetažené konstrukce vybrané ve dvou objektech stejného vysunutého produktu z předchozího náčrtu. V takovém případě jsou použity k vytvoření vazeb dotyku s obvodem. Linka na menším obdélníku není využita.

In this case they are used as a reference for tangency constraints with the circumferences of one circle. They are also used as the reference for a horizontal and a vertical constraint to locate the centre of the second circle relative to the end and top of the Pad.

<FILE:Sketcher_ExternalEsempio2.png>

Aktivní náčrt se základním tvarem je skryt a přetažené konstrukce jsou viditelné.

<FILE:Sketcher_ExternalEsempio4.png>

Při uzavření skicáře nejsou přetažené konstrukce viditelné.

<FILE:Sketcher_ExternalEsempio3.png>


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}  

[Category:Sketcher/cs](Category:Sketcher/cs.md)

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/cs
