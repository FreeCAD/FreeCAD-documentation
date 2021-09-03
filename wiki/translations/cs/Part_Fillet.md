---
- GuiCommand:/cs   Name:Part Fillet   Name/cs:Díl Zaoblení   MenuLocation:Díl → Zaoblení   Workbenches:[SeeAlso:[[Part Chamfer/cs|Díl Zkosení](Part_Workbench/cs___Díl]],_Kompletace.md)---


</div>


<div class="mw-translate-fuzzy">

#### Popis

Tento nástroj vytváří zaoblení na vybraných hranách objektu. Dialogové okno umožňuje vybrat objekty a hrany pro zaoblení.


</div>

This tool creates a fillet (round) on the selected edges of an object. A dialog allows you to choose which objects and which edges to work on.


<div class="mw-translate-fuzzy">

#### Použití

-   Spusťte nástroj z nástrojového pruhu Díl nebo z menu. Objekt můžete vybrat buď před nebo po spuštění nástroje.
-   Pokud nebyl objekt vybrán před spuštěním nástroje, vyberte jej v rozbalovacím menu Tvar v panelu Úkolů.
-   Vyberte typ zaoblení, buď pevný poloměr (defaultní) nebo proměnný poloměr.
-   Vyberte hrany. Buď ve 3D pohledu nebo jejích výběrem v seznamu hran v panelu Úkolů.
-   Nastavte hodnotu poloměru.
-   Potvrďte kliknutím na **OK**.


</div>

-   Start the tool from the Part toolbar or from the menu. You can either select the object before or after starting the tool.
-   If the shape was not selected prior to starting the tool, select it in the Shape drop down list in the [Task Panel](Task_panel.md).
-   Select the fillet type, either constant radius (default) or variable radius.
-   Select the edges either in the [3D view](3D_view.md), or by ticking them in the edge list in [Task Panel](Task_panel.md).
-   Set the radius value.
-   Click **OK** to validate.


<div class="mw-translate-fuzzy">

![](images/Dialog-fillet.jpg )


</div>


<div class="mw-translate-fuzzy">

### Díl Zaoblení VS. Návrh dílu Zaoblení {#díl_zaoblení_vs._návrh_dílu_zaoblení}

V pracovní ploše Návrh dílu je jiný nástroj pro zaoblení. Pamatujte si prosím, že jejich funkce jsou docela odlišné. Projděte si referenční stránku [Návrh dílu Zaoblení](PartDesign_Fillet/cs.md), kde je podrobnější popis rozdílů.


</div>

## Notes on application of Part Fillet {#notes_on_application_of_part_fillet}

Part Fillet might do nothing if the result would touch or cross the next adjacent edge. So if you do not get the expected result, try with a smaller value. This is the same for <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Chamfer](Part_Chamfer.md).

The fillet tool sometimes fails when trying to fillet complex objects. A common cause of this may be that the shape being filleted is not geometrically correct. This may be the result of lines/planes etc not being removed after previous operations used to construct the shape ( e.g. Cut/Intersection/Fusion). A number of steps can be used to minimize problems:

-   Where possible leave filleting a part until the part is completely generated. This will minimize interaction of fillets with subsequent Boolean operations;
-   Use the {{MenuCommand|Part → Check Geometry}} to check for any errors in the shape geometry and correct;
-   Use {{MenuCommand|Part → Refine shape}} to remove any artifacts introduced by previous Boolean operations before filleting (and in some cases between filleting operations in sequence);
-   Consider using {{MenuCommand|Edit → Preferences → PartDesign}} to enable automatic checking and refining of the model after Boolean and sketch based operations (performance may be affected if these options are left switched on).

Also note that the part Fillet feature is affected by the [Topological naming problem](Topological_naming_problem.md) when the any change is done to a modeling step earlier in the chain that affects the number of facets or vertices. This could cause unpredictable result. Until that is resolved (possibly with V0.19) it is advised to apply Chamfer and [Fillet](Part_Fillet.md) operations at the last steps in the chain.





  
