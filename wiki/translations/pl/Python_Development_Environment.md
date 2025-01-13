# Python Development Environment/pl
## Uproszczone środowisko programistyczne dla Python w FreeCAD 

[Python](https://pl.wikipedia.org/wiki/Python) to środowisko programistyczne, które zostało włączone do systemu [FreeCAD](https://www.freecadweb.org/). Za jego pomocą wiele operacji oferowanych przez FreeCAD jest dostępnych dla środowiska programistycznego. Programy Python dla FreeCAD są zwykle tworzone tak, aby można je było uruchamiać w konsoli Python lub za pomocą funkcji makr FreeCAD *(patrz [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md))*.

Dostępnych jest wiele narzędzi do tworzenia programów w środowisku Python. Czynniki komplikujące rozwój Pythona do użytku z FreeCAD są dwojakie: po pierwsze narzędzia nie mają żadnego wsparcia dla licznych struktur danych i punktów dostępu FreeCAD. Po drugie nie działają \"w FreeCAD\". Oznacza to, że można ich używać do rozwijania kodu poza FreeCAD i nie być w stanie testować w środowisku docelowym, lub można rozwijać Pythona w środowisku docelowym *(tj. środowisku FreeCAD)*, ale nie mieć żadnego wsparcia ze strony narzędzi programistycznych. Żadne z tych rozwiązań nie jest akceptowalne.



## Kontekst

Nowoczesne tworzenie oprogramowania w standardzie komercyjnym odbywa się zwykle przy użyciu zestawu narzędzi ogólnie określanych jako [IDE](https://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne). Zazwyczaj narzędzia te obejmują następujące elementy:

-   edytor kodu źródłowego,
-   narzędzia do automatyzacji kompilacji,
-   debugger.

które są standardowe, podczas gdy poniższe są obecne w niektórych IDE, ale nie we wszystkich:

-   inteligentne uzupełnianie kodu,
-   zintegrowany kompilator, interpreter lub oba te elementy,
-   system kontroli wersji,
-   Budowa graficznego interfejsu użytkownika *(GUI)*,
-   przeglądarka klas,
-   przeglądarka obiektów,
-   diagram hierarchii klas.

Podsumowanie statusu tych narzędzi w FreeCAD jest następujące *(\"N/A\" oznacza \"Niedostępne\")*:


<table style="width: 100%" border="1">


<tr>


<td>

editor kodu


</td>


<td>

dla platform obsługiwanych przez FreeCAD dostępne są różne edytory, omówione poniżej


</td>


</tr>


<tr>


<td>

narzędzia automatyzacji kompilacji


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

debugger


</td>


<td>

Planowane, ale jeszcze niedostępne, istnieją pewne obejścia omówione poniżej


</td>


</tr>


<tr>


<td>

inteligentne uzupełnianie kodu


</td>


<td>

niektóre są dostępne za pośrednictwem konsoli Python, ale to wszystko


</td>


</tr>


<tr>


<td>

zintegrowany kompilator, interpreter lub oba te elementy


</td>


<td>

kompilator Python jest zintegrowany z konsolą Python, ale nie z edytorami


</td>


</tr>


<tr>


<td>

system kontroli wersji


</td>


<td>

N/A - istnieje tylko jedna wersja pliku


</td>


</tr>


<tr>


<td>

budowa graficznego interfejsu użytkownika *(GUI)*


</td>


<td>

To, co jest dostępne, jest podstawowe i opiera się na kopiowaniu / wklejaniu kodu *(patrz [PySide](PySide/pl.md))*.


</td>


</tr>


<tr>


<td>

przeglądarka klasy


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

przeglądarka obiektów


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

diagram hierarchii klas


</td>


<td>

N/A


</td>


</tr>


</table>

Istnieje wiele narzędzi wspierających powyższą funkcję dla programowania w Pythonie, ale niestety nie integrują się one ze środowiskiem programistycznym FreeCAD.

Lista IDE dla Python znajduje się na stronie [Integrated Development Environments for Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).



## Edytor

Istnieje edytor Python będący częścią FreeCAD, jest on uruchamiany poprzez kliknięcie przycisku Edycja na Makrodefinicjach -\> [Makrodefinicje \...](Std_DlgMacroExecute/pl.md). Jeśli chcesz korzystać z innego edytora, który wykorzystuje twoją platformę, dostępne są różne edytory Python, dla wielu platform i z różnym poziomem funkcjonalności. Jedną z zalet korzystania z zewnętrznego edytora jest to, że obszar wyświetlania FreeCAD może być używany do wyjścia *(zarówno graficznego, jak i tekstowego do konsoli)*, podczas gdy kod źródłowy jest wyświetlany w innej aplikacji. Lista edytorów dla Python dla różnych platform jest dostępna pod adresem [edytory Python](https://wiki.python.org/moin/PythonEditors).

Uwaga: Na komputerach Macintosh dobrze sprawdza się edytor tekstu [TextWrangler](http://www.barebones.com/products/textwrangler/). Posiada podświetlanie kodu i doskonałe możliwości wyszukiwania. Istnieją opcje wykonywania zadań w Pythonie, ale oczywiście nie działają one w środowisku FreeCAD.



### Katalogi kodu źródłowego makrodefinicji 

Istnieją dwa katalogi używane przez FreeCAD, domyślnie są one tym samym katalogiem, ale są wskazywane przez różne punkty wywoływalne w FreeCAD:

-   FreeCAD.ConfigGet(\"UserAppData\")
-   FreeCAD.ParamGet(\'User parameter:BaseApp/Preferences/Macro\').GetString(\'MacroPath\')

Pierwszy z nich \"UserAppData\" wskazuje na katalog, w którym mogą być przechowywane takie rzeczy, jak pliki konfiguracyjne lub inne pliki przeznaczone dla użytkownika, ale nie do edycji przez użytkownika.

Drugi \"MacroPath\" wskazuje na katalog, w którym przechowywane są pliki Python, które są plikami makrodefinicji dla FreeCAD. Aby oznaczyć plik Python jako plik makra dla FreeCAD, rozszerzenie pliku zmienia się z \".py\" na \".FCMacro\".

Domyślnie te dwa katalogi znajdują się w tej samej lokalizacji, ale nie jest to konieczne. Wygodna może być zmiana lokalizacji plików makr (\*.FCMacro) na inną.

Edycja plików znajdujących się w \"MacroPath\" jest prosta, edytor tekstu to umożliwi. Aby ułatwić korzystanie z plików makr FreeCAD, zaleca się przechowywanie wszystkich plików makr w katalogu wskazywanym przez \"MacroPath\".

Aby zmienić katalog \"MacroPath\", użyj ** Przybory -> Edycja parametrów ...**, a następnie wybierz Preferences/Macro/MacroPath, gdzie tekst można kliknąć dwukrotnie i edytować. Alternatywnie \"MacroPath\" można zmienić za pomocą kodu:


```python
FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')
```

## Debugger


**'''Debugger jest planowany dla FreeCAD, a te kroki są obejściem do czasu jego udostępnienia. Zobacz informacje w serwisie: github.com/mumme74/FreeCAD/tree/editor_fixes'''**

[Debuggery](https://en.wikipedia.org/wiki/Debugger) zazwyczaj zapewniają dwie główne funkcje *(między innymi)*:

-   punkty przerwania w kodzie źródłowym
-   inspekcja zmiennych

**Punkty przerwania** to \"pułapki\", które są umieszczane w kodzie, jeśli ścieżka wykonania kodu napotka jeden z tych punktów przerwania, wykonanie zostanie zatrzymane lub zawieszone. Należy pamiętać, że wykonywanie nie zostaje zatrzymane, ponieważ gdy program zostaje zatrzymany, wszystkie informacje znajdujące się w pamięci, takie jak zmienne, zostają utracone. Podczas gdy program jest zawieszony, zawartość zmiennych może być sprawdzana i czasami zmieniana *(co zależy od możliwości debuggera)*. Ogólnie rzecz biorąc, kod źródłowy nie może być zmieniany, chociaż niektóre środowiska to obsługują. Gdy kod źródłowy jest gotowy, można wznowić jego wykonywanie. W kodzie można umieścić liczne punkty przerwania i mogą wystąpić liczne zawieszenia przez punkty przerwania. Celem debuggera jest upewnienie się, że wykonanie z punktami przerwania i zawieszeniami jest funkcjonalnie identyczne z wykonaniem bez punktów przerwania.

**Inspekcje zmiennych** są dostępne podczas zawieszenia wykonywania spowodowanego punktem przerwania. Zasadniczo można przeglądać zawartość zmiennych, wiele debuggerów obsługuje również edycję zawartości przed wznowieniem wykonywania.

Chociaż dla FreeCAD planowany jest w pełni funkcjonalny debugger, nie jest on jeszcze dostępny. Ta sekcja zawiera szczegółowe informacje na temat niektórych obejść tymczasowych do czasu wydania debuggera.



### Punkty przerwania 

Wdrożenie punktów przerwania wymaga nadzorczego poziomu kodu, który zarządza wykonaniem kodu w trakcie rozwoju. Taki poziom kodu dla rozwoju Python w FreeCAD nie jest obecnie dostępny. Jako słaby substytut, poniższy kod jest opcją. Zamiast zawieszać wykonywanie, kod całkowicie zatrzyma wykonywanie, dzieląc liczbę przez zero. Jest to naprawdę bardzo słaba opcja w porównaniu do właściwego punktu przerwania debuggera, również ta opcja jest przydatna tylko wtedy, gdy jest używana razem z procedurą pokazaną w następnej sekcji \"Inspekcja zmiennych\".

**Breakpoint Code** 
```python
def breakpoint(*args):
    # this routine will print an optional parameter on the console and then stop execution by diving by zero
    # e.g. breakpoint()
    # e.g. breakpoint("summation module")
    #
    if len(args)>0:
        FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
    hereWeStop = 12/0
    
```

**Śledzenie konsoli**

Gdy program zawiedzie podczas wykonywania, Python generuje tak zwany traceback, który zawiera listę kolejności wykonywania programu *(tj. który program wywołał który program w jakiej kolejności)*.

Przykładowy kod:


```python
breakpoint('amalgamation routine')
```

otrzymujemy następujący traceback:


```python
Breakpoint: amalgamation routine
Traceback (most recent call last):
  File "/Users/wylbur/Library/Preferences/FreeCAD/testStub.FCMacro", line 40, in <module>
    breakpoint()
  File "/Users/wylbur/Library/Preferences/FreeCAD/myNewMacro.FCMacro", line 28, in breakpoint
    hereWeStop = 12/0
ZeroDivisionError: integer division or modulo by zero
```

Czytając traceback możemy stwierdzić, że:

-   komunikat \"Breakpoint: amalgamation routine\" został wysłany przez punkt przerwania, który ma ciąg \"amalgamation routine,
-   błąd wykonania wystąpił w linii 28 modułu \"myNewMacro\",
-   procedura \'myNewMacro\' została wywołana z linii 40 w module \"testStub\".

Zakładając, że ciąg znaków przekazany do wywołania punktu przerwania jest znaczący, można łatwo określić lokalizację punktu przerwania. Należy pamiętać, że jest to złożony system, w którym śledzenie może zawierać dziesiątki, a nawet setki wpisów.

Aby uzyskać produktywność z tymi punktami przerwania, przejdź do następnej sekcji.



### Inspekcja zmiennych 

Drugą główną funkcją debuggera jest badanie i ewentualna zmiana zawartości zmiennych. Po raz kolejny, dopóki debugger FreeCAD dla Python nie będzie gotowy, musimy polegać na obejściach.

Cechą systemu FreeCAD jest dostarczanie zmiennych globalnych. Zmienne te są tworzone przez kod Python i istnieją w pamięci FreeCAD, dopóki użytkownik nie opuści FreeCAD. Postać tych zmiennych to:


```python
FreeCAD.myVariable = 123
```

Instrukcja tworzy zmienną Python w pamięci FreeCAD, która jest w pełni dostępna dla kodu Python, w rzeczywistości zachowuje się identycznie jak normalna zmienna Python. Jednak po zakończeniu działania kodu Python, niezależnie od tego, czy jest on uruchamiany jako makrodefinicja, czy przez konsolę, w pamięci pozostanie zmienna \"FreeCAD.myVariable\" o wartości 123. Wprowadzanie:


```python
>>> FreeCAD.myVariable
123
```

wyświetli zawartość zmiennej na konsoli. Wartość ta pozostanie we FreeCAD, dopóki nie zostanie zmieniona lub użytkownik nie opuści FreeCAD. Oznacza to, że wartość jest obecna i dostępna do odczytu przez kolejny program Python. W dowolnym momencie można ją sprawdzić z konsoli, wpisując jej nazwę. Tak więc program o nazwie \"Program A\":


```python
# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable
```

może uruchomić się i załadować wartości do zmiennej globalnej. Później drugi program o nazwie \"Program B\" może zostać uruchomiony i pobrać wartość:


```python
myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable
```

Przypuszczalnie \"Program B\" wykonuje następnie obliczenia obejmujące wartości pozostawione w FreeCAD.myVariable. W dowolnym momencie użytkownik może wpisać na konsoli, aby sprawdzić zawartość zmiennej:


```python
>>> FreeCAD.myVariable
[123, 'abc']
>>> 
```

Ważnym faktem, o którym należy pamiętać w przypadku zmiennych globalnych FreeCAD, jest to, że istnieją one w pamięci i są tracone po zamknięciu programu. Nie są one zapisywane z dokumentami, ale istnieją tylko w pamięci.



## Użycie

To prowadzi nas do punktu, w którym możemy połączyć te dwa kroki i użyć ich do śledzenia błędów w kodzie. Jest to nieco uciążliwe w użyciu, ale jest to tylko opcja, dopóki debugger FreeCAD nie będzie gotowy.

Prawdopodobnie najłatwiej jest to przedstawić na przykładzie, powiedzmy, że debugowany jest następujący program:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Wykonanie programu na konsoli daje wynik:


```python
>>> monthCounter()
10
```

co nie jest tym, czego się spodziewaliśmy! Zakładając, że nie jesteśmy w stanie zobaczyć błędów, możemy użyć naszego niewyszukanego breakpointa i egzaminatora zmiennych w następujący sposób. Możemy wstawić linię, aby skopiować wartość zmiennej, nad którą się zastanawiamy, do zmiennej globalnej, a następnie możemy umieścić punkt przerwania, aby zatrzymać wykonywanie w tym miejscu:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
    breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Teraz po uruchomieniu programu otrzymujemy:


```python
>>> monthCounter()
Breakpoint: is this assignment faulty?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 9, in monthCounter
  File "<input>", line 5, in breakpoint
ZeroDivisionError: integer division or modulo by zero
>>> 
```

Prawdopodobnie sprawy nie wyglądają tak dobrze, ale to, co możemy teraz zrobić, to sprawdzić wartość zmiennej Python \"temporaryVariable1\", ponieważ przypisaliśmy jej wartość do zmiennej globalnej \"FreeCAD.saveMyVariable\":


```python
>>> FreeCAD.saveMyVariable
15
>>>
```

Pamiętając, że zmienna \"FreeCAD.saveMyVariable\" przechowuje wartość zmiennej Python \"temporaryVariable1\", możemy teraz określić błąd w wartości i rozpocząć śledzenie wstecz, aby określić, skąd pochodzi błąd. Kiedy patrzymy na \"FreeCAD.saveMyVariable\", ważne jest, aby zdać sobie sprawę, że zmienna \"temporaryVariable1\" nie jest już dostępna - została wyczyszczona przez system Python.

Po zlokalizowaniu błędu w instrukcji


```python
numberOfSeasons = 3
```

i poprawieniu na:


```python
numberOfSeasons = 4
```

Następnie możemy ponownie uruchomić program i uzyskać wartość \"11\", która nadal nie jest prawidłowa. Możemy wykonać więcej przypisań do zmiennych globalnych FreeCAD, mieć wiele punktów przerwania *(chociaż pierwszy napotkany zatrzyma wykonywanie)*.


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 4
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable1 = temporaryVariable1
    #breakpoint('first assignment')
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    FreeCAD.saveMyVariable2 = numberOfMonths
    breakpoint('second assignment')
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Mamy teraz dwa punkty przerwania *(chociaż jeden jest zakomentowany)* i dwie zmienne globalne FreeCAD w użyciu. Nie ma praktycznego limitu zmiennych globalnych dostępnych w FreeCAD, więc nie ma potrzeby niepotrzebnego oszczędzania. Możemy teraz wygenerować następujące wyniki na konsoli:


```python
>>> FreeCAD.saveMyVariable1
10
>>> FreeCAD.saveMyVariable2
11
>>> 
```

Kilka punktów dotyczących korzystania ze zmiennych globalnych FreeCAD:

-   Python traktuje te zmienne identycznie jak każdą inną zmienną Pythona
-   zmienne te mogą przechowywać dowolny typ danych Pythona - wszystko, co może przechowywać zwykła zmienna Pythona
-   zmienne te mogą być użyte do \"wydobycia\" zawartości zmiennej Pythona, abyśmy mogli ją zobaczyć
-   zmienne te mogą być również używane do \"dostarczania\" wartości do zmiennej Python poprzez ustawienie ich wartości z konsoli przed uruchomieniem procedury lub ustawienie ich w poprzednim programie Python
-   zmienne te mogą być używane do przekazywania danych między dwoma programami, które działają w różnych punktach czasowych
-   *(powtarzam)* te zmienne są tylko na czas trwania sesji FreeCAD, gdy użytkownik wyjdzie z FreeCAD, zmienne zostaną utracone.



### Obserwowanie zmiennych 

Istnieje narzędzie [Podgląd zmiennych globalnych](Macro_Global_Variable_Watcher/pl.md), które pomaga monitorować zmienne globalne FreeCAD. Może wyświetlać zawartość zmiennej globalnej na żądanie lub w określonym czasie.



### Konflikt przestrzeni nazw 

Jedną rzeczą, o której należy pamiętać, jest to, że FreeCAD nie zarządza globalnymi nazwami zmiennych, więc istnieje możliwość zmiany zmiennej z systemu lub innego fragmentu kodu. W związku z tym dobrym pomysłem jest poprzedzenie zmiennych czymś unikalnym, takim jak nazwa procedury. Na przykład, aby użyć zmiennej z procedury o nazwie \"alpha1\", nazwa globalna może brzmieć \"FreeCAD.alpha1MyVariable\".



## Struktura kodowania 

Podczas opracowywania małych fragmentów kodu Python w FreeCAD wystarczające może być użycie konsoli Python. Jednak wraz ze wzrostem liczby linii kodu bardziej sensowne jest przechowywanie ich w pliku. Python może znajdować się w dowolnym pliku kończącym się rozszerzeniem \".py\", jednak FreeCAD zapewnia również mechanizm o nazwie Makrodefinicje do przechowywania takich programów i interakcji z nimi *(np. edycji, uruchamiania)*. Python w zwykłych plikach \".py\" może być uruchamiany tylko z konsoli, podczas gdy Python w pliku makrodefinicji \".FCMacro\" może być uruchamiany z interfejsu FreeCAD do wykonywania makr. Jedną z wad interfejsu menu FreeCAD jest to, że jest on oparty na menu z oknem sterowania i potencjalnie powoduje bałagan na ekranie GUI.

Łatwiejszym podejściem jest pobranie kodu Python i zamiast uruchamiania go z menu makrodefinicji FreeCAD, uruchomienie go z paska narzędzi. Procedura Python powiązana z przyciskiem na pasku narzędzi może zostać wykonana jednym kliknięciem. Ponadto, ponieważ paski narzędzi są pływającymi oknami, nie zaśmiecają ekranu. W rzeczywistości, jeśli okno FreeCAD jest mniejsze niż fizyczny rozmiar ekranu, pasek narzędzi może unosić się poza oknem FreeCAD. Jest to korzystne, gdy wymagane są zrzuty ekranu z wyświetlacza FreeCAD. Ponadto pasek narzędzi może być znacznie mniejszy niż okno sterowania makrami wyświetlane przez menu Macro FreeCAD.

Podłączanie makra do przycisku na pasku narzędzi zostało opisane w [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md) i [Dostosowanie pasków narzędzi](Customize_Toolbars/pl.md). Podłączenie makrodefinicji do przycisku na pasku narzędzi, wybranie ikony itp. może zająć kilka minut. Nie zawsze jest to wymagane, ponieważ czasami po prostu chcesz szybko opracować fragment kodu, który następnie zostanie zintegrowany z innym kodem. W takiej sytuacji Test Stub może być korzystny. Nie ma prawdziwej definicji tego, co pociąga za sobą skrót testowy, to naprawdę zależy od osoby i obszaru aplikacji. Przykład pokazano poniżej:


```python
#
#           TEST
#           TEST stub to clip any code onto...
#           TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
```

Ten skrót testowy służy również jako szablon kodu z lokalizacjami zdefiniowanymi dla różnych aspektów dużego programu Python. Po uruchomieniu skrót testowy po prostu generuje komunikat pokazujący jego nazwę i kończy działanie. Podczas korzystania ze skrótów testowych, każdy napisany kod głównej linii jest umieszczany na samym końcu pliku z kodem definicji klas, funkcji itp. umieszczonym w poprzednich sekcjach. Szablon można łatwo zmienić, aby dopasować go do sytuacji. Oczywiście dla programu składającego się z 5 linii nie ma potrzeby tworzenia takiej ilości dokumentacji.

Utrzymując przycisk na stałe na pasku narzędzi i łącząc ten przycisk ze skrótem testu, zawsze jest miejsce na napisanie kodu i natychmiastowe wykonanie go. Wykonanie będzie niezależne od konsoli Pythona. Również wykonanie może być niezależne od GUI ekranu. Dane wyjściowe z opracowywanego programu pojawią się na ekranie tak, jak powinny, bez żadnych innych artefaktów ze środowiska programistycznego. Konsola Pythona może być ukryta, aby zwiększyć obszar wyświetlania lub użyta do innych celów, jeśli zajdzie taka potrzeba. Gdy wykonanie jest obsługiwane przez przycisk na pasku narzędzi, konsola nie jest wymagana.

Gdy kod zostanie ukończony, można go po prostu skopiować/wkleić do innego pliku i pozostawić test stub pusty do następnego razu, gdy będzie potrzebny.

Wiele fragmentów kodu można opracować przy użyciu tego samego kodu testowego z dodatkowym kodem do obsługi wielu przycisków, który znajduje się pod adresem [Przykłady PySide dla początkujących - więcej niż dwa przyciski](PySide_Beginner_Examples/pl#Więcej_niż_2_przyciski.md).

**Więcej wsparcia dla PySide**

Więcej informacji na temat korzystania z PySide GUI można znaleźć na stronie opisującej [PySide](PySide/pl.md).

**Więcej wsparcia dla programowania w Python**

Aby uzyskać większą pomoc w kodowaniu w Pythonie, istnieje makro napisane, aby pomóc w tworzeniu kodu Python, znajduje się ono na stronie [Okno asystenta Python](Macro_Python_Assistant_Window/pl.md).



## Składanie wszystkiego w całość 

Zarządzanie ekranem może być wyzwaniem podczas tworzenia kodu, który ma złożone i szczegółowe dane graficzne, takie jak FreeCAD. Następujący system działa dobrze:

-   FreeCAD dla konsoli, raportów, wyświetlania GUI,
-   pasek narzędzi do wywoływania opracowywanego kodu,
-   zewnętrzny edytor do modyfikacji kodu,
-   PAW *(Python Assistant Window)* do wspomagania generowania kodu Python.

**Zarządzanie ekranem**

W przypadku, gdy skrót testowy jest obsługiwany z paska narzędzi i używany jest zewnętrzny edytor, układ okna na ekranie będzie wyglądał mniej więcej tak:

![](images/PythonDevelopmentEnvironment.jpg )

\"Drzewo\" na diagramie odnosi się do przeglądarek Combi lub Tree, konsola Python i widok raportu są połączone w dolnym oknie i wybierane za pomocą przycisków. Poprzez selektywne wykorzystanie narzędzi można zoptymalizować strumień rozwoju, powyższe jest tylko jednym z pomysłów. Dostosowanie odbywa się indywidualnie.



## Różne odnośniki 

Inne linki dotyczące IDE dla Python, które mogą być interesujące to:

-   [Comparison of Python IDEs for Development](http://www.pythoncentral.io/comparison-of-python-ides-development/).
-   [Wybór najlepszego IDE dla Pythona](http://pedrokroger.net/choosing-best-python-ide/).
-   [Twoje środowisko programistyczne](http://docs.python-guide.org/en/latest/dev/env/).
-   [PyCharm IDE w wersji Community Edition](http://www.jetbrains.com/pycharm/).
-   [Korzystanie z Pyzo Python IDE z FreeCAD](Pyzo/pl.md).



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Python Code](Category_Python Code.md) > Python Development Environment/pl
