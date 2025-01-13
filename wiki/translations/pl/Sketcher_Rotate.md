---
 GuiCommand:
   Name: Sketcher Rotate
   Name/pl: Szkicownik: Przekształcenie biegunowe
   MenuLocation: Szkic , Narzędzia szkicownika , Przekształcenie biegunowe
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **T**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Rotate/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Rotate.svg  style="width:24px;"> Narzędzie **Przekształcenie biegunowe** obraca lub opcjonalnie tworzy obrócone kopie wybranych elementów. Kopie są równomiernie rozłożone wzdłuż kąta obrotu.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [parametry w widoku](Sketcher_Preferences/pl#Ogólne.md).
Dim-OVP = Wymiarowe parametry w widoku.

1.  Wybierz jedną lub więcej krawędzi i/lub obiektów [punktów](Sketcher_CreatePoint/pl.md). Wiązania, z wyjątkiem [poziomych](Sketcher_ConstrainHorizontal/pl.md) i [pionowych](Sketcher_ConstrainVertical/pl.md), dotyczące wybranych elementów są również przetwarzane. Jeśli oryginalne elementy zostaną obrócone, wszelkie inne powiązane z nimi wiązania zostaną usunięte.
2.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnięcie przycisku **<img src="images/Sketcher_Rotate.svg" width=16px> '''Przekształcenie biegunowe'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Rotate.svg" width=16px> Przekształcenie biegunowe**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_Rotate.svg" width=16px> Przekształcenie biegunowe** z menu podręcznego.
    -   Skrót klawiaturowy: **Z**, a następnie **P**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Sekcja **Parametry obrotu** jest dodawana w górnej części [okna dialogowego](Sketcher_Dialog.md).
5.  Opcjonalnie zmień liczbę **kopii** *(jeśli liczba wynosi zero, oryginalne elementy są obracane)*:
    -   Wprowadź liczbę.
    -   Naciśnij przycisk **U**, aby zwiększyć liczbę.
    -   Naciśnij przycisk **J**, aby zmniejszyć liczbę.
6.  Opcjonalnie zaznacz pole wyboru **Zastosuj więzy równości**, aby utworzyć [więzy równości](Sketcher_ConstrainEqual/pl.md) zamiast kopii wiązań odległości, promienia i średnicy.
7.  Wybierz środek obrotu. Lub z Pos-OVP: wprowadź jego współrzędną X i/lub Y.
8.  Wybierz punkt do zdefiniowania kąta początkowego. Lub z Dim-OVP: wprowadź jego współrzędne.
9.  Wybierz punkt do zdefiniowania kąta obrotu. Lub z Dim-OVP: wprowadź jego współrzędne.
10. Oryginalne obiekty zostają obrócone lub powstają ich obrócone kopie. Nie są dodawane żadne wiązania oparte o Pos-OVP lub Dim-OVP.



## Uwagi

-   Wskazane może być [usunięcie wyrównania osi](Sketcher_RemoveAxesAlignment/pl.md) przed użyciem tego narzędzia.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Rotate/pl
