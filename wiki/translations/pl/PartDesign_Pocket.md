---
- GuiCommand:
   Name:PartDesign Pocket
   Name/pl:Projekt Części: Kiezeń
   MenuLocation:Projekt części → Utwórz cechę przez odjęcie → Kieszeń
   Workbenches:[Projekt części](PartDesign_Workbench/pl.md)
   SeeAlso:[Wyciągnięcie](PartDesign_Pad/pl.md)
---

# PartDesign Pocket/pl



## Opis

Narzędzie **Kieszeń** wycina bryły poprzez wyciągnięcie szkicu lub ściany bryły wzdłuż prostej ścieżki.

![](images/PartDesign_Pocket_example.svg ) *Profil szkicu (A) został odwzorowany na górnej ścianie bryły bazowej (B). Wynik po przebiciu kieszeni po prawej stronie.*



## Użycie

1.  Wybierz szkic lub ścianę do wykonania kieszeni. {{Version/pl|0.20}}: Alternatywnie można wybrać kilka szkiców lub ścian.
2.  Naciśnij przycisk **<img src="images/PartDesign_Pocket.svg" width=16px> '''Kieszeń'''**.
3.  Ustaw parametry kieszeni, patrz [Opcje](#Opcje.md) poniżej.
4.  Kliknij **OK**.

Podczas wybierania pojedynczego szkicu może on mieć wiele profili zamkniętych wewnątrz większego, na przykład prostokąt z dwoma okręgami w środku. Profile te nie mogą się jednak przecinać. {{Version/pl|0.20}}



## Opcje

Podczas tworzenia kieszeni zostanie wyświetlone okno dialogowe **Parametry kieszeni**. Oferuje ono następujące ustawienia:

![](images/pocket_parameters_cropped.png )



### Typ

Opcja Typ oferuje pięć różnych sposobów określania długości, na jaką kieszeń będzie wytłaczana:



#### Wymiar

Wprowadź wartość liczbową długości kieszeni. Domyślnym kierunkiem wyciągnięcia jest podpora, ale można go zmienić, zaznaczając opcję *Odwrócony*. Wyciągnięcia są domyślnie [normalne](http://en.wikipedia.org/wiki/Surface_normal) do definiującej płaszczyzny szkicu. Można to zmienić, określając inny **Kierunek** {{Version/pl|0.20}}. Z opcją **Symetrycznie do płaszczyzny** kieszeń będzie rozciągać się na połowę podanej długości po obu stronach płaszczyzny. Wymiary ujemne nie są możliwe. Zamiast tego należy użyć opcji **Odwrócony**.



#### Przez wszystkie 

Kieszeń będzie przechodzić przez wszystkie obiekty w kierunku wytłaczania. Po wybraniu opcji **Symetrycznie do płaszczyzny**, kieszeń będzie przecinać wszystkie materiały w obu kierunkach.
**Uwaga:** Z przyczyn technicznych, **Przez wszystkie\'\' jest w rzeczywistości kieszenią o głębokości 10 m\' Jeżeli potrzebujesz głębszych kieszeni, użyj opcji**Wymiar\'\'\'.



#### Do pierwszego 

Kieszeń będzie rozciągać się aż do pierwszej ściany podpory w kierunku wytłaczania. Innymi słowy, będzie przecinać cały materiał aż do osiągnięcia pustej przestrzeni.



#### Do ściany 

Kieszeń zostanie wycięta aż do ściany w modelu, którą można wybrać klikając na nią.



#### Dwa wymiary 

Umożliwia wprowadzenie drugiej długości, w której kieszeń powinna rozciągać się w przeciwnym kierunku *(do podpory)*. Kierunki można przełączać, zaznaczając opcję **Odwrócony**.



### Długość

Określa głębokość kieszeni. Może być używanych wiele jednostek, niezależnie od ustawionych w programie preferencji użytkownika *(m, cm, mm, nm, ft lub \', in lub \")*. Opcja ta jest dostępna tylko wtedy, gdy opcja **Typ** ma wartość **Wymiar** lub **Dwa wymiary**.



### Odsunięcie od ściany 

Odsunięcie od powierzchni, na której ma się kończyć kieszeń. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Przez wszystkie**, **Do pierwszego** lub **Do ściany**.



### Kierunek


{{Version/pl|0.20}}



#### Kierunek / krawędź 

Można wybrać kierunek wyciągania:

-   **Wektor normalny ściany** Szkic lub ściana zostanie wyciągnięty wzdłuż swojego wektora normalnego. Jeśli wybrałeś kilka szkiców lub ścian do wyciągnięcia, użyty zostanie wektor normalnej pierwszego z nich. {{Version/pl|0.20}}
-   **Wybierz odniesienie \...** Szkic zostanie wyciągnięty wzdłuż krawędzi modelu 3D. Gdy ta metoda jest wybrana, można wybrać dowolną krawędź w modelu 3D. Stanie się ona wtedy wektorem kierunku dla wytłoczenia. {{Version/pl|0.20}}
-   **Kierunek niestandardowy** Szkic jest wyciskany wzdłuż kierunku, który można określić za pomocą wartości wektorowych.



#### Pokaż kierunek 

Jeśli opcja jest zaznaczona, kierunek kieszeni zostanie wyświetlony. W przypadku, gdy kieszeń używa **Niestandardowego kierunku**, można go zmienić.



#### Długość wzdłuż wektora normalnego szkicu 

Jeśli opcja jest zaznaczona, długość kieszeni jest mierzona wzdłuż kierunku wektora normalnego szkicu, w przeciwnym razie wzdłuż kierunku niestandardowego.



### Symetrycznie do płaszczyzny 

Zaznacz pole wyboru, aby rozmieścić pośrodku zadaną długość wyciągnięcia, po obu stronach płaszczyzny szkicu.



### Odwrócony

Odwraca kierunek wykonania kieszeni.



### Kąt zwężenia 


{{Version/pl|0.20}}

Zwęża kieszeń w kierunku wytłaczania o podany kąt. Dodatni kąt oznacza, że zewnętrzna krawędź bryły staje się szersza. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Wymiar** lub **Dwa wymiary**. Należy pamiętać, że konstrukcje wewnętrzne otrzymują przeciwny kąt zwężenia. Ma to na celu ułatwienie projektowania form i elementów formowanych.

Ograniczenia:

-   Szkice zawierające [krzywe złożone](B-Splines/pl.md) często nie mogą być poprawnie zwężone. Jest to ograniczenie jądra [OpenCASCADE](OpenCASCADE/pl.md), którego używa FreeCAD.
-   Dla większych kątów zwężanie nie powiedzie się, jeżeli końcowa powierzchnia kieszeni będzie miała mniej krawędzi niż powierzchnia / szkic początkowy.



### Druga długość 

Określa długość kieszeni w przeciwnym kierunku wycinania. Można użyć wielu jednostek niezależnie od preferencji użytkownika dotyczących jednostek *(m, cm, mm, nm, ft lub \', in lub \")*. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Dwa wymiary**.



### Kąt drugiego zwężenia 


{{Version/pl|0.20}}

Zwęża kieszeń w przeciwnym kierunku wycinania o podany kąt. Dodatni kąt oznacza, że zewnętrzna powierzchnia bryły staje się szersza. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Dwa wymiary**. Należy pamiętać, że struktury wewnętrzne otrzymują przeciwny kąt zwężenia. Robi się to w celu ułatwienia projektowania form i wyprasek.



## Właściwości

-    **Typ**: Rodzaje, w jaki sposób kieszeń będzie wytłaczana, patrz sekcja [Opcje](#Opcje.md).

-    **Długość**: Określa długość kieszeni, patrz [Opcje](#Opcje.md).

-    **Długość2**: Druga długość kieszeni w przypadku, gdy **Typ** ma wartość **Dwa wymiary**, patrz [Opcje](#Opcje.md).

-    **Kierunek niestandardowy**: {{Version/pl|0.20}}. Jeśli opcja jest zaznaczona, kierunek kieszeni nie będzie wektorem normalnym szkicu, ale wektorem wskazanym, patrz sekcja [Opcje](#Opcje.md).

-    **Kierunek**: {{Version/pl|0.20}}. Wektor kierunku kieszeni, jeśli użyto **Kierunek niestandardowy**.

-    **Wzdłuż normalnej szkicu**: {{Version/pl|0.20}}. Jeśli wartość ta zostanie ustawiona na {{true/pl}}, długość kieszeni będzie mierzona wzdłuż normalnej szkicu. W przeciwnym razie i jeśli użyto **Kierunek niestandardowy**, jest ona mierzona wzdłuż niestandardowego kierunku.

-    **Do ściany**: Ściana, do której kieszeń będzie wytłaczana, patrz [Opcje](#Opcje.md).

-    **Ulepsz**: przyjmuje wartości {{true/pl}} lub {{false/pl}}. Czyści pozostałe krawędzie po operacji. Ta właściwość jest początkowo ustawiana zgodnie z ustawieniami użytkownika *(w **Preferencje → Część / Projekt Części → Ogólne → Ustawienia modelu**)*. Można ją potem zmienić samodzielnie. Właściwość ta zostanie zapisana wraz z dokumentem FreeCAD.



## Ograniczenia

-   Używaj typu **Wymiar** lub **Przez wszystkie**, gdy tylko jest to możliwe, ponieważ inne typy czasami sprawiają problemy, gdy są modelowane.
-   W przeciwnym razie cecha kieszeni ma takie same [ograniczenia](PartDesign_Pad/pl#Ograniczenia.md) jak cecha Wyciągnięcie.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/pl
