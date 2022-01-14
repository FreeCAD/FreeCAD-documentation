---
- GuiCommand:/pl
   Name:PartDesign Hole
   Name/pl:Projekt części: otwór
   MenuLocation:Projekt części → Utwórz cechę subtraktywną → Otwór
   Workbenches:[Projekt części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Kieszeń](PartDesign_Pocket/pl.md)
---

# PartDesign Hole/pl

## Opis

Funkcja **Otwór** tworzy jeden lub więcej otworów z okręgów wybranego szkicu. Jeśli są obecne łuki, muszą one być częścią zamkniętych konturów. Wszystkie elementy nie będące łukami/kolami są ignorowane, ale nadal muszą tworzyć zamknięte kontury. Można ustawić wiele parametrów, takich jak gwintowanie i rozmiar, pasowanie, typ otworu *(pogłębienie stożkowe, pogłębienie walcowe, lub bez pogłębiania)* i inne.

<img alt="" src=images/Countersunk_and_counterbored_holes_cross-section1.png  style="width:600px;">



*Otwory pogłębione stożkowo ''(z lewej strony)'' i otwory pogłębione walcowo ''(z prawej strony)'' przekrój podłużny.*

## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_Hole.svg" width=16px>. '''Otwór'''**.
2.  Jeśli zostanie wykryty istniejący, nieużywany szkic, zostanie on automatycznie zastosowany. Jeśli zostanie znalezionych więcej niż jeden szkic, zostanie wyświetlony panel **Wybierz rysunek** umożliwiający dokonanie wyboru. Alternatywnie można wybrać szkic przed uruchomieniem polecenia Otwór.
3.  Zdefiniuj parametry otworu, które są opisane w sekcji [Opcje](#Opcje.md).
4.  Naciśnij przycisk **OK**.

## Opcje

W zależności od tego, jakiego wyboru dokonamy, niektóre pola będą aktywne lub pozostaną nieaktywne.

![](images/PartDesign_Hole_parameters.png )

### Gwinty i rozmiar 

-   **Profil**: jeśli opcja jest ustawiona na *Brak*, nie definiuje się informacji o gwintowaniu. Profile gwintów [ISO](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) i [UTS](https://en.wikipedia.org/wiki/Unified_Thread_Standard) umożliwiają włączenie pola *Rozmiar*.
-   **Gwint**: jeżeli opcja jest zaznaczona, dane gwintu zostaną dodane do cechy *otwór* i zostanie użyta mniejsza średnica otworu. Jeżeli opcja nie jest zaznaczona, otwór jest traktowany jako niegwintowany i wybierana jest nominalna średnica główna ze zdefiniowanym *prześwitem*.
-   **Modeluj gwint**: jeżeli opcja jest zaznaczona, to zostanie wymodelowany autentyczny gwint. Zużywa to dużo mocy obliczeniowej i zazwyczaj nie jest używane w modelach, z wyjątkiem celów wyświetlania lub czasami dla wydruków 3D. Jeśli opcja zostanie użyta, zalecane jest sprawdzenie jej jako jednej z ostatnich czynności wykonywanych w modelu, ponieważ znacznie wzrasta ilość ponownych obliczeń. *({{Version/pl|0.20}})*
-   **Kierunek**: ustawia kierunek gwintu *(prawoskrętny lub lewoskrętny)*, jeżeli wybrano opcję *Gwint*.
-   **Rozmiar**: ustawia rozmiar gwintu. Wymaga *profilu* ustawionego na jeden z profili [ISO](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) lub [UTS](https://en.wikipedia.org/wiki/Unified_Thread_Standard).
-   **Prześwit**: ustawia standardową, bliską lub szeroką średnicę pasowania. Dla gwintów ISO średnice są zgodne z normą ISO 273, dla UTS są obliczane na zasadzie reguły z grubsza, ponieważ nie ma normy, która by je określała. Dostępne tylko dla otworów niegwintowanych.
-   **Klasa**: definiuje klasę tolerancji.
-   **Średnica**: definiuje średnicę otworu, jeżeli *profil* jest ustawiony na *Brak*.
-   **Głębokość**: głębokość otworu od płaszczyzny szkicu. Opcja **Wymiar** włącza pole do wpisania wartości. *Przez wszystkie* spowoduje wycięcie otworu przez cały korpus. **Uwaga:** Z powodów technicznych opcja *Przez wszystkie* to w rzeczywistości otwór o głębokości 10 metrów. Jeśli potrzebujesz głębszych otworów, użyj opcji *Wymiar*.

### Wycięcie otworu 

-   **Typ**: ustawia typ wycięcia otworu: *Brak* oznacza brak wycięcia, inne typy to różne normy dla śrub *({{Version/pl|0.19}})* oraz dwa typy ogólne *pogłębienie stożkowe* i *pogłębienie walcowe*.
-   **Średnica**: ustawia górną średnicę *(na płaszczyźnie szkicu)* dla wyciętego otworu.
-   **Głębokość**: głębokość wycięcia otworu, mierzona od płaszczyzny szkicu.
-   **Kąt pogłębiania stożkowego**: kąt stożkowego wycięcia otworu. Dotyczy tylko pogłębiania stożkowego.

### Punkt wiercenia 

-   **Typ**: definiuje zakończenie otworu, jeżeli *Głębokość* jest ustawiona na *Wymiar*,
    -   **Płaski** tworzy płaskie dno,
    -   **Kątowe** tworzy stożkowy punkt. Jego opcja **Uwzględnia głębokość** *({{Version/pl|0.19}})* odejmie wysokość stożka od *Wymiaru*. Zatem jeśli np. *Wymiar* wynosi 7.00 i opcja ta nie jest użyta, część cylindryczna otworu będzie miała wartość 7.00, a głębokość niezbędna dla części stożkowej zostanie dodana do głębokości otworu. Jeśli opcja ta zostanie użyta, całkowita głębokość otworu wraz z punktem stożkowym będzie wynosić 7.00.

### Różności

-   **Stożkowy**: ustawia kąt stożka otworu. Wartość jest obliczana na podstawie płaszczyzny normalnej szkicu. 90° ustawia prosty otwór. Wartość poniżej 90 generuje mniejszy promień otworu u dołu, wartość powyżej 90 zwiększa promień otworu u dołu.
-   **Odwrócony**: odwraca kierunek wyciskania otworu. Domyślnym kierunkiem jest kierunek odwzorowania szkicu otworu, na jego punkt zaczepienia.

## Właściwości

Duża część właściwości Danych jest taka sama jak te prezentowane w sekcji [Opcje](#Opcje.md).

-    **Etykieta**: nazwa nadana obiektowi, ta nazwa może być zmieniona dla wygody.

-    **Ulepsz **: przyjmuje wartość {{true}} lub {{false}}. Jeśli jest ustawiona na {{true}}, oczyszcza bryłę z resztek krawędzi pozostawionych przez cechy. Zobacz stronę **<img src="images/Part_RefineShape.svg" width=16px> [Część: udoskonalanie kształtu](Part_RefineShape.md)** aby uzyskać więcej szczegółów.

## Ograniczenia

-   Wybrany szkic musi zawierać jeden lub więcej okręgów. Promień okręgu*(ów)* na szkicu nie jest brany pod uwagę. Wygenerowane otwory będą identyczne, nawet jeśli okręgi w szkicu mają różne promienie.
-   Domyślnie element otworu jest wysuwany poniżej płaszczyzny szkicu. Jeśli bryła leży na płaszczyźnie **XY**, a szkic otworu jest dołączony do płaszczyzny **XY**, to będzie on próbował wytłaczać się z dala od bryły i pozornie nie da żadnego rezultatu. W takim przypadku należy ustawić opcję *Odwrócony*; alternatywnie szkic można zmapować do dolnej powierzchni bryły.
-   Modelowanie gwintu działa tylko wtedy, gdy nie jest ustawiona opcja Odwrócony.

## Definicje typów cięcia 

Typy cięcia *(typy śrub)* są zdefiniowane od wersji 0.19 w plikach [json](https://de.wikipedia.org/wiki/JavaScript_Object_Notation). Istnieje zestaw plików dystrybuowanych z programem FreeCAD, ale użytkownicy mogą tworzyć własne definicje. Pliki są wyszukiwane w <UserAppDataDir>/PartDesign/Hole. Folder `UserAppDataDir` można odnaleźć, wpisując ciąg `App.getUserAppDataDir()` w [konsoli Python](Python_console/pl.md).

Plik ten powinien zawierać:

-   **nazwa**: Nazwa definicji. Musi być ona unikalna, ponieważ będzie używana jako identyfikator w interfejsie użytkownika FreeCAD, oraz jako wewnętrzny indeks.
-   **typ\_cięcia**: Albo `pogłębienie stożkowe` lub `pogłębienie walcowe`.
-   **typ\_gwintu**: Albo ` metryczny ` albo ` metryczny drobnozwojowy `..
-   **kąt**: Kąt pogłębiania (nie jest konieczny dla pogłębienia walcoweego).
-   **dane**: Lista rozmiarowa, obejmująca:
    -   **gwint**: Nazwa gwintu używana w programie FreeCAD.
    -   **średnicę**: Średnica cięcia.
    -   **głębokość**: Głębokość pogłębienia *(nie jest konieczna w przypadku pogłębiania stożkowego)*.

Przykład: {{Code|lang=json|code=
{
    "name": "DIN 7984",
    "cut_type": "counterbore",
    "thread_type": "metric",
    "data": [
        { "thread": "M2",   "diameter":  4.3, "depth":  1.6 },
        { "thread": "M2.5", "diameter":  5.0, "depth":  2.0 },
        …
    ]
}
}}





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Hole/pl
