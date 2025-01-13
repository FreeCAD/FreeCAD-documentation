# Extra python modules/pl
## Informacje ogólne 

Ta strona zawiera listę kilku dodatkowych modułów środowiska Python lub innych elementów oprogramowania, które można pobrać z Internetu i dodać do swojej instalacji FreeCAD.



## PySide

-   strona główna *(PySide)*: [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   licencja: LGPL
-   opcjonalny, ale wymagany przez kilka modułów: Rysunek Roboczy, BIM, Statek, Wykres, OpenSCAD, Arkusz Kalkulacyjny

PySide jest wymagany przez kilka modułów FreeCAD, aby uzyskać dostęp do interfejsu Qt FreeCAD. Jest on już dołączony do wersji FreeCAD dla systemu Windows i jest zwykle instalowany automatycznie przez FreeCAD w systemie Linux podczas instalacji z oficjalnych repozytoriów. Jeśli te moduły *(Rysunek Roboczy, BIM itp.)* są włączone po zainstalowaniu FreeCAD, oznacza to, że PySide już tam jest i nie trzeba nic więcej robić.

**Uwaga:** FreeCAD stopniowo odchodził od PyQt po wersji 0.13, na rzecz [PySide](http://qt-project.org/wiki/PySide), który wykonuje dokładnie to samo zadanie, ale ma licencję *(LGPL)* bardziej kompatybilną z FreeCAD.



## Instalacja



#### Linux

Najprostszym sposobem na zainstalowanie PySide jest skorzystanie z menedżera pakietów danej dystrybucji. W systemach Debian / Ubuntu nazwa pakietu to zazwyczaj *python-PySide*, podczas gdy w systemach opartych na RPM nosi on nazwę *pyside*. Niezbędne zależności *(Qt i SIP)* zostaną pobrane automatycznie.



#### Windows

Program można pobrać ze strony <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads . Przed instalacją PySide należy zainstalować biblioteki Qt i SIP *(co zostanie udokumentowane)*.



#### Mac OS 

PySide na Maca może być zainstalowany przez `homebrew` lub `port`. Więcej informacji można znaleźć w [Instalacja zależności](Compile_on_MacOS/pl#Instalacja_zależności.md).



### Użycie

Po zainstalowaniu można sprawdzić, czy wszystko działa, wpisując w konsoli Python programu FreeCAD:


```python
import PySide
```

Aby uzyskać dostęp do interfejsu programu FreeCAD, należy wpisać:


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Teraz możesz zacząć poznawać interfejs za pomocą polecenia dir(). Możesz dodać nowe elementy, takie jak niestandardowy widżet, za pomocą poleceń takich jak:


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Praca z Unicode:


```python
text = text.encode('utf-8')
```

Praca z QFileDialog i OpenFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Praca z QFileDialog i SaveFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
```



### Dokumentacja dodatkowa 

-   [Oficjalna strona dokumentacji Qt](https://doc.qt.io/qt.html#qtforpython)



## Pivy

-   strona główna: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   licencja: BSD.
-   opcjonalny, ale wymagany przez kilka modułów FreeCAD: Rysunek Roboczy, BIM.

Pivy jest wymagany przez kilka modułów, aby uzyskać dostęp do widoku 3D FreeCAD. W systemie Windows Pivy jest już dołączony do instalatora FreeCAD, a w systemie Linux jest zwykle instalowany automatycznie po zainstalowaniu FreeCAD z oficjalnego repozytorium. Na macOS niestety będziesz musiał samodzielnie skompilować pivy.



### Instalacja 



#### Wymagania wstępne 

Myślę, że przed kompilacją Pivy będziesz chciał mieć zainstalowane Coin i SoQt.

Odkryłem, że do kompilacji na Macu wystarczy zainstalować [Coin3 pakiet binarny](http://www.coin3d.org/lib/plonesoftwarecenter_view). Próba zainstalowania monety z MacPorts była problematyczna: próbowałem dodać wiele pakietów X Windows i ostatecznie zawiesiłem się z błędem skryptu.

Dla Fedory znalazłem RPM z Coin3.

SoQt skompilowany ze źródła [1](http://www.coin3d.org/lib/soqt/releases/1.5.0) działa dobrze na Macu i Linuksie.



#### Debian oraz Ubuntu 

Począwszy od Debiana Squeeze i Ubuntu Lucid, pivy będzie dostępne bezpośrednio z oficjalnych repozytoriów, oszczędzając nam wiele kłopotów. W międzyczasie możesz pobrać jeden z pakietów *(dla Debiana i Ubuntu Karmic)* dostępnych na stronach [pobierania](Download/pl.md) lub skompilować go samodzielnie.

Najlepszym sposobem na łatwą kompilację pivy jest pobranie pakietu źródłowego Debiana dla pivy i utworzenie pakietu za pomocą debuild. Jest to ten sam kod źródłowy z oficjalnej strony pivy, ale ludzie z Debiana dodali kilka poprawek błędów. Kompiluje się również dobrze na ubuntu karmic: <http://packages.debian.org/squeeze/python-pivy> pobierz plik .orig.gz i .diff.gz, następnie rozpakuj oba, a następnie zastosuj .diff do źródła: przejdź do rozpakowanego folderu źródłowego pivy i zastosuj łatkę .diff:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

wtedy:


```python
debuild
```

aby pivy zostało poprawnie wbudowane w oficjalny pakiet instalacyjny. Następnie wystarczy zainstalować pakiet za pomocą gdebi.



#### Inne dystrybucje linuksa 

Najpierw pobierz najnowsze źródła z [repozytorium projektu](https://github.com/coin3d/pivy):

Informacje do uzupełnienia.

Od marca 2012 r. najnowszą wersją jest Pivy-0.5.

Następnie potrzebne jest narzędzie o nazwie SWIG do generowania kodu C++ dla wiązań Python. Pivy-0.5 informuje, że był testowany tylko z SWIG 1.3.31, 1.3.33, 1.3.35 i 1.3.40. Możesz więc pobrać źródłowy tarball dla jednej z tych starych wersji z [<http://www.swig.org>](http://www.swig.org). Następnie rozpakuj go i z wiersza poleceń wykonaj *(jako root)*:


```python
./configure
make
make install (or checkinstall if you use it)
```

Jego utworzenie zajmuje zaledwie kilka sekund.

Alternatywnie, można spróbować kompilacji z nowszą wersją SWIG. Od marca 2012, typową wersją repozytorium jest 2.0.4. Pivy ma niewielki problem z kompilacją z SWIG 2.0.4 na macOS (patrz poniżej), ale wydaje się, że kompiluje się dobrze na Fedora Core 15.

Następnie przejdź do źródeł pivy i wywołaj:


```python
python setup.py build
```

która tworzy pliki źródłowe. Zauważ, że build może wygenerować tysiące ostrzeżeń, ale miejmy nadzieję, że nie będzie żadnych błędów.

Prawdopodobnie jest to przestarzałe, ale możesz napotkać błąd kompilatora, w którym \'const char\*\' nie może zostać przekonwertowane na \'char\*\'. Aby to naprawić, wystarczy napisać \"const\" przed odpowiednimi liniami. Do naprawienia jest sześć linii.

Następnie zainstaluj, wydając polecenie *(jako root)*:


```python
python setup.py install (or checkinstall python setup.py install)
```

To wszystko, `pivy` jest zainstalowany.



#### Mac OS 

Te instrukcje mogą nie być kompletne. Coś zbliżonego do tego działało dla OS 10.7 od marca 2012. Używam MacPorts dla repozytoriów, ale inne opcje powinny również działać.

As for linux, get the latest source:


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

Jeśli nie masz hg, możesz go pobrać z MacPorts:


```python
port install mercurial
```

Następnie, jak wyżej, potrzebujesz SWIG. Powinno to być kwestią:


```python
port install swig
```

Okazało się, że potrzebowałem również:


```python
port install swig-python
```

Od marca 2012, MacPorts SWIG jest w wersji 2.0.4. Jak wspomniano powyżej dla linuxa, może być lepiej pobrać starszą wersję. SWIG 2.0.4 wydaje się mieć błąd, który zatrzymuje budowanie Pivy. Zobacz pierwszą wiadomość w tym [streszczeniu](https://sourceforge.net/mailarchive/message.php?msg_id=28114815).

Można to poprawić, edytując 2 lokalizacje źródłowe, aby dodać odsyłacze: \*arg4, \*arg5 zamiast arg4, arg5. Teraz Pivy powinien się zbudować:


```python
python setup.py build
sudo python setup.py install
```



#### Windows 

Zakładając, że używasz Visual Studio 2005 lub nowszego, powinieneś otworzyć wiersz polecenia za pomocą \"Wiersz polecenia Visual Studio 2005\" z menu Narzędzia. Jeśli interpreter Python nie znajduje się jeszcze w ścieżce systemowej, wykonaj następujące czynności:


```python
set PATH=path_to_python_3.x;%PATH%
```

Aby uruchomić pivy, należy pobrać najnowsze źródła z repozytorium projektu:

Informacje do uzupełnienia.

Następnie potrzebne jest narzędzie o nazwie SWIG do generowania kodu C++ dla wiązań Pythona. Zaleca się użycie wersji 1.3.25 SWIG, nie najnowszej, ponieważ w tej chwili pivy będzie działać poprawnie tylko z wersją 1.3.25. Pobierz pliki binarne dla wersji 1.3.25 ze strony [<http://www.swig.org>](http://www.swig.org). Następnie rozpakuj je i z wiersza poleceń dodaj do ścieżki systemowej


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

i ustaw COINDIR na odpowiednią ścieżkę


```python
set COINDIR=path_to_coin
```

W systemie Windows plik konfiguracyjny pivy domyślnie oczekuje SoWin zamiast SoQt. Nie znalazłem oczywistego sposobu na kompilację z SoQt, więc zmodyfikowałem plik setup.py bezpośrednio. W linii 200 wystarczy usunąć część \'sowin\': (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') *(nie usuwaj nawiasu zamykającego)*.

Następnie przejdź do źródeł pivy i wywołaj:


```python
python setup.py build
```

który tworzy pliki źródłowe. Możesz napotkać błąd kompilatora, gdy nie można znaleźć kilku plików nagłówkowych. W takim przypadku należy dostosować zmienną INCLUDE


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

a jeśli nagłówki SoQt nie znajdują się w tym samym miejscu, co nagłówki Coin również:


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

i wreszcie nagłówki Qt


```python
set INCLUDE=%INCLUDE%;path_to_pyside\include\Qt
```

Jeśli korzystasz z Express Edition Visual Studio, możesz otrzymać wyjątek błędu klucza Python. W takim przypadku należy zmodyfikować kilka rzeczy w pliku msvccompiler.py znajdującym się w instalacji Python.

Przejdź do linii 122 i zastąp linię


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

przez


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Następnie spróbuj ponownie. Jeśli pojawi się drugi błąd jak np.


```python
error: Python was built with Visual Studio 2003;...
```

musisz również zastąpić linię 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

przez


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Spróbuj ponownie. Jeśli ponownie pojawi się błąd, taki jak


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

następnie należy sprawdzić zmienne środowiskowe DISTUTILS_USE_SDK i MSSDK za pomocą


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

Jeśli nie jest jeszcze ustawiony, wystarczy ustawić go np. na 1.


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Teraz możesz napotkać błąd kompilatora, w którym \"const char\*\" nie może zostać przekonwertowany na \"char\*\". Aby to naprawić, wystarczy napisać \"const\" przed w odpowiednich wierszach. Do poprawienia jest sześć linii. Następnie skopiuj wygenerowany katalog pivy do miejsca, w którym interpreter Pythona we FreeCAD może go znaleźć.



### Użycie 

Aby sprawdzić, czy Pivy jest poprawnie zainstalowany:


```python
import pivy
```

Aby Pivy uzyskał dostęp do scenorysu FreeCAD, wykonaj następujące czynności:


```python
from pivy import coin
App.newDocument() # Open a document and a view
view = Gui.ActiveDocument.ActiveView
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene
```

Możesz teraz eksplorować FCSceneGraph za pomocą polecenia dir().



### Dokumentacja dodatkowa 

Niestety dokumentacja na temat pivy jest wciąż prawie nieobecna w sieci. Ale dokumentacja Coin może okazać się przydatna, ponieważ pivy po prostu tłumaczy funkcje, węzły i metody Coin w Python, wszystko zachowuje tę samą nazwę i właściwości, pamiętając o różnicach w składni między C i Pythonem:

-   <https://github.com/coin3d/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - \"biblia\" języka opisu sceny programu Inventor.

Możesz również spojrzeć na plik Draft.py w folderze FreeCAD Mod/Draft, ponieważ w dużym stopniu wykorzystuje on pivy.



## pyCollada

-   strona główna: <https://pycollada.github.io>
-   licencja: BSD.
-   opcjonalne, potrzebne do umożliwienia importu i eksportu plików Collada *(.DAE)*.

pyCollada to biblioteka Python, która umożliwia programom odczytywanie i zapisywanie plików [Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA). Po zainstalowaniu pyCollada w systemie, FreeCAD będzie w stanie obsługiwać import i eksport w formacie pliku Collada.



### Instalacja 



#### Linux 


```python
sudo apt-get install python3-collada
```

Możesz sprawdzić, czy pycollada została poprawnie zainstalowana, wydając polecenie w konsoli Python:


```python
import collada
```

Jeśli nic nie zwróci *(brak komunikatu o błędzie)*, wszystko jest w porządku



#### Linux AppImages i Snaps 

Wklej ten kod do [konsoli Python](Python_console/pl.md):


```python
import addonmanager_utilities as utils
import subprocess
import os

if hasattr(utils, "get_python_exe"):
    # For v0.21:
    python_exe = utils.get_python_exe()
else:
    # For v0.22/v1.0:
    from freecad.utils import get_python_exe

python_exe = get_python_exe()
vendor_path = utils.get_pip_target_directory()
if not os.path.exists(vendor_path):
    os.makedirs(vendor_path)

subprocess.run(
    [
        python_exe,
        "-m",
        "pip",
        "install",
        "--disable-pip-version-check",
        "--target",
        vendor_path,
        "pycollada",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    timeout=120,
    check=True,
)
```



#### Windows 

W systemie Windows od wersji 0.15 pycollada jest zawarta zarówno w wersji FreeCAD, jak i w kompilacjach deweloperskich, więc nie są wymagane żadne dodatkowe kroki.



#### MacOS

Jeśli korzystasz z wersji Homebrew FreeCAD, możesz zainstalować pycollada w swoim systemie Python za pomocą programu.

Jeśli musisz zainstalować program:


```python
$ sudo easy_install pip
```

Zainstaluj pycollada:


```python
$ sudo pip install pycollada
```

Jeśli używasz binarnej wersji FreeCAD, możesz polecić programowi, aby zainstalował pycollada w pakietach witryn wewnątrz FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python3.x/site-packages" pycollada
```

lub po pobraniu kodu pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python3.x/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.2x.yyyy.app/Contents
```



## IfcOpenShell

-   strona główna: <http://www.ifcopenshell.org>
-   licencja: LGPL.
-   opcjonalne, potrzebne do rozszerzenia możliwości importu plików IFC.

IFCOpenShell jest obecnie rozwijaną biblioteką, która umożliwia importowanie (a wkrótce również eksportowanie) plików [Industry Foundation Classes *(\*.IFC)*](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). IFC jest rozszerzeniem formatu STEP i staje się standardem w przepływach pracy [BIM](http://en.wikipedia.org/wiki/Building_information_modeling). Gdy ifcopenshell jest poprawnie zainstalowany w systemie, Środowisko pracy FreeCAD [BIM](BIM_Workbench/pl.md) wykryje go i użyje do importowania plików IFC, zamiast wbudowanego podstawowego importera. Ponieważ ifcopenshell jest oparty na OpenCasCade, podobnie jak FreeCAD, jakość importu jest bardzo wysoka, tworząc wysokiej jakości geometrię brył.



### Instalacja 



#### Linux 

Instrukcje instalacji można znaleźć [tutaj](https://docs.ifcopenshell.org/ifcopenshell-python/installation.html).

Możesz sprawdzić, czy ifcopenshell został poprawnie zainstalowany, wydając polecenie w konsoli Python:


```python
import ifcopenshell
```

Jeśli nic nie zwróci *(brak komunikatu o błędzie)*, wszystko jest w porządku



#### Windows i macOS 

IfcOpenShell jest zawarty zarówno w wydaniu FreeCAD, jak i w kompilacjach deweloperskich, więc nie są wymagane żadne dodatkowe kroki.



### Odnośniki internetowe 

Poradnik [Import / Eksport IFC - kompilacja IfcOpenShell](Import/Eksport_IFC_-_kompilacja_IfcOpenShell.md)



## LazyLoader

LazyLoader to moduł Python, który umożliwia odroczone ładowanie, a jednocześnie importowanie na początku skryptu. Jest to przydatne, jeśli importujesz inny moduł, który jest powolny i jest używany kilka razy w skrypcie. Korzystanie z LazyLoader może poprawić czas uruchamiania środowiska pracy, ale moduł nadal będzie musiał zostać załadowany przy pierwszym użyciu.



### Instalacja 

LazyLoader jest dołączony do FreeCAD v0.19



### Użycie 

Będziesz musiał zaimportować LazyLoader, a następnie zmienić import dowolnego modułu, który chcesz poddać odroczeniu.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

Zmienna Part to nazwa modułu w skrypcie. Możesz powtórzyć \"import Part as P\", zmieniając zmienną.


```python
P = LazyLoader('Part', globals(), 'Part')
```

You can also import a module from a package. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` Nie można importować pojedynczych funkcji, tylko całe moduły.



### Odnośniki internetowe 

-   Oryginalne źródło: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Dalsze wyjaśnienia: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Kod w kodzie źródłowym FreeCAD: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Dyskusja na forum: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>



---
⏵ [documentation index](../README.md) > [Python Code](Category_Python Code.md) > [Developer Documentation](Category_Developer Documentation.md) > Extra python modules/pl
