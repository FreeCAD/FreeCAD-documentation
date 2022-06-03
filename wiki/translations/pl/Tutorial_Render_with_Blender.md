---
- TutorialInfo   */pl
   Topic   *Renderowanie
   Level   *średniozaawansowany
   Time   *60 minut
   Author   *[https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
   FCVersion   *0.18 lub nowszy
   Files   *brak
---

# Tutorial Render with Blender/pl





## Wprowadzenie

Ten poradnik prezentuje jak stworzyć wyrenderowany obraz w programie [Blender](https   *//www.blender.org/), zaczynając od części lub zespołu stworzonego w programie FreeCAD. Zakłada on, że użytkownik stworzył już część w programie FreeCAD, lub zaimportował ją do niego. Następnie część ta jest eksportowana do Blendera w celu wyrenderowania.

Przedstawia renderowanie w Blenderze 2.80 z wykorzystaniem zarówno renderera EEVEE jak i Cycles. Demonstruje różne polecenia środowiska [Python](Python/pl.md), które mogą być użyte by wykonać działania szybciej, zarówno w programie FreeCAD jak i Blender.

Podobny opis tego procesu jest zaprezentowany w serii filmów, [Renderuj modele Solidworks i FreeCAD w Blenderze](https   *//www.youtube.com/watch?v=U7e6-Wfv2b0), autorstwa Joko Engineering.

## FreeCAD

1\. Stwórz złożenie, używając zawartości ze środowiska [Caęść](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md), albo dowolnego innego środowiska, które tworzy obiekty brył, na przykład [Architektura](Arch_Workbench/pl.md). Przypisz kolory lub materiały poszczególnym zawartościom tworzącym złożenie, w przybliżeniu odpowiadające kolorowi, który chcesz uzyskać w renderingu.

<img alt="" src=images/01_T03_FreeCAD_Blender_model.png  style="width   *600px;">



*align=center|Złożenie trzech brył stworzonych w programie FreeCAD, z przypisanymi kolorami lub materiałami.*

2\. Jeśli twój model jest bardzo szczegółowy, upewnij się, że wartość {{PropertyView/pl|Odchyłka}} zawartości jest ustawiona na niską wielkość, pomiędzy `0.1` a `0.01`, lub nawet mniejszą. Im niższa jest ta wartość, tym bardziej szczegółowa będzie wyeksportowana siatka, a co za tym idzie, tym lepsza będzie jakość otrzymanego renderu.

![](images/02_T03_FreeCAD_Blender_deviation.png )



*align=center|Właściwość odchylenia zawartości utworzonych w programie FreeCAD. Wartość odchylenia musi być małe, aby można było eksportować części z dobrą rozdzielczością.*

3\. Wybierz środowisko `Part`, kolejnie z menu **Plik → Eksport**, lub naciśnij klawisze **Ctrl** + **E**, i wyeksportować jako `OBJ`.

Alternatywnie, eksport może być wykonany z konsoli [Python](Python/pl.md). Zdefiniuj listę obiektów, które mają być wyeksportowane i użyj funkcji eksportującej z nazwą pliku.


```python
import importOBJ
objs = FreeCAD.ActiveDocument.getObjectsByLabel("Part")[0]

importOBJ.export(objs, "/home/user/assembly.obj")
```


**Uwaga   ***

podczas eksportu do OBJ, tworzone są dwa pliki. Pierwszy zawiera informacje o siatce, `assembly.obj`, drugi zawiera definicję materiałów, która w większości przypadków zawiera tylko kolor, `assembly.mtl`.


**Uwaga 2   ***

Jeśli wynikowy plik OBJ wydaje się być pusty, być może trzeba będzie wyeksportować poszczególne zawartości. W takim przypadku należy zaznaczyć każdą z nich pod częścią i powtórzyć eksport.


```python
import importOBJ
objs = [FreeCAD.ActiveDocument.getObjectsByLabel("Body.base")[0],
FreeCAD.ActiveDocument.getObjectsByLabel("Body.bolt")[0],
FreeCAD.ActiveDocument.getObjectsByLabel("Body.bolt.big")[0]]

importOBJ.export(objs, "/home/user/assembly.obj")
```

## Blender

### Przygotowanie modelu 

4\. Otwórz Blendera. Zmień panel `Oś czasu` na `konsolę Python` *(**Shift** + **F4**)*. To pomoże Ci wprowadzać komendy i widzieć wyniki. Możesz podzielić ten panel tak, aby po jednej stronie pozostała konsola, a po drugiej panel `Info`, pozwoli ci to zobaczyć działanie kodu po kliknięciu w interfejs.

Upewnij się, że używasz renderera EEVEE. W panelu `Properties` przejdź do `Render`, i dla `Render Engine` wybierz `Eevee`.


```python
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
```

5\. Zaimportuj plik modelu z menu, **Pilik → Import → Wavefront ''(.obj)''**.

Alternatywnie, import można wykonać z poziomu `konsoli Python`.


```python
obj_file = "/home/user/assembly.obj"
bpy.ops.import_scene.obj(filepath=obj_file)
```

6\. Zmień skalę.

Jeśli zawartości wydają się być bardzo duże, może być konieczna zmiana jednostek, aby obiekty były wyświetlane w odpowiedniej skali.

W panelu `Properties` przejdź do `Scene`, `Units` i wybierz odpowiednie ustawienia `Unit System`, `Unit Scale` i `Length`.

Dla małych części, możesz chcieć zachować długość na `Millimeters`, a skalę na `0.001`. W przypadku większych części, na przykład modelu budynku, może być konieczne ustawienie tych wartości na `Meters` i `0.001`. W razie potrzeby wypróbuj inne wartości skali.

Może to być ustawione również z poziomu `Python console`.


```python
bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
# or bpy.context.scene.unit_settings.length_unit = 'METERS'
bpy.context.scene.unit_settings.scale_length = 0.001
```


**Uwaga   ***

Zmiana skali i jednostek sceny jest konieczna tylko wtedy, gdy chcesz pracować z obiektami w ich prawdziwych wymiarach. Jeśli chcesz tylko szybko wyrenderować scenę, możesz pominąć wszelkie regulacje.

6.1. W przypadku pomniejszenia, gdy widok przycina importowane części, może być konieczne dostosowanie wartości przycinania widoku.

Naciśnij klawisz **N**, aby wyświetlić panel pomocniczy. Przejdź do sekcji `View` i ustaw `End` na dużą wartość, na przykład `1E6 mm` lub `1000 m`.

6.2. Jeśli chcesz, możesz również dostosować rozmiar siatki. Przejdź do `Overlays`, następnie `Guides` i ustaw `Scale` dla tej siatki na `0.001`.

7\. Ustal obrót obiektów.

Po zaimportowaniu obiekty mogą być obrócone wokół wybranej osi, na przykład o 90 stopni wokół osi X. Naciśnij klawisz **N**, aby wyświetlić panel pomocniczy. Wybierz obiekt, przejdź do sekcji `Transform` i ustaw `Rotation` na `0°` w każdym polu. Zrób to dla każdego obiektu.

Można to zautomatyzować za pomocą małego skryptu, który po prostu ustawia rotację każdego importowanego ciała na zero, z wyjątkiem obiektów wewnątrz tupli `fixed_objs`. Może to być przydatne, jeśli importujesz obiekty do istniejącej sceny, gdzie inne obiekty są już we właściwych pozycjach.


```python
fixed_objs = ('Camera', 'Cube', 'Light')

for obj in bpy.data.objects   *
    if any(s for s in fixed_objs if s in obj.name)   *
        print('%s %s  [[No change]]' % (obj.name, obj.rotation_euler))
        continue
    else   *
        obj.rotation_euler = (0, 0, 0)
        print('%s %s  ... rotated' % (obj.name, obj.rotation_euler))
```

![](images/03_T03_FreeCAD_Blender_imported_assembly.png )



*align=center|Zespół stworzony w programie FreeCAD zaimportowany do Blendera; model został obrócony, a jednostki sceny dopasowane do zaimportowanych obiektów.*

### Przygotuj ujęcie kadru 

8\. Ustaw ujęcie widoku we właściwej pozycji.

Dostosuj rzutnię, aby spojrzeć na model w żądanej orientacji, a następnie naciśnij klawisze **Ctrl** + **Alt** + **0** *(klawiatura numeryczna)*, albo użyj opcji z menu **View → Align View → Align Active Camera to View**.

8.1. Jeśli w ujęciu widoku nic nie widać, być może trzeba dostosować przycięcie. Zaznaczając kamerę w `Outliner`, przejdź do panelu `Properties`, następnie `Object Data`, potem `Lens`, a następnie ustaw `Clip End` na dużą wartość, na przykład `1E3 mm` lub `1000 m`.


```python
bpy.context.object.data.clip_end = 1e+03
```

Jeśli widzisz obiekt w ujęciu widoku, możesz teraz szybko wyrenderować model, naciskając **F12**, co spowoduje otwarcie `Image Editor` z wynikiem. Naciśnij **Esc**, aby wyjść i powrócić do `3D Viewport`.

<img alt="" src=images/04_T03_FreeCAD_Blender_first_render.png  style="width   *600px;">



*align=center|Pierwszy render montażu w Blenderze, z ujęciem z poprawnym clippingiem, ale bez oświetlenia*

Możesz przełączać się między ujęciem widoku a rzutnią 3D, naciskając klawisz **0** na klawiaturze numerycznej. Naciśnięcie klawisza **F12** spowoduje wyświetlenie widoku z kamery w dowolnym momencie.

8.2. Jeśli ujęcie wygląda na bardzo małe w rzutni 3D, przejdź do panelu `Properties`, następnie `Object Data`, potem `Viewport Display` i ustaw większą wartość dla pola `Size`, na przykład `20 mm`. Włącz także pole wyboru `Limits`, aby zobaczyć odległość obcinania ujęcia widoku.


```python
bpy.context.object.data.display_size = 20
bpy.context.object.data.show_limits = True
```

### Przygotuj oświetlenie sceny 

9\. Zaznacz światło w `Outliner`, przejdź do panelu `Properties`, następnie `Object Data`, naciśnij na `Sun` i ustaw `Strength` na `5.0`.


```python
bpy.context.object.data.type = 'SUN'
bpy.context.object.data.energy = 5
```

Spowoduje to przekształcenie światła w lampę słoneczną. Ten typ lampy emituje nieskończoną liczbę równoległych promieni świetlnych, które docierają do sceny pod stałym kątem.

Możesz umieścić lampę słoneczną w dowolnym miejscu rzutni nad swoim modelem, tak aby określić kierunek promieni świetlnych. Dla lampy słonecznej nie ma znaczenia jak blisko lub daleko umieścisz lampę, tylko kierunek promieni, które są definiowane przez rotację obiektu `Light`.


```python
bpy.context.active_object.location = (150, 100, 100)
bpy.context.active_object.rotation_euler = (0.6, 0.05, 1.88)
```

Naciśnij ponownie klawisz **F12**, aby zobaczyć wstępny render modelu.

<img alt="" src=images/05_T03_FreeCAD_Blender_render_sun_lamp.png  style="width   *600px;">



*align=center|Render złożenia w Blenderze z dodaną lampą słoneczną, która emituje równoległe promienie świetlne o stałym kącie*

### Więcej ustawień   * podłoga, oświetlenie globalne, odbicia i miękkie cienie 

10\. Dodaj płaszczyznę podłogi. Naciśnij klawisze **Shift**+**A**, a następnie wybierz `Mesh`, `Plane` i nadaj mu wymiary około 10 razy większe niż twój model. Ten obiekt będzie służył jako płaszczyzna podłogi lub blat stołu, na którym stoi model. Przesuń również płaszczyznę nieco w dół, tak aby nie przecinała modelu. Wystarczy `-1 mm` poniżej obiektu.


```python
bpy.ops.mesh.primitive_plane_add(size=1500, view_align=False, enter_editmode=False, location=(0, 0, -1))
```

11\. Ustaw iluminację świata. W panelu `Properties` przejdź do `World` i ustaw `Color` na wartość jasnoniebiesko-szarą, `RGB (0.358, 0.512, 0.527)`, a także ustaw `Strength` na `0.3`.

12\. Ustaw odbicia i cienie. Renderer EEVEE w Blenderze produkuje szybkie obrazy poprzez dezaktywację większości efektów na początku. W celu uzyskania lepszych obrazów, niektóre opcje muszą być uaktywnione.

Przejdź do panelu `Properties`, następnie `Render` i zaznacz opcję `Screen Space Reflections`. W sekcji `Shadows` zaznacz również opcję `Soft Shadows`.


```python
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_soft_shadows = True
```

### Ustawienie rodzaju materiału dla obiektów 

13\. Zmień panel `Python Console` w panel `Shader Editor` *(**Shift**+**F3**)*.

13.1. Zaznacz płaszczyznę podłoża, przejdź do panelu `Properties`, następnie `Material` i kliknij przycisk `New`. W oknie `Shader Editor` powinien pojawić się węzeł `Principled BSDF`. Nadaj mu beżowy kolor `Base Color` `RGB ''(0.318, 0.267, 0.187)''`, suwak `Metallic` ustaw na `0.000`, a suwak `Roughness` na `1.000`.

![](images/06_T03_FreeCAD_Blender_Principled_shader.png )



*align=center|Podstawowy shader BSDF używany w Blenderze do symulacji różnych materiałów, od błyszczących metali po szorstkie i nieprzezroczyste bryły..*

13.2. Zaznacz każdą z części modelu i dostosuj odpowiedni węzeł materiałowy `Principled BSDF`. W przypadku części metalowych ustaw właściwość `Metallic` na wartość `1.000`. Dostosuj wartość właściwości `Roughness`, aby mieściła się w przedziale od `0.2` do `0.7`. Im bardziej `0.000` zbliża się do wartości `Roughness`, tym bardziej będzie się odbijał *(przypominał lustro)*.

W przypadku materiałów innych niż metale, takich jak tworzywa sztuczne, drewno i tkaniny, ustaw suwak `Metallic` na wartość `0.000`, a wartość parametru `Roughness` na wartość pomiędzy `0.4` a `1.0`.

Ogólnie rzecz biorąc, metale są naturalnie gładkie i dlatego ich wartość chropowatości jest mała, co sprawia, że są bardzo odblaskowe (błyszczące). Inne materiały są mikroskopijnie szorstkie i dlatego nie odbijają tak dużo światła, co czyni je nieprzezroczystymi.

14\. Testuj różne kombinacje materiałów, aż do uzyskania akceptowalnego wyglądu. Wciśnij **Z** a następnie **8** W tym trybie renderer EEVEE pokazuje w czasie rzeczywistym na rzutni 3D, jak będzie wyglądał końcowy obraz. Użyj **Z** by otworzyć menu pie i przełączyć się z powrotem do trybu `Solid` (**Z** **6**), lub przejść do trybu `LookDev` (**Z** **2**), trybu który dodaje różne rodzaje oświetlenia do sceny by przetestować wygląd materiałów.

Naciśnij przycisk **F12**, aby wyświetlić widok z kamery i sprawdzić jakość obrazu.

### Renderowanie i zapisywanie 

15\. Jeśli Twój model wygląda w miarę dobrze z rendererem EEVEE możesz już zapisać obraz poprzez **Image → Save As** lub naciskając **Shift**+**S** w {{Incode|Image Editor}}.

<img alt="" src=images/07_T03_FreeCAD_Blender_EEVEE_render.png  style="width   *600px;">



*align=center|Renderowane złożenie wykonane w Blenderze EEVEE. Wszystkie materiały używają shadera Principled BSDF, użyta jest tylko jedna lampa słoneczna, z niewielką ilością światła otoczenia.*

16\. Jeśli chcesz poprawić jakość obrazu, wypróbuj renderer Cycles.

Przejdź do panelu `Properties`, następnie `Render`, i dla `Render Engine` wybierz `Cycles`. W przypadku renderera Cycles, Blender będzie stopniowo udoskonalał obraz, aż minie pewna liczba iteracji. Za każdym razem, gdy rzutnia się zmieni, przeliczanie rozpocznie się od nowa.


```python
bpy.context.scene.render.engine = 'CYCLES'
```

16.1. Dostosuj częstotliwość próbkowania. Przejdź do panelu `Properties`, następnie `Render`, po czym w sekcji `Sampling` wybierz odpowiednią liczbę dla `Render` i `Viewport`.

Dla `Viewport` wystarczy niewielka liczba próbek, w zakresie od `32` do `128`, aby uzyskać dobry podgląd obrazu. W celu uzyskania ostatecznego obrazu należy ustawić `Render` na wyższą liczbę, od `128` do `2000`, w zależności od złożoności i ilości szczegółów sceny.

Wciśnij klawisz **F12** aby wyrenderować końcowy widok przez kamerę. W zależności od Twojej karty graficznej *(GPU)* renderowanie obrazu w Cycles powinno zająć kilka sekund lub minut więcej niż w EEVEE, ale jakość obrazu powinna być lepsza.

17\. Kiedy jesteś zadowolony z jakości renderingu, w `Image Editor` przejdź do **Image → Save As** lub naciśnij **Shift**+**S**.

<img alt="" src=images/08_T03_FreeCAD_Blender_Cycles_render.png  style="width   *600px;">



*align=center|Renderowane złożenie wyprodukowane w Blender Cycles. Wszystkie opcje, materiały i światła, które były używane w EEVEE zostały zachowane do użycia w Cycles.*

### Renderowanie z poziomu wiersza poleceń 

18\. Jeśli scena jest już całkowicie ukończona, możesz chcieć renderować ją spoza Blendera, z linii poleceń systemu operacyjnego. Może to być przydatne do wsadowego renderowania różnych scen w zdalnym systemie. Zarówno EEVEE jak i Cycles są obsługiwane.


{{Code|lang=sh|code=
blender -b assembly.blend -E BLENDER_EEVEE -o //assembly_EEVEE_#### -t 3 -F PNG -x 1 -f 1
}}


{{Code|lang=sh|code=
blender -b assembly.blend -E CYCLES -o //assembly_CYCLES_#### -t 3 -F PNG -x 1 -f 1
}}

Pozwala to określić, że renderowanie powinno odbywać się w tle za pomocą `-b`., Silnik renderujący jest wybierany za pomocą `-E`, nazwa pliku wyjściowego jest wybierana za pomocą `-o`, podwójny ukośnik wprzód `//` wskazuje ścieżkę względem pliku wejściowego. Znak skrótu `#` jest używany do wskazania numeru ramki, w razie potrzeby uzupełnionego zerami, na przykład `0001`. Liczba wątków procesora używanych podczas renderowania jest wybierana za pomocą `-t 3`, format pliku wyjściowego określa się za pomocą `-F`, a opcja `-x 1` automatycznie dodaje do nazwy rozszerzenie. Ostatnią opcją jest `-f 1`, która oznacza, że renderowana będzie tylko pierwsza klatka, co jest normalnym przypadkiem dla statycznej sceny. W przypadku animacji należy użyć przełącznika `-a`, aby dla każdej klatki utworzyć obraz, który następnie można złożyć w plik wideo.

## Importowanie wtyczek 

Stworzenie pośredniej siatki Wavefront (.obj) i następnie zaimportowanie jej do Blendera zadziała w większości sytuacji. Jednakże, istnieje również możliwość importu pliku FreeCAD (.FCStd) bezpośrednio do Blendera za pomocą pluginu.

-   [io\_import\_fcstd.py](https   *//gist.github.com/yorikvanhavre/e873d51c8f0e307e333fe595c429ba87), oryginalna wersja dla Blendera 2.79
-   [FreeCAD .FCStd importer for Blender 2.80](https   *//gist.github.com/yorikvanhavre/680156f59e2b42df8f5f5391cae2660b)

Jest to wtyczka do Blendera. Aby działała, Blender musi być w stanie zaimportować FreeCAD jako moduł z `Python Console`. 
```python
import FreeCAD
```

Jest to możliwe tylko wtedy, gdy zarówno Blender jak i FreeCAD są skompilowane z tą samą `pythonX.Y` *(główną i podrzędną)* wersją. Na przykład, jeśli Blender jest skompilowany z wersją środowiska Python 3.7, FreeCAD również musi być skompilowany z wersją Python 3.7. Jeśli FreeCAD jest skompilowany z inną wersją, na przykład Python 2.7.15 lub Python 3.6.7, wtyczka nie będzie działać. Numer wersji mikro *(trzecia cyfra)* nie ma znaczenia, to znaczy, że wtyczka powinna działać, jeśli jeden program jest skompilowany z Pythonem 3.7.5, a drugi z Pythonem 3.7.8.

Dodatkowo, prekompilowany moduł FreeCAD w Pythonie, `FreeCAD.so` w Linuksie i `FreeCAD.pyd` w Windows, powinien znajdować się w ścieżce Pythona używanej przez Blendera do importowania modułów. Ścieżka ta może być ustawiona na różne sposoby, w zależności od systemu operacyjnego i dystrybucji środowiska Python.

W Blenderze możesz zobaczyć wszystkie przeszukiwane ścieżki poprzez sprawdzenie zmiennej `sys.path`. Moduł FreeCAD powinien znajdować się w każdym z tych katalogów. 
```python
import sys
print(sys.path)```

-   Kopia lub dowiązanie symboliczne wewnątrz jednego z tych katalogów może zostać utworzone wskazując na moduł FreeCAD.


```python
ln -s /usr/lib/freecad/lib/FreeCAD.so $HOME/.config/blender/2.80/scripts/addons

ln -s /usr/lib/freecad/lib/FreeCAD.so $HOME/.local/lib/python3.7/site-packages
```

-   Inną możliwością jest dodanie modułu bezpośrednio do ścieżki wewnątrz Blendera.


```python
import sys
sys.path.append("/usr/lib/freecad/lib/FreeCAD.so")
```

## Uwagi końcowe 

EEVEE nie jest fizycznie dokładnym rendererem, jednak jego główną siłą jest to, że jest to silnik czasu rzeczywistego, więc jest w stanie produkować szybkie renderingi bezpośrednio w rzutni 3D. W wielu przypadkach obrazy te mają wystarczającą jakość dla końcowej produkcji, co oznacza, że możliwe jest uzyskanie dobrego rezultatu w bardzo krótkim czasie. W przypadkach, gdy pożądane są złożone interakcje światła *(odbicia, załamania, światło wolumetryczne i kaustyka)*, EEVEE jest bardziej ograniczony i wymaga pewnych opcji i sztuczek, aby obejść niektóre z tych ograniczeń.

Z drugiej strony, Cycles jest prawdziwym rendererem raytracingowym, co oznacza, że jest bardziej dokładny w obliczaniu ścieżek światła w przestrzeni sceny. Cycles jest zalecanym rendererem, gdy pożądana jest najwyższa jakość *(fotorealistyczne rezultaty)*, kosztem dłuższego czasu renderowania.

Oba renderery mogą być użyte w celu wykorzystania zalet każdego z nich. W wielu przypadkach scena może być szybko przygotowana i przetestowana z EEVEE, aby uzyskać wstępne renderingi. Następnie ta sama scena może być użyta z niewielkimi zmianami z Cycles, aby uzyskać wyższej jakości, ostateczny rendering. W szczególności, gdy scena, która została ustawiona w EEVEE będzie używana w Cycles, światła mogą wymagać korekty wartości i pozycji, jako że oba renderery traktują światło w różny sposób.

Uzyskanie dobrych rezultatów zależy w dużej mierze od opcji renderowania, materiałów i oświetlenia. Shader materiałów `Principled BSDF` jest ogólnym rozwiązaniem, które sprawdza się w wielu przypadkach, jednak aby uzyskać prawdziwie fotorealistyczne rezultaty, nadal bardzo ważne jest użycie map tekstur i map normalnych, wraz z dokładnym oświetleniem sceny.  {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Tutorial Render with Blender/pl
