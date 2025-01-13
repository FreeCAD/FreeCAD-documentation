# LuxRender/pl
**LuxRender nie jest już rozwijany, ponieważ projekt został zrestartowany jako [LuxCoreRender](LuxCoreRender/pl.md) z poważnym przepisaniem kodu i wieloma zmianami naruszającymi kompatybilność. Informacje tutaj są podane, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' ze środowiskiem pracy [Raytracing](Raytracing_Workbench/pl.md), które oficjalnie obsługuje tylko LuxRender. W każdym razie wydaje się, że działa również z [LuxCoreRender](LuxCoreRender/pl.md), więc warto rozważyć wypróbowanie go przed użyciem LuxRender.**



# Opis

[LuxRender](https://luxcorerender.org/history/) jest jednym z dwóch silników renderujących wspieranych przez środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) wraz z [POV-Ray](POV-Ray/pl.md). W 2013 roku projekt został reaktywowany, stając się [LuxCoreRender](LuxCoreRender/pl.md), z poważnym przepisaniem kodu i zmianami łamiącymi kompatybilność, tym samym projekt LuxRender został porzucony. Oficjalnie [LuxCoreRender](LuxCoreRender/pl.md) nie jest wspierany przez środowisko [Raytracing](Raytracing_Workbench/pl.md), choć być może warto spróbować go użyć.



# Instalacja



## Środowisko pracy Raytracing 


**Środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) jest zastępowane przez nowe środowisko [https://github.com/FreeCAD/FreeCAD-render Render], które ma być następcą. Środowisko Render można zainstalować poprzez [menadżer dodatków](Std_AddonMgr/pl.md). Informacje tutaj są podane, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' ze środowiskiem Raytracing.**



### Wersja stabilna 

Najnowsza stabilna wersja to [LuxRender 1.6 *(2017-12-28)*](https://github.com/LuxCoreRender/LuxCore/releases/tag/luxrender_v1.6).

#### Linux

***Skompilowane binaria***

Ponieważ LuxRender nie jest już rozwijany, prawie żadna dystrybucja nie ma go w swoich repozytoriach, więc będziesz musiał ręcznie zainstalować oficjalne binaria. Najpierw sprawdź, czy twoja karta graficzna obsługuje [OpenCL](https://en.wikipedia.org/wiki/OpenCL) i czy masz zainstalowane wszystkie niezbędne zależności. Jeśli tak, pobierz [LuxRender 1.6 z obsługą OpenCL](https://github.com/LuxCoreRender/LuxCore/releases/download/luxrender_v1.6/lux-v1.6-x86_64-sse2-OpenCL.tar.bz2). W przeciwnym razie pobierz [LuxRender 1.6 bez OpenCL](https://github.com/LuxCoreRender/LuxCore/releases/download/luxrender_v1.6/lux-v1.6-x86_64-sse2-NoOpenCL.tar.bz2), ale rozważ zakup nowszej karty graficznej lub zainstalowanie niezbędnego oprogramowania, aby włączyć ją na swoim komputerze.

Szybszym rozwiązaniem *(choć nie najlepszą praktyką)* jest wyodrębnienie zawartości archiwum w odpowiedniej lokalizacji, takiej jak *\~\\LuxRender*. W razie potrzeby zmień uprawnienia do plików, aby użytkownik mógł wykonać wyodrębnione pliki.

***Kompilacja ze źródeł***

Jeśli twoja dystrybucja nie ma LuxRender w repozytoriach i oficjalne binaria nie działają na twojej dystrybucji, lub jeśli chcesz, możesz skompilować LuxRender ze źródła. [Pobierz kod źródłowy LuxRender 1.6 z GitHub](https://github.com/LuxCoreRender/LuxCore/archive/refs/tags/luxrender_v1.6.tar.gz).

***Konfiguracja FreeCAD***

Po zainstalowaniu LuxRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), załaduj środowisko pracy [Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną Luxrender, aby wskazywała na instalację LuxRender, w szczególności na plik wykonywalny *luxrender* i zastosuj. W powyższym przykładzie, ścieżką będzie *\~\\LuxRender\\luxrender*.



#### MacOS

Użyj [oficjalnego instalatora LuxRender 1.6 dla OSX](https://github.com/LuxCoreRender/LuxCore/releases/download/luxrender_v1.6/LuxRender_1.6_OSXIntel_64bit.dmg).

#### Windows

Najpierw sprawdź, czy twoja karta graficzna obsługuje [OpenCL](https://en.wikipedia.org/wiki/OpenCL) i czy masz zainstalowane niezbędne sterowniki graficzne. Jeśli tak, pobierz [LuxRender 1.6 with OpenCL support setup](https://github.com/LuxCoreRender/LuxCore/releases/download/luxrender_v1.6/LuxRender.1.6.x64.OpenCL.Setup.exe). W przeciwnym razie pobierz [LuxRender 1.6 without OpenCL setup](https://github.com/LuxCoreRender/LuxCore/releases/download/luxrender_v1.6/LuxRender.1.6.x64.NoOpenCL.Setup.exe), ale rozważ zakup nowszej karty graficznej lub zainstalowanie niezbędnego oprogramowania, aby włączyć ją na komputerze. Następnie uruchom pobrany instalator i postępuj zgodnie z proponowanymi krokami.

Domyślnie folderem docelowym jest *C:\\Program Files\\LuxRender*, a przykładowe sceny znajdują się w *C:\\Users\\Public\\Documents\\LuxRender\\Example Scene*.

Po zainstalowaniu LuxRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), [załaduj środowisko Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę do pliku wykonywalnego Luxrender, aby wskazywała na instalację LuxRender, zwykle jest to *C:/Program Files/LuxRender/luxrender.exe* i naciśnij zastosuj ustawienia.



### Wersja rozwojowa 

Nie istnieje wersja rozwojowa LuxRender, gdyż rozwój został wstrzymany na rzecz uruchomienia wersji [LuxCoreRender](LuxCoreRender/pl.md).



## Środowisko pracy Render 

[Środowisko pracy Render](https://github.com/FreeCAD/FreeCAD-render) porzuciło wsparcie dla LuxRender, ponieważ jest ono przestarzałe. Zamiast tego obsługuje nowoczesny ponowne zaprojektoany [LuxCoreRender](LuxCoreRender/pl.md).



---
⏵ [documentation index](../README.md) > LuxRender/pl
