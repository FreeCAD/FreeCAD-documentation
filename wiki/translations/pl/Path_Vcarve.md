---
 GuiCommand:
   Name: Path Vcarve
   Name/pl: CAM: Wycięcie V
   MenuLocation: Ścieżka , Wycięcie V
   Workbenches: Path_Workbench/pl
   Version: 0.19
---

# Path Vcarve/pl



## Opis

Narzędzie <img alt="" src=images/Path_Vcarve.svg  style="width:24px;"> **Wycięcie V** służy przede wszystkim do grawerowania w linii środkowej <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> [Kształtu z tekstu](Draft_ShapeString/pl.md) na części. Jednakże, może być przydatne dla innych rodzajów operacji 2D.

W przeciwieństwie do grawerowania, które podąża za liniami w obrysie, Wycięcie V wykorzystuje frez w kształcie litery V i próbuje oczyścić obszar, przesuwając frez w dół środka obszaru i zmieniając głębokość cięcia. Ponieważ promień frezu w kształcie litery V zmienia się wraz z głębokością, zmienia się również szerokość cięcia. Rezultatem jest bardziej naturalnie wyglądające cięcie, szczególnie w przypadku czcionek szeryfowych.

![](images/Engravepath.png ) ![Example Vcarving Path](images/Vcarvepath.png ) ![](images/Vcarved.png ) ![](images/Scrolltest.png )

Algorytm Wycięcie V oblicza ścieżkę wzdłuż linii środkowej regionu przy użyciu diagramu Woronoja. Ta linia środkowa jest ścieżką, którą narzędzie będzie podążać w płaszczyźnie XY. Następnie oblicza \"maksymalny wpisany okrąg\" wzdłuż ścieżki. Jest to największy okrąg, jaki można narysować w tym punkcie i pozostać całkowicie wewnątrz obszaru oczyszczania. Korzystając z promienia okręgu i kąta wierzchołkowego frezu, obliczana jest głębokość cięcia.



## Użycie



### Przygotowanie kształtów do grawerowania 

-    **[<img src=images/Draft_ShapeString.svg style="width:24px"> [Kształt z tekstu](Draft_ShapeString/pl.md)**są użyteczne \"po wyjęciu z pudełka\".

-   Pliki SVG wymagają pewnego dopracowania, zarówno w edytorze, jak i w środowisku pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md):
    -   W edytorze *(np. [Inkscape](https://www.inkscape.org))*: upewnij się, że plik zawiera tylko ścieżki i że ścieżki są niezgrupowane. Upewnij się, że nie ma przecinających się ścieżek, *(w Inkscape)* użyj Ścieżka → Uprość i połącz, aby połączyć ścieżki, które się nakładają.
    -   Przełącz się na <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) w selektorze [środowisk pracy](Std_Workbench/pl.md).
    -   Zaimportuj SVG używając **Plik → Import → wybierz "SVG jako geometria"**.
    -   Wynik powinien wyglądać podobnie do tego:

        :   ![bez ramki](images/Svgimport.png )

        :   
            
*Powyżej: Wyniki importu "SVG jako geometria"*
            

:   

    :   Ścieżki z dziurami *(litery, winorośl na powyższym obrazku)* są importowane jako dwie oddzielne ścieżki (nazwane zgodnie z `Path905` i `Path905001` w oknie [Widoku drzewa](Tree_view/pl.md)), jedna z nich to dziura, a druga to kontur;. Zajmiemy się tym w następnym kroku

-   -   Aby uzyskać ściany 2D, **Wycięcie V** potrzebuje:
        -   Dla ścieżek bez otworów:
            1.  Wybierz ścieżkę
            2.  Wybierz **Modyfikacja → ![](images/)_[Ulepsz_kształt](Draft_Upgrade/pl.md)**
            3.  Następnie **Modyfikacja → ![](images/)_[Rozbij_kształt](Draft_Downgrade/pl.md)**
        -   Dla ścieżek z dziurami:
            1.  Wybierz ścieżkę zewnętrzną, a następnie wewnętrzną
            2.  Wybierz **Modyfikacja → ![](images/)_[Rozbij_kształt](Draft_Downgrade/pl.md)** **dwa razy**

        :   Niektóre ścieżki będą zachowywać się inaczej, więc może być konieczne pobawienie się **<img src="images/Draft_Upgrade.svg" width=16px> Ulepsz kształt** i **<img src="images/Draft_Downgrade.svg" width=16px> Rozbij kształt**, aż otrzymasz coś o nazwie: `Face<numer>`.
        :   Wynik końcowy powinien wyglądać następująco:
        :   ![bez ramki](images/Svgfaces.png )



### Tworzenie operacji Wycięcie V 

-   Przełącz na środowisko pracy **[<img src=images/Workbench_Path.svg style="width:16px"> [Część](Path_Workbench/pl.md)** w [selektorrze środowisk pracy](Std_Workbench/pl.md).
-   Dodaj zadanie, użyj obiektów o nazwie `Face<numer>` *(lub Kształt z tekstu)* jako podstawy, dodać kontroler narzędzia v-bit, ustawić posuwy, prędkości itp.
-   Operacja obsługuje tylko jeden obiekt (albo pojedynczy obiekt ściany, albo Kształtu z tekstu), więc dla każdego obiektu:
    -   Wybierz **Ścieżka → <img src="images/Path_Vcarve.svg" width=24px> Wycięcie V** z menu głównego. Spowoduje to otwarcie panelu konfiguracji.
    -   Otwórz zakładkę **Geometria bazowa** i dodaj wszystkie ściany Kształtu z tekstu lub ściany pojedynczego obiektu ściany uzyskanego powyżej
    -   Naciśnij **Zastosuj** i sprawdź wygenerowaną ścieżkę; w razie potrzeby dostosuj parametry operacji (w większości sytuacji można ustawić wyższy próg).
    -   Naciśnij **OK**, aby zakończyć



## Opcje

Pusto



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Umiejscowienie**: -

-    **Etykieta**: -


{{TitleProperty|Głębokość}}

-    **WysokośćPrześwitu**: -

-    **GłębokośćKońcowa**: -

-    **WysokośćBezpieczna**: -

-    **GłębokośćStartowa**: -

-    **KrokWDół**: -


{{TitleProperty|Wartości operacyjne}}

-    **OpGłębokośćKOńcowa**: -

-    **OpGłębokośćStartowa**: -

-    **OpZMaxPrzygotówki**: -

-    **OpZMinPrzygotówki**: -

-    **OpŚrednicaNarzędzia**: -


{{TitleProperty|Ścieżka}}

-    **Aktywna**: -

-    **Komentarz**: -

-    **TrybChłodzenia**: -

-    **WierzchołekStartowy**: -

-    **KontrolerNarzędzia**: -

-    **EtykietaUżytkownika**: -



#### Ukryte

-    **Baza**: -

-    **ObjektBazowy**: -

-    **KształtBazowy**: -

-    **SilnikWyrażeń**: -

-    **Etykieta2**: -

-    **Ścieżka**: -

-    **Proxy**: -

-    **Widoczność**: -



### Widok

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Vcarve/pl
