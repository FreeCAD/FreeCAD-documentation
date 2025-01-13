---
 TutorialInfo:l
   Topic: Renderowanie
   Level: średniozaawansowany
   Time: 120 minut
   Author: https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx
   FCVersion: 0.18 lub nowszy
   Files: brak
---

# Tutorial FreeCAD POV ray/pl




**Środowisko [Raytracing](Raytracing_Workbench/pl.md) zostało zastąpione przez nowe [https://github.com/FreeCAD/FreeCAD-render środowisko Render], które ma je zastąpić. Środowisko pracy Render może być zainstalowane poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Informacja tutaj jest podana, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' ze środowiskiem Raytracing, i ponieważ nowy moduł powinien w zasadzie działać w ten sam sposób.**





## Wprowadzenie

Ten poradnik pokazuje jak stworzyć wyrenderowany obraz w programie FreeCAD, używając renderera POV-Ray. Zakłada on, że użytkownik stworzył już część lub złożenie w FreeCAD, lub zaimportował je do niego. Do wytworzenia pliku do renderowania użyto środowiska pracy [Raytracing](Raytracing_Workbench/pl.md).

Ten poradnik jest oparty na poście forum autorstwa schupin [FreeCAD / pov ray tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=32745), który zawiera również jeden `.pov` plik wymagany do produkcji renderingu.

<img alt="" src=images/Povray_before_after.png  style="width:600px;">



*align=center|Przykład autorstwa użytkownika ''schupin'' modelu 3D i wysokiej jakości renderu wykonanego za pomocą programu FreeCAD i POV-Ray.*

Pliki użyte w tym poradniku znajdują się w poście #8 [w tym samym wątku](https://forum.freecadweb.org/viewtopic.php?f=36&t=32745#p305169).



## Konfiguracja podstawowa 

Postępuj zgodnie z podstawowym przepływem pracy opisanym w dokumentacji środowiska pracy [Raytracing](Raytracing_Workbench/pl.md).

Aby renderowanie bezpośrednie działało, wykonawczy plik `povray` musi być ustawiony w **Edycja → Preferencje ...→ Raytracing → Renderowanie → Plik wykonywalny POV-Ray**. Ustaw go na swoją lokalizację w systemie, na przykład `/usr/bin/povray`. Inne opcje używane przez renderowanie mogą być również zdefiniowane tutaj, włączając szerokość `+W` i wysokość `+H` obrazu, oraz użycie antyaliasingu `+A`.



## Przygotowanie pliku .pov 

1\. Stwórz projekt korzystając z części wytworzonych za pomocą środowisk[Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) czy dowolnego innego które pozwoli na stworzenie bryły jak na przykład środowisko [Architektura](Arch_Workbench/pl.md). Następnie przypisz elementom kolory lub materiały tak by w przybliżeniu przypominały ostateczny docelowy wygląd.

<img alt="" src=images/01_T04_FreeCAD_POVray_model.png  style="width:600px;">



*align=center|Złożenie trzech elementów w FreeCAD, z wstępnie przypisanymi kolorami lub / i materiałami.*

2\. Jeśli twój model jest bardzo szczegółowy, upewnij się, że wartość {{PropertyView/pl|Odchyłka}} zawartości jest ustawiona na niską wielkość, pomiędzy `0.1` a `0.01`, lub nawet mniejszą. Im niższa jest ta wartość, tym bardziej szczegółowa będzie wyeksportowana siatka, a co za tym idzie, tym lepsza będzie jakość otrzymanego renderu.

![](images/02_T04_FreeCAD_POVray_deviation.png )



*align=center|Właściwość odchylenia zawartości utworzonych w programie FreeCAD. Wartość odchylenia musi być małe, aby można było eksportować części z dobrą rozdzielczością.*

3\. Utwórz projekt POV-Ray, klikając **<img src="images/Raytrace_New.svg" width=16px> [Nowy](Raytracing_New/pl.md)**. Jeśli widok jest ustawiony jako [ortogonalny](Std_OrthographicCamera/pl.md), zmień go na [perspektywiczny](Std_PerspectiveCamera/pl.md), ponieważ renderer zazwyczaj pracuje z kamerą o widoku perspektywicznym. Użycie widoku perspektywicznego pozwoli ci lepiej zobaczyć rodzaj sceny, który zostanie zrenderowany.

4\. Zaznacz wszystkie obiekty, które chcesz dodać do sceny, a następnie zaznacz utworzony obiekt {{Incode|PovProject}} i kliknij przycisk **<img src="images/Raytrace_NewPartSegment.svg" width=16px> [Wstaw część](Raytracing_InsertPart/pl.md)**.


**Uwaga:**

należy uważać na obiekty, które nie są aktualnie widoczne w rzutni 3D. Jeśli są one niewidoczne, ale znajdują się w scenie, nadal będą renderowane. Z drugiej strony, jeśli naprawdę chcesz pominąć bryłę w renderowaniu, nie wybieraj jej do włączenia do projektu POV-Ray.


**Uwaga 2:**

Wszystkie obiekty w projekcie POV-Ray będą miały nazwę opartą na ich wewnętrznej nazwie FreeCAD. Ważne jest, aby pamiętać, która jest nazwą POV-Ray, ponieważ dalsze opcje, na przykład tekstury materiałów, zostaną przypisane do tych nazw POV-Ray.

5\. W widoku 3D, przybliż, przesuń i obróć widok, aby ustawić scenę zgodnie z własnymi preferencjami. Upewnij się, że obiekty są wyśrodkowane w widoku, a następnie wybierz utworzony obiekt `PovProject` i kliknij przycisk **<img src="images/Raytrace_ResetCamera.svg" width=16px> [Resetuj kamerę](Raytracing_ResetCamera/pl.md)**.

6\. Plik POV-Ray jest teraz gotowy. Zawiera wybrane obiekty oraz informacje o kamery. Wybierz utworzony obiekt `PovProject`, a następnie kliknij przycisk **<img src="images/Raytrace_ExportProject.svg" width=16px> [Eksportuj projekt](Raytracing_ExportProject/pl.md)** aby zapisać plik `.pov`.

7\. Utworzony plik `.pov` może teraz być renderowany bezpośrednio z programu FreeCAD. Wybierz utworzony obiekt `PovProject`, a następnie kliknij przycisk **<img src="images/Raytrace_Render.svg" width=16px> [Renderuj](Raytracing_Render/pl.md)**. Gdy pojawi się obraz w wyskakującym okienku, kliknij na niego, aby został przesłany do programu FreeCAD w swojej własnej karcie okna.

<img alt="" src=images/03_T04_FreeCAD_POVray_first_render.png  style="width:600px;">



*align=center|Pierwszy render zespołu wykonany za pomocą POV-Ray, ze standardowym szablonem napisanym przez środowisko pracy Raytracing.*

7.1. Mając już utworzony plik `.pov`, możliwe jest również uruchomienie `povray` z wiersza poleceń. 
```python
povray assembly.pov +W800 +H600 +AM2 +A
```

Opcje `+WX +HY` ustawiają poziomy i pionowy rozmiar pikseli końcowego obrazu.

Opcje `+AM2` (typ 2, rekurencyjne superpróbkowanie) i `+A` (typ 2, rekursywne super-próbkowanie) i `+A` uruchamiają antyaliasing w celu uzyskania gładszego obrazu.

8\. Klikając dwukrotnie obiekt `PovProject` można zobaczyć, że używa on szablonu `ProjectStd.pov`. Szablon ten tworzy podstawowy plik `.pov`, który wygeneruje prosty i ciemny obraz.

Aby poprawić wygląd obrazu, użyj lepszego szablonu. Kliknij dwukrotnie obiekt `PovProject` i wybierz szablon `RadiosityNormal.pov`. Następnie wyeksportuj nowy plik `.pov` i ponownie uruchom renderer. Obraz powinien wyglądać jaśniej i ogólnie lepiej.

<img alt="" src=images/04_T04_FreeCAD_POVray_first_render_radiosity.png  style="width:600px;">



*align=center|Render zespołu wykonanego za pomocą POV-Ray, z szablonem RadiosityNormal napisanym przy użyciu środowiska Raytracing.*

Ponownie kliknij dwukrotnie obiekt `PovProject` i wybierz szablon `RadiosityOutdoorHQ.pov`. Następnie wyeksportuj nowy plik `.pov` i ponownie uruchom renderer. Tworzenie obrazu powinno potrwać dłużej, ale wynik powinien mieć lepszą jakość. <img alt="" src=images/05_T04_FreeCAD_POVray_first_render_radiosity_outdoor.png  style="width:600px;">



*align=center|Render zespołu wykonany za pomocą POV-Ray, z szablonem RadiosityOutdoorHQ napisanym przy użyciu środowiska Raytracing.*

Jeśli wyrenderowany obraz jest wystarczająco dobry, można go zapisać i nie trzeba nic więcej robić. Aby jednak precyzyjnie kontrolować wygląd materiałów i uzyskać jeszcze lepsze rezultaty, plik `.pov` należy edytować ręcznie.

W kolejnych sekcjach edytujemy podstawowy plik `.pov` utworzony przy użyciu szablonu `ProjectStd`.



## Edycja pliku .pov 

9\. Wygenerowany przez FreeCAD plik `.pov` to zwykły plik tekstowy, który można otworzyć za pomocą dowolnego edytora. Luźno przypomina plik źródłowy w języku C++: dyrektywy zaczynają się od znaku krzyżyka `#` i kończą średnikiem `;`. Nawiasy klamrowe { } są używane do ograniczenia bloków sekcji, a wcięcia to dowolne białe znaki. Komentarze są oznaczane podwójnym ukośnikiem `//`. Komentarze blokowe można zdefiniować za pomocą pary `/*  */`, podobnie jak w języku C.

Na początku plik może wyglądać na skomplikowany, ale 90% jego zawartości to tylko dane siatki, które nie wymagają wielu zmian, ponieważ siatki te reprezentują geometrię ciał, które chcemy renderować.

Plik jest zorganizowany w następujący sposób:

-   Dołączenia,
-   Globalne ustawienia,
-   Sfera nieba,
-   Płaszczyzny,
-   Wykończenia i tekstury,
-   Kamera,
-   Informacje o siatce i bryle,
-   Źródło światła.

Informacje o kamerze nie zostaną zmienione, podobnie jak większość informacji w siatkach. Główne modyfikacje zostaną wprowadzone w pozostałych sekcjach.

Ponieważ siatki nie będą mocno modyfikowane, plik można przeorganizować tak, aby te informacje znajdowały się na końcu pliku.


<div class="toccolours mw-collapsible mw-collapsed">

To jest kompletna zawartość pliku `.pov`, bez siatek.


<div class="mw-collapsible-content">


```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http://www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"

// 

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}  

// 


sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}


// 

plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}

// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;

// declares position and view direction

// Generated by FreeCAD (http://www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
// Written by FreeCAD http://www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...




//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```


</div>


</div>



### Podstawowa reorganizacja 

10\. Otwórz plik \.pov\ za pomocą edytora tekstu, przejdź do końca pliku, zaznacz i wyciągnij sekcję \light_source\, a następnie wklej ją przed pierwszą linią z komentarzem \//face number1\.

Plik wynikowy powinien mieć sekcje `camera` i `light_source` obok siebie, na przykład:


```python
// Generated by FreeCAD (http://www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}

//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
// Written by FreeCAD http://www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.
.
.
```



### Przygotowanie oświetlenia 

11\. Domyślnie plik projektu definiuje jedno światło z pozycją i kolorem. 
```python
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```

Pozycja światła jest określana przez wektor `<x, y, z>`. Kolor może być określony jako wektor `<r, g, b>` lub można użyć nazwanego koloru, takiego jak `White`. Jeśli podano wartości RGB, powinny się one zawierać w zakresie od `0.0` do `1.0`, aby światło miało normalną jasność.

Podobnie jak inne obiekty, światło można modyfikować za pomocą wielu opcji. Opcja `area_light` tworzy źródło prostokątne, co jest bardziej realistyczne, ponieważ powoduje rozproszone oświetlenie tworzące miękkie cienie. Słowo kluczowe `adaptive` pomaga zmniejszyć czas obliczeń ścieżek świetlnych; im większa wartość, tym dokładniejszy będzie wynik; aby uniknąć długiego czasu renderowania, należy użyć najmniejszej wartości całkowitej, która daje akceptowalny wynik *(zwykle wystarczy `1` lub `2`)*. Dla uzyskania najlepszego rezultatu usuń całkowicie słowo kluczowe *(długi czas renderowania)*. Słowo kluczowe `jitter` pomaga poprawić cienie poprzez losowe przesunięcie pozycji świateł. Słowa kluczowe `circular` i `orient` zamieniają światło obszarowe w źródło sferyczne, co pozwoli uzyskać lepsze cienie w przypadku obiektów zaokrąglonych na scenie. Włączenie `fade_distance` i `fade_power` jest pomocne w tłumieniu wartości światła wraz z odległością, tak jak ma to miejsce w przypadku prawdziwego źródła światła.

Ustaw światło padające z prawej strony i z góry. 
```python
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
```

Jeśli źródło światła ma znajdować się w scenie, przydatne może być wyświetlenie na ekranie odniesienia do miejsca, w którym to źródło powinno się znajdować. W tym celu utwórz kulę o małym promieniu i załóż, że reprezentuje ona źródło światła. Umieść kulę w wybranym miejscu, a następnie przesuń światło bardzo blisko tych współrzędnych i przetestuj oświetlenie sceny. Gdy będziesz zadowolony z położenia światła, po prostu usuń kulę. 
```python
sphere {
    <1200, 1000, -1200>, 10
    pigment { color White }
}
```

12\. Sekcja `sky_sphere` służy do stworzenia realistycznego tła nieba. Zazwyczaj definiuje się je jako `gradient` oraz `color_map` składający się przynajmniej z dwóch kolorów, aby uzyskać płynny przejście od koloru horyzontu do koloru zenitu sceny.


```python
sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}
```

<img alt="" src=images/06_T04_FreeCAD_POVray_render_lights.png  style="width:600px;">



*align=center|Zaczynając od standardowego szablonu, wyrenderuj scenę za pomocą POV-Ray, z ustawionym źródłem światła i sferą nieba.*



### Przygotowanie tekstur obiektów 

13\. Tekstury każdego elementu muszą zostać dopasowane. Jest to najbardziej czasochłonne zadanie w tym procesie.

W pliku `.pov` każdy element jest opisane w ten sposób:

-   Face1, Face2, Face3, Face4, \...
-   Element *(suma zbiorów ścian)*,
-   Obiekt.

Siatka elementu jest określana przez ściany, a każda ściana jest określana przez serię trójkątnych elementów, które same są określane przez `vertex_vectors`, `normal_vectors`, i `face_indices`. Te informacje nie wymagają żadnych zmian. Następnie, każdy element jest zdefiniowany jako suma określonych ścian. Ponownie, te informacje nie wymagają modyfikacji.

Wreszcie, każdy `object` do wyrenderowania jest definiowany jako jeden z określonych elementów, z określoną `texture`, która sama jest definiowana przez właściwości takie jak `pigment` i `finish`. 
```python
// instance to render
object {Pov_Body
 texture {
      pigment {color rgb <0.827451,0.827451,0.431373>}
      finish {StdFinish } //definition on top of the project
  }
}
```

Przeszukując plik `.pov` pod kątem słowa kluczowego `object`, można przejść bezpośrednio do wybranej części pliku i odpowiednio zmodyfikować jej `texture`.

Jak wskazano w komentarzu, definicja `StdFinish` znajduje się na górze pliku, w tym przypadku przed informacjami o kamerze. Wartość ta może być zadeklarowana na wiele sposobów, jako kombinacja różnych właściwości, jak pokazano w zakomentowanych i niezakomentowanych liniach. 
```python
// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;
```

Generalnie, tekstura `texture` to kontener opisujący materiał. Zawiera informacje takie jak `pigment` *(kolor lub grafika)*, `normal` *(jak kolor zmienia się w zależności od krzywizny powierzchni)*, `finish` *(interakcja powierzchni z światłem)*, `pattern` *(agat, cegła, wgłębienia, lampart, promienisty, fale, kafle, fale, drewno, itp.)* oraz inne właściwości. Istnieje wiele opcji, które można połączyć, aby uzyskać teksturę. To mieszanie nie jest trywialne, ale istnieje wiele przykładów online, które pozwalają uzyskać pożądany wygląd materiału.



#### Biblioteka materiałów 

14\. POV-Ray jest dostarczany z obszerną biblioteką materiałów, które mogą być używane według nazwy. Domyślnie szablon projektu udostępnia niektóre materiały za pomocą instrukcji `#include` na początku pliku. Materiały te można dowolnie modyfikować. 
```python
#include "colors.inc"
#include "metals.inc"
```

Biblioteka `colors.inc` definiuje podstawowe kolory według nazwy, takie jak `Red`, `Green`, `Blue`, `Yellow`, `Cyan`, `Magenta`, `Clear`, `White` i `Black`. Zawiera również kilka innych odcieni oraz funkcje do transformacji kolorów. Biblioteka `metals.inc` zawiera tekstury miedzi, srebra, chromu i mosiądzu, a `golds.inc` zawiera tekstury złota.

Standardowe biblioteki znajdują się w katalogu instalacyjnym POV-ray, na przykład: 
```python
/usr/share/povray-3.7/include/
```



#### Nowe tekstury 

Na przykład, aby stworzyć teksturę lustra, właściwości `finish` są ustawione na wysoką wartość odbicia, czyli `reflection`. 
```python
#declare T_mirror = texture {
    finish { reflection {0.9} }
}
```

Alternatywnie, w przypadku metali, można zastosować predefiniowane wykończenie. 
```python
#include "metals.inc"
#declare T_mirror = texture {
    finish { F_MetalE }
}
```

Następnie można je przypisać do określonego obiektu. 
```python
object {Pov_Body002
    texture { T_mirror }
}
```

Biblioteka `woods.inc` definiuje teksturę `T_Wood7` *(sosna żółta, nieregularne słoje)*. Może być wykorzystana jako podstawa dla bardziej złożonej tekstury, z dodatkowym skalowaniem i translacją. 
```python
#include "woods.inc"
#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}
```

Następnie można ją przypisać do określonego obiektu. 
```python
object {Pov_Body
    texture { T_wood }
}
```

Biblioteka `glass.inc` definiuje `F_Glass2` jako wykończenie dla transparentnego akrylu. Definiuje również `I_Glass` jako materiał wewnętrzny, który w połączeniu z opcją `caustics` jest używany do obliczenia jak najdokładniejszych efektów światła przechodzącego przez materiał transparentny. W tym przypadku sekcja `material` jest używana, zawierając zewnętrzne *(`texture`)* i wewnętrzne *(`interior`)* informacje o materiale.


```python
#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
```

Następnie można je przypisać do określonego obiektu. 
```python
object {Pov_Body001
    material { M_vase }
}
```

<img alt="" src=images/07_T04_FreeCAD_POVray_render_materials.png  style="width:600px;">



*align=center|Zaczynając od standardowego szablonu, render sceny w POV-Ray, z ustawionym źródłem światła i sferą nieba oraz przypisanymi materiałami.*



### Przygotowanie płaszczyzn 

16\. Jeśli oryginalny model 3D tego nie zapewnia, można dodać płaszczyzny symulujące podłogę lub blat stołu, na którym stoją obiekty. Więcej płaszczyzn można zdefiniować jako ściany lub inne rodzaje granic.

Domyślnie tworzona jest pojedyncza płaszczyzna. Jest ona umieszczona 1 milimetr pod modelem, dzięki czemu wygląda jak podłoga. Płaszczyzna ma przypisaną podstawową teksturę, która jest czarna i lekko odblaskowa. 
```python
plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}
```

Zauważ, że w POV-Ray oś X jest zdefiniowana jako pozioma *(lewo-prawo)*, oś Y jest zdefiniowana jako pionowa *(góra-dół)*, a oś Z jest zdefiniowana jako głębokość *(przód-tył)*.

Aby uzyskać zwykłe szare podłorze, która jest ledwo odblaskowa, użyj: 
```python
plane {
  y, -1
  texture { pigment {rgb <0.3, 0.3, 0.3>} finish {ambient 0.0 reflection 0.01 specular 0.0} }
}
```

<img alt="" src=images/08_T04_FreeCAD_POVray_render_floor_gray.png  style="width:600px;">



*align=center|Starting from the standard template, render of the scene with POV-Ray, with the light source and sky sphere set up, materials assigned, and a floor plane with a basic gray texture.*

17\. Płaszczyźnie można nadać bardziej złożony wygląd za pomocą normalnych i bibliotek materiałów.

Zdefiniuj mapę normalnych, która zostanie użyta do nadania płaszczyźnie wyglądu parkietu.


```python
#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;
```

Następnie zdefiniuj płaszczyznę. Jako `pigment` użyj tekstury drewna zdefiniowanej w `woods.inc`, a następnie zmodyfikuj ją za pomocą `turbulence` i `scale`, aby słoje drewna wyglądały losowo. Następnie dodaj utworzoną normalną, razem z inną normalną; spowoduje to efekt tekstury parkietu z lekkimi niedoskonałościami. Na koniec, jako `finish`, ustaw nieco odbijający i błyszczący efekt.


```python
#include "woods.inc"
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}
```

<img alt="" src=images/09_T04_FreeCAD_POVray_render_floor_wood.png  style="width:600px;">



*align=center|Zaczynając od standardowego szablonu, render sceny w POV-Ray, z ustawionym źródłem światła i sferą nieba, przypisanymi materiałami i płaszczyzną podłogi z teksturą parkietu.*

18\. Dodaj drugą płaszczyznę, tym razem prostopadłą do kierunku Z, aby służyła jako ściana tylna. Przesuń ją nieco za model, aby uniknąć zakrycia lustra. Dołącz bibliotekę `stones.inc`, dodaj ogólną teksturę granitu i nieco ją przeskaluj. Spowoduje to uzyskanie wyglądu prostej suchej ściany.


```python
#include "stones.inc"
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

Trzecią płaszczyznę można dodać za pozycją kamery, tak aby lustro odbijało ograniczony obszar między dwiema ścianami.


```python
#include "stones.inc"
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

<img alt="" src=images/10_T04_FreeCAD_POVray_render_floor_wood_walls.png  style="width:600px;">



*align=center|Zaczynając od standardowego szablonu, render sceny w POV-Ray, z ustawionym źródłem światła i sferą nieba, przypisanymi materiałami, płaszczyzną podłogi z teksturą parkietu i tylnymi ścianami z teksturami płyt kartonowo-gipsowych.*



### Przygotuj ustawienia globalne, radiosity 

19\. Ustawienia globalne definiują oświetlenie otoczenia.


```python
global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}
```

Właściwość `radiosity` wewnątrz `global_settings` kontroluje sposób, w jaki POV-Ray oblicza interakcje rozproszonego światła między różnymi obiektami. Dostosowanie tej właściwości jest niezbędne do uzyskania dobrych wyników renderowania.

Ponieważ testowanie różnych ustawień `radiosity` może być czasochłonne, można użyć zmiennej `Rad_Quality` i instrukcji `#switch`, aby szybko ustawić niską, średnią lub wysoką jakość renderowania. Im wyższe ustawienia jakości, tym więcej czasu potrzeba na wyrenderowanie obrazu.


```python
#declare Rad_Quality = 1;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        pretrace_start 0.08
        pretrace_end   0.02
        count 50
        error_bound 0.5
        recursion_limit 1
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        pretrace_start 0.08
        pretrace_end   0.01
        count 120
        error_bound 0.25
        recursion_limit 1
    }
    #break
 #case (3)
    radiosity { // Settings 3 (high quality)
        pretrace_start 0.08
        pretrace_end   0.005
        count 400
        error_bound 0.1
        recursion_limit 2
    }
    #break
#end
}
```

<img alt="" src=images/11_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_1.png  style="width:600px;">



*align=center|Zaczynając od standardowego szablonu, render sceny w POV-Ray, z ustawionym źródłem światła i sferą nieba, przypisanymi materiałami, płaszczyzną podłogi z teksturą parkietu i tylnymi ścianami z teksturami płyt kartonowo-gipsowych. Ustawienia Radiosity dla szybkiego renderowania.*

20\. Biblioteka `rad_def.inc` definiuje makro do szybkiej konfiguracji `radiosity` do predefiniowanej konfiguracji. 
```python
#include "rad_def.inc"
global_settings {
    radiosity {
        Rad_Settings(Setting, Normal, Media)
    }
}
```

Wartość `Setting` może być jedną z predefiniowanych stałych: 
```python
Radiosity_Default
Radiosity_Debug
Radiosity_Fast
Radiosity_Normal
Radiosity_2Bounce
Radiosity_Final
Radiosity_OutdoorLQ
Radiosity_OutdoorHQ
Radiosity_OutdoorLight
Radiosity_IndoorLQ
Radiosity_IndoorHQ
```

Wartości `Normal` i `Media` to albo `off` albo `on`.

Dlatego, aby przetestować różne ustawienia, instrukcja `#switch` może być również napisana jak poniżej.


```python
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}
```

Dokładne wartości używane przez te ustawienia można znaleźć w pliku `rad_def.inc`, który znajduje się na przykład w katalogu instalacyjnym POV-Ray: 
```python
/usr/share/povray-3.7/include/
```

W środowisku pracy [Raytracing](Raytracing_Workbench/pl.md) są trzy domyślne szablony: - `ProjectStd.pov`, który w ogóle nie używa `radiosity`. - `RadiosityNormal.pov`, który używa predefiniowanego ustawienia `Radiosity_Normal`. - `RadiosityOutdoorHQ.pov`, który używa predefiniowanego ustawienia `Radiosity_OutdoorHQ`.



## Renderowanie końcowe 

21\. Edytowany plik `.pov` można zapisać po wprowadzeniu wszystkich zmian.

Ostateczna struktura wygląda następująco:

-   Włączenia, z dodatkowymi bibliotekami,
-   Globalne ustawienia, z parametrami radiosity,
-   Sfera niebieska, z jaśniejszym kolorem,
-   Płaszczyzny, ustawione i z teksturami,
-   Wykończenia i tekstury, z własnymi definicjami,
-   Kamera, niezmieniona,
-   Źródło światła, z dodatkowymi właściwościami,
-   Informacje o siatce i bryłach, korzystające z wcześniej zdefiniowanych tekstur.


**Uwaga:**

sekcje pliku `.pov` mogą być w dowolnej kolejności, choć prawdopodobnie łatwiej będzie pracować z plikiem, jeśli informacje o siatce będą na końcu.

Ostateczny rendering można wykonać klikając **<img src="images/Raytrace_Render.svg" width=16px> [Render](Raytracing_Render.md)** lub uruchamiając plik wykonywalny z wiersza poleceń.


```python
povray assembly.pov +W800 +H600 +AM2 +A
```

<img alt="" src=images/12_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_final.png  style="width:600px;">



*align=center|Rozpocznij od standardowego szablonu, wyrenderuj scenę z użyciem POV-Ray, gdzie źródło światła i sfera niebieska są skonfigurowane, materiały przypisane, płaszczyzna podłogi z teksturą parkietu, a tylne ściany z teksturami gipsowymi. Ustawienia radiosity dla wysokiej jakości wyniku: `Radiosity_Final* oraz {{incode|recursion_limit 2`.}}


<div class="toccolours mw-collapsible mw-collapsed">

To jest kompletna zawartość pliku `.pov`, bez ostatniej sekcji, czyli bez siatek.


<div class="mw-collapsible-content">


```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http://www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"
#include "woods.inc"
#include "glass.inc"
#include "stones.inc"
#include "rad_def.inc"

// 
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}

// 


sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}


// 

#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;

// Floor
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}

// Back wall
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}

// Behind camera wall
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}

#declare T_mirror = texture {
    finish { reflection {0.9} }
//    finish { F_MetalE }
}

#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}

#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
// declares position and view direction

// Generated by FreeCAD (http://www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
//default light
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
// Written by FreeCAD http://www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...
```


</div>


</div>



## Uwagi końcowe 

POV-Ray to stosunkowo stary program, który został wydany na początku lat 90. Jego główne zalety w porównaniu z bardziej nowoczesnymi oprogramowaniami to:

-   jest to przetestowane rozwiązanie, które istnieje od wielu lat,
-   działa w wielu systemach operacyjnych,
-   scena może być ustawiona za pomocą jednego pliku tekstowego,
-   do wygenerowania wysokiej jakości obrazu wymaga prostych zasobów obliczeniowych, dlatego działa nawet na stosunkowo starym sprzęcie.

Użytkownikowi zaleca się przeczytanie dokumentacji POV-Ray oraz zapoznanie się z dodatkowymi samouczkami lub przykładami, aby uzyskać odpowiednie ustawienia zgodne z jego potrzebami.

-   [POV-Ray dla systemu Unix w wersji 3.7](http://www.povray.org/documentation/3.7.0/index.html)
-   [Samouczek POV-Ray](http://www.povray.org/documentation/3.7.0/t2_0.html)
-   [Dokumentacja POV-Ray](http://www.povray.org/documentation/3.7.0/r3_0.html)


{{Raytracing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Raytracing](Category_Raytracing.md) > Tutorial FreeCAD POV ray/pl
