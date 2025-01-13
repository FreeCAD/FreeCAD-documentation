---
 GuiCommand:
   Name: PartDesign Pocket
   Name/pl: Projekt Części: Kiezeń
   MenuLocation: Projekt Części , Utwórz cechę przez odjęcie , Kieszeń
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Pad/pl
---

# PartDesign Pocket/pl



## Opis

Narzędzie **Kieszeń** wycina bryły poprzez wyciągnięcie szkicu lub ściany bryły wzdłuż prostej ścieżki.

![](images/PartDesign_Pocket_example.svg ) *Profil szkicu (A) został odwzorowany na górnej ścianie bryły bazowej (B). Wynik po przebiciu kieszeni po prawej stronie.*



## Użycie

1.  Wybierz pojedynczy szkic lub jedną lub więcej ścian.
2.  Naciśnij przycisk **<img src="images/PartDesign_Pocket.svg" width=16px> '''Kieszeń'''**.
3.  Ustaw parametry kieszeni, patrz [Opcje](#Opcje.md) poniżej.
4.  Kliknij **OK**.



## Opcje

Podczas tworzenia kieszeni lub po dwukrotnym kliknięciu istniejącej kieszeni w oknie [Widok drzewa](Tree_view/pl.md), wyświetlany jest panel zadań **Parametry kieszeni**. Zawiera on następujące ustawienia:

![](images/PartDesign_Pocket_Taskpanel.png )



### Typ

Opcja Typ oferuje pięć różnych sposobów określania długości, na jaką kieszeń będzie wytłaczana:



#### Wymiar

Wprowadź wartość liczbową dla **Długości** kieszeni. Dzięki opcji **Symetryczny do płaszczyzny**, kieszeń zostanie rozszerzony o połowę podanej długości na obie strony względem szkicu lub powierzchni.



#### Przez wszystkie 

Kieszeń będzie rozciągać się do ostatniej powierzchni podpory, którą napotka w swoim kierunku. Z opcją **Symetryczna do płaszczyzny** kieszeń przetnie cały materiał w obu kierunkach. Należy pamiętać, że ze względów technicznych opcja **Przez wszystko** jest w rzeczywistości kieszenią o głębokości 10 metrów. Jeśli potrzebujesz głębszych kieszeni, użyj typu **Wymiar**.



#### Do pierwszego 

Kieszeń będzie sięgać do pierwszej powierzchni podpory, którą napotka w swoim kierunku.



#### Do ściany 

Kieszeń rozszerzy się do powierzchni. Naciśnij przycisk **Wybierz ścianę** i wybierz ścianę lub [płaszczyznę odniesienia](PartDesign_Plane/pl.md) z bryły.



#### Dwa wymiary 

Pozwala to na wprowadzenie drugiej długości, w której kieszeń powinna rozciągać się w przeciwnym kierunku. Parametr może zostać ponownie modyfikowany gdy zaznaczysz opcję **Odwrócony**.



#### Do kształtu 


{{Version/pl|1.0}}

: Kieszeń będzie utworzona aż do wskazanego kształtu. Opcjonalnie, wciśnij przycisk **Wybierz kształt** i wskaż kształt. Pozostaw pole **Zaznacz wszystkie ściany** włączone lub wyłącz je, wciśnij przycisk **Wybierz** i wskaż ściany, do których ma być utworzona kieszeń.



### Odsunięcie od ściany 

Odsunięcie od powierzchni, na której ma się kończyć kieszeń. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Przez wszystkie**, **Do pierwszego** lub **Do ściany**.



### Długość

Określa długość kieszeni. Opcja ta jest dostępna tylko wtedy, gdy opcja **Typ** ma wartość **Wymiar** lub **Dwa wymiary**. Długość jest mierzona wzdłuż wektora kierunku lub wzdłuż normalnej do szkicu lub powierzchni. Wartości ujemne nie są możliwe. Zamiast tego użyj opcji **Odwrócony**.



### Druga długość 

Określa długość kieszeni w przeciwnym kierunku wycinania. Można użyć wielu jednostek niezależnie od preferencji użytkownika dotyczących jednostek *(m, cm, mm, nm, ft lub \', in lub \")*. Opcja ta jest dostępna tylko gdy **Typ** jest ustawiony na **Dwa wymiary**.



### Symetrycznie do płaszczyzny 

Zaznacz tę opcję, aby rozszerzyć kieszeń o połowę podanego kąta po obu stronach szkicu lub powierzchni, jeśli **Typ** to **Wymiar**, lub **Przez wszystkie**, jeśli taki jest **Typ**.



### Odwrócony

Odwraca kierunek wykonania kieszeni.



### Kierunek



#### Kierunek / krawędź 

Można wybrać kierunek wyciągania:

-   **Normalna szkicu** lub **Normalna ściany:** Szkic lub powierzchnia jest wyciągana w kierunku swojej normalnej. Jeśli wybrano kilka szkiców lub powierzchni do wyciągnięcia, użyta zostanie normalna pierwszego z nich.
-   **Wybierz odniesienie \...:** Szkic lub powierzchnia jest wyciągana w kierunku prostej krawędzi lub [linii odniesienia](PartDesign_Line/pl.md) wybranej z bryły.
-   **Kierunek niestandardowy:** Szkic lub powierzchnia jest wyciągana w kierunku określonego wektora.



#### Pokaż kierunek 

Jeśli opcja jest zaznaczona, kierunek kieszeni zostanie wyświetlony. W przypadku, gdy kieszeń używa **Niestandardowego kierunku**, można go zmienić.



#### Długość wzdłuż wektora normalnego szkicu 

Jeśli opcja jest zaznaczona, długość kieszeni jest mierzona wzdłuż kierunku wektora normalnego szkicu lub ściany, w przeciwnym razie wzdłuż kierunku niestandardowego.



### Kąt zwężenia 

Przechyla kieszeń w kierunku wytłaczania o podany kąt. Kąt dodatni oznacza, że zewnętrzny brzeg kieszeni się rozszerza. Należy zauważyć, że wewnętrzne struktury otrzymują przeciwny kąt przechylenia. Ma to ułatwić projektowanie form i odlewów. Ta opcja jest dostępna tylko wtedy, gdy **Typ** jest ustawiony na **Wymiar** lub **Dwa wymiary**.



### Kąt drugiego zwężenia 

Pochyla kieszeń w przeciwnym kierunku wyciągania o podany kąt. Patrz: **Kąt pochylenia**. Ta opcja jest dostępna tylko w przypadku gdy **Typ** to **Dwa wymiary**.



## Właściwości



### Dane


{{TitleProperty|Projekt Części}}

-    {{PropertyData/pl|Udoskonal}}: {{True/pl}} lub {{false/pl}}. Czyści resztkowe krawędzie pozostawione po operacji. Ta właściwość jest początkowo ustawiana zgodnie z ustawieniami użytkownika *(znajduje się w **Preferencje → Projekt Części → Ogólne → Ustawienia modelu**)*.


{{TitleProperty|Kieszeń}}

-    **Typ|Enumeration**: Określa w jaki sposób kieszeń będzie wytłaczana, patrz sekcja [Opcje](#Opcje.md).

-    **Długość|Length**: Określa długość kieszeni, patrz [Opcje](#Opcje.md).

-    **Długość2|Length**: Druga długość kieszeni w przypadku, gdy **Typ** ma wartość **Dwa wymiary**, patrz [Opcje](#Opcje.md).

-    **Kierunek niestandardowy|Bool**: {{Version/pl|0.20}}. Jeśli opcja jest zaznaczona, kierunek kieszeni nie będzie wektorem normalnym szkicu, ale wektorem wskazanym, patrz sekcja [Opcje](#Opcje.md).

-    **Kierunek|Vector**: {{Version/pl|0.20}}. Wektor kierunku kieszeni, jeśli użyto **Kierunek niestandardowy**.

-    **Oś odniesienia|LinkSub**
    

-    **Wzdłuż normalnej szkicu|Bool**: {{Version/pl|0.20}}. Jeśli wartość ta zostanie ustawiona na {{true/pl}}, długość kieszeni będzie mierzona wzdłuż normalnej szkicu. W przeciwnym razie i jeśli użyto **Kierunek niestandardowy**, jest ona mierzona wzdłuż niestandardowego kierunku.

-    **Do ściany|LinkSub**: Ściana, do której kieszeń będzie wytłaczana, patrz [Opcje](#Opcje.md).

-    **Odsunięcie|Length**
    

-    **Kąt nachylenia|Angle**
    

-    **Kąt nachylenia2|Angle**
    


{{TitleProperty|Szkic bazowy}}

-    **Profil|LinkSub**
    

-    **Płaszczyzna pośrednia|Bool**
    

-    **Odwrócony|Bool**
    

-    **Zezwalaj na wiele ścian|Bool**
    



## Ograniczenia

-   Używaj typu **Wymiar** lub **Przez wszystkie**, gdy tylko jest to możliwe, ponieważ inne typy czasami sprawiają problemy, gdy są modelowane.
-   W przeciwnym razie cecha kieszeni ma takie same [ograniczenia](PartDesign_Pad/pl#Ograniczenia.md) jak cecha Wyciągnięcie.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/pl
