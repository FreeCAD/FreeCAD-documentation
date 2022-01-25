# Basic modeling tutorial/pl
---
- TutorialInfo:/pl
   Topic: Wprowadzenie do modelowania
   Level: Początkujący
   Time: 15 minut
   Author:[NormandC](User_Normandc.md)
   FCVersion:dowolny
   Files:Nie dołączono
}}

## Wprowadzenie

Ten Podstawowy Samouczek Modelowania pokaże Ci jak modelować żelazny kształtownik. Jedną rzeczą, którą należy wiedzieć jest to, że FreeCAD jest z założenia modularny, i tak jak w przypadku wielu innych programów CAD, zawsze jest więcej niż jeden sposób na zrobienie czegoś. Przeanalizujemy tutaj dwie metody.

## Zanim zaczniemy 

Pamiętaj, że FreeCAD jest wciąż we wczesnej fazie rozwoju, więc możesz nie być tak wydajny jak w przypadku innych aplikacji CAD i z pewnością napotkasz błędy lub doświadczysz awarii. FreeCAD ma teraz możliwość zapisywania plików kopii zapasowych. Liczba tych plików może być określona w oknie dialogowym preferencji. Nie wahaj się pozwolić na dwa lub trzy pliki zapasowe, dopóki nie poznasz dobrze zasad działania programu FreeCAD.

Często zapisuj swoją pracę, od czasu do czasu zapisz ją pod inną nazwą, abyś miał \"bezpieczną\" kopię, do której możesz wrócić, i bądź przygotowany na to, że niektóre polecenia mogą nie dać Ci oczekiwanych rezultatów.

## Techniki modelowania Intro 

Pierwszą *(i podstawową)* techniką modelowania bryłowego jest [Constructive Solid Geometry *(CSG)*](http://en.wikipedia.org/wiki/Constructive_solid_geometry). Istnieje również szczegółowe wyjaśnienie *(w kontekście FreeCAD)* [Konstrukcyjna geometria bryły](Constructive_solid_geometry/pl.md) na wiki. Pracujesz z kształtami typu bryły pierwotne, takimi jak sześciany, walce, kule i stożki, aby skonstruować geometrię poprzez łączenie ich, odejmowanie jednego kształtu od drugiego lub przecinanie ich. Narzędzia te są częścią środowiska pracy [Część](Part_Workbench/pl.md). Możesz również stosować przekształcenia na kształtach, jak np. zaokrąglenia lub sfazowania na krawędziach. Te narzędzia również znajdują się w środowisku pracy [Część](Part_Workbench/pl.md).

Dostępne są też bardziej zaawansowane narzędzia. Zaczynasz od narysowania dwuwymiarowego profilu, który będziesz albo wyciągać, albo obracać.

Zacznijmy więc od próby zrobienia kilku żelaznych nóg do stołu za pomocą tych 2 metod.

## Metoda pierwsza - Konstrukcyjna geometria bryły 

1.  Zacznij od środowiska pracy [Część](Part_Workbench/pl.md) ![](images/Switch_PartWorkbench.JPG ).
2.  Jeśli nie otworzyłeś nowego dokumentu FreeCAD *(większość okna FreeCAD wygląda na nieaktywną)*, z rozwijanego menu kliknij **Plik → Nowy** lub kliknij przycisk <img alt="" src=images/Document-new.png  style="width:32px;">. **Utwórz nowy, pusty dokument**.
3.  Kliknij na przycisk <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Sześcian](Part_Box/pl.md), aby utworzyć sześcian.
4.  Zmień jego wymiary wybierając go w przestrzeni 3D lub klikając na zakładce Projekt po lewej stronie, a następnie,
5.  Kliknij na zakładkę Dane na dole i zmień wartości dla Długość, Szerokość i Wysokość na 50mm, 50 i 750 *(patrz rys. 1.1)* **Uwaga**: *w czasie, gdy te rysunki były wykonywane, właściwości były uporządkowane inaczej, wysokość była pierwsza*\'.
6.  Sześcian wypełnia teraz większą część widoku 3D. Kliknij na przycisk <img alt="" src=images/Std_ViewFitAll.svg  style="width:32px;"> [Dopasuj wszystko](Std_ViewFitAll/pl.md), aby dopasować widok do nowo utworzonego sześcianu.
7.  Utwórz następny sześcian w ten sam sposób, ale z wartościami L=40, W=40 i H=750mm. Domyślnie będzie on nałożony na pierwszy. *(patrz rys. 1.2)*
8.  Odejmij teraz drugi sześcian od pierwszego. Wybierz najpierw pierwszy kształt *(o nazwie Sześcian)*, a następnie drugi *(o nazwie Sześcian001)*, kolejność wyboru jest ważna! *(Upewnij się, że oba kształty są zaznaczone w drzewie projektu. **Jedna rzecz do zapamiętania:** w trybie nawigacji Inventora, **Ctrl** + kliknięcie nie działa w przypadku wielokrotnego zaznaczania. Przełącz [Profil nawigacji myszką](Mouse_navigation/pl.md) na wybór CAD lub Blender)*.
9.  Na pasku narzędzi środowiska pracy Część, kliknij na przycisk narzędzia <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Wytnij](Part_Cut/pl.md).

![Rys. 1.1 Pierwszy sześcian](images/Tutorial-normand01.jpg )

![Rys. 1.2 Drugi sześcian nałożony na pierwszy, gotowy do przeprowadzenia operacji odjęcia](images/Tutorial-normand02.jpg )

![Rys. 1.3 Po odjęciu](images/Tutorial-normand03.jpg )

Masz teraz swój pierwszy żelazny kątownik *(rys. 1.3)*. Zauważysz, że w zakładce Model po lewej stronie, oba pola zostały zastąpione obiektem \"Cięcie\". Właściwie to nie zniknęły, lecz zostały zgrupowane pod obiektem Cięcie. Kliknij przycisk **+** znajdujący się przed nim, a zobaczysz, że oba pola nadal tam są, ale nie są już aktywne *(rys. 1.4)*. Jeśli klikniesz na którymś z nich i wciśniesz **Spacja**, zostanie uaktywnione. Spacja przełącza [widoczność](Std_ToggleVisibility.md) wybranych obiektów. *(Rys. 1.5)*

Nie chcesz, aby kąt był ustawiony w ten sposób? Wystarczy, że zmienisz położenie kształtu Box001. Zaznacz go, wyłącz jego ukrycie i w zakładce Dane kliknij na przycisk **+** przed napisem Umiejscowienie, następnie rozwiń parametr Pozycja i zmień jego współrzędne X i Y. Wciśnij klawisz **Enter**, ponownie ukryj kształt Box001, a orientacja kąta jest teraz inna. *(Rys. 1.5)* Możesz nawet zmienić wymiary któregoś z kształtów, a obiekt Cięcie zostanie zaktualizowany.

![Rys. 1.4 Operacja wycięcia zachowuje swoje oryginalne obiekty *(sześciany)*](images/Tutorial-normand04.jpg )

![Rys. 1.5 Oryginalne sześciany mogą być nadal widoczne.](images/Tutorial-normand05.jpg )

Przy okazji, możemy dodać zaokrąglenia do kątownika, aby wyglądał bardziej realistycznie, używając narzędzia <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Zaokrąglenie](Part_Fillet/pl.md). 
*(Rys. 1.6)*

![Fig. 1.6 Zaokrąglone krawędzie](images/Tutorial-normand06.jpg )

## 2. Metoda - przez wyciągnięcie profilu 

Ta metoda wymaga, abyś zaczął od narysowania profilu 2D. Musisz aktywować środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) ![](images/Switch_DraftWorkbench.JPG ).

-   Jeśli nie otworzyłeś nowego dokumentu FreeCAD *(większość okna FreeCAD wygląda na nieaktywne)*, z rozwijanego menu kliknij Plik → Nowy lub kliknij przycisk <img alt="" src=images/Document-new.png  style="width:32px;"> **Utwórz nowy pusty dokument**.

### Ustawienie płaszczyzny roboczej 

Najpierw musimy określić, na której [płaszczyźnie robocza](Draft_SelectPlane/pl.md) ma być umieszczony nasz profil.

1.  Zlokalizuj pasek narzędzi wyświetlony poniżej. W zależności od preferencji użytkownika Rysunku Roboczego, może on znajdować się poniżej głównego paska narzędzi, po lewej lub po prawej stronie.

    :   ![](images/DraftPlaneAuto.png )
2.  Naciśnij przycisk **Automatycznie** *(może być oznaczony jako \"Brak\")*.
3.  W zależności od preferencji Rysunku Roboczego, rozwija się okno dialogowe **Wybierz płaszczyznę** w panelu bocznym Zadania, lub poziomy pasek narzędzi oznaczony jako \"aktywne polecenie\": **Wybierz płaszczyznę**. Zobacz na stronie [Uwaga na temat przycisku płaszczyzny roboczej](#Uwaga_na_temat_przycisku_p.C5.82aszczyzny_roboczej.md) zrzuty ekranu pokazujące dwa rozwinięte tryby.
4.  Pozostawimy w polu *Odsunięcie* wartość zero.
5.  Naciśnij przycisk **XY** aby ustawić płaszczyznę roboczą na XY. Zamyka to panel Zadania lub rozwinięte przyciski. Przycisk \"Automatycznie\" będzie teraz ponownie oznaczony jako \"Góra\", aby pokazać, że jest to aktywna płaszczyzna.

### Kreślenie profilu 

1.  Wybierz narzędzie <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Linia łamana *(wielopunktowa polilinia)*](Draft_Wire/pl.md).
2.  Zaznacz pola \"Względnie\" i \"Wypełnienie\".
3.  Zamiast rysować kształt w widoku 3D, wpiszemy współrzędne w polach *Globalnie X*, *Globalnie Y* i *Globalnie Z*. Proces ten wygląda następująco:
    1.  Kliknij w pole wejściowe *Globalnie X*;
    2.  Wprowadź wartość zgodnie z listą wypunktowaną poniżej i naciśnij klawisz **TAB**, aby przejść do pola wejściowego *Globalnie Y*.
    3.  Wprowadź wartość *Globalnie Y* i naciśnij klawisz **TAB** aby przejść do pola wejściowego *Globalnie Z*.
    4.  W polu *Globalnie Z* pozostaw wartość zero i naciśnij klawisz **ENTER** aby zatwierdzić współrzędne punktu.
    5.  Powtórz dla następnych 5 punktów.
        -   **Współrzędne** *(X, Y, Z)*.
        -   Pierwszy punkt: 0, 0, 0.
        -   Drugi punkt: 50, 0, 0.
        -   Trzeci punkt: 0,10, 0.
        -   Czwarty punkt: -40, 0, 0 **Uwaga:** *W wersji FreeCAD 0.16 występuje błąd, który usuwa poprzedni punkt, gdy wprowadzamy znak minus w polu wprowadzania danych. Obejściem tego problemu jest wprowadzenie wartości dodatniej, następnie umieszczenie kursora przed liczbą i dodanie znaku minus. (Ten błąd został usunięty w v0.17)*.
        -   Piąty punkt: 0, 40, 0.
        -   Szósty punkt: -10, 0, 0.
4.  Naciśnij przycisk **Zamknij** aby zamknąć profil. Powinieneś teraz mieć ten profil, zatytułowany **DWire** w zakładce Model:

![Fig. 1.7 Bazowa linia łamana](images/Tutorial-normand07.jpg )

Naciśnij klawisz **0** *(zero)* na klawiaturze numerycznej, aby ustawić widok na aksonometryczny.

### Wyciągnie profilu 

Aktywuj środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Część](Part_Workbench/pl.md) albo z menu wyboru [Środowisk pracy](Std_Workbench/pl.md), albo z menu **[[Std_View_Menu/pl   Widok]] → Środowiska pracy → Część**.

Kliknij na przycisk narzędzia **![](images/)**.

W zakładce Zadania po lewej stronie wybierz obiekt **Polilinia**. Następnie wprowadź żądaną długość, powiedzmy {{Value   750mm}}. Pozostaw kierunek na Z = 1. Wciśnij przycisk **OK**. Powinieneś mieć teraz obiekt **Wyciągnięcie** w zakładce Model *(rys. 1.8)*.

![Fig. 1.8 Wyciągnięty obiekt](images/Tutorial-normand08.jpg )

Ta metoda ma małe zastrzeżenie w porównaniu do poprzedniej: aby edytować kształt, musisz edytować linię łamaną, nie jest to tak proste jak w poprzedniej metodzie.

Jest też kilka innych sposobów, aby to zrobić! Mam nadzieję, że te dwa przykłady pozwolą Ci na rozpoczęcie pracy. Na pewno napotkasz jakieś przeszkody po drodze *(ja tak miałem, gdy po raz pierwszy uczyłem się programu FreeCAD, a mam doświadczenie w projektowaniu 3D CAD)*, ale nie wahaj się zadawać pytań na [forum FreeCAD](https://forum.freecadweb.org)!

### Uwaga na temat przycisku płaszczyzny roboczej 

Etykieta na twoim przycisku może być różna, w zależności od twojej wersji, a także od tego, co robiłeś wcześniej. Etykieta przycisku może być następująca: \" Góra\", \"Przód\", \"Bok\", \"Brak\" lub też przedstawiać reprezentację wektorową, taką jak d(0.0,0.0,1.0). Może być również pusta. Na przykład:

![Wybierz płaszczyznę - Brak](images/DraftPlaneNone.png )

![Wybierz płaszczyznę - Góra](images/DraftPlaneTop.png )

![Wybierz płaszczyznę - Widok](images/DraftPlaneView.png )  Po naciśnięciu przycisku opcje zostaną rozwinięte do jednej z poniższych konfiguracji.

![**Wybór płaszczyzny** parametry przedstawione w trybie panelu Zadania.](images/DraftPlaneTasks.png )

![**Wybór płaszczyzny** parametry przedstawione w trybie paska narzędzi.](images/DraftPlaneToolbarMode.png ) 

Powyższe instrukcje będą działać, bez względu na to, jaką etykietę posiada Twój przycisk.


  {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > Basic modeling tutorial/pl
