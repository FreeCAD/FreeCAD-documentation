---
 GuiCommand:
   Name: TechDraw StackTop
   Name/pl: Rysunek Techniczny: Przesuń poziom na górę
   MenuLocation: Rysunek Techniczny , Sortowanie , Przesuń poziom na górę
   Workbenches: TechDraw_Workbench/pl
   Shortcut: 
   Version: 0.21
   SeeAlso: TechDraw_StackBottom/pl, TechDraw_StackUp/pl, TechDraw_StackDown/pl.
---

# TechDraw StackTop/pl



## Opis

Narzędzie **Przesuń poziom na górę** przenosi widoki na górę porządku układania. Kolejność układania kontroluje widoczną głębokość widoków na stronie.



## Użycie

1.  Wybierz jeden lub więcej widoków na [stronie](TechDraw_PageDefault/pl.md) lub w oknie [widoku Drzewa](Tree_view/pl.md). W przypadku tego narzędzia oraz [Przesuń poziom na dół](TechDraw_StackBottom/pl.md), kolejność wyboru jest istotna.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Nacisnąć przycisk **<img src="images/TechDraw_StackTop.svg" width=16px> '''Przesuń poziom na górę'''**.
    -   Wybierz z menu **Rysunek Techniczny → Sortowanie → <img src="images/TechDraw_StackTop.svg" width=16px> Przesuń poziom na górę**.
3.  Właściwość **Kolejność sortowania** widoków jest zmieniana.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Kolejność układania można zmienić w skryptach poprzez zmianę właściwości {{Incode|StackOrder}} obiektu {{Incode|ViewObject}} widoku.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw StackTop/pl
