---
- GuiCommand:/pl
   Name:PartDesign Pad
   Name/pl:Projekt Części: Wyciągnij
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Wyciągnij
   Workbenches:[Środowisko pracy Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Kieszeń](PartDesign_Pocket/pl.md)
---

# PartDesign Pad/pl


</div>

## Opis

Narzędzie **Wyciągnij** umożliwia wyciągnięcie szkicu lub powierzchni bryły wzdłuż prostej ścieżki.

![](images/PartDesign_Pad_example.svg )

\"Szkic (A) jest pokazany po lewej stronie; wynik końcowy działania operacji wyciągnięcia (B) prezentowany jest po prawej stronie.

## Jak używać 

1.  Wybierz szkic lub ścianę do wyciągnięcia. {{Version/pl|0.20}} Alternatywnie można wybrać kilka szkiców lub kilka ścian.
2.  Naciśnij przycisk**<img src="images/PartDesign_Pad.svg" width=24px> '''Wyciągnij przez obrót'''**.
3.  Ustaw wymagane parametry dla tej operacji *(opisane w następnym akapicie [Opcje](#Opcje.md))*.
4.  Naciśnij przycisk **OK**.

## Opcje

Podczas tworzenia wyciągnięcia zostanie wyświetlone okno dialogowe **Parametry wyciągnięcia**. Oferuje ono następujące ustawienia:

![](images/pad_parameters_cropped.png )

### Typ

Opcja **Typ** pozwala na wybranie pięciu różnych wariantów wyciągnięcia:

#### Długość

Podaj długość wyciągnięcia. Domyślnie, kształt wyciągany jest poza bryłę, ale może to zostać zmienione wybierając opcje **Odwrócony**. Wytłoczenia występują [normalnie](http://en.wikipedia.org/wiki/Surface_normal) do płaszczyzny szkicu definiującego. Można to zmienić określając inny **Kierunek**\'. Za pomocą opcji **Symetryczna do płaszczyzny** wyciągnięcie zostanie przemieszczone tak, aby płaszczyzna szkicu znajdowała się pośrodku zadanej długości. Wymiary poprzedzone znakiem minus nie są akceptowalne. Zamiast tego należy użyć opcji \"Odwrócony\".

#### Do ostatniego 

Wyciągnięcie będzie wytłaczane aż do ostatniej ściany podparcia w kierunku wytłaczania. Jeśli podparcie nie wystąpi, pojawi się komunikat o błędzie.

#### Do pierwszego 

Wyciągnięcie będzie wytłaczane aż do pierwszej ściany podparcia w kierunku wytłaczania. Jeśli podparcie nie wystąpi, pojawi się komunikat o błędzie.

#### Do powierzchni 

Wyciągnięcie będzie wytłaczane do powierzchni modelu, którą można wybrać klikając.

#### Dwa wymiary 

Pozwala na podanie drugiej długości, odpowiadającej wyciągnięciu obiektu w przeciwnym kierunku. Parametr może zostać ponownie modyfikowany gdy zaznaczysz opcję **Odwrócony**.

### Długość 

Określa długość wyciągnięcia. Może być używanych wiele jednostek, niezależnie od ustawionych w programie preferencji użytkownika (m, cm, mm, nm, ft lub \', in lub \"). Opcja ta jest dostępna tylko wtedy, gdy opcja **Typ**\' ma wartość **Wymiar** lub **Dwa wymiary**.

### Odsunięcie od ściany 

Odsunięcie od powierzchni, na której ma się kończyć wyciągnięcie. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Do ostatniego**, **Do pierwszego** lub *\'Do ściany*.

### Kierunek

#### Kierunek / krawędź 

Można wybrać kierunek wyciągania:

-   **Ściana / Normalna szkicu** Szkic lub ściana zostanie wyciągnięty wzdłuż swojego wektora normalnego. Jeśli wybrałeś kilka szkiców lub ścian do wyciągnięcia, użyty zostanie wektor normalnej pierwszego z nich. {{Version/pl|0.20}}
-   **Wybierz odniesienie\...**. Szkic zostanie wyciągnięty wzdłuż krawędzi modelu 3D. Gdy ta metoda jest wybrana, można wybrać dowolną krawędź w modelu 3D. Stanie się ona wtedy wektorem kierunku dla wyłożenia. {{Version/pl|0.20}}
-   **Kierunek niestandardowy** Szkic jest wyciskany wzdłuż kierunku, który można określić za pomocą wartości wektorowych. {{Version/pl|0.19}}

#### Wskazanie kierunku 

Jeśli opcja jest zaznaczona, kierunek wyciągnięcia zostanie wyświetlony. W przypadku, gdy pad używa **Niestandardowego kierunku**, można go zmienić. {{Version/pl|0.20}}

#### Długość wzdłuż wektora normalnego szkicu 

Jeśli opcja jest zaznaczona, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu, w przeciwnym razie wzdłuż kierunku niestandardowego. {{Version/pl|0.20}}

### Symetrycznie do płaszczyzny 

Zaznacz pole wyboru, aby rozmieścić pośrodku zadaną długość wyciągnięcia, po obu stronach płaszczyzny szkicu.

### W kierunku przeciwnym 

Opcja Reversed odwraca kierunek wyciągnięcia.

Odwraca kierunek wyciągnięcia.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pad would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pad in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pad in the opposite extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Właściwości

-    {{PropertyData/pl|Typ}}: Sposób, w jaki wyciągnięcie będzie wykonywane, patrz [Opcje](##Opcje.md).

-    {{PropertyData/pl|Długość}}: Określa długość wyciągnięcia, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Długość2}}: Druga długość w przypadku użycia opcji {{PropertyData/pl|Typ}} **Dwie długości**, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Użyj wektora własnego}}: {{Version/pl|0.19}} Jeśli jest zaznaczone, kierunek wyciągnięcia nie będzie wektorem normalnym szkicu, ale wektorem podanym, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Kierunek}}: {{Version/pl|0.19}} Wektor określający kierunek wyciągnięcia, gdy użyta jest opcja {{PropertyData/pl|Użyj wektora własnego}}.

-    {{PropertyData/pl|Wzdłuż normalnej szkicu}}: <small>(v0.20)</small>  Jeśli wartość ta to {{True}}, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu. W przeciwnym razie i jeśli użyto {{PropertyData/pl|Użyj wektora własnego}}, długość jest mierzona wzdłuż kierunku niestandardowego.

-    {{PropertyData/pl|Do powierzchni}}: Powierzchnia do której wykonane zostanie wyciągnięcie, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Przesunięcie}}: Odsunięcie od powierzchni, w której ma zakończyć się wyciągniecie. Jest to brane pod uwagę tylko wtedy, gdy używana jest opcja {{PropertyData/pl|Typ}} **Do ostatniego**, **Do pierwszego** lub **Do powierzchni**.

-    {{PropertyData/pl|Udoskonal}}: {{True/pl}} lub {{false/pl}}. Czyści resztkowe krawędzie pozostawione po operacji. Ta właściwość jest początkowo ustawiana zgodnie z ustawieniami użytkownika *(znajduje się w **Preferencje → Projekt części → Ogólne → Ustawienia modelu**)*. Można to zmienić ręcznie. Ta właściwość zostanie zapisana w dokumencie FreeCAD.

## Ograniczenia

-   tak jak wszystkie funkcje środowiska pracy Projekt Części, wyciągnięcie tworzy bryłę. a zatem szkic musi zawierać **zamknięty** kształt. Jeśli kształt nie jest zamknięty pojawi się błąd *Nie udało się zweryfikować uszkodzonej powierzchni*. W większym szkicu może znajdować się wiele zamkniętych kształtów, pod warunkiem, że żaden z nich się nie przecina *(na przykład prostokąt z dwoma okręgami w środku)*.
-   Algorytmy używane w **Do pierwszego** i **Do ostatniego**:
    -   utwórz linię przechodzącą przez środek ciężkości szkicu,
    -   znajdź wszystkie powierzchnie podparcia przecięte przez tę linię,
    -   wybierz ścianę, na której punkt przecięcia znajduje się najbliżej / najdalej od szkicu.

:   Oznacza to, że znaleziona ściana może nie zawsze być tą, której się spodziewałeś. Jeśli natkniesz się na ten problem, zamiast tego użyj **odwrotnie do ściany** i wybierz ścianę, którą chcesz.
:   W bardzo szczególnym przypadku wytłaczania do powierzchni wklęsłych, gdzie szkic jest większy niż ta powierzchnia, wytłoczenie nie powiedzie się. Jest to nierozwiązany błąd.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/pl
