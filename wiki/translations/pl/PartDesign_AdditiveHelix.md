---
- GuiCommand:
   Name: PartDesign AdditiveHelix
   Name/pl: Projekt Części: Addytywna helisa
   MenuLocation: Projekt Części -> Utwórz cechę przez dodanie -> Addytywna helisa
   Workbenches: PartDesign_Workbench/pl
   Version: 0.19
   SeeAlso: PartDesign_SubtractiveHelix/pl
---

# PartDesign AdditiveHelix/pl



## Opis

Narzędzie **Addytywna helisa** utworzy bryłę poprzez przeciągnięcie wybranego szkicu lub obiektu 2D po ścieżce spiralnej.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

*Profil (B) jest obracany wokół osi (A) w celu wytworzenia bryły spiralnej (C)*.



## Użycie

1.  Wybierz szkic, który ma zostać przekształcony w helisę. Alternatywnie można użyć ściany na istniejącej bryle.
2.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> '''Addytywna helisa'''**.
3.  Ustaw parametry helisy *(patrz następna sekcja)*.
4.  Sprawdź helisę w oknie widoku, aby upewnić się, że parametry nie powodują samo przecinającej się helisy.
5.  Naciśnij **OK**.



## Opcje

Podczas tworzenia helisy okno dialogowe **Parametry helisy** oferuje kilka różnych właściwości określających sposób wyciągnięcia szkicu.

![](images/PartDesign_AdditiveHelix_taskpanel.png )



### Oś

Ta opcja określa oś, wokół której szkic ma być obracany.

-   **Oś normalna do szkicu**: wybiera normalną szkicu, która przechodzi przez początek szkicu jako oś. {{Version/pl|0.20}}.
-   **Pionowa oś szkicu**: wybiera pionową oś szkicu. Jest to ustawienie domyślne dla nowych helis.
-   **Pozioma oś szkicu**: wybiera poziomą oś szkicu.
-   **Linia konstrukcyjna**: wybiera linię konstrukcyjną zawartą w szkicu używanym przez helisę. Lista rozwijana będzie zawierać pozycję dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna utworzona w szkicu będzie oznaczona jako *Linia konstrukcyjna 1*.
-   **Oś bazowa (X/Y/Z)**: wybiera oś X, Y lub Z punktu położenia odniesienia bryły.
-   **Wybierz odniesienie \...**: umożliwia wybór w oknie widoku 3D krawędzi na bryle lub [linii odniesienia](PartDesign_Line/pl.md).



### Tryb

Określa, jakie parametry zostaną użyte do zdefiniowania helisy. Dostępne opcje to:

-   **Skok - wysokość - kąt**: definicja poprzez wysokość na obrót i wysokość całkowitą.
-   **Skok - liczba obrotów - kąt**: definicja poprzez wysokość na obrót i liczbę obrotów
-   **Wysokość - liczba obrotów - kąt**: definicja poprzez wysokość całkowitą i liczbę obrotów
-   **Wysokość - liczba obrotów - przyrost** {{Version/pl|0.20}}: definicja poprzez całkowitą wysokość, liczbę zakrętów i przyrost promienia spirali. Wysokość równa zero prowadzi do ścieżki w formie spirali. Wysokość i przyrost równe zero prowadzą do ścieżki w kształcie okręgu.



### Skok

Odległość między zwojami w spirali.



### Wysokość

Wysokość spirali *(środek-środek)*.



### Obroty

Liczba zwojów w spirali. Definiowana jako wysokość / skok



### Kąt stożka 

Kąt stożka tworzącego kształt spirali Dopuszczalny zakres: \[-89°, +89°\].



### Lewostronnie

Jeśli opcja zostanie zaznaczona, kierunek tworzenia helisy ulegnie odwróceniu z domyślnego zgodnego z ruchem wskazówek zegara na przeciwny.



### Odwrócony

Jeżeli opcja ta jest zaznaczona, kierunek osi helisy jest odwrócony w stosunku do domyślnego.



### Aktualizuj widok 

Jeśli opcja ta jest zaznaczona, helisa będzie wyświetlana w oknie widoku w trakcie tworzenia i automatycznie aktualizowana przy każdej zmianie parametrów.



## Ustawienia

-   Helisa addytywna, która nie przecina bryły, będzie widoczna w podglądzie, jeśli parametr **Przybory → Edycja parameterów... → BaseApp → Preferencje → Mod → PartDesign → AdditiveHelixPreview** jest ustawiony na {{TRUE/pl}}. Domyślną wartością dla tej preferencji jest {{FALSE/pl}}. {{Version/pl|0.20}}.



## Właściwości

-    **Skok**: Odległość osiowa między dwoma zwojami.

-    **Wysokość**: Całkowita długość spirali *(bez uwzględnienia zasięgu profilu)*.

-    **Obroty**: Liczba obrotów *(nie musi być liczbą całkowitą)*.

-    **Lewostronnie**: Zobacz akapit [Lewostronnie](#Lewostronnie.md).

-    **Odwrócony**: Zobacz akapit [Odwrócony](#Odwrócony.md).

-    **Kąt**: Szybkość, z jaką promień spirali zwiększa się wzdłuż osi. Dozwolony zakres: \[-89°, +89°\].

-    **Oś odniesienia**: Oś helisy.

-    **Tryb**: Tryb wejściowy helisy *(skok-wysokość, skok-obrót, obrót-wysokość)*.

-    **Zewnętrzny**: Nieużywane *(używane w funkcji Subtraktywna helisa)*

-    **Został edytowany**: Jeśli wartość tego parametru to {{false/pl}}, narzędzie zaproponuje początkową wartość nachylenia w oparciu o obwiednię profilu, aby uniknąć samoczynnego przecięcia.

-    **Ulepsz**: Przyjmuje wartość {{true/pl}} lub {{false/pl}}. Jeśli ustawiona jest wartość true, czyści bryłę z resztkowych krawędzi pozostawionych przez elementy. Zobacz stronę [Część: Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów.

-    **Profil**: Albo szkic zawierający zamknięty kontur, albo ściana.

-    **Płaszczyzna środkowa**: Nieużywane.

-    **Aż do ściany**: Nieużywane.

-    **Zezwalaj na wiele ścian**: Nieużywane.



## Przykłady

![Przykładowa helisa wykorzystująca [krzywą złożoną](images/Sketcher_CreateBSpline/pl.md) w szkicu](PartDesign_AdditiveHelix_example_bspline.png )

![Przykładowa helisa, w której oś helisy jest normalna do płaszczyzny szkicu, co daje efekt \"skręconego wyciągnięcia\".](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/pl
