---
- GuiCommand:
   Name: Sketcher RemoveAxesAlignment
   Name/pl: Szkicownik: Usuń wyrównanie osi
   MenuLocation: Szkic - Narzędzia szkicownika - Usuń wyrównanie osi
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut: **Z** **R**
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/pl



## Opis

To narzędzie usuwa wyrównania osi *(wiązania <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Poziome](Sketcher_ConstrainHorizontal/pl.md), <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Pionowe](Sketcher_ConstrainVertical/pl.md))* z wybranych elementów, próbując zachować relację wiązań.



## Użycie

1.  Wybierz geometrię z wyrównaniem osi, na przykład [prostokąt](Sketcher_CreateRectangle/pl.md).
2.  Naciśnij przycisk <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Usuń wyrównanie osi** na pasku narzędzi.

W rezultacie wiązania *(poziome, pionowe)* zostaną usunięte. W przykładzie prostokąta, pozostaje on prostokątem, ale staje się obracalny.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Wybrany prostokąt z wiązaniami poziomymi i pionowymi.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Prostokąt po użyciu funkcji ''Usuń wyrównanie osi''.*





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/pl
