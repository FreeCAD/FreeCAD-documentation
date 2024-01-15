---
 TutorialInfo:l
   Topic: Analiza MES
   Level: Początkujący
   Time: Nie dotyczy
   Author: http://www.freecadweb.org/wiki/index.php?title=User:NewJoker NewJoker
   FCVersion: 0.21 lub nowszy
   SeeAlso: FEM_Workbench/pl
---

# FEM Geometry Preparation and Meshing/pl







## Kontekst

Przygotowanie geometrii i tworzenie siatek to kluczowe elementy preprocessingu symulacji MES (metoda elementów skończonych). Podczas gdy łatwo dostępne oprogramowanie do analiz połączone ze środowiskiem CAD (takie jak [środowisko pracy MES](FEM_Workbench/pl.md) we FreeCAD) zachęca do przeprowadzania symulacji na nowych projektach bez żadnych przygotowań, należy pamiętać, że MES to zaawansowana metoda i wymaga odpowiednio przygotowanej geometrii i siatki aby zapewnić prawidłowe wyniki. Stara zasada [*garbage in, garbage out*](https://pl.wikipedia.org/wiki/Garbage_in,_garbage_out) (śmieci na wejściu - śmieci na wyjściu) jest tu szczególnie istotna. Są jeszcze inne istotne ustawienia, od których w znaczącym stopniu zależy dokładność analiz MES (takie jak właściwości materiałów i warunki brzegowe), ale pierwsze etapy i jedne z najczęstszych źródeł błędów to właśnie przygotowanie geometrii i tworzenie siatek, opisane na tej stronie.



## Typy geometrii używanej do analiz MES we FreeCAD 

-   Linie - używane w analizach z elementami belkowymi
-   Powierzchnie - używane w analizach z elementami powłokowymi
-   Bryły - używane w analizach z elementami bryłowymi



## Wybór typu geometrii 

Podczas gdy większość modeli CAD składa się z brył, często bardzo zalecane jest użycie linii i powierzchni w analizach MES jeśli pozwala na to dana konstrukcja:

-   jeśli część jest smukła (długa i wąska) i przypomina belkę oraz ma regularny przekrój należący do jednego z obecnie wspieranych typów przekrojów belkowych (prostokątny, okrągły lub rurowy) to powinna być liczona z użyciem elementów belkowych (chyba że występują pewne specyficzne formy obciążenia, odpowiedzi lub detale geometrii, których nie można pominąć, a które sprawiają, że to założenie upraszczające jest nieprawdziwe). Należy po prostu narysować linię środkową (kilka rad na temat jej uzyskiwania z istniejącej geometrii bryłowej można znaleźć w [tym wątku na forum](https://forum.freecad.org/viewtopic.php?t=81589)) i zdefiniować odpowiedni [przekrój belki](FEM_ElementGeometry1D/pl.md) z opcjonalnym [obrotem](FEM_ElementRotation1D/pl.md). Nie ma jednej przyjętej zasady kiedy można używać elementów belkowych, ale często zaleca się aby wymiary przekroju były \< 1/10 długości części żeby można było zastosować teorię belek.

<img alt="" src=images/FEM_beam_model.JPG  style="width:600px;">



*Smukła część nadająca się do analizy przy pomocy elementów belkowych - podświetlona linia środkowa*

-   jeśli część jest cienkościenna (np. konstrukcje blachowe) to powinna być liczona z użyciem elementów powłokowych (chyba że potrzebne są dokładne wyniki związane z kontaktem lub problem stanowią pewne ograniczenia elementów powłokowych). Jest to bardzo istotne i często pomijane. Do uzyskania odpowiedniej dokładności wyników (zwłaszcza gdy występuje zginanie) potrzeba kilku elementów (co najmniej 3-5) po grubości. W przypadku części cienkościennych, zwykle prowadzi to do uzyskania dużych siatek (szczególnie gdy używane są elementy czworościenne, ponieważ sześciościenne nie mogą być wygenerowane we FreeCAD) i znacznego zwiększenia kosztu obliczeń (wymaganej mocy komputera i czasu analizy). Aby uzyskać geometrię odpowiednią do analizy z użyciem elementów powłokowych, należy narysować powierzchnię środkową części (kilka rad na temat jej uzyskiwania z istniejącej geometrii bryłowej można znaleźć w [tym wątku na forum](https://forum.freecad.org/viewtopic.php?t=67505), [tym](https://forum.freecad.org/viewtopic.php?t=71821) oraz [tym](https://forum.freecad.org/viewtopic.php?t=81834)) i zdefiniować odpowiednią [grubość](FEM_ElementGeometry2D/pl.md). Tu również nie ma jednej przyjętej zasady, ale zaleca się aby grubość była \< 1/10 typowego wymiaru globalnego (długość/szerokość) części żeby można było zastosować teorię powłok.

<img alt="" src=images/FEM_shell_model.JPG  style="width:600px;">



*Cienkościenna część nadająca się do analizy przy pomocy elementów powłokowych - podświetlona powierzchnia środkowa*

Należy pamiętać, że elementy belkowe i powłokowe w CalculiX nie są prawdziwymi elementami tego typu (nie korzystają ze sformułowań elementów belkowych/powłokowych znanych z literatury i innego oprogramowania) - wewnętrznie są przekształcane w elementy bryłowe. Pomimo tego, zaleca się korzystanie z nich w wyżej wymienionych przypadkach.



## Poprawność geometrii 

Geometria używana w analizach MES musi być poprawna. Przede wszystkim, nie mogą występować żadne przenikania. Jest to częsty problem, zwykle występujący gdy złożenia są modelowane bez odpowiednich połączeń między częściami. Narzędzie [Część: Wycinek z przekroju](Part_SectionCut/pl.md) może pomóc w znalezieniu takich przenikań między częściami. Oczywiście narzędzie [Część: Połączenie](Part_Fuse/pl.md) może pomóc je naprawić jeśli są celowe. Inne problemy z geometrią (takie jak geometrie typu non-manifold, zbędne krawędzie i ściany itp.) również muszą być naprawione przed przystąpieniem do tworzenia siatki. Narzędzie [Część: Sprawdź geometrię](Part_CheckGeometry/pl.md) może być pomocne, ale istotna jest też wizualna ocena. Przy przygotowywaniu symulacji z użyciem elementów bryłowych, w razie wątpliwości czy część faktycznie jest bryłą czy tylko zamkniętą powłoką, wyżej wymienione narzędzia (Część: Wycinek z przekroju i zakładka *Zawartość kształtu* w wynikach narzędzia Część: Sprawdź geometrię) mogą rozwiać te wątpliwości.



## Upraszczanie geometrii 

Projekty przygotowane w programach CAD często są zbyt szczegółowe żeby nadawały się do analiz MES. W wielu przypadkach konieczne jest najpierw ich uproszczenie. Ten krok jest często pomijany a jest bardzo istotny, ponieważ może być trudno uzyskać dobrą siatkę jeśli część jest zbyt szczegółowa a nawet jeśli uda się w końcu uzyskać taką siatkę, to może być bardzo gęsta, prowadząc do przesadnie długiego czasu rozwiązywania. Zatem należy zawsze przyjrzeć się projektowi i postarać się go uprościć tak bardzo jak to możliwe, zostawiając tylko te cechy geometrii, które mogą mieć istotny wpływ na wyniki (wytrzymałość/sztywność), więc nie można ich pominąć. Następujące cechy zwykle są pomijane:

-   małe zaokrąglenia i sfazowania,
-   małe otwory,
-   inne małe detale,
-   spawy,
-   śruby, gwinty,
-   elementy dekoracyjne (loga, grawerunki).

Narzędzie [Część: Usuwanie cech](Part_Defeaturing/pl.md) i dodatkowe [środowisko pracy Upraszczanie](Defeaturing_Workbench/pl.md) mogą być pomocne podczas upraszczania części do analiz.

<img alt="" src=images/FEM_bracket_original.PNG  style="width:400px;">



*Oryginalna geometria kątownika*

<img alt="" src=images/FEM_bracket_simplified.PNG  style="width:400px;">



*Geometria kątownika uproszczona przy pomocy samego narzędzia Część: Usuwanie cech*

W przypadku złożeń (więcej o nich w jednej z kolejnych sekcji), często niektóre części można wykluczyć z symulacji i zastąpić warunkami brzegowymi jeśli były one połączone z częściami podlegającymi analizie. Takie podejście jest prawidłowe jeśli wykluczone części są znacznie sztywniejsze (w rozumieniu sztywności strukturalnej, więc biorąc pod uwagę nie tylko materiał, ale też geometrię części) niż analizowane części, z którymi były połączone. Jest tak dlatego, że warunki brzegowe blokady przemieszczeń wprowadzają sztywność (jakby analizowana część była połączona z nieskończenie sztywnym komponentem) a podpory sprężyste, takie jak elementy typu sprężyna, nie są dostępne w środowisku pracy MES programu FreeCAD w przypadku korzystania z solvera CalculiX (Elmer ma zaimplementowane [sprężyny](FEM_ConstraintSpring/pl.md)).

Upraszczanie geometrii do analiz MES może też oznaczać jej cięcie w jednej z płaszczyzn symetrii aby skorzystać z założenia symetrii planarnej w symulacji. Jest ono prawidłowe tylko gdy wszystkie poniższe aspekty modelu wykazują symetrię w danej płaszczyźnie:

-   geometria,
-   obciążenia,
-   warunki brzegowe,
-   odpowiedź (należy uważać w przypadku analiz częstotliwości drgań własnych i wyboczenia korzystających z symetrii - nie uzyska się asymetrycznych postaci drgań własnych i wyboczenia).

Korzystanie z symetrii (1/2, 1/4 lub 1/8 modelu) jest zalecane gdy tylko wchodzi to w grę, ponieważ można w ten sposób znacznie zredukować koszt obliczeń. Inną zaletą jest to, że eliminowane są niektóre ruchy sztywne, dzięki czemu łatwiej jest związać część. Warunek brzegowy symetrii powinien być zadany na ściany należące do płaszczyzny symetrii:

-   przesunięcie w kierunku normalnym do płaszczyzny symetrii powinno być zablokowane dla części bryłowych,
-   przesunięcie w kierunku normalnym do płaszczyzny symetrii i obroty w kierunkach innych niż wokół osi normalnej do płaszczyzny symetrii powinny być zablokowane dla części powłokowych i belkowych.

Przyłożoną siłę należy odpowiednio zredukować jeśli płaszczyzna symetrii przecina obszar jej przyłożenia (nieistotne w przypadku obciążenia ciśnieniem).

<img alt="" src=images/FEM_symmetric_vessel.JPG  style="width:400px;">



*Model 1/8 zbiornika cylindrycznego z warunkami brzegowymi symetrii i ciśnieniem wewnętrznym*



## Partycjonowanie geometrii 

Tak zwane partycjonowanie to podział geometrii na mniejsze segmenty. W innych programach jest to powszechnie używane aby umożliwić tworzenie siatek złożonych z elementów sześciościennych, ale we FreeCAD może być przydatne z innych powodów. Głównym zastosowaniem partycjonowania są przypadki gdy obciążenie (lub warunek brzegowy) trzeba przyłożyć tylko do wybranego obszaru na powierzchni części. Najłatwiejszym sposobem aby to osiągnąć jest utworzenie szkicu z odpowiednim konturem na ścianie i użycie narzędzia [Część: Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md) aby podzielić ścianę przy pomocy szkicu. Innym powodem partycjonowania może być przypadek gdy na jedną część trzeba nałożyć wiele materiałów (bez używania wielu części połączonych ze sobą). Wtedy partycjonowania można dokonać przy pomocy [płaszczyzny odniesienia](PartDesign_Plane/pl.md) i narzędzia Fragmentacja funkcją logiczną z trybem *Compsolid* (bryła złożona).

<img alt="" src=images/FEM_partition.JPG  style="width:400px;">



*Część ze ścianą podzieloną do zadania obciążenia lub warunku brzegowego*



## Geometrie złożeń 

Obecnie jednym z największych ograniczeń środowiska pracy MES jest brak wsparcia dla wielu siatek w jednej analizie. W praktyce oznacza to, że nie można nałożyć siatki na każdą część złożenia osobno i połączyć je odpowiednimi więzami do analizy. Zamiast tego, należy utworzyć pojedynczy obiekt zawierający wszystkie części złożenia i nałożyć siatkę na ten obiekt. Jest tu kilka opcji, wszystkie korzystające z [operacji boolowskich](Part_Module/pl#Narzędzia_do_przeprowadzania_operacji_logicznych.md). Wybór zależy od oczekiwanego efektu - czy poszczególne części/objętości i ich brzegi mają być wskazywalne (np. do przypisania materiałów lub definicji warunków brzegowych na wewnętrznych ścianach) czy nie:

-   [Część: Połączenie](Part_Fuse/pl.md) - scala części, uniemożliwiając ich indywidualne wskazywanie np. do definicji materiałów,
-   [Część: Utwórz kształt złożony](Part_Compound/pl.md) - tworzy obiekt złożony, umożliwiając wskazywanie poszczególnych części,
-   [Część: Połącz obiekty](Part_JoinConnect/pl.md) - działa jak Część: Połączenie, scalając części i uniemożliwiając ich indywidualne wskazywanie,
-   [Część: Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md) - działa jak Część: Utwórz kształt złożony, uniemożliwiając indywidualne wskazywanie części.

Należy wspomnieć, że jeśli części się stykają to na obiekcie boolowskim powstanie ciągła siatka i nie będzie potrzeby zadawania więzów do symulacji. Jeśli jest nawet drobna przerwa między częściami, siatka nie będzie ciągła i konieczne będą więzy takie jak [tie](FEM_ConstraintTie/pl.md) lub [kontakt](FEM_ConstraintContact/pl.md). Przeprowadzenie analizy częstotliwości drgań własnych to dobry sposób na sprawdzenie czy siatka jest ciągła czy nie - jeśli części nie są połączone to pierwsze postaci drgań własnych z deformacją zwizualizowaną przy pomocy [filtra wizualizacji deformacji](FEM_PostFilterWarp/pl.md) pokażą ich separację - częśći będą \"odlatywać\".

<img alt="" src=images/FEM_modal_separation.JPG  style="width:400px;">



*Pierwsza postać drgań własnych z filtrem wizualizacji deformacji - analizie poddano dwie kostki z niewielką początkową przerwą między nimi*

Wskazywanie wewnętrznych obszarów (ścian/objętości) bywa problematyczne. Może być konieczne do zdefiniowania różnych materiałów, obciążeń objętościowych lub warunków brzegowych (zwłaszcza w analizach termicznych i elektromagnetycznych). Istnieje kilka sposobów:

-   włączenie [płaszczyzny tnącej](Std_ToggleClipPlane/pl.md) na czas dokonywania wskazania i wybranie wewnętrznych ścian,
-   schowanie obiektu boolowskiego, zostawiając pokazaną tylko jedną z części, na których został on zastosowany i wybranie jej,
-   wybranie innego, zewnętrznego obiektu i edycja właściwości *References* w zakładce *Dane* określonej cechy analizy (wymaga ręcznego podania numeru obiektu geometrycznego)



## Podstawy tworzenia siatek 

Zbyt rzadka siatka to jedno z najczęstszych źródeł niedokładności i innych problemów w MES. Często jest to po części wina automatycznych ustawień generatorów siatek - zwykle tworzą bardzo rzadkie, nienadające się do analizy siatki gdy rozmiar elementu nie jest ręcznie podany tylko zostawiony z domyślną wartością. Należy zawsze znać przybliżone rozmiary części, zwłaszcza rozmiar najmniejszej istotnej cechy (może w tym pomóc narzędzie [Część: Pomiary liniowe](Part_Measure_Linear/pl.md)) i wprowadzać odpowiedni maksymalny rozmiar elementu w oparciu o to. W przypadku generowania siatki za pomocą narzędzia Gmsh, dostępne jest też ustawienie minimalnego rozmiaru elementu, które zapobiega powstawaniu zbyt drobnych elementów wokół małych cech geometrii, co może prowadzić do niepotrzebnie gęstych siatek (a czasem nawet crashy i zawieszania się programu FreeeCAD podczas prób generowania takich siatek). Ogólnie rzecz biorąc, lepiej zacząć od rzadszej siatki (generowanej szybciej), zobaczyć jak wygląda (potrzeba pewnego doświadczenia) i zagęścić ją w razie potrzeby. Często sens ma użycie gęstej siatki tylko w pobliżu obszarów zainteresowania (miejsc z dużymi gradientami/koncentracjami naprężeń - karby) i względnie rzadkiej siatki z dala od nich. Dzięki temu liczba elementów jest znacząco redukowana, co prowadzi do krótszego czasu obliczeń. Lokalnego zagęszczenia siatki można dokonać przy pomocy narzędzia [MES: Obszar siatki](FEM_MeshRegion/pl.md).

<img alt="" src=images/FEM_default_mesh.PNG  style="width:400px;">



*Domyślna, zbyt rzadka siatka*

<img alt="" src=images/FEM_globally_refined_mesh.PNG  style="width:400px;">



*Globalnie zagęszczona siatka*

<img alt="" src=images/FEM_locally_refined_mesh.PNG  style="width:400px;">



*Lokalnie zagęszczona siatka*

Wybór typu elementów skończonych nie jest łatwy i zależy od wielu czynników, ale ogólną zasadą jest to, że preferowane są elementy sześciościenne i czworokątne w stosunku do czworościennych i trójkątnych. Jednak skomplikowane geometrie nie mogą być dyskretyzowane przy pomocy elementów sześciościennych a FreeCAD nie potrafi ich w ogóle generować (jedynie siatki czworokątne mogą być generowane na powierzchniach - zobacz [ten wątek na forum](https://forum.freecad.org/viewtopic.php?t=20351)). Elementy sześciościenne można zaimportować z zewnętrznych generatorów takich jak [Gmsh](https://gmsh.info) i wykorzystać w środowisku pracy MES, co pokazano w [tym filmiku](https://www.youtube.com/watch?v=vylt24G7qj4&t=932s).

Wybór rzędu elementów (pierwszy lub drugi) zależy od warunków analizy, ale w większości przypadków preferowane są elementy drugiego rzędu. Jest tak zwłaszcza w przypadku elementów trójkątnych i czworokątnych - ich wersje pierwszego rzędu (liniowe) nie powinny być normalnie używane - zaleca się korzystanie z nich tylko jak z wypełniaczy w mało istotnych obszarach. Jednak ponieważ FreeCAD nie może generować elementów sześciościennych to można korzystać z liniowych czworościanów w niektórych przypadkach jeśli siatki są wystarczająco gęste. Dotyczy to zwłaszcza analiz z [kontaktem](FEM_ConstraintContact.md).



## Studia zbieżności siatki 

Studia zbieżności siatki są zalecane w przypadku wszystkich poważnych projektów wymagających dokładnych wyników. Wynika to z faktu, iż wyniki mogą się znacznie różnić, zbliżając się do poprawnych wartości wraz z zagęszczaniem siatki. Powinno się stosować następujące podejście:

1.  Po uzyskaniu pierwszych wyników i zanotowaniu ich (zwykle maksymalne naprężenia von Mises, naprężenia von Mises w danym miejscu i maksymalne przemieszczenia) należy zagęścić siatkę (globalnie lub lepiej lokalnie - przy pomocy narzędzia [MES: Obszar siatki](FEM_MeshRegion/pl.md)) i ponownie uruchomić analizę.
2.  Sprawdź wyniki i zanotuj ich nowe wartości. Jeśli odbiegają znacznie od początkowych wartości, ponownie zagęść siatkę i uruchom analizę.
3.  Powtórz proces jeśli wyniki nadal się znacząco zmieniają (zwykle rosną) wraz z zagęszczaniem siatki.

Zwykle pomaga utworzenie wykresu z danym wynikiem w funkcji gęstości siatki. W ten sposób łatwiej zauważyć kiedy wyniki zaczynają się zbiegać. Akceptowalna różnica w wynikach między dwoma uruchomieniami to zwykle kilka procent (np. poniżej 5%).

W niektórych przypadkach zdarza się, że maksymalne naprężenia rosną w nieskończoność niezależnie od tego, jak gęsta jest siatka. Taki niefizyczny efekt to osobliwość naprężeń. Może mieć kilka powodów:

-   siły skupione (punktowe) przyłożone do modeli bryłowych i powłokowych,
-   warunki brzegowe zadane w punktach (pojedynczych węzłach),
-   ostre narożniki,
-   kontakt występujący w narożniku.

Typowe sposoby radzenia sobie z osobliwościami naprężeń to:

-   zadawanie obciążeń i warunków brzegowych na małe powierzchnie zamiast punktów - zobacz sekcję o partycjonowaniu powyżej
-   dodawania małych zaokrągleń do ostrych narożników (wyjątek zasady pomijania małych zaokrągleń podczas upraszczania modeli do analiz),
-   dodanie plastyczności do zachowania materiału aby umożliwić redystrybucję naprężeń i ograniczyć je do wartości, na jakie pozwala definicja plastyczności przy obserwowaniu odpowiedniego poziomu uplastycznienia (odkształcenia plastyczne),
-   ignorowanie osobliwości i odczytywanie wyników z dala od nich jeśli to możliwe (w oparciu o regułę St. Venanta).

<img alt="" src=images/FEM_mesh_convergence.PNG  style="width:400px;">



*Typowe wykresy zbieżności siatki:<br>
- przemieszczenia ('''zielona krzywa''') zbiegają się szybko,<br>
- maksymalne naprężenia w karbie takim jak otwór ('''niebieska krzywa''') potrzebują więcej iteracji zagęszczania siatki aby się zbiegać,<br>
- maksymalne naprężenia w ostrym narożniku z warunkiem brzegowym utwierdzenia ('''czerwona krzywa''') nie zbiegają się w ogóle - występuje osobliwość naprężeń i potrzebne jest małe zaokrąglenie i zamodelowanie połączenia w bardziej realistyczny, podatny sposób aby uniknąć tego zjawiska.<br>*


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Geometry Preparation and Meshing/pl
