# Drawing Workbench/cs
**The '''Drawing Workbench''' is no longer included after version 0.20.<br>
The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduction

Modul Výkres umožňuje dostat Vaši 3D práci na papír. To znamená dát pohledy na Vaše modely do 2D okna a vložit toto okno do výkresu, např. list s okraji, hlavička a logo a nakonec tento list vytisknout.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## GUI Nástroje 

These are tools for creating, configuring and exporting 2D drawing sheets

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Open scalable vector graphic](Drawing_Open_SVG/cs.md): Opens a drawing sheet previously saved as an SVG file

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New A3 landscape drawing](Drawing_Landscape_A3/cs.md): Creates a new drawing sheet from FreeCAD\'s default A3 template

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insert a view](Drawing_View/cs.md): Inserts a view of the selected object in the active drawing sheet

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation/cs.md): Adds an annotation to the current drawing sheet

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip/cs.md): Adds a clip group to the current drawing sheet

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser/cs.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews/cs.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol/cs.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save/cs.md): Saves the current sheet as a SVG file

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

**Poznámka** [Kreslicí modul](Draft_Workbench/cs.md) má také svůj vlastní [Výkres](Draft_Drawing/cs.md) pro umístění Kreslených objektů na papír. Má pár zvláštních možností nad standardními nástroji Výkresu a podporuje specifické objekty jako je [Kótování](Draft_Dimension/cs.md).

Na obrázku vidíte koncept modulu Výkresu. Dokument obsahuje konstrukční objekt, který chceme vyjmout do výkresu. Proto je vytvořena \"Stránka (Page)\". Stránka je realizována pomocí šablony, v tomto případě přes šablonu \"A3_Landscape\". Šablona je SVG dokument, který může obsahovat Váš běžný rámeček stránky, Vaše logo nebo dodržuje Vaše prezentační standardy.

Do stránky můžeme vložit jeden nebo více pohledů. Každý pohled má svoji pozici na stránce (Vlastnosti X,Y), měřítko (Vlastnost měřítko) a další vlastnosti. Pokaždé když se stránka, pohled nebo odkazovaný objekt změní, stránka změny zachytí a zobrazení se aktualizuje.



## Skriptování

V současnosti je uživatelské rozhraní (GUI) velmi omezené, proto je skriptovací API mnohem zajímavější. Následují příklady ukazují jak použít skriptovací API modulu Výkresu.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.



## Rozšíření modulu Výkres 

Některé poznámky k programovací stránce vykreslovacího modulu budou přidány na stránku [Dokumentace výkresu](Drawing_Documentation/cs.md). Je to příspěvek k rychlejšímu porozumění jak funguje modul výkresu, aby programátorům umožnily rychle začít s jejich programováním.

## External links 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


<div class="mw-translate-fuzzy">


{{docnav/cs|[Modul Díl](Part_Workbench/cs.md)|[The Raytracing workbench](Raytracing_Workbench/cs.md)}}


</div>


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/cs
