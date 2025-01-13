---
 GuiCommand:
   Name: PartDesign Pad
   Name/pl: Projekt Części: Wyciągnij
   MenuLocation: Projekt Części , Utwórz cechę przez dodanie , Wyciągnij
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Pocket/pl
---

# PartDesign Pad/pl



## Opis

Narzędzie **Wyciągnij** umożliwia wyciągnięcie szkicu lub powierzchni bryły wzdłuż prostej ścieżki.

![](images/PartDesign_Pad_example.svg )

\"Szkic (A) jest pokazany po lewej stronie; wynik końcowy działania operacji wyciągnięcia (B) prezentowany jest po prawej stronie.



## Użycie

1.  Wybierz szkic lub ścianę do wyciągnięcia.
2.  Naciśnij przycisk **<img src="images/PartDesign_Pad.svg" width=24px> [Wyciągnij](PartDesign_Pad.md)**.
3.  Ustaw wymagane parametry dla tej operacji *(opisane w następnym akapicie [Opcje](#Opcje.md))*.
4.  Naciśnij przycisk **OK**.



## Opcje

Podczas tworzenia wyciągnięcia lub po dwukrotnym kliknięciu istniejącego wyciągnięcia w oknie [Widok drzewa](Tree_view/pl.md) wyświetlany jest panel zadań **Parametry wyciągnięcia**. Oferuje on następujące ustawienia:

![](images/PartDesign_Pad_Taskpanel.png )



### Typ

Opcja **Typ** pozwala na wybranie pięciu różnych wariantów wyciągnięcia:



#### Długość

Wprowadź wartość liczbową dla **Długości** wyciągnięcia. Dzięki opcji **Symetryczny do płaszczyzny**, wyciągnięcie zostanie rozszerzonye o połowę podanej długości na obie strony względem szkicu lub powierzchni.



#### Do ostatniego 

Wyciągnięcie zostanie wykonane do ostatniej powierzchni podpory napotkanej w danym kierunku. W przypadku braku podpory pojawi się komunikat o błędzie.



#### Do pierwszego 

Wyciągnięcie zostanie wykonane do pierwszej powierzchni podpory napotkanej w danym kierunku. W przypadku braku podpory pojawi się komunikat o błędzie.



#### Do powierzchni 

Wyciągnięcie rozszerzy się do powierzchni. Naciśnij przycisk **Wybierz ścianę** i wybierz ścianę lub [płaszczyznę odniesienia](PartDesign_Plane/pl.md) z bryły.



#### Dwa wymiary 

Pozwala na podanie drugiej długości, odpowiadającej wyciągnięciu obiektu w przeciwnym kierunku. Parametr może zostać ponownie modyfikowany gdy zaznaczysz opcję **Odwrócony**.



#### Do kształtu 


{{Version/pl|1.0}}

: Wyciągnięcie będzie utworzone aż do wskazanego kształtu. Opcjonalnie, wciśnij przycisk **Wybierz kształt** i wskaż kształt. Pozostaw pole **Zaznacz wszystkie ściany** włączone lub wyłącz je, wciśnij przycisk **Wybierz** i wskaż ściany, do których ma być utworzone wyciągnięcie.



### Odsunięcie od ściany 

Odsunięcie od powierzchni, na której ma się kończyć wyciągnięcie. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Do ostatniego**, **Do pierwszego** lub **Do ściany**.



### Długość 

Określa długość wyciągnięcia. Opcja ta jest dostępna tylko wtedy, gdy opcja **Typ** ma wartość **Wymiar** lub **Dwa wymiary**. Długość jest mierzona wzdłuż wektora kierunku lub wzdłuż normalnej do szkicu lub powierzchni. Wartości ujemne nie są możliwe. Zamiast tego użyj opcji **Odwrócony**.



### Druga długość 

Określa długość wyciągnięcia w przeciwnym kierunku wyciskania. Opcja ta jest dostępna tylko gdy **Typ** wybrano **Dwa wymiary**.



### Symetrycznie do płaszczyzny 

Zaznacz pole wyboru, aby rozmieścić pośrodku zadaną długość wyciągnięcia, po obu stronach płaszczyzny szkicu lub ściany. Ta opcja jest dostępna tylko wtedy, gdy jako **Typ** wybrano **Wymiar**.



### W kierunku przeciwnym 

Opcja Reversed odwraca kierunek wyciągnięcia.

Odwraca kierunek wyciągnięcia.



### Kierunek



#### Kierunek / krawędź 

Można wybrać kierunek wyciągania:

-   **Normalna szkicu** lub **Normalna ściany:** Szkic lub powierzchnia jest wyciągana w kierunku swojej normalnej. Jeśli wybrano kilka szkiców lub powierzchni do wyciągnięcia, użyta zostanie normalna pierwszego z nich.
-   **Wybierz odniesienie \...:** Szkic lub powierzchnia jest wyciągana w kierunku prostej krawędzi lub [linii odniesienia](PartDesign_Line/pl.md) wybranej z bryły.
-   **Kierunek niestandardowy:** Szkic lub powierzchnia jest wyciągana w kierunku określonego wektora.



#### Wskazanie kierunku 

Jeśli opcja jest zaznaczona, kierunek wyciągnięcia zostanie wyświetlony. W przypadku, gdy pad używa **Niestandardowego kierunku**, można go zmienić. {{Version/pl|0.20}}



#### Długość wzdłuż wektora normalnego szkicu 

Jeśli opcja jest zaznaczona, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu lub ściany, w przeciwnym razie wzdłuż kierunku niestandardowego. {{Version/pl|0.20}}



### Kąt zwężenia 

Zwęża wyciągnięcie w kierunku wytłaczania o podany kąt. Dodatni kąt oznacza, że zewnętrzna krawędź bryły staje się szersza. Należy pamiętać, że konstrukcje wewnętrzne otrzymują przeciwny kąt zwężenia. Ma to na celu ułatwienie projektowania form i elementów formowanych. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Wymiar** lub **Dwa wymiary**.



### Drugi kąt zwężenia 

Pochyla wyciągnięcie w przeciwnym kierunku wyciągania o podany kąt. Patrz: **Kąt pochylenia**. Ta opcja jest dostępna tylko w przypadku gdy **Typ** to **Dwa wymiary**.



## Właściwości



### Dane


{{TitleProperty|Wyciągnięcie}}

-    {{PropertyData/pl|Typ|Enumeration}}: Definiuje sposób, w jaki wyciągnięcie będzie wykonywane, patrz [Opcje](##Opcje.md).

-    {{PropertyData/pl|Długość|Length}}: Określa długość wyciągnięcia, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Długość2|Length}}: Druga długość w przypadku użycia opcji {{PropertyData/pl|Typ}} **Dwie długości**, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Użyj wektora własnego|Bool}}: Jeśli jest zaznaczone, kierunek wyciągnięcia nie będzie wektorem normalnym szkicu, ale wektorem podanym, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Kierunek|Vector}}: Wektor określający kierunek wyciągnięcia, gdy użyta jest opcja {{PropertyData/pl|Użyj wektora własnego}}.

-    **Oś odniesienia|LinkSub**
    

-    {{PropertyData/pl|Wzdłuż normalnej szkicu|Bool}}: Jeśli wartość ta to {{True}}, długość wyciągnięcia jest mierzona wzdłuż kierunku wektora normalnego szkicu. W przeciwnym razie i jeśli użyto {{PropertyData/pl|Użyj wektora własnego}}, długość jest mierzona wzdłuż kierunku niestandardowego. {{Version/pl|0.20}}

-    {{PropertyData/pl|Do powierzchni|LinkSub}}: Powierzchnia do której wykonane zostanie wyciągnięcie, patrz [Opcje](#Opcje.md).

-    {{PropertyData/pl|Odsunięcie|Length}}: Odsunięcie od powierzchni, w której ma zakończyć się wyciągniecie. Jest to brane pod uwagę tylko wtedy, gdy używana jest opcja {{PropertyData/pl|Typ}} **Do ostatniego**, **Do pierwszego** lub **Do powierzchni**.

-    **Kąt nachylenia|Angle**
    

-    **Kąt nachylenia2|Angle**
    


{{TitleProperty|Projekt Części}}

-    {{PropertyData/pl|Udoskonal}}: {{True/pl}} lub {{false/pl}}. Czyści resztkowe krawędzie pozostawione po operacji. Ta właściwość jest początkowo ustawiana zgodnie z ustawieniami użytkownika *(znajduje się w **Preferencje → Projekt Części → Ogólne → Ustawienia modelu**)*.


{{TitleProperty|Szkic bazowy}}

-    **Profil|LinkSub**
    

-    **Płaszczyzna pośrednia|Bool**
    

-    **Odwrócony|Bool**
    

-    **Zezwalaj na wiele ścian|Bool**
    



## Ograniczenia

-   Podobnie jak wszystkie funkcje projektowania części, funkcja wyciągnięcia tworzy bryłę, dlatego szkic musi zawierać profil zamknięty, w przeciwnym razie operacja zakończy się niepowodzeniem z błędem \"Nie udało się zweryfikować uszkodzonej powierzchni\".
-   Szkice zawierające [krzywe złozone](B-Splines/pl.md) często nie mogą być prawidłowo zwężane. Jest to ograniczenie jądra [OpenCASCADE](OpenCASCADE/pl.md), z którego korzysta FreeCAD.
-   W przypadku większych kątów zwężanie nie powiedzie się, jeśli powierzchnia końcowa będzie miała mniej krawędzi niż powierzchnia początkowa / szkic.
-   Algorytmy używane w **Do pierwszego** i **Do ostatniego**:
    -   utwórz linię przechodzącą przez środek ciężkości szkicu,
    -   znajdź wszystkie powierzchnie podparcia przecięte przez tę linię,
    -   wybierz ścianę, na której punkt przecięcia znajduje się najbliżej / najdalej od szkicu.

:   Oznacza to, że znaleziona ściana może nie zawsze być tą, której się spodziewałeś. Jeśli natkniesz się na ten problem, zamiast tego użyj **odwrotnie do ściany** i wybierz ścianę, którą chcesz.
:   W bardzo szczególnym przypadku wytłaczania do powierzchni wklęsłych, gdzie szkic jest większy niż ta powierzchnia, wytłoczenie nie powiedzie się. Jest to nierozwiązany błąd.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/pl
