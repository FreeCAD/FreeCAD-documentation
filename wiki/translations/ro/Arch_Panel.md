---
- GuiCommand:/ro
   Name:Arch Panel   Name/ro:Arch Panel
   MenuLocation:Arch → Panel Tools → Panel
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**P** **A**
   SeeAlso:[Arch Panel Cut](Arch_Panel_Cut/ro.md), [Arch Panel Sheet](Arch_Panel_Sheet/ro.md)
   Version:0.15
---

# Arch Panel/ro


</div>

## Descriere

Acest instrument vă permite să construiți tot felul de elemente de tip panou, de obicei pentru construcții de panouri, cum ar fi proiectul [WikiHouse](http://www.wikihouse.cc/), dar și pentru toate tipurile de obiecte bazate pe un profil plat.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*Imaginea de mai sus prezintă o serie de obiecte de panou, realizate pur și simplu din contururi 2D importate dintr-un fișier DXF. Ele pot fi apoi rotite și asamblate pentru a crea structuri.*


<div class="mw-translate-fuzzy">

Din versiunea 0.17, Panoul Arch poate fi de asemenea utilizat pentru a crea profiluri ondulate sau trapezoidale:


</div>

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați o formă 2D (obiect Draft, fațetă sau Schetch) - opțional
2.  apăsați butonul **<img src="images/Arch_Panel.png" width=16px> [Arch Panel](Arch_Panel.md)
**, sau apăsați tasta **P** apoi tasta **A**
3.  Ajustați proprietățile dorite


</div>


<div class="mw-translate-fuzzy">

## Limite


</div>


<div class="mw-translate-fuzzy">

-   În prezent nu există un sistem automat pentru a produce foi de tăiere 2D de la obiectele panoului, însă o astfel de caracteristică se află în plan și va fi adăugată în viitor.
-   Acest instrument nu este disponibil în versiunile FreeCAD înainte de 0.15


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Panels share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The thickness of a panel can be adjusted after creation
-   Press **ESC** or the **'''Cancel'''** button to abort the current command.
-   Double-clicking on the panel in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property.
-   Panels can make use of [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the panel will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Panel\'s own Thickness value, after subtracting the other layers.


</div>

## Proprietăți

-    **Length**: The length of the panel

-    **Width**: The width of the panel

-    **Thickness**: The thickness of the panel

-    **Area**: The area of the panel (automatic)

-    **Sheets**: The number of sheets of material the panel is made of

-    **Wave Length**: The length of the wave for corrugated panels

-    **Wave Height**: The height of the wave for corrugated panels

-    **Wave Type**: The type of the wave for corrugated panels, curved, trapezoidal or spiked

-    **Wave Direction**: The orientation of the waves for corrugated panels

-    **Bottom Wave**: If the bottom wave of the panel is flat or not

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Panel poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții:


</div>


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Creates a `Panel` object from the given `baseobj`, which is a closed profile, and the given extrusion `thickness`.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width`, and `thickness` to create a block panel.
-   If a `placement` is given, it is used.

Exempluː 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```

## Tutoriale


<div class="mw-translate-fuzzy">

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav/ro|[Arch CompPanel](Arch_CompPanel.md)|[Panel Cut](Arch_Panel_Cut.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CompPanel.png |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Cut.svg}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel/ro
