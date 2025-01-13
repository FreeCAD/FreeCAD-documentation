---
 GuiCommand:
   Name: Arch MultiMaterial
   Name/pl: Architektura: Narzędzia materiałowe
   MenuLocation: Architektura , Narzędzia materiałowe , Materiał wielowarstwowy
   Workbenches: Arch_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: Arch_SetMaterial/pl
---

# Arch MultiMaterial/pl



## Opis

Narzędzie Materiał wielowarstwowy definiuje listę [materiały](Material/pl.md) z nazwą i wartością grubości dla każdego materiału. Taką listę materiałów można następnie dodać do obiektu [Architektury](Arch_Workbench/pl.md) zamiast pojedynczego [materiału](Arch_SetMaterial/pl.md).

![](images/Arch_multimaterial_example.png )

Nie wszystkie obiekty Architektury mogą obecnie korzystać z materiałów wielowarstwowych, a sposób ich wykorzystania jest różny. Obecnie:

-   <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Ściana](Arch_Wall/pl.md) z materiałem wielowarstwowym użyje definicji materiału i grubości do stworzenia wielowarstwowej ściany.
-   <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Okno](Arch_Window/pl.md) z materiałem wielowarstwowym przypisze materiały o danej nazwie zdefiniowanej wewnątrz materiału wielowarstwowego do komponentów okna o tej samej nazwie lub typie *(patrz poniżej)*. Grubość materiału nie jest brana pod uwagę.
-   <img alt="" src=images/Arch_Panel.svg  style="width:24px;"> [Panel](Arch_Panel/pl.md) z materiałem wielowarstwowym użyje definicji i grubości materiału do utworzenia wielowarstwowego panelu.



## Użycie

1.  Stwórz najpierw serię **<img src="images/Arch_SetMaterial.svg" width=16px> [materiałów](Arch_SetMaterial/pl.md)**, które będą potrzebne w twoim materiale wielowarstwowym.
2.  Opcjonalnie, wybierz obiekt Architektury, któremu chcesz przypisać nowy materiał wielowarstwowy.
3.  Naciśnij przycisk **<img src="images/Arch_MultiMaterial.svg" width=16px> [Materiał wielowarstwowy](Arch_MultiMaterial/pl.md)**.
4.  Ustaw żądane warstwy materiału.



## Opcje

![](images/Arch_multimaterial_panel.png )

Po utworzeniu lub edycji materiału wielowarstwowego poprzez dwukrotne kliknięcie go w drzewie, dostępne są następujące opcje:

-   **Duplikuj** inny istniejący Materiał wielowarstwowy z tego samego dokumentu. Kopiuje to tylko wartości i nie łączy w żaden sposób tych dwóch materiałów.
-   Pole *Nazwa* ustawi również etykietę obiektu materiału.
-   Lista *Kompozycja* to lista różnych warstw materiału, które składają się na ten materiał. Każda warstwa ma nazwę, materiał i wartość grubości.
-   Kliknij **Dodaj**, aby dodać nową warstwę, **Up**, aby przesunąć wybraną warstwę w górę, **Down**, aby przesunąć wybraną warstwę w dół lub **Del**, aby usunąć wybraną warstwę.
-   Dwukrotne kliknięcie na **nazwę** warstwy umożliwia jej edycję, obiekt materiał wyświetli rozwijaną listę dostępnych [materiałów](Arch_SetMaterial/pl.md) w tym samym dokumencie, a grubość można ustawić na dowolną wartość w dowolnej jednostce.
-   Pola Nazwa i Materiał są obowiązkowe. Grubość może pozostać pusta *(przyjmie wtedy wartość 0)*.
-   Gdy Materiał wielowarstwowy zawiera warstwy o grubości równej zero, grubość ta jest uważana za zmienną. Obiekty Architektury, które używają tego materiału, takie jak Ściany i Panele, potraktują to odpowiednio i dadzą tej warstwie pozostałą dostępną przestrzeń, biorąc pod uwagę ich własną szerokość lub grubość.
-   Jeśli nazwiesz różne komponenty Materiału wielowarstwowego \"Rama\", \"Panel pełny\", \"Panel szklany\" lub \"Żaluzja\" i zastosujesz ten materiał do okna, podane materiały zostaną zastosowane do odpowiednich komponentów okna.



## Powiązania z IFC 

Z grubsza odpowiada to kombinacji [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) i [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).



## Ograniczenia



## Tworzenie skryptów 





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch MultiMaterial/pl
