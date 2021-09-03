---
- GuiCommand:/pl
   Name:PartDesign Pad
   Name/pl:Projekt Części: Wyciągnij
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Wyciągnij
   Workbenches:[Środowisko pracy Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Kieszeń](PartDesign_Pocket/pl.md)
---

## Opis

Narzędzie **<img src="images/PartDesign_Pad.svg" width=16px> [Projekt Części: Wyciągnij przez obrót](PartDesign_Pad/pl.md)** narzędzie powoduje wyciągnięcie szkicu do bryły w kierunku normalnej do płaszczyzny szkicu. Od wersji {{VersionPlus/pl|0.17}} można również użyć ścian na bryle zamiast szkiców.

![](images/PartDesign_Pad_example.svg )

\"Szkic (A) jest pokazany po lewej stronie; wynik końcowy działania operacji wyciągnięcia (B) prezentowany jest po prawej stronie.

**Note:** {{VersionMinus/pl|0.16}} Jeśli wybrany szkic jest przyporządkowany do powierzchni czołowej istniejącej bryły lub innej funkcji projektowania części, wyciągnięcie zostanie do niej połączone.

## Jak używać 

1.  Wybierz szkic do wyciągnięcia. **Note:** W wersji {{VersionPlus/pl|0.17}} i wyższej można alternatywnie użyć powierzchni czołowej na istniejącej bryle.
2.  Naciśnij przycisk**<img src="images/PartDesign_Pad.svg" width=16px> '''Wyciągnij przez obrót'''**.
3.  Ustaw wymagane parametry dla tej operacji *(opisane w następnym akapicie [Opcje](#Opcje.md))*.
4.  Naciśnij przycisk **OK**.

## Opcje

Podczas tworzenia wyciągnięcia, widok złożony automatycznie przełącza się do panelu **Zadania**, pokazując okno dialogowe **Parametry wyciągnięcia**.

![](images/pad_parameters_cropped.png )

### Typ

Opcja **Typ** pozwala na wybranie pięciu różnych wariantów wyciągnięcia.

#### Długość

Podaj długość wyciągnięcia. Domyślnie, kształt wyciągany jest poza bryłę, ale może to zostać zmienione wybierając opcje **Odwrócony**. Wytłoczenia występują [normalnie](http://en.wikipedia.org/wiki/Surface_normal) do płaszczyzny szkicu definiującego. Za pomocą opcji **Symmetryczna do płaszczyzny** wyciągnięcie zostanie przemieszczone tak, aby płaszczyzna szkicu znajdowała się pośrodku zadanej długości. Wymiary poprzedzone znakiem minus nie są akceptowalne. Zamiast tego należy użyć opcji \"Odwrócony\".

#### Dwa wymiary 

Pozwala na podanie drugiej długości, odpowiadającej wyciągnięciu obiektu w przeciwnym kierunku. Parametr może zostać ponownie modyfikowany gdy zaznaczysz opcję **Odwrócony**.

#### Do ostatniego 

Wyciągnięcie będzie wytłaczane aż do ostatniej ściany podparcia w kierunku wytłaczania. Jeśli podparcie nie wystąpi, pojawi się komunikat o błędzie.

#### Do pierwszego 

Wyciągnięcie będzie wytłaczane aż do pierwszej ściany podparcia w kierunku wytłaczania. Jeśli podparcie nie wystąpi, pojawi się komunikat o błędzie.

#### Do powierzchni 

Wyciągnięcie będzie wytłaczane do powierzchni, którą można wybrać klikając. Jeśli podpora nie wystąpi, żaden wybór nie zostanie zaakceptowany.

### Długość 

Określa długość wyciągnięcia. Może być używanych wiele jednostek, niezależnie od ustawionych w programie preferencji użytkownika (m, cm, mm, nm, ft lub \', in lub \").

### Użyj określonego kierunku 


{{Version/pl|0.19}}

Jeśli opcja ta jest zaznaczona, kierunek wyciągnięcia nie będzie normalnym wektorem szkicu, ale wektorem podanym. Długość wyciągnięcia jest jednak ustawiona zgodnie z kierunkiem wektora normalnego.

### Długość wzdłuż wektora normalnego szkicu 

Jeśli opcja jest zaznaczona, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu, w przeciwnym razie wzdłuż kierunku niestandardowego. {{Version/pl|0.20}}

### Odsunięcie od ściany 

Odsunięcie od powierzchni, na której ma się kończyć wyciągnięcie. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Do ostatniego**, **Do pierwszego** lub *\'Do ściany*.

### Symetrycznie do płaszczyzny 

Zaznacz pole wyboru, aby rozmieścić pośrodku zadaną długość wyciągnięcia, po obu stronach płaszczyzny szkicu.

### W kierunku przeciwnym 

Opcja Reversed odwraca kierunek wyciągnięcia.

Odwraca kierunek wyciągnięcia.

## Właściwości

-    {{PropertyData/pl|Typ}}: Sposób, w jaki wyciągnięcie będzie wykonywane, patrz [Opcje](##Opcje.md).

-    {{PropertyData/pl|Długość}}: Określa długość wyciągnięcia, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Długość2}}: Druga długość w przypadku użycia opcji {{PropertyData/pl|Typ}} **Dwie długości**, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Użyj wektora własnego}}: {{Version/pl|0.19}} Jeśli jest zaznaczone, kierunek wyciągnięcia nie będzie wektorem normalnym szkicu, ale wektorem podanym, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Kierunek}}: {{Version/pl|0.19}} Wektor określający kierunek wyciągnięcia, gdy użyta jest opcja {{PropertyData/pl|Użyj wektora własnego}}.

-    {{PropertyData/pl|Wzdłuż normalnej szkicu}}: <small>(v0.20)</small>  Jeśli wartość ta to {{True}}, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu. W przeciwnym razie i jeśli użyto {{PropertyData/pl|Użyj wektora własnego}}, długość jest mierzona wzdłuż kierunku niestandardowego.

-    {{PropertyData/pl|Do powierzchni}}: Powierzchnia do której wykonane zostanie wyciągnięcie, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Przesunięcie}}: Odsunięcie od powierzchni, w której ma zakończyć się wyciągniecie. Jest to brane pod uwagę tylko wtedy, gdy używana jest opcja {{PropertyData/pl|Typ}} **Do ostatniego**, **Do pierwszego** lub **Do powierzchni**.

-    {{PropertyData/pl|Udoskonal}}: {{VersionPlus/pl|0.17}} prawda lub fałsz. Czyści resztkowe krawędzie pozostawione po operacji. Ta właściwość jest początkowo ustawiana zgodnie z ustawieniami użytkownika (znajduje się w „Preferencje → Projekt części → Ogólne → Ustawienia modelu"). Można to zmienić ręcznie. Ta właściwość zostanie zapisana w dokumencie FreeCAD.

## Ograniczenia

-   tak jak wszystkie funkcje środowiska pracy Projekt Części, wyciągnięcie tworzy bryłę. a zatem szkic musi zawierać **zamknięty** kształt. Jeśli kształt nie jest zamknięty pojawi się błąd *Nie udało się zweryfikować uszkodzonej powierzchni*. W większym szkicu może znajdować się wiele zamkniętych kształtów, pod warunkiem, że żaden z nich się nie przecina *(na przykład prostokąt z dwoma okręgami w środku)*.
-   Algorytmy używane w **Do pierwszego** i **Do ostatniego**:
    -   utwórz linię przechodzącą przez środek ciężkości szkicu,
    -   znajdź wszystkie powierzchnie podparcia przecięte przez tę linię,
    -   wybierz ścianę, na której punkt przecięcia znajduje się najbliżej/najdalej od szkicu.

:   Oznacza to, że znaleziona ściana może nie zawsze być tą, której się spodziewałeś. Jeśli natkniesz się na ten problem, zamiast tego użyj **odwrotnie do ściany** i wybierz ścianę, którą chcesz.
:   W bardzo szczególnym przypadku wytłaczania do powierzchni wklęsłych, gdzie szkic jest większy niż ta powierzchnia, wytłoczenie nie powiedzie się. Jest to nierozwiązany błąd.

-    {{VersionMinus/pl|0.16}}Nie ma funkcjonalności automatycznej optymalizacji np. łączenia sąsiednich powierzchni płaskich w jedną powierzchnię. Można to naprawić samodzielnie w Środowisku pracy Part za pomocą środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) i funkcji **<img src="images/Part_RefineShape.svg" width=16px> [Udoskonal kształt ](Part_RefineShape/pl.md)** *(która tworzy niepowiązaną, nieparametryczną bryłę)* lub za pomocą **<img src="images/OpenSCAD_RefineShapeFeature.svg" width=24px> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature/pl.md)** na podstawie środowiska pracy <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:16px;"> [penSCAD](OpenSCAD_Workbench/pl.md), który utworzy cechę parametryczną.





{{PartDesign Tools navi

}} 
