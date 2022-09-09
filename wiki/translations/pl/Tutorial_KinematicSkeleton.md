---
- TutorialInfo   */pl
   Topic   *Złożenie 3, i Szkielet kinematyczny
   Level   *Podstawowa wiedza o środowisku Złożenie 3 i Szkicownik będzie pomocna
   FCVersion   *0.20 lub nowsza
   Time   *40 minut
   Author   *[FBXL5](User_FBXL5.md)
   SeeAlso   *[Poradnik Złożenie kinematyczne](Tutorial_KinematicAssembly/pl.md), [Poradnik Sterownik kinematyczny](Tutorial_KinematicController/pl.md)
---

# Tutorial KinematicSkeleton/pl





## Wprowadzenie

Ten poradnik prezentuje, jak zbudować prosty mechanizm 2D i dodać elementy przestrzenne, głównie przy użyciu narzędzi z zewnętrznego <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [środowiska Złożenie 3](Assembly3_Workbench/pl.md).

Ten poradnik nie wykorzystuje zasady szkicu szkieletu *(patrz Złożenie 3 [Create-Skeleton-Sketch](https   *//github.com/realthunder/FreeCAD_assembly3/wiki/Create-Skeleton-Sketch) na GitHub)*.

Zamiast tego użyjemy <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części zawierającej tylko jeden <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Szkic](Sketcher_Workbench/pl.md), aby zbudować mechanizm 2D, czyli **szkielet wielu szkiców**.

Wymiary, a także kolory, pochodzą z [poradnika SolveSpace](http   *//solvespace.com/linkage.pl), do którego odwołuje się strona Złożenie 3 z GitHub *(patrz wyżej)*.

## Szkielet wieloszkieletowy 

Ten tzw. szkielet wieloszkicowy składa się z kilku indywidualnych <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Zawartości](PartDesign_Body/pl.md) oraz kontenera <img alt="" src=images/Assembly_New_Assembly.svg  style="width   *16px;"> [Złożenia](Assembly3_CreateAssembly/pl.md). Aby móc dołączyć kolejne obiekty, każda bryła jest umieszczana w osobnym kontenerze Złożenia.

## Obiekty Zawartości 2D 

Zawartości, oraz ich szkice, które są wykorzystywane w tym montażu   *

-   Płyta podstawy *(zielona)*,
-   Korba *(niebieska)*,
-   Dwie ruchome płyty *(czerwona i szara)*,
-   Cztery korbowody *(biały, żółty, fioletowy i brązowy)*.

<img alt="" src=images/Assembly3_SketchSkeleton-01.png  style="width   *400px;"> 
*Wszystkie osiem szkiców indywidualnie pokolorowanych i ręcznie pozycjonowanych poprzez przesunięcie ich zawartości.*

Kształt może odbiegać od kształtu rzeczywistej części, ale położenie złącza definiującego geometrię musi być dokładne.

### Montaż kontenerów 

#### Złożenie nadrzędne 

Aby ustalić lub kontrolować pozycje wszystkich Zawartości potrzebujemy <img alt="" src=images/Assembly_New_Assembly.svg  style="width   *16px;"> Obiektu Złożenia. Dodaje on gałąź złożenia do [Widoku drzewa](Tree_view/pl.md)

-   Naciśnij przycisk **<img src="images/Assembly_New_Assembly.svg" width=16px> [Utwórz złożenie](Assembly3_CreateAssembly/pl.md)**, aby utworzyć gałąź złożenia w [Widoku drzewa](Tree_view/pl.md).

#### Złożenia podrzędne 

Powtórz powyższą czynność, aby utworzyć obiekt Złożenia dla każdej Zawartości i przeciągnij ją go jej kontenera Części. Następnie połącz Zawartość z jej Złożeniem   *

1.  Uaktywnij obiekt Złożenie *(podwójne kliknięcie)*.
2.  Zaznacz okrąg / łuki należące do obiektu Zawartość.
3.  Naciśnij przycisk **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Wiązanie ''zablokowania''](Assembly3_ConstraintLock/pl.md)**, aby przytwierdzić Zawartość w jej złożeniu podrzędnym.

Na przykład Złożenie korbowe powinno wyglądać następująco   *

<img alt="" src=images/Assembly3_SketchSkeleton-25.png  style="width   *500px;"> 
*Gałąź złożenia korby w widoku drzewa oraz korba z zablokowanym elementem w oknie widoku 3D.*

#### Drzewo złożenia 

W widoku Drzewa przeciągnij wszystkie gałęzie złożeń podrzędnych do kontenera Części obiektu nadrzędnego Złożenia.

<img alt="" src=images/Assembly3_SketchSkeleton-26.png  style="width   *300px;"> 
*Gałąź Złożenia w widoku Drzewa*

Teraz są one gotowe do ułożenia.

#### Nieruchoma płyta podstawy 

Najpierw potrzebujemy elementu nieruchomego. Aby całkowicie zamocować Bazę, zwykle wybralibyśmy ścianę, ale w tym przypadku równie dobrze sprawdzi się okrąg.

1.  Wybierz okrąg w części bazowej.
2.  Naciśnij przycisk **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Wiązanie zablokowania](Assembly3_ConstraintLock/pl.md)**, aby ustalić Bazę.

<img alt="" src=images/Assembly3_SketchSkeleton-02.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-03.png  style="width   *300px;"> 
*Wybrany okrąg → Nieruchoma podstawa z utworzonym obiektem Element i wyświetlonym układem współrzędnych ''(ECS)'' elementu ''(kolor zielony)''.*

### Połączenia

W przypadku przegubów wybieramy jeden okrąg z każdego szkicu i używamy funkcji <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width   *16px;"> [Wiązanie zbieżności](Assembly3_ConstraintCoincidence/pl.md). Wiązanie to nie tylko ustawia płaszczyzny XY obu elementów współbieżnie, ale także ustawia ich osie Z współbieżnie.

1.  Wybierz okrąg każdego obiektu, który chcesz połączyć.
2.  Naciśnij przycisk **<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Wiązanie zbieżności](Assembly3_ConstraintCoincidence/pl.md)**.

#### Baza - Korba 

<img alt="" src=images/Assembly3_SketchSkeleton-04.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-05.png  style="width   *300px;"> 
*Zaznaczone okręgi na obiekcie bazowym i korbie → Ulokowana korba z zaznaczonymi utworzonymi obiektami Elementów i ECS ''(kolor zielony)''.*

#### Baza - Płyta górna 

<img alt="" src=images/Assembly3_SketchSkeleton-06.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-07.png  style="width   *300px;"> 
*Zaznaczone okręgi na podstawie i górnej płycie → Ulokowana płyta górna*

Poprzednio utworzone przeguby można rozpoznać po ich reprezentacjach wiązań *(kolor czerwony)*.

#### Korba - Pręt 1 

<img alt="" src=images/Assembly3_SketchSkeleton-08.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-09.png  style="width   *300px;"> 
*Zaznaczone okręgi na Korbie i Pręcie 1 → Ulokowany Pręt 1 i przechylona Korba*

#### Płyta górna - Pręt 1 

Ostatnie ogniwo w tym łańcuchu kinematycznym łączy dwa Elementy, których kierunki Z są już zdefiniowane, a wiązanie <img alt="" src=images/Assembly_ConstraintPointOnLine.svg  style="width   *16px;"> [punkt na linii](Assembly3_ConstraintPointOnLine/pl.md) jest wszystkim, czego potrzebujemy.

1.  Wybierz okrąg z każdego obiektu do połączenia.
2.  Naciśnij przycisk wiązania **<img src="images/Assembly_ConstraintPointOnLine.svg" width=16px> [Punkt na linii](Assembly3_ConstraintPointOnLine/pl.md)**.

<img alt="" src=images/Assembly3_SketchSkeleton-10.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-11.png  style="width   *300px;"> 
*Zaznaczone okręgi na Płycie górnej i Pręcie 1 → Ulokowany Pręt 1 i odchylona Korba i Płyta górna*

Jeśli osie Z trzech elementów lub przegubów są równoległe i leżą na tej samej płaszczyźnie wirtualnej, solver może nie zmienić ich położenia w kolejnym kroku, ponieważ nie jest w stanie zdecydować, w którym kierunku należy obrócić środkowy przegub. Taka sytuacja może wystąpić dla elementu Pręt 1, przegubu Korba - Pręt 1 oraz przegubu Baza - Korba, który mamy tutaj. W takiej sytuacji musimy pomóc solverowi i obrócić jeden obiekt *(np. Korbę)* ręcznie za pomocą narzędzia <img alt="" src=images/Assembly_AxialMove.svg  style="width   *16px;"> [Przesunięcie osiowe](Assembly3_AxialMove/pl.md).

#### Płyta górna - Pręt 2 

Kolejny *(podrzędny)* łańcuch kinematyczny zaczyna się od wiązania <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [zbieżności](Assembly3_ConstraintCoincidence/pl.md).

<img alt="" src=images/Assembly3_SketchSkeleton-12.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-13.png  style="width   *300px;"> 
*Zaznaczone okręgi na Płycie górnej ''(lub podstawie)'' i Pręcie 2 → Umiejscowiony Pręt 2*

#### Pręt 2 - Płyta dolna 

<img alt="" src=images/Assembly3_SketchSkeleton-14.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-15.png  style="width   *300px;"> 
*Zaznaczone okręgi na Pręcie 2 i Płycie dolnej → Ulokowana Płyta dolna i przechylony Pręt 2*

#### Płyta górna - Pręt 3 

<img alt="" src=images/Assembly3_SketchSkeleton-16.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-17.png  style="width   *300px;"> 
*Zaznaczone okręgi na Płycie górnej i Pręcie 3 → Ulokowany Pręt 3 i przeorganizowany górny podłańcuch kinematyczny*

#### Płyta dolna - Pręt 3 

Kolejny *(podrzędny)* łańcuch kinematyczny kończy się na wiązaniu <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Punkt na linii](Assembly3_ConstraintPointOnLine/pl.md).

<img alt="" src=images/Assembly3_SketchSkeleton-18.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-19.png  style="width   *300px;"> 
*Zaznaczone okręgi na Płycie Dolnej i Pręcie 3 → Ulokowany Pręt 3 i przeorganizowane podłańcuchy ukinematyczne*.

Do połączenia obu podłańcuchów kinematycznych wykorzystujemy Pręt 4 z wiązaniem <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width   *16px;"> [Zbieżności](Assembly3_ConstraintCoincidence/pl.md) na jednym końcu oraz wiązaniem <img alt="" src=images/Assembly_ConstraintPointOnLine.svg  style="width   *16px;"> [Punkt na linii](Assembly3_ConstraintPointOnLine/pl.md) na drugim końcu.

#### Korba - Pręt 4 

<img alt="" src=images/Assembly3_SketchSkeleton-20.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-21.png  style="width   *300px;"> 
*Zaznaczone kręgi na Korbie i Pręcie 4 → Umiejscowiony Pręt 4*

#### Płyta dolna - Pręt 1 

<img alt="" src=images/Assembly3_SketchSkeleton-22.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-23.png  style="width   *300px;"> 
*Zaznaczone okręgi na Płycie dolnej i Pręcie 4 → Ulokowany Pręt 4 i ostateczny widok układ zespołu kinematycznego.*

### Siłownik

Ponieważ środowisko Złożenie 3 nie dostarcza żadnych środków do sterowania złożeniami kinematycznymi, potrzebujemy zewnętrznej pomocy, takiej jak w poradniku [Sterownik kinematyczny](Tutorial_KinematicController/pl.md). Aby użyć tego kontrolera, musimy oznaczyć etykietę jednego z wiązań przyrostkiem {{Incode|"Driver"}}, aby uczynić je wiązaniem napędzającym. Może on być oddzielony przez {{Incode|"."}} lub {{Incode|"-"}} dla jasności, ponieważ kontroler sprawdzi tylko czy etykieta kończy się na {{Incode|"Driver"}}.

Zmieniamy zatem etykietę złącza Baza-Korba na {{Incode|Base-Crank.Driver}}.

### Ukończony szkielet 

Gotowy zespół kinematyczny z dezaktywowaną reprezentacją Elementów i Więzów powinien wyglądać następująco   *

<img alt="" src=images/Assembly3_SketchSkeleton-24.png  style="width   *500px;"> 
*Ukończone złożenie widok w oknie [Widoku drzewa](Tree_view/pl.md) oraz w oknie [widoku 3D](3D_view/pl.md)*.

<img alt="" src=images/Assembly3_SketchSkeleton-27.gif  style="width   *500px;"> 
*Animacja GIF wykonana na podstawie sekwencji obrazów z tematu [Poradnik   * Sterownik kinematyczny](Tutorial_KinematicController/pl.md).*

## Dołączanie geometrii w przestrzeni 3D 

Moje oczekiwania dotyczące dołączania nowego obiektu do obiektu bazowego należącego do zespołu kinematycznego były czymś w rodzaju   *

-   Umieść nowy obiekt w kontenerze Część obiektu bazowego.
-   Ustaw nowy obiekt w stosunku do obiektu bazowego.
-   Ustalenie względnego przesunięcia i orientacji za pomocą wiązania Mocowanie.

Ale to byłoby zbyt proste.

Narzędzie <img alt="" src=images/Assembly_ConstraintAttachment.svg  style="width   *16px;"> [Wiązanie umocowania](Assembly3_ConstraintAttachment/pl.md), jak każde narzędzie wiązania w środowisku Złożenie 3, opiera się na wykorzystaniu obiektów Elementów i ich układów współrzędnych *(ECS)* do zadań pozycjonowania.

I tak dołączanie obiektów jest po prostu innym sposobem dodawania obiektów do *(pod)*zespołu.

Dla przykładu dołączmy pręt 4-3D do pręta 4   *

Obiekty mają inną orientację i obiekt 3D powinien być przesunięty względem obiektu 2D.

1.  Umieść nowy obiekt w kontenerze Części obiektu bazowego.
2.  Wybierz dwa odpowiadające sobie okręgi lub łuki.
3.  Naciśnij przycisk **<img src="images/Assembly_ConstraintAttachment.svg" width=16px> [Wiązanie umocowania](Assembly3_ConstraintAttachment/pl.md)**.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-28.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-29.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;">



*Pręt 4 (zablokowany) i pręt 4-3D → Zaznaczone łuki → Ulokowany pręt 4-3D ''(oba układy ECS są w tym samym miejscu z identyczną orientacją)''.*

Widać teraz wyraźnie, że narzędzie <img alt="" src=images/Assembly_ConstraintAttachment.svg  style="width   *16px;"> [Wiązanie umocowania](Assembly3_ConstraintAttachment/pl.md) ignoruje odsunięcie i orientację pomiędzy oboma obiektami.

Jednak pozycja jest już zdefiniowana tak, jak chcieliśmy, więc musimy tylko ręcznie dostosować kąt i zdefiniować pożądane odsunięcie   *

-   Ustaw **Odsunięcie, Kąt** pierwszego elementu w kontenerze Dołączenie, aby dopasować orientację.
-   Ustaw **Odsunięcie, Pozycja, Z** tego samego Elementu, aby zastosować odsunięcie.

W przypadku, gdy ustawimy właściwości drugiego Elementu, ruch kąta i przesunięcia poszedłby w przeciwnym kierunku.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-31.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-32.png  style="width   *200px;">



*Umocowane → Kąt dostosowany → Przesunięcie zdefiniowane*

Gdyby do każdego obiektu 2D był dołączony obiekt 3D, mogłoby to wyglądać następująco   *

<img alt="" src=images/Assembly3_SketchSkeleton-33.gif  style="width   *500px;">

## Uwagi

Sekcja [Dołączanie geometrii w przestrzeni 3D](Tutorial_KinematicSkeleton/pl#Do.C5.82.C4.85czanie_geometrii_w_przestrzeni_3D.md) tylko pokazuje zarys możliwości rozbudowy podzespołu, a inne wiązania lub kombinacje wiązań mogą być bardziej odpowiednie niż wiązanie dołączania.

Ważne jest, aby przesuwać taki zespół kinematyczny w małych krokach, w przeciwnym razie solver podda się i zawiedzie. Prawie niemożliwe jest użycie funkcji <img alt="" src=images/Assembly_Move.svg  style="width   *16px;"> [Przenieś część](Assembly3_MovePart/pl.md) lub <img alt="" src=images/Assembly_AxialMove.svg  style="width   *16px;"> [Przesunięcie osiowe](Assembly3_AxialMove/pl.md) dla tego zadania.

Funkcja <img alt="" src=images/Assembly_ConstraintCoincidence.svg  style="width   *16px;"> [Wiązanie zbieżności](Assembly3_ConstraintCoincidence/pl.md) jest używana do sterowania zespołem kinematycznym, jego właściwość **Kat** *(włączona przez właściwość **Kąt blokady**)* przyjmuje dodatnie lub ujemne liczby zmiennoprzecinkowe większe niż 360, więc może wykonać kilka pełnych obrotów.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tutorial KinematicSkeleton/pl
