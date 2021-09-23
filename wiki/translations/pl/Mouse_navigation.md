# Mouse navigation/pl
{{TOCright}}

## Informacje ogólne 

**Nawigacja myszką** w programie FreeCAD jest bardzo elastyczna i intuicyjna, z kilkoma wskazówkami możesz go używać po minucie praktyki. FreeCAD obsługuje wiele stylów nawigacji myszki. Domyślny styl nawigacji jest określany jako **Nawigacja CAD** i jest bardzo intuicyjny i praktyczny, ale FreeCAD oferuje również alternatywne style nawigacji, które możesz wybrać zgodnie z własnymi preferencjami.

## Nawigacja

Ruch myszką używany do manipulacji obiektem różni się w zależności od wybranego stylu nawigacji; aktualnie wybrany styl jest używany dla wszystkich środowisk pracy.

Istnieją dwa sposoby zmiany stylu nawigacji:

-   W menu [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md), {{MenuCommand/pl|Edycja → Preferencje → Wyświetlanie → Widok 3D → Nawigacja 3D}}.
-   Klikając prawym przyciskiem myszy w pustym miejscu okienka widoku 3D, a następnie wybierając {{MenuCommand/pl|Style Nawigacji}} w menu kontekstowym.

### CAD

Jest to domyślny styl nawigacji. Pozwala on użytkownikowi na prostą kontrolę widoku i nie wymaga użycia klawiszy klawiatury poza dokonywaniem wielokrotnego wyboru.


{{CAD Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obróć widok<br>Metoda pierwsza
|Rotate_view_alt_name=Obróć widok<br>Metoda druga
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszki nad obiektem, który chcesz wybrać.

Przytrzymanie przycisku **Ctrl** umożliwia wybór wielu obiektów.
|Pan_text=Trzymając wciśnięty środkowy przycisk myszy, przesuń kursor.
|Pan_mode_text=Tryb przesuwania: przytrzymaj wciśnięty klawisz **Ctrl**, naciśnij raz prawy przycisk myszy, a następnie przesuń wskaźnik. {{VersionPlus/pl|0.17}}
|Zoom_text=Użyj rolki myszy, aby przybliżyć lub oddalić widok.

Kliknięcie środkowego przycisku myszy ponownie wyśrodkowuje widok na pozycję kursora.
|Zoom_mode_text=Tryb powiększania: Przytrzymaj wciśnięty klawisz **Ctrl** oraz **Shift** Naciśnij jednokrotnie prawy przycisk myszy, a następnie przesuń wskaźnik. {{VersionPlus/pl|0.17}}
|Rotate_view_text=Przytrzymaj wciśnięty środkowy przycisk myszy, a następnie przytrzymaj wciśnięty lewy przycisk myszy, kolejnie przesuń kursor.

Położenie kursora po naciśnięciu środkowego przycisku myszy określa środek obrotu. Obracanie działa jak obracanie piłki, poruszającej się wokół jej punktu środkowego. Jeśli przyciski zostaną zwolnione przed zatrzymaniem ruchu myszy, [obracanie](spinning/pl.md) widoku jest kontynuowane, jeśli opcja ta jest włączona.

Podwójne kliknięcie środkowym przyciskiem myszy ustawia nowy punkt obrotu.
|Rotate_view_mode_text=Tryb obracania: Przytrzymaj klawisz **Shift**, naciśnij raz prawy przycisk myszy, a następnie przesuń kursor. {{VersionPlus/pl|0.17}}
|Rotate_view_alt_text=Przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

W tej metodzie środkowy przycisk myszy może zostać puszczony po naciśnięciu prawego przycisku myszy.

Użytkownicy, którzy używają myszki prawą ręką, mogą uznać tę metodę za łatwiejszą od metody pierwszej.
}}

### OpenInventor

Nawigacja OpenInventor *(dawniej Inventor)* została wymodelowana na podstawie [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Aby móc wybrać obiekty kursorem myszki, należy dodatkowo przytrzymać klawisz **Ctrl**.

Ten styl nie jest oparty na nawigacji Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal
|Rotate_view_name=Obracanie widoku
|Ctrl=**Ctrl**
|Select_text=Przytrzymaj klawisz **Ctrl**, a następnie naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Użyj rolki myszki, aby przybliżyć lub oddalić widok.

Alternatywnie można przytrzymać środkowy przycisk myszy, następnie nacisnąć i przytrzymać lewy przycisk myszy, a następnie przesunąć kursor. 
|Rotate_view_text=Przytrzymaj naciśnięty lewy przycisk myszy, a następnie przesuń kursor.}}

### Blender

Styl nawigacji Blendera został wzorowany na modelu [Blender](https://www.blender.org). Wcześniej nie było możliwości przesuwania tylko myszą; zawsze wymagało to trzymania klawisza **Shift**. Zmieniło się to w 2016 roku, teraz można przytrzymać równocześnie lewy i prawy przycisk myszy do przesuwania.


{{Blender Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obracanie widoku
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Shift** i środkowy przycisk myszy, a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć wskaźnik.
|Zoom_text=Użyj rolki myszki, aby przybliżyć lub oddalić widok.
|Rotate_view_text=Przytrzymaj naciśnięty środkowy przycisk myszy, a następnie przesuń kursor.
}}

### Touchpad

W stylu nawigacji Touchpad przy użyciu panelu dotykowego, przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza zmieniającego podstawową funkcję panelu dotykowego. {{Touchpad Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obróć widok
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Naciśnij lewy przycisk panelu dotykowego nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Shift**, a następnie przesuń kursor.
|Zoom_text=Użyj klawisza **PageUp** lub **PageDown** aby przybliżyć i oddalić widok.
|Zoom_alt_text=Alternatywnie, przytrzymaj klawisz **Shift** oraz jednocześnie **Ctrl**, a następnie przesuń kursor.
|Rotate_view_text=Przytrzymaj klawisz **Alt**, a następnie przesuń kursor.
|Rotate_view_alt_text=Alternatywnie, przytrzymaj klawisz **Shift** i lewy przycisk, a następnie przesuń wskaźnik.
}}

### Gesture

Ten styl został wprowadzony w wersji 0.16 i został dostosowany do użycia z ekranem dotykowym i piórem. Niemniej jednak może być również używany z myszką, i jest zalecany do stosowania w przypadku komputerów Mac z tabliczką dotykową. {{Gesture Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obróć widok
|Tilt_view_name=Widok pochylenia
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Select_gesture_text=Stuknij, aby wybrać.
|Pan_text=Przytrzymaj prawy przycisk myszy, a następnie przesuń kursor.
|Pan_gesture_text=Przeciągnij dwoma palcami.

Alternatywnie, dotknij i przytrzymaj, a następnie przeciągnij. W ten sposób symuluje się ruch obrotowy prawym przyciskiem myszy.
|Zoom_text=Użyj rolki myszy, aby powiększyć lub pomniejszyć obraz.
|Zoom_gesture_text=Przeciągnij dwa palce (uszczypnij) bliżej lub dalej od siebie.
|Rotate_view_text=Przytrzymaj lewy przycisk myszy, a następnie przesuń kursor.
W [Sketcher](Sketcher_Workbench.md) i innych trybach edycji ten sposób działania jest wyłączony. Przytrzymaj klawisz **Alt** po naciśnięciu przycisku myszy, aby wejść w tryb rotacji.

To set the camera's focus point for rotation, click a point with the middle mouse button. Opcjonalnie można wycelować kursor w punkt i nacisnąć klawisz **H** na klawiaturze.
|Rotate_view_gesture_text=Przeciągnij jednym palcem, aby obracać.

Przytrzymaj klawisz **Alt** gdy pracujesz w środowisku [Sketcher](Sketcher_Workbench.md).
|Tilt_view_text=Przytrzymaj oba lewy i prawy przycisk myszy, a następnie przesuń kursor na bok. 
|Tilt_view_gesture_text=Obróć umowną linię utworzoną przez dwa punkty dotyku.

W wersji 0.18 metoda ta jest domyślnie wyłączona. Aby ją uaktywnić, przejdź do **Edit → Preferencje → Display** i odznacz pole wyboru "Disable touchscreen tilt gesture".
}}

### Maya-Gesture 

W nawigacji Maya-Gesture, przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza **Alt** wraz z przyciskiem myszy; dlatego też wymagana jest myszka z trzema przyciskami. Możliwe jest również korzystanie z gestów, ponieważ tryb ten został opracowany na podstawie trybu [Gesture](Mouse_navigation/pl#Gesture.md) {{MayaGesture Navigation
|Select_name=Wybór
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obróć widok
|Alt=**Alt**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Alt** i środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Przytrzymaj klawisz **Alt** i prawy przycisk myszy, a następnie przesuń kursor.

Opcjonalnie można użyć kółka myszy, aby powiększyć lub pomniejszyć obraz.
|Rotate_view_text=Przytrzymaj klawisz {**Alt**} i lewy przycisk myszy, a następnie przesuń kursor.
}}

### Revit

Ten styl został wprowadzony w wersji 0.18. <small>(v0.18)</small> 


{{Revit Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - Oddal 
|Rotate_view_name=Obróć widok
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć kursor.

|Zoom_text=Użyj rolki myszy, aby przybliżyć lub oddalić widok.
|Rotate_view_text=Przytrzymaj klawisz **Shift** i środkowy przycisk myszy, a następnie przesuń kursor.

Ewentualnie przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.
}}

### OpenCascade

Ten styl nawigacji został wprowadzony w wersji 0.18. <small>(v0.18)</small> 


{{OpenCascade Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Ctrl=**Ctrl**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Użyj rolki myszy, aby przybliżać i oddalać widok.

Ewentualnie przytrzymaj klawisz **Ctrl** i lewy przycisk myszy, a następnie przesuń kursor.
|Rotate_view_text=Przytrzymaj klawisz **Ctrl** i prawy przycisk myszy, a następnie przesuń kursor.
}}

## Zaznaczanie obiektów 

Obiekty mogą być zaznaczane przez kliknięcie lewym przyciskiem myszy, także przez kliknięcie na obiekt w widoku 3D lub przez zaznaczenie w drzewie widoku. Obecny jest także mechanizm preselekcji, który podświetla obiekty i wyświetla informacje o nich przed zaznaczeniem, podczas najechania myszą na obiekt. Tesli nie chcesz tego zachowania lub masz wolną maszynę, możesz wyłączyć preselekcję w ustawieniach.

### Prosty wybór 

Obiekty można wybrać klikając lewym przyciskiem myszy. Przez kliknięcie na nim w oknie [widoku 3D](3D_view/pl.md), albo wybierając go w [widoku drzewa](Tree_view/pl.md).

### Wybór wstępny 

Istnieje również mechanizm \"Preselekcji\", który podświetla obiekty i wyświetla informacje przed ich wyborem, po prostu wskazuj obiekty kursorem myszki. Jeśli nie podoba Ci się to zachowanie lub posiadasz wolniejszą maszynę, możesz wyłączyć preselekcję w preferencjach.

## Manipulowanie obiektami 

FreeCAD oferuje [manipulator](Manipulator/pl.md), który może być użyty do modyfikowania wyglądu, kształtu lub innych parametrów obiektu.

## Wspierany sprzęt 

FreeCAD obsługuje również niektóre [urządzenia wejściowe 3D](3D_input_devices/pl.md).

## Polecana nawigacja dla macOS 

W komputerach MacBook z gładzikiem nawigacja za pomocą gestów działa bardzo dobrze, ale gesty mają specjalne znaczenie:

-   Powiększenie: przeciągnij dwoma palcami,
-   Obrót: przeciągnij trzema palcami,
-   Przesuwanie: **Ctrl** + trzy palce.

## Opracowanie własnego schematu nawigacji 

Poradnik [Dodanie nowego stylu nawigacji myszką do FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) wprowadza programistów, którzy chcą stworzyć własny wariant nawigacji za pomocą myszy. Wymagana jest znajomość składni języka C++.

---
[documentation index](../README.md) > Mouse navigation/pl
