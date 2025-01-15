# Artwork Guidelines/pl
## Wprowadzenie


**Uwaga:**

wszystkie ikony w drzewie źródłowym, zobacz na stronie [grafika](Artwork/pl.md).

**Ikona** FreeCAD składa się z 6 elementów, które można zapamiętać za pomocą akronimu SALCHO: **S**troke, **A**lignment, **L**ighlighting, **C**olor, **H**ighlighting, **O**utline.

Oto konkretny, aczkolwiek dowolny przykład:

![](images/FreeCAD_icon_example_details.svg )

  --- 
  A   Kolor podświetlenia jest używany na całej powierzchni, aby wskazać światło padające z góry.
  B   Obowiązkowy ciemny kontur otacza kształt ikony, aby zapewnić kontrast kształtu.
  C   Obrys wewnątrz konturu *(kolor podświetlenia)* zapewnia kontrast na ciemnym tle.
  D   Ta powierzchnia ma głównie kolor bazowy, ale jasny gradient od podświetlenia *(u góry po lewej)* do bazy *(u dołu po prawej)* sprawia wrażenie światła padającego z góry po lewej.
  E   Podświetleniem jest tutaj kolor bazowy *(o jeden ton niższy)*, aby sprawić wrażenie, że jest to twarz najbardziej oddalona od światła.
  F   Ta powierzchnia jest podobna do D, ale przechodzi od podstawy *(lewy górny róg)* do ciemności *(prawy dolny róg)*, aby wskazać, że jest to powierzchnia najbardziej oddalona od światła.
  --- 

Poniższe sekcje wyjaśniają te elementy bardziej szczegółowo.

Ikona ta jest wyświetlana w następujący sposób:

+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:64px;"> | 64 px, oryginalny rozmiar, duże przyciski.                                        |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:32px;"> | 32 px, średni rozmiar, zwykłe przyciski.                                          |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:16px;"> | 16 px, mały rozmiar, tak jak pojawia się w [widoku drzewa](Tree_view.md). |
+++



## Kolory


**Obowiązkowe**

FreeCAD używa palety zaadaptowanej z [palety Tango](https://web.archive.org/web/20190921043652/http://tango.freedesktop.org/tango_icon_theme_guidelines). Każdy główny kolor ma 4 odcienie: Podświetlenia, Bazy, Ciemnego i Konturu. Zauważ, że Kontur nie jest całkowicie czarny, ale jest bardzo ciemną odmianą Bazy.

+++++
| #fce94f         | #edd400         | #c4a000         | #302b00         |
| (252, 233, 79)  | (237, 212, 0)   | (196, 160, 0)   | (48, 43, 0)     |
| Butter 1        | Butter 2        | Butter 3        | Butter 4        |
+=================+=================+=================+=================+
| #8ae234         | #73d216         | #4e9a06         | #172a04         |
| (138, 226, 52)  | (115, 210, 22)  | (78, 154, 6)    | (23, 42, 4)     |
| Chameleon 1     | Chameleon 2     | Chameleon 3     | Chameleon 4     |
+++++
| #fcaf3e         | #f57900         | #ce5c00         | #321900         |
| (252, 175, 62)  | (245, 121, 0)   | (206, 92, 0)    | (50, 25, 0)     |
| Orange 1        | Orange 2        | Orange 3        | Orange 4        |
+++++
| #729fcf         | #3465a4         | #204a87         | #0b1521         |
| (114, 159, 207) | (52, 101, 164)  | (32, 74, 135)   | (11, 21, 33)    |
| Sky Blue 1      | Sky Blue 2      | Sky Blue 3      | Sky Blue 4      |
+++++
| #ad7fa8         | #75507b         | #5c3566         | #171018         |
| (173, 127, 168) | (117, 80, 123)  | (92, 53, 102)   | (23, 16, 24)    |
| Plum 1          | Plum 2          | Plum 3          | Plum 4          |
+++++
| #e9b96e         | #c17d11         | #8f5902         | #271903         |
| (233, 185, 110) | (193, 125, 17)  | (143, 89, 2)    | (39, 25, 3)     |
| Chocolate 1     | Chocolate 2     | Chocolate 3     | Chocolate 4     |
+++++
| #ef2929         | #cc0000         | #a40000         | #280000         |
| (239, 41, 41)   | (204, 0, 0)     | (164, 0, 0)     | (40, 0, 0)      |
| Scarlet Red 1   | Scarlet Red 2   | Scarlet Red 3   | Scarlet Red 4   |
+++++
| #34e0e2         | #16d0d2         | #06989a         | #042a2a         |
| (52, 224, 226)  | (22, 208, 210)  | (6, 152, 154)   | (4, 42, 42)     |
| FreeTeal 1      | FreeTeal 2      | FreeTeal 3      | FreeTeal 4      |
+++++
| #ffffff         | #eeeeec         | #d3d7cf         | #babdb6         |
| (255, 255, 255) | (238, 238, 236) | (211, 215, 207) | (186, 189, 182) |
| Snowy White     | Aluminium 1     | Aluminium 2     | Aluminium 3     |
+++++
| #888a85         | #555753         | #2e3436         | #000000         |
| (136, 138, 133) | (85, 87, 83)    | (46, 52, 54)    | (0, 0, 0)       |
| Aluminium 4     | Aluminium 5     | Aluminium 6     | Jet Black       |
+++++



*Kompletna paleta*

Wybór niektórych kluczowych kolorów.

      
                                                                                                                                                          Użyj żółtych odcieni dla narzędzi tworzących obiekty, np. zobacz środowiska pracy [Część](Part_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md).
  style=\"background-color:#729fcf;\|   style=\"background-color:#3465a4;\|   style=\"background-color:#204a87;\|   style=\"background-color:#0b1521;\|   Użyj niebieskich odcieni dla narzędzi modyfikujących obiekty, np. zobacz środowiska pracy [Część](Part_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md).
  style=\"background-color:#34e0e2\|    style=\"background-color:#16d0d2\|    style=\"background-color:#06989a\|    style=\"background-color:#042a2a\|    Użyj odcieni barwy morskiej dla narzędzi związanych z widokami, np. zobacz [Menu Widok](Std_View_Menu/pl.md).
  style=\"background-color:#ef2929\|    style=\"background-color:#cc0000\|    style=\"background-color:#a40000\|    style=\"background-color:#280000\|    Użyj czerwonych odcieni dla narzędzi związanych z wiązaniami, np. zobacz [Szkicownik](Sketcher_Workbench/pl.md).
      

   
  style=\"width: 25%;\|Dlaczego ograniczać się do tych kolorów?   Ograniczenie kolorów do określonej palety pomaga uniknąć niejednorodnej ikonografii i poprawia czytelność w przypadku wielu ikon.
  Jak używać palety FreeCAD?                                      Instalacja [palety](https://gist.github.com/GAZ082/724d2092b2986e3b17b9663f34093cf5) jest tak prosta, jak [skopiowanie jej do folderu palety Inkscape](https://inkscape.org/en/learn/faq/#how-install-new-extensions-palettes-document-templates-symbol-sets-icon-sets-etc).
   



## Szerokość siatki i obrysu 


**Obowiązkowe**

Ikony FreeCAD mają nominalny rozmiar 64 pikseli zarówno w szerokości, jak i wysokości. Podczas tworzenia lub edycji ikony należy upewnić się, że rozmiar dokumentu wynosi 64 x 64, a jednostkami są piksele (px). Pozostawienie wewnętrznego marginesu 2px pustej przestrzeni wokół obszaru dokumentu jest przydatne, ponieważ zapobiega efektom takim jak antyaliasing (rozmycie krawędzi). Oznacza to, że przestrzeń użytkowa dla ikony powinna wynosić 60 x 60, a krawędzie powinny pozostać puste.

<img alt="" src=images/FreeCAD_icon_size.svg  style="width:128px;"> 
*Narysuj ikonę wewnątrz niebieskiego obszaru, a wszystko będzie działać poprawnie.*

Zdecydowanie zaleca się również użycie siatki wizualnej, która ma mniejszą linię siatki co piksel i główną linię siatki co 2 piksele. Obrysy ikony powinny być wyrównane wzdłuż przecięć siatki pomocniczej.

Obrysy nie powinny być *cieńsze* niż 2px, z zaokrąglonymi nakładkami i narożnikami w większości przypadków. Obrysy mogą być *grubsze*, ale powinny być wielokrotnością 2 pikseli, aby zminimalizować rozmycie skalowania.

<img alt="" src=images/FreeCAD_icon_stroke_2px.svg  style="width:320px;"> 
*Siatka z obrysami będącymi wielokrotnością 2px.*

   
  Dlaczego używana jest ta siatka i rozmiar obrysu?   Ze względów historycznych FreeCAD używa ikony 64x64, która jest następnie skalowana w dół. Nie jest to idealne rozwiązanie, ale dodaje charakteru. W rezultacie utrzymywanie rzeczy wyrównanych do siatki potęgi dwójki i grubości będących potęgami dwójki pomaga uniknąć lub przynajmniej złagodzić problemy z antyaliasingiem podczas ponownego skalowania.
  Jak mogę się do tego zastosować?                    Jeśli używasz Inkscape, przejdź do **File → Document Properties** i potwierdź, że szerokość, wysokość i jednostki strony są prawidłowe. Następnie przejdź do zakładki **Grids**, kliknij **New**, ustaw jednostki na `px`, `Spacing X` i `Spacing Y` na 1 oraz `Major grid line every` na 2.
   



## Kontur


**Obowiązkowe**

Opierając się na głównym kolorze ikony, upewnij się, że istnieje ciemny kontur 2px, jak wspomniano wcześniej. Działa to w połączeniu z podświetleniem, aby zapewnić dobry kontrast formy na wielu odcieniach tła.

<img alt="" src=images/Draft_Point.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Point_backgrounds.svg  style="width:" height="128px;"> 
*Ciemna krawędź ikony to kontur.*

   
  Dlaczego kontur jest potrzebny?    Kontur jest szkieletem, na którym wszystko inne wisi, dodając kontrast formy. Użycie koloru konturu lub ciemnego koloru zależy od sytuacji, ale bez tej linii zakres tła, na którym ikona jest widoczna, zostaje drastycznie ograniczony
  Jak mogę się do tego zastosować?   Wystarczy dodać obrys 2px wokół każdej części ikony, która będzie przylegać do koloru tła, czyli kontur jest dla obrysów zewnętrznych. W przypadku kształtów, które mają otwór w środku, na przykład oponka pączek, kontur należy również dodać do wewnętrznego otworu. Przyciągaj węzły ścieżki do siatki, gdy tylko jest to możliwe, celując w mniejsze przecięcia siatki.
   



## Podświetlenie


**Zdecydowanie zalecane**

Używając koloru podświetlenia, dodaj wewnętrzny obrys o wielkości 2 pikseli, aby kontur był bardziej widoczny. Na ciemnych tłach to właśnie to podświetlenie będzie stanowić formę ikony.

<img alt="" src=images/Draft_Move.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Move_backgrounds.svg  style="width:" height="128px;"> 
*Jasne podświetlenie jest pomocne na ciemnym tle.*

   
  Dlaczego warto używać podświetlenia?   Podświetlenie działa w połączeniu z konturem, aby poprawić kontrast formy, szczególnie na ciemnych tłach. Nigdy nie jest to zły pomysł, ale jeśli nie masz miejsca, na przykład masz bardzo cienką linię, możesz z niego zrezygnować, pod warunkiem, że zapewniłeś wystarczający kontrast między głównym kolorem a konturem.
  Jak mogę się do tego zastosować?       Podobnie jak w przypadku obrysu, po prostu narysuj kontur o szerokości 2 pikseli wokół wewnętrznej strony obrysu, przyciągając węzły do siatki, jeśli to możliwe, celując w mniejsze przecięcia siatki.
   



## Podświetlenie 


**Opcjonalne**

Zgodnie z wytycznymi Tango, jeśli dodajesz efekt oświetlenia gradientowego, postaraj się, aby wyglądało na to, że światło pochodzi z lewego górnego rogu. Odbywa się to poprzez dodanie koloru podświetlenia w lewym górnym rogu i koloru bazowego lub ciemnego w prawym dolnym rogu. Zauważ, że używane są tylko kolory z palety.

<img alt="" src=images/Draft_Clone.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Clone_backgrounds.svg  style="width:" height="128px;"> 
*Subtelny efekt podświetlenia od lewego górnego rogu.*

   
  style=\"width:25%;\|Dlaczego warto używać oświetlenia?   Oświetlenie to tylko kolejny sposób na powiązanie ikon i zapewnienie różnych poziomów [\"wartości\"](https://en.wikipedia.org/wiki/Lightness) w celu poprawy ich czytelności. Pod warunkiem jednak, że kontur i podświetlenie są obecne, można je uznać za opcjonalne
  Jak mogę się do tego zastosować?                         Ustaw wypełnienie jako gradient liniowy lub radialny. W Inkscape jest to dostępne w ustawieniach obrysu i wypełnienia; za pomocą \"F2\" można przesuwać węzły gradientu, aby upewnić się, że są pod odpowiednim kątem.
   



## Zalecany format zapisu 

Wszystkie ikony powinny być tworzone w formacie [SVG](SVG/pl.md) za pomocą aplikacji do tworzenia obrazów wektorowych, takiej jak [Inkscape](http://inkscape.org). Ułatwia to wprowadzanie zmian i tworzenie dodatkowych ikon w tej samej przestrzeni aplikacji.

Podczas zapisywania ikon, które mają być używane bezpośrednio przez FreeCAD *(w pliku \*.qrc)*, należy zapisać je jako \"Plain SVG\". Zmniejszy to rozmiar ikony i zaoszczędzi miejsce na dysku i w pamięci.



## Uwagi końcowe 

Pamiętaj: **SALCHO**, *(**S**troke, **A**lignment, **L**ighting, **C**olor, **H**ighlight, **O**utline)* Obrys, Wyrównanie, Oświetlenie, Kolor, Podświetlenie, Kontur

Oto kilka wskazówek, jak sprawdzić swoją pracę.



### Sprawdzanie rozmiaru 

Inkscape posiada przydatne narzędzie do sprawdzania ikon w różnych rozmiarach. Przejdź do **View → Icon Preview...**, by zobaczyć podgląd ikony w rozmiarze 16, 24, 32 i 64 pikseli.



### Sprawdzanie konturu 

1.  Umieść ikonę na dużym prostokącie, który ma ten sam kolor co najciemniejszy kolor ikony.
2.  Nadal wygląda OK? Świetnie. Przejdź do następnego kroku. Jeśli nie, dostosuj podświetlenie.
3.  Zrób to samo, ale tym razem używając najjaśniejszego koloru.
4.  Nadal wygląda dobrze? Świetnie. Kontury i podświetlenia zostały użyte prawidłowo. W przeciwnym razie dostosuj kontur.

<img alt="" src=images/Draft_Move_backgrounds_outline.svg  style="width:" height="128px;"> 
*Testowanie ikony na tle najciemniejszego i najjaśniejszego koloru.*

   
  Moja ikona jest ledwo widoczna.   Masz słaby kontrast kształtu. Dokładnie sprawdź kontur i podświetlenie, prawdopodobnie brakuje jednego z nich lub są one nieprawidłowo zastosowane.
   



### Sprawdzanie kontrastu 

1.  Wyeksportuj ikonę z SVG do formatu bitmapy, takiego jak `.png` lub `.jpg`.
2.  Załaduj bitmapę do programu graficznego i przekształć ją do odcieni szarości. Na przykład, w programie GIMP należy przejść do **Image → Mode → Grayscale**.
3.  Inkscape pozwala na bezpośrednią konwersję SVG do skali szarości za pomocą **Extensions → Color → Grayscale**.
4.  Czy nadal wyraźnie widać wewnętrzne szczegóły? Świetnie. Kontrast jest dobry.

Obraz w skali szarości pozwala łatwiej zidentyfikować problemy z kontrastem, ponieważ obecna jest tylko mieszanka czerni i bieli. Testowanie obrazów w skali szarości jest również dobre dla użytkowników niewidzących kolorów. Jeśli widzą oni szczegóły na obrazie w skali szarości, to kontrast w pełni kolorowego obrazu jest prawdopodobnie również dobry.

<img alt="" src=images/Draft_Move_contrast_grayscale.svg  style="width:" height="128px;"> 
*Testowanie kontrastu ikony w skali szarości.*

   
  Nie jestem w stanie rozróżnić wszystkich szczegółów.   Wybrane kolory mają słaby kontrast wartości. Spróbuj użyć kolorów, które są bardziej oddalone od siebie w palecie 4 tonów, to znaczy, że podświetlona zieleń obok podświetlonej żółci będzie trudna do zobaczenia, obniż jeden z tych kolorów do poziomu podstawowego lub ciemnego.



---
⏵ [documentation index](../README.md) > [Artwork](Category_Artwork.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Artwork Guidelines/pl
