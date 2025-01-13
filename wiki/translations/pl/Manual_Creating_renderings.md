# Manual:Creating renderings/pl
{{Manual:TOC}}

[Renderowanie](https://pl.wikipedia.org/wiki/Renderowanie) to proces tworzenia bardzo realistycznych obrazów z modeli 3D poprzez symulację oświetlenia, materiałów i tekstur. Jest powszechnie stosowane w branżach takich jak film, gry wideo i projektowanie produktów, gdzie fotorealistyczne wizualizacje są niezbędne do prezentowania projektów lub koncepcji. Choć renderowanie może tworzyć obrazy, które przypominają realistyczne fotografie, wymaga specjalistycznych narzędzi do kontrolowania takich elementów jak oświetlenie, odbicia i cienie.

FreeCAD koncentruje się jednak głównie na modelowaniu technicznym, a nie na efektach artystycznych czy wizualnych. Jego głównym celem jest tworzenie precyzyjnych modeli 3D na potrzeby inżynierii, projektowania i produkcji. W rezultacie FreeCAD nie posiada zaawansowanych, wbudowanych narzędzi renderujących do fotorealizmu.

FreeCAD oferuje jednak [środowisko pracy Render](https://github.com/FreeCAD/FreeCAD-render?tab=readme-ov-file), które można zainstalować jako dodatek (nie jest to jedno z domyślnych środowisk pracy). To środowisko pracy pozwala użytkownikom łączyć modele FreeCAD z zewnętrznymi silnikami renderującymi, takimi jak Blender Cycles, LuxCoreRender czy POV-Ray. Dzięki środowisku pracy Render użytkownicy mogą wykorzystać swoje modele i skorzystać z potężnych zewnętrznych narzędzi do renderowania projektów z realistycznym oświetleniem i teksturami. Takie podejście utrzymuje FreeCAD jako lekkie i skoncentrowane oprogramowanie, zapewniając jednocześnie elastyczność w zakresie fotorealistycznego renderowania, gdy jest to potrzebne.

Środowisko pracy Render w FreeCAD integruje się z kilkoma zewnętrznymi rendererami, w tym [LuxCoreRender](https://en.wikipedia.org/wiki/LuxRender), [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray) i [Blender Cycles](https://www.cycles-renderer.org/). LuxCoreRender to nowoczesny, oparty o fizykę silnik renderujący, który generuje fotorealistyczne obrazy, ale wymaga znacznej mocy obliczeniowej, zwłaszcza przy dużych scenach. POV-Ray, choć starszy, pozostaje niezawodnym silnikiem [raytracingowym](https://pl.wikipedia.org/wiki/%C5%9Aledzenie_promieni) i jest mniej zasobożerny, choć brakuje mu realizmu nowszych technologii. Blender Cycles, dostępny we FreeCAD po zainstalowaniu Blendera, oferuje potężne rozwiązanie renderujące z obsługą GPU i CPU, umożliwiające efektywne tworzenie wysokiej jakości obrazów. Wymaga jednak oddzielnej instalacji Blendera i eksportu modeli do tego programu w celu renderowania. Każdy z tych rendererów ma swoje mocne strony, w zależności od potrzeb użytkownika w zakresie realizmu, wydajności i możliwości systemowych. Najlepszym sposobem na wybór odpowiedniego silnika jest zapoznanie się z przykładami na stronach internetowych każdego z nich.



### Instalacja

Przed użyciem środowiska pracy Render w FreeCAD należy zainstalować zarówno samo środowisko pracy (jak pokazano w [tej sekcji](https://wiki.freecad.org/Manual:Installing#Installing_additional_content)), jak i jedną z zewnętrznych aplikacji renderujących, takich jak LuxCoreRender, POV-Ray lub Blender Cycles (wraz z zainstalowanym Blenderem). Instalacja tych aplikacji jest zazwyczaj prosta, ponieważ dostarczają one instalatory dla różnych platform i często znajdują się w repozytoriach oprogramowania w dystrybucjach Linuksa. Po zainstalowaniu tych narzędzi możliwe będzie połączenie programu FreeCAD z wybranymi silnikami renderującymi w celu generowania wysokiej jakości obrazów.

Po zainstalowaniu POV-Ray lub LuxCorerender, musimy ustawić ścieżkę do ich głównego pliku wykonywalnego w preferencjach FreeCAD. Zazwyczaj jest to wymagane tylko w systemach Windows i Mac. W systemie Linux FreeCAD wybierze go ze standardowych lokalizacji. Lokalizację plików wykonywalnych povray lub luxrender można znaleźć, wyszukując w systemie pliki o nazwie povray *(lub povray.exe w systemie Windows)* i luxrender *(lub luxrender.exe w systemie Windows)*. W zakładce **Preferencje** można wprowadzić ścieżkę i ustawić pewne parametry.

![](images/FreeCAD_Render_Preferences.png )



### Renderowanie przy użyciu PovRay 

Wykorzystamy stół, który modelowaliśmy w rozdziale [tradycyjne modelowanie](Manual:Traditional_modeling,_the_CSG_way/pl.md), aby stworzyć rendery za pomocą PovRay.

-   Zacznij od załadowania pliku table.FCStd, który modelowaliśmy wcześniej lub pobrania go z linku na dole tego rozdziału, a następnie przejdź do <img alt="" src=images/Render_workbench_icon.svg  style="width:16px;"> [środowiska pracy Render](https://github.com/FreeCAD/FreeCAD-render).
-   Utwórz projekt renderowania, naciskając przycisk na pasku narzędzi odpowiadający wybranemu silnikowi renderującemu. W naszym przykładzie wybierzemy <img alt="" src=images/Render_Povray.svg  style="width:16px;"> renderer povray.
-   Wybierz szablon odpowiedni dla Twojego projektu. W naszym przypadku użyjemy szablonu **povray_sunlight.pov**.
-   Możesz także wypróbować inne szablony po utworzeniu nowego projektu, po prostu edytując jego właściwość *Template*.
-   Nowy projekt został utworzony:

![](images/FreeCAD_Render_Project.png )

-   Możesz dodać żądane obiekty do projektu, zaznaczając je i wybierając opcję <img alt="" src=images/Render_RenderingView.svg  style="width:16px;"> [Widok renderowania](Render_RenderingView/pl.md).

![](images/FreeCAD_Render_Bodies.png )

-   Jeśli chcemy, możemy przypisać materiał do naszych obiektów, wybierając <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Materiał](Arch_SetMaterial/pl.md). W naszym przypadku wybierzemy opcję matte.
-   Teraz możemy nacisnąć przycisk <img alt="" src=images/Render_workbench_icon.svg  style="width:16px;">, a wyrenderowany rezultat pojawi się w osobnym oknie.

![](images/FreeCAD_Render_Result.png )

Prawdę mówiąc, końcowy rezultat nie jest szczególnie imponujący. Proces renderowania jest iteracyjny i wymaga czasu oraz cierpliwości, aby osiągnąć wysokiej jakości efekty. Dodatkowo, jak wspomniano wcześniej, POV-Ray jest nieco ograniczony pod względem realizmu. Zachęcamy do eksperymentowania z różnymi silnikami renderującymi. Procedura pozostaje w dużej mierze taka sama, z tą różnicą, że na początku procesu wybierany jest inny silnik renderujący.

**Do pobrania**

-   Model tabeli: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   Plik wygenerowany podczas tego ćwiczenia: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**Więcej informacji:**

-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)




{{Raytracing Tools navi}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/pl
