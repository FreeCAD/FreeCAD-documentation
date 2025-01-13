---
 GuiCommand:
   Name: TechDraw BrokenView
   Name/pl: Rysunek Techniczny: Widok przerwania
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw widok przerwania
   Workbenches: TechDraw_Workbench/pl
   Version: 1.0
   SeeAlso: TechDraw_View/pl
---

# TechDraw BrokenView/pl



## Opis

To narzędzie wstawia widok z przerwaniem, który jest oparty na istniejącym [widoku części](TechDraw_View/pl.md) lub jednym bądź wielu obiektach, takich jak [Zawartości](PartDesign_Body/pl.md) lub [Części](Std_Part/pl.md). Widok z przerwaniem wymaga też jednego lub więcej [szkiców](Sketcher_NewSketch/pl.md) definiujących położenie i rozmiar obszarów do usunięcia. Widok z przerwaniem zachowuje się podobnie do innych widoków. Kierunek rzutowania jest brany z istniejącego widoku części, kierunku ujęcia widoku w oknie widoku 3D lub kierunku normalnego wskazanej ściany.

<img alt="" src=images/TechDraw_BrokenView_example3d.png  style="width:350px;"> 
*Kształt do przerwania i szkice definiujące przerwanie.*

<img alt="" src=images/TechDraw_BrokenView_example2d.png  style="width:350px;"> 
*Otrzymany rezultat.*



## Użycie

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). Widok 3D determinuje początkowe wartości właściwości **Direction** i **XDirection** widoku przerwania.
2.  Wybierz obiekt, którego widok z przerwaniem chcesz utworzyć lub wybierz istniejący widok środowiska Rysunek Roboczy, który zawiera ten obiekt.
3.  Dodaj jeden lub więcej szkiców z liniami przerwania do zaznaczenia wybierając je w [widoku drzewa](Tree_view/pl.md). Każdy szkic powinien zawierać tylko linie równoległe. Możesz również skorzystać z innych obiektów z dwiema równoległymi liniami.
4.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wciśnij przycisk **<img src="images/TechDraw_BrokenView.svg" width=16px> [Wstaw widok z przerwaniem](TechDraw_BrokenView/pl.md)**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_BrokenView.svg" width=16px> Wstaw widok z przerwaniem**.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Widok z przerwaniem, formalnie obiekt {{Incode|TechDraw::DrawBrokenView}}, wywodzi się z [Widoku części](TechDraw_View/pl#Właściwości_-_Widok_części.md), formalnie obiektu {{Incode|TechDraw::DrawViewPart}} i dziedziczy wszystkie jego właściwości. Ma również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Broken View}}

-    **Breaks|LinkList**: Obiekty w widoku 3D, które definiują punkty początkowe / końcowe i kierunek przerwań w tym widoku.

-    **Gap|Length**: Rozmiar przerwy dla przerwań w tym widoku *(nieskalowana długość 3D)*.



## Uwagi

-   Przerwania muszą być pionowe lub poziome. Przerwania ukośne nie są wspierane.
-   Zobacz też [Wstaw widok](TechDraw_View/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wstaw widok z przerwaniem może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
profile = doc.Sketch
page = doc.Page

brokenView = doc.addObject("TechDraw::DrawBrokenView", "BrokenView")
page.addView(brokenView)
brokenView.Source= box
brokenView.Breaks = [doc.Sketch]
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw BrokenView/pl
