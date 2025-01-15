# Doxygen/pl
## Informacje o 




Doxygen jest popularnym narzędziem do generowania dokumentacji z adnotacji w źródłach C++; obsługuje również inne popularne języki programowania, takie jak C#, PHP, Java i Python. Odwiedź stronę [Doxygen](http://www.doxygen.nl/), aby dowiedzieć się więcej o systemie, i zapoznaj się z [Podręcznikiem Doxygen](http://www.doxygen.nl/manual/index.html), aby uzyskać pełne informacje.



## Doxygen i FreeCAD 

Niniejszy dokument zawiera krótkie wprowadzenie do Doxygen, w szczególności w jaki sposób jest on używany w FreeCAD do dokumentowania jego źródeł. Odwiedź stronę [Dokumentacja źródeł](Source_documentation/pl.md), aby uzyskać instrukcje dotyczące tworzenia dokumentacji FreeCAD, która jest również dostępna online na witrynie [FreeCAD API](https://www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Ogólny przepływ pracy do tworzenia dokumentacji kodu źródłowego za pomocą Doxygen.*



## Doxygen z kodem C++ 

Sekcja [Pierwsze kroki *(Krok 3)*](http://www.doxygen.nl/manual/starting.html) podręcznika Doxygen wspomina o podstawowych sposobach dokumentowania źródeł.

W przypadku członków, klas i przestrzeni nazw istnieją zasadniczo dwie opcje:

1.  Umieścić specjalny \"blok dokumentacji\" *(skomentowany akapit)* przed deklaracją lub definicją funkcji, członka, klasy lub przestrzeni nazw. W przypadku członków *(zmiennych)* plików, klas i przestrzeni nazw dozwolone jest również umieszczenie dokumentacji bezpośrednio po członie. Zobacz sekcję [Specjalne bloki komentarzy](http://www.doxygen.nl/manual/docblocks.html#specialblock) w podręczniku, aby dowiedzieć się więcej o tych blokach.
2.  Umieść specjalny blok dokumentacji w innym miejscu *(inny plik lub inna lokalizacja w tym samym pliku)* i umieść \"polecenie strukturalne\" w bloku dokumentacji. Polecenie strukturalne łączy blok dokumentacji z pewną jednostką, która może być dokumentowana (funkcja, element członkowski, zmienna, klasa, przestrzeń nazw lub plik). Zobacz sekcję [Dokumentacja w innych miejscach](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) w podręczniku, aby dowiedzieć się więcej o poleceniach strukturalnych.

Uwaga:

-   Zaletą pierwszej opcji jest to, że nie trzeba powtarzać nazwy encji (funkcji, członka, zmiennej, klasy lub przestrzeni nazw), ponieważ Doxygen przeanalizuje kod i wyodrębni odpowiednie informacje.
-   Pliki mogą być dokumentowane tylko przy użyciu drugiej opcji, ponieważ nie ma możliwości umieszczenia bloku dokumentacji przed plikiem. Oczywiście członkowie pliku *(funkcje, zmienne, definicje typów, definicje)* nie potrzebują wyraźnego polecenia strukturalnego. Po prostu umieszczenie bloku dokumentacji przed lub po nich będzie działać dobrze.



### Styl pierwszy: blok dokumentacji przed kodem 

Zazwyczaj warto dokumentować kod w pliku nagłówkowym, tuż przed deklaracją klasy lub prototypem funkcji. Dzięki temu deklaracja i dokumentacja są blisko siebie, więc łatwo jest zaktualizować tę drugą, jeśli pierwsza ulegnie zmianie.

Specjalny blok dokumentacji zaczyna się jak komentarz w stylu C `/*`, ale ma dodatkową gwiazdkę, więc `/**`; blok kończy się pasującym `*/`. Alternatywą jest użycie komentarzy w stylu C++ `//` z dodatkowym ukośnikiem, więc `//`. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



### Styl drugi: blok dokumentacji w innym miejscu 

Alternatywnie, dokumentacja może być umieszczona w innym pliku (lub w tym samym pliku na górze lub na dole, lub gdziekolwiek), z dala od deklaracji klasy lub prototypu funkcji. W takim przypadku informacje zostaną zduplikowane, raz w rzeczywistym pliku źródłowym, a raz w pliku dokumentacji.

Plik pierwszy, `source.h`: 
```python
std::string name() const;
void setName(const std::string&);
```

Plik drugi, `source.h.dox`: 
```python
/** \file source.h
 *  \brief The documentation of source.h
 *   
 *   The details of this file go here.
 */

/** \fn std::string name() const;
 *  \brief Returns the name of the workbench object.
 */
/** \fn void setName(const std::string&);
 *  \brief Set the name to the workbench object.
 */
```

W tym przypadku polecenie strukturalne `\file` służy do wskazania, który plik źródłowy jest dokumentowany. Polecenie strukturalne `\fn` wskazuje, że poniższy kod jest funkcją, a polecenie `\brief` służy do podania krótkiego opisu tej funkcji.

Ten sposób dokumentowania pliku źródłowego jest przydatny, jeśli chcesz dodać dokumentację do projektu bez dodawania rzeczywistego kodu. Po umieszczeniu bloku komentarza w pliku z jednym z następujących rozszerzeń `.dox`, `.txt` lub `.doc`, Doxygen przeanalizuje komentarze i utworzy odpowiednią dokumentację, ale ukryje ten plik pomocniczy na liście plików.

Projekt FreeCAD dodaje kilka plików kończących się na `.dox` w wielu katalogach w celu dostarczenia opisu lub przykładów znajdującego się tam kodu. Ważne jest, aby takie pliki były poprawnie skategoryzowane w grupie lub przestrzeni nazw, dla których Doxygen udostępnia kilka poleceń pomocniczych, takich jak `\defgroup`, `\ingroup` i `\namespace`.


<div class="mw-collapsible mw-collapsed toccolours">

Przykład `src/Base/core-base.dox`. Plik ten w drzewie źródłowym FreeCAD zawiera krótkie wyjaśnienie przestrzeni nazw `Base`.


<div class="mw-collapsible-content">


```python
/** \defgroup BASE Base
 *  \ingroup CORE
    \brief Basic structures used by other FreeCAD componentsThe Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units

*/

/*! \namespace Base
    \ingroup BASE
    \brief Basic structures used by other FreeCAD components

    The Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units
*/
```


</div>


</div>

Innym przykładem jest plik `src/Gui/Command.cpp`. Przed szczegółami implementacji metod `Gui::Command` znajduje się blok dokumentacji, który wyjaśnia niektóre szczegóły struktury poleceń FreeCAD. Zawiera on różne polecenia `\section` w celu uporządkowania dokumentacji. Zawiera nawet przykładowy kod zawarty w parze słów kluczowych `\code` i `\endcode`. Gdy plik jest przetwarzany przez Doxygen, ten przykład kodu zostanie specjalnie sformatowany, aby się wyróżniał. Słowo kluczowe `\ref` jest używane w kilku miejscach do tworzenia linków do nazwanych sekcji, podrozdziałów, stron lub kotwic w innym miejscu dokumentacji. Podobnie, polecenia `\see` lub `\sa` wypisują \"Zobacz także\" i zapewniają link do innych klas, funkcji, metod, zmiennych, plików lub adresów URL.


<div class="mw-collapsible mw-collapsed toccolours">

. Przykład `src/Gui/Command.cpp`


<div class="mw-collapsible-content">


```python
/** \defgroup commands Command Framework
    \ingroup GUI
    \brief Structure for registering commands to the FreeCAD system
 * \section Overview
 * In GUI applications many commands can be invoked via a menu item, a toolbar button or an accelerator key. The answer of Qt to master this
 * challenge is the class \a QAction. A QAction object can be added to a popup menu or a toolbar and keep the state of the menu item and
 * the toolbar button synchronized.
 *
 * For example, if the user clicks the menu item of a toggle action then the toolbar button gets also pressed
 * and vice versa. For more details refer to your Qt documentation.
 *
 * \section Drawbacks
 * Since QAction inherits QObject and emits the \a triggered() signal or \a toggled() signal for toggle actions it is very convenient to connect
 * these signals e.g. with slots of your MainWindow class. But this means that for every action an appropriate slot of MainWindow is necessary
 * and leads to an inflated MainWindow class. Furthermore, it's simply impossible to provide plugins that may also need special slots -- without
 * changing the MainWindow class.
 *
 * \section wayout Way out
 * To solve these problems we have introduced the command framework to decouple QAction and MainWindow. The base classes of the framework are
 * \a Gui::CommandBase and \a Gui::Action that represent the link between Qt's QAction world and the FreeCAD's command world. 
 *
 * The Action class holds a pointer to QAction and CommandBase and acts as a mediator and -- to save memory -- that gets created 
 * (@ref Gui::CommandBase::createAction()) not before it is added (@ref Gui::Command::addTo()) to a menu or toolbar.
 *
 * Now, the implementation of the slots of MainWindow can be done in the method \a activated() of subclasses of Command instead.
 *
 * For example, the implementation of the "Open file" command can be done as follows.
 * \code
 * class OpenCommand : public Command
 * {
 * public:
 *   OpenCommand() : Command("Std_Open")
 *   {
 *     // set up menu text, status tip, ...
 *     sMenuText     = "&Open";
 *     sToolTipText  = "Open a file";
 *     sWhatsThis    = "Open a file";
 *     sStatusTip    = "Open a file";
 *     sPixmap       = "Open"; // name of a registered pixmap
 *     sAccel        = "Shift+P"; // or "P" or "P, L" or "Ctrl+X, Ctrl+C" for a sequence
 *   }
 * protected:
 *   void activated(int)
 *   {
 *     QString filter ... // make a filter of all supported file formats
 *     QStringList FileList = QFileDialog::getOpenFileNames( filter,QString::null, getMainWindow() );
 *     for ( QStringList::Iterator it = FileList.begin(); it != FileList.end(); ++it ) {
 *       getGuiApplication()->open((*it).latin1());
 *     }
 *   }
 * };
 * \endcode
 * An instance of \a OpenCommand must be created and added to the \ref Gui::CommandManager to make the class known to FreeCAD.
 * To see how menus and toolbars can be built go to the @ref workbench.
 *
 * @see Gui::Command, Gui::CommandManager
 */
```


</div>


</div>



### Przykład z projektu VTK 

Jest to przykład z [VTK](https://vtk.org/), biblioteki wizualizacji 3D używanej do prezentacji danych naukowych, takich jak wyniki elementów skończonych i informacje o chmurze punktów.

Klasa do przechowywania kolekcji współrzędnych jest zdefiniowana w pliku nagłówkowym C++. Górna część pliku jest opatrzona komentarzem i użyto kilku słów kluczowych, takich jak `@class`, `@brief` i `@sa`, aby wskazać ważne części. Wewnątrz klasy, przed prototypami metod klasy, blok komentowanego tekstu wyjaśnia, co robi funkcja i jej argumenty.

-   Kod źródłowy [vtkArrayCoordinates.h](https://github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Dokumentacja stworzona przez Doxygen dla klasy [vtkArrayCoordinates](http://www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html).



## Kompilacja dokumentacji 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Ogólny przepływ pracy do tworzenia dokumentacji kodu źródłowego za pomocą Doxygen.*

Aby wygenerować dokumentację kodu źródłowego, należy wykonać dwa podstawowe kroki:

1.  Utwórz plik konfiguracyjny, aby kontrolować sposób, w jaki Doxygen będzie przetwarzał pliki źródłowe.
2.  Uruchom `doxygen` na tej konfiguracji.


<div class="mw-collapsible mw-collapsed toccolours">

Proces ten opisano poniżej.


<div class="mw-collapsible-content">

-   Upewnij się, że masz w systemie programy `doxygen` i `doxywizard`. Zalecane jest również posiadanie programu `dot` z [Graphviz](https://www.graphviz.org/), w celu generowania diagramów z relacjami między klasami i przestrzeniami nazw. W systemach Linux programy te można zainstalować z poziomu menedżera pakietów.


```python
sudo apt install doxygen doxygen-gui graphviz
```

-   Upewnij się, że znajdujesz się w tym samym folderze co pliki źródłowe lub w katalogu najwyższego poziomu drzewa źródłowego, jeśli masz wiele plików źródłowych w różnych podkatalogach.


```python
cd toplevel-source
```

-   Uruchom `doxygen -g DoxyDoc.cfg`, aby utworzyć plik konfiguracyjny o nazwie `DoxyDoc.cfg`. Jeśli pominiesz tę nazwę, domyślnie będzie to `Doxyfile` bez rozszerzenia.
-   Jest to duży, zwykły plik tekstowy, który zawiera wiele zmiennych wraz z ich wartościami. W podręczniku Doxygen zmienne te nazywane są \"tagami\". Plik konfiguracyjny i wszystkie znaczniki są obszernie opisane w sekcji [Konfiguracja](http://www.doxygen.nl/manual/config.html) podręcznika. Możesz otworzyć plik za pomocą dowolnego edytora tekstu i edytować wartość każdego tagu w razie potrzeby. W tym samym pliku można przeczytać komentarze wyjaśniające każdy ze znaczników i ich wartości domyślne.


```python
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = "My Project"
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       =
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = NO
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
...
```

-   Zamiast korzystać z edytora tekstu, można uruchomić `doxywizard`, aby edytować wiele tagów jednocześnie. Za pomocą tego interfejsu można zdefiniować wiele właściwości, takich jak informacje o projekcie, typ danych wyjściowych (HTML i LaTeX), użycie Graphviz do tworzenia diagramów, komunikaty ostrzegawcze do wyświetlenia, wzorce plików (rozszerzenia) do udokumentowania lub wykluczenia, filtry wejściowe, opcjonalne nagłówki i stopki dla generowanych stron HTML, opcje dla danych wyjściowych LaTeX, RTF, XML lub Docbook i wiele innych opcji.


```python
doxywizard DoxyDoc.cfg
```

-   Inną opcją jest utworzenie pliku konfiguracyjnego od zera i dodanie tylko tych tagów, które chcesz za pomocą edytora tekstu.
-   Po zapisaniu konfiguracji, można uruchomić Doxygen na tym pliku konfiguracyjnym.


```python
doxygen DoxyDoc.cfg
```

-   Wygenerowana dokumentacja zostanie utworzona wewnątrz folderu o nazwie `toplevel-source/html`. Będzie składać się z wielu stron HTML, obrazów PNG dla grafiki, kaskadowych arkuszy stylów (`.css`), plików Javascript (`.js`) i potencjalnie wielu podkatalogów z większą liczbą plików w zależności od rozmiaru kodu. Punktem wejścia do dokumentacji jest `index.html`, który można otworzyć za pomocą przeglądarki internetowej.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

Jeśli piszesz nowe klasy, funkcje lub całe nowe środowisko pracy, zaleca się okresowe uruchamianie `doxygen`, aby sprawdzić, czy bloki dokumentacji, [Markdown](#Obsługa_znaczników_Markdown.md) i [polecenia specjalne](#Znaczniki_Doxygen.md) są poprawnie odczytywane i czy wszystkie funkcje publiczne są w pełni udokumentowane. Prosimy również o zapoznanie się z [wskazówkami dotyczącymi dokumentacji](https://github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) znajdującymi się w kodzie źródłowym.

Podczas generowania pełnej dokumentacji FreeCAD nie uruchamia się bezpośrednio `doxygen`. Zamiast tego projekt używa `cmake` do skonfigurowania środowiska kompilacji, a następnie `make` uruchamia kompilację źródeł FreeCAD i dokumentacji Doxygen. Jest to wyjaśnione na stronie [Dokumentacja źródłowa](Source_documentation/pl.md).



## Znaczniki Doxygen 

Wszystkie polecenia dokumentacji Doxygen [1](http://www.doxygen.nl/manual/commands.html) zaczynają się od odwrotnego ukośnika `\` lub symbolu at `@`, zgodnie z preferencjami użytkownika. Zwykle używany jest odwrotny ukośnik `\`, ale czasami używany jest `@` w celu poprawy czytelności.

Polecenia mogą mieć jeden lub więcej argumentów. W podręczniku Doxygen argumenty opisano w następujący sposób.

-   Jeśli używane są nawiasy `<klamrowe>`, argumentem jest pojedyncze słowo.
-   W przypadku użycia nawiasów `(okrągłych)` argument rozciąga się do końca wiersza, w którym znaleziono polecenie.
-   Jeśli używane są nawiasy {klamrowe}, argument rozciąga się aż do następnego akapitu. Akapity oddzielane są pustą linią lub wskaźnikiem sekcji.
-   Jeśli używane są nawiasy `[kwadratowe]`, argument jest opcjonalny.


<div class="mw-collapsible mw-collapsed toccolours">

Poniżej przedstawiono niektóre z najczęściej używanych słów kluczowych w dokumentacji FreeCAD.


<div class="mw-collapsible-content">

-    (group title), zobacz [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), oraz [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   ]), zobacz [\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), oraz [Grouping](http://www.doxygen.nl/manual/grouping.html).
-    [(title)], zobacz [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), oraz [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, zobacz [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); wskazuje autora tego fragmentu kodu.
-   \brief { brief description }, zobacz [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); krótko opisuje tę funkcję.
-   ], zobacz [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); dokumentuje plik źródłowy lub nagłówkowy.
-    (title), zobacz [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); umieszcza informacje na osobnej stronie, niezwiązanej bezpośrednio z konkretną klasą, plikiem lub członkiem.
-   , v [\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); wskazuje dokumentację dla pakietu Java *(ale jest również używana w Python)*.
-   \fn (function declaration), zobacz [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); dokumentuje funkcję.
-   \var (variable declaration), zobacz [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); dokumentuje zmienną, jest to równoważne z `\fn`, `\property`, and `\typedef`.
-    (section title), zobacz [\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); rozpoczyna sekcję.
-    (subsection title), zobacz [\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); rozpoczyna sekcję podrzędną.
-   , zobacz [\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); wskazuje informacje dla przestrzeni nazw.
-   \cond [(section-label)], oraz \endcond, zobacz [\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); definiuje blok do warunkowego udokumentowania lub pominięcia.
-   , zobacz [\\a](http://www.doxygen.nl/manual/commands.html#cmda); wyświetla argument kursywą dla podkreślenia.
-    { parameter description }, zobacz [\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); wskazuje parametr funkcji.
-   \return { description of the return value }, zobacz [\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); określa wartość zwracaną.
-   \sa { references }, zobacz [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); drukuje \"Zobacz także\".
-   \note { text }, zobacz [\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); dodaje akapit, który będzie używany jako notatka.


</div>


</div>



## Obsługa znaczników Markdown 

Od wersji Doxygen 1.8 rozpoznawana jest składnia Markdown w blokach dokumentacji. Markdown to minimalistyczny język formatowania inspirowany zwykłym tekstem e-mail, który, podobnie jak składnia Wiki, ma być prosty i czytelny, nie wymagając skomplikowanego kodu, jaki można znaleźć w HTML-u, LaTeX-u czy własnych komendach Doxygen. Markdown zyskał popularność wśród wolnego oprogramowania, zwłaszcza w platformach internetowych takich jak Github, ponieważ umożliwia tworzenie dokumentacji bez użycia skomplikowanego kodu. Zobacz sekcję [Obsługa Markdown](http://www.doxygen.nl/manual/markdown.html) w podręczniku Doxygen, aby dowiedzieć się więcej. Odwiedź [Strona Markdown](https://daringfireball.net/projects/markdown/), aby dowiedzieć się więcej o pochodzeniu i filozofii Markdown.

Doxygen obsługuje standardowy zestaw instrukcji Markdown, a także niektóre rozszerzenia, takie jak [Github Markdown](https://github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

. Poniżej przedstawiono kilka przykładów formatowania Markdown.


<div class="mw-collapsible-content">

Poniższy tekst jest standardowym Markdown. 
```python
Oto tekst dla jednego akapitu.

Kontynuujemy z większą ilością tekstu w innym akapicie.

To jest nagłówek poziomu 1
========================

To jest nagłówek poziomu 2


# To jest nagłówek poziomu 1

### To jest nagłówek poziomu 1 #######

> To jest cytat blokowy
> obejmujący wiele wierszy

- Pozycja 1

  Więcej tekstu dla tej pozycji.

- Pozycja 2
  * zagnieżdżony element listy.
  * kolejny zagnieżdżony element.
- Pozycja 3

1. Pierwsza pozycja.
2. Druga pozycja.

*pojedyncza gwiazdka: podkreślenie*

 _pojedyncze znaki podkreślenia_

 **podwójne gwiazdki: wyraźne podkreślenie**

 __podwójne podkreślenie__

To jest normalny akapit

    To jest blok kodu

Ponownie kontynuujemy normalny akapit.

Użyj funkcji printf(). Wewnątrz code.

[Tekst linku](http://example.net/)

![Tekst podpisu](images//path/to/img.jpg)

<http://www.example.com>
```

Poniżej znajdują się rozszerzenia Markdown.

    [TOC]

    Nagłówek pierwszy | Nagłówek drugi
     | 
    Treść komórki     | Treść komórki
    Treść komórki     | Treść komórki 

    <nowiki>~~~~~~~~~~~~~</nowiki>{.py}
    # Klasa
    class Dummy:
        pass
    <nowiki>~~~~~~~~~~~~~</nowiki>

    <nowiki>~~~~~~~~~~~~~</nowiki>{.c}
    int func(int a, int b) { return a*b; }
    <nowiki>~~~~~~~~~~~~~</nowiki>
int func(int a, int b) { return a*b; }
    


</div>


</div>



## Parsowanie bloków dokumentacji 

Tekst wewnątrz specjalnego bloku dokumentacji jest analizowany przed zapisaniem go w plikach wyjściowych HTML i LaTeX. Podczas parsowania wykonywane są następujące kroki:

-   Formatowanie Markdown jest zastępowane odpowiednimi poleceniami HTML lub specjalnymi.
-   Wykonywane są specjalne polecenia wewnątrz dokumentacji. Zobacz sekcję [Polecenia specjalne](http://www.doxygen.nl/manual/commands.html) w podręczniku, aby uzyskać wyjaśnienie każdego polecenia.
-   Jeśli linia zaczyna się od białych znaków, po których następuje jedna lub więcej gwiazdek (`*`), a następnie opcjonalnie więcej białych znaków, to wszystkie białe znaki i gwiazdki są usuwane.
-   Wszystkie powstałe puste linie są traktowane jako separatory akapitów.
-   Tworzone są automatycznie odnośniki do słów odpowiadających udokumentowanym klasom lub funkcjom. Jeśli słowo jest poprzedzone symbolem procentu `%`, to symbol ten jest usuwany, a link nie jest tworzony dla tego słowa.
-   Tworzone są odnośniki, gdy w tekście zostaną znalezione określone wzorce. Więcej informacji można znaleźć w sekcji [Automatyczne generowanie linków](http://www.doxygen.nl/manual/autolink.html) w podręczniku.
-   Znaczniki HTML znajdujące się w dokumentacji są interpretowane i konwertowane na odpowiedniki LaTeX dla wyjścia LaTeX. Zobacz sekcję [Polecenia HTML](http://www.doxygen.nl/manual/htmlcmds.html) w podręczniku, aby uzyskać wyjaśnienie każdego obsługiwanego znacznika HTML.



## Doxygen z kodem Python 

Doxygen działa najlepiej dla statycznie typowanych języków, takich jak C++. Może jednak również tworzyć [dokumentację dla plików Python](http://www.doxygen.nl/manual/docblocks.html#pythonblocks).

Istnieją dwa sposoby tworzenia bloków dokumentacji dla Python:

1.  W środowisku Python, używając „docstringów", czyli bloku tekstu otoczonego ''potrójnymi cudzysłowami'' bezpośrednio po definicji klasy lub funkcji.
2.  W środowisku Doxygen, umieszczanie komentarzy przed definicją klasy lub funkcji. W tym przypadku do rozpoczęcia bloku dokumentacji używane są podwójne znaki mieszające `##`, a następnie w kolejnych wierszach można zastosować pojedynczy znak mieszający.

Uwaga:

-   Pierwsza opcja jest preferowana, aby zachować zgodność ze standardami [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings), [PEP257](https://www.python.org/dev/peps/pep-0257/) i większością wytycznych dotyczących stylu pisania w środowisku Python *(patrz [1](https://realpython.com/python-pep8/), [2](https://realpython.com/documenting-python-code/))*. Zaleca się używanie tego stylu, jeśli zamierzasz tworzyć udokumentowane źródła przy użyciu [Sphinx](https://www.sphinx-doc.org/en/master/), który jest bardzo popularnym narzędziem do dokumentowania kodu Python. Jeśli użyjesz tego stylu, Doxygen będzie w stanie wyodrębnić komentarze dosłownie, ale specjalne polecenia Doxygen zaczynające się od `\` lub `@` nie będą działać.
-   Druga opcja nie jest tradycyjnym stylem Python, ale pozwala na użycie specjalnych poleceń Doxygen, takich jak `\param` i `\var`.



### Styl pierwszy: Dokumentacja Pythonic 

W poniższym przykładzie jeden docstring znajduje się na początku, aby wyjaśnić ogólną zawartość tego modułu *(pliku)*. Następnie docstringi pojawiają się wewnątrz definicji funkcji, klas i metod klas. W ten sposób Doxygen wyodrębni komentarze i zaprezentuje je w niezmienionej formie, bez modyfikacji.


```python
'''@package pyexample_a
Dokumentacja dla tego modułu.
Więcej szczegółów.
'''


def func():
    '''Dokumentacja dla funkcji.
    Więcej szczegółów.
    '''
    pass


class PyClass:
    '''Dokumentacja dla klasy.
    Więcej szczegółów.
    '''

    def __init__(self):
        '''Konstruktor.'''
        self._memVar = 0

    def PyMethod(self):
        '''Dokumentacja dla metody.'''
        pass
```



### Styl drugi: blok dokumentacji przed kodem 

W poniższym przykładzie bloki dokumentacji zaczynają się od podwójnych znaków hash `##`. Jeden pojawia się na początku, aby wyjaśnić ogólną zawartość tego modułu (pliku). Następnie są bloki przed definicjami funkcji, klas i metod klas, a jeden blok znajduje się po zmiennej klasy. W ten sposób Doxygen wyodrębni dokumentację, rozpozna specjalne polecenia `@package`, `@param` i `@var` i odpowiednio sformatuje tekst. 
```python
## @package pyexample_b
#  Documentation for this module.
#
#  More details.


## Documentation for a function.
#
#  More details.
def func():
    pass


## Documentation for a class.
#
#  More details.
class PyClass:

    ## The constructor.
    def __init__(self):
        self._memVar = 0

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self):
        pass

    ## A class variable.
    classVar = 0
    ## @var _memVar
    #  a member variable
```



### Kompilacja dokumentacji 

Kompilacja dokumentacji przebiega tak samo jak [dla źródeł C++](#Kompilacja_dokumentacji.md). Jeśli oba pliki Python, `pyexample_a.py` i `pyexample_b.py`, z różnymi stylami komentowania znajdują się w tym samym katalogu, oba zostaną przetworzone. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

Dokumentacja powinna zawierać informacje podobne do poniższych oraz tworzyć odpowiednie odnośniki do poszczególnych modułów i klas. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```



### Konwersja stylu Pythonic na styl Doxygen 

Poprzedni przykład pokazuje, że plik Python, który jest komentowany w [Styl Doxygen](#Styl_drugi__blok_dokumentacji_przed_kodem.md) pokazuje bardziej szczegółowe informacje i formatowanie dla jego klas, funkcji i zmiennych. Powodem jest to, że ten styl pozwala środowisku Doxygen wyodrębnić specjalne polecenia, które zaczynają się od `\` lub `@`, podczas gdy [styl Pythonic](#Styl_perwszy__dokumentacja_Pythonic.md) nie. Dlatego pożądane byłoby przekonwertowanie stylu Pythonic na styl Doxygen przed kompilacją dokumentacji. Jest to możliwe dzięki pomocniczemu programowi Python o nazwie [doxypypy](https://github.com/Feneric/doxypypy). Ten program jest inspirowany starszym programem o nazwie [doxypy](https://github.com/Feneric/doxypy), który pobierał '''docstrings''' Python i konwertował je na bloki komentarzy Doxygen, które zaczynają się od podwójnego hasha `##`. Doxypy idzie dalej, ponieważ analizuje dokumentację i wyodrębnia interesujące elementy, takie jak zmienne i argumenty, a nawet doctesty *(przykładowy kod w dokumentacji)*.

Doxypypy można zainstalować za pomocą `pip`, instalatora pakietów Python. 
```python
pip3 install --user doxypypy
```

Jeśli polecenie `pip` zostanie użyte bez opcji `--user`, będzie wymagało uprawnień superużytkownika (root) do zainstalowania pakietu, ale w większości przypadków nie jest to konieczne; używaj uprawnień roota tylko wtedy, gdy masz pewność, że pakiet nie będzie kolidował z pakietami dostarczonymi przez twoją dystrybucję.

Jeśli pakiet został zainstalowany z poziomu użytkownika, może znajdować się w jego katalogu domowym, na przykład w `$HOME/.local/bin`. Jeśli katalog ten nie znajduje się w katalogu `PATH`, program nie zostanie znaleziony. Dlatego należy dodać katalog do zmiennej `PATH`, albo w pliku `$HOME/.bashrc`, albo w pliku `$HOME/.profile`. 
```python
export PATH="$HOME/.local/bin:$PATH"
```

Alternatywnie, można utworzyć dowiązanie symboliczne do programu `doxypy`, umieszczając dowiązanie w katalogu, który jest już zawarty w `PATH`. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Gdy program `doxypy` jest zainstalowany i dostępny z terminala, plik Python z Pythonowymi docstringami może zostać przeformatowany na styl Doxygen za pomocą poniższych instrukcji. Program wypisuje przeformatowany kod na standardowe wyjście, więc należy przekierować to wyjście do nowego pliku. 
```python
doxypypy -a -c pyexample_pythonic.py > pyexample_doxygen.py
```


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_pythonic.py`


<div class="mw-collapsible-content">


```python
'''@package pyexample_pythonic
Documentation for this module.
More details go here.
'''


def myfunction(arg1, arg2, kwarg='whatever.'):
    '''
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    '''
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`


<div class="mw-collapsible-content">


```python
##@package pyexample_pythonic
#Documentation for this module.
#More details go here.
#


## @brief     Does nothing more than demonstrate syntax.
#
#    This is an example of how a Pythonic human-readable docstring can
#    get parsed by doxypypy and marked up with Doxygen commands as a
#    regular input filter to Doxygen.
#
#
# @param        arg1    A positional argument.
# @param        arg2    Another positional argument.
#
#
# @param        kwarg   A keyword argument.
#
# @return
#        A string holding the result.
#
#
# @exception        ZeroDivisionError
# @exception        AssertionError
# @exception        ValueError.
#
# @b Examples
# @code
#        >>> myfunction(2, 3)
#        '5 - 0, whatever.'
#        >>> myfunction(5, 0, 'oops.')
#        Traceback (most recent call last):
#            ...
#        ZeroDivisionError: integer division or modulo by zero
#        >>> myfunction(4, 1, 'got it.')
#        '5 - 4, got it.'
#        >>> myfunction(23.5, 23, 'oh well.')
#        Traceback (most recent call last):
#            ...
#        AssertionError
#        >>> myfunction(5, 50, 'too big.')
#        Traceback (most recent call last):
#            ...
#        ValueError
# @endcode
#

def myfunction(arg1, arg2, kwarg='whatever.'):
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>

Oryginalny plik posiada komentarz na górze '''@package pyexample_pythonic, który wskazuje moduł lub przestrzeń nazw opisywaną przez plik. To słowo kluczowe `@package` nie jest interpretowane podczas używania potrójnych cudzysłowów w bloku komentarza.

W nowym pliku styl komentowania został zmieniony, więc linia staje się `##@package pyexample_pythonic`, która teraz będzie interpretowana przez Doxygen. Aby jednak argument został poprawnie zinterpretowany, musi zostać ręcznie edytowany, aby pasował do nowej nazwy modułu (pliku); po wykonaniu tej czynności linia powinna mieć postać `##@package pyexample_doxygen`.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

*(góra jest edytowana ręcznie, reszta pozostaje bez zmian)*


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

Aby skompilować, utwórz konfigurację i uruchom `doxygen` w katalogu toplevel zawierającym pliki. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

Dokumentacja powinna zawierać informacje podobne do poniższych i zawierać odpowiednie linki do poszczególnych modułów. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```



### Konwertowanie stylu komentarzy w locie 

W poprzednim przykładzie konwersja bloków dokumentacji została wykonana ręcznie tylko z jednym plikiem źródłowym. Idealnie chcielibyśmy, aby ta konwersja następowała automatycznie, w locie, z dowolną liczbą plików Python. Aby to zrobić, należy odpowiednio edytować konfigurację Doxygen.

Aby rozpocząć, nie używaj bezpośrednio programu `doxypy`. Zamiast tego utwórz plik konfiguracyjny za pomocą `doxygen -g`, a następnie edytuj utworzony `Doxyfile` i zmodyfikuj następujący znacznik. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

Powoduje to, że pliki pasujące do wzorca, wszystkie pliki z rozszerzeniem kończącym się na `.py`, będą przechodzić przez program `doxypypy_filter`. Za każdym razem, gdy Doxygen napotka taki plik w drzewie źródłowym, nazwa pliku zostanie przekazana jako pierwszy argument do tego programu. 
```python
doxypypy_filter example.py
```

Program `doxypypy_filter` nie istnieje domyślnie; powinien zostać utworzony jako skrypt powłoki uruchamiający `doxypypy` z odpowiednimi opcjami i przyjmujący plik jako pierwszy argument. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

Po zapisaniu tego skryptu powłoki, upewnij się, że ma on uprawnienia do wykonywania i że znajduje się w katalogu zawartym w twoim systemie `PATH`. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

W systemach Windows plik wsadowy może być używany w podobny sposób. 
```python
doxypypy -a -c %1
```

Po wykonaniu tej konfiguracji można uruchomić komendę `doxygen Doxyfile` w celu wygenerowania dokumentacji w standardowy sposób. Każdy plik Python korzystający z '''potrójnych cudzysłowów''' w Pythonie zostanie na bieżąco przeformatowany, aby używać komentarzy w stylu `##Doxygen`, a następnie zostanie przetworzony przez Doxygen, który teraz będzie mógł interpretować [specjalne polecenia](#Znaczniki_Doxygen.md) i [Składnia Mardown](#Obsługa_znaczników_Markdown.md). Oryginalny kod źródłowy nie zostanie zmodyfikowany i nie trzeba tworzyć pliku tymczasowego o innej nazwie, jak w [poprzedniej sekcji](#Konwersja_stylu_Pythonic_na_styl_Doxygen.md). Dlatego też, jeśli zostanie znaleziona instrukcja `@package example`, nie trzeba jej samodzielnie modyfikować.

Zauważ, że istniejące pliki Python, które już używają stylu `##double hash` dla swoich bloków komentarzy, nie zostaną dotknięte przez filtr `doxypypy` i będą normalnie przetwarzane przez Doxygen.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">



*Ogólny przepływ pracy do tworzenia dokumentacji kodu źródłowego za pomocą Doxygen, gdy pliki Python są filtrowane w celu przekształcenia bloków komentarzy.*



### Kontrola jakości kodu Python 

Aby skorzystać z automatycznej konwersji bloków dokumentacji, ważne jest, aby oryginalne źródła Python były poprawnie napisane, zgodnie z wytycznymi Python zawartymi w [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings) i [PEP257](https://www.python.org/dev/peps/pep-0257/). Niechlujnie napisany kod spowoduje, że `doxypypy` zawiedzie podczas przetwarzania pliku, a tym samym Doxygen nie będzie w stanie poprawnie sformatować dokumentacji.


<div class="mw-collapsible mw-collapsed toccolours">

Następujące style komentowania nie pozwolą na analizowanie docstringów przez `doxypy`, więc należy ich unikać.


<div class="mw-collapsible-content">


```python
'''@package Bad
'''

def first_f(one, two):

    "Bad comment 1"

    result = one + two
    result_m = one * two
    return result, result_m

def second_f(one, two):
    "Bad comment 2"
    result = one + two
    result_m = one * two
    return result, result_m

def third_f(one, two):
    'Bad comment 3'
    result = one + two
    result_m = one * two
    return result, result_m

def fourth_f(one, two):
    #Bad comment 4
    result = one + two
    result_m = one * two
    return result, result_m
```


</div>


</div>

Zawsze używaj potrójnych cudzysłowów dla docstrings i upewnij się, że następują one bezpośrednio po deklaracji klasy lub funkcji.

Dobrym pomysłem jest również zweryfikowanie jakości kodu Python za pomocą narzędzia takiego jak [flake8](http://flake8.pycqa.org/en/latest/) ([Gitlab](https://gitlab.com/pycqa/flake8)). Flake8 łączy przede wszystkim trzy narzędzia, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle) *(dawniej pep8)* i [McCabe complexity checker](https://github.com/PyCQA/mccabe), w celu wymuszenia właściwego stylu kodu Python.


```python
pip install --user flake8
flake8 example.py
```

Aby sprawdzić wszystkie pliki wewnątrz drzewa źródeł użyj `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

Jeśli projekt tego wymaga, niektóre kontrole kodu uznane za zbyt rygorystyczne mogą zostać zignorowane. Kody błędów można sprawdzić w [dokumentacji Pycodestyle](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

W podobny sposób programem, który przede wszystkim sprawdza zgodność komentarzy z [PEP257](https://www.python.org/dev/peps/pep-0257/) jest [Pydocstyle](https://github.com/PyCQA/pydocstyle). Kody błędów można sprawdzić w [dokumentacji Pydocstyle](http://www.pydocstyle.org/en/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Użyj go również z `find`, aby wykonać sprawdzanie docstringów we wszystkich plikach źródłowych. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```



## Dokumentacja źródłowa z użyciem Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/) jest najpopularniejszym systemem do dokumentowania kodu źródłowego Pythona. Ponieważ jednak podstawowe funkcje i środowiska pracy FreeCAD są napisane w języku C++, uznano, że Doxygen jest lepszym narzędziem dokumentacyjnym dla tego projektu.

Podczas gdy Sphinx może natywnie analizować dokumentację Python, analizowanie źródeł C++ wymaga nieco więcej pracy. Projekt [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) jest próbą wypełnienia luki między Sphinx i Doxygen, w celu zintegrowania zarówno dokumentacji kodu źródłowego Python, jak i C++ w tym samym systemie. Po pierwsze, Doxygen musi być skonfigurowany do wyprowadzania pliku XML. Dane wyjściowe XML są następnie odczytywane przez Breathe i konwertowane na odpowiednie dane wejściowe dla Sphinx.

Aby dowiedzieć się więcej o tym procesie, zobacz [Skróconą instrukcję obsługi](https://breathe.readthedocs.io/en/latest/quickstart.html) w dokumentacji Breathe.

Zobacz tę odpowiedź w [Stackoverflow](https://stackoverflow.com/a/35377654), aby zapoznać się z innymi alternatywami dla dokumentowania kodu C++ i Python razem w tym samym projekcie.



## Powiązane

-   [Dokumentacja kodu źródłowego](Source_documentation/pl.md)
-   [Strona internetowa FreeCAD API](https://www.freecadweb.org/api/)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd%20Party.md) > Doxygen/pl
