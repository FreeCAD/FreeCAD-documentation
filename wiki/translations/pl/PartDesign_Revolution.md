---
- GuiCommand:/pl
   Name:PartDesign Revolution
   Name/pl:Projekt Części: Wyciągnij przez obrót
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Wyciągnij przez obrót
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Rowek](PartDesign_Groove/pl.md)
---

# PartDesign Revolution/pl



## Opis

Narzędzie **Wyciągnij przez obrót** tworzy bryłę poprzez obrót wybranego szkicu lub obiektu 2D wokół określonej osi.

![](images/PartDesign_Revolution_example.svg ) 
*Powyżej: szkic ''(A)'' jest obracany o 270 stopni w kierunku przeciwnym do ruchu wskazówek zegara wokół osi ''(B)'', wynikowa bryła ''(C)'' jest pokazana po prawej stronie.*



## Użycie

1.  Wybierz szkic, który ma zostać obrócony. Alternatywnie można użyć ściany na istniejącej bryle.
2.  Naciśnij przycisk **<img src="images/PartDesign_Revolution.svg" width=24px> '''Wyciągnij przez obrót'''**.
3.  Ustaw parametry wyciągnięcia *(patrz następna sekcja)*.
4.  Naciśnij przycisk **OK**.



## Opcje

Podczas tworzenia obrotu okno dialogowe *Parametry wyciągnięcia przez obrót* oferuje kilka różnych właściwości określających sposób obrotu szkicu.

+++
| ![](images/partdesign_revolution_parameters.png ) |                                                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Oś                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Ta opcja określa oś, wokół której szkic ma być obracany.                                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | -   **Pionowa oś szkicu**: wybiera pionową oś szkicu.                                                                                                                                                                                                                                                                                     |
|                                                                                  | -   **Pozioma oś szkicu**: wybiera poziomą oś szkicu.                                                                                                                                                                                                                                                                                     |
|                                                                                  | -   **Linia konstrukcyjna**: wybiera linię konstrukcyjną zawartą w szkicu używanym przez wyciągnięcie. Lista rozwijana będzie zawierać pozycję dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna będzie oznaczona jako *Linia konstrukcyjna 1*.                                                                               |
|                                                                                  | -   **Oś bazowa (X/Y/Z)**: wybiera oś X, Y lub Z odniesienia położenia bryły.                                                                                                                                                                                                                                                             |
|                                                                                  | -   **Wybierz odniesienie \...**: umożliwia wybór w widoku 3D krawędzi na bryle lub [linii odniesienia](PartDesign_Line/pl.md).                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Kąt                                                                                                                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Kontroluje to kąt, przez który ma zostać utworzony obrót, np. 360° będzie pełnym, ciągłym obrotem. Obrazy w sekcji [Przykłady](#Przykłady.md) demonstrują niektóre z możliwości określania różnych kątów. Nie jest możliwe określenie kątów ujemnych (zamiast tego należy użyć opcji **Odwrócony**) lub kątów większych niż 360°. |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Symetrycznie do płaszczyzny                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Jeśli opcja ta jest zaznaczona, obrót będzie rozciągał się o połowę określonego kąta w obu kierunkach od płaszczyzny szkicu.                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  |                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | ### Odwrócony                                                                                                                                                                                                                                                                                                                             |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
|                                                                                  | Jeśli opcja zostanie zaznaczona, kierunek obrotu ulegnie odwróceniu z domyślnego zgodnego z ruchem wskazówek zegara na przeciwny.                                                                                                                                                                                                         |
+++



## Właściwości

Poniżej znajdują się właściwości, które można zdefiniować po utworzeniu elementu. Właściwości danych \"Podstawowe\" i \"Oś\" nie można edytować.

-    **Kąt**: kąt obrotu. Patrz sekcja [Kąt](#Kąt.md).

-    **Etykieta**: etykieta nadana operacji, może zostać zmieniona w dogodny sposób.

-    **Midplane**: przyjmuje wartość {{true/pl}} lub {{false/pl}}. Zobacz sekcję [Symetrycznie do płaszczyzny](#Symetrycznie_do_płaszczyzny.md).

-    **Odwrócony**: przyjmuje wartość prawda lub fałsz. Zobacz sekcję [Odwrócony](#Odwrócony.md).

-    **Ulepsz**: przyjmuje wartość {{true/pl}} lub {{false/pl}}. Ustawienie na prawda powoduje oczyszczenie bryły z resztek krawędzi pozostawionych przez elementy. Zobacz stronę [Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów.



## Przykłady

![Przykładowy obrót przy użyciu linii konstrukcyjnej jako osi obrotu: Na tym obrazku kąt wynosi 75°, obrót odbywa się wokół linii konstrukcyjnej *(oś szkicu 0)*.](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg )



## Przydatne odnośniki internetowe 

[Szczegółowy przykład użycia](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) na forum.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/pl
