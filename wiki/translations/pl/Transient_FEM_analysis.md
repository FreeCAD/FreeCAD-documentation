---
 TutorialInfo:l
   Topic:  Przejściowa analiza MES
   Level:  
   Time: 
   Author: 
   FCVersion: 
   Files: 
---

# Transient FEM analysis/pl

 }





## Kontekst



## Tworzenie modelu 

1.  Zaczynając od pustego projektu FreeCAD, budujemy naszą listwę bimetaliczną w środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md)
2.  Narysuj <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Sześcian](Part_Box/pl.md) i zmień jego nazwę na `aluminium`.
3.  Nadaj temu elementowi wymiary 100 x 10 x 2 mm *(długość x szerokość x wysokość)*.
4.  Utwórz drugą bryłę [sześcianu](Part_Box/pl.md) **stal** o takich samych wymiarach
5.  Przesuń tę część o 2 mm wzdłuż osi Z *(za pomocą **Edycja ... → Umiejscowienie → Pozycja → Z**)*.
6.  Zaznacz obie bryły *(używając klawisza **Shift** + kliknięcie myszą)* i utwórz z nich obiekt funkcją <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragmentacja](Part_BooleanFragments/pl.md).
7.  Zmień nazwę obiektu Boolean Fragments na `listwa bimetaliczna`.
8.  W [Edytorze właściwości](Property_editor/pl.md) zmieniamy tryb z **Standard** na **CompSolid**. *(Powinno też zadziałać użycie polecenia [Utwórz kształt złożony](Part_Compound/pl.md) zamiast <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragmentacji funkcją logiczną](Part_BooleanFragments/pl.md), jednak w przypadku bardziej złożonych przecinających się kształtów mogą wystąpić problemy z późniejszą analizą MES. Lepiej więc przyzwyczaić się do używania w pierwszej kolejności Fragmentacji funkcją logiczną)*. Wynik powinien wyglądać następująco:

<img alt="" src=images/Transient_FEM_Bimetal_(1).JPG  style="width:700px;">



## Przygotowanie i uruchomienie analizy MES 



### Przydzielanie materiałów 

W środowisku pracy MES tworzymy nową analizę <img alt="" src=images/FEM_Analysis.svg  style="width:20px;"> i dodajemy do niej nowy materiał <img alt="" src=images/FEM_MaterialSolid.svg  style="width:20px;">. W następnym oknie zadania wybieramy jeden z predefiniowanych stopów aluminium. W sekcji \"Wybór odniesienia dla geometrii\" przypisujemy materiał do niższej części naszego modelu, ustawiając tryb wyboru na *Bryła*. W środowisku pracy MES tworzymy nową analizę <img alt="" src=images/FEM_Analysis.svg  style="width:20px;"> i dodajemy do niej nowy materiał <img alt="" src=images/FEM_MaterialSolid.svg  style="width:20px;">. W następnym oknie zadania wybieramy jeden z predefiniowanych stopów aluminium. W sekcji \"Wybór odniesienia dla geometrii\" przypisujemy materiał do niższej części naszego modelu, ustawiając tryb wyboru na *Bryła*, klikając **Dodaj** i wybierając powierzchnię lub krawędź dolnego paska. W widoku listy powinna pojawić się pozycja \"BooleanFragments:Solid1\".

<img alt="" src=images/Transient_FEM_Bimetal_(2).JPG  style="width:700px;">

Zamykamy okno zadań i powtarzamy kroki, aby utworzyć drugi materiał \"Stal\" *(karta materiału \"CalculiX-Steel\")* i przypisać go do górnego paska *(\"BooleanFragments:Solid2\")*.



### Tworzenie siatki 

Ponieważ analiza elementów skończonych wymaga oczywiście elementów do pracy, musimy podzielić nasz model na tak zwaną siatkę. Środowisko pracy MES oferuje dwa narzędzia do tworzenia siatek: Netgen i GMSH. W tym przypadku wybierzemy Netgen: Po wybraniu obiektów Boolean Fragments \"listwa bimetaliczna\", klikamy na ikonę <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:20px;">. Netgen w oknie roboczym MES. W następnym oknie zadań musimy dokonać różnych wyborów, zaczynając od góry:

-   Maksymalny rozmiar to maksymalny rozmiar *(w milimetrach)* elementu. Im mniejszy maksymalny rozmiar elementu, tym więcej elementów otrzymamy - zwykle wynik będzie bardziej precyzyjny, ale z dramatycznym wzrostem czasu obliczeń. Ustawiliśmy go na {{Value|10}}.
-   Drugi rząd oznacza, że w każdym elemencie zostaną utworzone dodatkowe węzły. Zwiększa to czas obliczeń, ale zwykle jest dobrym wyborem, jeśli chodzi o zginanie, jak w naszej analizie. Pozostawiamy to pole zaznaczone.
-   Stopień rozdrobnienia: Wybierz, jak drobno model powinien zostać pocięty na elementy. W przypadku bardziej złożonych modeli z krzywiznami i przecięciami możemy zwiększyć liczbę elementów w tych regionach, aby uzyskać lepsze wyniki *(oczywiście kosztem dłuższego czasu obliczeń)*. Eksperci mogą również ustawić opcję Zdefiniowane przez użytkownika i ustawić następujące parametry. W przypadku naszego prostego modelu prostokątnego wybór stopnia rozdrobnienia nie ma większego wpływu, dlatego utrzymujemy go na **umiarkowanym** poziomie.
-   Optymalizuj: Jakiś rodzaj przetwarzania końcowego po generowaniu siatki. Pozostawiamy to pole zaznaczone.

Kliknięcie **Zastosuj** uruchamia generator siatki i - w czasie zależnym od komputera - na naszym modelu pojawia się szkielet siatki. Siatka powinna utworzyć około 4000 węzłów.

<img alt="" src=images/Transient_FEM_Bimetal_(3).JPG  style="width:700px;">



### Przypisywanie warunków brzegowych 

Analiza MES nic by teraz nie dała, ponieważ w naszym modelu nic się jeszcze nie dzieje. Dodajmy więc trochę temperatury: Użyj <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:20px;"> temperatury początkowej ze środowiska pracy MES i ustaw temperaturę na 300 K. Tutaj nie można wybrać żadnych części modelu, ponieważ ta nastawa dotyczy całego modelu.

Następnie używamy <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:20px;"> temperatury działającej na powierzchnię. Zaznaczamy dwie powierzchnie na jednym końcu paska *(Ctrl + lewy klawisz myszy)* i klikamy **Dodaj** w oknie zadań. Dwie powierzchnie obiektu Fragmentacji funkcją logiczną, powinny pojawić się na liście, a na modelu powinny pojawić się małe ikony temperatury. Ustawiamy temperaturę na 400 K i zamykamy okno zadań. Na początku analizy wybrane powierzchnie otrzymają natychmiastowy wzrost temperatury z 300 do 400 K. Ciepło będzie przewodzone wzdłuż metalowych pasków i spowoduje ich odgięcie.

<img alt="" src=images/Transient_FEM_Bimetal_(4).JPG  style="width:700px;">

Przed uruchomieniem analizy należy ustawić dodatkowy warunek brzegowy: Analiza może zostać uruchomiona tylko wtedy, gdy nasz model jest zamocowany gdzieś w przestrzeni. Za pomocą <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:20px;"> wybieramy te same dwie ściany, co dla 400 K powyżej i dodajemy je do listy. Na modelu pojawią się czerwone paski, wizualizujące, że te powierzchnie są zamocowane w przestrzeni i nie mogą się poruszać podczas analizy.

<img alt="" src=images/Transient_FEM_Bimetal_(5).JPG  style="width:700px;">



### Uruchomienie analizy 

Analiza powinna już zawierać obiekt solwera **[CalculiXccx](FEM_SolverCalculixCxxtools/pl.md)**. Jeśli nie, dodajemy go za pomocą ikony solvera <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:20px;"> z paska narzędzi. *(Istnieją dwie identyczne ikony, solwer eksperymentalny powinien również działać)*. Obiekt solwera ma listę właściwości poniżej w lewej części okna. Tutaj wybieramy następujące opcje *(te niewymienione pozostawiamy bez zmian)*:

-   Typ analizy: Chcemy przeprowadzić analizę termomechaniczną. Inne opcje to tylko statyczna *(bez wpływu temperatury)*, częstotliwościowa *(oscylacje)* lub tylko w celu sprawdzenia poprawności modelu.
-   Termomechaniczny stan ustalony: Stan ustalony oznacza, że solwer zwróci jeden wynik, w którym fizyka osiągnie równowagę. NIE chcemy tego robić, chcemy uzyskać wiele wyników w czasie *(analiza przejściowa)*. Należy więc ustawić wartość {{false/pl}}.
-   Czas zakończenia: Chcemy, aby nasza analiza zatrzymała się po 60 sekundach *(tj. w czasie symulacji, a nie w czasie rzeczywistym)*.

<img alt="" src=images/Transient_FEM_Bimetal_(6).JPG  style="width:700px;">

Po dwukrotnym kliknięciu obiektu solwera sprawdzamy, czy wybrana jest opcja \"termomechaniczna\" i uruchamiamy **Zapisz plik .inp**. Zwykle zajmuje to kilka sekund *(lub znacznie więcej w przypadku większych modeli)* i zwraca komunikat \"zapis zakończony\" w polu poniżej. Teraz rozpoczynamy obliczenia za pomocą **Uruchom CalculiX**. Po pewnym czasie powinny pojawić się ostatnie komunikaty \"Bezbłędnie wykonane obliczenia CalculiX!\" i \"Ładowanie zestawów wyników\...\". Gdy licznik czasu na dole zatrzyma się, zamykamy okno zadań. *(Przy większych modelach i / lub wolniejszych komputerach FreeCAD może się zawiesić i nie zobaczymy działającego timera. Ale bądź cierpliwy, w większości przypadków CalculiX nadal działa w tle i ostatecznie wygeneruje wyniki)*.

Powinniśmy teraz mieć wiele <img alt="" src=images/FEM_ResultShow.svg  style="width:20px;"> obiektów wynikowych MES na liście. Klikając dwukrotnie, możemy otworzyć każdy z nich i zwizualizować obliczone temperatury, przemieszczenia i naprężenia. Możemy wizualizować zginanie, wybierając opcję \"Pokaż\" w sekcji \"Przemieszczenie\". Ponieważ bezwzględne przemieszczenia są małe, używamy \"Współczynnika\", aby wyolbrzymić wartości.

<img alt="" src=images/Transient_FEM_Bimetal_(7).JPG  style="width:700px;">

W programie FreeCAD możemy użyć <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:20px;"> [Prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md), aby wykonać post-processing wyników. Alternatywnie, możemy wyeksportować wyniki w formacie VTK i zaimportować je do dedykowanych postprocesorów, takich jak ParaView. Do eksportu wielu wyników *(jak w przypadku tej analizy)* dostępna jest [makrodefinicja](Macro_export_transient_FEM_results/pl.md).



### Pobieranie

-   [Przykładowy plik bez wyników *(200 kB)*](https://drive.google.com/file/d/1m3RiJ-JM7QSJ6YDhZnafHIbyL92V6sYU/view?usp=sharing).

-   [Przykładowy plik z wynikami *(10 MB)*](https://drive.google.com/file/d/157aIdVpIyfpVW9WxL-ReGz0FIsQebH_q/view?usp=sharing).



## Inny przykład 

-   [Analityczny przykład bimetalu](https://forum.freecadweb.org/viewtopic.php?f=18&t=43040&start=10#p366664). Przykład analityczny przedstawiony na forum jest zawarty w przykładach FreeCAD FEM. Można go uruchomić w Pythonie za pomocą:

from femexamples.thermomech_bimetall import setup
setup()


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Transient FEM analysis/pl
