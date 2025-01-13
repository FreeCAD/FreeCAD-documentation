# Mouse navigation/pl
## Informacje ogólne 

**Nawigacja myszką** w programie FreeCAD jest bardzo elastyczna i intuicyjna, z kilkoma wskazówkami możesz go używać po minucie praktyki. FreeCAD obsługuje wiele stylów nawigacji myszki. Domyślny styl nawigacji jest określany jako [Nawigacja CAD](#CAD.md) i jest bardzo intuicyjny i praktyczny, ale FreeCAD udostępnia również kilka alternatywnych stylów nawigacji do wyboru. Wybrany styl jest używany we wszystkich środowiskach pracy.

Więcej informacji na temat zaznaczania obiektów znajdziesz na stronie [Metody zaznaczania](Selection_methods/pl.md).

Więcej informacji na temat manipulowania obiektami znajdziesz na stronie [Przemieszczenie](Std_TransformManip/pl.md).



## Wybór stylu nawigacji 

1.  Wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk **[<img src=images/NavigationCAD_dark.svg style="width:16px">** na pasku [Statusu](Status_bar/pl.md)
    -   Kliknij prawym przyciskiem myszy pusty obszar w oknie [widoku 3D](3D_view/pl.md), a następnie wybierz **Style nawigacji** z menu kontekstowego.
    -   Użyj [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md). W menu wybierz **Edycja → Preferencje**, a następnie **Wyświetlanie → Nawigacja → Styl nawigacji w przestrzeni 3D**.
2.  Wybierz styl z listy.
3.  Opcjonalnie zmień styl **Techniki orbitalnej**: naciśnij przycisk **[<img src=images/NavigationCAD_dark.svg style="width:24px">** w pasku [Statusu](Status_bar/pl.md), a następnie wybierz **Ustawienia  → Technika orbitalna**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).
4.  Opcjonalnie zmień **Tryb obracania**. Zobacz [Edytor preferencji](Preferences_Editor/pl.md).
5.  Jeśli wybrano styl nawigacji **CAD**: opcjonalnie zmień ustawienie **Włącz animację**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).



## Dostępne style nawigacji 

W przypadku wszystkich stylów nawigacji, o ile obiekty nie są wybierane ze szkicu w trybie edycji, należy przytrzymać klawisz **Ctrl**, aby wybrać wiele obiektów.

Następujące opcje klawiatury są dostępne dla wszystkich trybów:

-    **Ctrl**\+ {{ASCII|43}} i **Ctrl** + {{ASCII|22}} lub **PgUp** i **PgDn** aby odpowiednio przybliżać i oddalać.

-   Klawisze strzałek, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, aby przesuwać widok w lewo/prawo i góra/dół.

-    **Shift**\+ {{ASCII|17}} i **Shift** + {{ASCII|16}} aby obracać widok o 90 stopni.



### Blender

Styl nawigacji Blendera był wzorowany na [Blender](https://www.blender.org).


{{Blender Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obracanie widoku
|Pan_name=Przesuń

|Shift=**Shift**

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

|Rotate_view_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor.

|Pan_text=Przytrzymaj **Shift** i środkowy przycisk myszy a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć kursor.
}}



### CAD

Jest to domyślny styl nawigacji. Pozwala on użytkownikowi na prostą kontrolę widoku i nie wymaga użycia klawiszy klawiatury poza dokonywaniem wielokrotnego wyboru.


{{CAD Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok<br>Metoda pierwsza
|Rotate_view_alt_name=Obróć widok<br>Metoda druga
|Pan_name=Przesuń

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Naciśnij lewy przycisk myszki nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do powiększania i pomniejszania.

Kliknięcie środkowego przycisku myszy wyśrodkowuje widok na położeniu kursora.

|Rotate_view_text=Przytrzymaj środkowy przycisk myszy a następnie wciśnij i przytrzymaj lewy przycisk myszy, po czym przesuń kursor.

Jeśli przyciski zostaną zwolnione przed zatrzymaniem ruchu myszy, obracanie widoku jest kontynuowane, jeśli opcja ta jest włączona.

Podwójne kliknięcie środkowym przyciskiem myszy ustawia nowy punkt obrotu.

|Rotate_view_alt_text=Przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

W tej metodzie środkowy przycisk myszy może zostać puszczony po naciśnięciu prawego przycisku myszy.

Użytkownicy, którzy używają myszki prawą ręką, mogą uznać tę metodę za łatwiejszą od metody pierwszej.

|Pan_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor.

|Zoom_mode_text=Tryb przybliżania/oddalania: przytrzymaj klawisze **Ctrl** i **Shift**, wciśnij prawy przycisk myszy raz a następnie przesuń kursor.

|Rotate_view_mode_text=Tryb obracania: Przytrzymaj klawisz **Shift**, naciśnij raz prawy przycisk myszy, a następnie przesuń kursor.

|Pan_mode_text=Tryb przesuwania: przytrzymaj klawisz **Ctrl**, wciśnij prawy przycisk myszy raz a następnie przesuń kursor.
}}



### Gesture

Ten styl został opracowany z myślą o obsłudze za pomocą ekranu dotykowego i pióra. Można go jednak używać także z myszą i jest zalecany do stosowania na komputerach Mac z gładzikiem.


{{Gesture Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Pan_name=Przesuń
|Tilt_view_name=Widok pochylenia

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

|Rotate_view_text=Przytrzymaj lewy przycisk myszy a następnie przesuń kursor.
W [Szkicowniku](Sketcher_Workbench/pl.md) i innych trybach edycji to zachowanie jest wyłączone. Przytrzymaj **Alt** podczas wciskania przycisku myszy aby wejść w tryb obrotu.

Aby ustawić punkt skupienia kamery do obrotu, kliknij punkt środkowym przyciskiem myszy. Opcjonalnie można wycelować kursor w punkt i nacisnąć klawisz **H** na klawiaturze.

|Pan_text=Przytrzymaj prawy przycisk myszy a następnie przesuń kursor.

|Tilt_view_text=Przytrzymaj lewy i prawy przycisk myszy a następnie przesuń kursor w bok.

|Select_gesture_text=Stuknij aby wybrać.

|Zoom_gesture_text=Przesuń dwoma palcami bliżej lub dalej od siebie.

|Rotate_view_gesture_text=Przesuń jednym palcem aby obrócić.

Przytrzymaj klawisz **Alt** gdy pracujesz w [Szkicowniku](Sketcher_Workbench/pl.md).

|Pan_gesture_text=Przesuń dwoma palcami.

Alternatywnie, dotknij i przytrzymaj, a następnie przeciągnij. W ten sposób symuluje się ruch obrotowy prawym przyciskiem myszy.

|Tilt_view_gesture_text=Obróć wyobrażalną linię, którą tworzą dwa punkty dotknięcia.

Metoda ta jest domyślnie wyłączona. Aby ją uaktywnić, przejdź do **Edycja → Preferencje ... → Wyświetlanie → Nawigacja** i odznacz pole wyboru "Wyłącz gest obrotu na ekranie dotykowym".
}}



### Maya-Gesture 

W trybie nawigacji Maya-Gesture, przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza **Alt** i przycisku myszy, dlatego wymagana jest mysz z trzema przyciskami. Możliwe jest także używanie gestów, ponieważ ten tryb został rozwinięty w stosunku do trybu [Gesture](#Gesture.md).

{{MayaGesture Navigation \|Select_name=Wybór \|Zoom_name=Przybliż - oddal \|Rotate_view_name=Obróć widok \|Pan_name=Przesuń \|Tilt_view_name=Widok pochylenia

\|Alt=**Alt**

\|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

\|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

Można również przytrzymać **Alt** i prawy przycisk myszy, a następnie przesunąć kursor.

\|Rotate_view_text=Przytrzymaj **Alt** i lewy przycisk myszy a następnie przesuń kursor.

\|Pan_text=Przytrzymaj **Alt** i środkowy przycisk myszy a następnie przesuń kursor.

\|Tilt_view_text=Przytrzymaj **Alt** oraz lewy i prawy przycisk myszy a następnie przesuń kursor w bok.



### OpenCascade

Styl nawigacji OpenCascade był wzorowany na [OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal
|Rotate_view_name=Obróć widok
|Pan_name=Przesuń

|Ctrl=**Ctrl**

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

Można również przytrzymać **Ctrl** i lewy przycisk myszy, a następnie przesunąć kursor.

|Rotate_view_text=Przytrzymaj środkowy przycisk myszy a następnie wciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

Można również przytrzymać **Ctrl** i prawy przycisk myszy, a następnie przesunąć kursor.

|Pan_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor. Można przytrzymać **Ctrl**.
}}



### OpenInventor

Nawigacja OpenInventor *(dawniej Inventor)* została wymodelowana na podstawie [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Aby móc wybrać obiekty kursorem myszki, należy dodatkowo przytrzymać klawisz **Shift** lub **Ctrl**.

Ten styl nie jest oparty na nawigacji Autodesk Inventor.

{{OpenInventor Navigation \|Select_name=Wybierz \|Zoom_name=Przybliż - oddal \|Rotate_view_name=Obróć widok \|Pan_name=Przesuń

\|Shift=**Shift**

\|Select_text=Przytrzymaj **Shift**, a następnie naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

Przytrzymaj klawisz **Ctrl**, aby wybrać wiele obiektów.

\|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

Alternatywnie można przytrzymać środkowy przycisk myszy, a następnie nacisnąć i przytrzymać lewy przycisk myszy, po czym przesunąć kursor.

\|Rotate_view_text=Przytrzymaj lewy przycisk myszy, a następnie przesuń kursor.

\|Pan_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor.



### OpenSCAD

Styl nawigacji w programie OpenSCAD był wzorowany na [OpenSCAD](https://openscad.org/).

{{OpenSCAD_Navigation \|Select_name=Wybierz \|Zoom_name=Przybliż - oddal \|Rotate_view_name=Obróć widok \|Pan_name=Przesuń

\|Shift=**Shift**

\|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz zaznaczyć.


{{VersionMinus/pl|0.21}}

Przytrzymaj **Ctrl** i **Shift** podczas naciskania przycisku myszki, aby przeciągnąć obiekt na szkicu w trybie edycji.

\|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

Można również przytrzymać środkowy przycisk myszy, a następnie przesunąć kursor.

Lub przytrzymaj **Shift** i prawy przycisk myszy a następnie przesuń kursor.

\|Rotate_view_text=Przytrzymaj lewy przycisk myszy, a następnie przesuń kursor.

Alternatywnie, gdy szkic jest w trybie edycji, przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

\|Pan_text=Przytrzymaj prawy przycisk myszy a następnie przesuń kursor.



### Revit

Styl nawigacji Revit był wzorowany na stylu [Revit Autodesk](https://en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Pan_name=Przesuń

|Shift=**Shift**

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

|Rotate_view_text=Przytrzymaj **Shift** i środkowy przycisk myszy a następnie przesuń kursor.

Ewentualnie przytrzymaj środkowy przycisk myszy, a następnie naciśnij i przytrzymaj prawy przycisk myszy, po czym przesuń kursor.

|Pan_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor.

Można również przytrzymać lewy i prawy przycisk myszy, a następnie przesunąć kursor.

<span id="TinkerCAD_navigation"></span>
===TinkerCAD===

Styl nawigacji TinkerCAD był wzorowany na stylu [https://en.wikipedia.org/wiki/Tinkercad TinkerCAD].

{{TinkerCAD Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Pan_name=Przesuń

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Użyj kółka myszy do przybliżania i oddalania.

|Rotate_view_text=Przytrzymaj prawy przycisk myszy, a następnie przesuń kursor.

|Pan_text=Przytrzymaj środkowy przycisk myszy a następnie przesuń kursor.
}}

<span id="Touchpad_navigation"></span>
===Touchpad===

W przypadku nawigacji za pomocą panelu dotykowego przesuwanie, powiększanie i obracanie widoku wymaga użycia klawisza modyfikatora przy jednoczesnej obsłudze panelu dotykowego. This style can also be used with a mouse.

{{Touchpad Navigation
|Select_name=Wybierz
|Zoom_name=Przybliż - oddal 
|Rotate_view_name=Obróć widok
|Pan_name=Przesuń

|Ctrl=**Ctrl**
|Shift=**Shift**
|Alt=**Alt**

|Select_text=Naciśnij lewy przycisk myszy nad obiektem, który chcesz wybrać.

|Zoom_text=Przytrzymaj **Ctrl** i **Shift** a następnie przesuń kursor.

|Rotate_view_text=Przytrzymaj **Alt** a następnie przesuń kursor.

Można również przytrzymać **Shift** i lewy przycisk myszy, a następnie przesunąć kursor.

|Pan_text=Przytrzymaj **Shift** a następnie przesuń kursor.
}}

<span id="Hardware_support"></span>
== Wspierany sprzęt ==

FreeCAD obsługuje również niektóre [urządzenia wejściowe 3D](3D_input_devices/pl.md).

<span id="Recommended_navigation_for_macOS"></span>
==Polecana nawigacja dla macOS==

W komputerach MacBook z gładzikiem nawigacja za pomocą gestów działa bardzo dobrze, ale gesty mają specjalne znaczenie:
* Powiększenie: przeciągnij dwoma palcami,
* Obrót: przeciągnij trzema palcami,
* Przesuwanie: **Ctrl** + trzy palce.



---
⏵ [documentation index](../README.md) > Mouse navigation/pl
