# History/pl
\_\_FORCETOC\_\_

## Początki

<img alt="Wczesny FreeCAD, wersja nieznana" src=images/Screenshot_mesh.jpg  style="width   *300px;"> <img alt="FreeCAD w wersji 0.7 z 2009 roku" src=images/Part_BooleanOperations.png  style="width   *300px;">

## Jak to się wszystko zaczęło 

Początki programu FreeCAD sięgają stycznia 2001 roku, kiedy [Jürgen Riegel](User_Jriegel.md) rozpoczął pracę nad projektem **Cas.CADE**. Cas.CADE był komercyjnym szkieletem programistycznym, który zawierał [jądro modelowania geometrycznego](Glossary#Geometric_modeling_kernel.md) *(lub jądro CAD)*   * został on wydany na licencji open source w 2000 roku i przemianowany na [OpenCASCADE](OpenCASCADE/pl.md). Umożliwiło to realizację otwartego programu CAD 3D, ponieważ zaprogramowanie jądra CAD od podstaw wymagałoby ogromnego nakładu pracy.

Jak mówi Jürgen   *


{{Quote|text=''Projekt FreeCAD został rozpoczęty przeze mnie w styczniu 2001, jako tak zwany GOM (Graphical Object Modeler), z pomysłem użycia Qt, Pythona i Cas.CADE, komercyjnego CAD-Kernel, którego używałem w projektach Daimlera. Cas.CADE stał się open source krótko przed tym, więc wydawało się, że nadszedł właściwy czas, aby spróbować poruszyć się w pustej wówczas przestrzeni open source CAD. Miałem dwuletnie doświadczenie z OpenCascade w projekcie o nazwie QSpect, w którym, pod koniec, byłem głównym projektantem oprogramowania. Nauczyłem się wiele o programowaniu 3D i CAD. Byłem również pod wpływem Catia V5 i jej bardzo specjalnego interfejsu użytkownika i programowania... W marcu 2002, w ramach projektu OpenCascade, zarejestrowałem oprogramowanie jako FreeCAD. Nie mogłem wymyślić lepszej nazwy, jestem bardzo kiepski w nazewnictwie... W kwietniu 2003, Werner Meyer, jeden z kolegów w projekcie QSpect, przeszedł do firmy o nazwie Imetric. Kontakt z Imetric był bardzo obiecujący, ponieważ poszukiwali oni nowej platformy oprogramowania 3D dla swoich czujników 3D. W 2005 roku Imetric przekazał większość swojego modułu Mesh Module do FreeCAD i społeczności Open Source, i od tego czasu używają FreeCAD jako podstawy dla swojego oprogramowania systemu czujników. Od tego czasu Werner Meyer jest bardzo aktywnym deweloperem FreeCAD. W 2005 roku, po roku zmagań, zdecydowałem się pozbyć się szkieletu dokumentów OpenCascade i zastąpić go własną implementacją. Tak więc, ostatecznie używamy tylko jądra CAD OpenCascade, a nie reszty jego frameworka. Rok 2007 był kolejnym interesującym kamieniem milowym. Przeszliśmy na QT4 i, co za tym idzie, na licencję LGPL. W tym czasie wykonaliśmy wiele pracy, głównie Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http   *//forum.freecadweb.org/viewtopic.php?f=8&t=295 Kto stoi za FreeCadem?]''}}

Projekt został ogłoszony publicznie na [Forum OpenCascade](https   *//dev.opencascade.org/forums) w 2003 roku   *


{{Quote|text=''Cześć wszystkim, nazywam się Juergen Riegel i dzisiaj chcę ogłosić projekt OpenCasCade, FreeCAD. Jest to Open Source CAx RAD oparty na OpenCasCade, QT i Pythonie. Posiada kilka kluczowych koncepcji, takich jak nagrywanie makr, środowiska pracy, możliwość działania jako serwer i jako dynamicznie ładowane rozszerzenie aplikacji, i jest zaprojektowany jako niezależny od platformy... Mimo, że jest we wczesnej fazie i nie nadaje się do użytku dla użytkowników ani programistów - pierwsze wydanie dla użytkowników jest planowane na koniec 2003 roku - chciałbym uzyskać kilka opinii na temat kierunku i projektowania FreeCAD. GUI jest prawie skończone i teraz my, mój współtwórca Werner Mayer i ja, zaczęliśmy dodawać pierwsze funkcje CAD. FreeCAD może być postrzegany jako mechaniczny system CAD ogólnego przeznaczenia, ale myślę, że jego pierwszymi odbiorcami będą programiści CAx, którzy potrzebują podstaw do własnego rozwoju''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https   *//dev.opencascade.org/content/announcing-freecad-project Ogłoszenie projektu FreeCAD w niedzielę, 08/17/2003 - 19   *23]''}}

### Werner Mayer 

Werner Mayer dołączył do projektu jak tylko został on ogłoszony jako projekt open source *(przed ogłoszeniem projekt był prywatnym projektem Jürgena)*. Zobacz ten post na forum od Wernera w języku niemieckim   * <https   *//forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Z czasem projekt nabrał rozmachu i dołączyli do niego nowi kluczowi współpracownicy.

-   **Początki Linuksa**


{{Quote|text=''Zabawnym faktem jest to, że chciał mieć oprogramowanie CAD typu otwartoźródłowego głównie dla Linuksa, ponieważ w tamtym czasie nie istniało właściwie nic na tę platformę. Jednakże, od samego początku, przez następne 1,5 roku pracowaliśmy wyłącznie na Windowsie. Potem pewien czeski gość przyczynił się do tego, że kod rdzenia został zbudowany dla Linuksa.   * https   *//github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Pół roku później kontynuowałem tworzenie wersji dla Linuxa   * https   *//github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**P   *** Czy możesz podzielić się tym, jak minęło pierwsze 1,5 roku? Czy spotykaliście się osobiście czy online?


{{Quote|text=''Cóż, w tamtym czasie byliśmy kolegami ''(do 2005 roku)'', więc mogliśmy omawiać sprawy twarzą w twarz. Po tym czasie nadal mieliśmy kilka osobistych spotkań, ale większość rzeczy omawialiśmy przez e-mail lub telefon.''}}


{{Quote|text=''Jako trzeci deweloper dołączył ''' ''Yorik'' ''' pod koniec 2007 roku, ale minęły kolejne 3 lub 4 lata zanim społeczność i liczba współtwórców zaczęła znacząco rosnąć.''}}

**P   *** Czy dzieliliście zadania lub pracowaliście nad konkurencyjnymi implementacjami?


{{Quote|text=''Tak. Jürgen projektował i implementował większość logiki aplikacji i dokumentów, a ja zajmowałem się podstawami GUI.''}}


{{Quote|text=''Nie był to jednak proces stopniowy, ale na początku eksperymentowaliśmy z wieloma rzeczami. Na przykład w początkowej wersji korzystaliśmy ze struktury dokumentów OCC OCAF i jej przeglądarki, ale po roku lub dwóch wpadliśmy w ślepy zaułek, ponieważ dokumentacja dotycząca OCC była bardzo słaba i nie mogliśmy zmusić jej do pracy, aby rozszerzyć OCAF o nasze własne typy elementów. Zdecydowaliśmy się więc wykorzystać tylko możliwości modelowania OCC, ale opracować własne ramy aplikacji / dokumentów.''}}

**P   *** Czy w tamtym czasie myślałeś, że FreeCAD będzie w tym miejscu, w którym jest dzisiaj?


{{Quote|text=''Nie wiedzieliśmy, ale mieliśmy nadzieję. Oczywiście nie mogliśmy przewidzieć, jak dokładnie FreeCAD będzie wyglądał dzisiaj.<br>Najważniejszymi decyzjami projektowymi było udostępnienie go na wszystkich głównych platformach i uczynienie całego SW tak przystępnym, jak to tylko możliwe, tzn. narzucenie wszystkich ważnych funkcji Pythona, tak aby ''(zaawansowani)'' użytkownicy byli w stanie rozszerzyć program FreeCAD o własne funkcje. W ten sposób mieliśmy nadzieję na zdobycie szerokiej rzeszy odbiorców.''}}

*(Zobacz ten post od Wernera na forum [Re   * FreeCAD History](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))*

### Yorik dołącza do projektu 

Użytkownik [Yorik van Havre](User_Yorik.md) dołączył do projektu w 2008 roku i rozpoczął pracę nad [Rysunek Roboczy](Draft_Workbench/pl.md). Do tego momentu nie było możliwości tworzenia geometrii 2D poprzez [GUI](Glossary/pl#GUI.md). Moduł ten został zaprogramowany w całości w środowisku Python, a nie w C++ *(podstawowy język programowania używany w FreeCAD)*. Nowe środowisko pracy Rysunek Roboczy udowodniło, że integracja Pythona jest sukcesem i może być użyta do rozszerzenia lub dostosowania możliwości programu FreeCAD. Oprócz pracy nad środowiskiem Rysunek Roboczy, Yorik pracował nad rozszerzeniem dokumentacji programu FreeCAD i stał się de facto \"dyrektorem artystycznym\" FreeCAD, tworząc wiele ikon dla GUI programu FreeCAD i [definiując jego styl](Artwork/pl.md).

Wersja 0.7 programu FreeCAD wydana w kwietniu 2009 roku była pierwszą, która zawierała moduł Rysunek Techniczny. Moduł Część zapewniał prosty przepływ pracy [CSG](Glossary/pl#Constructive_Solid_Geometry.md) z tworzeniem pierwotnych kształtów i operacjami logicznymi dostępnymi poprzez menu Część. Możliwe było również wytłaczanie profili 2D i zaokrąglanie.

Wersja 0.8 wydana w lipcu 2009 roku zawierała kilka nowych elementów w module Rysunek Roboczy, w tym nowe narzędzie Wymiar. Moduł Część zyskał nowy pasek narzędziowy wraz z nowymi narzędziami, Obrót i Przekrój.

Pod koniec 2009 roku, FreeCAD został zaakceptowany jako pakiet Debiana w repozytoriach Debiana. FreeCAD został dodany do repozytoriów Ubuntu 10.04 w 2010 roku.

### Projekt jest kontynuowany 

Wersja 0.10 została wydana w lipcu 2010 roku i wprowadziła środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md), oparte na Sketchsolve, solverze opartym na wiązaniach do tworzenia geometrii 2D. Pierwsza wersja była ograniczona do tworzenia prostokątów i linii.

Na początku 2011 roku, korzystając z okazji, jaką dała platforma online [Launchpad](https   *//launchpad.net), powstał zespół [FreeCAD Maintainers team](https   *//launchpad.net/~freecad-maintainers), aby dostarczać użytkownikom systemu operacyjnego Ubuntu świeże stabilne wydania wraz z codziennie budowanymi pakietami programu FreeCAD.

Wersja 0.11 została wydana w maju 2011 i wprowadziła nowe narzędzie do projektowania części, które zawierało takie narzędzia jak Wyciągnięcie, Kieszeń, Zaokrąglenie i Fazka. Środowisko robocze Rysunek Roboczy otrzymało ulepszenia i nowe narzędzia, takie jak Linia złożona. Środowisko robocze Robota zawierało więcej narzędzi graficznych.

Wersja 0.12 została wydana w styczniu 2012 i zawierała bardziej kompletne środowisko pracy Szkicownik. Zawierała całkowicie przepisany solver, FreeGCS. Był to rezultat miesięcy pracy głównych programistów FreeCAD wraz z nowicjuszami logari81 *(który zaprogramował solver)* i mrlukeparry. Dodano więcej narzędzi do środowiska pracy Projekt Części.

## Powiększenie zespołu deweloperów rdzenia 

W kwietniu 2019 roku zespół core developerów został powiększony   * Jürgen, Werner i Yorik zostali wsparci przez Abdullaha, Bernda, sliptonic i WandererFan

## Ciekawe posty na forum 

-   o PartDesignNext i innych decyzjach projektowych   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   o historii forum   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   o historii projektu   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   o historii kodu   * <https   *//forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW   * pierwsze sprawdzenie kodu miało miejsce 18 marca 2002 roku (może to data urodzin?)
-   o projekcie, który ma być OpenSource   * <https   *//forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   o historii commitów wydania   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   o tym kto stoi za FreeCAD   * <http   *//forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   o historii MES   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   o historii MES mesher   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>

## Historia wydania 

#### Przegląd

  Version   Nazwa wydania   Data ogłoszenia   Uwagi                                                           Commit wydania                                                                            Gałąź wydania
       
  0.20      ?               w opracowaniu     [Informacje o wydaniu 0.20](Release_notes_0.20.md)      [head master](https   *//github.com/FreeCAD/FreeCAD/commits/master)                          
  0.19      ?               w opracowaniu     [Informacje o wydaniu 0.19](Release_notes_0.19/pl.md)   [head master](https   *//github.com/FreeCAD/FreeCAD/commits/master)                          
  0.18      \-              2019-03-12        [Informacje o wydaniu 0.18](Release_notes_0.18/pl.md)   [release commit 0.18](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland          2018-04-06        [Informacje o wydaniu 0.17](Release_notes_0.17/pl.md)   [release commit 0.17](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-              2016-04-18        [Informacje o wydaniu 0.16](Release_notes_0.16/pl.md)   [release commit 0.16](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-              2015-04-08        [Informacje o wydaniu 0.15](Release_notes_0.15/pl.md)   [release commit 0.15](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-              2014-07-01        [Informacje o wydaniu 0.14](Release_notes_0.14/pl.md)   [release commit 0.14](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-              2013-01-29        [Informacje o wydaniu 0.13](Release_notes_0.13/pl.md)   [release commit 0.13](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12      \-              2011-12-20        [Informacje o wydaniu 0.12](Release_notes_0.12/pl.md)                                                                                             
  0.11      \-              2011-05-03        [Informacje o wydaniu 0.11](Release_notes_0.11/pl.md)                                                                                             
  0.10      \-              2010-07-24                                                                                                                                                                  
  0.9       \-              2010-01-16                                                                                                                                                                  
  0.8       \-              2009-07-10                                                                                                                                                                  
  0.7       \-              2009-04-24                                                                                                                                                                  
  0.6       \-              2007-02-27                                                                                                                                                                  
  0.5       \-              2006-10-05                                                                                                                                                                  
  0.4       \-              2006-01-15                                                                                                                                                                  
  0.3       \-              2005-10-31                                                                                                                                                                  
  0.2       \-              2005-08-09                                                                                                                                                                  
  0.1       \-              2003-01-27                                                                                                                                                                  
  0.0.1     \-              2002-10-29        Pierwsze wysłanie wersji                                                                                                                                  

#### Legenda

  Kolor   Version Type
   
          Przyszłe wydanie
          Najnowsza wersja podglądowa
          **Bieżąca wersja**
          Stara wersja, wciąż wspierana
          Stara wersja
          

## Linki zewnętrzne 

-   [Sekcja plików SourceForge](http   *//sourceforge.net/projects/free-cad/files/)
-   [Sekcja starych plików SourceForge](http   *//sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Ogłoszenie projektu FreeCAD](http   *//www.opencascade.org/org/forum/thread_6572/?forum=11) na forum OpenCascade

[Category   *News](Category_News.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > History/pl
