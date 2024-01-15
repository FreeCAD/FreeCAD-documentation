---
 TutorialInfo:l
   Topic:  Beton zbrojony w MES
   Level:  średnio zaawansowany
   Time:  60 minut
   Author: User:HarryvL   HarryvL, https://forum.freecadweb.org/memberlist.php?mode: viewprofile&u=18062 HarryvL
   FCVersion:  0.19 lub nowszy
   Files: nie dołączono
---

# Analysis of reinforced concrete with FEM/pl







## Kontekst

Środowisko pracy [MES](FEM_Workbench/pl.md) ma możliwość szacowania poziomu zbrojenia wymaganego w konstrukcji betonowej do uniknięcia kruchego pękania pod wpływem rozciągania lub ścinania.

<img alt="" src=images/Femconcrete_Wall_3D_rx_PSS.png  style="width:700px;">

Wykorzystywana jest metoda opisana w [\"Computation of reinforcement for solid concrete\", P.C.J. Hoogenboom and A. de Boer, HERON Vol. 53 (2008) No. 4](http://heronjournal.nl/53-4/3.pdf). W skrócie, jest to narzędzie do obróbki wyników z analiz w CalculiX, które oblicza naprężenia główne rozciągające w betonie z analizy liniowo sprężystej i używa ich do określenia minimalnego zbrojenia w 3 kierunkach wymaganego do uniknięcia zniszczenia. W analizie zakłada się, że beton nie może przenosić naprężeń rozciągających, podczas gdy stal jest wykorzystywana do maksymalnej nośności (osiąga uplastycznienie).

Wymagane zbrojenie jest wyrażone w formie stosunku zbrojenia. Jest to stosunek pola powierzchni stali do betonu. Przykładowo, stosunek 0.01 w kierunku X *(rx=0.01)* oznacza, że całkowite pole przekroju poprzecznego prętów zbrojenia przebiegających w kierunku X powinno wynosić 1% pola przekroju poprzecznego betonu, przez który pręty przechodzą. Hipotetyczny przekrój poprzeczny 1mx1m powinien w tym wypadku zawierać 0.01 m2 stali, co można osiągnąć używając 90 prętów zbrojeniowych o średnicy 12mm każdy *(pole przekroju poprzecznego stali = 90\*PI\*(0.012)\^2/4=0.0102 m\^2)*. Jeśli wymagany stosunek zbrojenia w tym przekroju betonu jest jednorodny to pręty powinny być umieszczone na równoodległej siatce 9x10 z odległością środek do środka ok. 10 cm. To nadal sensowna wartość gdzie zostaje wystarczająco dużo miejsca dla betonu między prętami i zapewnia wysokiej jakości osłonę. Znacznie większe wartości mogłyby prowadzić do bardzo gęstej siatki zbrojenia z potencjalnym ryzykiem złej jakości, podczas gdy znacznie mniejsze wartości mogłyby prowadzić do dużych pęknięć przy rozciąganiu w przekroju między prętami. W praktyce, typowy zakres to 0.002 do 0.02 *(= 0.2% do 2%)*. Więcej wskazówek można znaleźć w normach budowlanych.

Jeśli wymagany stosunek zbrojenia nie jest równomierny dla całego przekroju poprzecznego to przekrój można podzielić na podobszary z mniej lub bardziej jednorodnym stosunkiem i zbrojeniem nałożonym na te przekroje. Przykład zostanie przedstawiony później.

Dla ostrożności, potrzeba znacznie więcej niż to co oferuje środowisko pracy MES żeby zaprojektować bezpieczne i wytrzymałe konstrukcje betonowe. Przykładowo, ta metoda nie oblicza szerokości pęknięcia *(ważna dla wytrzymałości i funkcjonalności)*, dokładnych deformacji *(wyniki MES dla betonu są tu tylko liniowo-sprężyste)* ani nie uwzględnia wymogów kotwienia zbrojenia (powodującego wzrost wymaganych stosunków zbrojenia w obszarach kotwienia). Nie przewiduje też zgniatania betonu *(chociaż wskaźnik tego można uzyskać poprzez wyświetlenie naprężeń Mohra-Coulomba - zobacz dalej)*, co może oznaczać, że beton ulegnie zniszczeniu przed uplastycznieniem zbrojenia, powodując kruche zniszczenie całej konstrukcji. Te i inne ograniczenia oznaczają, że funkcjonalności tu opisywana może być używana tylko do oceny projektów koncepcyjnych, podczas gdy szczegółowe decyzje projektowe krytyczne dla bezpieczeństwa i eksploatacji powinny być podejmowane przez wykwalifikowanych specjalistów.



## Geometria modelu, obciążenia i podpory 

Chociaż ta funkcjonalność nie ma żadnych dodatkowych wymogów dotyczących geometrii, obciążeń i podpór, należy pamiętać, że ostre narożniki i podpory na krawędziach lub w wierzchołkach mogą wprowadzać koncentracje naprężeń i skutkować ekstremalnie wysokimi i nierealistycznymi stosunkami zbrojenia w tych obszarach lub w ich pobliżu.



## Właściwości materiału 

Środowisko pracy MES posiada specjalny obiekt materiału dla materiałów zbrojonych, który łączy materiał matrycy *(np. beton)* z materiałem zbrojenia *(np. stal)*. Do analizy betonu zbrojonego w MES muszą być określone przynajmniej te właściwości:

dla betonu:

-   moduł Younga (używany w analizie w CalcuiX do obliczenia deformacji sprężystych)
-   współczynnik Poissona *(j.w.)*
-   wytrzymałość na ściskanie *(używana podczas obróbki wyników do obliczenia naprężeń Mohra-Coulomba jako wskaźnika zniszczenia na skutek zgniatania lub ścinania w betonie)*
-   kąt tarcia *(j.w.)*

dla stali:

-   granica plastyczności (używana podczas obróbki wyników do obliczenia stosunków zbrojenia)

Należy pamiętać, iż przeprowadzane są trzy typy analizː

1.  Analiza sprężysta w CalculiX *(używając tylko sprężystych właściwości betonu)*. \# Krok obróbki wyników aby przeanalizować wymagane wzmocnienie *(używając tylko granicy plastyczności stali)*.
2.  Obliczanie naprężeń Mohra-Coulomba *(używając tylko właściwości wytrzymałościowych betonu, tzn. wytrzymałości na ściskanie i kąta tarcia)*. Naprężenia Mohra-Coulomba można obejrzeć w obiekcie prezentacji graficznej wyników VTK.



## Zastosowanie

W dalszej części tego artykułu zostanie przeanalizowanych kilka praktycznych przypadków aby omówić zastosowania tej metody.



### Belka swobodnie podparta z obciążeniem ciągłym 

Belka betonowa 4.0x0.1x0.3m jest obciążona ciężarem własnym i obciążeniem ciągłym 100kN *(25kN/m)*.

Właściwości materiałów są następujące:

dla betonu:

-   moduł Younga = 32 GPa *(domyślna wartość dla betonu w CalculiX)*
-   współczynnik Poissona = 0.17 *(domyślna wartość dla betonu w CalculiX)*
-   wytrzymałość na rozciąganie = 30 MPa (typ betonu C30/37)
-   kąt tarcia = 30 stopni

dla stali:

-   granica plastyczności = 500 MPa

Ciężar własny betonu został przyjęty jako 24kN/m\^3.

Wymagany poziom wzmocnienia w kierunku X jest bardzo wysoki *(5.4%)* i przekracza typowe wartości procentowe dozwolone przez normy aby zapobiegać kruchemu zniszczeniu. Wysokie naprężenia styczne w podporach również prowadzą do wymogu wysokiego poziomu zbrojenia:

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_RR_x_0.054.jpg  style="width:700px;">

Wykres Mohra-Coulomba pokazuje, że belka jest rzeczywiście podatna na zgniatanie po stronie ściskania *(naprężenia Mohra-Coulomba \> 0.0)*, co byłoby spodziewane z bardzo wysokim procentem zbrojenia:

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_MC.jpg  style="width:700px;">

Zarówno stosunek zbrojenia, jak i naprężenia Mohra-Coulomba wskazują, że występuje problem i że należy ponownie przemyślnie projekt koncepcyjny. Potencjalne rozwiązania to zwiększenie wymiarów belki lub użycie wstępnie sprężonego betonu. Więcej informacji można znaleźć w następującym wątku:

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p235003>



### Belka z podporą w połowie rozpiętości 

Belka betonowa 8.0x0.2x0.4m jest obciążona ciężarem własnym i obciążeniem ciągłym 160kN *(20kN/m)*.

Właściwości materiałów są następujące:

dla betonu:

-   moduł Younga = 32 GPa *(domyślna wartość dla betonu w CalculiX)*.
-   współczynnik Poissona = 0.17 *(domyślna wartość dla betonu w CalculiX)*.
-   wytrzymałość na rozciąganie = 25 MPa *(typ betonu B25)*.
-   kąt tarcia = 30 stopni.

dla stali:

-   granica plastyczności = 286 MPa *(zredukowana z 500 MPa aby uwzględnić współczynnik bezpieczeństwa 1.75)*.

Ciężar własny betonu został przyjęty jako 24kN/m\^3.

Wykres w ParaView dla wyeksportowanego pliku VTK pokazuje, że wymóg zbrojenia jest największy w górnej części belki przy centralnej podporze. Tam występuje największy moment gnący. Maksymalny stosunek zbrojenia to 0.02 przy samej górnej granicy praktycznie dopuszczalnego zakresu wspomnianego wcześniej:

<img alt="" src=images/Beam_with_Central_Support_rx_full.png  style="width:700px;">

Wymagane pole przekroju poprzecznego stali dla centralnej podpory można określić przy pomocy filtru całkowania w ParaView użytego na środkowym przekroju belki:

<img alt="" src=images/CoG_Reinforcement.png  style="width:700px;">

Panel w dolnej części rysunku pokazuje, że całkowite wymagane pole przekroju poprzecznego stali w tym przekroju to 389.6 mm\^2. Ponieważ jeden pręt zbrojenia o średnicy 12 mm ma pole przekroju 113mm\^2 to potrzebne będą 4 takie pręty, dając pole przekroju 452 mm\^2. Należałoby je umieścić w pobliżu górnej części belki, zachowując jednocześnie odpowiednią osłonę z betonu. Teoretyczny środek ciężkości zbrojenia można znaleźć poprzez całkowanie:

CoG_y = Integrate (rx \* y dy dz) / Integrate (rx dy dz)

CoG_z = Integrate (rx \* z dy dz) / Integrate (rx dy dz)

Te całki można również obliczyć w ParaView i zastosować je dla obecnego przypadku (zobacz dolne panele na rysunku powyżej):

CoG_y = 38961 / 389.6 = 100.0 mm

CoG_z = 134917 / 389.6 = 346.3 mm

co jest, jak można się spodziewać, w środku szerokości i w pobliżu górnej części belki.

Określony wymóg zbrojenia dobrze pokrywa się z tym oszacowanym metodami analitycznymi:

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=20#p235063>

Ostatecznie, należy sprawdzić naprężenia Mohra-Coulomba aby zweryfikować potencjalne zgniatanie betonu. Do tego sprawdzenia powinno się podzielić charakterystyczną wytrzymałość na ściskanie betonu *(25MPa)* przez odpowiedni współczynnik materiału *(\>1.0)*.



### Ściana usztywniająca z obciążeniem ciągłym 

Ściana 4.0x2.0x0.15m jest wsparta na dwóch kolumnach o szerokości 0.5m. Ściana jest obciążona ciężarem własnym i obciążeniem ciągłym 1.0MN na górze.

Właściwości materiałów są następujące:

dla betonu:

-   moduł Younga = 32 GPa *(domyślna wartość dla betonu w CalculiX)*
-   współczynnik Poissona = 0.17 *(domyślna wartość dla betonu w CalculiX)*
-   wytrzymałość na rozciąganie = 20 MPa
-   kąt tarcia = 30 stopni

dla stali:

-   granica plastyczności = 286 MPa

Ciężar własny betonu został przyjęty jako 24kN/m\^3.

Stosunek wzmocnienia w kierunku poziomym osiąga 0.014 (1.4%) w pobliżu dolnego środkowego przekroju ściany, zaś w kierunku pionowym 0.008 (0.8%) w pobliżu narożników ściany z kolumnami, gdzie naprężenia styczne są najwyższe:

<img alt="" src=images/Wall_3D.jpg  style="width:1000px;">

Powyższy rysunek pokazuje możliwe strefy stałego stosunku zbrojenia do projektowania zbrojenia. Chociaż wybrano minimalny stosunek zbrojenia 0.2%, trudno będzie uzyskać tak niską wartość w praktyce, biorąc pod uwagę, że odstępy nie powinny przekraczać praktycznego limitu *(np. 300mm)*. Nawet z rzadką siatką zbrojenia prętami 10mm *(pole przekroju poprzecznego = 78mm\^2)*, stosunek zbrojenia wynosiłby 2 \* 78 / (150 \* 300) = 0.0035 *(0.35%)*. *(Uwaga: wartość 2 wynika z faktu, iż siatka będzie umieszczona na obu stronach ściany)*. Jeśli dodamy jeszcze jeden pręt do siatki *(zmniejszając odległość o połowę)* to stosunek zbrojenia podwoi się osiągając 0.7% a jeszcze jeden pręt dałby 1%. Więc większość wymagania zbrojenia można by osiągnąć zaczynając z siatką z d=10mm przy odległościach 300x300mm i dodając pręty w kierunkach poziomym i pionowym, jak to jest wymagane. To pokryłoby całe wymaganie oprócz tego dla dolnej części ściany, gdzie można by dodać 3 pręty d=12mm, uzyskując stosunek zbrojenia 3 \* 113mm\^2 / (150mm \* 150mm) = 0.015 (1.5%). Tu zakłada się, że wysokość dolnej strefy to 150mm. Opcjonalnie, moglibyśmy wybrać 2 pręty o średnicy 16mm, które dałyby ten sam stosunek zbrojenia dla obszaru o wysokości 180mm.

Wreszcie, ocena naprężeń Mohra-Coulomba pokazuje, że zgniatanie betonu nie jest przewidywane w ścianie.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p234673>



### Głęboka belka z otwarciem 

Dokument FIB Practitioners\' Guide to Finite Element Modelling of Reinforced Concrete Structures zawiera przykład projektu głębokiej belki betonowej z otwarciem. Ten przykład jest tu użyty aby zademonstrować metodę \"Strut-and-Tie\". Wyniki zostaną porównane z tymi uzyskanymi w środowisku pracy FreeCAD MES.

Wymiary belki to 11.0x4.0x0.6m i jest ona obciążona na górze obciążeniem ciągłym 120kN/m i obciążeniem 5000kN wprowadzanym przez kolumnę o szerokości 1m. Wytrzymałość na ściskanie betonu to 0.75 x 0.6 x fc = 0.45 \* 35 = 15.8MPa a granica plastyczności stali zbrojeniowej to 315MPa.

Stosunki zbrojenia i naprężenia główne w betonie (tylko ściskanie) uzyskane z FreeCAD wynosząː

<img alt="" src=images/FIB_Deep_Concrete_Beam_1.png  style="width:1000px;">

Wymagane poziome zbrojenie (poniżej na czerwono) jest określone przez całkowanie stosunku zbrojenia poziomego w określonych pionowych cięciach (poniżej na czarno). Jest to przeprowadzone przy pomocy filtra całkowania w ParaView.

<img alt="" src=images/FIB_Reinforcement(2).jpg  style="width:700px;">

Wkładka do powyższego rysunku pokazuje porównanie wymogów zbrojenia (w mm\^2 dla stali) określonych we FreeCAD z tymi w raporcie FIB.

Poniżej pokazano jak działa całkowanie po wybranych liniach w ParaView:

<img alt="" src=images/FIB_Reinforcement_ry.jpg  style="width:700px;">

Wreszcie, wykres naprężeń głównych ściskających i rozciągających pokazuje przepływ naprężeń przez belkę.

<img alt="" src=images/FIB_Beam_Stresses_and_Cables.jpg  style="width:700px;">

Wzór naprężeń rozciągających sugeruje alternatywną koncepcję projektu przy pomocy cięgen wstępnie sprężonych (nałożone na biało). Ta koncepcja jest dokładniej wyjaśniona w następującym wątku: <https://forum.freecadweb.org/viewtopic.php?f=18&t=33049>



## Powiązane

-   [MES: Beton](FEM_Concrete/pl.md)


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Analysis of reinforced concrete with FEM/pl
