 {{TOCright}}


<div class="mw-translate-fuzzy">

## Přehled

Prostředky k duplikování objektů (odstavců, buněk tabulkových kalkulátorů, obrázků, atd.) jsou k dispozici u mnoha aplikací. FreeCAD není výjimkou. Objekty [Dokumentu](Document_structure.md) mohou být libovolně kopírovány uvnitř dokumentu nebo mezi dokumenty použitím [Kopírovat](Std_Copy.md), [Vložit](Std_Paste.md) a příkazem [Duplikovat výběr](Std_DuplicateSelection.md).

## Kopírování propojených objektů 

Objekty [Dokumentu](Document_structure.md) mohou být propojeny na jiné objekty (např. deska může být propojena se svým náčrtem a Fusion feature je propojena s svými komponentními objekty). To znamená, že stejně musí být postaráno i o kopírované objekty.


</div>

![](images/Copy_past_duplicate.png )

Please consider that the copy-pasted objects are not dependent on the original. If You want dependant clones please use <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [ Draft Workbench\'s Clone](Draft_Clone.md) or <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [ Part Design Workbench\'s Clone](PartDesign_Clone.md). If you need a dependant clone nor a parametric replica, you may also use <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [ Part Workbench\'s Simple Copy](Part_SimpleCopy.md). For patterned clones, please look into the [ Other Methods section](Copying_Objects#Other_Methods.md) of this page.

## Copying Linked Objects 

[Document](Document_structure.md) objects may be linked to other objects (for example, a Pad feature is linked to its Sketch, and a Fusion feature is linked to its component objects). This means that some care must be exercised in selecting objects to copy.


<div class="mw-translate-fuzzy">

Je-li nějaký objekt vybrán bez svých dětí (následovníků), tyto děti nejsou automaticky duplikovány použitím Kopírovat/Vložit nebo Duplikováním výběru. V takovém případě může kopírovaný objekt vykazovat nečekané chování, protože nejsou k dispozici očekávaná propojení.


</div>

In general, recommended practice is to select all dependent objects when copying a parent object.


<div class="mw-translate-fuzzy">

Obecně doporučovaná praxe je při kopírování rodičovského objektu vybrat všechny závislé objekty.

## Hledání a pozicování vkládaných objektů 

Po operaci Kopírovat/Vložit nemusí být zřejmé kde jsou zkopírované objekty v okně dokumentu umístěny. Je to proto, že nový objekt má stejnou vlastnost [Umístění](Placement.md) jako měl originál. Přepnutím vlastnosti Viditelnost (mezerníkem) skryjete originál. Potom použijete dialog Umístění abyste přesunuli nový objekt na jeho správnou pozici.


</div>


<div class="mw-translate-fuzzy">

## Další metody 

Jako mnoho věcí ve FreeCADu, je mnoho způsobů jak vytvořit kopii. Pro další inspiraci se podívejte na:

-   Návrh dílu: [Zrcadlo](PartDesign_Mirrored.md), [Lineární vzor](PartDesign_LinearPattern.md), [Polární vzor](PartDesign_PolarPattern.md), [MultiTransformace](PartDesign_MultiTransform.md)
-   Díl: [Zrcadlo](Part_Mirror.md)
-   Výkres: [Pole](Draft_Array.md),[Klon](Draft_Clone.md)

## Poznámky

-   Ve verzi v0.14+, jestliže nějaký kopírovaný objekt je propojen s objektem, který není kopírován, FreeCAD se zeptá jestli by nevybraný objekt neměl být také zahrnut do kopírování.


</div>

## Notes

-   If an object to be copied has links to object(s) not in the selection, FreeCAD will ask if the unselected objects should be included in the copy operation. <small>(v0.14)</small> 

## Další

-   [Kopírovat](Std_Copy.md)
-   [Vložit](Std_Paste.md)
-   [Duplikace výběru](Std_DuplicateSelection.md)


