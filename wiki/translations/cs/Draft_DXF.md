
{{Page in progress}}







{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) *Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Otevírání

Tato funkce otevírá soubory DXF (jakoukoliv verzi od 12 do 2007) v novém výkresu. V současné době jsou podporovány následující objekty DXF:

-   přímky
-   lomené čáry a lwpolylines
-   kružnice
-   oblouky
-   vrstvy (vrstvy obsahující objekty jsou konvertovány do skupin FreeCADu)
-   texty a mtexty
-   kótování
-   bloky (pouze konstrukce; texty, kóty a atributy uvnitř bloků jsou přeskočeny)
-   body <small>(v0.13)</small> 
-   vynášecí čáry <small>(v0.13)</small> 

Ostatní DXF entity nejsou v současné době importovány, protože zatím nejsou ve FreeCADU implementovány korespondující objekty. Jakmile budou implementovány nové funkcionality, bude pravděpodobně možné importovat více typů entit.


</div>

The importer has two modes, settable under {{MenuCommand|Edit → Preferences → Import/Export → DXF}}: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D objects inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD. Simpler entities like 3DFACEs, though, are supported.

The following DXF objects can be imported:

-   lines
-   polylines (and lwpolylines)
-   circles
-   arcs
-   splines
-   ellipses
-   layers
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dimensions and attributes inside blocks will be skipped)
-   points
-   leaders
-   paper space objects


<div class="mw-translate-fuzzy">

### Exportování

Exportovaný DXF je kompatibilní s Autocadem verze 12 a vyšší, takže by mělo být možné jej otevřít v jakékoliv aplikaci, která podporuje DXF formát. V současnosti jsou exportovány následující objekty FreeCADu:

-   přímky a dráty (lomené čáry)
-   oblouky a kružnice
-   texty
-   barvy jsou mapovány z RGB barev objektů na indexy barev Autocadu (ACI). Černá bude vždy \"podle vrstvy\"
-   vrstvy jsou mapovány z názvů skupin. Jsou-li skupiny \"zahnízděny\" (skupina ve skupině), pak je jméno vrstvy podle nejhlubší skupiny.
-   kóty, které jsou exportovány ve \"Standardním\" stylu kót


</div>

Files are exported in the R14 DXF format which can be handled by many applications.

The following FreeCAD objects can be exported:

-   all of FreeCAD\'s 2D geometry such as Draft objects or sketches
-   3D objects are exported as a flattened 2D view
-   Compound objects are exported as blocks
-   texts
-   colors are mapped from objects RGB colors to autocad color index (ACI). Black will always be \"by layer\"
-   layers are mapped from group names. When groups are nested, the deepest group gives the layer name.
-   dimensions, which are exported with \"Standard\" dimstyle.

## Installing

For licensing reasons, the required [DXF](DXF.md) import/export libraries needed by the legacy version of the importer are not part of the FreeCAD source code. For more information see: [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).

## Preferences


<div class="mw-translate-fuzzy">

### Předvolby

V záložce [Předvoby kreslení](Draft_Preferences.md) (menu Úpravy -\> Předvolby -\> Kreslení) mohou být specifikovány následující parametry:

-   Styl importu: Ten umožňuje vybrat způsob jak budou objekty z DXF souboru vykresleny ve FreeCADu. Výběr je mezi:
    -   Žádný: to je rychlejší způsob bez konverzí, všechny objekty budou černé se šířkou 2px (defaultně podle FreeCADu)
    -   Použít defaultní barvu a tloušťku čáry: všechny importované DXF objekty budou přebírat barvu a tloušťku čáry z příkazového pruhu kreslení
    -   Originální barvu a tloušťku čáry: Objektům zůstane barva a tloušťka čáry (pokud je specifikována) jakou mají v DXF souboru
    -   Barvy mapovány na tloušťku čáry: Je-li vybrána tato volba, bude využit mapovací soubor uvedený dále
-   Mapovací soubor barev: Tato volba umožňuje specifikovat mapovací soubor, který bude využit pro transformaci DXF barev a tloušťek čar stejným způsobem jak funguje nákresový styl v Autocadu. Mapovací soubor musí být textový soubor s oddělovacím znakem tabelátorem. Existuje šikovná utilita nazvaná [Prohlížeč nákresového stylu](http://www.noliturbare.com/TablePrintGUI.php), která může konvertovat soubory Autocadu CTB nebo STB (nákresové styly) do souboru s oddělovacími tabulátory, které jsou připraveny k použití ve FreeCADu. Existuje i druhá možnost využít připravené [mapovací soubory](Draft_mapping_files.md) dostupné zde.
-   Import textů: To umožňuje specifikovat, zda chcete importovat DXF texty a kótování nebo ne. Mnoho textů může učinit práci ve FreeCADu velmi obtížnou, takže někdy se může tato volba docela hodit..
-   Import objektů rozložení: Zapnutím tohoto přepínače se importuje objekt prostoru papíru. Budou spojeny ve stejném dokumentu s objektem prostoru modelu.


</div>

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to DXF by using the following function: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Example: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/cs](Category:User_Documentation/cs.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)
