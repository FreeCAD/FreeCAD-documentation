---
- TutorialInfo:/pl
   Topic: Szkicownik
   Level: początkujący
   Time: 60 minut
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei] oraz vocx
   FCVersion:0.19 lub nowszy
   Files:[https://forum.freecadweb.org/viewtopic.php?f=36&t=43594 Basic Sketcher tutorial updated]
---

# Basic Sketcher Tutorial/pl







### Wprowadzenie

Ten poradnik ma na celu zapoznanie czytelnika z podstawowym przepływem pracy środowiska <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md).

Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) funkcjonuje jako samodzielny moduł, dzięki czemu może być używany do rysowania podstawowych obiektów 2D *(płaskich)*. Jest on jednak najczęściej używany w połączeniu ze środowiskiem pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md). Zamknięty szkic jest zwykle używany do utworzenia powierzchni lub profilu, który ma zostać wyciągnięty do bryły [Zawartość](PartDesign_Body/pl.md) przy użyciu operacji takiej jak **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnij wybrany szkic](PartDesign_Pad/pl.md)**.

Przećwiczymy:

-   Tworzenie geometrii konstrukcyjnej.
-   Tworzenie geometrii.
-   Stosowanie wiązań geometrycznych.
-   Stosowanie wiązań wymiarów.
-   Uzyskanie profilu zamkniętego.

Aby uzyskać bardziej szczegółowy opis szkicownika, przeczytaj stronę [Szkicownik: odniesienie](Sketcher_reference/pl.md).

![](images/00_Sk01_Sketcher_fully_constrained_final.png ) 
*Wynik końcowy szkicu, z geometrią w pełni ograniczoną w całości, łącznie z geometrią konstrukcji pomocniczej.*



## Sposób postępowania 

1\. Uruchom program FreeCAD, utwórz nowy pusty dokument przez menu **Plik → [<img src=images/Std_New.svg style="width:16px"> [Nowy](Std_New/pl.md)**.

:   1.1. Przełacz interfejs na środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) z [paska narzędzi Środowisko](Std_Workbench/pl.md), lub menu **[Widok](Std_View_Menu/pl.md) → Środowisko → Szkicownik**.

Kilka działań do zapamiętania:

-   Naciśnij prawy przycisk myszy, lub naciśnij jeden raz klawisz **Esc** na klawiaturze, aby wyłączyć aktywne narzędzie w trybie edycji.
-   Aby wyjść z trybu edycji szkicu, naciśnij przycisk **Zamknij** w [panelu zadań](task_panel.md), lub naciśnij dwukrotnie klawisz **Esc** na klawiaturze.
-   Aby ponownie wejść w tryb edycji, kliknij dwukrotnie na obiekt szkicu w [widoku drzewa](Tree_view/pl.md), lub wybierz go, a następnie kliknij na przycisk **[<img src=images/Sketcher_EditSketch.svg style="width:16px">. [Edycja szkicu](Sketcher_EditSketch/pl.md)**.



## Utwórz szkic 

2\. Kliknij w przycisk **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [Utwórz nowy szkic](Sketcher_NewSketch/pl.md)**.

:   2.1. Wybierz orientację szkicu, czyli jedną z płaszczyzn bazowych XY, XZ lub YZ. Wybierz również, czy chcesz mieć odwróconą orientację i przesunięcie od płaszczyzny bazowej.
:   2.2. Będziemy korzystać z domyślnej płaszczyzny i opcji.
:   2.3. Kliknij **OK**, aby rozpocząć konstruowanie szkicu.

Jesteśmy obecnie w trybie edycji szkicu, w którym możemy korzystać z większości narzędzi tego warsztatu.


**Uwaga:**

w [panelu zadań](Task_panel/pl.md) widoku połączonego należy rozwinąć sekcję **Edycja kontrolek** i upewnić się, że opcja **Automatyczne wiązania** jest włączona. Tutaj mogą zostać zmienione również inne opcje, w tym gęstość widocznej siatki, oraz to czy chcemy aktywować przyciąganie do siatki. W tym poradniku nie będziemy aktywować przyciągania do siatki i ukryjemy ją. W innych sekcjach [panelu zadań](Task_panel/pl.md) możesz również zobaczyć, które elementy geometryczne i wiązania zostały zdefiniowane.

<img alt="" src=images/01_Sk01_Sketcher_Task_panel.png  style="width:" height="400px;">



*Górna część [panelu zadań](Task_panel/pl.md) szkicownika.*



## Geometrie konstrukcyjne 

3\. Geometria konstrukcyjna służy do wspomagania tworzenia właściwej geometrii. Rzeczywista geometria będzie wyświetlana poza trybem edycji szkicu, podczas gdy geometria konstrukcyjna będzie wyświetlana tylko i wyłącznie w trybie edycji. Dlatego też, możesz użyć tyle geometrii konstrukcji ile potrzebujesz by zbudować konkretne kształty.

:   3.1. Kliknij na przycisk **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)**. Teraz elementy geometryczne zostaną narysowane w **trybie konstrukcyjnym**.
:   3.2. Kliknij na przycisk **<img src="images/Sketcher_Line.svg" width=16px> [Utwórz linię](Sketcher_CreateLine/pl.md)**.
:   3.3. Zbliż kursor do punktu początku szkicu, powinien zostać podświetlony, a przy kursorze <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> pojawi się ikona [wiązania żbieżności](Sketcher_ConstrainCoincident.md).
:   3.4. Kliknij na punkt, a następnie przesuń kursor, aby rozpocząć rysowanie od niego nowej linii. Przesuń wskaźnik tak, aby linia miała długość około {{Value|30mm}}. Nie musisz być bardzo precyzyjny w tym kroku, po zakończeniu ustawimy odpowiedni wymiar.
:   3.5. Powtórz tę procedurę jeszcze cztery razy, aby umieścić linie konstrukcji na wzór gwiazdy. Nie martw się zbytnio o ich rozmiar lub położenie, po prostu przedłuż je w czterech strefach.
:   3.6. Aby wyjść z trybu konstrukcyjnego, po prostu kliknij ponownie na przycisk **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)**.


**Uwaga:**

do tej pory narzędzie [Utwórz linię](Sketcher_CreateLine/pl.md) jest nadal aktywne. Oznacza to, że możemy nadal klikać na [widok 3D](3D_view/pl.md), aby narysować tyle linii ile chcemy. Jeśli chcemy zakończyć pracę z tym narzędziem, możemy nacisnąć prawy przycisk myszy, lub nacisnąć raz klawisz **Esc** na klawiaturze. W ten sposób kursor nie będzie już tworzył linii, będzie to po prostu kursor pozwalający nam na zaznaczenie obiektów, które właśnie stworzyliśmy. W tym trybie możemy wybrać i przeciągnąć punkty końcowe każdej z linii, aby dostosować ich położenie.


**Uwaga 2:**

nie naciskaj klawisza **Esc** drugi raz, ponieważ spowoduje to zamknięcie trybu edycji szkicu. Jeśli to zrobisz, wejdź ponownie w tryb edycji, klikając dwukrotnie na szkic w [widoku drzewa](Tree_view/pl.md).

Spójrz jeszcze raz na [panel zadań](Task_panel/pl.md). Sekcja **Komunikaty solwera** wskazuje, że szkic jest niedostatecznie związany, i podaje liczbę **stopni swobody**.

Spójrz na sekcje **Wiązania** i **Elementy**, aby zobaczyć nowo utworzone wiązania i linie. Gdy twoje szkice mają wiele elementów, może być trudno je wybrać w oknie [widoku 3D](3D_view/pl.md), więc możesz użyć tych list, aby wybrać dokładnie ten obiekt który chcesz.

<img alt="" src=images/02_Sk01_Sketcher_construction.png  style="width:" height="400px;">



*Linie konstrukcyjne tworzące kształt gwiazdy ze środkiem w miejscu początku układu współrzędnych.*



## Geometria detalu 

Geometria właściwa musi mieć kształt zamknięty, jeśli ma być użyta jako profil, który może być wytłaczany za pomocą takich narzędzi jak **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Projekt Części: Wyciągnij wybrany szkic](PartDesign_Pad/pl.md)**.

Jeśli wcześniej nie opuściłeś tego trybu, upewnij się, że nie jesteś w trybie konstrukcji, klikając na przycisk **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)**.



### Łuki zewnętrzne 

4\. Rysujemy okrąg.

:   4.1. Kliknij w przycisk **[<img src=images/Sketcher_Circle.svg style="width:16px"> [Utwórz okrąg w szkicowniku](Sketcher_CreateCircle/pl.md)**.
:   4.2. Kliknij na **początek** szkicu, aby ustawić punkt środka okręgu.
:   4.3. Kliknij w dowolnym miejscu w oknie [widoku 3D](3D_view/pl.md), aby ustawić promień obwodu jako odległość od punku początku. Zrób to w przybliżeniu - około {{Value|8mm}}. Wymiar ustawimy ponownie później.

5\. Utwórz kilka łuków.

:   5.1. Kliknij na przycisk **[<img src=images/Sketcher_Arc.svg style="width:16px"> [Utwórz łuk w szkicowniku](Sketcher_CreateArc/pl.md)**.
:   5.2. Przesuń kursor do punktu końcowego jednej z linii konstrukcyjnych i kliknij na nią. Spowoduje to ustawienie środkowego punktu łuku w pozycji <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [zbierznej](Sketcher_ConstrainCoincident/pl.md) z punktem końcowym tej linii.
:   5.3. Kliknij raz w oknie [widoku 3D](3D_view/pl.md) w dowolnym miejscu, aby jednocześnie ustalić promień łuku i pierwszy z jego punktów końcowych. Wyznacz promień w przybliżeniu na wartość {{Value|8mm}}.
:   5.4. Przesuń kursor w kierunku przeciwnym do ruchu wskazówek zegara, aby wyznaczyć łuk, który ma swoją wklęsłość skierowaną ku początkowi szkicu. Kliknij, aby ustawić ostateczny punkt końcowy łuku, definiując łuk, który w przybliżeniu rozciąga się na {{Value|180°}} lub połowę okręgu.
:   5.5. Powtórz te kroki dla każdej linii konstrukcyjnej, tak aby każda z nich posiadała okrągły łuk na swoim końcu. Nazwiemy te łuki łukami zewnętrznymi.

<img alt="" src=images/03_Sk01_Sketcher_outer_arcs.png  style="width:" height="400px;">



*Łuki dodane w punktach końcowych linii konstrukcyjnych. Dodatkowo okrąg centralny.*



### Łuki wewnętrzne 

6\. Rysujemy łuk pomiędzy każdą parą łuków zewnętrznych.

:   6.1. Nadal przy aktywnym narzędziu **[<img src=images/_Sketcher_Arc.svg style="width:16px"> [Utwórz łuk](Sketcher_CreateArc.md)** kliknij gdzieś pomiędzy dwoma łukami zewnętrznymi, ale w odstępie od początku szkicu, aby ustawić środek nowego łuku.
:   6.2. Kliknij w pobliżu punktu końcowego pierwszego z łuków zewnętrznych. Następnie przesuń kursor, aby przeciągnąć zakończenie tworzonego łuku w pobliże kolejnego punktu końca, sąsiedniego łuku zewnętrznego, tak jakbyś próbował połączyć punkty końcowe łuków zewnętrznych. Tym razem wklęsłość musi być tworzona w kierunku od punktu początku szkicu.
:   6.3. Powtórz te kroki, tak aby każda para łuków zewnętrznych miała nowy łuk pomiędzy nimi. Nazwiemy nowo utworzone łuki, łukami wewnętrznymi.

**Podsumowując**, łuki zewnętrzne powinny mieć krzywiznę skierowaną na zewnątrz, a wklęsłość skierowaną w stronę początku szkicu;
łuki wewnętrzne powinny mieć krzywiznę skierowaną do wewnątrz, a ich wklęsłość powinna być skierowana od tego samego punktu początku szkicu.

<img alt="" src=images/04_Sk01_Sketcher_inner_arcs.png  style="width:" height="400px;">



*Łuki dodawane pomiędzy pierwszym zestawem umieszczonych łuków zewnętrznych.*



## Wiązania

Spójrz raz jeszcze na [panel zadań](Task_panel/pl.md). Ze względu na nowe elementy geometryczne, które narysowaliśmy, sekcja **Komunikaty solwera** wskazuje jeszcze więcej **stopni swobody**. **Stopień swobody** *(DOF)* wskazuje na możliwy ewentualny ruch jednego elementu. Na przykład, punkt może być przesuwany zarówno w kierunku poziomym jak i pionowym, a więc ma dwa stopnie swobody. Linia jest zdefiniowana przez dwa punkty, a więc w sumie posiada cztery stopnie swobody. Jeżeli zwiążemy jeden z tych punktów, to cały system ma tylko dwa stopnie swobody. Jeżeli dodatkowo zwiążemy ruch poziomy pozostałego punktu, to mamy tylko jeden stopień swobody. Jeżeli natomiast zwiążemy również ruch pionowy tego punktu, to ostatni stopień swobody zniknie, a linia nie będzie mogła być już przemieszczana.

Do tej pory, kiedy rysowaliśmy linie i łuki, szkicownik dodawał dla nas automatyczne wiązania, te, które utrzymują linie powiązane z początkiem, a łuki zewnętrzne powiązane z liniami konstrukcyjnymi. Nie dodaliśmy jednak innych wyraźnych wiązań, dzięki czemu kształty geometryczne mogą być nadal przesuwane w wielu kierunkach. **Wiązania to *zasady*, które mówią nam, w jakich warunkach obiekt geometryczny może się poruszać i na ile jest to możliwe.** Służą one do eliminacji stopni swobody, dzięki czemu szkic jest stabilny. Jeśli wyeliminujemy wszystkie stopnie swobody, wówczas szkic jest **całkowicie związany** i posiada sztywny kształt, to znaczy, że jego punkty nie mogą być przemieszczane. Ogólnie rzecz biorąc, dobrym pomysłem jest całkowite związanie szkiców, ponieważ spowoduje to powstanie stabilnych modeli.

Istnieją dwa główne rodzaje wiązań:

-    **Wiązania geometrii**definiują właściwości kształtów bez określania dokładnych wymiarów, np. poziomu, pionu, równoległości, prostopadłości i zbieżności.

-    **Wiązania danych**definiują charakterystykę kształtów poprzez określenie wymiarów, na przykład wymiar długości lub kąta.



## Wiązania geometrii 



### Jednakowa długość i promień 

7\. Wiązania geometrii linii i łuków.

:   7.1 Zaznacz wszystkie pięć linii konstrukcyjnych. Wystarczy kliknąć tylko raz, by wybrać element.
:   7.2. Naciśnij przycisk **[<img src=images/Constraint_EqualLength.svg style="width:16px"> [Utwórz wiązanie równości](Sketcher_ConstrainEqual/pl.md)**.
:   
    **Uwaga:**utworzone zostaną cztery wiązania. Są one tworzone łańcuchowo, pierwsza linia ma taką samą długość jak druga, która ma taką samą długość jak trzecia, która ponownie ma taką samą długość jak czwarta, która z kolei ma taką samą długość jak piąta. Tak więc w tym przypadku, pierwsza i piąta mają tę samą długość.





:   7.3. Wybierz wszystkie pięć łuków zewnętrznych, te, które są umieszczone na końcu linii konstrukcyjnej.
:   7.4. Naciśnij przycisk **[<img src=images/Constraint_EqualLength.svg style="width:16px"> [Utwórz wiązanie równości](Sketcher_ConstrainEqual/pl.md)**.
:   7.5. Powtórz to ze wszystkimi łukami wewnętrznymi, tymi między łukami zewnętrznymi.
:   
    **Uwaga:**ponowne wiązania mają charakter łańcuchowy. Dlatego wszystkie łuki zewnętrzne będą miały ten sam promień, a wszystkie łuki wewnętrzne będą miały ten sam promień. W tym momencie, konkretna wartość tych długości nie jest zdefiniowana. Możesz użyć kursora myszki do przeciągnięcia punktu i zobaczyć, jak szkic jest aktualizowany z uwzględnieniem istniejących wiązań.





:   7.6. Zaznacz linię konstrukcyjną, której pozycja jest najbliższa osi pionowej.
:   7.7. Wybierz narzędzie **[<img src=images/Constraint_Vertical.svg style="width:16px"> [Utwórz wiązanie pionowe](‎Sketcher_ConstrainVertical/pl.md)** *(opcjonalnie)*. Jeśli narysujesz linię konstrukcyjną w dół nad osią Y, automatycznie <img alt="" src=images/_Constraint_PointOnObject.svg  style="width:32px;"> [Punkt dotyczący wiązania z obiektem](Sketcher_ConstrainPointOnObject/pl.md) zostanie już umieszczony, utrzymując linię konstrukcyjną w pionie. W takim przypadku nie jest wymagane tworzenie dodatkowego <img alt="" src=images/_Constraint_Vertical.svg  style="width:32px;"> [wiązania pionowego](Sketcher_ConstrainVertical/pl.md).


**Uwaga:**

w trakcie dodawania wiązań, w obszarze okna [widoku 3D](3D_view/pl.md), nad rysunkiem geometrii pojawiają się symbole graficzne wskazujące typ zastosowanego wiązania. Jeśli te symbole przysłaniają ci widok, możesz je ukryć, usuwając zaznaczenie wiązań w polu [panelu zadań](Task_panel/pl.md). Należy również zauważyć, że liczba stopni swobody maleje po dodaniu każdego z wiązań.


**Uwaga 2:**

jeśli chcesz tymczasowo wyłączyć wiązanie, możesz zaznaczyć je i nacisnąć przycisk **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Przełącz aktywność wiązania](Sketcher_ToggleActiveConstraint/pl.md)**. Gdy zechcesz zastosować je ponownie, wciśnij powtórnie ten sam przycisk.

<img alt="" src=images/05a_Sk01_Sketcher_equality_constraints_lines.png  style="width:" height="400px;"> <img alt="" src=images/05b_Sk01_Sketcher_equality_constraints_O-arcs.png  style="width:" height="400px;">

<img alt="" src=images/05c_Sk01_Sketcher_equality_constraints_I-arcs.png  style="width:" height="400px;">



*Szkic z wiązaniami równości stosowanymi do linii konstrukcyjnych oraz do dwóch zestawów łuków.*



### Zbieżność

8\. Nakładamy wiązanie zbieżności na łuki.

:   8.1. Zaznacz punkt końcowy łuku zewnętrznego i najbliższy mu punkt końcowy sąsiedniego łuku wewnętrznego.
:   8.2. Wybierz narzędzie **[<img src=images/Constraint_Tangent.svg style="width:16px"> [Utwórz styczną](Sketcher_ConstrainTangent/pl.md)**. Dzięki temu dwa sąsiadujące ze sobą łuki łagodnie połączą się w punktach końcowych.

8.3. Powtarzaj tą czynność dla poszczególnych punktów końcowych łuków, aż powstanie profil zamknięty.


**Uwaga:**

bardzo często zastosowanie wiązania zbieżności spowoduje przesunięcie geometrii w celu uzyskania płynnego połączenia. Być może trzeba będzie użyć kursora do zmiany położenia punktów przed nałożeniem następnego wiązania zbieżności. Spróbuj umieścić punkty końcowe w taki sposób, aby dwa łuki nie były zbytnio od siebie oddalone, dzięki czemu można je połączyć za pomocą krótkiej, a nie długiej linii.

Na tym etapie stworzyliśmy zamknięty profil, ponieważ końce wszystkich łuków zostały związane razem. Teraz możemy wprowadzić wiązania punktów odniesienia, aby ustalić kształt szkicu. Podczas gdy wymiary linii i łuków pozostają niezmienione, możemy przeciągać punkty szkicu i obserwować, jak zmienia się cały szkic.

<img alt="" src=images/06_Sk01_Sketcher_tangency_constraints.png  style="width:" height="400px;">



*Szkic z wiązaniami zbieżności nałożonymi na łuki, które powodują zamknięcie kształtu.*



## Wiązania wymiarów 

Wiązania te definiują liczbowe odległości między dwoma punktami, oraz kąty między dwoma liniami.



### Odległości i kąty 

9\. Ustalamy rozmiar linii konstrukcyjnych.

:   9.1. Zaznacz linię konstrukcyjną związaną pionowo.
:   9.2. Wybierz narzędzie **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Ustal pionowa odległość ...](Sketcher_ConstrainDistanceY/pl.md)**
:   9.3. Ustaw długość na {{Value|30 mm}}. Ponieważ wszystkie linie konstrukcyjne są związane taką samą długością, wszystkie te linie dostosowują swoje rozmiary w tym samym czasie.

10\. Ustawiamy kąt pomiędzy liniami konstrukcyjnymi.

:   10.1. Zaznacz pionową linię konstrukcyjną i kolejna linię znajdującą się najbliżej niej.
:   10.2. Wybierz narzędzie **[<img src=images/Constraint_InternalAngle.svg style="width:16px"> [Ustaw kąt linii](Sketcher_ConstrainAngle/pl.md)**.
:   10.3. Ustaw wartość kąta na {{Value|72°}}.
:   10.4. Powtórz tę samą procedurę dla każdej pary sąsiadujących linii.
:   
    **Uwaga:**na tym etapie szkic może mieć bardzo niewiele swobody, co oznacza, że jego kształt nie może być zbytnio zmieniony. Jeśli spróbujesz dodać więcej wiązań, mogą one spowodować konflikt z już istniejącymi. Jeśli tak jest, nie dodawaj tych wiązań i przejdź do następnych kroków.

<img alt="" src=images/07a_Sk01_Sketcher_length_constraint.png  style="width:" height="400px;"> <img alt="" src=images/07b_Sk01_Sketcher_angle_constraint.png  style="width:" height="400px;">



*Szkic z wiązaniem długości nakładanym na jedną pionową linię konstrukcyjną ''(po lewej)'', oraz wiązaniem kątowym na trzy pary linii konstrukcyjnych ''(po prawej)''.*



### Promień

11\. Ustalamy rozmiar łuków.

:   11.1. Zaznacz jeden z łuków zewnętrznych umieszczonych na końcu linii konstrukcyjnej.
:   11.2. Wybierz narzędzie **[<img src=images/Constraint_Radius.svg style="width:16px"> [Zwiąż łuk ...](Sketcher_ConstrainRadius/pl.md)**.
:   11.3. Ustaw długość promienia na {{Value|8 mm}}. Ponieważ wszystkie łuki zewnętrzne są związane tym samym promieniem, wszystkie te łuki dostosowują rozmiary w tym samym czasie.
:   11.4. Zaznacz jeden z łuków wewnętrznych, pomiędzy dwoma łukami zewnętrznymi.
:   11.5. Wybierz narzędzie **[<img src=images/Constraint_Radius.svg style="width:16px"> [Zwiąż łuk ...](Sketcher_ConstrainRadius/pl.md)**.
:   11.6. Ustaw wartość promienia na {{Value|11mm}}. Ponieważ wszystkie łuki wewnętrzne są związane tym samym promieniem, wszystkie te łuki dostosowują rozmiary w tym samym czasie.

<img alt="" src=images/08a_Sk01_Sketcher_radius_1_constraint.png  style="width:" height="400px;"> <img alt="" src=images/08b_Sk01_Sketcher_radius_2_constraint.png  style="width:" height="400px;">



*Szkic z wiązaniami promienia nałożonymi na łuki zewnętrzne ''(po lewej)'' i wewnętrzne ''(po prawej)''.*


:   11.7. Na koniec wybierz koło ze środka szkicu, naciśnij przycisk **[<img src=images/Constraint_Radius.svg style="width:16px"> [Zwiąż łuk ...](Sketcher_ConstrainRadius/pl.md)**, i podaj wartość {{Value|8mm}}.

Powinieneś zakończyć swoją pracę szkicem całkowicie związanym. Można to potwierdzić zauważając zmianę koloru geometrii głównej oraz komunikatem, który jest pokazany w polu [Widoku połączonego](Task_panel/pl.md).

<img alt="" src=images/09_Sk01_Sketcher_fully_constrained.png  style="width:" height="400px;">



*Szkic z zastosowanymi wszystkimi wiązaniami geometrycznymi i dotyczącymi układu odniesienia.*



## Wytłaczanie

12\. Teraz, gdy mamy już całkowicie związany szkic, można go wykorzystać do stworzenia jednolitej bryły.

:   12.1. Wyjdź z trybu edycji szkicu, naciskając przycisk **Zamknij** lub naciskając dwukrotnie klawisz **Esc**. Szkic powinien pojawić się w [widoku drzewa](tree_view/pl.md) oraz w oknie [widoku 3D](3D_view/pl.md).
:   12.2. Przejdź do Środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md).
:   12.3. Po wybraniu szkicu w [widoku drzewa](Tree_view/pl.md) naciśnij **[<img src=images/PartDesign_Body.svg style="width:16px"> [Stwórz nową zawartość](PartDesign_Body/pl.md)**, wybierz domyślną płaszczyznę *XY* i naciśnij **OK**. Szkic powinien pojawić się teraz wewnątrz obiektu.
:   12.4. Wybierz szkic, a następnie naciśnij **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnij wybrany szkic](PartDesign_Pad/pl.md)**, wybierz domyślne opcje i naciśnij przycisk **OK**, aby wykonać wyciągnięcie bryły.

<img alt="" src=images/09b_Sk01_Sketcher_fully_constrained_clean.png  style="width:" height="400px;"> <img alt="" src=images/10_Sk01_Sketcher_solid_extrusion.png  style="width:" height="400px;">



*Po lewej: szkic w pełni związany, z zaznaczonymi tylko najważniejszymi z wiązań. Po prawej: wyciągnięcie wykonane z [Projekt Części: Wyciągnij wybrany szkic](PartDesign_Pad/pl.md).*



## Informacje dodatkowe 

Aby uzyskać bardziej szczegółowy opis szkicownika, przejdź do dokumentacji [Środowiska pracy Szkicownik](Sketcher_Workbench/pl.md), a także przeczytaj dokumentację [Informator do szkicownika](Sketcher_reference/pl.md).

Ograniczenie szkicu może być wykonane na wiele różnych sposobów. Ogólnie rzecz biorąc, zaleca się użycie najpierw ograniczeń geometrycznych i zminimalizowanie liczby ograniczeń w układzie odniesienia, ponieważ upraszcza to pracę wewnętrznego solwera wiązań. Aby to zbadać, powtórz ten przykład, dodając teraz ograniczenia w innej kolejności.

-   Najpierw należy związać linie konstrukcyjne przed narysowaniem łuków.
-   Lub określ rozmiar łuków przed uczynieniem ich stycznymi.
-   Lub ustaw kąt linii konstrukcyjnych przed dodaniem kolejnych elementów.
-   Spróbuj użyć innej geometrii konstrukcji.


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > Basic Sketcher Tutorial/pl
