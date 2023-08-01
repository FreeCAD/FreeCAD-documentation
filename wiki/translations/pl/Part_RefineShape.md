---
- GuiCommand:/pl
   Name:Part RefineShape
   Name/pl:Część: Udoskonal kształt
   MenuLocation:Część → Utwórz kopię → Udoskonal kształt
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Szybka kopia](Part_SimpleCopy/pl.md), [Utwórz przekształconą kopię](Part_TransformedCopy/pl.md), [Utwórz kopię kształtu elementu](Part_ElementCopy/pl.md), [Udoskonal kształt cechy](OpenSCAD_RefineShapeFeature/pl.md)
---

# Part RefineShape/pl



## Opis

Narzędzie środowiska Część **<img src="images/Part_RefineShape.svg" width=16px> [Udoskonal kształt](Part_RefineShape/pl.md)** tworzy nieparametryczną kopię o dopracowanym kształcie, czyli z \"oczyszczonymi\" niektórymi krawędziami i powierzchniami.

Po niektórych operacjach logicznych, takich jak [Połączenie](Part_Fuse/pl.md), pewne linie z poprzednich kształtów mogą pozostać widoczne. To narzędzie tworzy kopię wyniku operacji logicznej i usuwa te szwy.

**Alternatywnie**, aby stworzyć inne kopie nieparametryczne użyj narzędzi **<img src="images/Part_SimpleCopy.svg" width=16px> [Szybka kopia](Part_SimpleCopy/pl.md)**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Przekształcona kopia](Part_TransformedCopy/pl.md)**, oraz **<img src="images/Part_ElementCopy.svg" width=16px> [Kopia kształtu elementu](Part_ElementCopy/pl.md)**.

![](images/PartRefineShape_it.png ) 
*Oryginalny wynik działania funkcji logicznej z 11 ścianami ''(po lewej)'' oraz dopracowana kopia kształtu z 7 ścianami ''(po prawej)''.*



## Użycie

1.  Wybierz obiekt, który chcesz oczyścić i skopiować.
2.  Przejdź do menu **Część → Utwórz kopię → <img src="images/Part_RefineShape.svg" width=16px> Udoskonal kształt**.
3.  Tworzona jest ulepszona, niezależna kopia oryginalnego obiektu, oryginalny obiekt jest ukryty.

Od {{VersionPlus/pl|0.19}} rezultat ten jest domyślny dla parametrycznej *(połączonej)* kopii.

To zachowanie można zmienić w <img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Edytorze parametrów](Std_DlgParameter/pl.md):

1.  Przejdź do grupy podrzędnej: `BaseApp/Preferences/Mod/Part`
2.  Zmień wartość parametru `ParametricRefine` typu `Boolean` na {{FALSE/pl}}, aby uzyskać stare zachowanie *(niezależna kopia)*.

Zobacz inne parametry na stronie [Dostrajanie parametrów](Fine-tuning/pl.md).



## Uwagi

-   Funkcja ta może być używana jako ostatni etap prac nad modelowaniem w celu oczyszczenia kształtów w tradycyjnym przepływie pracy [konstrukcyjnej geometrii bryły](Constructive_solid_geometry/pl.md).
-   Funkcja ta może pomóc w oczyszczeniu modelu przed zastosowaniem innej funkcji, takiej jak np. [zaokrąglenie](Part_Fillet/pl.md).
-   To czyszczenie może powstrzymać drukarki 3D od drukowania niechcianych krawędzi, gdy model bryłowy zostanie wyeksportowany do formatu siatki.
-   Tej funkcji można również użyć po konwersji siatki na kształt *(funkcją [Kształt z siatki](Part_ShapeFromMesh/pl.md))*, aby wyczyścić szczątkowe krawędzie na płaskich ścianach.
-   Niektóre interesujące informacje o tym, co dzieje się z umiejscowieniem i jak uzyskać dostęp za pośrednictwem środowiska Python, można znaleźć w tym [temacie na forum](https://forum.freecad.org/viewtopic.php?t=77568#p675456).



## Ograniczenia

-   Algorytm udoskonalania działa tylko na powłokach. Dlatego wykonuje iterację po powłokach kształtu wejściowego, a następnie dla każdej powłoki tworzy nową powłokę z połączonymi ścianami, jeśli to możliwe. Oznacza to, że jeśli twój kształt wejściowy jest tylko powierzchnią, polilinią , krawędzią lub wierzchołkiem, to algorytm nie zrobi nic.
-   W przeciwieństwie do narzędzia <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD: Udoskonal kształt cechy](OpenSCAD_RefineShapeFeature/pl.md), narzędzie <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Udoskonal kształt](Part_RefineShape/pl.md) środowiska Część nie będzie samoczynnie aktualizować bryły, gdy zostaną zmienione kształty poprzedzające.



## Tworzenie skryptów 

Polecenie środowiska Python służące do dopracowania kształtu jest następujące:


```python
shape.removeSplitter()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/pl
