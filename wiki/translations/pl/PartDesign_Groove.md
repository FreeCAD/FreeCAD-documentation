---
- GuiCommand:
   Name: PartDesign Groove
   Name/pl: Projekt Części: Rowek
   MenuLocation: Projekt części -> Utwórz cechę przez odjęcie -> Kieszeń
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Revolution/pl
---

# PartDesign Groove/pl



## Opis

Narzędzie **Rowek** obraca wybrany szkic lub profil wokół danej osi, wycinając materiał z podpory.

![](images/PartDesign_Groove_example.svg )



*Powyżej: szkic ''(A)'' jest obracany wokół osi ''(B)''. Wynikowy rowek na bryle ''(C)'' jest pokazany po prawej stronie.*



## Użycie

1.  Wybierz szkic, który ma zostać obrócony.

    :   Alternatywnie można użyć ściany na istniejącej bryle. {{VersionPlus/pl|0.17}}
2.  Szkic musi być zmapowany do płaskiej ściany istniejącej bryły lub elementu środowiska Projekt Części, w przeciwnym razie zostanie wyświetlony komunikat o błędzie. {{VersionMinus/pl|0.16}}
3.  Naciśnij przycisk **<img src="images/PartDesign_Groove.svg" width=24px> '''Rowek'''**.
4.  Ustaw parametry rowka *(patrz następna sekcja)*.
5.  Naciśnij przycisk **OK**.



## Opcje

Podczas tworzenia rowka okno dialogowe **Parametry wyciągnica przez obrót** oferuje kilka parametrów określających sposób obracania szkicu.

+++
| ![](images/partdesign_groove_parameters.png ) | ### Oś                                                                                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | -   **Pionowa oś szkicu**: wybiera pionową oś szkicu.                                                                                                                                                                                                                                                             |
|                                                                          | -   **Pozioma oś szkicu**: wybiera poziomą oś szkicu.                                                                                                                                                                                                                                                             |
|                                                                          | -   **Oś szkicu**: wybiera linię konstrukcyjną zawartą w szkicu używanym przez Rowek. Pierwsza linia konstrukcyjna utworzona w szkicu będzie oznaczona jako *Oś szkicu 0*. Lista rozwijana będzie zawierać jedną niestandardową oś szkicu dla każdej linii konstrukcyjnej. {{VersionMinus/pl|0.16}} |
|                                                                          | -   **Linia konstrukcyjna**: wybiera linię konstrukcyjną zawartą w szkicu używanym przez Rowek. Lista rozwijana będzie zawierać pozycję dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna utworzona w szkicu będzie oznaczona jako *Linia konstrukcyjna 1*. {{VersionPlus/pl|0.17}}     |
|                                                                          | -   **Oś bazowa (X/Y/Z)**: wybiera oś X, Y lub Z położenia początkowego bryły. {{VersionPlus/pl|0.17}}.                                                                                                                                                                                             |
|                                                                          | -   **Wybierz odniesienie\...**: umożliwia wybór w oknie widoku 3D krawędzi na bryle lub [linii odniesienia](PartDesign_Line/pl.md). {{VersionPlus/pl|0.17}}.                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Kąt                                                                                                                                                                                                                                                                                                           |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | Określa kąt, przez który ma zostać utworzony rowek, np. 360° oznacza pełny, ciągły obrót. Nie jest możliwe określenie ujemnych kątów *(zamiast tego należy użyć opcji **Odwrócony**)* lub kątów większych niż 360°.                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Symetrycznie do płaszczyzny                                                                                                                                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | Jeśli opcja ta jest zaznaczona, rowek będzie rozciągał się o połowę określonego kąta w obu kierunkach od płaszczyzny szkicu.                                                                                                                                                                                      |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                      |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Odwrócony                                                                                                                                                                                                                                                                                                     |
|                                                                          |                                                                                                                                                                                                                                                                                                                   |
|                                                                          | Jeśli opcja zostanie zaznaczona, kierunek wykonania rowka ulegnie odwróceniu z domyślnego zgodnego z ruchem wskazówek zegara na przeciwny.                                                                                                                                                                        |
+++



## Właściwości

Poniżej znajdują się właściwości, które można zdefiniować po utworzeniu elementu. Właściwości danych \"Podstawowe\" i \"Oś\" nie można edytować.

-    **Kąt**: kąt obrotu. Patrz sekcja [Kąt](#Kąt.md).

-    **Etykieta**: etykieta nadana operacji, może zostać zmieniona w dogodny sposób.

-    **Midplane**: przyjmuje wartość {{true/pl}} lub {{false/pl}}. Zobacz sekcję [Symetrycznie do płaszczyzny](#Symetrycznie_do_płaszczyzny.md).

-    **Odwrócony**: przyjmuje wartość prawda lub fałsz. Zobacz sekcję [Odwrócony](#Odwrócony.md).

-    **Ulepsz**: przyjmuje wartość {{true/pl}} lub {{false/pl}}. Ustawienie na prawda powoduje oczyszczenie bryły z resztek krawędzi pozostawionych przez elementy. Zobacz stronę [Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów. {{VersionPlus/pl|0.17}}





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/pl
