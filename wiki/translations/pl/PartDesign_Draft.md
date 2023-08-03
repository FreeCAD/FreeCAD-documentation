---
 GuiCommand:
   Name: PartDesign Draft
   Name/pl: Projekt części: Pochylenie ścian
   MenuLocation: Projekt Części , Zastosuj funkcjeę ulepszenia , Pochylenie ścian
   Workbenches: PartDesign_Workbench/pl
---

# PartDesign Draft/pl



## Opis

Narzędzie <img alt="" src=images/PartDesign_Draft.svg  style="width:24px;"> **Pochylenie ścian** tworzy pochylenie kątowe wybranych ścian obiektu. Dodaje on do dokumentu obiekt **Pochylenie ścian** wraz z jego reprezentacją w oknie [widoku drzewa](Tree_view/pl.md).

   --
  ![Wybierz jedną lub więcej ścian na obiekcie przed uruchomieniem narzędzia. Tutaj zostały wybrane 2 ściany.](images/PartDesign_Draft-01.png ) ![Wyświetlanie parametrów funkcji w Panelu zadań.](images/PartDesign_Draft-02.png ) ![Dodano 2 ściany i zastosowano 10 stopniowe pochylenie. Dolna płaszczyzna pozostała wymiarowo niezmienna, podczas gdy pochylenie spowodowało zmniejszenie górnej płaszczyzny.](images/PartDesign_Draft-03.png ) ![Płaszczyzna neutralna została zmieniona na górną. Teraz górna płaszczyzna pozostała stabilna wymiarowo, podczas gdy szkic powiększył dolną płaszczyznę..](images/PartDesign_Draft-04.png ) ![Kierunek ścinania jest ustawiony na dolną prawą krawędź, co powoduje, że projekt jest ścinany w lewo..](images/PartDesign_Draft-05.png ) ![Zaznaczenie pola wyboru Kierunek odwrotny spowodowało zastosowanie zanurzenia do wewnątrz zamiast na zewnątrz..](images/PartDesign_Draft-06.png )   
   --






## Użycie



### Dodanie pochylenia ścian 

1.  Opcjonalnie [aktywuj](PartDesign_Body#Active_status/pl.md) bryłę, do której ma zostać zastosowane ścięcie.
2.  Wybierz jedną lub więcej powierzchni bryły.
3.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/PartDesign_Draft.svg" width=16px> [Pochylenie ścian](PartDesign_Draft/pl.md)**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj funkcję ulepszenia → <img src="images/PartDesign_Draft.svg" width=16px> Pochylenie ścian**.
4.  Jeśli nie ma aktywnej bryły, a w dokumencie znajdują się dwie lub więcej brył, zostanie otwarte okno dialogowe **Wymagana jest aktywna zawartość** z prośbą o uaktywnienie jednej z nich. Jeśli jest tylko jedna zawartość, zostanie ona uaktywniona automatycznie.
5.  Zostanie otwarty [panel zadań](Task_panel/pl.md) funkcji **Parametry funkcji pochylenie ścian**. Więcej informacji na ten temat znajdziesz w sekcji [Opcje](#Opcje.md).
6.  Naciśnij przycisk **OK**, aby zakończyć.

:   *Pamiętaj*\':
    -   Ponieważ dla danej cechy musi istnieć przynajmniej jedna ściana, ostatnia pozostała na liście ściana nie może zostać usunięta.



### Edycja pochylenia ścian 

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Szkic w oknie [Widok drzewa](Tree_view.md).
    -   Kliknij obiekt Szkic prawym przyciskiem myszy w oknie [Widok drzewa](Tree_view.md) i wybierz **Edytuj Pochylenie ścian** z menu kontekstowego.
2.  Otworzy się panel [Panel zadań](Task_panel.md) **Parametry funkcji pochylenia ścian**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.



## Opcje

-    **Dodaj ścianę**: Dodaje ściany do zaznaczenia, naciśnij przycisk **Dodaj ścianę** i wybierz więcej ścian.

-    **Usuń ścianę**: Wybierz sposób usuwania ścian z zaznaczenia:

    -   Zaznacz jedną lub więcej powierzchni na liście i naciśnij klawisz **Del** lub kliknij listę prawym przyciskiem myszy i wybierz z menu kontekstowego polecenie **Skasuj**.
    -   Naciśnij przycisk **Usuń ścianę**. Wszystkie poprzednio zaznaczone powierzchnie zostaną podświetlone na fioletowo. Zaznacz każdą ścianę, która ma zostać usunięta.

-    **Kąt początkowy**: Ustaw kąt nachylenia narzędzia, wprowadzając wartość lub klikając strzałki w górę/w dół.

-    **Płaszczyzna neutralna**: Ustaw płaszczyznę neutralną, naciskając przycisk **Płaszczyzna neutralna** i wybierając ścianę, która nie może zmieniać wymiarów.

-    **Kierunek wyciągania**: Ustaw kierunek wyciągnięcia, naciskając przycisk **Kierunek wyciągnięcia**, a następnie wybierz krawędź. Kierunek wyciągania działa tylko wtedy, gdy została ustawiona płaszczyzna neutralna. Wyniki mogą być nieprzewidywalne.

-    **Odwróć kierunek wyciągnięcia**: Odwróć kierunek wyciągnięcia, zaznaczając pole wyboru **Odwróć kierunek wyciągnięcia**. Spowoduje to przełączenie pochylenia między kątami dodatnimi i ujemnymi.



## Uwagi

Narzędzie Pochylenie ścian działa tylko na powierzchniach, które nie są styczne z innymi powierzchniami. Często popełnianym błędem jest próba zastosowania funkcji do powierzchni, na którą nałożono już zaokrąglenie. Aby rozwiązać ten problem, należy usunąć zaokrąglenie, zastosować pochylenie ścian, a następnie ponownie zastosować zaokrąglenie.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Pochylenie ścian środowiska Projekt Części wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Kąt|Angle**: Wartość nie może być ujemna. Domyślnie: {{value|1.5 °}}.

-    **Odwrócony|Bool**: Domyślnie przyjmuje wartość: {{FALSE/pl}}.

-    **Baza|LinkSub**: Łącze podrzędne do listy wybranych krawędzi i powierzchni elementu nadrzędnego.

-    **Wsparcie Przekształcenia|Bool**: \"Uwzględnia podstawowy kształt addytywny/subtraktywny, gdy jest używany w cechach wzoru. Jeśli ta opcja zostanie wyłączona, do tworzenia wzorów będzie używana tylko podstawowa część kształtu\". Wartość domyślna: {{FALSE/pl}}.

-    **Dodaj kształt podrzędny|PartShape|ukryte**
    

-    **Cecha bazowa|Link|ukryte**: Łącze do elementu nadrzędnego.

-    **_ Zawartość|LinkHidden|ukryte**: Łącze do zawartości nadrzędnej.


{{Properties_Title|Pochylenie}}

-    **Neutral Plane|LinkSub**: Łącze podrzędne do listy cech nadrzędnych zawierającej płaszczyznę neutralną.

-    **Kierunek wyciągnięcia|LinkSub**
    


{{Properties_Title|Projekt Części}}

-    **Ulepsz|Bool**: \"Ulepsz kształt (usuń zbędne krawędzie) po operacji dodawania/odejmowania\". Wartość domyślna jest określana przez preferencję **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu**. Zobacz [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Og.C3.B3lne.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Draft/pl
