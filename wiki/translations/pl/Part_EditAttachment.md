---
- GuiCommand:
   Name: Part EditAttachment
   Name/pl: Część: Dołączenie
   MenuLocation: Część -> Dołączenie ...
   Workbenches: Part_Workbench/pl, PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: Placement/pl, Basic_Attachment_Tutorial/pl, Part_Part2DObject/pl
---

# Part EditAttachment/pl



## Opis

**Dołączenie** jest narzędziem do dołączania obiektu do innego. Dołączony obiekt jest powiązany z drugim obiektem, co oznacza, że jeśli położenie tego drugiego zostanie zmienione, dołączony obiekt zostanie zaktualizowany do nowej pozycji.



## Użycie

1.  Wybierz obiekt, który ma zostać dołączony.
2.  Przejdź do menu *Część → Dołączenie \...*.
3.  **Uwaga**: podczas pracy w środowisku [Projekt Części](PartDesign_Workbench/pl.md) i tworzenia szkiców, geometrii odniesienia lub brył pierwotnych, kroki 1 i 2 są zbędne: okno dialogowe Dołączanie jest wyświetlane automatycznie.
4.  W parametrach dołączania można odczytać \"Nie dołączono\". Pierwszy przycisk poniżej jest oznaczony **Wybieranie ...**, aby wskazać, że oczekuje się zaznaczenia w oknie widoku 3D.
5.  Wybierz element topologii obiektu, do którego chcesz dołączyć: wierzchołek, krawędź lub ścianę / płaszczyznę. Geometria układu odniesienia z kontenerów [Część](Std_Part/pl.md) jest również dostępna.
6.  Etykieta pierwszego przycisku przyjmuje teraz nazwę wybranego typu topologii. W białym polu po prawej stronie dodawany jest obiekt i jego element. Na przykład, jeśli wybrano ścianę na bryle pierwotnej sześcianu, w polu pojawi się opis Box:Face6.
7.  Wybierz [Tryb dołączania](#Tryb_dołączania.md) z listy. Dostępne tryby są filtrowane według wybranych odniesień. *Dołączono w trybie * zostanie wyświetlone pod nagłówkiem **Dołączenie**.
8.  Aby uzyskać aktualne informacje o trybach dołączania, najedź kursorem myszki na jeden z trybów na liście, aby wyświetlić podpowiedź.
9.  Opcjonalnie można dodać do 3 kolejnych referencji, naciskając przyciski **Odniesienie 2**, **Odniesienie 3** i **Odniesienie 4** i powtarzając krok 4.
10. Opcjonalnie ustaw [Odsunięcie dołączenia](#Odsunięcie_dołączenia.md).
11. Naciśnij **OK**.



## Opcje

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">



### Tryb dołączenia 



#### Nieaktywny

Domyślnie, nie wybrano odniesienia.



#### Normalna do krawędzi 

Obiekt jest ustawiony prostopadle do krawędzi. Opcjonalne odniesienie do wierzchołka definiuje lokalizację.

:; Kombinacje odniesienia:

:   krawędź
:   krawędź, wierzchołek
:   wierzchołek, krawędź

Zobacz [Wyrównanie trybów dołączania typu O-X-Y](O-X-Y_type_attachment_modes/pl.md), aby uzyskać więcej informacji na temat następujących trybów:



#### Wyrównanie O-Z-X 

Dopasowuje początek obiektu do pierwszego wskazywanego wierzchołka, a następnie wyrównuje jego normalną i poziomą oś płaszczyzny w kierunku wierzchołka / wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Wyrównanie O-Z-Y 

Dopasowuje początek obiektu do pierwszego wskazywanego wierzchołka, a następnie wyrównuje swoją normalną i pionową oś płaszczyzny w kierunku wierzchołka / wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Wyrównanie O-X-Y 

Dopasowuje punkt początkowy obiektu do pierwszego wskazywanego wierzchołka i wyrównuje jego poziome i pionowe osie płaszczyzny w kierunku wierzchołka / wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Wyrównanie O-X-Z 

Dopasowuje początek obiektu do pierwszego wskazywanego wierzchołka i wyrównuje jego oś płaszczyzny poziomej i normalną w kierunku wierzchołka/wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Wyrównanie O-Y-Z 

Dopasowuje początek obiektu do pierwszego wskazywanego wierzchołka i wyrównuje jego pionową oś płaszczyzny i normalną w kierunku wierzchołka / wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Wyrównanie O-Y-X 

Dopasowuje początek obiektu do pierwszego wskazywanego wierzchołka i wyrównuje jego pionowe i poziome osie płaszczyzny w kierunku wierzchołka / wzdłuż linii.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek
:   wierzchołek, wierzchołek, krawędź
:   wierzchołek, krawędź, wierzchołek
:   wierzchołek, krawędź, krawędź
:   wierzchołek, wierzchołek
:   wierzchołek, krawędź



#### Przekształcenia położenia odniesienia 

Początek obiektu jest wyrównany do dopasowanego wierzchołka. Orientacja jest kontrolowana przez właściwość [Umiejscowienie](Placement/pl.md).

:; Kombinacje odniesienia:

:   wierzchołek.



#### XY Obiektu 

Płaszczyzna jest wyrównana do lokalnej płaszczyzny XY połączonego obiektu.

:; Kombinacje odniesienia:

:   dowolny, stożek.



#### XZ Obiektu 

Płaszczyzna jest wyrównana do lokalnej płaszczyzny XZ połączonego obiektu.

:; Kombinacje odniesienia:

:   dowolny, stożek.



#### YZ Obiektu 

Płaszczyzna jest wyrównana do lokalnej płaszczyzny YZ połączonego obiektu.

:; Kombinacje odniesienia:

:   dowolny, stożek.



#### Płaszczyzna ściany 

Płaszczyzna jest wyrównana tak, aby pokrywała się z płaską powierzchnią.

:; Kombinacje odniesienia:

:   płaszczyzna.



#### Styczna do powierzchni 

Płaszczyzna jest styczna do powierzchni w punkcie wierzchołka.

:; Kombinacje odniesienia:

:   ściana, wierzchołek,
:   wierzchołek, ściana.



#### NB układu Freneta 

Płaszczyzna jest ustawiana na osie normalne-binormalne *(NB)* [współrzędnych Frenet-Serret](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) w punkcie krzywej krawędzi, który jest najbliżej wierzchołka *(lub zdefiniowany przez właściwość MapPathParameter, jeśli wierzchołek nie jest połączony)*. Początek obiektu jest przekształcany do wierzchołka, jeśli wierzchołek jest pierwszy, lub utrzymywany na krzywej, jeśli krawędź jest pierwsza. Ten tryb jest podobny do *Normalna do krawędzi*, z wyjątkiem tego, że oś X jest dobrze zdefiniowana.

:;Kombinacje odniesienia:

:   krzywa,
:   krzywa, wierzchołek,
:   wierzchołek, krzywa.
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">



#### TN układu Freneta 

Płaszczyzna jest ustawiana na osie normalne styczne *(TN)* [współrzędnych Frenet-Serret](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) w punkcie krzywej krawędzi, który jest najbliżej wierzchołka *(lub zdefiniowany przez właściwość MapPathParameter, jeśli wierzchołek nie jest połączony)*. Początek szkicu jest przekształcany do wierzchołka, jeśli wierzchołek jest pierwszy, lub zachowany na krzywej, jeśli krawędź jest pierwsza. W efekcie, jeśli krzywa jest płaska, płaszczyzną szkicowania jest płaszczyzna krzywej.

:;Kombinacje odniesienia:

:   krzywa,
:   krzywa, wierzchołek,
:   wierzchołek, krzywa.
:   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">



#### TB układu Freneta 

Płaszczyzna jest ustawiana na osie styczne-binormalne *(TB)* [współrzędnych Frenet-Serret](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) w punkcie krzywej krawędzi, który jest najbliżej wierzchołka *(lub zdefiniowany przez właściwość MapPathParameter, jeśli wierzchołek nie jest połączony)*. Początek szkicu jest przekształcany do wierzchołka, jeśli wierzchołek jest pierwszy, lub utrzymywany na krzywej, jeśli krawędź jest pierwsza.

:;Kombinacje odniesienia:

:   krzywa,
:   krzywa, wierzchołek,
:   wierzchołek, krzywa.
:   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">



#### Współosiowo

Wyrównuje do płaszczyzny z okręgiem obrotu krawędzi. Opcjonalne łącze wierzchołka określa, gdzie.

:; Kombinacje odniesienia:

:   krzywa,
:   okrąg,
:   krzywa, wierzchołek,
:   okrąg, wierzchołek,
:   wierzchołek, krzywa,
:   wierzchołek, okrąg.



#### Przekrój przez obrót 

Płaszczyzna jest prostopadła do krawędzi, a oś Y jest dopasowana do osi okręgu. Opcjonalne łącze do wierzchołka określa, gdzie.

:; Kombinacje odniesienia:

:   krzywa,
:   okrąg,
:   krzywa, wierzchołek,
:   okrąg, wierzchołek,
:   wierzchołek, krzywa,
:   wierzchołek, okrąg.



#### Płaszczyzna przez trzy punkty 

Wyrównuje płaszczyznę XY tak, aby przechodziła przez trzy wierzchołki.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek,
:   linia, wierzchołek,
:   wierzchołek, linia,
:   linia, linia.



#### Normalna do trzech punktów 

Wyrównuje płaszczyznę przechodzącą przez pierwsze dwa wierzchołki i prostopadłą do płaszczyzny przechodzącej przez trzy wierzchołki.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek,
:   linia, wierzchołek,
:   wierzchołek, linia,
:   linia, linia.



#### Składany

Specjalny tryb składania wielościanów. Wybierz kolejno cztery krawędzie: krawędź do sklejenia, linia zagięcia, inna linia zagięcia, inna krawędź do sklejenia. Płaszczyzna zostanie wyrównana do złożenia pierwszej krawędzi. Na poniższym obrazku nie jest wymagane, aby oba liście do złożenia były takie same.

:; Kombinacje odniesienia

:   linia, linia, linia, linia.
:   ![ 250px](images/Attacher_mode_Folding.png )



#### Bezwładność 2-3 

Obiekt zostanie dołączony do płaszczyzny przechodzącej przez drugą i trzecią główną oś bezwładności *(przechodzi przez środek masy)*.

:; Kombinacje odniesienia:

:   dowolny,
:   dowolny, dowolny,
:   dowolny, dowolny, dowolny,
:   dowolny, dowolny, dowolny, dowolny.



### Odsunięcie dołączenia 

Funkcja Odsunięcie dołączenia jest używana do zastosowania liniowego lub obrotowego odsunięcia od obiektu, do którego następuje odwołanie. Oznacza to, że przesunięcia są względem \"lokalnego\" układu współrzędnych, a nie globalnego. Funkcja ta staje się aktywna po wybraniu trybu dołączania innego niż *Nieaktywny*.

-   **X**: ustawia odległość przesunięcia w osi X obiektu odniesienia.

-   **Y**: ustawia odległość przesunięcia w osi Y obiektu odniesienia.

-   **Z**: ustawia odległość przesunięcia w osi Z obiektu odniesienia. Ta współrzędna jest używana w częstych przypadkach, gdy szkic ma być przesunięty prostopadle do płaszczyzny.

-   **Wokół osi Z**: obraca dołączony obiekt wzdłuż osi Z obiektu odniesienia.

-   **Wokół osi Y**: obraca dołączony obiekt wokół osi Y obiektu odniesienia.

-   **Wokół osi X**: obraca dołączony obiekt wokół osi X obiektu odniesienia.

-   **Odwróć strony**: jeśli opcja zostanie zaznaczona, dołączony obiekt zostanie odwrócony względem swojej płaszczyzny XY.



## Ograniczenia

-   Kontenery [Część](Std_Part/pl.md) i [Zawartość](PartDesign_Body/pl.md) nie są obsługiwane. Chociaż możliwe jest użycie dołączenia do ich wyrównania, dołączenie nie będzie połączone parametrycznie.
-   Jeśli wybranie dwóch linii spowoduje błąd \"Punkty są współliniowe. Nie można utworzyć płaszczyzny\", spróbuj zamiast tego wybrać trzy punkty [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/pl
