# POV-Ray/pl
**Rozwój POV-Ray wydaje się być wstrzymany. Najnowsza stabilna wersja to 3.7.0.8 (2018-05-27), najnowsza wersja rozwojowa to 3.8.0-x (2019-02-19), [https://github.com/POV-Ray/povray/ oficjalny projekt na GitHub] został ostatnio edytowany 2019-03-08. Usuń to ostrzeżenie, jeśli sytuacja ulegnie zmianie.**



# Opis

POV-Ray *(The Persistence of Vision Raytracer)* jest jednym z dwóch rendererów obsługiwanych przez środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) wraz z [LuxRender](LuxRender/pl.md). Jest on również obsługiwany przez nowe środowisko pracy [Render](https://github.com/FreeCAD/FreeCAD-render), wraz z [LuxCoreRender](LuxCoreRender/pl.md), produktami Appleseed, Blender Cycles i Intel Ospray Studio (eksperymentalnie).



# Instalacja



## Środowisko pracy Raytracing 


**Środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) jest zastępowane przez nowe środowisko [https://github.com/FreeCAD/FreeCAD-render Render], które ma je zastąpić. Środowisko Render można zainstalować poprzez [menadżer dodatków](Std_AddonMgr/pl.md). Informacje tutaj są podane, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' ze środowiskiem Raytracing.**



### Wersja stabilna 

Najnowszą stabilną wersją POV-Ray dostarczaną z plikami binarnymi jest 3.7.0.0 *(2013-11-06)*, która jako pierwsza jest wolnym oprogramowaniem, wydanym na licencji AGPL3 *(lub nowszej)*. Najnowsza stabilna wersja POV-Ray, wydana tylko jako kod źródłowy, to 3.7.0.8 *(2018-05-27)*.

#### Linux

***Skompilowane binaria***

Jeśli twoja dystrybucja ma go w oficjalnych repozytoriach, możesz zainstalować POV-Ray i wszystkie powiązane zależności za pomocą menedżera pakietów. Do takich dystrybucji należą: [Arch Linux](https://archlinux.org/packages/community/x86_64/povray/), [Debian](https://packages.debian.org/search?keywords=povray), [Gentoo](https://packages.gentoo.org/packages/media-gfx/povray), [openSUSE](https://software.opensuse.org/package/povray), [Ubuntu](https://packages.ubuntu.com/search?keywords=povray).

***Kompilacja ze źródeł***

Jeśli twoja dystrybucja nie ma POV-Ray w repozytoriach lub chcesz, możesz skompilować POV-Ray ze źródła. [Pobierz kod źródłowy POV-Ray 3.7.0.8 z GitHub](https://github.com/POV-Ray/povray/archive/refs/tags/v3.7.0.8.tar.gz).

***Konfiguracja FreeCAD***

Po zainstalowaniu POV-Ray uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), [załaduj środowisko Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną POV-Ray, aby wskazywała na instalację POV-Ray, zwykle jest to */usr/bin/povray* i zastosuj.



#### MacOS

Nie ma oficjalnej wersji binarnej POV-Ray 3.7 lub nowszej dla macOS, jeśli chcesz skompilować ją ze źródeł, prawdopodobnie jesteś zdany na siebie.

Najnowsze dostępne [pliki binarne](http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Old-Versions/Official-3.62/Macintosh/povpmac.zip) są starym zamkniętym źródłem POV-Ray 3.6x.

#### Windows

Najnowszą stabilną wersją POV-Ray ze skompilowanymi binariami dla systemu Windows jest POV-Ray 3.7.0.0. [Pobierz ją z GitHub](https://github.com/POV-Ray/povray/releases/download/v3.7.0.0/povwin-3.7-agpl3-setup.exe), uruchom instalator i postępuj zgodnie z proponowanymi krokami.

Domyślnie folderem docelowym jest *C:\\Program Files\\POV-Ray\\v3.7*, a dokumenty i sceny znajdują się w *C:\\Users\\{twój użytkownik}\\Documents\\POV-Ray\\v3.7*.

Po zainstalowaniu POV-Ray uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), [załaduj środowisko Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę do pliku wykonywalnego POV-Ray, aby wskazywała na instalację POV-Ray, zwykle jest to *C:/Program Files/POV-Ray/v3.7/bin/pvengine64.exe* i naciśnij zastosuj.

Następnie, zanim spróbujesz coś wyrenderować, uruchom POV-Ray osobno i [ustaw ograniczenia I/O zgodnie z dokumentacją POV-Ray](https://wiki.povray.org/content/Documentation:Windows_Section_2.1), w przeciwnym razie renderowanie nie będzie działać poprawnie *(lub nie będzie działać wcale)*.



### Wersja rozwojowa 

Rozwój wydaje się być wstrzymany, niemniej jednak najnowsze eksperymentalne kompilacje i kod źródłowy są dostępne. Ponieważ jest to wersja eksperymentalna, odradza się używanie jej w środowiskach produkcyjnych.

#### Linux 

Nie ma oficjalnych binariów rozwojowych POV-Ray, powinieneś skompilować go ze źródła. Najnowsze wydanie oficjalnej gałęzi rozwojowej to [POV-Ray v3.8.0-alpha.10064268](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.tar.gz).

Najnowsze wersje rozwojowe *(nie będące częścią oficjalnej gałęzi rozwojowej)* to [POV-Ray v3.8.0-x.freetype.3](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.tar.gz) i [POV-Ray v3.8.0-x.10064738](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.tar.gz).



#### MacOS 

Nie było kompilacji POV-Ray na macOS od czasu zamkniętej wersji źródłowej 3.6x. Możesz spróbować skompilować go ze źródeł, ale pamiętaj, że może to nie być możliwe.

Najnowsze wydanie oficjalnej gałęzi rozwojowej to [POV-Ray v3.8.0-alpha.10064268](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.zip).

Najnowsze wersje rozwojowe *(nie będące częścią oficjalnej gałęzi rozwojowej)* to [POV-Ray v3.8.0-x.freetype.3](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.zip) i [POV-Ray v3.8.0-x.10064738](https://github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.zip).

#### Windows 

Przede wszystkim musisz zainstalować POV-Ray 3.7, zobacz [instrukcje instalacji stabilnej wersji](POV-Ray/pl#Windows.md). Następnie otwórz katalog instalacyjny POV-Ray, domyślnie *C:\\Program Files\\POV-Ray\\v3.7*, i w podkatalogu *bin* zmień nazwę pliku wykonywalnego POV-Ray, tak aby go nie podmienić. Na przykład zmień jego nazwę na BAK-pvengine64.exe.

Następnie pobierz wersję rozwojową POV-Ray, której chcesz użyć. Najnowsza wersja oficjalnej gałęzi rozwojowej to [POV-Ray v3.8.0-alpha.10064268-av69](https://github.com/POV-Ray/povray/releases/download/v3.8.0-alpha.10064268/povray-3.8.0-alpha.10064268-av691-Win64.7z).

Najnowsze wersje rozwojowe *(nie będące częścią oficjalnej gałęzi rozwojowej)* to [POV-Ray v3.8.0-x.freetype.3-av693](https://github.com/POV-Ray/povray/releases/download/v3.8.0-x.freetype.3/povray-3.8.0-x.freetype.3-av693-Win64.7z) i [POV-Ray v3.8.0-x.10064738-av694](https://github.com/POV-Ray/povray/releases/download/v3.8.0-x.10064738/povray-3.8.0-x.10064738-av694-Win64.7z).

Rozpakuj pobrane archiwum *(jeśli nie masz odpowiedniego oprogramowania, użyj [7-Zip](https://www.7-zip.org/))* i skopiuj plik wykonywalny POV-Ray do folderu \"bin\" instalacji POV-Ray 3.7.



## Środowisko pracy Render 

Na chwilę obecną nie ma znaczących różnic pomiędzy środowiskiem pracy Raytracing i Render w części dotyczącej instalacji zewnętrznego oprogramowania, więc odnieś się do sekcji [środowiska Raytracing](POV-Ray/pl#Środowisko_pracy_Raytracing.md), aby zainstalować POV-Ray i do tej sekcji, aby skonfigurować środowisko pracy Render.

Przede wszystkim zainstaluj środowisko Render poprzez [menadżer dodatków](Std_AddonMgr/pl.md) i uruchom ponownie FreeCAD.

#### Linux 

Po zainstalowaniu środowiska pracy Render i POV-Ray, uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor.md), [załaduj środowisko Render](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do ustawień tego środowiska.

Ustaw ścieżkę wykonywalną POV-Ray, aby wskazywała na instalację POV-Ray, zwykle jest to */usr/bin/povray* i zastosuj zmiany.

#### Windows 

Po zainstalowaniu środowiska pracy Render i POV-Ray, uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor.md), [załaduj środowisko Render](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do ustawień tego środowiska.

Ustaw ścieżkę do pliku wykonywalnego POV-Ray, aby wskazywała na instalację POV-Ray, zwykle jest to *C:/Program Files/POV-Ray/v3.7/bin/pvengine64.exe* i naciśnij zastosuj.

Następnie, zanim spróbujesz coś wyrenderować, uruchom POV-Ray osobno i [ustaw ograniczenia I/O zgodnie z dokumentacją POV-Ray](https://wiki.povray.org/content/Documentation:Windows_Section_2.1), w przeciwnym razie renderowanie nie będzie działać poprawnie *(lub nie będzie działać wcale)*.



---
⏵ [documentation index](../README.md) > POV-Ray/pl
