---
 GuiCommand:
   Name: Part EditAttachment
   Name/pl: Część: Dołączenie
   MenuLocation: Część , Dołączenie ...
   Workbenches: Part_Workbench/pl, PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: Placement/pl, Basic_Attachment_Tutorial/pl
---

# Part EditAttachment/pl



## Opis

<img alt="" src=images/Part_EditAttachment.svg  style="width:24px;"> **Dołączenie** jest narzędziem do dołączania obiektu do jednego lub większej liczby innych obiektów. Dołączony obiekt jest powiązany z obiektem, do którego się odnosi, co oznacza, że jeśli [umiejscowienie](Std_Placement/pl.md) lub geometria obiektu, do którego wykonano odniesienie zostanie zmieniona, położenie dołączonego obiektu zostanie odpowiednio zaktualizowane.



## Silniki dołączania 

Dołączanie obiektu jest kontrolowane przez jeden z czterech silników dołączania. Domyślny silnik używany dla obiektu zależy od jego typu. Silnik dołączania obiektu można zmienić poprzez jego właściwość **Attacher Engine** (<small>(v1.0)</small> ) lub [ukrytą](Property_editor/pl#Menu_kontekstowe.md) właściwość **Attacher Type**.

Dostępne silniki są wymienione w tabeli poniżej. Silniki dołączania kontrolują właściwość **Umiejscowienie** obiektów. Wszystkie silniki mogą być użyte dla dowolnych obiektów z tą właściwością. Ale wyniki ostatnich trzech z nich mają najwięcej sensu jeśli kształt obiektu pasuje do wspomnianego \'kształtu logicznego\'.

  Silnik dołączania                                   Typ dołączania                Kształt logiczny
    
  [Silnik 3D](#Engine_3D/pl.md)               Attacher::AttachEngine3D      
  [Silnik Płaszczyzna](#Engine_Plane/pl.md)   Attacher::AttachEnginePlane   Płaska ściana zbieżna z płaszczyzną XY Umiejscowienia
  [Silnik Linia](#Engine_Line/pl.md)          Attacher::AttachEngineLine    Prosta krawędź współliniowa z osią Z Umiejscowienia
  [Silnik Punkt](#Engine_Point/pl.md)         Attacher::AttachEnginePoint   Wierzchołek zbieżny z początkiem układu współrzędnych Umiejscowienia

Pozostała część tej strony skupia się na Silniku 3D. Tryby innych silników są tylko wymienione. Należy pamiętać, że tryby Silnika Płaszczyzna są w rzeczywistości identyczne z trybami Silnika 3D.



## Użycie

1.  Wybierz obiekt, który ma zostać dołączony.
2.  Wykonaj jedną z poniższych czynności:
    -   Jeśli obiekt ma już właściwość **Map Mode**: kliknij na tym polu w [Edytorze właściwości](Property_editor/pl.md) i wciśnij przycisk **...**, który się pojawi.
    -   Wybierz opcję z menu **Część → <img src="images/Part_EditAttachment.svg" width=16px> Dołączenie ...**.
3.  Otworzy się panel zadań **Dołączenie**.
4.  W górnej części panelu zadań można odczytać *Nie dołączono*. Pierwszy przycisk oznaczony **Wybieranie ...** jest podświetlony, aby wskazać, że oczekiwany jest wybór w oknie [widoku 3D](3D_view.md).
5.  Wybierz wierzchołek, krawędź lub ścianę/płaszczyznę należącą do innego obiektu.
6.  W polu wprowadzania po prawej stronie przycisku wyświetlany będzie wybrany obiekt i jego element podrzędny. Na przykład, jeśli wybrana jest ściana [sześcianu środowiska Część](Part_Box/pl.md), pole może pokazywać informację {{Value|Sześcian:Ściana6}}. Etykieta przycisku wyświetla teraz typ elementu podrzędnego.
7.  Dostępne tryby są filtrowane na podstawie wybranych odniesień i ich kolejności. Na przykład dla trybów [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md) do [Wyrównanie O-Y-X](#Wyrównanie_O-Y-X.md) pierwsze odniesienie musi być wierzchołkiem. Jeśli pierwsze odwołanie jest elementem podrzędnym innego typu, są one automatycznie usuwane z listy.
8.  W górnej części panelu zadań jest teraz wyświetlana informacja *Dołączono w trybie *.
9.  Opcjonalnie wybierz inny [Tryb dołączania](#Tryb_dołączania.md) z listy. Aby uzyskać informacje na temat trybów dołączania, wskaż je kursorem myszki, aby wyświetlić podpowiedź.
10. W zależności od wybranego trybu, można dodać do trzech kolejnych odniesień, naciskając przyciski **Odniesienie2**, **Odniesienie3** i **Odniesienie4** i powtarzając krok 5. Możliwe jest również określenie wszystkich odniesień przed wybraniem trybu dołączania.
11. Opcjonalnie ustaw [Odsunięcie dołączenia](#Odsunięcie_dołączenia.md).
12. Naciśnij **OK**.
13. Jeśli dotyczy, opcjonalnie zmień właściwość **Map Path Parameter** w [Edytorze właściwości](Property_editor/pl.md).



## Tryby dołączenia 



### Silnik 3D 

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">



#### Nieaktywny

Dołączanie jest wyłączone. Obiekt można przenieść, edytując jego właściwość [Umiejscowienie](Placement/pl.md).



#### Przekształcenia położenia odniesienia 

Początek obiektu jest wyrównany do dopasowanego wierzchołka. Orientacja jest kontrolowana przez właściwość [Umiejscowienie](Placement/pl.md).

:; Kombinacje odniesienia:

:   wierzchołek.



#### XYZ Obiektu 

Umiejscowienie jest równe umiejscowieniu powiązanego obiektu.

:; Kombinacje odniesienia:

:   dowolne,
:   stożek.



#### XZY Obiektu 

Osie X, Y i Z są dopasowywane odpowiednio do lokalnych osi X, Z i -Y połączonego obiektu.

:; Kombinacje odniesienia:

:   dowolne,
:   stożek.



#### YZX Obiektu 

Osie X, Y i Z są dopasowywane odpowiednio do lokalnych osi Y, Z i X połączonego obiektu.

:; Kombinacje odniesienia:

:   dowolne,
:   stożek.



#### XY na płaszczyźnie 

Płaszczyzna XY jest wyrównana tak, aby pokrywała się z płaską powierzchnią.

:; Kombinacje odniesienia:

:   płaszczyzna.



#### Styczna do powierzchni XY 

Płaszczyzna XY jest styczna do ściany w punkcie wierzchołka.

:; Kombinacje odniesienia:

:   ściana, wierzchołek,
:   wierzchołek, ściana.



#### Z stycznie do krawędzi 

Oś Z jest wyrównana tak, aby była styczna do krawędzi. Opcjonalny wierzchołek określa to miejsce.

Jeśli żaden wierzchołek nie jest powiązany, właściwość **Parametr ścieżki mapowania** określa punkt.

:; Kombinacje odniesienia:

:   krawędź
:   krawędź, wierzchołek
:   wierzchołek, krawędź



#### NBT układu Freneta 

<img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

Osie X i Y są wyrównane do osi normalnej *(N)* i binormalnej *(B)* układu współrzędnych [Frenet\'a-Serret\'a](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) w punkcie na zakrzywionej krawędzi. Opcjonalny wierzchołek określa położenie.

Jeśli żaden wierzchołek nie jest powiązany, właściwość **Parametr ścieżki mapowania** określa punkt. Początek obiektu jest przenoszony do wierzchołka, jeśli wierzchołek jest pierwszy, lub utrzymywany na krzywej, jeśli krzywa jest pierwsza.

*Frenet NBT* jest podobny do *Z stycznie do krawędzi*, z tą różnicą, że oś X jest ściśle zdefiniowana.

:;Kombinacje odniesienia:

:   krzywa,
:   krzywa, wierzchołek,
:   wierzchołek, krzywa.



#### TNB układu Freneta 

<img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

Osie X i Y są wyrównane do osi stycznej *(T)* i normalnej *(N)* układu współrzędnych Frenet\'a-Serret\'a w punkcie na zakrzywionej krawędzi. Opcjonalny wierzchołek określa miejsce.

Patrz [NBT układu Freneta](#NBT_układu_Freneta.md).



#### TBN układu Freneta 

<img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

Osie X i Y są wyrównane do osi stycznej *(T)* i binormalnej *(B)* układu współrzędnych Frenet-Serret w punkcie na zakrzywionej krawędzi. Opcjonalny wierzchołek określa miejsce.

Patrz [NBT układu Freneta](#NBT_układu_Freneta.md).



#### Współosiowo

Płaszczyzna XY jest wyrównana do [osculating okręgu](https://en.wikipedia.org/wiki/Osculating_circle) w punkcie na krawędzi. Opcjonalny wierzchołek określa miejsce.

Jeśli żaden wierzchołek nie jest powiązany, właściwość **Parametr ścieżki mapowania** określa punkt.

:; Kombinacje odniesienia:

:   krzywa,
:   okrąg,
:   krzywa, wierzchołek,
:   okrąg, wierzchołek,
:   wierzchołek, krzywa,
:   wierzchołek, okrąg.



#### Przekrój przez obrót 

Oś Y jest wyrównana tak, aby pasowała do osi okręgu oscylującego w punkcie na krawędzi. Opcjonalny wierzchołek określa miejsce.

Patrz [Współosiowo](#Współosiowo.md)



#### Płaszczyzna XY przez trzy punkty 

Płaszczyzna XY jest wyrównana tak, aby przechodziła przez trzy wierzchołki. Oś X będzie przechodzić przez pierwsze dwa wierzchołki.

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek,
:   linia, wierzchołek,
:   wierzchołek, linia,
:   linia, linia.



#### Płaszczyzna XZ przez trzy punkty 

Płaszczyzna XZ jest wyrównana tak, aby przechodziła przez trzy wierzchołki. Oś X będzie przechodzić przez pierwsze dwa wierzchołki.

Patrz [Płaszczyzna XY przez trzy punkty](#Płaszczyzna_XY_przez_trzy_punkty.md).



#### Składany

<img alt="" src=images/Attacher_mode_Folding.png  style="width:250px;">

Jest to specjalny tryb składania wielościanów. Wybierz cztery linie, które mają wspólny punkt w następującej kolejności: linia konturu *(1)*, linia zagięcia *(2)*, inna linia zagięcia *(3)*, inna linia konturu *(4)*. Aby określić układ współrzędnych, wybrane linie konturowe są zbieżne poprzez obrócenie linii 1 wokół linii 2 i linii 4 wokół linii 3. Początek jest dopasowany do punktu wspólnego, oś X jest dopasowana do linii 2, oś Y jest wyrównana w kierunku zbieżnych linii konturowych.

:; Kombinacje odniesienia

:   linia, linia, linia, linia.



#### Bezwładność CS 

Osie X, Y i Z są dopasowane do osi układu współrzędnych bezwładnościowych, zbudowanego na głównych osiach bezwładności i środku masy.

:; Kombinacje odniesienia:

:   dowolny,
:   dowolny, dowolny,
:   dowolny, dowolny, dowolny,
:   dowolny, dowolny, dowolny, dowolny.



#### Wyrównanie O-Z-X 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie Z i X są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Zapoznaj się z treścią strony [Wyrównanie trybów dołączania typu O-X-Y](O-X-Y_Type_Attachment_Modes/pl.md), aby uzyskać więcej informacji na temat następujących trybów:

:; Kombinacje odniesienia:

:   wierzchołek, wierzchołek, wierzchołek,
:   wierzchołek, wierzchołek, linia,
:   wierzchołek, linia, wierzchołek,
:   wierzchołek, linia, krawędź,
:   wierzchołek, wierzchołek,
:   wierzchołek, linia.



#### Wyrównanie O-Z-Y 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie Z i Y są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Patrz [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md).



#### Wyrównanie O-X-Y 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie X i Y są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Patrz [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md).



#### Wyrównanie O-X-Z 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie X i Z są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Patrz [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md).



#### Wyrównanie O-Y-Z 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie Y i Z są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Patrz [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md).



#### Wyrównanie O-Y-X 

Początek obiektu jest dopasowany do pierwszego wierzchołka. Osie Y i X są wyrównane w kierunku wierzchołka lub wzdłuż linii.

Patrz [Wyrównanie O-Z-X](#Wyrównanie_O-Z-X.md).



#### XY równoległe do płaszczyzny 


{{Version/pl|1.0}}

Płaszczyzna XY jest wyrównywana aby była równoległa do płaszczyzny XY Umiejscowienia powiązanego obiektu i przechodziła przez wierzchołek. Początek jest dopasowywany do rzutu początku powiązanego obiektu na płaszczyznę XY.

Zauważ, że musisz wskazać cały obiekt a nie tylko jego element podrzędny, taki jak ściana czy płaszczyzna.

:; Kombinacje odniesień:

:   Dowolny cały obiekt (z właściwością **Umiejscowienie**), wierzchołek


<div class="toccolours mw-collapsible mw-collapsed">



### Silnik Płaszczyzna 


<div class="mw-collapsible-content">

-   Nieaktywny
-   Przenieś odniesienie położenia
-   XY obiektu
-   XZ obiektu
-   YZ obiektu
-   Płaszczyzna ściany
-   Prostopadle do powierzchni
-   Normalna do krawędzi
-   NB układu Freneta
-   TN układu Freneta
-   TB układu Freneta
-   Współosiowo
-   Przekrój przez obrót wokół osi
-   Płaszczyzna wyznaczona przez 3 punkty
-   Normalna do 3 punktów
-   Składany
-   Bezwładność 2-3
-   Wyrównanie O-N-X
-   Wyrównanie O-N-Y
-   Wyrównanie O-X-Y
-   Wyrównanie O-X-N
-   Wyrównanie O-Y-N
-   Wyrównanie O-Y-X
-   XY równolegle do płaszczyzny {{Version/pl|1.0}}


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Silnik Linia 


<div class="mw-collapsible-content">

-   Nieaktywny
-   Oś X Obiektu
-   Oś Y obiektu
-   Oś Z obiektu
-   Oś krzywizny
-   Linia kontrolna 1
-   Linia kontrolna 2
-   Asymptota 1
-   Asymptota 2
-   Stycznie
-   Normalna do krawędzi
-   Binormalna
-   Przez dwa punkty
-   Przecięcie {{Version/pl|1.0}}
-   Linia zbliżeniowa
-   Pierwsza oś główna
-   Druga oś główna
-   Trzecia oś główna
-   Normalna do powierzchni


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Silnik Punkt 


<div class="mw-collapsible-content">

-   Nieaktywny
-   Odniesienie położenia obiektów
-   Ogniskowa 1
-   Ogniskowa 2
-   Na krawędzi
-   Środek krzywizny
-   Środek ciężkości
-   Wierzchołek
-   W pobliżu punktu 1
-   W pobliżu punktu 2


</div>


</div>



## Odsunięcie dołączenia 

Odsunięcie dołączania staje się aktywne po wybraniu trybu dołączania innego niż \"Niedołączono\". Służy do zastosowania przesunięcia liniowego lub obrotowego w układzie współrzędnych dołączenia *(ACS)*, zgodnie z definicją trybu umocowania i obiektu *(obiektów)*, do którego się odwołano.

-   **W kierunku X**: ustawia odległość przesunięcia wzdłuż osi X układu współrzędnych dołączenia.

-   **Y**: **W kierunku Y**: ustawia odległość przesunięcia wzdłuż osi Y układu współrzędnych dołączenia *(ACS)*.

**W kierunku Z**: ustawia odległość przesunięcia wzdłuż osi Z układu współrzędnych dołączenia *(ACS)*.

-   **Wokół osi X**: obraca dołączony obiekt wokół osi X układu współrzędnych dołaczenia *(ACS)*.

-   **Wokół osi Y**: obraca dołączony obiekt wokół osi Y układu współrzędnych dołaczenia *(ACS)*.

-   **Wokół osi Z**: obraca dołączony obiekt wokół osi Z układu współrzędnych dołaczenia *(ACS)*.

-   **Odwróć strony**: jeśli opcja zostanie zaznaczona, dołączony obiekt zostanie odwrócony. Jest to równoznaczne z obróceniem obiektu o 180° wokół osi Y systemu współrzędnych dołączenia.



## Ograniczenia

-   Jeśli wybranie dwóch linii spowoduje błąd \"Punkty są współliniowe. Nie można utworzyć płaszczyzny\", spróbuj zamiast tego wybrać trzy wierzchołki [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/pl
