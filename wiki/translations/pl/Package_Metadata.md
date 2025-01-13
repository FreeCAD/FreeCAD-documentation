# Package Metadata/pl
## Wprowadzenie

Począwszy od wersji 0.20 programu FreeCAD, zewnętrzne dodatki (środowiska pracy, makra i pakiety preferencji) mogą być dystrybuowane z plikiem metadanych opisującym zawartość pakietu. Jeżeli plik \"package.xml\" jest obecny, jest on odczytywany przez FreeCAD i jego zawartość jest wykorzystywana w różnych częściach interfejsu użytkownika. Obecnie jest on opcjonalny dla środowisk pracy i makrodefinicji, a wymagany dla pakietów preferencji. Ta strona dokumentuje format tego pliku metadanych. Format *(i zawartość tej strony Wiki)* są oparte na [REP 149](https://ros.org/reps/rep-0149.html).



## Ogólny format pliku 

Ten dokument opisuje obecnie format pliku w wersji 1.

Plik metadanych musi być prawidłowym, dobrze uformowanym dokumentem XML 1.0. Musi on nosić nazwę \"package.xml\" i musi istnieć w katalogu bazowym głównej gałęzi pakietu oprogramowania *(jak określono w pliku [FreeCAD-addons .gitmodules](https://github.com/FreeCAD/FreeCAD-addons/blob/master/.gitmodules))* w jego repozytorium git. Tylko plik package.xml z głównej gałęzi jest brany pod uwagę przez Menadżera dodatków. Wszystkie zrozumiałe znaczniki XML są pisane małymi literami, ale nierozpoznane znaczniki nie stanowią błędu. Większość znaczników jest opcjonalna, a niektóre mają zastosowanie tylko do niektórych typów zawartości pakietów *(na przykład, tylko środowiska pracy zapewniają obecnie element \"classname\")*. Niepotrzebne lub nierozpoznane elementy są ignorowane.

Każda ścieżka pliku określona w package.xml musi używać ukośnika *(\"/\")* jako separatora katalogu: w systemach, które oczekują innego separatora podczas wykonywania *(np. Windows)* FreeCAD automatycznie przekonwertuje go na prawidłowy separator.



## Elementy zawartości 



### 

Jedynym dozwolonym elementem najwyższego poziomu jest , a plik może zawierać tylko jeden element . Bezpośrednio pod nim znajduje się kilka wymaganych lub opcjonalnych elementów, zdefiniowanych tutaj. Żadne inne znaczniki nie są dozwolone bezpośrednio pod elementem .

    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">

Znacznik  jest unikalnym znacznikiem najwyższego poziomu w pliku package.xml. Wszystkie inne znaczniki są zagnieżdżone pod nim.



#### Atrybuty

-   format=\"NUMBER\": Określenie używanego formatu package.xml. Dla tego interfejsu należy określić format=\"1\".
-   xmlns=\"NAMESPACE\": Określa przestrzeń nazw XML dla tego pakietu i musi być dołączona dokładnie tak, jak pokazano powyżej, jako link do <https://wiki.freecad.org/Package_Metadata>.



#### Wymagane identyfikatory podrzędne 

Element  najwyższego poziomu musi zawierać co najmniej następujące znaczniki:

-   [](#.3Cname.3E.md)
-   [](#.3Cversion.3E.md)
-   [](#.3Cdate.3E.md)
-   [](#.3Cdescription.3E.md)
-   [](#.3Cmaintainer.3E.md) *(wiele, ale co najmniej jeden)*
-   [](#.3Clicense.3E.md) *(wiele, ale co najmniej jeden)*
-   [](#.3Cicon.3E.md)
-   [](#.3Ccontent.3E.md) *(element kontenera dla elementów zawartości pakietu)*



#### Opcjonalne identyfikatory podrzędne 

-   [](#.3Curl.3E.md) *(wiele)*
-   [](#.3Cauthor.3E.md) *(wiele)*
-   [](#.3Cdepend.3E.md) *(wiele)*
-   [](#.3Cconflict.3E.md) *(wiele)*
-   [](#.3Creplace.3E.md) *(wiele)*
-   [](#.3Ctag.3E.md) *(wiele)*
-   [](#.3Cfreecadmin.3E.md)
-   [](#.3Cfreecadmax.3E.md)
-   [](#.3Cpythonmin.3E.md)



###  

WYMAGANE

Nazwa tego pakietu. Musi zawierać tylko znaki, które są prawidłowe dla nazw plików *(niedozwolone znaki to /\\?%\*:\|\"\<\> )*.



###  

WYMAGANE

Numer wersji zgodny ze standardem [semantic versioning 2.0](https://semver.org) (np. 1.0.2-beta) lub [CalVer style](https://calver.org/) (np. 2021.12.08). Należy pamiętać, że nie można dołączyć obu typów, a przełączanie między typami nie jest obsługiwane. Wewnętrznie kod nie ma pojęcia, który typ został wybrany, podczas porównywania wersji wykonuje proste porównanie numeryczne między każdym kolejnym składnikiem numerycznym, niezależnie od typu. Należy pamiętać, że nie można pozostawić tego pola pustego, należy przypisać jakiś numer wersji. Gdy Menedżer dodatków wykryje podwyższenie numeru wersji, wyświetli użytkownikom informację \"dostępna aktualizacja\".



###  

WYMAGANE

Data bieżącej wersji, w formacie RRRR-MM-DD lub RRRR.MM.DD.



###  

WYMAGANE

Zwięzły *(do kilku zdań)* tekstowy opis tego pakietu. Nie są obsługiwane żadne znaczniki.



###  

CO NAJMNIEJ JEDEN WYMAGANY *(dopuszczalna jest większa liczba)*

Imię i nazwisko osoby opiekującej się pakietem. Wszystkie pakiety wymagają opiekuna. Dla osieroconych pakietów patrz uwagi poniżej.



#### Atrybuty 

-   email=\"name@domain.tld\" *(wymagane)*: Adres e-mail opiekuna.

Osierocony pakiet to taki, który nie ma aktualnego opiekuna. Osierocone pakiety powinny używać następujących informacji o opiekunie:

    <maintainer email="no-one@freecad.org">No current maintainer</maintainer>



###  

CO NAJMNIEJ JEDEN WYMAGANY *(dopuszczalna jest większa liczba)*

Skrócony identyfikator SPDX licencji dla tego pakietu, np. BSD-2-Clause, PL-3.0 lub nowszy, LGPL-2.1 lub nowszy. W celu ułatwienia odczytu maszynowego, należy dołączyć tylko krótki identyfikator SPDX licencji *(patrz [strona SPDX](https://spdx.org/licenses/))*. W przypadku wielu licencji należy użyć wielu oddzielnych znaczników. Pakiet będzie miał wiele licencji, jeśli różne pliki źródłowe mają różne licencje. Każda licencja występująca w plikach źródłowych powinna mieć odpowiedni znacznik . W przypadku tekstu objaśniającego zastrzeżenia licencyjne należy użyć znacznika . Aby określić, że nie ma zastosowania żadna licencja *(np. \"Wszystkie prawa zastrzeżone.\")*, należy ustawić tę wartość na \"UNLICENSED\". Aby określić niestandardową licencję bez identyfikatora SPDX, należy ustawić tę wartość na \"SEE LICENSE IN \".

Powszechnie używane ciągi nazw licencji:

-    `"Apache-2.0"`
    

-    `"BSD-2-Clause"`
    

-    `"BSD-3-Clause"`
    

-    `"BSL-1.0"`
    

-    `"GPL-2.0-or-later"`
    

-    `"GPL-3.0-or-later"`
    

-    `"LGPL-2.1-or-later"`
    

-    `"LGPL-3.0-or-later"`
    

-    `"MIT"`
    

-    `"MPL-1.1"`
    

-    `"CC0-1.0"`*(Dedykacja domeny publicznej)*

**Uwaga dotycząca kompatybilności wstecznej**: Menedżer dodatków będzie próbował znormalizować identyfikatory licencji, które nie są dokładnie zgodne z ciągiem licencyjnym SPDX. Czasami będzie to skutkować identyfikatorem licencji, który daje licencję inną niż FSF-Libre lub niezatwierdzoną przez OSI: na przykład \"LGPL2\" zostanie znormalizowana do \"LGPL-2.0\", która jest licencją inną niż FSF-Libre: prawdopodobnie chodziło o \"LGPL-2. lub nowszą\".



#### Atrybuty 

-    `file<nowiki>=</nowiki>"FILE"`*(opcjonalnie)*: Ścieżka do pliku `package.xml` zawierającego pełny tekst licencji. Wiele licencji wymaga dołączenia tekstu licencji podczas redystrybucji oprogramowania. Np. Licencja Apache, wersja 2.0 stwierdza w paragrafie 4.1: \"Musisz przekazać każdemu innemu odbiorcy Utworu lub Utworów Pochodnych kopię niniejszej Licencji\".



###  

WYMAGANE

Znacznik  opisuje rzeczywistą zawartość pakietu. Nie posiada atrybutów i zawiera dowolną liczbę elementów podrzędnych. Te elementy podrzędne mogą mieć dowolne nazwy znaczników, z których tylko niektóre mogą być rozpoznawane przez FreeCAD. FreeCAD obsługuje obecnie elementy \"workbench\", \"macro\" i \"preferencepack\". Każdy element potomny jest następnie definiowany rekurencyjnie przez ten standard, zawierający dowolne lub wszystkie elementy dozwolone dla węzła głównego . Na przykład:

    <content>
      <preferencepack>
        <name>Unicorn Sparkles Theme</name>
        <version>1.0.0</version>
        <url type="readme">https://github.com/chennes/FreeCAD-themes/blob/main/Unicorn%20Sparkles%20Theme/Readme.md</url>
        <icon>sparkles.svg</icon>
      </preferencepack>
    </content>

Istnienie elementów  implikuje zestaw podfolderów, po jednym dla każdego elementu zawartości, nazwanych dokładnie tak, jak dana nazwa elementu. Tak więc w powyższym przykładzie struktura folderów pakietu jest następująca:

    Package Directory/
      package.xml
      Unicorn Sparkles Theme/
        Unicorn Sparkles Theme.cfg
        sparkles.svg
        (the theme's other files)

Oprócz innych elementów , elementy zawartości mogą opcjonalnie dostarczać informacji w identyfikatorach ,  i  *(technicznie mogą one być również dostarczane do głównego identyfikatora , ale generalnie nie są tam używane)*.

**Uwaga dotycząca kompatybilności wstecznej**: aby uniknąć konieczności restrukturyzacji pakietów sprzed tego standardu metadanych, opcjonalny identyfikator [](#.3Csubdirectory.3E.md) może określać \"./\" jako podkatalog dla elementu zawartości, w którym to przypadku nie jest wymagany żaden inny katalog podrzędny. Odpowiada to systemowi sprzed standardu, w którym pojedynczy obszar roboczy znajdował się na szczycie struktury katalogów.



####  

WYMAGANE dla środowisk pracy

Ścieżka do pliku ikony. Jeśli jest to ikona dla pakietu najwyższego poziomu, ścieżka jest względna do samego pliku package.xml. Jeśli ikona jest elementem elementu , ścieżka jest względna do folderu zawartości. Menedżer dodatków wyświetli ikonę najwyższego poziomu jako ikonę całego pakietu. Jeśli nie ma ikony najwyższego poziomu, pierwsza określona ikona środowiska pracy zostanie użyta jako ikona pakietu.



####  

Opcjonalnie.

Zwykle zakłada się, że element zawartości znajduje się w podkatalogu o tej samej nazwie co element. W niektórych przypadkach przydatne jest jednak wyraźne określenie podkatalogu. Na przykład, wiele makr może znajdować się w jednym podkatalogu, ale każde z nich ma swój własny wpis w pliku package.xml. Zapewnia również wsparcie kompatybilności wstecznej dla pakietów, które poprzedzają specyfikację formatu pliku package.xml i nie są zgodne z oczekiwaną strukturą podkatalogów. Często w takich przypadkach używa się zapisu \"./\", aby wskazać, że element w ogóle nie znajduje się w katalogu podrzędnym.



####  

WYMAGANE dla środowisk pracy

W przypadku środowisk pracy, nazwa głównej klasy wejściowej Python. Jest to klasa, którą FreeCAD będzie próbował załadować podczas uruchamiania, aby zlokalizować ikonę stołu warsztatowego, która powinna być ustawiona jako zmienna członkowska klasy. Na przykład, jeśli stół warsztatowy definiuje następującą klasę *(zwykle w InitGui.py)*:


```python
class MyNewWB:
    Icon = "resources/icon.svg"
```

wtedy plik package.xml oczekuje:

    <classname>MyNewWB</classname>



####  

Opcjonalnie

Dla wygody innych narzędzi można tu wymienić dowolną liczbę innych plików. Ich użycie zależy od typu zawartości. W elemencie zawartości makra każdy wpis pliku jest pojedynczym makrem i zostanie połączony z katalogiem instalacyjnym makrodefinicji użytkownika przez [Menedżera dodatków](Std_AddonMgr/pl.md).



###  

Dozwolonych jest wiele typów: \"repozytorium\" jest wymagane, a typ \"readme\" jest wysoce zalecany.

Ujednolicony lokalizator zasobów *(**U**niform **R**esource **L**ocator)* dla strony internetowej pakietu, narzędzia do śledzenia błędów, repozytorium źródłowego, linku do pobrania pliku zip, pliku readme lub dokumentacji *(zgodnie z atrybutem \"type\", patrz poniżej)*.

Określając typ \"readme\", należy podać bezpośredni link do renderowanej wersji README. Na przykład na GitHub jest to link typu \"blob\", taki jak \"<https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md>\" lub na instancji GitLab \"<https://gitlab.com/opensimproject/cfdof/-/blob/master/README.md>\" *(zwróć uwagę na nieco inny format adresu URL między tymi wersjami)*.

Dobrym pomysłem jest dołączenie znaczników  kierujących użytkowników do zasobów online pakietu. Zazwyczaj jest to strona wiki na wiki.freecad.org, gdzie użytkownicy mogą na przykład znaleźć i zaktualizować informacje o pakiecie. Menedżer dodatków wymienia te adresy URL i zapewnia klikalne linki do nich w opisie pakietu.



#### Atrybuty 

-   type=\"TYPE\" (wymagane): Typ powinien być jednym z następujących identyfikatorów: \"website\", \"bugtracker\", \"repository\", \"readme\", \"documentation\", lub \"discussion\".
-   branch=\"BRANCH\" *(wymagane dla type=\"repository\")*: Nazwa gałęzi do sprawdzenia w celu uzyskania tego pakietu. Zazwyczaj jest to nazwa głównej gałęzi rozwojowej. Może również określać dowolny inny typ odniesienia git, np. identyfikator lub konkretny commit.



###  

Dozwolona jest wielokrotność

Imię i nazwisko osoby, która jest autorem pakietu, jako potwierdzenie jej pracy i w przypadku pytań.



#### Atrybuty 

-   email=\"name@domain.tld\" *(opcjonalnie)*: Adres e-mail autora.



###  

Dozwolona jest wielokrotność

Deklaruje zależność od innego dodatku FreeCAD lub wewnętrznego środowiska pracy, lub pakietu Python. Nazwana zależność jest najpierw sprawdzana względem listy znanych dodatków *(np. tych dostępnych w oficjalnym repozytorium git FreeCAD Addons lub tych w niestandardowym repozytorium określonym przez użytkownika)*. Sprawdzana jest kanoniczna nazwa dodatku. Jeśli plik package.xml jest obecny dla tego dodatku, nazwa jest elementem  tego pakietu. Wymagane jest dokładne dopasowanie. Jeśli nie zostanie znalezione żadne dopasowanie, sprawdzana jest lista znanych wewnętrznych środowisk pracy *(zarówno zainstalowanych, jak i odinstalowanych)*. Wreszcie, jeśli nazwana zależność nie została zlokalizowana w poprzednich dwóch krokach, zakłada się, że jest to zależność pakietu Python. Należy pamiętać, że nie wszystkie funkcje związane z zależnościami są jeszcze w pełni zaimplementowane.



#### Atrybuty 

Wszystkie zależności i relacje mogą ograniczać ich zastosowanie do określonych wersji. Dla każdego operatora porównania można użyć atrybutu. Dwa z tych atrybutów mogą być użyte razem do opisania zakresu wersji.

-   version_lt=\"VERSION\" *(opcjonalnie)*: Zależność od pakietu jest ograniczona do wersji mniejszych niż podany numer wersji.
-   version_lte=\"VERSION\" *(opcjonalne)*: Zależność od pakietu jest ograniczona do wersji mniejszych lub równych podanemu numerowi wersji.
-   version_eq=\"VERSION\" *(opcjonalne)*: Zależność od pakietu jest ograniczona do wersji równej podanemu numerowi wersji.
-   version_gte=\"VERSION\" *(opcjonalne)*: Zależność od pakietu jest ograniczona do wersji większych lub równych podanemu numerowi wersji.
-   version_gt=\"VERSION\" *(opcjonalne)*: Zależność od pakietu jest ograniczona do wersji większych niż podany numer wersji.
-   condition=\"CONDITION_EXPRESSION\": Każda zależność może być uzależniona od wyrażenia warunku. Jeśli wyrażenie warunku ma wartość \"true\", zależność jest używana i traktowana tak, jakby nie miała atrybutu warunku. Jeśli wyrażenie warunku ma wartość \"false\", zależność jest ignorowana i traktowana tak, jakby nie istniała. Wyrażenie musi być prawidłowym wyrażeniem FreeCAD (tj. składnią Pythona) i może odnosić się do zmiennych \"\$BuildVersionMajor\", \"\$BuildVersionMinor\" i \"\$BuildRevision\" reprezentujących aktualnie uruchomioną wersję FreeCAD.
-   optional=\"true\|false\": Jeśli \"optional\" ma wartość \"true\", wówczas zależność jest traktowana jako opcjonalna, gdy dodatek jest instalowany za pomocą Menedżera dodatków. Ogólnie oznacza to, że niepowodzenie instalacji zależności nie uniemożliwia instalacji dodatku, a użytkownik może zostać zapytany, czy chce go zainstalować. Wersje FreeCAD wcześniejsze niż 0.21 nie rozpoznają tego atrybutu i będą go ignorować.
-   type=\"automatic\|addon\|internal\|python\": Opcjonalny, domyślnie \"automatyczny\". Wskazuje, do czego odnosi się ta instrukcja zależności. \"addon\" dotyczy dodatków zewnętrznych, \"internal\" dotyczy wewnętrznych środowisk pracy *(np. \"arch\", \"sketcher\" itp.)*, a \"python\" wskazuje na zależność od pakietu Python. Wersje FreeCAD wcześniejsze niż 0.21 nie używają tego atrybutu, a \"automatic\" jest zawsze zakładany.



###  

Dozwolona jest wielokrotność

Deklaruje nazwę pakietu, z którym ten pakiet jest w konflikcie. Ten pakiet i pakiet będący w konflikcie nie powinny być instalowane w tym samym czasie.



#### Atrybuty 

Zobacz .



###  

Dozwolona jest wielokrotność

Deklaruje nazwę pakietu, który ten pakiet ma zastąpić.



#### Atrybuty 

Zobacz .



###  

Prosty identyfikator tekstowy używany do kategoryzacji podczas korzystania z menedżera pakietów. Można określić wiele elementów .



###  

Minimalna wersja FreeCAD wymagana do korzystania z tego pakietu / elementu, jako ciąg semantyczny wersji 2.0 w formacie MAJOR.MINOR.BUILD



###  

Maksymalna wersja FreeCAD wymagana do korzystania z pakietu / elementu, jako ciąg semantyczny wersji 2.0 w formacie MAJOR.MINOR.BUILD



###  

*(Nowość w FreeCAD 0.21, ignorowana przez poprzednie wersje.)* Minimalna wersja środowiska Python wymagana do użycia pakietu/elementu, jako ciąg semantyczny wersji 2.0 w formacie MAJOR.MINOR. Menedżer dodatków nie zezwoli na zainstalowanie dodatku w systemie z wersją Python wcześniejszą niż ta. Obsługiwane są tylko wersje Python 3.x. Chociaż można określić wersję trójskładnikową, tylko numer minor jest brany pod uwagę podczas sprawdzania zgodności.



## Sprawdzanie poprawności 

Aby zweryfikować plik package.xml, możesz włączyć \"tryb deweloperski\" w menedżerze dodatków: utwórz zmienną logiczną o nazwie \"developerMode\" w grupie parametrów \"Addons\" i ustaw ją na True: **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Addons → developerMode**. Gdy menedżer dodatków zakończy odczytywanie bazy danych dodatków, sprawdzi wszystkie dostępne pliki package.xml pod kątem błędów.



## Krótki przewodnik 

Aby uzyskać krótki przewodnik na temat tworzenia podstawowego pliku package.xml i dodawania środowiska roboczego do [Menedżera dodatków](Std_AddonMgr/pl.md), zobacz stronę [Dodaj środowisko pracy do Menadżera dodatków](Add_Workbench_to_Addon_Manager/pl.md).



## Przykłady

Należy pamiętać, że komentarze *(tekst pomiędzy `&lt;&#33;--` i `--&gt;`)* są ignorowane przez parser XML i nie są wymaganą częścią formatu pliku. Są one podane tutaj w celach informacyjnych i mogą zostać pominięte w ostatecznym pliku package.xml, jeśli jest to pożądane.

Prosty pakiet tylko dla środowiska pracy *(na przykład, aby dodać plik metadanych do pakietu, który poprzedza ten format metadanych)*:

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Legacy Workbench</name> 
      <description>Text that the Addon Manager shows for the Addon. Any length, but remember that Addon Manager's compact view only shows the first sentence or so.</description>
      <version>1.0.1</version> 
      <date>2022-01-07</date> 
      <maintainer email="your_address@null.com">Your Name</maintainer>
      <license file="LICENSE">LGPL-2.1-or-later</license> 
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url> 
      <url type="readme">https://github.com/chennes/FreeCAD-Package/blob/main/README.md</url> 
      <icon>Resources/icons/PackageIcon.svg</icon> 

      <content>
        <workbench>
          <classname>MyLegacyWorkbench</classname> 
          <subdirectory>./</subdirectory>
        </workbench>
      </content>

    </package>

Złożony, wieloskładnikowy pakiet:

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Example Package Format</name>
      <description>An example of the package.xml file format</description>
      <version>2022.01</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3.0-or-later</license>
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <preferencepack>
          <name>FreeCAD Classic Colors</name>
          <description>FreeCAD default colors for core app and included Mods.</description>
          <version>1.0.0</version>
          <tag>color</tag>
          <tag>stylesheet</tag>
        </preferencepack>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>
          <version>0.9.0-alpha</version>
        </workbench>
        <macro>
          <name>Problem Solver 9000</name>
          <description>Deletes all emails in your inbox</description>
          <subdirectory>./</subdirectory>
          <file>PS9000.FCMacro</file>
        </macro>
      </content>

    </package>

Pakiet wraz z zależnościami:

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>Example with Dependencies</name>
      <description>An example of the package.xml file format</description>
      <version>1.0.1-beta3</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3.0-or-later</license>
      <url type="repository" branch="main">https://github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>

          <depend>FEM</depend>
          <depend version_gte="0.3.0">Curves workbench</depend>
          <depend version_gte="3.3" version_lt="4">Steel column</depend>

          
          <depend optional="true" type="python">markdown</depend>
          <depend type="addon">TabBar</depend>

          
          <replace>Metadata Creation Workbench Beta</replace>

          
          <conflict condition="$BuildRevision==24267">Do not use with build 24267</conflict> 

          
          <depend>matplotlib</depend>
          <depend>some_other_package</depend> 
        </workbench>
      </content>

    </package>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Package Metadata/pl
