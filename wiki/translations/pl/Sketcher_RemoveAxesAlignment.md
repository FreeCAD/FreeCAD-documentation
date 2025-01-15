---
 GuiCommand:
   Name: Sketcher RemoveAxesAlignment
   Name/pl: Szkicownik: Usuń wyrównanie osi
   MenuLocation: Szkic , Narzędzia szkicownika , Usuń wyrównanie osi
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **R**
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Usuń wyrównanie osi** usuwa wyrównanie osi wybranych krawędzi, zastępując wiązania [poziome](Sketcher_ConstrainHorizontal/pl.md) i [pionowe](Sketcher_ConstrainVertical/pl.md) wiązaniami [równolegle](Sketcher_ConstrainParallel/pl.md) i [prostopadle](Sketcher_ConstrainPerpendicular/pl.md). Krawędzie można następnie obracać bez utraty ich ortogonalnej relacji.



## Użycie

1.  Wybierz dwie lub więcej krawędzi z wiązaniami poziomymi lub pionowymi, na przykład [prostokąt](Sketcher_CreateRectangle/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> '''Usuń wyrównanie osi'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> Usuń wyrównanie osi**.
    -   Użyj skrótu klawiaturowego: **Z**, a następnie **R**.



## Przykład

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Wybrany prostokąt z wiązaniami poziomymi i pionowymi.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Prostokąt po użyciu narzędzia.*



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/pl
