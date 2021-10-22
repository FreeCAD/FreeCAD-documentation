# TechDraw Hatch/ro
---
- GuiCommand:   Name:TechDraw Hatch   Workbenches:[MenuLocation:TechDraw → Hatch   Shortcut:   SeeAlso:[[TechDraw_Hatching|TechDraw Hatching](TechDraw_Workbench___TechDraw]].md)---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul de hașurarea/Hatch umple o regiune închisă în View cu un model de hașură/Hatch pattern. Modelele sunt creat ca fișiere SVG ori bitmap . Eșantion de modele SVG sunt disponibile la \"\.../Mod/Draft/Resources/patterns\".


</div>

The Hatch tool fills a closed region in a View with a hatch pattern, which can be _ tool uses a specific PAT pattern file, see [Hatching](TechDraw_Hatching.md) for details.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*SVG hatch pattern on a face*


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Select an closed region in a View. The region will turn green.
2.  Press the <img alt="" src=images/TechDraw_Hatch.png  style="width:16px;"> **Hatch** button
3.  You may need to press recompute <img alt="" src=images/View-rotate-right.png  style="width:16px;">.


</div>

1.  Select an closed region in a View.
2.  Press the **<img src="images/TechDraw_Hatch.svg" width=16px> [Hatch a Face using Image File](TechDraw_Hatch.md)** button
3.  A dialog will open where you can select the pattern file, the scale and color.


<div class="mw-translate-fuzzy">

## Note

-   Hașurarea este vulnerabilă la infama \"topological naming problem\". Cea mai bună practică este de a amâna hașurarea până când desenul este stabil.
-   Rețineți că modelele de hașură SVG nu sunt incluse atunci când o pagină de desen este salvată ca fișier Svg.


</div>

-   Hatching objects are vulnerable to the \"[topological naming problem](Topological_naming_problem.md)\". See [TechDraw LengthDimension](TechDraw_LengthDimension.md) for more information. It is recommended that hatching be one of the last steps in your drawing process.
-   Sample [SVG](SVG.md) patterns are available locally in


```python
$INSTALL_DIR/data/Mod/TechDraw/Patterns
```

where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example 
```python
/usr/share/freecad/data/Mod/TechDraw/Patterns
``` and also on [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).


<div class="mw-translate-fuzzy">

## Proprietăți

-    **Source**: Vederea și Fațeta care va prim modelul de hașură.

-    **Hatch Pattern**: Calea de acces completă și numele fișierului spre un nume de fișier cu model SVG .

-    **Hatch Color**: Modelul de hașurare va fi afișat în această culaore.

-    **Hatch Scale**: Modificator de dimensiune a modelului de hașurae.


</div>

-    **Source**: The View and Face to receive the hatch pattern.

-    **Hatch Pattern**: Full path and filename to an SVG pattern file.

-    **Hatch Color**: Hatch pattern will be displayed in this color.

-    **Hatch Scale**: Hatch pattern size modifier.


<div class="mw-translate-fuzzy">

## Script

Hașurarea poate fi adăugată la zonele din Views folosind Python.


</div>


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Hatch tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/ro
