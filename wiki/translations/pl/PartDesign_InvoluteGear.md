---
- GuiCommand:
   Name: PartDesign InvoluteGear
   Name/pl: Projekt Części: Koło zębate ewolwentowe
   Icon: PartDesign_InternalExternalGear.svg
   MenuLocation: Projekt Części -> Koło zębate ewolwentowe ...
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: FCGear_Workbench/pl
---

# PartDesign InvoluteGear/pl



## Opis

Narzędzie to pozwala na utworzenie dwuwymiarowego profilu koła zębatego lub krzywej złożonej. Ten profil 2D jest w pełni parametryczny i może być wyciągnięty funkcją [Wyciągnięcie](PartDesign_Pad/pl.md) lub [Addytywna helisa](PartDesign_AdditiveHelix/pl.md).

Bardziej szczegółowe informacje można znaleźć również na stronach Wiki: [przekładnie](https://en.wikipedia.org/wiki/Gear) oraz [Zarys ewolwentowy](https://en.wikipedia.org/wiki/Involute_gear)

<img alt="" src=images/PartDesign_Involute_Gear_01.png  style="width:200px;">



## Użycie



### Utworzenie profilu 

1.  Opcjonalnie aktywuj właściwą zawartość.
2.  Przejdź do menu **Projekt Części → [<img src=images/PartDesign_InternalExternalGear.svg style="width:24px"> Przekładnia ewolwentowa ...**.
3.  Ustaw parametry zębatki.
4.  Kliknij **OK**.
5.  Jeśli koło zębate znajduje się poza aktywną zawartością: przeciągnij go i upuść do zawartości, aby zastosować dalsze funkcje, takie jak wyciągnięcie.



### Utworzenie koła zębatego czołowego 

1.  Wybierz profil koła zębatego w [widoku drzewa](Tree_view/pl.md).
2.  Naciśnij przycisk **<img src="images/PartDesign_Pad.svg" width=24px> [Wyciągnij](PartDesign_Pad/pl.md)**.
3.  Ustaw **Długość** wyciągnięcia na żądaną szerokość powierzchni czołowej koła zębatego.
4.  Kliknij na przycisk **OK**.



### Utworzenie koła zębatego walcowego 

1.  Wybierz profil koła zębatego w [widoku drzewa](Tree_view/pl.md).
2.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveHelix.svg" width=24px> [Addytywna helisa](PartDesign_AdditiveHelix/pl.md)**.
3.  Wybierz jako oś, wektor normalny profilu koła zębatego, czyli **Oś normalna szkicu** {{Version/pl|0.20}} *(We wcześniejszych wersjach można użyć **Bazowa oś Z**, o ile płaszczyzna profilu nie została zmieniona)*.
4.  Wybierz tryb **Wysokość - Obrót**.
5.  Ustaw **Wysokość** na żądaną szerokość czołową koła zębatego.
6.  Aby ustawić żądany kąt skrętu należy użyć [Wyrażenia](Expressions/pl.md) dla **Obrotów**.
    1.  Kliknij niebieską ikonę <img alt="" src=images/Bound-expression.svg  style="width:24px;"> po prawej stronie pola wprowadzania danych.
    2.  Wprowadź następującą formułę: `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, gdzie `25°` jest przykładem pożądanego kąta spiralnego *(znanego również jako wartość beta)*, a `InvoluteGear` jest **Nazwą** profilu.
    3.  Kliknij w przycisk **OK**, aby zamknąć edytor formuły.
7.  Kliknij w przycisk **OK**, aby zamknąć panel zadań.

Wskazówka: Aby uczynić kąt skrętu dostępnym parametrem, użyj \"właściwości dynamicznej\":

1.  Wybierz profil.
2.  W oknie [Edytora właściwości](Property_editor/pl.md) aktywuj opcję **Wyświetl wszystko** w menu kontekstowym.
3.  Ponownie w menu kontekstowym wybierz opcję **Dodaj właściwość**. Uwaga: ta pozycja jest dostępna tylko wtedy, gdy aktywna jest opcja **Wyświetl wszystko**.
4.  W oknie dialogowym **Dodaj właściwość**:
    1.  Wybierz `App::PropertyAngle` jako Typ.
    2.  Ustaw wartość `Gear` w polu Grupa,
    3.  Ustaw wartość `HelicalAngle` jako nazwę *(bez spacji)*,
    4.  Kliknij **OK**.
5.  Teraz pojawi się nowa właściwość **Helical Angle** *(spacja dodana automatycznie)*, z wartością początkową `0.0°`, staje się dostępna.
6.  Przypisz do nowej właściwości żądany kąt spiralny.
7.  W formule właściwości **Obrót** profilu AdditiveHelix można teraz odwołać się do `InvoluteGear.HelicalAngle` zamiast zakodowanej wartości np. `25°`; ponownie zakładając, że `InvoluteGear` jest właściwością **Nazwy** profilu.



### Wycięcie piasty dla wału wielowypustowego ewolwentowego 


{{Version/pl|0.21}}

1.  Aktywuj właściwą Zawartość.
2.  Utwórz profil wewnętrznego koła zębatego ewolwentowego z wymaganą liczbą rowków i dostosuj wartości kąta natarcia, współczynnika wysokości głowy zęba, wysokości stopy zęba i główny współczynnik zaokrąglenia. Zobacz również tabelę w [Uwagi](#Uwagi.md) poniżej dla wartości wykonalnych. Na przykład:
    -   
        **Zębatka zewnętrzna**
        
        : {{False/pl}}

    -   
        **Liczba zębów**
        
        : 12

    -   
        **Kąt natarcia**
        
        : 37.5°

    -   
        **Współczynnik wysokości głowy zęba**
        
        : 0.45

    -   
        **Współczynnik wysokości stopy zęba**
        
        : 0.7

    -   
        **Główny współczynnik zaokrąglenia**
        
        : 0.3
3.  Wybierz profil koła zębatego w [Widoku drzewa](Tree_view/pl.md)
4.  Naciśnij przycisk **<img src="images/PartDesign_Pocket.svg" width=16px> '''Kieszeń'''
**
5.  Ustaw **Typ** kieszeni na **Przez wszystkie**.
6.  Zaznacz opcję kieszeni **Symetrycznie do płaszczyzny**.
7.  Kliknij **OK**.



## Właściwości

-    **Współczynnik wysokości głowy zęba**: Wysokość zęba od koła podziałowego aż do jego wierzchołka, znormalizowana przez moduł. Domyślnie wynosi 1.0 dla standardowego systemu pełnej głębokości. {{Version/pl|0.21}}

-    **Współczynnik wysokości stopy zęba**: Wysokość zęba od koła podziałowego w dół do jego korzenia, znormalizowana przez moduł. Domyślnie wynosi 1,25 dla standardowego systemu pełnej głębokości. {{Version/pl|0.21}}

-    **Zarys zewnętrzny**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Wysoka dokładność**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Modułowość**: średnica podziałki podzielona przez liczbę zębów.

-    **Liczba zębów**: ustawia liczbę zębów.

-    **Kąt przyporu**: kąt ostry między linią działania a normalną do linii łączącej środki kół zębatych. Domyślnie jest to 20°

. Zobacz stronę [koło zębate ewolwentowe](https://en.wikipedia.org/wiki/Involute_gear) aby uzyskać więcej informacji.

-    **Przesunięcie profilu zęba**: Odległość, o jaką profil referencyjny jest przesunięty na zewnątrz, znormalizowana przez moduł. Domyślnie zero. Przesunięcie profilu może być dodatnie lub ujemne. {{Version/pl|0.21}}

-    **Zaokrąglenie korzenia zęba**: Promień zaokrąglenia u korzenia zęba, znormalizowany przez moduł. Domyślnie 0,38 zgodnie z definicją statywu ISO. {{Version/pl|0.21}}



## Uwagi

-   Aby dwa koła zębate mogły się zazębić, muszą mieć ten sam moduł i kąt nacisku. [Wyrażenia](Expressions/pl.md) mogą pomóc w zapewnieniu spójności. Ich odległość środkowa musi wynosić `(NumberOfTeeth + OtherGear.NumberOfTeeth) * Modules / 2` *(czyli w przypadku, gdy suma przesunięcia profilu wynosi zero)*. Odejmij liczbę zębów w przypadku przekładni wewnętrznej.

-   Przesunięcie profilu może być stosowane do zapobiegania podcięciu na kołach zębatych o małej liczbie zębów. Innym zastosowaniem jest regulacja odległości środkowej dwóch kół zębatych o danej liczbie zębów i module.

-   Podczas wizualnego sprawdzania poprawności siatki lub zakłóceń pomocna jest znacznie niższa wartość dla **Odchylenia**, np. 0.05 zamiast domyślnego 0.5. W przeciwnym razie reprezentacja w oknie [widoku 3D](3D_view.md) może być zbyt zgrubna.

-   Dla standardowych kół zębatych najbardziej powszechnym kątem nacisku jest 20 °, a następnie 14,5 °. Inne zastosowania, zwłaszcza [wielowypusty](https://en.wikipedia.org/wiki/Spline_(mechanical)), wykorzystują wyższe kąty.

-   W standardowym układzie pełnej głębokości stosuje się współczynnik addytywny 1,0 i dedytywny 1,25, co daje luz 0,25 *(różnica między addytywnością jednego biegu a dedytywnością drugiego)*. Rzeczywista długość zęba to suma obu współczynników, pomnożona przez moduł.

-   Zmniejszenie długości zębów może być wymagane, aby zapobiec podcięciu lub wzmocnić zęby *(patrz [zęby czopowe](https://khkgears.net/new/gear_knowledge/gear-nomenclature/stub-teeth.html))*. W przypadku przekładni wewnętrznych uzupełnienie *(tutaj skierowane do wewnątrz)* może wymagać skrócenia, aby uniknąć pewnych zakłóceń lub nieobrotowych boków; gdy jest to wskazane w połączeniu z dłuższymi zębami zębnika.

-   Dla wałów i piast z wielowypustem ISO 4156 definiuje następujące parametry:

:   {\| class=\"wikitable\"

\|- ! Kąt natarcia !! 30 ° (flat root) !! 30 ° (fillet root) !! 37,5 ° !! 45 ° \|- \| Współczynnik wysokości głowy zęba \|\| 0.5 \|\| 0.5 \|\| 0.45 \|\| 0.4 \|- \| Współczynnik wysokości stopy zęba \|\| 0.75 \|\| 0.9 \|\| 0.7 \|\| 0.6 \|- \| Współczynnik zaokrąglenia korzenia zęba \|\| 0.2 \|\| 0.4 \|\| 0.3 \|\| 0.25 \|}



## Ograniczenia

-   Obecnie nie ma możliwości regulacji grubości zęba. Ząb i przestrzeń zęba są rozmieszczone równomiernie na kole podziałowym. Dlatego jedynym sposobem na kontrolowanie luzu jest dostosowanie odległości środka w parowaniu przekładni.
-   Obecnie nie ma [podcięcia](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) w generowanym profilu przekładni. Oznacza to, że koła zębate z małą liczbą zębów mogą kolidować z zębami współpracującego koła zębatego. Dolna granica zależy od **Kąt docisku** i wynosi około 17 zębów dla 20° i 32 dla 14.5°. Większość praktycznych zastosowań toleruje brak podcięcia dla kół zębatych nieco mniejszych niż ta teoretyczna granica.



## Poradniki

Folm: [Jak zrobić przekładnie zębate w FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)



## Powiązane

-   [Środowisko pracy FCGear](FCGear_Workbench.md)





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/pl
