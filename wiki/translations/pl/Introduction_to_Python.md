# Introduction to Python/pl
## Wprowadzenie

To jest krótki poradnik dla osób, dla których [Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) jest całkowicie nowy. Python to wieloplatformowy [język programowania](https://en.wikipedia.org/wiki/Programming_language) o otwartym kodzie źródłowym. Ma kilka cech, które odróżniają go od innych języków programowania i jest bardzo przystępny dla nowych użytkowników:

-   Został zaprojektowany tak, aby był czytelny dla ludzi, dzięki czemu jest stosunkowo łatwy do nauczenia i zrozumienia.
-   Jest interpretowany, co oznacza, że programy nie muszą być kompilowane przed ich wykonaniem. Kod Pythona może być wykonywany natychmiast, nawet linijka po linijce, jeśli chcesz.
-   Może być osadzony w innych programach jako język skryptowy. FreeCAD posiada wbudowany interpreter Python. Możesz pisać kod Python, aby manipulować częściami FreeCAD. Jest to bardzo potężne, oznacza to, że można budować własne narzędzia.
-   Jest rozszerzalny, można łatwo podłączyć nowe moduły do instalacji Python i rozszerzyć jego funkcjonalność. Na przykład istnieją moduły, które pozwalają środowisku Pyton odczytywać i zapisywać obrazy, komunikować się z Twitterem, planować zadania do wykonania przez system operacyjny itp.

Poniższa instrukcja jest bardzo podstawowym wprowadzeniem i w żadnym wypadku nie jest kompletnym poradnikiem. Mamy jednak nadzieję, że będzie to dobry punkt wyjścia do dalszej eksploracji FreeCAD i jego mechanizmów. Zdecydowanie zachęcamy do wprowadzenia poniższych fragmentów kodu do interpretera Python.



## Interpreter

Zwykle, gdy piszesz programy komputerowe, po prostu otwierasz edytor tekstu i lub środowisko programistyczne *(które w większości przypadków zawiera edytor tekstu z kilkoma dodatkowymi narzędziami)*, wpisujesz swój program, następnie kompilujesz go i wykonujesz. Przez większość czasu robisz błędy podczas pisania, więc twój program nie działa. Otrzymujesz komunikat błędu mówiący co poszło źle. Potem wracasz do edytora tekstu, poprawiasz błędy, uruchamiasz ponownie, aż program zacznie działać prawidłowo.

W środowisku Python cały ten proces można wykonać w sposób przezroczysty wewnątrz interpretera Python. Interpreter to okno z wierszem poleceń, w którym można po prostu wpisać kod. Jeśli zainstalowałeś Python na swoim komputerze (pobierz go ze strony [Python](https://www.python.org/), jeśli korzystasz z systemu Windows lub Mac, zainstaluj go z repozytorium pakietów jeśli korzystasz z systemu GNU/Linux), będziesz miał interpreter Python w menu startowym. Ale, jak już wspomniano, FreeCAD ma również wbudowany interpreter: [konsola Python](Python_console/pl.md).

![](images/FreeCAD_Python_console.png ) 
*Konsola Python programu FreeCAD*

Jeśli jej nie widzisz, kliknij **Widok → Panele → Konsola Python**. Rozmiar konsoli Python można zmienić, a także ją odblokować.

Interpreter pokazuje wersję Python, a następnie symbol `>>`, który jest znakiem zachęty. Pisanie kodu w interpreterze jest proste: jedna linia to jedna instrukcja. Po naciśnięciu **Enter**, linia kodu zostanie wykonana *(po natychmiastowej i niewidocznej kompilacji)*. Na przykład, spróbuj napisać to:


```python
print("hello")
```


`print()`

to polecenie Python, które oczywiście wypisuje coś na ekranie. Po naciśnięciu **Enter**, operacja jest wykonywana, a wiadomość `"hello"` jest drukowana. Jeśli popełnimy błąd, na przykład napiszemy:


```python
print(hello)
```

Python natychmiast ci to powie. W tym przypadku Python nie wie, czym jest `hello`. Znaki `" "` określają, że zawartość jest ciągiem znaków, programistycznym żargonem dla fragmentu tekstu. Bez nich polecenie `print()` nie rozpoznaje `hello`. Naciskając strzałkę w górę można wrócić do ostatniej linii kodu i poprawić ją.

Interpreter Python posiada również wbudowany system pomocy. Powiedzmy, że nie rozumiemy, co poszło nie tak z `print(hello)` i chcemy uzyskać szczegółowe informacje o poleceniu:


```python
help(print)
```

Otrzymasz długi i kompletny opis wszystkiego, co może zrobić polecenie `print()`.

Teraz, gdy rozumiesz już interpreter Python, możemy przejść do poważniejszych rzeczy. 

## Zmienne

W programowaniu bardzo często zachodzi potrzeba przechowywania wartości pod nazwą. W tym miejscu pojawiają się zmienne. Na przykład, wpisz to:


```python
a = "hello"
print(a)
```

Prawdopodobnie rozumiesz co się tutaj stało, zapisaliśmy ciąg `"hello"` pod nazwą `a`. Teraz, gdy `a` jest znany, możemy go użyć gdziekolwiek, na przykład w poleceniu `print()`. Możemy użyć dowolnej nazwy, musimy tylko przestrzegać kilku prostych zasad, takich jak nieużywanie spacji lub znaków interpunkcyjnych i nieużywanie słów kluczowych Python. Na przykład, możemy napisać:


```python
hello = "my own version of hello"
print(hello)
```

Teraz `hello` nie jest już niezdefiniowane. Zmienne mogą być modyfikowane w dowolnym momencie, dlatego są nazywane zmiennymi, ich zawartość może się zmieniać. Na przykład:


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

Zmieniliśmy wartość `myVariable`. Możemy również kopiować zmienne:


```python
var1 = "hello"
var2 = var1
print(var2)
```

Zaleca się nadawanie zmiennym znaczących nazw. Po pewnym czasie nie będziesz pamiętać, co reprezentuje zmienna o nazwie `a`. Ale jeśli nazwiesz ją na przykład `myWelcomeMessage`, łatwo zapamiętasz jej przeznaczenie. Dodatkowo, twój kod jest o krok bliżej do bycia samodokumentującym się.

Wielkość liter jest bardzo ważna, 

## Liczby

Oczywiście programy w Python mogą obsługiwać wszystkie rodzaje danych, nie tylko ciągi tekstowe. Jedna rzecz jest ważna, Python musi wiedzieć z jakim rodzajem danych ma do czynienia. W naszym przykładzie print hello widzieliśmy, że polecenie `print()` rozpoznało nasz ciąg `"hello"`. Używając znaków `" "`, określiliśmy, że to, co następuje, jest ciągiem tekstowym.

Zawsze możemy sprawdzić typ danych zmiennej za pomocą polecenia `type()`:


```python
myVar = "hello"
type(myVar)
```

Poinformuje nas, że zawartość `myVar` to `'str'`, co jest skrótem od string. Mamy również inne podstawowe typy danych, takie jak liczby całkowite i zmiennoprzecinkowe:


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python wie, że 10 i 20 są liczbami całkowitymi, więc są one przechowywane jako `'int'`, a Python może zrobić z nimi wszystko, co może zrobić z liczbami całkowitymi. Spójrz na wyniki tego działania:


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Tutaj zmusiliśmy Pythona do wzięcia pod uwagę, że nasze dwie zmienne nie są liczbami, ale fragmentami tekstu. Python może dodać do siebie dwa fragmenty tekstu, choć w takim przypadku oczywiście nie wykona żadnych działań arytmetycznych. Ale mówiliśmy o liczbach całkowitych. Istnieją również liczby zmiennoprzecinkowe. Różnica polega na tym, że liczby zmiennoprzecinkowe mogą mieć część dziesiętną, a liczby całkowite nie:


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Liczby całkowite i zmiennoprzecinkowe mogą być mieszane bez problemów:


```python
total = var1 + var2
print(total)
print(type(total))
```

Ponieważ `var2` jest liczbą zmiennoprzecinkową, interpreter automatycznie decyduje, że wynik również musi być liczbą zmiennoprzecinkową. Istnieją jednak przypadki, w których interpreter nie wie, jakiego typu użyć. Na przykład:


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

Powoduje to błąd, `varA` jest łańcuchem znaków, a `varB` jest liczbą całkowitą i interpreter nie wie, co zrobić. Możemy jednak wymusić konwersję między typami:


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Teraz, gdy obie zmienne są łańcuchami, operacja działa. Zwróć uwagę, że \"stringowaliśmy\" `varB` w czasie drukowania, ale nie zmieniliśmy samego `varB`. Gdybyśmy chcieli zmienić `varB` na stałe w ciąg znaków, musielibyśmy wykonać tę operację:


```python
varB = str(varB)
```

Możemy również użyć `int()` i `float()` do konwersji na liczbę całkowitą i zmiennoprzecinkową, jeśli chcemy:


```python
varA = "123"
print(int(varA))
print(float(varA))
```

Pewnie zauważyłeś, że użyliśmy polecenia `print()` na kilka sposobów. Drukowaliśmy zmienne, sumy, kilka rzeczy oddzielonych przecinkami, a nawet wynik innego polecenia z języka Python. Być może zauważyłeś również, że te dwa polecenia:


```python
type(varA)
print(type(varA))
```

daje ten sam wynik. Dzieje się tak, ponieważ jesteśmy w interpreterze i wszystko jest automatycznie drukowane. Kiedy piszemy bardziej złożone programy, które działają poza interpreterem, nie będą one drukowane automatycznie, więc będziemy musieli użyć polecenia `print()`. Mając to na uwadze, przestańmy go tutaj używać. Od teraz będziemy po prostu pisać:


```python
myVar = "hello friends"
myVar
```


{{Top}}



## Listy

Innym przydatnym typem danych jest lista. Lista jest zbiorem innych danych. Aby zdefiniować listę używamy `[ ]`:


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Jak widać, lista może zawierać dowolny typ danych. Z listą można robić wiele rzeczy. Na przykład policzyć jej elementy:


```python
len(myOtherList)
```

Lub pobrać jeden element:


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

Podczas gdy komenda `len()` zwraca całkowitą liczbę elementów na liście, pierwszy element na liście jest zawsze na pozycji `0`, więc w naszym `myOtherList` `"Bob"` będzie na pozycji `2`. Możemy zrobić znacznie więcej z listami, takimi jak sortowanie elementów i usuwanie lub dodawanie elementów.

Co ciekawe, ciąg tekstowy jest bardzo podobny do listy znaków w języku Python. Spróbuj zrobić to:


```python
myvar = "hello"
len(myvar)
myvar[2]
```

Zazwyczaj to, co można zrobić z listami, można również zrobić z ciągami. W rzeczywistości zarówno listy, jak i ciągi znaków są sekwencjami.

Oprócz ciągów znaków, liczb całkowitych, zmiennoprzecinkowych i list, istnieje więcej wbudowanych typów danych, takich jak słowniki, a nawet można tworzyć własne typy danych za pomocą klas. 

## Wcięcia

Jednym z ważnych zastosowań list jest możliwość \"przeglądania\" ich i robienia czegoś z każdym elementem. Na przykład spójrz na to:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```

Wykonaliśmy iterację (w żargonie programistycznym) po naszej liście za pomocą polecenia `for in` i zrobiliśmy coś z każdym z elementów. Zwróć uwagę na specjalną składnię: polecenie `for` kończy się `:`, wskazując, że następne polecenie będzie blokiem jednego lub więcej poleceń. W interpreterze, natychmiast po wprowadzeniu wiersza poleceń kończącego się `:`, znak zachęty wiersza poleceń zmieni się na `…`, co oznacza, że Python wie, że jest jeszcze coś do zrobienia.

Skąd interpreter będzie wiedział, ile kolejnych linii będzie musiało zostać wykonanych wewnątrz operacji `for in`? W tej kwestii Python polega na wcięciach. Następne linie muszą zaczynać się od pustej spacji, lub kilku pustych spacji, lub tabulatora, lub kilku tabulatorów. Dopóki wcięcie pozostaje takie samo, linie będą uważane za część bloku `for in`. Jeśli zaczniesz jedną linię od 2 spacji, a następną od 4, pojawi się błąd. Kiedy skończysz, po prostu napisz kolejną linię bez wcięć lub naciśnij **Enter**, aby powrócić z bloku `for in`

Wcięcia pomagają również w czytelności programu. Jeśli użyjesz dużych wcięć *(na przykład użyjesz tabulatorów zamiast spacji)* podczas pisania dużego programu, będziesz mieć wyraźny widok na to, co jest wykonywane wewnątrz czego. Zobaczymy, że inne polecenia również używają wciętych bloków kodu.

Komenda `for in` może być używana do wielu rzeczy, które muszą być wykonane więcej niż jeden raz. Można ją na przykład połączyć z poleceniem `range()`:


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("")
print(total)
```

Jeśli uruchamiałeś przykłady kodu w interpreterze poprzez kopiuj-wklej, poprzedni blok tekstu spowoduje wyświetlenie błędu. Zamiast tego skopiuj do końca wciętego bloku, tj. do końca linii `total <nowiki>=</nowiki> total + number`, a następnie wklej w interpreterze. W interpreterze naciskaj **Enter**, aż zniknie trzykropkowy znak zachęty i kod zostanie uruchomiony. Następnie skopiuj dwie ostatnie linie, po czym naciśnij **Enter**. Powinna pojawić się ostateczna odpowiedź.

Jeśli wpiszesz do interpretera `help(range)` zobaczysz:


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Tutaj nawiasy kwadratowe oznaczają opcjonalny parametr. Oczekuje się jednak, że wszystkie będą liczbami całkowitymi. Poniżej wymusimy, aby parametr step był liczbą całkowitą przy użyciu `int()`:


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
    print(float(i) / number)
```

Kolejny przykład `range()`:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```

Komenda `range()` ma również tę dziwną cechę, że zaczyna się od `0` *(jeśli nie podasz liczby początkowej)*, a jego ostatnia liczba będzie o jeden mniejsza niż podana liczba końcowa. Dzieje się tak oczywiście dlatego, że działa dobrze z innymi poleceniami Python. Na przykład:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```

Innym interesującym zastosowaniem wciętych bloków jest polecenie `if`. Polecenie to wykonuje blok kodu tylko wtedy, gdy spełniony jest określony warunek, na przykład:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```

Oczywiście zawsze spowoduje to wydrukowanie zdania, ale spróbuj zastąpić drugą linię:


```python
if "Lucky" in alldaltons:
```

Wtedy nic nie zostanie wydrukowane. Możemy również określić instrukcję `else`:


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```


{{Top}}



## Funkcje

Istnieje bardzo niewiele [standardowych poleceń Python](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) i znamy już kilka z nich. Można jednak tworzyć własne polecenia. W rzeczywistości większość dodatkowych modułów, które można podłączyć do instalacji Pythona, robi właśnie to - dodaje polecenia, których można używać. Niestandardowa komenda w Pythonie nazywana jest funkcją i jest tworzona w następujący sposób:


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```

Polecenie `def()` definiuje nową funkcję, nadaje jej nazwę, a wewnątrz nawiasów definiuje argumenty, których funkcja będzie używać. Argumenty to dane, które zostaną przekazane do funkcji. Na przykład, spójrz na polecenie `len()`. Jeśli po prostu napiszesz `len()`, Python powie ci, że potrzebuje argumentu. Co jest oczywiste: chcesz poznać długość czegoś. Jeśli napiszesz `len(myList)` to `myList` jest argumentem, który przekazujesz do funkcji `len()`. Funkcja `len()` jest zdefiniowana w taki sposób, że wie, co zrobić z tym argumentem. To samo zrobiliśmy z naszą funkcją `printsqm`.

Nazwa `myValue` może być dowolna i będzie używana tylko wewnątrz funkcji. Jest to po prostu nazwa, którą nadajesz argumentowi, abyś mógł coś z nim zrobić. Definiując argumenty, informujesz również funkcję, ilu argumentów może oczekiwać. Na przykład, jeśli zrobisz tak:


```python
printsqm(45, 34)
```

wystąpi błąd. Nasza funkcja została zaprogramowana do przyjmowania tylko jednego argumentu, ale otrzymała dwa, `45` i `34`. Wypróbujmy inny przykład:


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Tutaj stworzyliśmy funkcję, która otrzymuje dwa argumenty, sumuje je i zwraca tę wartość. Zwracanie czegoś jest bardzo przydatne, ponieważ możemy zrobić coś z wynikiem, na przykład zapisać go w zmiennej 

## Moduły

Teraz, gdy masz już dobre pojęcie o tym, jak działa Python, musisz wiedzieć jeszcze jedną rzecz: jak pracować z plikami i modułami.

Do tej pory pisaliśmy instrukcje Python linia po linii w interpreterze. Ta metoda nie jest oczywiście odpowiednia dla większych programów. Zwykle kod programów Python jest przechowywany w plikach z rozszerzeniem **.py**. Są to zwykłe pliki tekstowe, a do ich tworzenia i edycji można użyć dowolnego edytora tekstu *(Linux Gedit, Emacs, vi, Kate lub nawet notatnika Windows)*.

Istnieje kilka sposobów na wykonanie programu w języku Python. W systemie Windows wystarczy kliknąć plik prawym przyciskiem myszy, otworzyć go w środowisku Python i wykonać. Ale można również wykonać go z poziomu samego interpretera Python. W tym celu interpreter musi wiedzieć, gdzie znajduje się program. We FreeCAD najprostszym sposobem jest umieszczenie programu w folderze, który interpreter Python dla FreeCAD zna domyślnie, takim jak folder użytkownika FreeCAD **Mod**:

-   W systemie Linux jest to zazwyczaj **/home/<nazwa użytkownika>/.local/share/FreeCAD/Mod/** ({{VersionPlus/pl|0.20}}) lub **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/pl|0.19}}).
-   Na macOS jest to zazwyczaj **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.
-   W systemie Windows jest to **%APPDATA%\FreeCAD\Mod\**, którym zwykle jest **C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\**.

Dodajmy tam podfolder o nazwie **scripts**, a następnie napiszmy taki plik:


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```

Zapisz plik jako **myTest.py** w folderze **scripts** i w oknie interpretera wpisz:


```python
import myTest
```

bez rozszerzenia **.py**. Spowoduje to wykonanie zawartości pliku, linia po linii, tak jakbyśmy napisali go w interpreterze. Funkcja sumy zostanie utworzona, a wiadomość zostanie wydrukowana. Pliki zawierające funkcje, takie jak nasza, nazywane są modułami.

Kiedy piszemy funkcję `sum()` w interpreterze, wykonujemy ją w ten sposób:


```python
sum(14, 45)
```

Kiedy jednak importujemy moduł zawierający funkcję `sum()`, składnia jest nieco inna:


```python
myTest.sum(14, 45)
```

Oznacza to, że moduł jest importowany jako \"kontener\", a wszystkie jego funkcje znajdują się wewnątrz tego kontenera. Jest to bardzo przydatne, ponieważ możemy importować wiele modułów i utrzymywać wszystko dobrze zorganizowane. Zasadniczo, gdy widzisz `something.somethingElse`, z kropką pomiędzy, oznacza to, że `somethingElse` znajduje się wewnątrz `something`.

Możemy również zaimportować naszą funkcję sum() bezpośrednio do głównej przestrzeni interpretera:


```python
from myTest import *
sum(12, 54)
```

Prawie wszystkie moduły to robią: definiują funkcje, nowe typy danych i klasy, których można używać w interpreterze lub we własnych modułach Pythona, ponieważ nic nie stoi na przeszkodzie, aby importować inne moduły wewnątrz swojego modułu!

Skąd mamy wiedzieć, jakie moduły posiadamy, jakie funkcje się w nich znajdują i jak ich używać *(czyli jakich argumentów potrzebują)*? Widzieliśmy już, że Python posiada funkcję `help()`. Wykonanie:


```python
help("modules")
```

da nam listę wszystkich dostępnych modułów. Możemy zaimportować dowolny z nich i przeglądać jego zawartość za pomocą polecenia `dir()`:


```python
import math
dir(math)
```

Zobaczymy wszystkie funkcje zawarte w module `math`, a także dziwne rzeczy o nazwach `__doc__`, `__file__`, `__name__`. Każda funkcja w dobrze stworzonym module ma `__doc__`, który wyjaśnia, jak z niej korzystać. Na przykład widzimy, że w module matematycznym znajduje się funkcja `sin()`. Chcesz wiedzieć, jak z niej korzystać? 
```python
print(math.sin.__doc__)
```

Może to nie być oczywiste, ale po obu stronach `doc` znajdują się dwa znaki podkreślenia.

I wreszcie ostatnia wskazówka: Podczas pracy nad nowym lub istniejącym kodem lepiej nie używać rozszerzenia pliku makra FreeCAD, **.FCMacro**, ale zamiast tego używać standardowego rozszerzenia **.py**. Dzieje się tak, ponieważ Python nie rozpoznaje rozszerzenia **.FCMacro**. Jeśli użyjesz **.py**, twój kod może być łatwo załadowany za pomocą `import`, jak już widzieliśmy, a także przeładowany za pomocą `importlib.reload()`:


```python
import importlib
importlib.reload(myTest)
```

Istnieje jednak alternatywa:


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```


{{Top}}



## Rozpoczęcie pracy z FreeCAD 

Mamy nadzieję, że masz teraz wyobrażenie o tym, jak działa Python i możesz zacząć odkrywać, co FreeCAD ma do zaoferowania. Wszystkie funkcje Python FreeCAD są dobrze zorganizowane w różnych modułach. Niektóre z nich są już załadowane (zaimportowane) podczas uruchamiania FreeCAD. Wystarczy spróbować:


```python
dir()
```


{{Top}}



## Uwagi

-   FreeCAD został pierwotnie zaprojektowany do pracy ze środowiskiem Python 2. Ponieważ Python 2 osiągnął koniec swojego życia w 2020 r., przyszły rozwój FreeCAD będzie odbywał się wyłącznie w Pythonie 3, a kompatybilność wsteczna nie będzie obsługiwana.
-   Znacznie więcej informacji na temat Pythona można znaleźć w [oficjalnym przewodniku po Pythonie](https://docs.python.org/3/tutorial/index.html) i [oficjalnym dokumencie referencyjnym Python](https://docs.python.org/3/reference/).


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Introduction to Python/pl
