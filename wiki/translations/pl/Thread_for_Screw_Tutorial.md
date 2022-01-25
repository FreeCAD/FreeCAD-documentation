---
- TutorialInfo:/pl
   Topic: Projektowanie wyrobu
   Level: Zaawansowany
   Time: 60 minut
   Author:[DeepSOIC](User_DeepSOIC.md), [Murdic](User_Murdic.md), vocx
   FCVersion:0.19
   Files: [https://forum.freecadweb.org/viewtopic.php?f=36&t=44668 Aktualizacja - Przewodnik: Tworzenie gwintów.]
---

# Thread for Screw Tutorial/pl





## Wprowadzenie

Ten poradnik jest zbiorem technik modelowania gwintów śrubowych w programie FreeCAD. Został on zaktualizowany dla wersji **0.19**, chociaż ogólny proces jest zasadniczo taki sam od v0.14, kiedy to poradnik ten został pierwotnie napisany. Zaktualizowana zawartość skupia się na użyciu <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench/pl.md), aby utworzyć gwint, oraz dodano nowe ilustracje dla metod 0 do 3.

W tradycyjnych systemach CAD modelowanie gwintów śrubowych jest odradzane, ponieważ stanowi duże obciążenie dla jądra modelowania, jak również podczas renderowania kształtów. W tradycyjnych systemach gwint nie musi być przedstawiany bezpośrednio w przestrzeni 3D, ponieważ można go wskazać z jego wymaganą charakterystyką na rysunku technicznym, który jest wysyłany do produkcji. Jednakże, wraz z popularyzacją produkcji dodatków *(druk 3D)*, istnieje obecnie realna potrzeba modelowania gwintów przestrzennych, aby wydrukować je dokładnie tak, jak zostały zaprojektowane. I właśnie dlatego powstał ten poradnik.

Wiele z prezentowanych tu technik zostało zebranych z różnych wątków forum:

-   [Techniki modelowania gwintu](https://forum.freecadweb.org/viewtopic.php?f=3&t=12593)
-   [Tworzenie gwintu: Nieoczekiwane rezultaty](https://forum.freecadweb.org/viewtopic.php?f=3&t=6506)

Zobacz też pomocne filmy:

-   [Wprowadzenie strategii projektowania śruby bez powszechnie spotykanych problemów.](https://forum.freecadweb.org/viewtopic.php?f=8&t=44259)

Należy pamiętać, że kształty gwintów zajmują dużo pamięci, a posiadanie tylko jednego gwintu w dokumencie może znacznie zwiększyć rozmiar pliku, dlatego zaleca się tworzenie gwintów tylko wtedy, gdy jest to absolutnie konieczne.

### Metoda 0. Zdobądź jedną z bibliotek do tworzenia części 

Korzystanie z modeli, które opracowały inne osoby, jest wygodne i pozwala zaoszczędzić wiele czasu. Zapoznaj się z stroną zawierającą informacje o [zewnętrznych Środowiskach pracy](external_workbenches.md).

W szczególności polecane są dwa zasoby, które mogą być zainstalowane z narzędzia [Addon Manager](Std_AddonMgr.md):

-   [Fasteners Workbech](https://github.com/shaise/FreeCAD_FastenersWB), aby wstawiać śruby parametryczne i podkładki zgodne z normami ISO. Śruby i nakrętki domyślnie nie pokazują gwintu, ale można to kontrolować za pomocą opcji.
-   [BOLTSFC](https://github.com/berndhahnebach/BOLTSFC), aby umieścić części standardowe z biblioteki BOLTS, które również odpowiadają standardom ISO.

<img alt="" src=images/T13_00_Threads_fasteners.png  style="width:" height="300px;"> 
*Różne standardowe wkręty ISO osadzone w Środowisku pracy Fasteners. Istnieje możliwość kontroli, czy obiekt przedstawia prawdziwy gwint, czy tylko zwyczajny cylinder.*

## Metoda 1. Używanie makrodefinicji 

-   W przeszłości, do wstawiania części z biblioteki BOLTS używano [Makra BOLTS](Macro_BOLTS.md). Teraz jest już ono nieaktualne. Zamiast tego należy użyć Środowiska pracy BOLTSFC.

Znany jest skrypt [Screw Maker](Macro_screw_maker1_2/pl.md) autorstwa ulrich1a, został użyty do stworzenia pojedynczych śrub, wkrętów i podkładek. Obecnie jest to już przestarzałe rozwiązanie. Stanowisko pracy Fasteners autorstwa shaise, zawiera kompletne makro do tworzenia śrub, wraz z paskiem narzędzi do wyboru odpowiedniego elementu.

## Metoda 2. Środowisko pracy Fasteners 

Użyj zewnętrznego Środowiska pracy [Elementy złączne](Fasteners_Workbench/pl.md), aby dodać/dołączyć różne elementy złączne do części. Środowisko to może być zainstalowane za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).

## Metoda 3. Imitacja przez ułożenie stosu krążków. 

w wielu przypadkach nie potrzebujemy rzeczywistych gwintów, potrzebujemy tylko wizualnej wskazówki, że gwinty tam będą.

Fałszywy gwint możemy utworzyć za pomocą ścieżki bez spirali, np. obracając profil piły lub układając w stosy tarcze o stożkowych krawędziach. Tego rodzaju sztuczny gwint jest trudny do rozpoznania obok prawdziwie ślimakowego poprzez zwykłą obserwację. Ta metoda jest dobra do wizualizacji obiektu przypominającego gwint, ale nie jest przydatna, jeśli musimy wydrukować rzeczywisty gwint techniką 3D.

<img alt="" src=images/T13_01_Threads_comparison_fake_real.png  style="width:" height="300px;"> 
*Po lewej: prosta śruba ze sztucznym, nie spiralnym gwintem. Z prawej: zwykła śruba z prawdziwym gwintem spiralnym. Gdy druk 3D nie jest potrzebny, do wizualizacji często wystarcza symulowany gwint.*

### Obrotowy profil piły zębatej 

1.  Kliknij w przycisk **[<img src=images/PartDesign_Body.svg style="width:16px"> [PatrDesign: Stwórz zawartość](PartDesign_Body.md)**.
2.  Kliknij w przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PatrDesign: Utwórz nowy szkic](PartDesign_NewSketch.md)**. Wybierz {{Value|Płaszczyznę XZ}}.
3.  Narysuj szkic zamknięty z odpowiednią średnicą wewnętrzną {{Value|10mm}}, zewnętrzna średnica wokół {{Value|12.6mm}}, gęstość {{Value|3mm}}, liczba ząbków {{Value|8}}, oraz wysokość całkowita {{Value|30mm}}.
4.  Wybierz narysowany szkic, a następnie kliknij na przycisk **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PatrDesign: Wyciągnij przez obrót](PartDesign_Revolution.md)**. Wybierz {{Value|Pionowa oś szkicu}}, i kliknij w **OK**.

<img alt="" src=images/T13_02_Threads_Sawtooth_sketch_profile.png  style="width:" height="300px;"> 
*Profil używany do stworzenia wyciągnięcia przez obrót, który będzie symulować gwint.*

<img alt="" src=images/T13_03_Threads_Sawtooth_revolution_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_04_Threads_Sawtooth_revolution_2.png  style="width:" height="300px;"> 
*Widok przekroju powstałego gwintu nie spiralnego poprzez obracanie profilu piły wokół osi pionowej.*

### Krążki ułożone w stosy 

1.  Powtarzamy dwa pierwsze kroki z poprzedniej sekcji.
2.  Narysuj szkic zamknięty z wymaganą średnicą wewnętrzną {{Value|10mm}}, średnicą zewnętrzną wokół {{Value|12,6mm}}, i podziałką {{Value|3mm}}, ale narysuj tylko jeden ząb piły.
3.  Wybierz narysowany szkic, a następnie kliknij na przycisk **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PatrDesign: Wyciągnij przez obrót](PartDesign_Revolution.md)**. Wybierz {{Value|Pionowa oś szkicu}}, i kliknij w **OK**.
4.  Wybierz obiekt wyjściowy {{Value|Wyciągnięcia przez obrót}}, kolejnie kliknij w **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign: Utwórz szyk liniowy](PartDesign_LinearPattern.md)**. Wybierz {{Value|Oś pionową szkicu}}. Dla imitacji gwintu z podziałką {{Value|3mm}}, ustaw **Długość** na {{Value|3}}, oraz wartość **Wystąpienia** na {{Value|2}}, następnie naciśnij przycisk **OK**. W ten sposób powstaną dwa kolejne krążki, jeden na drugim.
5.  Możesz dodać więcej krążków, zwiększając wartość **Wystąpienia** w formacji liniowej oraz zwiększając **Długośc**, która jest całkowitą długością imitowanego gwintu.

Opcje **Długośc** oraz **Wystąpienia** są powiązane ze sobą. Jeśli długość jest zbyt duża, ale liczba wystąpień nie jest wystarczająco duża, nastąpi rozdzielenie krążków, a obliczenie bryły zakończy się niepowodzeniem, ponieważ obiektem wynikowym musi być zawsze [jedna zwarta bryła](PartDesign_Body/pl.md). Na przykład, aby uzyskać całkowitą wysokość {{Value|30mm}}, ustaw wartość **Długość** na {{Value|27mm}} i **Wystąpienia** na wartość {{Value|10}}.

Jeśli chcesz, możesz dodać **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign: Dodatkowy cylinder](PartDesign_AdditiveCylinder.md)** o średnicy równej wewnętrznej średnicy krążków i o całkowitej wysokości gwintu. Dzięki temu wszystkie krążki zostaną połączone w jedną bryłę, co gwarantuje, że nie zostaną rozłączone.

<img alt="" src=images/T13_05_Threads_Stacked_discs_sketch.png  style="width:" height="300px;"> 
*Profil używany do tworzenia obrotowego krążka, który będzie używany do imitowania gwintu.*

<img alt="" src=images/T13_06_Threads_Stacked_discs_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_07_Threads_Stacked_discs_2.png  style="width:" height="282px;"> 
*Po lewej: pojedynczy krążek stworzony przez wyciągnięcie przez obrót. Po prawej: wiele krążków umieszczonych w formacji liniowej w kierunku osi Z, imitującej gwint spiralny.*

## Metoda 4. Modyfikacja *owinięciem* profilu pionowego. 

### Środowisko pracy Part Design 

Prawdziwy gwint składa się z zamkniętego profilu prowadzącego bryłę wzdłuż spiralnej ścieżki.

1.  Znajdując się w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md), kliknij w przycisk **[<img src=images/Part_Primitives.svg style="width:16px"> [Part: Bryły pierwotne](Part_Primitives/pl.md)** aby utworzyć **[<img src=images/Part_Helix.svg style="width:16px"> [Part: Helisę](Part_Helix/pl.md)**. Podaj odpowiednie wartości dla parametrów **Gęstość** {{Value|3mm}}, **Wysokość** {{Value|23mm}}, oraz **Promień** {{Value|10mm}}.
2.  Przejdź do środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), i kliknij na przycisk **[<img src=images/PartDesign_Body.svg style="width:16px"> [Projekt Części: Utwórz zawartość](PartDesign_Body/pl.md)**.
3.  Kliknij w przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Projekt Części: Utwórz nowy szkic](PartDesign_NewSketch/pl.md)**. Wybierz {{Value|płaszczyznę XZ}}.
4.  Narysuj zamknięty szkic z wymaganym profilem zębów gwintu, zwykle w kształcie trójkąta. W tym przypadku użyjemy wysokości {{Value|2,9 mm}}, która jest nieco mniejsza niż skok {{Value|3,0 mm}} stosowany dla ścieżki spirali. Profil nie może tworzyć samoprzecięć przy przesuwaniu się wzdłuż helisy, ani między zakrętami, ani na środku, dlatego nie można użyć szkicu przedstawionego dla układania krążków w stos.
5.  Wybierz utworzony szkic, a następnie kliknij na przycisk **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [Projekt Części: Rozciągnij wybrany rysunek wzdłuż ścieżki ...](PartDesign_AdditivePipe/pl.md)**. W polu **Ścieżka do wyciągnięcia**, kliknij w pole **Obiekt**, i wybierz wcześniej utworzony obiekt helisy. Następnie zmień **Rodzaj orientacji** to {{Value|Wektor Freneta}} tak aby profil przebiegał po ścieżce bez skręcania, następnie naciśnij przycisk **OK**.
6.  Gdy okno dialogowe prosi o odnośnik, wybierz {{Value|Twórz odniesienie}}.
7.  Tworzona jest cewka spiralna, ale nie ma centralnego korpusu ani wału.
8.  Kliknij w przycisk **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [Projekt Części: Dodatkowy cylinder](PartDesign_AdditiveCylinder/pl.md)** z odpowiednimi wartościami dla **Promień** {{Value|10mm}} oraz **Wysokość** {{Value|29.9mm}} aby dotknąć reszty gwintu spiralnego i automatycznie się z nim połączyć.
9.  Dodatkowe operacje logiczne są potrzebne, aby ukształtować ostre końce cewki. Na przykład, można użyć funkcji dodawania, aby dodać łeb do śruby i czubek.

<img alt="" src=images/T13_08_Threads_Helical_thread_profile.png  style="width:" height="300px;"> <img alt="" src=images/T13_09_Threads_Helical_thread_path.png  style="width:" height="300px;"> 
*Z lewej: profil dla gwintu spiralnego. <br>Z prawej: ścieżka spiralna, która zostanie użyta do wyciągnięcia.*

<img alt="" src=images/T13_10_Threads_Helical_thread_coil.png  style="width:" height="300px;"> <img alt="" src=images/T13_11_Threads_Helical_thread_coil_sliced.png  style="width:" height="300px;"> 
*Z lewej: spirala wynikająca z operacji przeciągnięcia profilu zamkniętego wzdłuż ścieżki spiralnej. <br>Po prawej: widok przekroju zwoju powstałego w wyniku operacji przeciągania.*

<img alt="" src=images/T13_12_Threads_Helical_thread_cylinder.png  style="width:" height="300px;"> <img alt="" src=images/T13_13_Threads_Helical_thread_finished.png  style="width:" height="300px;"> 
*Z lewej: spirala śrubowa połączona z centralnym cylindrem w celu utworzenia korpusu śruby. <br>Po prawej: więcej elementów, łeb i czubek, dodane w celu poprawienia kształtu śruby.*

### Środowisko pracy Part 

Proces ten można również wykonać za pomocą narzędzi środowiska pracy [Część](Part_Workbench/pl.md).

1.  Znajdując się w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) kliknij w przycisk **[<img src=images/Part_Primitives.svg style="width:24px"> [Tworzenie brył parametrycznych](Part_Primitives/pl.md)** aby utworzyć **[<img src=images/Part_Helix.svg style="width:24px"> [Część: Helisa](Part_Helix/pl.md)**. Podaj odpowiednie wartości dla parametrów **Gęstość** {{Value|3mm}}, **Wysokość** {{Value|23mm}} i **Promień** {{Value|10mm}}.

Teraz możesz przystąpić do dodawania innych elementów pierwotnych, takich jak **[<img src=images/Part_Cylinder.svg style="width:16px"> [Część: Cylinder](Part_Cylinder/pl.md)** , lub innych kształtów, aby posłużyć się funkcją **[<img src=images/Part_Fuse.svg style="width:16px"> [Część: Suma](Part_Fuse/pl.md)** lub **[<img src=images/Part_Cut.svg style="width:16px"> [Część: Wytnij](Part_Cut.md)**.

<img alt="" src=images/T13_14_Threads_components.png  style="width:" height="300px;"> 
*Tworzenie zwoju gwintu poprzez przesuwanie pionowego profilu, (1) the [szkic profilu](sketch.md), (2) [helical](Part_Helix.md) ścieżka przeciągania, oraz (3) wynik [przeciągnięcia](Part_Sweep/pl.md).*

### Sztuczki wzmagające sukces 

-    **Reguła 1.**
    

Wyciągnięty wzdłuż spirali profil nie może zawierać krawędzi, które się przecinają lub stykają, ponieważ utworzy nieprawidłową bryłę. Dotyczy to zarówno profilu poruszającego się wzdłuż elementu spiralnego, jak i przecięć w jego środku. Próby wykonania z użyciem tego elementu operacji logicznych (bezpiecznik lub przecięcie) najprawdopodobniej się nie powiodą. Należy sprawdzić jakość wykonania cewki za pomocą funkcji **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part: Sprawdź geometrię](Part_CheckGeometry.md)**. Jeśli będą zgłaszane samoprzecięcia, musisz zwiększyć skok spirali.

<img alt="" src=images/T13_15_Threads_self_intersection.png  style="width:" height="300px;"> <img alt="" src=images/T13_16_Threads_no_self_intersections_OK.png  style="width:" height="300px;"> 
*Po lewej: nieprawidłowy przebieg wygenerowany przez zastosowanie bardzo małego skoku helisy w stosunku do wysokości profilu trójkątnego. <br>Po prawej: skok, który jest wystarczająco duży i nie powoduje samoistnych przecięć.*

-    **Reguła 2.**Gdy cylinder jest dodawany do cewki w celu utworzenia głównego trzonu śruby, nie może być styczny z profilem cewki. Oznacza to, że cylinder nie może mieć tego samego promienia jak wewnętrzny promień gwintu, ponieważ jest bardzo prawdopodobne, że nie powiedzie się operacja fuse. Ogólnie rzecz biorąc, należy unikać geometrii stycznych do elementów przeciągnięcia, takich jak ściany styczne lub krawędzie styczne do ścian, z którymi nie są połączone. Aby uzyskać dobre połączenie logiczne, wyciągnięta cewka oraz cylinder muszą się przecinać.

Sprawdź jakość połączenia za pomocą funkcji **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part: Sprawdź geometrię](Part_CheckGeometry.md)**, jeśli zgłaszane są powierzchnie współpłaszczyznowe, zwiększ promień cylindra o niewielką wartość.

-   Jeśli cewka i cylinder są ze sobą styczne, to jeśli nawet pierwsza operacja połączenia się powiedzie, to może się nie powieść w kolejnych krokach z trzecią bryłą.
-   Jest to ograniczenie jądra technologii OpenCASCADE *(OCCT)*, na ogół nie radzi sobie dobrze z operacjami między powierzchniami współpłaszczyznowymi.

<img alt="" src=images/T13_17_Threads_tangent_faces.png  style="width:" height="300px;"> <img alt="" src=images/T13_18_Threads_no_tangent_faces_OK.png  style="width:" height="300px;"> 
*Po lewej: bryła cylindra jest styczna do wewnętrznego promienia gwintu, może to spowodować nieprawidłowe połączenie funkcja logiczną. <br>Po prawej: cylinder ma nieco większy promień, więc dwa elementy brył przecinają się, wówczas połączenie funkcją logiczną będzie prawidłowe.*

-    **Reguła 3.**Wewnętrzny cylinder posiada linię szwu. Należy unikać umieszczania początku spirali wzdłuż tego szwu. Należy obrócić spiralę lub cylinder o kilka stopni.

-    **Wskazówka nr 1.**Promień spirali nie ma znaczenia, chyba że spirala jest stożkowa. Liczy się tylko gęstość zwojów (pitch) i wysokość spirali. Oznacza to, że możesz użyć jednej **[<img src=images/Part_Helix.svg style="width:16px"> [Part: Helisy](Part_Helix.md)** *(spirali)* do wygenerowania określonej liczby zwojów gwintu o jednakowym skoku. To, co decyduje o pozycji powstałej cewki, to pozycja profilu [Szkicu](Sketch/pl.md).

-    **Wskazówka 2.**Zadbaj o to, aby model gwintu był krótki, posiadał małą liczbę obrotów. Długie gwinty mają tendencję do generowania nieudanych operacji logicznych. Rozważ możliwość układanie długich gwintów z krótkich elementów za pomocą funkcji **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft: OrthoArray](Draft_OrthoArray.md)**, w przypadku gdy długi gwint okaże się problematyczny.

-    **Wskazówka 3.**W przypadku wizualizacji 3D i drukowania 3D może być w porządku pozostawienie cylindra i gwintu niezwiązanego, to znaczy z przecięciami między dwoma bryłami. Zmniejszenie ilości operacji logicznych skutkuje mniejszym zużyciem pamięci i mniejszymi plikami wynikowymi.

### Zalety i wady 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Koncepcja budowy modelu łatwa do zrozumienia.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Bardzo naturalny sposób definiowania profilu gwintu.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Brak problemów z zazębieniem się powstałego obiektu, w odróżnieniu od metody 4.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Z powodu zawodności samoczynnie przecinających się kształtów wyciągnięć, prawie niemożliwe jest wygenerowanie gwintu bez szczelin, to znaczy bez powierzchni płaskich na wewnętrznej powierzchni gwintu.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Operacje logiczne są wymagane do uzyskania pojedynczej zwartej bryły. Obliczenia operacji logicznych zajmują stosunkowo dużo czasu i często kończą się niepowodzeniem.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Gwinty o dużej liczbie zwojów są problematyczne.

## Metoda 5. Wyciągnięcie profilu poziomego 

### Informacje ogólne 

Koncepcja polega na wyciągnięciu poziomego przekroju gwintu wzdłuż spirali. Głównym problemem jest tutaj ustalenie, jakiego profilu użyć, aby uzyskać określony gwint.

<img alt="" src=images/thread-by-horz-profile.png  style="width:600px;">

Jeśli użyjemy okręgu jako profilu poziomego, profil gwintu będzie sinusoidalny (środek okręgu musi być umieszczony poza punktem początku, przesunięcie to określa głębokość gwintu).

Aby otrzymać standardowy profil zęba piły, para lustrzanych odbić spirali łukowych musi zostać połączona w jedną ścieżką. W rezultacie tej operacji otrzymamy kształt serca, który staje się ledwie odróżnialny od okręgu, w przypadku gdy głębokość gwintu jest niewielka w zestawieniu z jego średnicą (to dlatego taki \"gruby\" gwint pokazano na powyższym rysunku).

### Generowanie kształtu 

Nie jest łatwo określić, jak przygotować profil poziomy, aby uzyskać określony kształt pionowy. W sytuacjach nieskomplikowanych, dotyczących kształtu trójkątnego lub trapezowego, profil może być wykonany ręcznie. Alternatywnie można go skonstruować, tworząc krótki gwint metodą 3 i pobierając jego kawałek poprzez wykonanie funkcji [common](Part_Common/pl.md) pomiędzy płaszczyzną poziomą a gwintem.

#### Kształt dla gwintu trójkątnego 

1.  stwórz spiralę łukową (archimedian) w płaszczyźnie XY,
    1.  ustaw liczbę zwojów na 0.5,
    2.  wartość promienia zdefiniuje wewnętrzny promień gwintu *(promień zewnętrzny będzie powiększony o głębokość nacięcia)*,
    3.  oraz wysokość, by podwoić głębokość nacięcia gwintu.
2.  [Część: Mirror](Part_Mirror/pl.md) spirala na przeciw płaszczyzny XY.
3.  [Część: Suma](Part_Fuse/pl.md) spirala i jej odbicie lustrzane w celu uzyskania zamkniętego odcinka w kształcie serca.

#### Kształt dla dowolnego przekroju 

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">

1.  Stwórz pionowy zarys cięcia; upewnij się, że wysokość szkicu odpowiada skokowi potrzebnego gwintu,
2.  Stwórz spiralę 1 o wysokości równej skokowi gwintu, oraz o promieniu spirali równym 0,42 średnicy nominalnej gwintu,
3.  Wyciągnij profil cięcia wzdłuż spirali 1; zaznacz opcje {{CheckBox|TRUE|Utwórz bryłę}} i {{CheckBox|TRUE|wektor Freneta}},
4.  Wykreśl okrąg o wymiarze promienia równym wymiarowi nominalnego promienia gwintu w płaszczyźnie XY,
5.  Przekształć okrąg w płaszczyznę. Można to zrobić funkcją **[<img src=images/Part_Builder.svg style="width:16px"> [Part: Konstruktor kształtów Builder](Part_Builder/pl.md)** lub **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Draft: Upgrade](Draft_Upgrade.md)**, następnie ustaw wartość **MakeFace** na `True`.
6.  Wytnij ścianę przy pomocy profilu wyciągnięcia.
7.  Wykonaj kopię opcją **[<img src=images/Draft_Clone.svg style="width:16px"> [Draft: Klon](Draft_Clone.md)** z wyciętego kawałka.
8.  Użyj funkcji **[<img src=images/Draft_Downgrade.svg style="width:16px"> [Draft: Downgrade](Draft_Downgrade/pl.md)** na klonie, by otrzymać linię łamaną. Utworzy ona poziomy profil potrzebny do tej metody.
9.  Wykonaj spiralę o wymiarze promienia równym wymiarowi nominalnemu promienia gwintu i skoku gwintu, oraz potrzebnej wysokości gwintu.
10. Wyciągnij odcinek wzdłuż spirali; zaznacz opcje {{CheckBox|TRUE|Utwórz bryłę}} i {{CheckBox|TRUE|wektor Freneta}},
11. To wszystko.

Przewodnik krok po kroku od [forum, post Ulrich1a](http://forum.freecadweb.org/viewtopic.php?f=3&t=6506#p52558) *(Tworzenie gwintu: Nieoczekiwane wyniki)*, nieznacznie zmodyfikowane.

Drogę postępowania zaprezentował Gaurav Prabhudesai w przygotowanym przez siebie [filmie instruktażowym](http://www.youtube.com/watch?v=fxKxSOGbDYs) (\"FreeCAD: Jak tworzyć gwinty\").

### Zalety i wady 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> gotowy do użycia kształt bryły z gwintem na rdzeniu jest tworzony bezpośrednio przez wyciągnięcie.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> wymagana jest mniejsza liczba operacji logicznych lub nawet ich brak, więc prędkość generowania jest bardzo wysoka w porównaniu z metodą 3.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> końce gwintów są ładnie przycięte natychmiastowo.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> długie gwinty nie stanowią problemu, chyba że konieczne jest przeprowadzenie operacji logicznych. W przeciwnym razie nie będzie ona dużo lepsza niż Metoda 3.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> gwinty bez przerwy nie stanowią problemu.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> zdefiniowanie kształtu gwintu jest skomplikowane.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Użycie standardowej siatki z tak stworzonym gwintem generuje brzydkie oczka, co może prowadzić do problemów. Inne siatki są lepsze, na przykład Mefisto wydaje się dawać najlepsze rezultaty.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> duża ilość pamięci według [Techniki modelowania gwintu](http://forum.freecadweb.org/viewtopic.php?f=3&t=12593&start=10#p101197).

## Metoda 5. Wyciąganie pomiędzy wytłaczanymi ścianami ślimakowymi 

### Informacje ogólne 

Spiralne wypusty będą wyciskać współosiowe powierzchnie, które mogą być poddane wyciąganiu, podczas gdy spirala parametryczna FreeCAD nie będzie miała takiej możliwości. Do zdefiniowania gwintu potrzebne są dwa spiralne wypusty (helical splines). Te dwa wypusty mogą być skalowane z biblioteki, a następnie odpowiednio rozmieszczone i wytłoczone, w celu uzyskania właściwego kształtu bryły.

Parametryczne spirale FreeCAD tak naprawdę nie są spiralne, ale spiralne b-splines nie są trudne do rozmieszczenia. Jedną z dostępnych metod jest układanie dwunastokątów o promieniu 5 mm w odstępach Z 1/12 mm (0.08333 mm) i ścieżkami Spline od wierzchołka do wierzchołka w porządku rosnącym i obrotowym, oraz aby rozważyć zrobienie tego raz, z powiedzmy, 10 obrotami, tak aby Spline mógł być ponownie użyty jako plik biblioteczny do importu i ponownego użycia. Dla ułatwienia skalowania wygodnie jest używać średnicy 10 mm i rastra 1 mm. Jeśli robisz to ręcznie, narysowanie Dwire, a następnie przekształcenie go w b-spline jest łatwiejsze niż narysowanie Spline. Odcinki Dwire nie mają obliczonej krzywizny podczas rysowania, więc podążają za kursorem i zatrzaskują się bardziej posłusznie.

Po przeskalowaniu Spline do odpowiedniej wielkości i umieszczeniu ich w taki sposób, że wyciągnięcie będzie miało odpowiedni kąt zawarty pomiędzy boczkami gwintu, są one wytłaczane wzdłuż ich osi, długość skoku jest odpowiednia dla Spline wewnętrznego, skok zewnętrzny/8.

<img alt="" src=images/splineextrudeloft.png  style="width:912px;">

ISO i inne gwinty zostały uelastycznione, czyli płaskie, wewnętrzne i zewnętrzne krawędzie, zamiast ostrrych, co odpowiada użytkownikom FreeCAD w tej metodzie, ponieważ możemy wyciągnąć do spiralnej powierzchni czołowej przy nominalnym rozmiarze połączenia, podczas gdy powierzchnia wewnętrzna nie może być wyciągnięta do zewnętrznej krawędzi Spline, ponieważ powierzchnia czołowa jest profilem zamkniętym, Spline jest otwarty.

![761PX](images/Threadform.PNG )

Ta metoda produkuje wysoce stabilne bryły, które prawidłowo działają z funkcjami logicznymi. Chociaż nie wytwarza ona \"parametrycznych\" gwintów śrubowych w standardowych rozmiarach w sensie prostego dostępu do kształtu poprzez rozmiar łącznika, jest to łatwy sposób na stworzenie wiarygodnej biblioteki do ponownego użycia. Modele o specjalnych kształtach, takich jak ACME czy śruby z serii Archimedian, są również nieskomplikowane do modelowania jako rozwiązania jednorazowe.   {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Thread for Screw Tutorial/pl
