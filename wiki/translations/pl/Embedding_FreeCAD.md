# Embedding FreeCAD/pl
## Wprowadzenie

FreeCAD może być importowany jako moduł [Python](Python/pl.md) w innych programach lub w samodzielnej konsoli środowiska Python wraz ze wszystkimi jego modułami i komponentami. Możliwe jest nawet zaimportowanie interfejsu użytkownika FreeCAD jako modułu Python, ale z pewnymi ograniczeniami wskazanymi w akapicie [Zastrzeżenia](#Zastrzeżenia.md).



## Używanie FreeCAD bez GUI 

Pierwszym, bezpośrednim, łatwym i użytecznym zastosowaniem jest importowanie dokumentów FreeCAD do programu. W poniższym przykładzie zaimportujemy geometrię części dokumentu FreeCAD do [Blender](http://www.blender.org). Oto kompletny skrypt. Mam nadzieję, że będziesz pod wrażeniem jego prostoty: {{Code|lang=python|code=
<nowiki>
FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.pyd file,
# for Windows you must either use \\ or / in the path, using a single \ is problematic
# FREECADPATH = 'C:\\FreeCAD\\bin'
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}

Pierwszą i ważną częścią jest upewnienie się, że Python znajdzie naszą bibliotekę FreeCAD. Gdy ją znajdzie, wszystkie moduły FreeCAD, takie jak Part *(których również będziemy używać)*, będą dostępne automatycznie. Więc po prostu bierzemy zmienną `sys.path`, która jest miejscem, w którym python szuka modułów, i dołączamy ścieżkę biblioteki FreeCAD. Ta modyfikacja jest tylko tymczasowa i zostanie utracona, gdy zamkniemy nasz interpreter Python. Alternatywnym sposobem może być: utworzenie linku do biblioteki FreeCAD w jednej ze ścieżek wyszukiwania środowiska Python. Zapisałem ścieżkę w stałej (`FREECADPATH`), aby ułatwić innemu użytkownikowi skryptu skonfigurowanie go do własnego systemu. Dla użytkowników Windows ważne jest, aby ścieżka była określona przy użyciu `\\` lub `/` jako separatora zamiast po prostu `\`, ponieważ jest to znak sterujący.


{{Code|lang=python|code=
FREECADPATH = 'C:\\FreeCAD\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
import sys
sys.path.append(FREECADPATH)
}}

Po upewnieniu się, że biblioteka jest załadowana *(sekwencja `try`/`except`)*, możemy teraz pracować z FreeCAD, w taki sam sposób, jak wewnątrz własnego interpretera Python FreeCAD. Otwieramy dokument FreeCAD, który został nam przekazany przez funkcję `main()` i tworzymy listę jego obiektów. Następnie, ponieważ zdecydowaliśmy się dbać tylko o geometrię części, sprawdzamy, czy właściwość Type każdego obiektu zawiera \"`Part`\", a następnie teselujemy go.


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Teselacja tworzy listę wierzchołków i listę ścian zdefiniowanych przez indeksy wierzchołków. Jest to idealne rozwiązanie, ponieważ jest to dokładnie ten sam sposób, w jaki Blender definiuje siatki. Nasze zadanie jest więc śmiesznie proste, po prostu dodajemy zawartość obu list do wierzchołków i ścian siatki Blendera. Kiedy wszystko jest gotowe, po prostu przerysowujemy ekran i to wszystko!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}

Oczywiście ten skrypt jest bardzo prosty (w rzeczywistości stworzyłem bardziej zaawansowany [importer FreeCAD do Blendera](https://yorik.uncreated.net/archive/scripts/blender24/import_freecad.py)), możesz chcieć go rozbudować, na przykład importując również obiekty siatkowe, importując geometrię Części, która nie ma ścian, lub importując inne formaty plików, które FreeCAD potrafi odczytać. Możesz również chcieć eksportować geometrie do dokumentu FreeCAD, co można zrobić w podobny sposób. Możesz też zbudować okno dialogowe, aby użytkownik mógł wybrać, co chce zaimportować, itd. Piękno tego wszystkiego polega na tym, że pozwalasz FreeCAD wykonać podstawową pracę, a jego wyniki prezentujesz w wybranym przez siebie programie.


**Uwaga:**

sprawdź stronę [FreeCAD bez GUI](Headless_FreeCAD/pl.md) aby uzyskać informacje o uruchamianiu programu FreeCAD bez GUI.



## Używanie FreeCAD z GUI 

Od wersji 4.2 Qt ma intrygującą możliwość osadzania wtyczek zależnych od Qt-GUI w aplikacjach innych niż Qt i współdzielenia pętli zdarzeń hosta.

Zwłaszcza w przypadku FreeCAD oznacza to, że może być zaimportowany z poziomu innej aplikacji razem z całym interfejsem użytkownika, gdzie aplikacja nadrzędna ma wtedy pełną kontrolę nad FreeCAD.

Cały kod Pythona do osiągnięcia tego ma tylko dwie linie


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Jeśli aplikacja nadrzędna jest oparta na Qt, to to rozwiązanie powinno działać na wszystkich platformach, które są obsługiwane przez Qt. Jednakże aplikacja nadrzędna powinna korzystać z tej samej wersji Qt, co FreeCAD, ponieważ w przeciwnym razie mogą wystąpić nieoczekiwane błędy podczas działania programu.

Dla aplikacji nieopartych na Qt istnieje jednak kilka ograniczeń, o których należy pamiętać. To rozwiązanie prawdopodobnie nie działa w połączeniu ze wszystkimi innymi zestawami narzędzi. Na Windows działa, o ile aplikacja nadrzędna jest bezpośrednio oparta na Win32 lub innym zestawie narzędzi, który wewnętrznie korzysta z API Win32, takim jak wxWidgets, MFC czy WinForms. Aby to działało pod X11, aplikacja nadrzędna musi być połączona z biblioteką \"glib\".

Zauważ, że w przypadku jakiejkolwiek aplikacji konsolowej to rozwiązanie oczywiście nie zadziała, ponieważ nie ma uruchomionej pętli zdarzeń.



## Zastrzeżenia

Chociaż możliwe jest zaimportowanie FreeCAD do zewnętrznego interpretera Pythona, nie jest to powszechny scenariusz użycia i wymaga pewnej ostrożności. Ogólnie rzecz biorąc, lepiej jest używać Pythona dołączonego do FreeCAD, uruchamiać FreeCAD z poziomu linii poleceń lub jako podproces. Zobacz stronę [Uruchomienie i konfiguracja](Start_up_and_Configuration/pl.md) aby uzyskać więcej informacji na temat dwóch ostatnich opcji.

Ponieważ moduł FreeCAD Python jest kompilowany z C++ (a nie jest czystym modułem Pythona), można go zaimportować tylko z kompatybilnego interpretera Pythona. Ogólnie oznacza to, że interpreter Pythona musi być skompilowany przy użyciu tego samego kompilatora C, który został użyty do budowy FreeCAD. Informacje o kompilatorze użytym do budowy interpretera Pythona (w tym tego dołączonego do FreeCAD) można znaleźć w następujący sposób:


```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```



## Powiązane

-   [FreeCAD bez GUI](Headless_FreeCAD/pl.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Embedding FreeCAD/pl
