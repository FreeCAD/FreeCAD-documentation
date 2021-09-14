# PartDesign tutorial/pl

 {{TutorialInfo/pl
|Topic= Szkicowanie
|Level= Początkujący
|Time= 15 minut
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 lub nowszy
|Files= Nie dołączono
}}

## Wprowadzenie

Ten poradnik ma na celu zapoznanie czytelnika z podstawowym przepływem pracy w środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md). Czytelnik zobaczy jak tworzyć obiekty 3D na podstawie szkiców, wykonywać operacje odejmowania oraz jak powielać określone cechy we wzorze.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width:480px;">

### Wymagania

-   FreeCAD w wersji v0.17 lub wyższej.
-   Czytelnik ukończył poradnik [Podstawy dla środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md)

### Procedura

#### Tworzenie geometrii 3D 

Celem środowiska roboczego **Projekt Części** jest umożliwienie użytkownikowi tworzenia geometrii w przestrzeni 3D. W związku z tym jest ono wyposażone w narzędzia do wykorzystania szkiców i przekształcania ich w obiekty 3D.

Aby to osiągnąć, istnieją dwa narzędzia: <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Wyciągnij](PartDesign_Pad/pl.md) oraz <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Wyciągnij przez obrót](PartDesign_Revolution/pl.md). Obok ich subtraktywnych odpowiedników *(<img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [kieszeń](PartDesign_Pocket/pl.md) i <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [rowek](PartDesign_Groove/pl.md))* tworzą większość typowych akcji używanych przez to środowisko pracy.

1.  Przełącz się do środowiska produkcyjnego Projekt Części.
2.  Z zaznaczonym szkicem w oknie <img src=images/PartDesign_Body.svg style="width:widoku drzewa](Tree_view/pl.md), naciśnij przycisk **[16px"> [Zawartość](PartDesign_Body/pl.md)**, wybierz domyślną płaszczyznę XY i naciśnij przycisk **OK**. Szkic powinien pojawić się teraz wewnątrz zawartości.
3.  Wybierz <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Wyciągnij wybrany szkic](PartDesign_Pad/pl.md).
4.  Ustaw odległość na {{SpinBox|5 mm }}.
5.  Naciśnij na przycisk **OK**.

Innym sposobem na tworzenie geometrii 3D jest narzędzie <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Wyciągnij wybrany szkic przez obrót](PartDesign_Revolution/pl.md).

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width:480px;">

1.  Utwórz nową zawartość narzędziem **<img src=images/PartDesign_Body.svg style="width:16px"> [Projekt Części Zawartość](PartDesign_Body/pl.md)**, a następnie szkic na podstawie powyższego obrazka.
2.  Szkic może znajdować się na dowolnej płaszczyźnie, ale powinien przylegać do osi poziomej.
3.  Wybierz narzędzie <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Wyciągnij wybrany szkic przez obrót](PartDesign_Revolution/pl.md).
4.  Ustaw parametr **Oś** na wartość {{ComboBox|Pozioma oś szkicu}}.
5.  Ustaw kąt na 360°.

#### Cechy odejmujące 

Zaczniemy od utworzenia szkicu z kształtem, który chcemy odjąć.

1.  Wybierz górną płaską powierzchnię \"wyciągnięcia przez obrót\".
2.  Wybierz <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Utwórz nowy szkic](Sketcher_NewSketch/pl.md).
3.  Wybierz narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometria zewnętrzna](Sketcher_External/pl.md).
4.  Zbliż się do krawędzi wyciągnięcia. Łuk powinien być podświetlony.
5.  Wybierz łuk. W szkicu powinien zostać on wyświetlony innym kolorze.
6.  Utwórz sześciokąt o środku w tym samym punkcie co łuk i ustaw promień okręgu pomocniczego na 5mm.


{{Message| '''Geometria zewnętrzna'''
Po utworzeniu elementu 3D możliwe jest utworzenie odniesień do niego w szkicu.
# Wybierz narzędzie <img src="images/Sketcher_External.svg" width=32px> [Geometria zewnętrzna](Sketcher_External/pl.md).
# Przybliż kursor myszki do elementu, do którego chcesz się odnieść, na przykład do krawędzi '''wyciągnięcia'''.
# Kliknij na nim
# Na szkicu w miejscu elementu, do którego chcesz się odnieść, powinny pojawić się nowe elementy w innym kolorze.}}

<img alt="" src=images/PartDesign_pocket_exercise.png  style="width:480px;">

Następnie przejdziemy do zastosowania funkcji **Kieszeń**.

1.  Wybierz szkic.
2.  Wybierz narzędzie <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;">. [Kieszeń](PartDesign_Pocket/pl.md).
3.  Ustaw parametr **Typ** na wartość {{ComboBox|Przez wszystkie}}.

#### Cechy tworzone wzorami 

Przypomnij sobie profil wyciągany, który został utworzony na początku tego poradnika.

1.  Wybierz górną ścianę obiektu.
2.  Utwórz nowy szkic.
3.  Utwórz geometrię odniesienia powiązaną z górnym ramieniem figury.
4.  Utwórz okrąg związany ze środkiem łuku pomocniczego.
5.  Ustaw jego promień na 3mm.
6.  Przesuń szkic przez cały detal.

Zamiast tworzyć okrąg dla każdego otworu w szkicu, wprowadzimy pojęcie **Cechy wzorca**. Narzędzia te działają na zasadzie powielania elementu, który został już utworzony i który chcemy odtworzyć w układzie liniowym lub kołowym. Użyjemy kombinacji **liniowych** i **biegunowych**\' cech wzoru symulacyjnie, aby uzyskać końcowy detal.

1.  W [widoku drzewa](Tree_view/pl.md) wybierz element **Kieszeń**, który właśnie utworzyliśmy.
2.  Wybierz narzędzie <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Utwórz cechę wielokrotnej transformacji](PartDesign_MultiTransform/pl.md)

W oknie [widoku połączonego](Combo_view/pl.md) jesteśmy teraz proszeni o wprowadzenie obiektów do **Transformacji**, którą chcemy uzyskać. Zauważ, że w sekcji **Parametry Transformacji wielokrotnej** widzimy, że FreeCAD zidentyfikował Kieszeń jako **Cechę bazową**, a w drugiej części okienka proszeni jesteśmy o **Kliknięcie prawym przyciskiem myszy** w celu wprowadzenia cech wzoru.

1.  Kliknij prawym przyciskiem myszy w pole.
2.  Wybierz pozycję **Dodaj szyk liniowy**.
3.  Ustaw opcję **Kierunek**\' na wartość {{ComboBox|Pionowa Oś Szkicu}}.
4.  Ustaw długość na wartość {{SpinBox|10 mm }}.
5.  Pozostaw liczbę wystąpień na {{SpinBox|2 }}.
6.  Kliknij na przycisk **OK**.
7.  Kliknij prawym przyciskiem myszy ponownie w pole, aby dodać **Wzór biegunowy**. Zauważ, że w oknie widoku 3D został dodany wzór liniowy.
8.  Ustaw liczbę wystąpień na {{SpinBox|5 }}.
9.  Kliknij dwukrotnie na przycisk **OK**.

Po wykonaniu tego zadania powinieneś mieć następujący wynik.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width:480px;">

Jeśli nie, edytuj ponownie operację Transformacja wielokrotna, klikając na niej dwukrotnie w widoku drzewa. Sprawdź obie cechy wzoru, aby wykryć konieczne modyfikacje, takie jak **Oś** oraz czy **Kierunek** musi zostać odwrócony.

Zakończyliśmy teraz prezentacje podstawowego przepływu pracy dla środowiska [Projekt Części](PartDesign_Workbench/pl.md).
