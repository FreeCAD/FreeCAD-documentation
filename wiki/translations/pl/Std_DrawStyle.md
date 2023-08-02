---
- GuiCommand:
   Name: Std DrawStyle
   Name/pl: Std: Styl kreślenia
   MenuLocation: Widok -> Styl kreślenia -> ...
   Workbenches: Wszystkie
   Shortcut: **V** **1** - **V** **7**
   SeeAlso: Std_SelBoundingBox/pl
---

# Std DrawStyle/pl



## Opis

Polecenie **Styl kreślenia** może zastąpić efekt {{PropertyView/pl|wyświetlanego trybu}} [właściwości](Property_editor/pl.md) obiektów w oknie [widoku 3D](3D_view/pl.md).



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Kliknij na czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_DrawStyleAsIs.svg" width=24px> [Styl kreślenia](Std_DrawStyle/pl.md)** i wybierz styl z menu podręcznego.
    -   W menu przejdź do **Widok → Styl kreślenia** i wybierz styl.
    -   W menu kontekstowym okna [widoku 3D](3D_view/pl.md) przejdź do **Styl kreślenia** i wybierz styl.
    -   Użyj jednego ze skrótów klawiaturowych: **V**, a następnie **1**, **2**, **3**, **4**, **5**, **6** lub **7**.



## Dostępne style kreślenia 



### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> Domyślny 

Styl **Domyślny** nie nadpisuje właściwości **Trybu wyświetlania** obiektów.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 identyczne obiekty, każdy z innym trybem wyświetlania ''(od lewej do prawej: "Tylko punkty", "Szkieletowy", "Cieniowany" i "Cieniowany z krawędziami")'' z zastosowanym stylem rysowania "Domyślny".*



### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Tylko punkty 

Styl **Tylko punkty** nadpisuje styl **Tryb wyświetlania** obiektów. Ten styl odpowiada trybowi wyświetlania *Tylko punkty*. Wierzchołki są wyświetlane w jednolitych kolorach. Krawędzie i ściany nie są wyświetlane.

![](images/Std_DrawStylePoints_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Tylko punkty"*



### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Szkieletowy 

Styl **Szkieletowy** nadpisuje styl **Tryb wyświetlania** obiektów. Ten styl odpowiada trybowi wyświetlania *Szkieletowy*. Wierzchołki i krawędzie są wyświetlane w jednolitych kolorach. Twarze nie są wyświetlane.

![](images/Std_DrawStyleWireframe_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Szkieletowy"*



### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Cieniowany z ukrytymi krawędziami 

Styl **Cieniowany z ukrytymi krawędziami** nadpisuje styl **Tryb wyświetlania** obiektów. Obiekty są wyświetlane tak, jakby były przekształcone w siatki trójkątów.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Cieniowany z ukrytymi krawędziami"*



### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Jednolity z krawędziami 

Styl **Jednolity z krawędziami** nadpisuje styl **Tryb wyświetlania** obiektów. Wierzchołki, krawędzie i ściany są wyświetlane w jednolitych kolorach.

![](images/Std_DrawStyleNoShading_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Jednolity z krawędziami"*



### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Cieniowany 

Styl **Cieniowany** nadpisuje styl **Tryb wyświetlania** obiektów. Ten styl odpowiada trybowi wyświetlania *Cieniowany*. Wierzchołki i krawędzie nie są wyświetlane. Powierzchnie są podświetlane w zależności od ich orientacji.

![](images/Std_DrawStyleShaded_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Cieniowany"*



### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Cieniowany z krawędziami 

Styl **Płaskie linie** zastępuje styl **Tryb wyświetlania** obiektów. Ten styl odpowiada trybowi wyświetlania *Cieniowany z krawędziami*. Wierzchołki i krawędzie są wyświetlane w jednolitych kolorach. Powierzchnie są podświetlane w zależności od ich orientacji.

![](images/Std_DrawStyleFlatLines_example.png ) 
*Te same obiekty z zastosowanym stylem rysowania "Cieniowany z krawędziami"*



## Uwagi

-   Obiekty w oknie [widoku 3D](3D_view/pl.md) mają również właściwość **Styl kreślenia**. Ta właściwość kontroluje typ linii używany dla krawędzi. Polecenie **Std: Styl kreślenia** nie zastępuje tej właściwości.
-   Makro do przełączania między dwoma stylami rysowania: [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle/pl.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DrawStyle/pl
