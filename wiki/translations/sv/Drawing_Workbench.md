# Drawing Workbench/sv

 


{{VeryImportantMessage|Development of the [[Drawing Workbench]] stopped in FreeCAD 0.16, and the new [[TechDraw Workbench]] aiming to replace it was introduced in v0.17. Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases.}}

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduction

Ritnings modulen tillåter dig att lägga ut ditt 3D arbete på papper. Det är, att lägga vyer av dina modeller i ett 2D fönster osh att sätta in det fönstret i en ritning, till exempel ett ark med en ram, en titel och din logotyp och slutligen skriva ut det arket. Ritningsmodulen är för närvarande under konstruktion och är mer eller mindre en teknologisk förhandstitt!


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">

## Gränssnittsverktyg

Detta är verktyg för att skapa, konfigurera och exportera 2D ritningsark

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Open scalable vector graphic](Drawing_Open_SVG.md): Opens a drawing sheet previously saved as an SVG file

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New A3 landscape drawing](Drawing_Landscape_A3.md): Creates a new drawing sheet from FreeCAD\'s default A3 template

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insert a view](Drawing_View.md): Inserts a view of the selected object in the active drawing sheet

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation.md): Adds an annotation to the current drawing sheet

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md): Adds a clip group to the current drawing sheet

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md): Saves the current sheet as a SVG file

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

**Note** The [Draft Workbench](Draft_Workbench.md) has its own [Draft\_Drawing](Draft_Drawing.md) too to place Draft objects on paper. It has a couple of extra capabilities over the standard Drawing tools, and supports specific objects like [Draft dimensions](Draft_Dimension.md).

I bilden så ser du huvudkoncepten av Ritningsmodulen. Dokumentet innehåller ett formobjekt (Schenkel) som vi vill göra en ritning av. Därför så är en \"Sida\" skapad. Sidan fås genom en mall, i detta fall \"A3\_Landskap\" mallen. Mallen är ett SVG dokument som kan innehålla din vanliga sidram, din logotyp eller så den överensstämmer med dina presentationsstandarder.

I denna sida så kan vi sätta in en eller fler vyer. Varje vy har en position på sidan (Egenskaper X,Y), en skalfaktor (Egenskap skala) och ytterligare egenskaper. Varje gång som sidan ,eller vyn, eller det refererade objektet ändras så regenereras sidan och visningen uppdateras.

## Skript

För tillfället så är arbetsflödet för slutanvändaren väldigt begränsat, så skript API\'t är intressantare. Här följer exempel på hur man använder skript API\'t för ritningsmodulen.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.

Here a script that can easily fill the [Macro\_CartoucheFC](Macro_CartoucheFC.md) leaf FreeCAD A3\_Landscape.

## Exempel

FreeCAD kommer med ett standardset med mallar, men du kan hitta fler på [Ritningsmallar](Drawing_templates/sv.md) sidan.

## Extending the Drawing Module 

Some notes on the programming side of the drawing module will be added to the [Drawing Documentation](Drawing_Documentation.md) page. This is to help quickly understand how the drawing module works, enabling programmers to rapidly start programming for it.

## Tutorials

-   [Drawing tutorial](Drawing_tutorial.md)

## External links 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


{{docnav/sv|Part Workbench/sv|Raytracing Workbench/sv}}


{{Drawing Tools navi

}} 

[Category:Obsolete Workbenches](Category:Obsolete_Workbenches.md)
