# Basic modeling tutorial/pl
---
 TutorialInfo:l
   Topic:  Wprowadzenie do modelowania
   Level:  Początkujący
   Time:  15 minut
   Author: User:Normandc
   FCVersion: dowolny
   Files: Nie dołączono
}}



## Wprowadzenie

Ten Podstawowy Samouczek Modelowania pokaże Ci jak modelować żelazny kształtownik. Jedną rzeczą, którą należy wiedzieć jest to, że FreeCAD jest z założenia modularny, i tak jak w przypadku wielu innych programów CAD, zawsze jest więcej niż jeden sposób na zrobienie czegoś. Przeanalizujemy tutaj dwie metody.

Ten poradnik został napisany przy użyciu wersji 0.15 programu FreeCAD.

## Zanim zaczniemy 

Pamiętaj, że FreeCAD jest wciąż we wczesnej fazie rozwoju, więc możesz nie być tak wydajny jak w przypadku innych aplikacji CAD i z pewnością napotkasz błędy lub doświadczysz awarii. FreeCAD ma teraz możliwość zapisywania plików kopii zapasowych. Liczba tych plików może być określona w oknie dialogowym preferencji. Nie wahaj się pozwolić na dwa lub trzy pliki zapasowe, dopóki nie poznasz dobrze zasad działania programu FreeCAD.

Często zapisuj swoją pracę, od czasu do czasu zapisz ją pod inną nazwą, abyś miał \"bezpieczną\" kopię, do której możesz wrócić, i bądź przygotowany na to, że niektóre polecenia mogą nie dać Ci oczekiwanych rezultatów.

## Techniki modelowania Intro 

Pierwszą ** techniką modelowania bryłowego jest Constructive Solid Geometry **. Istnieje również szczegółowe wyjaśnienie ** Konstrukcyjna geometria bryły na wiki. Pracujesz z kształtami typu bryły pierwotne, takimi jak sześciany, walce, kule i stożki, aby skonstruować geometrię poprzez łączenie ich, odejmowanie jednego kształtu od drugiego lub przecinanie ich. Narzędzia te są częścią środowiska pracy Część. Możesz również stosować przekształcenia na kształtach, jak np. zaokrąglenia lub sfazowania na krawędziach. Te narzędzia również znajdują się w środowisku pracy Część.

Dostępne są też bardziej zaawansowane narzędzia. Zaczynasz od narysowania dwuwymiarowego profilu, który będziesz albo wyciągać, albo obracać.

Zacznijmy więc od próby zrobienia kilku żelaznych nóg do stołu za pomocą tych 2 metod.

## Metoda pierwsza - Konstrukcyjna geometria bryły 

1.  Zacznij od środowiska pracy Część !.
2.  Jeśli nie otworzyłeś nowego dokumentu FreeCAD **, z rozwijanego menu kliknij **Plik , Nowy** lub kliknij przycisk !{width="32"}. **Utwórz nowy, pusty dokument**.
3.  Kliknij na przycisk !{width="32"} Sześcian, aby utworzyć sześcian.
4.  Zmień jego wymiary wybierając go w przestrzeni 3D lub klikając na zakładce Projekt po lewej stronie, a następnie,
5.  Kliknij na zakładkę Dane na dole i zmień wartości dla Długość, Szerokość i Wysokość na 50mm, 50 i 750 ** **Uwaga**: *w czasie, gdy te rysunki były wykonywane, właściwości były uporządkowane inaczej, wysokość była pierwsza*\'.
6.  Sześcian wypełnia teraz większą część widoku 3D. Kliknij na przycisk !{width="32"} Dopasuj wszystko, aby dopasować widok do nowo utworzonego sześcianu.
7.  Utwórz następny sześcian w ten sam sposób, ale z wartościami L=40, W=40 i H=750mm. Domyślnie będzie on nałożony na pierwszy. **
8.  Odejmij teraz drugi sześcian od pierwszego. Wybierz najpierw pierwszy kształt **, a następnie drugi **, kolejność wyboru jest ważna! * na wybór CAD lub Blender)*.
9.  Na pasku narzędzi środowiska pracy Część, kliknij na przycisk narzędzia !{width="32"} Wytnij.

!Rys. 1.1 Pierwszy sześcian

!Rys. 1.2 Drugi sześcian nałożony na pierwszy, gotowy do przeprowadzenia operacji odjęcia

!Rys. 1.3 Po odjęciu

Masz teraz swój pierwszy żelazny kątownik **. Zauważysz, że w zakładce Model po lewej stronie, oba pola zostały zastąpione obiektem \"Cięcie\". Właściwie to nie zniknęły, lecz zostały zgrupowane pod obiektem Cięcie. Kliknij przycisk **+** znajdujący się przed nim, a zobaczysz, że oba pola nadal tam są, ale nie są już aktywne **. Jeśli klikniesz na którymś z nich i wciśniesz **Spacja**, zostanie uaktywnione. Spacja przełącza widoczność wybranych obiektów. **

Nie chcesz, aby kąt był ustawiony w ten sposób? Wystarczy, że zmienisz położenie kształtu Box001. Zaznacz go, wyłącz jego ukrycie i w zakładce Dane kliknij na przycisk **+** przed napisem Umiejscowienie, następnie rozwiń parametr Pozycja i zmień jego współrzędne X i Y. Wciśnij klawisz **Enter**, ponownie ukryj kształt Box001, a orientacja kąta jest teraz inna. ** Możesz nawet zmienić wymiary któregoś z kształtów, a obiekt Cięcie zostanie zaktualizowany.

!Rys. 1.4 Operacja wycięcia zachowuje swoje oryginalne obiekty **")

!Rys. 1.5 Oryginalne sześciany mogą być nadal widoczne.

Przy okazji, możemy dodać zaokrąglenia do kątownika, aby wyglądał bardziej realistycznie, używając narzędzia !{width="32"} Zaokrąglenie. **

!Fig. 1.6 Zaokrąglone krawędzie

## 2. Metoda - przez wyciągnięcie profilu 

Ta metoda wymaga, abyś zaczął od narysowania profilu 2D. Musisz aktywować środowisko pracy Rysunek Roboczy !.

-   Jeśli nie otworzyłeś nowego dokumentu FreeCAD **, z rozwijanego menu kliknij Plik , Nowy lub kliknij przycisk !{width="32"} **Utwórz nowy pusty dokument**.

### Ustawienie płaszczyzny roboczej 

Najpierw musimy określić, na której płaszczyźnie robocza ma być umieszczony nasz profil.

1.  Zlokalizuj pasek narzędzi wyświetlony poniżej. W zależności od preferencji użytkownika Rysunku Roboczego, może on znajdować się poniżej głównego paska narzędzi, po lewej lub po prawej stronie.

    :   !
2.  Naciśnij przycisk **Automatycznie** **.
3.  W zależności od preferencji Rysunku Roboczego, rozwija się okno dialogowe **Wybierz płaszczyznę** w panelu bocznym Zadania, lub poziomy pasek narzędzi oznaczony jako \"aktywne polecenie\": **Wybierz płaszczyznę**. Zobacz na stronie Uwaga na temat przycisku płaszczyzny roboczej zrzuty ekranu pokazujące dwa rozwinięte tryby.
4.  Pozostawimy w polu *Odsunięcie* wartość zero.
5.  Naciśnij przycisk **XY** aby ustawić płaszczyznę roboczą na XY. Zamyka to panel Zadania lub rozwinięte przyciski. Przycisk \"Automatycznie\" będzie teraz ponownie oznaczony jako \"Góra\", aby pokazać, że jest to aktywna płaszczyzna.

### Kreślenie profilu 

1.  Wybierz narzędzie !{width="32"} Linia łamana **.
2.  Zaznacz pola \"Względnie\" i \"Wypełnienie\".
3.  Zamiast rysować kształt w widoku 3D, wpiszemy współrzędne w polach *Globalnie X*, *Globalnie Y* i *Globalnie Z*. Proces ten wygląda następująco:
    1.  Kliknij w pole wejściowe *Globalnie X*;
    2.  Wprowadź wartość zgodnie z listą wypunktowaną poniżej i naciśnij klawisz **TAB**, aby przejść do pola wejściowego *Globalnie Y*.
    3.  Wprowadź wartość *Globalnie Y* i naciśnij klawisz **TAB** aby przejść do pola wejściowego *Globalnie Z*.
    4.  W polu *Globalnie Z* pozostaw wartość zero i naciśnij klawisz **ENTER** aby zatwierdzić współrzędne punktu.
    5.  Powtórz dla następnych 5 punktów.
        -   **Współrzędne** **.
        -   Pierwszy punkt: 0, 0, 0.
        -   Drugi punkt: 50, 0, 0.
        -   Trzeci punkt: 0,10, 0.
        -   Czwarty punkt: -40, 0, 0 **Uwaga:** *W wersji FreeCAD 0.16 występuje błąd, który usuwa poprzedni punkt, gdy wprowadzamy znak minus w polu wprowadzania danych. Obejściem tego problemu jest wprowadzenie wartości dodatniej, następnie umieszczenie kursora przed liczbą i dodanie znaku minus. *.
        -   Piąty punkt: 0, 40, 0.
        -   Szósty punkt: -10, 0, 0.
4.  Naciśnij przycisk **Zamknij** aby zamknąć profil. Powinieneś teraz mieć ten profil, zatytułowany **DWire** w zakładce Model:

!Fig. 1.7 Bazowa linia łamana

Naciśnij klawisz **0** ** na klawiaturze numerycznej, aby ustawić widok na aksonometryczny.

### Wyciągnie profilu 

Aktywuj środowisko pracy !{width="32"} Część albo z menu wyboru Środowisk pracy, albo z menu **Std_View_Menu/pl   Widok , Środowiska pracy , Część**{: mediawiki}.

Kliknij na przycisk narzędzia **Image:Part_Extrude.svg   32px Part_Extrude/pl**{: mediawiki}.

W zakładce Zadania po lewej stronie wybierz obiekt **Polilinia**. Następnie wprowadź żądaną długość, powiedzmy {{Value   750mm}}{: mediawiki}. Pozostaw kierunek na Z = 1. Wciśnij przycisk **OK**. Powinieneś mieć teraz obiekt **Wyciągnięcie** w zakładce Model **.

!Fig. 1.8 Wyciągnięty obiekt

Ta metoda ma małe zastrzeżenie w porównaniu do poprzedniej: aby edytować kształt, musisz edytować linię łamaną, nie jest to tak proste jak w poprzedniej metodzie.

Jest też kilka innych sposobów, aby to zrobić! Mam nadzieję, że te dwa przykłady pozwolą Ci na rozpoczęcie pracy. Na pewno napotkasz jakieś przeszkody po drodze **, ale nie wahaj się zadawać pytań na forum FreeCAD!

### Uwaga na temat przycisku płaszczyzny roboczej 

Etykieta na twoim przycisku może być różna, w zależności od twojej wersji, a także od tego, co robiłeś wcześniej. Etykieta przycisku może być następująca: \" Góra\", \"Przód\", \"Bok\", \"Brak\" lub też przedstawiać reprezentację wektorową, taką jak d. Może być również pusta. Na przykład:

!Wybierz płaszczyznę - Brak

!Wybierz płaszczyznę - Góra

!Wybierz płaszczyznę - Widok  Po naciśnięciu przycisku opcje zostaną rozwinięte do jednej z poniższych konfiguracji.

!**Wybór płaszczyzny** parametry przedstawione w trybie panelu Zadania.

!**Wybór płaszczyzny** parametry przedstawione w trybie paska narzędzi. 

Powyższe instrukcje będą działać, bez względu na to, jaką etykietę posiada Twój przycisk.


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/pl
