---
- GuiCommand:/pl
   Name:PartDesign LinearPattern
   Name/pl:Projekt Części: Szyk Liniowy
   MenuLocation:Projekt części → Zastosuj szyk → Szyk Liniowy
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:
   SeeAlso:
---

# PartDesign LinearPattern/pl

## Opis

Narzędzie **Szyk liniowy** tworzy równomiernie rozmieszczone kopie elementu wzdłuż linii lub prostej krawędzi.

![](images/PartDesign_LinearPattern_example.svg )

\'\'Powyżej: wyciągnięcie w kształcie litery L *(B)* wykonane na pbazie bryły *(A, zwanej również podstawą)* jest używane do tworzenia liniowego wzou. Wynik *(C)* jest pokazany po prawej stronie\'\'.

## Użycie

Aby utworzyć wzorzec:

1.  Wybierz element *({{Version/pl|0.19}} lub kilka elementów)*, które mają być układane we wzór.
2.  Naciśnij przycisk **[<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''Szyk kołowy'''**.
3.  Zdefiniuj **Kierunek**. Patrz [Opcje](#Opcje.md).
4.  Zdefiniuj **Długość** *(odległość)* między ostatnim skopiowanym wystąpieniem a oryginalnym elementem.
5.  Ustaw liczbę **Wystąpień**.
6.  Jeśli masz kilka elementów we wzorcu, ich kolejność może być ważna, zobacz obrazek z funkcją [Szyk kołowy](PartDesign_PolarPattern/pl#Użycie.md). {{Version/pl|0.19}} Możesz zmienić kolejność, przeciągając element na liście, a wynik pojawi się natychmiast jako podgląd.
7.  Naciśnij **OK**.

Aby dodać lub usunąć elementy z istniejącego wzorca:

1.  Naciśnij przycisk **Dodaj element**, aby dodać element, który ma być wzorcem. Element musi być widoczny w oknie [widoku 3D](3D_view.md):
    1.  Przejdź do widoku drzewa modelu,
    2.  Wybierz w drzewie element, który ma zostać dodany i naciśnij klawisz **Spacja**, aby wybrany element był widoczny w oknie [widoku 3D](3D_view.md),
    3.  Przejdź z powrotem do panelu zadań,
    4.  Wybierz element w oknie [widoku 3D](3D_view.md), zostanie on dodany do listy,
    5.  Powtórz czynność, aby dodać inne elementy.
2.  Naciśnij przycisk **Usuń element**, aby usunąć element z listy, lub kliknij prawym przyciskiem myszy na elemencie z listy i wybierz **Usuń**.

## Opcje

![Parametry Szyku liniowego](images/Linearpattern_parameters_v017.png )

### Kierunek

Podczas tworzenia cech szyku liniowego, dialog \"Szyk liniowy parametry\" oferuje różne sposoby określania kierunku dla szyku.

#### Pozioma oś szkicu 

Używa poziomej osi szkicu jako kierunku dla wzorca.

#### Pionowa oś szkicu 

Używa pionowej osi szkicu jako kierunku dla wzorca.

#### Oś normalna szkicu 

Używa normalnej osi szkicu jako kierunku.

#### Wybierz odniesienie\... 

Umożliwia wybranie linii odniesienia, krawędzi prostej z obiektu lub linii ze szkicu, która ma być użyta jako kierunek.

#### Niestandardowa oś szkicu 

Jeżeli szkic definiujący element, który ma być użyty jako wzór, zawiera również linię *(lub linie)* konstrukcyjną, to lista rozwijana będzie zawierać jedną niestandardową oś szkicu dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna będzie oznaczona etykietą *Oś szkicu 0*.

#### Oś bazowa *(X / Y / Z)* 

Wybierz jedną ze standardowych osi odniesienia bryły *(X, Y lub Z)* jako kierunek dla wzorca.

## Ograniczenia

-   Kształty wzorców nie mogą na siebie zachodzić, z wyjątkiem szczególnego przypadku tylko dwóch wystąpień *(oryginał plus jedna kopia)*.
-   Wszystkie kształty wzorców, które nie nakładają się na podstawę oryginału, będą wykluczone. Zapewnia to, że element środowiska Projekt części zawsze składa się z pojedynczej, połączonej bryły.
-   Wzorce środowiska Projekt części nie są jeszcze tak zoptymalizowane jak ich odpowiedniki w środowisku Rysunek roboczy. Więc dla większej liczby instancji powinieneś rozważyć użycie funkcji [Rysunek roboczy: szyk](Draft_OrthoArray/pl.md) zamiast tego, w połączeniu z operacją logiczna środowiska Część. Może to obejmować duże zmiany w modelu, gdy wychodzisz ze środowisko Projekt części, co oznacza, że nie możesz po prostu kontynuować dalszych funkcji Projektu części w tej samej zawartości. Przykład jest pokazany w tym wątku [na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   \* Funkcja ta nie może być zastosowany bezpośrednio do innego wzorca, czy to biegunowego, liniowego czy lustrzanego. Do tego potrzebujesz [transformacji wielokrotnej](PartDesign_MultiTransform/pl.md).
-   W celu poznania dalszych ograniczeń, patrz funkcja: [odbicia lustrzanego](PartDesign_Mirrored/pl.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/pl
