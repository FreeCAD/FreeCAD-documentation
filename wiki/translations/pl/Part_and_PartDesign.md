# Part and PartDesign/pl
{{TOCright}}



## Informacje ogólne 

Przez lata było wiele dyskusji o różnicach i konsekwencjach używania środowisk pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) i <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Dobrym pomysłem jest używanie jednego lub drugiego, dopóki użytkownik nie będzie czuł się komfortowo z jednym, a następnie nauczy się drugiego. Zazwyczaj zaleca się również, aby nowi użytkownicy nie mieszali ich ze sobą, dopóki nie zrozumieją konsekwencji takiego postępowania.

Porozmawiajmy o tych konsekwencjach.



## Koncepcje środowiska Część 

Środowisko pracy Część jest zasadniczo [Konstrukcyjną geometrią bryły CSG ](Constructive_solid_geometry/pl.md). Operator łączy różne bryły pierwotne, aby w końcu otrzymać reprezentację pożądanego kształtu. *(W rzeczywistości, środowisko Część idzie o krok dalej niż tylko bryły pierwotne i pozwala operatorowi na użycie operacji szkic + wyciągnięcie (lub szkic + odwrócenie, pochylenie, omiatanie \...)*, aby utworzyć losowe kształty również)*. Kiedy każda bryła pierwotna lub kształt jest tworzony, nie ma żadnego związku z innymi utworzonymi obiektami*(z wyjątkiem szkiców i ich załączników)\'\', jest to pojedyncza bryła.

![centre\|Pojedyncze bryły](images/Part_CSG_Prims.png )

Ten stan utrzymuje się do momentu, gdy operator użyje jakiejś operacji do ich połączenia *(zazwyczaj jest to operacja typu logicznego)*. Każda początkowa bryła pozostaje dostępna osobno, a operacja tworzy nowy obiekt.

Chodzi o pojedyncze elementy brył i ich łączenie.



## Koncepcje środowiska Projekt Części 

W środowisku pracy Projekt Części obiekt Zawartość jest konstruowany bezpośrednio jako pojedyncza zwarta bryła.

Pierwszym krokiem w bryle musi być blok materiału, albo z addytywnej bryły pierwotnej, albo z wyciągnięcia ze szkicu, albo z importowanego kształtu *(zwanego wtedy Bryłą Bazową)*.

Ten początkowy blok materiału będzie sukcesywnie zmieniany aż do uzyskania pożądanego kształtu końcowego *(bryły)*.

Jest on kumulatywny w tym sensie, że każda operacja dodaje lub usuwa materiał.

Domyślnie \"końcówka\" bryły - o ile nie nastąpi dobrowolna zmiana wizualizacji danej cechy - jest ostatnią operacją wykonaną na bryle. Jest to aktualny i widoczny stan zawartości, gotowy do ponownej zmiany przez nową cechę.

Każda funkcja pod bryłą reprezentuje skumulowany kształt bryły od pierwszej cechy do rozpatrywanej cechy.

Zatem **aby mieć kompletną bryłę**, z jednej strony cecha Czubka musi być ostatnim etapem budowy tej bryły, a z drugiej strony **to bryła musi być wybrana**, a nie etap jej budowy.

Umożliwi to, w przypadku modyfikacji, **posiadanie zawsze reprezentowanej ostatniej wersji bryły**.

**Uwagi i uzupełnienia :** W każdym momencie konstrukcji, ostatnią używaną funkcją jest \"Czubek\", którą można zdefiniować również jako \"aktywny etap w konstrukcji obiektu\" lub \"etap poprzedzający następną czynność w konstrukcji obiektu\". Kiedy rysunek obiektu jest kompletny, Czubek jest naturalnie ostatnim etapem lub cechą konstrukcji. Ale jeśli jest to pożądane, w przypadku zapomnienia, dowolna cecha konstrukcji może być tymczasowo zadeklarowana jako Czubek: staje się ona wtedy etapem poprzedzającym następne działanie w konstrukcji obiektu, co oznacza, że nowa cecha (nowe cechy) może być wstawiona w dowolnym miejscu konstrukcji, **pod warunkiem, że nie tworzy żadnej niezgodnej z zestawem**.

Kiedy wszystko jest skończone, musisz ponownie zadeklarować ostatnią cechę jako Czubek, która odpowiada gotowemu obiektowi.

![centre\|Skumulowana zawartość bryły](images/Part_Design_Cumulativ.png )

Ten obrazek przedstawia Zawartość. Jest to jednolita bryła, która składa się z warstwowego szkicu i bryły pierwotnej stożka. Jest to pojedyncza bryła.

Jeżeli czubek jest na **wyciągnięciu**, to wyciągnięcie może istnieć oddzielnie, ale jeżeli jest na **stożku**, stożek nie może istnieć oddzielnie *(wyciągnięcie na stożku = wyciągnięcie + stożek)*.

*(Inną rzeczą, o której często się wspomina jest to, że bryła ***musi*** być pojedynczą spójną bryłą. Oznacza to, że cała geometria utworzona przez element w Zawartości*musi*dotykać jego poprzednika)*.



## Następstwa

Chociaż nie jest to zalecane dla początkujących, możliwe jest połączenie narzędzi środowiska Część i Projekt Części, pod warunkiem, że wiesz co robisz. Na przykład:

Ludzie łapią się na tym, że próbują użyć jakiegoś elementu pod bryłą (a nie samej bryły) jako jednego wyboru operacji logicznej środowiska pracy Część. Jest to problem, ponieważ wybrana cecha nie reprezentuje **TEJ** kompletnej bryły.

W pewnym sensie, z punktu widzenia środowiska Część, Zawartość reprezentuje inna bryła pierwotna. Tak więc, użycie Zawartość *(pamiętaj, że jest to pośrednik dla czubka)* i obiektu środowiska Część do wykonania operacji logicznej jest poprawne. Ale wynikowy obiekt jest obiektem środowiska Część. I dlatego narzędzia środowiska Projekt Części nie mogą być już na nim użyte.

I, to może być jeszcze bardziej skomplikowane. Jeśli utworzysz nową bryłę i przeciągniesz do niej wynik z poprzedniego akapitu, powstanie obiekt bazowy *(BaseObject)*. I możesz użyć na nim narzędzi środowiska Projekt Części.



## Ograniczenia

Istnieje pewne zastrzeżenie dotyczące Czubka i jego reprezentacji pojedynczej bryły w Zawartości. *Jeżeli* czubek jest cechą odejmowania i jest używany w operacji ulepszenia, na przykład w Odbiciu lustrzanym, to działa na bazową cechę *(na przykład kieszeń)*. W ten sposób łączna bryła nie jest odbiciem lustrzanym, ale cecha odejmowania jest. W wyniku tego musi powstać pojedyncza bryła.

W tym przykładzie, lustrzane odbicie czubka *(który jest kieszenią)* wokół którejkolwiek z płaszczyzn bazowych lub nawet powierzchni bryły nie spowoduje powstania lustrzanej bryły całego modelu. *(W rzeczywistości, spowoduje to utworzenie elementu lustrzanego w drzewie, który jest w zasadzie pusty)*.

![centre\|Jednolite bryły](images/PhantomMirror.png )

W tym przykładzie, lustrzane odbicie czubka *(który jest kieszenią)* jest wykonywane wokół płaszczyzny odniesienia i tworzy lustrzaną szczelinę:

![centre\|Jednolite bryły](images/MirroredSlot.png )

Zobacz stronę wiki narzędzia <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Odbicie lustrzane](PartDesign_Mirrored/pl.md), aby uzyskać więcej informacji.



## Porównanie

Poniżej możesz zobaczyć ten sam przykład zbudowany przy użyciu każdego z dwóch środowisk pracy. Oczywiście, zawsze istnieje kilka możliwych przebiegów budowy dla każdego z tych środowisk pracy. ![Porównanie konstrukcji z użyciem środowisk Część i Projekt Części](images/PartWBvsPartDesignWBexample.jpg )

  scope=\"col\"; style=\"width:50% \| <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> środowisko Projekt Części                                                        scope=\"col\"; style=\"width:50% \| <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> środowisko Część
   
  01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> Stwórz zawartość → <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XZ   01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Szkicownik → <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XZ
  ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                                          ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                                                            

   
  scope=\"col\"; style=\"width:35% \| 02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Wyciągnij przez obrót / Z   scope=\"col\"; style=\"width:35% \| 02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Wyciągnij przez obrót \... / Z
  ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )                                                     ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg )
                                                                                                                                             
   

   
  scope=\"col\"; style=\"width:44% \| 03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XY   scope=\"col\"; style=\"width:44% \| 03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Szkicownik → <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> twórz nowy szkic na płaszczyźnie XY
  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                                                                ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                  
   

   
  scope=\"col\"; style=\"width:35% \| 04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Utwórz kieszeń z wybranego szkicu   scope=\"col\"; style=\"width:35% \| 04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Wyciągnij wybrany szkic
  ![](images/04pocket_PartWBvsPartDesignWBn.jpg )                                                               ![](images/04aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                                                                             
   

   
  scope=\"col\"; style=\"width:35% \|                                            scope=\"col\"; style=\"width:35% \| 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Wytnij
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/04bCut_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  scope=\"col\"; style=\"width:45% \| 05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XZ   scope=\"col\"; style=\"width:45% \| 05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Szkicownik → <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XZ
  ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                                                                  ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                                                                  
   

   
  scope=\"col\"; style=\"width:36% \| 06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> Wyciągnij wybrany szkic symetryczne/XZ   scope=\"col\"; style=\"width:36% \| 06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Wyciągnij wybrany szkic symetryczne/XZ
  ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )                                                            ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                                                                            
   

   
  scope=\"col\"; style=\"width:35% \|                                            scope=\"col\"; style=\"width:35% \| 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Rysunek Roboczy <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Szyk polarny
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  scope=\"col\"; style=\"width:35% \|                                            scope=\"col\"; style=\"width:35% \| 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> Utwórz sumę kilku kształtów
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06cFusion_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  scope=\"col\"; style=\"width:45% \| 07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Utwórz nowy szkic na płaskiej ścianie   scope=\"col\"; style=\"width:45% \| 07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Szkicownik → <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Utwórz nowy szkic na płaszczyźnie XZ
  ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )                                                 ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                                                                   
   

   
  scope=\"col\"; style=\"width:35% \| 08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> Utwórz otwór - pogłębienie walcowe   scope=\"col\"; style=\"width:35% \| 08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Wyciągnij przez obrót \...
  ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg )                                          ![](images/08aRevolve_PartWBvsPartDesignWB.jpg )
                                                                                                                                          
   

   
  scope=\"col\"; style=\"width:35% \|                                            scope=\"col\"; style=\"width:35% \| 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> Rysunek Roboczy <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> szyk polarny
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  scope=\"col\"; style=\"width:3% \| 09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> Utwórz cechę przez szyk kołowy dla otworu i wyciągniecia   scope=\"col\"; style=\"width:3% \| 09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Wytnij
  ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )                                                                   ![](images/09Cut_PartWBvsPartDesignWB.jpg )
                                                                                                                                                                               
   

Porównaj drzewa konstrukcji w obu środowiskach pracy, jak również ich organizację i przeczytaj chronologię:

   
  scope=\"col\"; style=\"width:35% \| 10- Drzewo konstrukcji w środowisku Projekt Części   scope=\"col\"; style=\"width:35% \| 10- Drzewo konstrukcji w środowisku Część
  ![](images/PartvsPartDesign_TreePartDesignWB.jpg )       ![](images/PartvsPartDesign_TreePartWB.jpg )
                                                                                           
   



## Rozważania

Środowiska pracy Część i Projekt Części mogą być używane razem przy zachowaniu pewnej ostrożności, umożliwiając tworzenie dość złożonych modeli.

[Na początek strony](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/pl
