# <img alt="Ikona środowiska pracy POV-Ray-Rendering" src=images/POV-Ray-Rendering_workbench_icon.svg  style="width:64px;"> POV-Ray-Rendering Workbench/pl






## Wprowadzenie

Środowisko POV-Ray-Rendering jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md) pozwalającym na łatwe stworzenie wizualizacji twojego projektu, nie ograniczając przy tym możliwości bardziej biegłym użytkownikom. Środowisko wykorzystuje oprogramowanie [POV-Ray](http://www.povray.org/).

<img alt="" src=images/POV-Ray-Rendering_Example.png  style="width:600px;">



## Funkcjonalności



### Teksturowanie

Istnieje ponad 100 predefiniowanych tekstur, które można zastosować, ale można również zdefiniować własne tekstury.

<img alt="" src=images/POV-Ray-Rendering_Textures.png  style="width:600px;">



#### Miniatury i podgląd na żywo 

Aby zobaczyć wpływ wybranych opcji tekstury, możesz sprawdzić wstępnie renderowaną miniaturę lub użyć podglądu na żywo, aby wyrenderować teksturę.



### Oświetlenie

Dzięki trzem rodzajom światła: obszarowemu, punktowemu i skupionemu oraz ich różnym opcjom można tworzyć zaawansowane oświetlenie.

<img alt="" src=images/POV-Ray-Rendering_Lights.png  style="width:600px;">



#### Oświetlenie pośrednie (GI) 

Środowisko pracy posiada opcję włączenia oświetlenia pośredniego w celu tworzenia bardziej realistycznych obrazów.

<img alt="" src=images/POV-Ray-Rendering_IndirectLighting.png  style="width:600px;">



### Środowiska HDRI 

Dzięki obsłudze środowisk HDRI, piękne otoczenia są łatwe w użyciu.

<img alt="" src=images/POV-Ray-Rendering_HDRI.png  style="width:600px;">



### Plik inc użytkownika 

Zaawansowani użytkownicy, którzy chcą uzyskać dostęp do \"wszystkich\" opcji renderera [POV-Ray](http://www.povray.org/), mogą to zrobić, tworząc specjalny plik. Więcej szczegółów można znaleźć na stronie [Power User](https://gitlab.com/usbhub/exporttopovray/-/blob/master/doc/PowerUser.md) na naszej Wiki.



## Użycie

Oto prosta demonstracja środowiska pracy:

![](images/POV-Ray-Rendering_Demo.gif )

W innych zakładkach znajduje się o wiele więcej opcji, z którymi można zapoznać się samodzielnie lub odwiedzając naszą Wiki: [Wiki Środowisko pracy](https://gitlab.com/usbhub/exporttopovray/-/tree/master/doc).



## Instalacja

To środowisko pracy może być instalowane i aktualizowane z poziomu <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menedżera dodatków](Std_AddonMgr/pl.md). Używany przez środowisko pracy renderer [POV-Ray](http://www.povray.org/) musi zostać zainstalowany osobno. Dla użytkowników systemu Windows instalator można pobrać ze strony [POV-Ray do pobrania](https://www.povray.org/download/), dla użytkowników systemu Linux można go zazwyczaj zainstalować z menedżera pakietów. Jeśli korzystasz z komputera Mac, szczegółowe instrukcje znajdziesz na stronie [POV-Ray Wiki](https://wiki.povray.org/content/HowTo:Install_POV).

Aby zakończyć instalację, ścieżka do pliku wykonywalnego POV-Ray musi być zdefiniowana w preferencjach środowiska pracy, zazwyczaj są to ścieżki domyślne:

-   **Windows:** **C:/Program Files/POV-Ray/v3.7/bin/pvengine64.exe** (folder **v*.*** może się zmienić w zależności od wersji POV-Ray)
-   **Linux:** **/usr/bin/povray**
-   **MacOS:** Niedostępne. Jeśli masz więcej informacji, daj nam znać.

<img alt="" src=images/POV-Ray-Rendering_ExePath.png  style="width:600px;">



## Przybory

-   <img alt="" src=images/POV-Ray-Rendering_OpenDialog.svg  style="width:32px;"> Export Model: Otwiera okno dialogowe pozwalające na skonfigurowanie oraz wyrenderowanie sceny.

-   <img alt="" src=images/POV-Ray-Rendering_PointLight.svg  style="width:32px;"> Insert Point Light: Dodaj światło punktowe.

-   <img alt="" src=images/POV-Ray-Rendering_AreaLight.svg  style="width:32px;"> Insert an Area Light: Dodaj światło obszarowe.

-   <img alt="" src=images/POV-Ray-Rendering_SpotLight.svg  style="width:32px;"> Insert a Spot Light: Dodaj światło reflektorowe.



## Odniesienia

-   Autorzy:
    -   Usb Hub: <https://gitlab.com/usbhub>
    -   DerUhrmacher: <https://gitlab.com/DerUhrmacher>
-   Kod dostępny na GitHub: <https://github.com/TheRaytracers/freecad-povray-render>



## Linki do środowiska pracy POV-Ray 

-   Dokumentacja: <https://gitlab.com/usbhub/exporttopovray/-/tree/master/doc>
-   Wątek na forum: <https://forum.freecadweb.org/viewtopic.php?f=9&t=48629>
-   Zgłaszanie błędów: Błędy można zgłaszać na GitHub oraz oficjalnym Forum FreeCAD



## Inne użyteczne odnośniki 

-   [Zewnętrzne środowiska prracy](External_workbenches/pl.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > POV-Ray-Rendering Workbench/pl
