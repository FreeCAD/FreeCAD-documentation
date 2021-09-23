# Macro Texture/cs



<div class="mw-translate-fuzzy">


{{Macro/cs
|Name=Macro Texture
|Translate=Macro Texture
|Icon=FCTexture.png
|Description=Vytvoří obraz 3D z obrázku BMP 8 bitů (256 barev).
|Author=Mario52
|Version=0.14c
|Date=2021/01/16
|FCVersion=0.18 and more
|Download=[https://www.freecadweb.org/wiki/images/9/90/FCTexture.png ToolBar Icon], [https://www.freecadweb.org/wiki/Macro_Loft Macro Loft] [16px|FCCreaLoft](File:FCCreaLoft.png.md)
|SeeAlso=[32px|FCCreaLoft](File:FCCreaLoft.png.md) [Macro Loft](Macro_Loft/cs.md)
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Toto malé makro vám umožňuje velmi snadno vytvořit 3D projekt z bitmapového obrázku 256 úrovní šedé.


</div>


<div class="mw-translate-fuzzy">

Doufám, že toto makro revoltuje způsob myšlení CAD a CNC jakéhokoli obrazu, když se může bez jakéhokoliv zásahu přeměnit na objekt 3D.


</div>


<div class="mw-translate-fuzzy">

Všechno je možné bez ohledu na složitost obrazu !


</div>


<div class="mw-translate-fuzzy">

Macro für die automatisierung des multi loft <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/cs.md) pro automatizaci multifunkčního loftu.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/262317bc7d8555885b0e/raw/3ec2ab127d8ad01a6b657aa5df9a6127ff07c7c0/Macro%2520FCTexture.FCMacro}}

<img alt="" src=images/Texture_004_Honda.png  style="width:480px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Texture_004_Honda.png  style="width:480px;"> 
*Texture 004 Honda*


</div>

## Usage


<div class="mw-translate-fuzzy">

## Použijte

Toto makro potřebuje obrázek v 256 odstínech šedé (0-255), proto před použitím makra převeďte snímek na stupně šedi (černé a bílé) Lowe. Počet barev je automaticky detekován, je-li obrázek více než 256 barev, očekává se další funkce. Každá barva (úroveň šedé) se považuje za hlubokou, bílou (255) vysokou a černou (0) nejnižší (hlubokou).


</div>

Konfigurace se provádí před otevřením souboru, výchozí hodnoty jsou nastavení poskytnutá pro získání rozměrů projektu:

-   šířka obrázku v bodech v souřadnici **X**,
-   výška obrázku v bodech v souřadnici **Y**,
-   hloubka nebo tloušťka projektu unikla 10 mm (v surovém režimu, na 256 mm) v souřadnici **Z**.

Soubor s obrázkem se rozkládá jako skener x1 x2 x3 \... v krocích po 1 mm v aplikaci FreeCAD podobně jako hodnota y 1 mm najednou. Hodnota z je dána hodnotou barvy. Tyto hodnoty lze konfigurovat v makru.


<div class="mw-translate-fuzzy">

Pozor: v závislosti na velikosti obrázku může být projekt velmi velký! pro záznam 100 pixelů široký a 100 pixelů na výšku dává 100 x 100 = 10000 bodů a každý bod odpovídá souřadnici, takže 10000 souřadnic XYZ tam je.


</div>


<div class="mw-translate-fuzzy">

### Rozhraní


</div>


<div class="mw-translate-fuzzy">

<img alt="Texture 002" src=images/Texture_002.png  style="width:300px;">


</div>

#### Coordinates


<div class="mw-translate-fuzzy">

#### Coordinate

-   Coordinate X <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}}: souřadnice X polohy objektu, implicitní: 0.
-   Coordinate Y <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}}: souřadnice Y polohy objektu, výchozí: 0.
-   Coordinate Z <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}}: souřadnice Z pozice objektu, výchozí: 0.


</div>

#### Stretching


<div class="mw-translate-fuzzy">

#### Stetching

-   Stetching X {{SpinBox|0,00 mm}}: zúžení nebo zvětšení délky objektu, default: 0.
-   Stetching Y {{SpinBox|0,00 mm}}: zúžení nebo zvětšení výšky objektu, default: 0.
-   Stetching Z {{SpinBox|0,00 mm}}: zúžení nebo zvětšení hloubky objektu, default: 0.


</div>

#### Inversion


<div class="mw-translate-fuzzy">

#### Inversion 

-    {{CheckBox|Axis X}}: zpětné souřadnice **X** obrázek.

-    {{CheckBox|Axis Y}}: zpětné souřadnice **Y** obrázek.

-    {{CheckBox|Axis Z}}: zpětné souřadnice **Z** obraz.


</div>

#### 8 bit Mode 


<div class="mw-translate-fuzzy">

#### Mode 8 Bits 

Začátek hodnoty operace se automaticky přizpůsobí zvolené funkci: 0, pokud je nastavení černé (**černé**) 255 nebo 20, je-li nastavení bílé (**bílá**).


</div>


<div class="mw-translate-fuzzy">

-    {{RadioButton|TRUE|<img src="images/Draft_Wire.svg" width=24px> Wire}}: postavte vaši linku (vektor) ve formě Wire.

-    {{RadioButton|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}: postavte svou linku (vektor) ve formě Bspline.

-    {{RadioButton|<img src="images/Workbench_Points.svg" width=24px> Cloud}}: buduje bodové vektory v bodovém oblaku.

-    {{RadioButton|<img src="images/Draft_Point.svg" width=24px> Point}}: vytvoří bod u každého pixelu (vektor). (postup může být dlouhý)

-    {{CheckBox|Nuance}}: Je-li zkontrolována volba odstínu, barva bodu je reprezentována jako obrázek.


</div>

#### 32 bit Mode 


<div class="mw-translate-fuzzy">

#### Mode 32 Bits 

-    {{RadioButton|TRUE|Photo}}: Režim foto je automaticky aktivován, když je detekován obraz **32 Bits**. (postup může být dlouhý)

-    {{RadioButton|Plan}}: plán umožňuje importovat **32 -bitový obrázek** a ignorovat pozadí plánu. Ve výchozím nastavení je pozadí mapy černé pro ignorování barev nastavitelné příkazem **Capping**. Pokud je zaškrtnuto políčko Bílý, ignorované dno bude bílé. (postup může být dlouhý)


</div>

#### File


<div class="mw-translate-fuzzy">

#### Files

-    {{CheckBox|.pcd}}: pokud je zaškrtnuto jeden soubor originalName.bmp.pcd je uložen ve stejném adresáři souboru (pcd v0.7).

-    {{CheckBox|.asc}}: pokud je zaškrtnuto jeden soubor originalName.bmp.asc je uložen ve stejném adresáři souboru. Tento soubor lze použít jako cloud point (formát: X Y Z).


</div>

#### Capping (10mm) 


<div class="mw-translate-fuzzy">

#### Capping (10mm) 

-   Slider: udávají výšku tvaru, výška je zobrazena v rámečku titulku.

-    {{SpinBox|0 height}}: udávají výšku tvaru, výška je zobrazena v rámečku titulku.

-   Raw mode {{CheckBox|20}}: pro nastavení počtu barev (hloubka). Výchozí režim je 0-20 (což představuje filtr a získání podrobnějších informací podle složitosti obrazu) po kontrole režimu 0 až 255 (celý rozsah barev).

-    {{CheckBox}}: Tento checkbox umožnil spouštění.

-    {{SpinBox|0/2 Contour}}: tento spinbox dává obrysovou čáru nepoužívejte (např. 0 pro základnu).

-   Capping {{CheckBox|White}} : Funkce zakončení může být provedena na základě výběru barev, bílé (výchozí) nebo černé. Stupně omezení pravidla 20 až 0 (nebo 255 až 0), pokud je zaškrtávací políčko nastaveno na **W** (nezaškrtnuto) nebo 0 až 20 (nebo 0 až 255) \'\'\' (kontrolovány).

-    {{SpinBox|20 Capping}}: Tento spinbox dává stupně omezení.


</div>

#### Command


<div class="mw-translate-fuzzy">

#### Command 

-    **File and launch**: otevře obrazový soubor a spustí konverzi.

-    **Help**: zobrazte wiki stránku ve webovém prohlížeči FreeCAD

    -   Zobrazte stránku Wiki v prohlížeči FreeCAD
    -   Pro změnu dostupného parametru: přejděte do **Nástroje → Upravit parametr \...**
    -   \_\_ Globální krok na spinBoxu: \_\_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → SingleStep**
    -   Upravte požadovanou hodnotu (standardně 1,0)
    -   \_\_ Pro vyhledávání, pokud je makro upgradováno: \_\_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → switchVesionMacroSearch**
    -   Upravte switchVesionMacroSearch na `True` (ve výchozím nastavení `False`)


</div>


<div class="mw-translate-fuzzy">

-    **Quit**: ukončí funkci.


</div>

## Skript

The icons .png <img alt="" src=images/FCTexture.png  style="width:64px;"> and .svg<img alt="" src=images/FCTexture.svg  style="width:64px;">

**Macro\_Texture.FCMacro**

Stáhněte makro k obsahu [Macro FCTexture.FCMacro](https://gist.github.com/mario52a/262317bc7d8555885b0e)

## Příklad

Obrazy byly nakloněny ke zvýšení efektu 3D.


<center>

<File:FCTexture_008.png%7CHonda>


</center>


<center>

<File:Macro_FCTexture_008b.png%7CHere> with option contour


</center>


<center>

<File:Texture> Nano Photo.png\|Here an example of a bmp image converted to points and restoring picture the width of the image is 6.5 nm
[thanks for the permission of Yorik](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075) Image:Texture NanoDesign.png\|Here an example of a bmp image converted to object 3D of 6.7 nm width.
[thanks for the permission of Yorik](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075)


</center>



<center>

Image:Texture 001 Logo.png\|The logo of FreeCAD. Image:Texture 002 Fe FC.png\|A portion of the screen FreeCAD. The [file](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353).


</center>



<center>

Image:Texture\_003\_napperon.png\|A portion of a tablecloth. Image:Texture\_005\_larme.png\|A diamond plate.


</center>



<center>

<File:FCTexture> 006.png\|Mode Plan: the image on the left the white background has been ignored in the right image the colour black has been ignored (an [example](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024) on the forum)


</center>



<center>

<File:Texture> Topographie.png\|Topography from a drawing or each level is represented with a degrees of different color.


</center>



<center>

<File:FCTexture_007_FreeCAD_ASCII_00.png%7CImage> converted in ASCII caracter.


</center>



<center>

<File:FCTexture_Example.gif%7CProcedure> for create solid:
**1:** Create loft with the <img alt="" src=images/Part_RuledSurface.svg  style="width:24px;"> tools or with the <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/cs.md)
**2:** Select all and extrude with the tools <img alt="" src=images/Part_Extrude.svg  style="width:24px;">
**3A:** For Linux Download [GMSHMesh](https://github.com/psicofil/Macros_FreeCAD) (author psicofil) [Macro\_GMSH Wiki page](Macro_GMSH.md)
**3B:** For Windows Download [GmshMesh2.zip](http://forum.freecadweb.org/download/file.php?id=15220) unzip the file and install it in your Mod directory (author ulrich1a)
**4:** Create your Mesh file and use it


</center>



<center>

<File:FCTexture> Example Mesh.png\|Convert solid in mesh with [GmshMesh.](Macro_GMSH.md)


</center>


## Links


<div class="mw-translate-fuzzy">

## Odkazy

Diskuse o [the forum](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893) abych získala své dojmy nebo mě kontaktovala.


</div>


<div class="mw-translate-fuzzy">

Macro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/cs.md) pro automatizaci multifunkčního loftu


</div>

[apply hair cell texture](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353)

[How to handle pdf import properly and feasibly?](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024)

## Revize

-   Ver 0.14c : 15-01-2021 include **Gui.SendMsgToActiveView(\"ViewFit\")**

-   Ver 0.14b : 15-01-2021 Create Tab Coordinate and Tab Stretching for diminish the height of the macro and accepted in 15\" screen

-   ver 0.13b: 30/12/2020 add try for **time.clock()** and **time.process\_time()** for Python 3xyz\...\*ver 0.13 : 17/04/2020 Layout and PySide2 Qt5
-   ver 0.13 : 17/04/2020 Layout and PySide2 Qt5
-   ver 0.12 : 04/08/2019 add spinbox button for height
-   ver 0.11 :03/07/2019 adapt to Python 3
-   ver 0.10 : 28/12/2016 add save point in .pcd, .asc display a points cloud, height form, contour
-   ver 0.9 : 12/12/2016 adding save file .asc for cloud point
-   ver 0.8 : 16/03/2016 adding progressBar
-   ver 0.7 : 03/09/2014 Delete \"**translate**\" forgotten and bug fix discovered by the passage of PyQt to Pyside !
-   ver 0.6 : 26/08/2014 Delete all \"**\_translate**\"
-   ver 0.5 : 25/08/2014 Delete \"**\_translate (\" MainWindow \",**\" Stretching X \"**, None)**\" that prevented the display of tooltip with PySide (Windows Vista)

-   ver 0.4 : 08/08/2014 PyQt4 PySide

-   ver 0.3 : 28/03/2014 :comment out the line \"**\# self.checkBox\_5.setAccessibleName(\_fromUtf8(\"\"))**\"

that causes an error with the version FreeCAD : Version: 0.14.3343 (Git), Python version: 2.7.6, Qt version: 4.8.5
