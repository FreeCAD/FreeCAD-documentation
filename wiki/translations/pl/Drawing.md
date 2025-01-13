# Drawing/pl
## Wprowadzenie

W FreeCAD słowo \"[Rysunek](Drawing/pl.md)\" jest zwykle używane w odniesieniu do rzutu 2D [modelu 3D](Model/pl.md). Zazwyczaj jest on tworzony za pomocą środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).



## Użycie

1.  Zacznij od już zbudowanego [modelu 3D](Model/pl.md), utworzonego na przykład za pomocą środowiska [Projekt Części](PartDesign_Workbench/pl.md). W rzeczywistości każdy obiekt, który ma [Kształt](Shape/pl.md), w tym obiekty 2D, będzie odpowiedni.
2.  Przejdź do środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).
3.  Naciśnij **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [Wstaw nową domyślną stronę rysunku](TechDraw_PageDefault/pl.md)** lub **[<img src=images/TechDraw_PageTemplate.svg style="width:16px"> [Wstaw nową stronę przy użyciu szablonu](TechDraw_PageTemplate/pl.md)**, aby utworzyć stronę.
4.  Wybierz istniejący model, a następnie naciśnij **[<img src=images/TechDraw_View.svg style="width:16px"> [Wstaw widok](TechDraw_View/pl.md)** lub **[<img src=images/TechDraw_ProjectionGroup.svg style="width:16px"> [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md)**.
5.  Zostanie utworzony rzut 2D na stronę. Możesz teraz dostosować jego właściwości, takie jak **Skala**, **Obrót** i **Kierunek**.
6.  Gdy rysunek będzie gotowy, możesz nacisnąć **[<img src=images/TechDraw_ExportPageSVG.svg style="width:16px"> [Wyeksportuj stronę do formatu SVG](TechDraw_ExportPageSVG/pl.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width:16px"> [Wyeksportuj stronę do formatu DXF](TechDraw_ExportPageDXF/pl.md)**, lub użyć narzędzia [Std: Eksportuj](Std_Export/pl.md), aby wyeksportować stronę do formatu SVG, DXF lub PDF do dalszego wykorzystania w innym oprogramowaniu lub do wydrukowania.



## Uwagi

W nieformalnym użyciu \"Rysunek\" może być dowolną figurą geometryczną widoczną w [Widoku 3D](3D_view/pl.md), a zatem jego pojęcie może być mylone z pojęciem \"[Zawartości](Body/pl.md)\", \"[Części](Part/pl.md)\" lub \"[modelu](Model/pl.md)\".

Jednakże, gdy wymagana jest większa precyzja, należy dokonać rozróżnienia.

-   \"[Zawartość](Body/pl.md)\" *([Zawartość](PartDesign_Body.md) środowiska Projekt Części)* jest obiektem pochodnym od [Cechy środowiska Część](Part_Feature/pl.md) *(klasa`Part::Feature`)*, utworzonym za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md).
-   \"[Part](Part/pl.md)\" *([App Part](App_Part/pl.md))* służy do grupowania kilku \"[Zawartości](Body/pl.md)\" w celu utworzenia złożenia.
-   \"Rysunek\" jest rzutem 2D obiektu \"Zawartości\" lub \"Części\".


{{TechDraw Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/pl
