# LuxCoreRender/pl
**LuxCoreRender nie jest oficjalnie obsługiwany przez środowisko pracy [Raytracing](Raytracing_Workbench/pl.md), zamiast tego jest obsługiwany przez nowe środowisko [https://github.com/FreeCAD/FreeCAD-render Render Workbench], które ma go zastąpić. Środowisko pracy Render można zainstalować poprzez [Menedżer dodatków](Std_AddonMgr/pl.md).**



# Opis

[LuxCoreRender](https://luxcorerender.org) to oparty na fizyce silnik renderujący, będący następcą przestarzałego [LuxRender](LuxRender/pl.md). Nie jest on oficjalnie wspierany przez środowisko pracy [Raytracing](Raytracing_Workbench/pl.md), choć może działać.



# Instalacja



## Środowisko pracy Raytracing 


**Oficjalnie środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) nie współpracuje z LuxCoreRender, a jedynie z przestarzałym [LuxRender](LuxRender/pl.md). Również środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) jest zastępowane przez nowe [https://github.com/FreeCAD/FreeCAD-render środowisko pracy Render], które ma go zastąpić. Środowisko Render można zainstalować poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Informacje te są podane tutaj, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' z środowiskiem Raytracing.**



### Wersja stabilna 

LuxCoreRender jest aktywnie rozwijany, więc aby dowiedzieć się, która wersja jest najnowsza [sprawdź najnowszą stabilną wersję na GitHub](https://github.com/LuxCoreRender/LuxCore/releases/latest).

#### Linux

***Skompilowane binaria***

Jeśli twoja dystrybucja ma go w oficjalnych repozytoriach, możesz zainstalować LuxCoreRender i wszystkie powiązane zależności za pomocą menedżera pakietów. Takie dystrybucje obejmują: [Arch Linux *(AUR)*](https://aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender), [Fedora](https://src.fedoraproject.org/rpms/luxcorerender).

W przeciwnym razie możliwe jest pobranie oficjalnych plików binarnych [najnowszego stabilnego wydania z GitHub](https://github.com/LuxCoreRender/LuxCore/releases/latest). Plik będzie miał postać *luxcorerender-{numer wersji}-linux64.tar.bz2*. Szybszym rozwiązaniem *(choć nie najlepszą praktyką)* jest wyodrębnienie zawartości archiwum w odpowiedniej lokalizacji, takiej jak *\~/LuxCoreRender*. W razie potrzeby zmień uprawnienia do plików, aby użytkownik mógł wykonać wyodrębnione pliki.

***Kompilacja ze źródeł***

Jeśli twoja dystrybucja nie ma LuxCoreRender w repozytoriach, a oficjalne binaria nie działają na twoim komputerze lub chcesz, możesz skompilować LuxCoreRender ze źródła. [Najnowsze stabilne wydanie](https://github.com/LuxCoreRender/LuxCore/releases/latest) zawiera źródło, które będzie czymś w rodzaju *luxcorerender-{numer wersji}.tar.bz2*

***Konfiguracja FreeCAD***

Po zainstalowaniu LuxCoreRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), załaduj środowisko pracy [Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną Luxrender, aby wskazywała na instalację LuxCoreRender, zwykle jest to */usr/bin/luxcoreui*(lub jeśli zainstalowałeś go ręcznie, coś w rodzaju *\~/LuxCoreRender/luxcoreui)* i zastosuj ustawienia.



#### MacOS

[Sprawdź na GitHub najnowszą stabilną wersję](https://github.com/LuxCoreRender/LuxCore/releases/latest), przewiń w dół do sekcji \"Assets\" *(w razie potrzeby rozwiń ją)* i pobierz plik macOS. Będzie to coś w rodzaju *luxcorerender-{numer wersji}-mac64.dmg*.

#### Windows

[Sprawdź na GitHub najnowszą stabilną wersję](https://github.com/LuxCoreRender/LuxCore/releases/latest), przewiń w dół do sekcji *Assets* *(w razie potrzeby rozwiń ją)* i pobierz plik Windows. Będzie to coś w stylu *luxcorerender-{numer wersji}-win64.zip*.

Następnie sprawdź w notatce nad zasobami, czy są jakieś uwagi dotyczące zależności dla użytkowników systemu Windows. Na przykład, aby [używać LuxRender 2.5](https://github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5) należy zainstalować [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://aka.ms/vs/15/release/vc_redist.x64.exe) i [Intel C++ Redistributable](https://software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

Po zainstalowaniu zależności rozpakuj pobrane archiwum w odpowiednim folderze, takim jak *C:\\Tools\\LuxCoreRender*. Unikaj używania folderów systemowych, takich jak *C:\\Program Files* lub *C:\\Program Files (x86)*.

Po zainstalowaniu LuxCoreRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), załaduj środowisko pracy [Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną Luxrender, aby wskazywała na instalację LuxCoreRender, będzie to coś w rodzaju *C:/Tools/LuxCoreRender/luxcoreui.exe* i zastosuj.



### Wersja rozwojowa 

LuxCoreRender jest aktywnie rozwijany, więc aby dowiedzieć się, która wersja jest [najnowszą wersją rozwojową](https://github.com/LuxCoreRender/LuxCore/releases), należy ręcznie sprawdzić na GitHub najnowszą wersję oznaczoną jako Pre-release.

#### Linux 

***Skompilowane binaria***

Jeśli twoja dystrybucja ma ją w oficjalnych repozytoriach, możesz zainstalować wersję rozwojową LuxCoreRender i wszystkie powiązane zależności za pomocą menedżera pakietów. Takie dystrybucje obejmują: [Arch Linux *(AUR)*](https://aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender).

W przeciwnym razie możliwe jest pobranie oficjalnych plików binarnych [najnowszej wersji rozwojowej, oznaczonej jako Pre-release, z GitHub](https://github.com/LuxCoreRender/LuxCore/releases). Plik będzie miał postać *luxcorerender-{numer wersji}-linux64.tar.bz2* lub *luxcorerender-latest-linux64.tar.bz2*. Szybszym rozwiązaniem (choć nie najlepszą praktyką) jest wyodrębnienie zawartości archiwum w odpowiedniej lokalizacji, takiej jak *\~/LuxCoreRender*. W razie potrzeby zmień uprawnienia do plików, aby użytkownik mógł wykonać wyodrębnione pliki.

***Kompilacja ze źródeł***

Jeśli twoje dystrybucje nie mają w repozytoriach wersji rozwojowej LuxCoreRender, a oficjalne binaria nie działają na twoim komputerze lub chcesz, możesz skompilować LuxCoreRender ze źródeł. [Sprawdź GitHub dla najnowszej wersji rozwojowej, oznaczonej jako Pre-release](https://github.com/LuxCoreRender/LuxCore/releases), która zawiera źródło, które będzie czymś w rodzaju \"luxcorerender-{numer wersji}.tar.bz2\"\'

***Konfiguracja FreeCAD***

Po zainstalowaniu LuxCoreRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), załaduj środowisko pracy [Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną Luxrender, aby wskazywała na instalację LuxCoreRender, zwykle jest to */usr/bin/luxcoreui*(lub jeśli zainstalowałeś go ręcznie, coś w rodzaju *\~/LuxCoreRender/luxcoreui)* i zastosuj ustawienia.



#### MacOS 

[Sprawdź na GitHub najnowszą wersję rozwojową](https://github.com/LuxCoreRender/LuxCore/releases), oznaczoną jako Pre-release, przewiń w dół do sekcji *Assets* *(w razie potrzeby rozwiń ją)* i pobierz plik Windows. Będzie to coś w stylu *luxcorerender-{numer wersji}-mac64.dmg* lub *luxcorerender-latest-mac64.dmg*.

#### Windows 

[Sprawdź na GitHub najnowszą wersję rozwojową](https://github.com/LuxCoreRender/LuxCore/releases), oznaczoną jako Pre-release, przewiń w dół do sekcji *Assets* *(w razie potrzeby rozwiń ją)* i pobierz plik Windows. Będzie to coś w stylu *luxcorerender-{numer wersji}-win64.zip* lub *luxcorerender-latest-win64.zip*.

Następnie sprawdź w notatce nad zasobami, czy są jakieś uwagi dotyczące zależności dla użytkowników systemu Windows. Na przykład, aby [używać LuxRender 2.5rc1](https://github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5rc1) należy zainstalować [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://aka.ms/vs/15/release/vc_redist.x64.exe) i [Intel C++ Redistributable](https://software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

Po zainstalowaniu zależności rozpakuj pobrane archiwum w odpowiednim folderze, takim jak *C:\\Tools\\LuxCoreRender*. Unikaj używania folderów systemowych, takich jak *C:\\Program Files* lub *C:\\Program Files (x86)*.

Po zainstalowaniu LuxCoreRender uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), załaduj środowisko pracy [Raytracing](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do [ustawień](Raytracing_Preferences/pl.md) środowiska Raytracing.

Ustaw ścieżkę wykonywalną Luxrender, aby wskazywała na instalację LuxCoreRender, będzie to coś w rodzaju *C:/Tools/LuxCoreRender/luxcoreui.exe* i zastosuj.



## Środowisko pracy Render 

Na chwilę obecną nie ma znaczących różnic między środowiskiem pracy Raytracing i Render w części dotyczącej instalacji zewnętrznego oprogramowania, więc odnieś się do sekcji: środowisko pracy[Raytracing](LuxCoreRender/pl#Raytracing_Workbench.md), aby zainstalować LuxCoreRender i do tej sekcji, aby skonfigurować środowisko pracy Render.

Przede wszystkim zainstaluj środowisko Render poprzez [menadżer dodatków](Std_AddonMgr/pl.md) i uruchom ponownie FreeCAD.

#### Linux 

Po zainstalowaniu środowiska pracy Render i LuxCoreRender, uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), [załaduj środowisko Render](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do ustawień tego środowiska.

Ustaw ścieżkę wykonywalną LuxCore UI, aby wskazywała na instalację LuxCoreRender, zwykle jest to */usr/bin/luxcoreui*(lub jeśli zainstalowałeś go ręcznie, coś w rodzaju *\~/LuxCoreRender/luxcoreui)* i zastosuj ustawienia.

#### Windows 

Po zainstalowaniu środowiska pracy Render i LuxCoreRender, uruchom FreeCAD, otwórz [edytor preferencji](Preferences_Editor/pl.md), [załaduj środowisko Render](Preferences_Editor/pl#Niezaładowane_środowiska_pracy.md) i przejdź do ustawień tego środowiska.

Ustaw ścieżkę poleceń (cli) LuxCore, coś w rodzaju *C:/Tools/LuxCore/pyluxcoretool.exe* i ścieżkę interfejsu użytkownika LuxCore, coś w rodzaju *C:/Tools/LuxCore/luxcoreui.exe*, a następnie zastosuj ustawienia.



---
⏵ [documentation index](../README.md) > LuxCoreRender/pl
