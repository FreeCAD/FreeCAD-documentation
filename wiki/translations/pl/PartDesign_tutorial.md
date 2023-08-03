---
 TutorialInfo:l
   Topic:  Szkicowanie
   Level:  Początkujący
   Time:  15 minut
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.16 lub nowszy
   Files:  Nie dołączono
}}

## Wprowadzenie

Ten poradnik ma na celu zapoznanie czytelnika z podstawowym przepływem pracy w środowisku pracy Projekt Części. Czytelnik zobaczy jak tworzyć obiekty 3D na podstawie szkiców, wykonywać operacje odejmowania oraz jak powielać określone cechy we wzorze.

!{width="480"}

### Wymagania

-   FreeCAD w wersji v0.17 lub wyższej.
-   Czytelnik ukończył poradnik Podstawy dla środowiska pracy Szkicownik

### Procedura

#### Tworzenie geometrii 3D 

Celem środowiska roboczego **Projekt Części** jest umożliwienie użytkownikowi tworzenia geometrii w przestrzeni 3D. W związku z tym jest ono wyposażone w narzędzia do wykorzystania szkiców i przekształcania ich w obiekty 3D.

Aby to osiągnąć, istnieją dwa narzędzia: !{width="32"} Wyciągnij oraz !{width="32"} Wyciągnij przez obrót. Obok ich subtraktywnych odpowiedników *{width="32"} kieszeń i !{width="32"} rowek)* tworzą większość typowych akcji używanych przez to środowisko pracy.

1.  Przełącz się do środowiska produkcyjnego Projekt Części.
2.  Z zaznaczonym szkicem w oknie widoku drzewa, naciśnij przycisk **File:PartDesign_Body.svg   16px PartDesign_Body/pl**{: mediawiki}, wybierz domyślną płaszczyznę XY i naciśnij przycisk **OK**. Szkic powinien pojawić się teraz wewnątrz zawartości.
3.  Wybierz !{width="32"} Wyciągnij wybrany szkic.
4.  Ustaw odległość na {{SpinBox   5 mm }}{: mediawiki}.
5.  Naciśnij na przycisk **OK**.

Innym sposobem na tworzenie geometrii 3D jest narzędzie !{width="32"} Wyciągnij wybrany szkic przez obrót.

!{width="480"}

1.  Utwórz nową zawartość narzędziem **File:PartDesign_Body.svg   16px PartDesign_Body/pl**{: mediawiki}, a następnie szkic na podstawie powyższego obrazka.
2.  Szkic może znajdować się na dowolnej płaszczyźnie, ale powinien przylegać do osi poziomej.
3.  Wybierz narzędzie !{width="32"} Wyciągnij wybrany szkic przez obrót.
4.  Ustaw parametr **Oś** na wartość {{ComboBox   Pozioma oś szkicu}}{: mediawiki}.
5.  Ustaw kąt na 360°.

#### Cechy odejmujące 

Zaczniemy od utworzenia szkicu z kształtem, który chcemy odjąć.

1.  Wybierz górną płaską powierzchnię \"wyciągnięcia przez obrót\".
2.  Wybierz !{width="32"} Utwórz nowy szkic.
3.  Wybierz narzędzie !{width="32"} Geometria zewnętrzna.
4.  Zbliż się do krawędzi wyciągnięcia. Łuk powinien być podświetlony.
5.  Wybierz łuk. W szkicu powinien zostać on wyświetlony innym kolorze.
6.  Utwórz sześciokąt o środku w tym samym punkcie co łuk i ustaw promień okręgu pomocniczego na 5mm.


{{Message| '''Geometria zewnętrzna'''
Po utworzeniu elementu 3D możliwe jest utworzenie odniesień do niego w szkicu.
# Wybierz narzędzie Image:Sketcher_External.svg Sketcher_External/pl.
# Przybliż kursor myszki do elementu, do którego chcesz się odnieść, na przykład do krawędzi '''wyciągnięcia'''.
# Kliknij na nim
# Na szkicu w miejscu elementu, do którego chcesz się odnieść, powinny pojawić się nowe elementy w innym kolorze.
---

# PartDesign tutorial/pl

 
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



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/pl
