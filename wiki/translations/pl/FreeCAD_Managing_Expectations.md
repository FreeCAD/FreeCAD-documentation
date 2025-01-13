# FreeCAD Managing Expectations/pl
**Chociaż witamy i zachęcamy do rozwoju i uczestnictwa wśród społeczności, żądania, emocjonalne tyrady i dzikie roszczenia są ogólnie słabo odbierane, ponieważ nasza społeczność składa się z wielu doświadczonych i pełnych pasji zwolenników FreeCAD, którzy wielokrotnie słyszeli podobne oświadczenia. Jeśli zauważysz brak jakiejś funkcji lub coś, co Cię denerwuje, gorąco zachęcamy do rozważenia zaangażowania się w sam kod. FreeCAD jest w dużej mierze rozwijany przez stosunkowo niewielką grupę utalentowanych ludzi, którzy mają pracę dzienną, rodziny i inne zainteresowania poza programowaniem na żądanie. Jeśli masz umiejętności ''(Python / C++)'' i motywację do udziału, Twój wkład może sprawić, że FreeCAD będzie jeszcze lepszy niż obecnie. Możesz znaleźć śledzone błędy / prośby o funkcje na stronie [https://github.com/FreeCAD/FreeCAD/issues zgłoszenia].**






## Przeznaczenie

Ta strona wiki jest przeznaczona dla nowych użytkowników programu FreeCAD odchodzących z innych rozwiązań CAD / CAM.



## Słowo wstępne 

Wielu hobbystów, niezależnych projektantów i małych firm często szuka schronienia przed wysokimi kosztami i ograniczeniami licencyjnymi komercyjnego oprogramowania, a może po prostu wybierasz FreeCAD, ponieważ wierzysz w filozofię stojącą za [FOSS](https://en.wikipedia.org/wiki/FOSS). W każdym z tych przypadków, WITAMY! Jest wielu użytkowników, tak jak Ty, którzy z powodzeniem przeszli na FreeCAD dla swoich osobistych i zawodowych potrzeb. Ta strona wiki jest zaprojektowana aby pomóc Ci w osiągnięciu sukcesu i ustalić realistyczne oczekiwania podczas nurkowania w *FreeCAD Way*, który najprawdopodobniej różni się od tego do czego przywykłeś w innych popularnych programach CAD.



## Czego mogę się spodziewać? 

W swoim rdzeniu FreeCAD jest modelerem parametrycznym. Wykorzystuje koncepcję środowisk pracy, gdzie każde środowisko jest odpowiedzialne za konkretne zadania i funkcje. Jako taki może być używany do wielu celów. Jest aktywnie wykorzystywany w produkcji i dość stabilny. Jednak, jak każdy inny program CAD, FreeCAD nie jest w 100% stabilny.

W swoim rdzeniu FreeCAD jest potężnym modelerem parametrycznym. Wykorzystuje on modułową koncepcję *środowisk pracy*, gdzie każde z nich odpowiada za określone zadania i funkcje. Koncepcja ta jest bardzo elastyczna i może być z powodzeniem wykorzystywana do wielu celów. FreeCAD jest aktywnie rozwijany, używany w produkcji i dość stabilny, ale jak każdy inny program CAD, nie jest stabilny w 100%.

Pochodząc z innego programu CAD możesz uznać terminologię, strukturę i organizację FreeCADa za nieco obcą. Prawdopodobnie będziesz musiał dokonać pewnych dostosowań w swoich przepływach pracy, nauczyć się funkcjonalnych obejść lub wykorzystać nasz potężny ekosystem [makrodefinicji](Macros.md), ale w większości przypadków będziesz w stanie osiągnąć to, co chcesz. A jeśli potrzebujesz pomocy: mamy bardzo aktywne i responsywne [forum](https://forum.freecad.org/index.php) chętne do pomocy. Wśród członków forum na pewno są (byli) użytkownicy twojego obecnego programu CAD. Nie wahaj się więc skorzystać z tych zasobów.



## Jak mogę pomóc? 

Jest wiele sposobów: możesz dokonać [wpłaty](Donate/pl.md), pomóc w pytaniach na [forum](https://forum.freecad.org/index.php), albo napisać dokumentację lub kod. Zobacz [Pomoc FreeCAD](Help_FreeCAD/pl.md).



## Zasoby dydaktyczne 



### Oficjalne

-   [To Wiki](Main_Page/pl.md)
-   [Forum Pomocy](https://forum.freecadweb.org/viewforum.php?f=3)
-   [Obejścia znanych problemów](Workarounds/pl.md)



### Nieoficjalne

Następujące kanały YouTube mają dość dobrej jakości treści skupione wokół programu FreeCAD (zaleca się ignorowanie wszelkich tutoriali opartych na wersji 0.17 lub wcześniejszej):

-   *MangoJelly Solutions* (kilka list odtwarzana dla początkujących, średnio-zaawansowanych i zaawansowanych użytkowników)
-   *Joko EngineeringHelp* (filmy dla średnio-zaawansowanych)
-   *Brodie Fairhall* (kilka filmów pomagających użytkownikom Fusion 360 w przejściu na FreeCAD)
-   I więcej\...



## Pytania i ospowiedzi 



### \"Czy FreeCAD może XYZ?\" 

FreeCAD ma już możliwość wykonywania następujących typów prac:

-   Modelowanie parametryczne oparte na splajnie z wykorzystaniem środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) i [Szkicownik](Sketcher_Workbench/pl.md).
-   Modelowanie [Powierzchnii 3D](Surface_Workbench/pl.md) / [Krzywych](Curves_Workbench/pl.md) z wykorzystaniem NURBS.
-   Import / modyfikacja [Siatek](Mesh_Workbench/pl.md).
-   Symulacja złożeń *(aktywnie rozwijane są 3 różne podejścia, [A2+](A2plus_Workbench/pl.md), [ASM3](Assembly3_Workbench/pl.md) i [ASM4](Assembly4_Workbench/pl.md))*.
-   Projektowanie [BIM](BIM_Workbench/pl.md).
-   Analiza naprężeń *([MES](FEM_Workbench/pl.md))*.
-   Obliczeniowa mechanika płynów *([CFD](Cfd_Workbench/pl.md))*.
-   [Rysunek Techniczny](TechDraw_Workbench/pl.md) / [Rysunek Roboczy](Draft_Workbench/pl.md).
-   Oraz więcej [podstawowych](Workbenches/pl.md) i [zewnętrznych](External_workbenches/pl.md) środowisk pracy\...



### \"Interfejs użytkownika (UI/UX) jest brzydki, dziwny, niezrozumiały lub nie taki jak w programie XYZ!\" 

FreeCAD pozwala na [rozległe dostosowanie](Interface_Customization/pl.md) interfejsu użytkownika. Zdajemy sobie sprawę, że domyślne kolory i rozmieszczenie elementów może nie być przyjemne dla każdego, ale zachęcamy do dostosowania go do własnych specyficznych potrzeb i organizacji pracy. Jeśli uważasz, że udało Ci się wymyślić mogący zdobyć popularność układ/temat/pasek narzędzi itp. zachęcamy do skorzystania z niedawno dodanej funkcji [Paczki Preferencji](Preference_Packs/pl.md) i podzielenia się nią ze społecznością. Być może Twoje wysiłki pomogą komuś innemu w przejściu na FreeCAD. Oprogramowanie FOSS rozwija się dzięki wkładom społeczności wszelkiego rodzaju i jest to częsty temat dyskusji.



### \"Dlaczego ta funkcja nie działa jak w programie XYZ?\" 

FreeCAD ma rodowód rozwojowy sięgający ponad [20 lat](History/pl.md). Funkcje i zachowania są intensywnie recenzowane, omawiane i oceniane zanim zostaną dodane lub zmienione. Miej otwarty umysł, podczas gdy może to nie być oczywiste, prawdopodobnie istnieje bardzo dobre uzasadnienie dla takich rzeczy. Nie oznacza to, że FreeCAD jest doskonały, ale proszę weź pod uwagę, że to do czego przywykłeś może nie być jedynym lub najlepszym sposobem na zrobienie czegoś.



### \"Nie mogę zrozumieć organizacji pracy w programie FreeCAD!\" 

FreeCAD ma filozofię niedyktowania \"jak\" go używać. Zamiast tego dostarcza narzędzia i szeroki wachlarz opcji, który \"możesz\" wykorzystać. Oznacza to dwie rzeczy. Po pierwsze, oprogramowanie nie będzie koniecznie \"prowadzić\" lub \"kierować\" Cię w stronę określonego stylu lub organizacji pracy. Po drugie, oznacza to, że możesz eksperymentować z narzędziami i znaleźć to, co działa najlepiej dla Ciebie. Nie oznacza to, że nie ma ogólnych [\"dobrych praktyk\"](Feature_editing/pl.md) do uwzględnienia podczas używania programu FreeCAD, ale te najlepsze praktyki generalnie dotyczą każdego profesjonalnego oprogramowania do projektowania gdy tworzone są stabilne modele.



### \"O co chodzi z tymi wszystkimi środowiskami pracy?\" 

Jedną z potężnych cech FreeCAD jest jego modularność. Jest to możliwe dzięki podzieleniu rozwoju narzędzi na środowiska pracy. Kiedy już zapoznasz się z dostarczonymi narzędziami, mogą one często działać synergicznie, aby tworzyć bardzo złożone i zaawansowane modele. Doskonałą analogią jest to, że FreeCAD ma strukturę podobną do szafki narzędziowej mechanika, a każdy środowisko pracy jest szufladą z określonymi narzędziami. Możesz użyć tych narzędzi do zbudowania samochodu, ale to do mechanika należy zrozumienie jak ich użyć aby osiągnąć swój cel.



### \"FreeCAD jest fundamentalnie zepsuty, moje modele się rozwalają!\" 

FreeCAD jest zbudowany wokół otwartego Kernela Modelowania Geometrycznego nazwanego \"[OpenCascade Technology](OpenCASCADE/pl.md)\" *(lub OCC)*. Jest to najbardziej bogate w funkcje i dojrzałe dostępne jądro modelowania open source. Posiada jednak błędy, dziwactwa i ograniczenia. Jeden z nich jest określany [\"Problemem Nazewnictwa Topologicznego\"](Topological_naming_problem/pl.md) *(lub TNP)*. Za każdym razem, gdy model jest modyfikowany, wewnętrzne nazwy powierzchni i krawędzi są zmieniane przez kernel, powodując niepożądane zachowanie dla wszystkich cech modelu, które się do nich odwołują. Obecny cykl rozwoju skupia się na implementacji algorytmu nazewnictwa zaprojektowanego tak, aby zminimalizować ten efekt w większości przypadków. Należy jednak pamiętać, że minimalizacja TNP nie jest zamiennikiem dla [dobrych praktyk i technik modelowania](Feature_editing/pl.md).



### Kernel OpenCascade 

OpenCascade *(OCC / OCCT)* jest podstawową zewnętrzną zależnością jądra CAD, od której FreeCAD jest całkowicie zależny. Istnieje wiele otwartych błędów \"upstream\", które społeczność FreeCAD zidentyfikowała i śledzi w odniesieniu do OCC. Śledzimy je poprzez:

-   [Bugtracker](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3A%223rd+Party%3A+OCC%22)
-   [Błędy OCC w Bugtrackerze *(wątek na forum)*](https://forum.freecad.org/viewtopic.php?t=20264)



## Odnośniki internetowe 

-   [Dyskusja: FreeCAD nie jest gotowy na 1.0 (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=8&t=43461)
-   [Why the GIMP Team Obviously\* Hates You (\*We Actually Love You. \*\*Mostly)](https://www.youtube.com/watch?v=JBmdbipkbrk) Pat David z prezentacji zespołu GIMP na SCaLE16x California 2016 r.
-   [Earning Your Support Instead of Buying it: A How-to Guide to Open Source Assistance](https://vimeo.com/144089061) autorstwa [Iana Turtona](https://twitter.com/ijturton) na FOSS4G Seul 2015



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > FreeCAD Managing Expectations/pl
