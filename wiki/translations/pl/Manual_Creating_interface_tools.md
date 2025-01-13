# Manual:Creating interface tools/pl
{{Manual:TOC}}

W ostatnich dwóch rozdziałach zobaczyliśmy, jak [tworzyć geometrię części](Manual:Creating_and_manipulating_geometry/pl.md) i [tworzyć obiekty parametryczne](Manual:Creating_parametric_objects/pl.md). Brakuje jeszcze jednego elementu, aby uzyskać pełną kontrolę nad FreeCAD: Tworzenie narzędzi, które będą współdziałać z użytkownikiem.

W wielu sytuacjach nie jest bardzo przyjazne dla użytkownika konstruowanie obiektu z zerowymi wartościami, tak jak zrobiliśmy to z prostokątem w poprzednim rozdziale, a następnie prośba o wypełnienie wartości Wysokości i Szerokości w panelu Właściwości. To działa dla bardzo niewielkiej liczby obiektów, ale stanie się bardzo uciążliwe, jeśli trzeba będzie tworzyć wiele prostokątów. Lepszym sposobem byłoby już podanie Wysokości i Szerokości podczas tworzenia prostokąta.

Python oferuje podstawowe narzędzie do wprowadzania tekstu na ekranie:

text = raw_input("Height of the rectangle?")
print("The entered height is ",text)

Wymaga to jednak aktywnej konsoli Python, a kiedy uruchamiamy nasz kod z makrodefinicji, nie zawsze mamy pewność, że konsola Python będzie aktywna.

[Graficzny interfejs użytkownika](https://pl.wikipedia.org/wiki/Graficzny_interfejs_u%C5%BCytkownika) (GUI) - zawierający menu, widoku 3D i inne wizualne komponenty programu FreeCAD - jest zaprojektowany tak, aby uczynić program intuicyjnym i dostępnym. Stanowi pomost między użytkownikiem i wewnętrznymi funkcjami środowiska FreeCAD, pozwalając na efektywną interakcję z programem zarówno początkującym użytkownikom, jak i ekspertom.

GUI programu FreeCAD jest zbudowane przy pomocy [Qt](https://pl.wikipedia.org/wiki/Qt), potężnego i otwartego zestawu narzędzi GUI, które zapewnia szeroki zakres funkcji. Qt oferuje podstawowe bloki do projektowania interfejsu, takie jak oknia dialogowe, przyciski, etykiety, pola do wprowadzania tekstu i menu rozwijane, zbiorczo nazywane \"widżetami\". Te widżety tworzą podstawę doświadczenia użytkownika programu FreeCAD.

Jedną z kluczowych zalet Qt jest jego międzyplatformowa kompatybilność, umożliwiając bezproblemowe uruchamianie programu FreeCAD na różnych systemach operacyjnych, takich jak Windows, macOS i Linux. Ponadto, elastyczność Qt ułatwia deweloperom rozszerzanie i dostosowywanie interfejsu programu FreeCAD poprzez tworzenie nowych pasków narzędzi i menu lub budowanie całkowicie nowych modułów, które integrują się z programem. Ta adaptacyjność sprawia, że FreeCAD pozostaje przyjazny użytkownikom i znacząco rozszerzalny.

Dla użytkowników zainteresowanych tworzeniem skryptów lub opracowywaniem nowych narzędzi, API Pythona programu FreeCAD również daje dostęp do wielu funkcji Qt. Oznacza to, że możesz nie tylko automatyzować zadania, ale również tworzyć własne widżety lub okna dialogowe, które są integrowane bezpośrednio ze środowiskiem FreeCAD.

Narzędzia Qt są bardzo łatwe do użycia z poziomu Pythona dzięki modułowi Pythona o nazwie [PySide](https://en.wikipedia.org/wiki/PySide). PySide to oficjalny moduł Pythona do biblioteki Qt, zapewniający bezpośredni sposób tworzenia i interakcji z widżetami poprzez programowanie. Pozwala deweloperom projektować interfejsy, zarządzać wprowadzaniem danych przez użytkowników (np. odczytywanie tekstu z pól wejściowych) i definiować akcje w oparciu o interakcje użytkowników, takie jak odpowiadanie na wciśnięcie przycisku. Używając PySide, możesz budować własne okna dialogowe, menu i paski narzędzi bezpośrednio z poziomu programu FreeCAD, rozszerzając jego funkcjonalność w sposób, który integruje się bezpośrednio z jego istniejącym interfejsem.

PySide ułatwia połączenie akcji użytkownika z określonymi funkcjami w kodzie. Przykładowo, możesz ustawić przycisk tak, że gdy jest on wciśnięty, uruchamia skrypt wykonujący polecenie lub modyfikujący obiekt w widoku 3D. Ta interaktywna funkcjonalność otwiera nieograniczone możliwości dostosowywania przepływów pracy i automatyzowania powtarzalnych czynności.

Qt udostępnia również inne interesujące narzędzie o nazwie [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), które jest obecnie wbudowane w większą aplikację o nazwie [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator). Umożliwia ono graficzne projektowanie okien dialogowych i paneli interfejsu, zamiast konieczności ich ręcznego kodowania. W tym rozdziale użyjemy Qt Creator do zaprojektowania widżetu panelu, którego użyjemy w panelu **Zadanie** programu FreeCAD. Będziesz więc musiał pobrać i zainstalować Qt Creator z [oficjalnej strony QT](https://www.qt.io/ide/), jeśli korzystasz z systemu Windows lub Mac *(w systemie Linux będzie on zwykle dostępny w aplikacji menedżera oprogramowania)*.

W poniższym ćwiczeniu najpierw utworzymy panel za pomocą Qt Creator, który poprosi o podanie wartości długości, szerokości i wysokości, a następnie utworzymy wokół niego klasę Python, która odczyta wartości wprowadzone przez użytkownika z panelu i utworzy pudełko o podanych wymiarach. Ta klasa Python będzie następnie używana przez FreeCAD do wyświetlania i sterowania panelem zadań:

![](images/Exercise_python_07.jpg )

Zacznijmy od stworzenia widżetu. Uruchom Qt Creator, a następnie menu **File → New File or Project → Qt → Qt Designer Form → Dialog without buttons**. Kliknij **Dalej**, nadaj mu nazwę pliku do zapisania, kliknij **Dalej**, pozostaw wszystkie pola projektu do wartości domyślnej *(\"\")* i **Utwórz**. System zadań FreeCAD automatycznie doda przyciski OK / Anuluj, dlatego wybraliśmy tutaj okno dialogowe bez przycisków.

![](images/Exercise_python_06.jpg )

-   Znajdź **Etykietę** na liście w lewym panelu (pod sekcją Display Widgets) i przeciągnij ją na obszar roboczy naszego widżetu. Kliknij dwukrotnie ostatnio umieszczoną etykietę i zmień jej tekst na **Długość**.
-   Kliknij prawym przyciskiem myszy kanwę widżetu i wybierz **Rozmieść → Rozmieść w siatce**. Spowoduje to przekształcenie naszego widżetu w siatkę z obecnie tylko jedną komórką, zajmowaną przez naszą pierwszą etykietę. Możemy teraz dodać kolejne elementy po lewej, prawej, górnej lub dolnej stronie naszej pierwszej etykiety, a siatka rozszerzy się automatycznie.
-   Dodaj dwie kolejne etykiety poniżej pierwszej i zmień ich tekst na Width i Height:

![](images/Exercise_python_08.jpg )

-   Umieść teraz 3 widżety „Double Spin Box" (pod sekcją Input Widgets) obok naszych etykiet „Długość", „Szerokość" i „Wysokość". Dla każdego z nich, w dolnym prawym panelu, który pokazuje wszystkie dostępne ustawienia dla wybranego widżetu, zlokalizuj „Suffix" i ustaw ich przyrostek na „mm". FreeCAD posiada bardziej zaawansowany widżet, który może obsługiwać różne jednostki, ale nie jest on dostępny w Kreatorze Qt domyślnie *(choć może zostać [skompilowany](Compile_on_Linux/pl#Wtyczka_Qt_designer.md))*, więc na razie skorzystamy z standardowego „Double Spin Box" i dodamy przyrostek „mm", aby upewnić się, że użytkownik wie, w jakich jednostkach pracują:

![](images/Exercise_python_09.jpg )

-   Teraz nasz widżet jest gotowy, musimy tylko upewnić się co do jednej ostatniej rzeczy. Ponieważ FreeCAD będzie musiał uzyskać dostęp do tego widżetu i odczytać wartości długości, szerokości i wysokości, musimy nadać tym widżetom odpowiednie nazwy, abyśmy mogli je łatwo odzyskać z poziomu FreeCAD. Kliknij każde z Double Spin Boxes, a następnie w prawym górnym oknie kliknij dwukrotnie ich Object Name i zmień je na coś łatwego do zapamiętania, na przykład: BoxLength, BoxWidth i BoxHeight:

![](images/Exercise_python_10.jpg )

-   Zapisz plik, możesz teraz zamknąć Qt Creator, reszta zostanie wykonana w Python.
-   Otwórz FreeCAD i utwórz nowe makro z menu **Makrodefinicje → Makrodefinicje \... → Utwórz**.
-   Wklej następujący kod. Upewnij się, że zmieniłeś ścieżkę pliku, aby pasowała do miejsca, w którym zapisałeś plik .ui utworzony w QtCreator:


```python
import FreeCAD,FreeCADGui,Part
 
# CHANGE THE LINE BELOW
path_to_ui = "C:\Users\yorik\Documents\dialog.ui"
 
class BoxTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
 
   def accept(self):
       length = self.form.BoxLength.value()
       width = self.form.BoxWidth.value()
       height = self.form.BoxHeight.value()
       if (length == 0) or (width == 0) or (height == 0):
           print("Error! None of the values can be 0!")
           # we bail out without doing anything
           return
       box = Part.makeBox(length,width,height)
       Part.show(box)
       FreeCADGui.Control.closeDialog()
        
panel = BoxTaskPanel()
FreeCADGui.Control.showDialog(panel)
```

W powyższym kodzie użyliśmy wygodnej funkcji **PySideUic.loadUi** z modułu **FreeCADGui**. Funkcja ta ładuje plik .ui, tworzy z niego widżet Qt i mapuje nazwy, dzięki czemu możemy łatwo uzyskać dostęp do podwidżetu według ich nazw *(np. self.form.BoxLength)*.

Funkcja \"akceptuj\" jest również udogodnieniem oferowanym przez Qt. Gdy w oknie dialogowym znajduje się przycisk \"OK\" *(co ma miejsce domyślnie podczas korzystania z panelu zadań FreeCAD)*, każda funkcja o nazwie \"akceptuj\" zostanie automatycznie wykonana po naciśnięciu przycisku \"OK\". Podobnie, można również dodać funkcję \"odrzuć\", która zostanie wykonana po naciśnięciu przycisku \"Anuluj\". W naszym przypadku pominęliśmy tę funkcję, więc naciśnięcie przycisku \"Anuluj\" spowoduje domyślne zachowanie *(nic nie robi i zamyka okno dialogowe)*.

Jeśli zaimplementujemy którąkolwiek z funkcji akceptacji lub odrzucenia, ich domyślne zachowanie *(nic nie rób i zamknij)* nie będzie już występować. Musimy więc sami zamknąć panel zadań. Odbywa się to za pomocą:


```python
FreeCADGui.Control.closeDialog() 
```

Gdy mamy już nasz BoxTaskPanel, który ma 1 - widżet o nazwie \"self.form\" i 2 - w razie potrzeby funkcje akceptacji i odrzucenia, możemy otworzyć panel zadań za jego pomocą, co odbywa się za pomocą tych dwóch ostatnich wierszy:


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```

Należy pamiętać, że widżet utworzony przez **PySideUic.loadUi** nie jest specyficzny dla FreeCAD, jest to standardowy widżet Qt, który może być używany z innymi narzędziami Qt. Moglibyśmy na przykład wyświetlić za jego pomocą osobne okno dialogowe. Wypróbuj to w konsoli Python FreeCAD *(oczywiście używając poprawnej ścieżki do pliku .ui)*:


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Oczywiście nie dodaliśmy żadnego przycisku \"OK\" lub \"Anuluj\" do naszego okna dialogowego, ponieważ zostało ono stworzone do użycia z panelu zadań FreeCAD, który już zapewnia takie przyciski. Nie ma więc możliwości zamknięcia okna dialogowego *(poza naciśnięciem przycisku zamykania okna)*. Ale funkcja show() tworzy niemodalne okno dialogowe, co oznacza, że nie blokuje reszty interfejsu. Tak więc, gdy nasze okno dialogowe jest nadal otwarte, możemy odczytać wartości pól:


```python
w.BoxHeight.value() 
```

Jest to bardzo przydatne do testowania.

Wreszcie, nie zapominaj, że istnieje znacznie więcej dokumentacji na temat korzystania z widżetów Qt na FreeCAD Wiki, na stronie [Centrum Power użytkowników](Power_users_hub/pl.md), która zawiera poradnik [Tworzenie dialogu](Dialog_creation/pl.md), specjalny 3-częściowy poradnik [PySide](PySide/pl.md), który obszernie omawia ten temat.

## Powiązane odnośniki 

-   [Dokumentacja Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
-   [Instalacja Qt Creator](https://www.qt.io/ide/)
-   [Dokumentacja skryptów FreeCAD Python](Power_users_hub.md)
-   [Tutorial tworzenia dialogów FreeCAD](Dialog_creation.md)
-   [Tutoriale FreeCAD PySide](PySide.md)
-   [http://srinikom.github.io/pyside-docs/index.html Dokumentacja PySide](http://srinikom.github.io/pyside-docs/index.html_Dokumentacja_PySide.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating interface tools/pl
