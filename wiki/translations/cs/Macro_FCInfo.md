# Macro FCInfo/cs
<div class="mw-translate-fuzzy">


{{Macro/cs
|Name=Macro_FCInfo
|Translate=FCInfo
|Icon=FCInfo.png
|Description=Dává řadu informací o tvaru.
|Author=Mario52
|Version=1.22
|Date=2020/11/12
|FCVersion=All
|Download=Download the [https://forum.freecadweb.org/download/file.php?id=50755 Macro_FCInfo_Icon] package and paste it in the same directory of the macro
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey/cs.md)<br />[Macro SimpleProperties](Macro_SimpleProperties/cs.md)
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Dává řadu informací o vybraném tvaru a může zobrazit konverzi délky, sklonu (stupně, radiány, procenta) tělesa, povrchu, objemu a váhy tvaru s měrnou hmotností vybranou v různých jednotkách hmotnosti mezinárodních i Anglo-Saských.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/4ecf1b82162b7a9e600c9ee511410ddf06c6e534/FCInfo_en_Ver_1-25d-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Utilisation


<div class="mw-translate-fuzzy">

### Použití

Vyberete objekt nebo spustíte aplikaci a vyberete objekt a zobrazí se řada informací. Jeho výpočty založené na jednotce FreeCADu, což je **mm** pro kažbý nový výběr, vrací vždy délku v **mm** a úhel v **dekadických stupních**.

<img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">


</div>




**Sector 1: Document**

-   Název dokumentu
-   Označení objektu
-   Interní název objektu
-   Název dílčího objektu
-   Typ objektu


<div class="mw-translate-fuzzy">

**Sector 2: Coordinates click mouse**

-   Souřadnice X, Y a Z kliknutím myší
-   Tlačítko vytváří na bodové, osové, rovinné, kopírovací vektorové formě osy \'\' \'FreeCAD.Vector (-24.0, 240.0, 7.0)\' \'\'


</div>


<div class="mw-translate-fuzzy">

**Sector 3: Value**

-   Délka objektu, je-li objekt obrys obličeje, zobrazí se velikost jednotky:
    km, hm, přehrada, m, dm, cm, \'\' \'mm\' \'\', μm, fm, palec, propojení, noha, yard, bidélko, řetěz, furlong, míle, ligy, námořní. Je-li objekt kružnicí o jednu sekundu, zobrazí se políčkoEdit a zobrazí poloměr kružnice.
-   Obvod tvaru


</div>


<div class="mw-translate-fuzzy">

**Sector 4: Vertexes and details**

-   CheckBox pro vyhledávání nebo ne všechny detaily objektu, pokud není zaškrtnuto pouze hlavní hodnota jsou zobrazeny.
-   Vertexy a detaily tvaru (compt\_Edge), (compt\_Faces), (compt\_Vector of Face)
    max 200 řádků v tabulce, pokud je více než 200 řádků se objeví (! + 200) a počet linky
    (všechny podrobnosti mohou uložit tlačítko **Save** ve formátu CSV a soubor v tabulce lze zobrazit pomocí **Read** nebo externí tabulky jako[LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other)


</div>


<div class="mw-translate-fuzzy">

**Sector 5: Inclination**

-   Záhyby objektu lze zobrazit v:
-   **desetinné stupně**, např .: 174.831872611 °
-   **stupeň minuty seconde**, např .: 174 ° 49 \'54.741401\' \'
-   **radian**, např .: 3.05139181449 rad
-   **stupeň**, např .: 194.257636235 gon
-   **pourcent** ex: 30 ° = 57,74%
-   Záhyby v rovinách XY, YZ, ZX a jejich souřadnicích
-   **Direction object**, udává směr objektu vypočítá se: coord\_1 - coord\_2 = směr (nebo reverzní)
    -   
        **Line**
        
        toto tlačítko vytvoří přímku ve směru objektu
-   **ValueAt** vrací 3D vektor odpovídající hodnotě parametru.


</div>


<div class="mw-translate-fuzzy">

**Sector 6: Surface and Volume**

-   Povrch zobrazené velikosti jednotky může být vybrán
-   Může být vybrán povrch zobrazené velikosti obličeje
-   Může být vybrána hlasitost zobrazené velikosti jednotky
-   hustota materiálu v **kg dm3**
    (\"spinBox\" je nastaven na \'\'\'7,5 \'\'\' kg, průměrná hustota oceli.Pokud chcete jinou výchozí hodnotu , změňte hodnotu hustoty, řádek 204)
-   Hmotnost **gram** buttom jednotky může být vybrána:
    t, quintal, kg, hg, dag, **gram**, dg, cg, fg, gr (obilí), dr (drachm), oz (jednou), oz t (troy trojúhelník), lb (livre troy), lb (livre av) , cwt (sto váha), tonneau fr, ct
-   může být vybrána váha zobrazené jednotky


</div>


<div class="mw-translate-fuzzy">

**Sector 7: BoundBox**

-   BoundBox extrémní rozměry tvaru


</div>


<div class="mw-translate-fuzzy">

**Sector 8: Center of:**

-   Střed tvaru a tyto souřadnice XYZ
-   Centrum hmotnosti a tyto souřadnice XYZ
-   Tlačítko vytváří na bodové, osové, rovinné, kopírovací vektorové formě osy **FreeCAD.Vector (-24.0, 240.0, 7.0)**


</div>


<div class="mw-translate-fuzzy">

**Sector 9: Inertia**

-   Moment setrvačnosti a tyto souřadnice délky a váhy
-   Tlačítko vytváří na bodové, osové, rovinné, kopírovací vektorové formě osy \'\' \'FreeCAD.Vector (-24.0, 240.0, 7.0)\' \'\'
    -   Akční řádek 1: x1, y1, z1
    -   Akční řádek 2: x2, y2, z2
    -   Akční řádek 3: x3, y3, z3
    -   Akční 4 úhlopříčky: x1, y2, z3

stejné pro délku a váhu

-   Determinant 1: vypočítá determinant vědecké hodnoty matice
-   Determinant 2: vypočte determinant maticové desetinné hodnoty


</div>

**Section 10: SpreadSheet**

-    **Read**: přečtěte si data v tabulce uložené **.FCInfo** nebo txt, asc, csv

-    **Save**: uloží data na disk ve formátu vybraném pod \'\'\' .FCInfo \'\'\' nebo txt, asc, csv

-    **Tabulation**: oddělovač je Tabulation

-    **Comma**: oddělovač je čárka

-    **Semicolon**: oddělovač je Semicolon

-    **Space**: oddělovač je Vesmír


<div class="mw-translate-fuzzy">

Možnost uložit nebo přečíst tabulku s různým oddělovačem, tabulka, čárka, středník, prostor
Tabulace jsou oddělovač pro modul FreeCAD spreadSheet
Počet těchto čtyř oddělovačů se vypočítá pro pomoc, pokud není známo
COMMA jsou starý (01.16 a dřívější) oddělovač maker FCInfo
Nyní pro kompatibilitu s rozložením FreeCAD spreadSheet a od verze 01.17 je TABULACE implicitně oddělovač
Chcete-li převést vaši starou tabulku FCInfo: Otevřete ji ve složce FCInfo a uložte ji pomocí možnosti Tabulace


</div>


<div class="mw-translate-fuzzy">

**Section 11: Main**

-    **CheckBox Clip Board**: pokud je zaškrtnuto, souřadnice jsou uloženy ve formátu clipBoard: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **CheckBox Point**: pokud je zaškrtnuto, vytvoří se jeden bod ve formě zobrazené souřadnice: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **Axis CheckBox**: pokud je zaškrtnuto, zobrazí se jedna osa ve formátu zobrazeném v souřadnicích: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **Plnicí plocha CheckBox**: pokud je zaškrtnuto jedna osová rovina v podobě souřadnic zobrazené: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **Ref**: Obnovení zobrazení dat v přehledu zpráv

-    **Exit**: Ukončete makro (musíte restartovat → panelu nástrojů nebo → nabídky \"View\> Panels\> FCInfo\"

-    **CheckBox****1**: Pokud je zaškrtnuto toto políčko Checkbox, jsou informace zobrazeny v okně zobrazení sestavy

-    **CheckBox****2**: Pokud není zaškrtnuto toto políčko CheckBox, makro okna se zobrazí vpravo (výchozí). Pokud je zaškrtnuto, makro okna se zobrazí vlevo


</div>

Po spuštění makra zůstane makro aktivní a okno zůstane viditelné. Chcete-li makro ukončit, stiskněte klávesu **Exit**. Pokud opustíte kříž, makro zůstane v paměti a data se objeví v zobrazení \"sestavy\" aplikace FreeCAD.


<div class="mw-translate-fuzzy">


<center>

Image:Macro\_FCInfo\_04.png\|Zakotveno vpravo, Image:Macro FCInfo 05.png\|nebo ponecháno v zobrazení Combo a dosažitelné pomocí karty, nebo není zakotveno k výběru.


</center>





</div>

## Options


<div class="mw-translate-fuzzy">

## Volby

### Použité jednotky 

#### Délková jednotka: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch(palec), link, foot(stopa), yard, perch, chain, furlong, mile, league, nautique.


</div>

#### Length unit: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Angle degrees : 


<div class="mw-translate-fuzzy">

#### Úhlové stupně : 

1.  **dekadické stupně**, např: 174.831872611°
2.  stupně minuty vteřiny, např.: 174° 49\' 54.741401\'\'
3.  radiány, např.: 3.05139181449 rad
4.  grade, např.: 194.257636235 gon
5.  procenta např.: 30° = 57.74%


</div>

Understanding of angles in FCInfo display.


<center>

Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in poucent in FCInfo display
click twice to see the animation (the image must be in full screen)


</center>




#### Weight unit : 


<div class="mw-translate-fuzzy">

#### Váhové jednotky : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
\"spinBox\" je nastaven na **7,5** kg, tj. průměrná měrná hmotnost oceli. Chcete-li jinou defaultní (přednastavenou) hodnotu, změňte hodnotu měrné hmotnosti na řádku 208


</div>


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```


<div class="mw-translate-fuzzy">

Soubor můůže být vytvořen tlačítkem **Save**. Takto je vytvořen soubor jako [.csv](https://fr.wikipedia.org/wiki/Comma-separated_values) soubor, data mohou být prohlížena v tabulkovém editoru ve FreeCADu nebo Openoffice, LibreOffice\...


</div>


<div class="mw-translate-fuzzy">

### Skript

Zkopírujte obsah tohoto makra do souboru nazvaného \"FCInfo.FCMacro\" (ve Windowsech) do \"C:\\Program Files\\FreeCAD0.13\".
Nebo přímo do okna FreeCADu
Ikona musí být ve stejném adresáři jako je makro pro Windows \"C:\\Program Files\\FreeCAD0.13\".
Stáhněte umístění obrázků u ikon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> a pravým tlačítkem je \"Uložte jako\" (neměňte jméno) (originál - Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name))


</div>

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your\_user\_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)


<div class="mw-translate-fuzzy">

**PS: příliš dlouhá na to, aby byla obsažena na stránce wiki (zatím jsou stránky wiki pouze 64 KB) kód makra byl umístěn na fóru**


</div>


<div class="toccolours mw-collapsible mw-collapsed">

Tam je také FCInfo\_Alternate\_Linux pouze pro FreeCAD verze 0.13 \... a PyQt4


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

Je tam také [Macro\_FCInfo\_Alternate\_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) zde je kód změněn (kvůli chybě zobrazení znaků: \'\' \'² ³ ° μ\' \'\' ordinal není v rozsahu (128) \"), které představovaly problémy v určitých konfiguracích, funkce jsou stejné
Příklad : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` nahrazeno 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Soubory uložené s touto verzí jsou nekompatibilní s jinou verzí (ukotvenou nebo nikoli)**


</div>


</div>



</div>

Stažení souboru ikon [Macro\_FCInfo\_Icon](https://forum.freecadweb.org/download/file.php?id=50755) rozbalte a zkopírujte ikonu ve stejném adresáři makra


<div class="mw-translate-fuzzy">

Stáhněte soubor makra na podstavec **ukotvený vpravo**


</div>


<div class="mw-translate-fuzzy">


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|last version Macro_FCInfo and the icons at the end of the page}}


</div>


<div class="mw-translate-fuzzy">

(Nebo **[On the forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)**)
**PS:** toto makro používá **getSelection ()** a seznam objektů začíná na 1 ex: pro pole \'\' \'Edge1 to Edge12\' a kód v konzole začíná na 0 ex: pro rámeček **Edge \[0\] na Edge \[11\]**
To je normální počítání na matici / seznamy uvnitř OpenCascade vždy začíná na **1 a ne na 0**


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Omezení

Pro ukončení vždy používejte tlačítko **Exit**. Ukončení jiným způsobem zapříčiní, že program zůstane v paměti a běží a zobrazuje data v \"reportovacím pohledu\". Abyste uvolnili pamět, musíte ukončit celý FreeCAD.
V tabulce je viditelných pouze prvních 200 prvků objektu. Je-li jich v objektu více zobrazí se upozornění \"\'(! +200)\" \'. Kompletní seznam dat je viditelný v souboru uloženém pomocí tlačítka **Save**.


</div>


<div class="mw-translate-fuzzy">

Pokud je makro okna po spuštění neviditelné, podívejte se do dolního okna:


</div>

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 


<div class="mw-translate-fuzzy">

projekt:
~~si přečtěte soubor přímo v tabulce.~~ provedeno
~~odpovídá okraji a jejich souřadnic~~, které byly provedeny
Sdružení látky s její hustotou
~~sklon k prvku spíše než globální objekt~~ proveden
~~vložte přímo do rozhraní FreeCADu~~ do


</div>

## Version


<div class="mw-translate-fuzzy">

-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


</div>


```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 little correction material field uncomment the \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 little correction new material
-   ver 1.23b, 20/11/2021 little correction, add text info in beginning run macro, and ordinal the text code
-   ver 1.23 , 19/11/2021 include icon in macro, number decimal displayed, text height, configure options in the Preference FC, correct info for elements of sketch in edit mode.
-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` and i adding the possibility display or not the \"Error Message\" window \"False\" by default, if you wand activate the warning window go to : 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
``` currently:
\*ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"

-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   ver 1.20 , 29/01/2018 optimization
-   ver 1.19 , 20/01/2018 create checkBox for use detection all elements of the object if wanted or not , the macro is faster. Optimisation
-   ver 1.18 , 19/12/2017 \...
-   ver 1.17c , 14/12/2017 create plane with coordinate give in one project in other project and replace \"FCInfo\" by \"\_\_title\_\_\"
-   ver 1.17b , 13/12/2017 little correction replace FCTreeView to FCInfo
-   ver 1.17 , 12/12/2017 add upgrade Moment of inertia mm and kg by pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), and create plane, axis, point, and add options separator for spreadsheet
-   ver 1.16 , 21/06/2017 add control height police (here PointSize 8) and checkbox for position the window to right or left
-   ver 1.15 , 19/12/2015 suppression PyQt4 option [see](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , add checkBox for editing infos in report view
-   ver 1.14 , 04/08/2014 replace PyQt4 and PySide and correct tooltip not displayed cause on PySide and add fg
-   ver 1.13 , 27/07/2014 replace FCInfo\_en\_Ver\_1-12\_Docked.FCMacro to FCInfo\_en\_Ver\_1-13\_Docked.FCMacro accept PyQt4 and PySide
-   ver 1.12 , 10/03/2014 adding tooltip
-   ver 1.11 , 04/03/2014 adding µm, nm, pm, fm, µg, ng, pg, pourcent, fixed of grandeur carat ~~\"cd\"~~ in **\"ct\"**, display of the label and internal name, fixed calculation of angles XY YZ ZX could give an error on a compound shape, window dockable in FreeCAD
-   ver 1.10.b , 19/11/2013 buttons outside the scrollbar and the dimensions of the window blocking

(ver 1.10 , 18/11/2013 create scrollbar)
\*ver 1.08.b , 10/11/2013 translation units in English, error correction to display the area of the faces listed in the table and replacement of the\"**print**\" by \"**App.Console.PrintMessage**\"
~~ver 1.09 , 04/11/2013 works perfectly on Windows and Linux (cause of errors on Linux the characters : ² ³ ° \"ordinal not in range(128)\")~~
In a Linux distribution and in the case of an error of **\"ordinal not in range (128)\"** an alternative version exists on this page [Macro\_FCInfo\_Alternate\_Linux](Macro_FCInfo_Alternate_Linux.md)
\*ver 1.08 , 24/10/2013 correction of high top \"Faces\" and \"Edges\" displaying 100 objects (in the saved file)
\*ver 1.07 , 11/10/2013 matches the \"Faces\" and their coordinates.
\*ver 1.06 , 22/09/2013 matches the \"Edges\" and their coordinates, inclination on the element rather than the global object
\*ver 1.05 , 17/09/2013 added an icon for the spreadsheet, conversion barrel fr, affichage des dimensions overall instead of coordinates.
\*ver 1.04 , 11/09/2013: read the file directly in a table.
\*ver 1.03 , 09/09/2013: clearer display in view report and replacement by \"typeObject = sel\[0\].Shape.ShapeType\"
\*ver 1.02 , 7/09/2013 : small updates
\*ver 1.00 , 6/09/2013


<div class="mw-translate-fuzzy">

## Odkazy

Viz také [Arch Survey](Arch_Survey/cs.md) <img alt="Arch Survey" src=images/Arch_Survey.png  style="width:36px;">


</div>

See Also: <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Survey](Arch_Survey.md)

Své připomínky můžete sdílet na fóru [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Zde je další příspěvek [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)

---
[documentation index](../README.md) > Macro FCInfo/cs
