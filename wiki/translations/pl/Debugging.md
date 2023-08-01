# Debugging/pl
{{TOCright}}



## Najpierw przetestuj 

Zanim przejdziesz przez ból debugowania użyj [środowiska pracy Test](Testing/pl.md) aby sprawdzić czy standardowe testy działają poprawnie. Jeśli testy nie są kompletne, prawdopodobnie instalacja jest uszkodzona.



## Wiersz poleceń 

**Debugowanie** w programie FreeCAD jest wspierane przez kilka wewnętrznych mechanizmów. Wersja programu FreeCAD z wierszem poleceń dostarcza kilka opcji do obsługi debugowania.

Są to obecnie rozpoznawane opcje w programie FreeCAD w wersji 0.19:

Opcje ogólne:

 -v [ --version ]     Drukuje ciąg znaków wersji.
 -h [ --help ]        Drukuje komunikat pomocy
 -c [ --console ]     Uruchamia się w trybie konsolowym
 --response-file arg  Można też podać z '@name'
 --dump-config        Zrzuca konfigurację
 --get-config arg     Wypisuje wartość żądanego klucza konfiguracyjnego

Konfiguracja:

 -l [ --write-log ]        Zapisuje plik dziennika do:
                           $HOME/.local/share/FreeCAD.log (Linux)
                           $HOME/Library/Application\ Support/FreeCAD/FreeCAD.log (macOS)
                           %APPDATA%FreeCAD/FreeCAD.log (Windows)
 --log-file arg            W przeciwieństwie do --write-log pozwala na logowanie do
                           dowolnego pliku. 
 -u [ --user-cfg ] arg     Plik konfiguracyjny użytkownika do ładowania / zapisywania
                           ustawień użytkownika
 -s [ --system-cfg ] arg   Plik konfiguracyjny systemu do załadowania / zapisu
                           ustawień systemowych
 -t [ --run-test ] arg     Przypadek testowy - lub 0 dla wszystkich
 -M [ --module-path ] arg  Ścieżki do dodatkowych modułów
 -P [ --python-path ] arg  Dodatkowe ścieżki dostępu do Pythona
 --single-instance         Pozwala na uruchomienie pojedynczej instancji aplikacji



## Generowanie śladu wstecznego 

Jeżeli używasz wersji FreeCAD z ostatniej fazy rozwoju, może ona ulec awarii. Możesz pomóc w rozwiązaniu takich problemów poprzez dostarczenie deweloperom *śladów wstecz*. Aby to zrobić, musisz mieć uruchomiony *debug build* oprogramowania. *Debug build* jest parametrem, który jest ustawiany w czasie kompilacji, więc albo będziesz musiał skompilować FreeCAD samodzielnie, albo zdobyć prekompilowaną wersję *debug*.



### Dla systemu Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Debugowanie w systemie Linux →


<div class="mw-collapsible-content">

Wymagania wstępne:

-   zainstalowany pakiet oprogramowania gdb
-   debug build FreeCAD *(w tym momencie dostępny tylko przez [kompilację ze źródeł](Compile_on_Linux/pl#Dla_kompilacji_Debug.md))*
-   model FreeCAD, który powoduje awarię

Postępowanie: W oknie terminala wprowadź następujące dane:

Znajdź binaria FreeCAD w swoim systemie:


```python
$ whereis freecad
freecad: /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

GNUdebugger wyśle kilka informacji inicjalizujących. Polecenie *(gdb)* pokazuje, że GNUDebugger jest uruchomiony w terminalu, teraz wprowadź dane:


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD zostanie teraz uruchomiony. Wykonaj czynności, które powodują awarię lub zawieszenie programu FreeCAD, a następnie wpisz w oknie terminala:


```python
(gdb) bt
```

Spowoduje to wygenerowanie długiej listy tego, co dokładnie robił program, kiedy się zawiesił lub przestał działać. Dołącz to do swojego raportu o problemie.


```python
(gdb) bt full
```

Wypisuje również wartości zmiennych lokalnych. Może to być połączone z liczbą, aby ograniczyć ilość wyświetlanych klatek.


</div>


</div>



### Dla systemu macOS 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Debugowanie w systemie macOS →


<div class="mw-collapsible-content">

Wymagania wstępne:

-   zainstalowany pakiet oprogramowania lldb
-   debug build FreeCAD
-   model FreeCAD, który powoduje awarię

Postępowanie: W oknie terminala wprowadź następujące dane:


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB wyśle kilka informacji inicjalizujących. Polecenie *(lldb)* pokazuje, że GNUDebugger jest uruchomiony w terminalu, teraz wprowadź dane:


```python
(lldb) run
```

FreeCAD zostanie teraz uruchomiony. Wykonaj czynności, które powodują awarię lub zawieszenie programu FreeCAD, a następnie wpisz w oknie terminala:


```python
(lldb) bt
```

Spowoduje to wygenerowanie długiej listy tego, co dokładnie robił program, kiedy się zawiesił lub przestał działać. Dołącz to do swojego raportu o problemie.


</div>


</div>



## Lista bibliotek załadowanych przez FreeCAD 

*(Dotyczy systemów Linux i macOS)*

Czasami pomocne staje się określenie, jakie biblioteki ładuje FreeCAD, szczególnie jeśli ładowane są biblioteki o tej samej nazwie, ale w różnych wersjach *(kolizja wersji)*. Aby zobaczyć, które biblioteki są ładowane przez FreeCAD podczas awarii, powinieneś otworzyć terminal i uruchomić go w debugerze. W drugim oknie terminala znajdź id procesu dla FreeCAD:


`ps -A &#124; grep FreeCAD`

Użyj uzyskanego identyfikatora i podaj go do `lsof`:


` lsof -p process_id`

Wyświetli to długą listę załadowanych zasobów. Tak więc, na przykład, jeśli próbujesz się upewnić, że więcej niż jedna wersja biblioteki Coin3d jest załadowana, przewiń listę lub poszukaj bezpośrednio Coin na liście:


`lsof -p process_id &#124; grep Coin`



## Debugowanie w Python 

Aby uzyskać bardziej nowoczesne podejście do debugowania w środowisku Python, zobacz te posty:

-   [Debugowanie makrodefinicji z VS 2017](https://forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Debugowanie środowisk pracy w Pythonie](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll i Qt5Core.dll nie znaleziono](https://forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Debugowanie w winpdb →


<div class="mw-collapsible-content">

Oto przykład użycia *Winpdb* wewnątrz FreeCAD:

Potrzebujemy debuggera Python *Winpdb*. Jeśli nie masz go zainstalowanego, na Ubuntu/Debianie zainstaluj go za pomocą:


```python
sudo apt-get install winpdb
```

Teraz skonfigurujmy debugger.

1.  Uruchom *Winpdb*.
2.  Ustaw hasło debuggera na \"test\": Przejdź do menu **Plik → Hasło** i ustaw hasło.

Teraz krok po kroku uruchomimy testowy skrypt Python w programie FreeCAD.

1.  Uruchomić winpdb i ustawić hasło *(np. test)*
2.  Utwórz plik Python z tą zawartością


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Uruchom program FreeCAD i załaduj powyższy plik do programu FreeCAD,
2.  Naciśnij klawisz **F6** aby go wykonać,
3.  Teraz FreeCAD przestanie reagować, ponieważ debugger Pythona czeka,
4.  Przełącz się do GUI Windpdb i kliknij na \"Dołącz\". Po kilku sekundach pojawi się element \"\", na którym należy dwukrotnie kliknąć,
5.  Teraz w Winpdb pojawi się aktualnie wykonywany skrypt,
6.  Ustaw punkt przerwanie w ostatniej linii i naciśnij klawisz **F5**,
7.  Teraz naciśnij klawisz **F7**, aby wejść do kodu Python Draft.makeWire.


</div>


</div>



### Kod Visual Studio *(VS Code)* 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Debugowanie kodu VS →


<div class="mw-collapsible-content">

Wymagania wstępne:

-   Pakiet **ptvsd** musi być zainstalowany w Python 3 poza środowiskiem programu FreeCAD, a następnie moduł musi być skopiowany do folderu biblioteki Pythona programu FreeCAD.


```python
# In a cmd window that has a path to you local Python 3:
pip install ptvsd
# Then if your Python is installed in C:\Users\<userid>\AppData\Local\Programs\Python\Python37
# and your FreeCAD is installed in C:\freecad\bin
xcopy "C:\Users\<userid>\AppData\Local\Programs\Python\Python37\Lib\site-packages\ptvsd" "C:\freecad\bin\Lib\site-packages\ptvsd"
```

[strona pypi](https://pypi.org/project/ptvsd/)

[Dokumentacja Visual Studio Code do zdalnego debugowania](https://code.visualstudio.com/docs/python/debugging#_remote-debugging)

Postępowanie:

-   Dodaj następujący kod na początku swojego skryptu


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Dodaj konfigurację debugowania w Visual Studio Code **Debug → Add Configurations...**.
-   Powinna ona wyglądać następująco:




        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },

-   W VS Code dodaj punkt przerwania gdziekolwiek chcesz.
-   Uruchom skrypt w programie FreeCAD. FreeCAD zatrzymuje się w oczekiwaniu na załącznik.
-   W VS Code rozpocznij debugowanie używając stworzonej konfiguracji. Powinieneś zobaczyć zmienne w obszarze debuggera.
-   Podczas ustawiania punktów przerwania VS Code będzie zgłaszał, że nie znalazł pliku .py otwartego w edytorze VS Code.
    -   Zmień \"remoteRoot\": \".\" na \"remoteRoot\": \"\"
    -   Na przykład, jeśli plik Python rezyduje w */home/FC_myscripts/myscript.py*
    -   Zmień na: \"remoteRoot\": \"/home/FC_myscripts\"
    -   Jeśli tylko debugujesz makrodefinicje FreeCAD z folderu makr FreeCAD, a ten folder to \"C:/Users//AppData/Roaming/FreeCAD/Macro\", to użyj:
        -   \"localRoot\": \"C:/Users//AppData/Roaming/FreeCAD/Macro\",
        -   \"remoteRoot\": \"C:/Users//AppData/Roaming/FreeCAD/Macro\".
-   Jeśli twoja makrodefinicja nie może znaleźć ptvsd, mimo że gdzieś go zainstalowało, poprzedź *import ptvsd* znakiem


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

Gdzie ścieżka wskazuje katalog, w którym ptvsd został zainstalowany.

-   W lewej dolnej krawędzi VSCode możesz wybrać plik wykonywalny Python - najlepiej, aby była to wersja spakowana z programem FreeCAD.

W pakiecie dla Maca jest to /Applications/FreeCAD.App/Contents/Resources/bin/python.

Można go zlokalizować w systemie wpisując:


```python
import sys
print(sys.executable)
```

w konsoli Python programu FreeCAD.


</div>


</div>



### Z LiClipse i AppImage 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Debugowanie LiClipse →


<div class="mw-collapsible-content">

-   Wyodrębnij AppImage.


```python
> ./your location/FreeCAD_xxx.AppImage --appimage-extract
> cd squashfs-root/
```

-   Lokalizacja sqashfs-root jest miejscem, do którego później zostanie podłączony debugger.

-   Upewnij się, że możesz rozpocząć sesję FreeCAD z lokalizacji squashfs-root.


```python
squashfs-root> ./usr/bin/freecadcmd
```

-   Powinna uruchomić się sesja wiersza poleceń programu FreeCAD.

-   Zainstaluj [LiClipse](https://www.liclipse.com/).
    -   Dostarczany jest z pydevem i posiada instalatory dla wszystkich platform.
    -   W przypadku linuksa wystarczy rozpakować *(do dowolnej lokalizacji)* i uruchomić.

-   Skonfiguruj liclipse do debugowania.
    -   Kliknij prawym przyciskiem myszy na ikonę pydev *(prawy górny róg)* i wybierz \"Dostosuj\".
        -   Aktywuj opcję \"PyDev Debug\" *(poprzez zaznaczenie pola wyboru, może być też konieczne przejście do zakładki \"Action Set Availability\" i aktywowanie jej)*.
        -   W menu pydev można teraz wybrać opcję \"Uruchom serwer debugowania\".
    -   Użyj menu okno → otwórz perspektywę → inne → debug.
        -   Kliknij prawym przyciskiem myszy ikonę debugowania *(prawy górny róg)* i wybierz polecenie Dostosuj.
        -   Zaznaczenie opcji \"Debuguj\" spowoduje pojawienie się na pasku narzędzi narzędzi narzędzi nawigacyjnych do debugowania.
    -   Otwórz preferencje przez okno menu → preferencje.
        -   W PyDev/Interpreters dodaj \"nowy interpreter przez przeglądanie\".
        -   Dodany interpreter powinien być umieszczony w: `Twoja lokalizacja/squashfs-root/usr/bin/python`.
        -   Jeśli używasz tego tylko z FC, możesz dodać także foldery AddOn workbench, lub zrobić to później w projekcie pydev.

-   Znajdź ścieżkę do `pydevd.py` w swojej instalacji w liclipse.
    -   Coś w stylu: `Twoja lokalizacja/liclipse/plugins/org.python.pydev.xx/pysrc`.
-   Utwórz zwykły projekt pydev w liclipse.
    -   Zaimportuj zewnętrzne źródła, na przykład makro, które chcesz debugować, lub zewnętrzne środowisko pracy.
    -   W makrodefinicji *(lub pliku .py)* dodaj linie kodu:

:   
    
```python
    import sys; sys.path.append("path ending with /pysrc")
    import pydevd; pydevd.settrace()
    
```
    

  - W tym miejscu zostanie zatrzymane wykonywanie makrodefinicji.

-   Uruchom serwer debugowania Liclipse *(menu pydev)*.

-   Uruchom program FreeCAD.


```python
squashfs-root> ./usr/bin/freecad
```

-   Uruchom makrodefinicję *(lub jakikolwiek inny plik z wyzwalaczem `pydevd.settrace()`)* w programie FreeCAD, tak jak robisz to normalnie.

-   Udanego debugowania.

-   Użycie LiClipse do zdalnego debugowania oraz opisane tutaj czynności związane z liclipse powinny działać na każdej platformie. Części związane z AppImage są przeznaczone tylko dla systemu linux.


</div>


</div>



## Debugowanie OpenCasCade 

Dla programistów chcących zagłębić się w kernel OpenCasCade, użytkownik \@abdullah stworzył [wątek](https://forum.freecadweb.org/viewtopic.php?f=10&t=47017) orientacyjny omawiający jak tego dokonać.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Debugging/pl
