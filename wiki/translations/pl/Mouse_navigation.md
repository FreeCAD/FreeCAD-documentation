# Mouse navigation/pl
{{TOCright}}

## Informacje ogólne 

**Nawigacja myszką** w programie FreeCAD jest bardzo elastyczna i intuicyjna, z kilkoma wskazówkami możesz go używać po minucie praktyki. FreeCAD obsługuje wiele stylów nawigacji myszki. Domyślny styl nawigacji jest określany jako [Nawigacja CAD](#CAD.md) i jest bardzo intuicyjny i praktyczny, ale FreeCAD udostępnia również kilka alternatywnych stylów nawigacji do wyboru. Wybrany styl jest używany we wszystkich środowiskach pracy.

Więcej informacji na temat zaznaczania obiektów znajdziesz na stronie [Metody zaznaczania](Selection_methods/pl.md).

Więcej informacji na temat manipulowania obiektami znajdziesz na stronie [Przemieszczenie](Std_TransformManip/pl.md).

## Wybór stylu nawigacji 

1.  Wykonaj jedną z następujących czynności   *
    -   Naciśnij przycisk **[<img src=images/NavigationCAD_dark.svg style="width   *16px">** na pasku [Statusu](Status_bar/pl.md)
    -   Kliknij prawym przyciskiem myszy pusty obszar w oknie [widoku 3D](3D_view/pl.md), a następnie wybierz **Style nawigacji** z menu kontekstowego.
    -   Użyj [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md). W menu wybierz **Edycja → Preferencje**, a następnie **Wyświetlanie → Nawigacja → Styl nawigacji w przestrzeni 3D**.
2.  Wybierz styl z listy.
3.  Opcjonalnie zmień styl **Techniki orbitalnej**   * naciśnij przycisk **[<img src=images/NavigationCAD_dark.svg style="width   *24px">** w pasku [Statusu](Status_bar/pl.md), a następnie wybierz **Ustawienia  → Technika orbitalna**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).
4.  Opcjonalnie zmień **Tryb obracania**. Zobacz [Edytor preferencji](Preferences_Editor/pl.md).
5.  Jeśli wybrano styl nawigacji **CAD**   * opcjonalnie zmień ustawienie **Włącz animację**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).

## Dostępne style nawigacji 

### Blender

Styl nawigacji Blendera był wzorowany na [Blender](https   *//www.blender.org).


{{Blender Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obracanie widoku
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Shift** i środkowy przycisk myszy, a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć wskaźnik.
|Zoom_text=Użyj rolki myszki, aby przybliżyć lub oddalić widok.
|Rotate_view_text=Przytrzymaj naciśnięty środkowy przycisk myszy, a następnie przesuń kursor.
}}

### CAD

Jest to domyślny styl nawigacji. Pozwala on użytkownikowi na prostą kontrolę widoku i nie wymaga użycia klawiszy klawiatury poza dokonywaniem wielokrotnego wyboru.


{{CAD Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok<br>Metoda pierwsza
|Rotate_view_alt_name=Obróć widok<br>Metoda druga
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszki nad obiektem, który chcesz wybrać.

Przytrzymanie przycisku **Ctrl** umożliwia wybór wielu obiektów.
|Pan_text=Trzymając wciśnięty środkowy przycisk myszy, przesuń kursor.
|Pan_mode_text=Tryb przesuwania   * przytrzymaj wciśnięty klawisz **Ctrl**, naciśnij raz prawy przycisk myszy, a następnie przesuń wskaźnik.
|Zoom_text=Użyj rolki myszy, aby przybliżyć lub oddalić widok.

Kliknięcie środkowego przycisku myszy ponownie wyśrodkowuje widok na pozycję kursora.
|Zoom_mode_text=Tryb powiększania   * Przytrzymaj wciśnięty klawisz **Ctrl** oraz **Shift** Naciśnij jednokrotnie prawy przycisk myszy, a następnie przesuń wskaźnik.
|Rotate_view_text=Przytrzymaj wciśnięty środkowy przycisk myszy, a następnie przytrzymaj wciśnięty lewy przycisk myszy, kolejnie przesuń kursor.

Jeśli przyciski zostaną zwolnione przed zatrzymaniem ruchu myszy, obracanie widoku jest kontynuowane, jeśli opcja ta jest włączona.

Podwójne kliknięcie środkowym przyciskiem myszy ustawia nowy punkt obrotu.
|Rotate_view_mode_text=Tryb obracania   * Przytrzymaj klawisz **Shift**, naciśnij raz prawy przycisk myszy, a następnie przesuń kursor.
|Rotate_view_alt_text=Przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

W tej metodzie środkowy przycisk myszy może zostać puszczony po naciśnięciu prawego przycisku myszy.

Użytkownicy, którzy używają myszki prawą ręką, mogą uznać tę metodę za łatwiejszą od metody pierwszej.
}}

### Gesture

Ten styl został opracowany z myślą o obsłudze za pomocą ekranu dotykowego i pióra. Można go jednak używać także z myszą i jest zalecany do stosowania na komputerach Mac z gładzikiem.


{{Gesture Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
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

W trybie nawigacji Maya-Gesture, przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza **Alt** i przycisku myszy, dlatego wymagana jest mysz z trzema przyciskami. Możliwe jest także używanie gestów, ponieważ ten tryb został rozwinięty w stosunku do trybu [Gesture](#Gesture.md).


{{MayaGesture Navigation
|Select_name=Wybór
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Alt=**Alt**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Alt** i środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Przytrzymaj klawisz **Alt** i prawy przycisk myszy, a następnie przesuń kursor.

Opcjonalnie można użyć kółka myszy, aby powiększyć lub pomniejszyć obraz.
|Rotate_view_text=Przytrzymaj klawisz {**Alt**} i lewy przycisk myszy, a następnie przesuń kursor.
}}

### OpenCascade

Styl nawigacji OpenCascade był wzorowany na [OpenCascade](https   *//www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal
|Rotate_view_name=Obróć widok
|Ctrl=**Ctrl**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Użyj rolki myszy, aby przybliżać i oddalać widok.

Ewentualnie przytrzymaj klawisz **Ctrl** i lewy przycisk myszy, a następnie przesuń kursor.
|Rotate_view_text=Przytrzymaj klawisz **Ctrl** i prawy przycisk myszy, a następnie przesuń kursor.
}}

### OpenInventor

Nawigacja OpenInventor *(dawniej Inventor)* została wymodelowana na podstawie [Open Inventor](http   *//en.wikipedia.org/wiki/Open_Inventor). Aby móc wybrać obiekty kursorem myszki, należy dodatkowo przytrzymać klawisz **Shift** lub **Ctrl**.

Ten styl nie jest oparty na nawigacji Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal
|Rotate_view_name=Obróć widok
|Ctrl=**Shift**
|Select_text=Przytrzymaj klawisz **Shift**, a następnie naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

Przytrzymaj klawisz **Ctrl**, aby wybrać wiele obiektów.
|Pan_text= Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Użyj kółka myszy do powiększania i pomniejszania.

Alternatywnie można przytrzymać środkowy przycisk myszy, następnie nacisnąć i przytrzymać lewy przycisk myszy, a następnie przesunąć kursor. 
|Rotate_view_text=Przytrzymaj naciśnięty lewy przycisk myszy, a następnie przesuń kursor.}}

### OpenSCAD

Styl nawigacji w programie OpenSCAD był wzorowany na [OpenSCAD](https   *//openscad.org/).


{{Version/pl|0.20}}


{{OpenSCAD_Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal
|Rotate_view_name=Obróć widok 
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz zaznaczyć.
|Pan_text=Przytrzymaj prawy przycisk myszy, a następnie przesuń kursor.
|Zoom_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.
Ewentualnie przytrzymaj klawisz **Shift** i prawy przycisk myszki, a następnie przesuń kursor.
|Rotate_view_text=Przytrzymaj lewy przycisk myszki, a następnie przesuń wskaźnik.
}}

### Revit

Styl nawigacji Revit był wzorowany na stylu [Revit Autodesk](https   *//en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Shift=**Shift**
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj środkowy przycisk myszy, a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć kursor.

|Zoom_text=Użyj rolki myszy, aby przybliżyć lub oddalić widok.
|Rotate_view_text=Przytrzymaj klawisz **Shift** i środkowy przycisk myszy, a następnie przesuń kursor.

Ewentualnie przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.
}}

### TinkerCAD

Styl nawigacji TinkerCAD był wzorowany na stylu [TinkerCAD](https   *//en.wikipedia.org/wiki/Tinkercad).


{{Version/pl|0.20}}


{{TinkerCAD Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok 
|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.
|Pan_text=Trzymając wciśnięty środkowy przycisk myszy, przesuń kursor. 
|Zoom_text=Użyj rolki myszy, aby przybliżyć lub oddalić widok. 
|Rotate_view_text=Trzymając wciśnięty prawy przycisk myszy, przesuń kursor. 
}}

### Touchpad

W przypadku nawigacji za pomocą panelu dotykowego przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza modyfikatora przy jednoczesnej obsłudze panelu dotykowego.


{{Touchpad Navigation
|Select_name=Wybierz
|Pan_name=Przesuń
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Ctrl=**Ctrl**
|Shift=**Shift**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Naciśnij lewy przycisk panelu dotykowego nad obiektem, który chcesz wybrać.
|Pan_text=Przytrzymaj klawisz **Shift**, a następnie przesuń kursor.
|Zoom_text=Użyj klawisza **PageUp** lub **PageDown** aby przybliżyć i oddalić widok.
|Zoom_alt_text=Alternatywnie, przytrzymaj klawisz **Ctrl** oraz jednocześnie **Shift**, a następnie przesuń kursor.
|Rotate_view_text=Przytrzymaj klawisz **Alt**, a następnie przesuń kursor.
|Rotate_view_alt_text=Alternatywnie, przytrzymaj klawisz **Shift** i lewy przycisk, a następnie przesuń wskaźnik.
}}

## Wspierany sprzęt 

FreeCAD obsługuje również niektóre [urządzenia wejściowe 3D](3D_input_devices/pl.md).

## Polecana nawigacja dla macOS 

W komputerach MacBook z gładzikiem nawigacja za pomocą gestów działa bardzo dobrze, ale gesty mają specjalne znaczenie   *

-   Powiększenie   * przeciągnij dwoma palcami,
-   Obrót   * przeciągnij trzema palcami,
-   Przesuwanie   * **Ctrl** + trzy palce.

## Opracowanie własnego schematu nawigacji 

Poradnik [Dodanie nowego stylu nawigacji myszką do FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) wprowadza programistów, którzy chcą stworzyć własny wariant nawigacji za pomocą myszy. Wymagana jest znajomość składni języka C++.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Mouse navigation/pl
