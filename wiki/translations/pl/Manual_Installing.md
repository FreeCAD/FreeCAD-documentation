# Manual:Installing/pl
{{Manual:TOC}}

Program FreeCAD korzysta z licencji [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), która pozwala go pobierać, instalować, redystrybuować i używać w dowolnym celu (komercyjnym lub niekomercyjnym) bez żadnych ograniczeń. Zachowujesz pełną własność plików, które tworzysz.

FreeCAD działa spójnie na systemach Windows, macOS i Linux, choć proces instalacji różni się w zależności od platformy. Dla użytkowników Windows i macOS społeczność FreeCAD oferuje gotowe, skompilowane instalatory. Na systemie Linux kod źródłowy jest dostarczany do opiekunów dystrybucji, którzy pakują oprogramowanie dla swoich specyficznych systemów. Zwykle użytkownicy Linux mogą zainstalować FreeCAD bezpośrednio przez menedżera oprogramowania swojego systemu.

Oficjalną stronę pobierania FreeCAD można znaleźć na [stronie pobierania FreeCAD](https://www.freecad.org/downloads.php). Dodatkowe informacje na temat procesu instalacji można znaleźć na dedykowanej [stronie wiki o pobieraniu](https://wiki.freecad.org/Download).

**Wersje FreeCAD**

Oficjalne stabilne wersje FreeCAD są dostępne na wspomnianej stronie pobierania oraz w menedżerze oprogramowania Twojej dystrybucji. Jednak tempo rozwoju FreeCAD jest szybkie, z nowymi funkcjami i poprawkami błędów dodawanymi niemal codziennie. Z powodu długich okresów między stabilnymi wydaniami, możesz chcieć eksperymentować z nowszymi wersjami FreeCAD. Te wersje deweloperskie, lub pre-wydania, można znaleźć na tej samej stronie pobierania. Dla użytkowników Ubuntu lub Fedory społeczność FreeCAD udostępnia także [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) oraz [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'daily builds\', które są regularnie aktualizowane o najnowsze zmiany.

Jeśli planujesz instalować FreeCAD na maszynie wirtualnej, pamiętaj, że jego wydajność może być mocno ograniczona, potencjalnie nawet uniemożliwiając pracę, ze względu na ograniczoną obsługę OpenGL na wielu maszynach wirtualnych.



## Instalacja w środowisku Windows 

1.  Pobierz instalator (.exe) ze strony pobierania. Instalatory FreeCAD powinny działać na każdej wersji Windows od Windows 7 wzwyż.
2.  Zaakceptuj warunki licencji LGPL; będzie to jeden z nielicznych przypadków, w których możesz bezpiecznie kliknąć przycisk \"zaakceptuj\" bez czytania tekstu. Brak ukrytych klauzul: ![](images/LicenseAgreement_0212.jpeg )
3.  Możesz zostawić domyślną ścieżkę lub zmienić ją, jeśli chcesz: ![](images/Path0212.jpeg )
4.  Upewnij się, że zaznaczone są wszystkie komponenty do zainstalowania: ![](images/Components0212.jpeg )
5.  To wszystko. Instalacja została zakończona i możesz zacząć odkrywać możliwości FreeCAD.

**Instalacja wersji rozwojowej**

Pakowanie FreeCAD i rozwijanie instalatora wymaga znacznego nakładu czasu i wysiłku. W związku z tym wersje deweloperskie (zwane również wersjami pre-release) są zazwyczaj udostępniane w postaci archiwów .zip lub .7z znajdujących się na [stronie pobierania FreeCAD](https://www.freecad.org/downloads.php). Nie ma potrzeby formalnego procesu instalacji przy tych plikach; wystarczy wyodrębnić zawartość i uruchomić FreeCAD, klikając dwukrotnie plik FreeCAD.exe znajdujący się w środku. Takie podejście pozwala również na utrzymanie zarówno stabilnych, jak i \"niestabilnych\" wersji na tym samym komputerze. To jak posiadanie zarówno niezawodnego codziennego samochodu, jak i eksperymentalnego plecaka odrzutowego w garażu!



## Instalacja w środowisku Linux 

Dla użytkowników nowoczesnych dystrybucji Linuksa, takich jak Ubuntu, Fedora, openSUSE, Debian, Mint czy Elementary, instalacja FreeCAD jest prosta i ogranicza się do jednego kliknięcia. Możesz bezproblemowo zainstalować go za pomocą narzędzia do zarządzania oprogramowaniem dostarczonego przez Twoją dystrybucję, choć wygląd tych narzędzi może różnić się od przedstawionych obrazków, ponieważ każda dystrybucja używa swojego własnego, charakterystycznego programu.

1.  Otwórz menedżera oprogramowania i wyszukaj \"freecad\":
2.  Kliknij przycisk \"zainstaluj\" i to wszystko, FreeCAD zostanie zainstalowany. Nie zapomnij go później ocenić!
    <img alt="" src=images/linuxInstallation.png  style="width:800px;">

**Alternatywne sposoby**

Jedną z wielkich przyjemności korzystania z Linuksa jest ogromna liczba opcji dostosowywania swojego doświadczenia z oprogramowaniem, więc nie krępuj się! Dla użytkowników Ubuntu i jego pochodnych, FreeCAD można zainstalować z [PPA](https://launchpad.net/~freecad-maintainers) utrzymywanego przez społeczność FreeCAD, które zawiera zarówno wersje stabilne, jak i deweloperskie. Na Fedory dostępne są najnowsze wersje deweloperskie FreeCAD za pomocą [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). Dodatkowo, ponieważ FreeCAD jest oprogramowaniem open source, masz także wolność, aby [skompilować FreeCAD samodzielnie](Compiling/pl.md).



## Instalacja w środowisku Mac OS 

Instalacja FreeCAD na Mac OSX jest obecnie równie łatwa jak na innych platformach. Ponieważ jednak w społeczności jest mniej osób posiadających komputery Mac, dostępne pakiety czasami pozostają kilka wersji w tyle za innymi platformami.

1.  Pobierz spakowany pakiet odpowiadający Twojej wersji.
2.  Otwórz folder Pobrane i rozpakuj pobrany plik zip: ![](images/Freecad-mac-01.jpg )
3.  Przeciągnij aplikację FreeCAD z pliku zip do folderu Aplikacje: ![](images/Freecad-mac-02.jpg )
4.  To wszystko, FreeCAD jest zainstalowany! ![](images/Freecad-mac-03.jpg )
5.  Jeśli system uniemożliwia uruchomienie FreeCAD z powodu ograniczonych uprawnień dla aplikacji niepochodzących ze sklepu App Store, należy włączyć je w ustawieniach systemu: ![](images/Freecad-mac-04.jpg )



### Deinstalacja

Zakladamy, że nigdy nie będziesz chciał rozstać się z FreeCAD, ale jeśli kiedykolwiek będziesz musiał go odinstalować, proces jest prosty. Na Windows użyj znanej opcji \"usuń oprogramowanie\" z panelu sterowania. Dla użytkowników Linuksa, odinstaluj go za pomocą tego samego menedżera oprogramowania, którego używałeś do instalacji. Użytkownicy Maca mają to najłatwiej --- wystarczy przeciągnąć FreeCAD z folderu Aplikacje do kosza.



### Ustawianie podstawowych preferencji 

Po zainstalowaniu programu FreeCAD, prawdopodobnie zechcesz spersonalizować go, dostosowując niektóre ustawienia. Możesz znaleźć ustawienia preferencji w FreeCAD, przechodząc do **Edycja → Preferencje** w menu. Poniżej znajdują się kilka podstawowych ustawień, które warto rozważyć do zmiany od razu, ale śmiało eksploruj różne strony preferencji, aby jeszcze bardziej dostosować oprogramowanie do swoich potrzeb.



#### Kategoria Ogólne, zakładka Ogólne 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Język**: Domyślnie FreeCAD wybierze język systemu operacyjnego, ale masz możliwość jego zmiany. Dzięki zaangażowaniu wielu współtwórców, FreeCAD jest dostępny w szerokiej gamie języków.
2.  **Jednostki**: To ustawienie pozwala na wybór domyślnego systemu jednostek dla Twoich projektów.



#### Kategoria Ogólne, zakładka Dokument 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Utwórz nowy dokument przy uruchomieniu**: FreeCAD automatycznie otworzy nowy dokument za każdym razem, gdy program się uruchomi.
2.  **Opcje przechowywania**: Skonfiguruj ustawienia tutaj, które pomogą Ci odzyskać pracę w przypadku awarii.
3.  **Autorstwo i licencja**: W tej sekcji możesz ustawić preferencje dla nowych plików. Aby ułatwić udostępnianie, rozważ rozpoczęcie od bardziej liberalnej licencji copyleft, takiej jak Creative Commons.



#### Kategoria Wyświetlanie, zakładka Nawigacja 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoomuj na kursorze**: Po włączeniu, akcje przybliżania będą koncentrować się na kursie myszy. Jeśli wyłączone, zoom będzie skupiać się na środku widoku.
2.  **Odwróć zoom**: Ta opcja odwraca kierunek zoomu w stosunku do ruchu myszy.



#### Zakładka Środowiska pracy 

![](images/FreeCAD_022_WBMenu.png )

Chociaż FreeCAD zwykle otwiera stronę startową, to ustawienie pozwala na ominięcie jej. Możesz rozpocząć bezpośrednio w wybranym środowisku pracy. Dodatkowo, możesz dostosować, które środowiska pracy mają być wyświetlane w menu selektora.



#### Zakładka Import-Export 

![](images/FreeCAD_022_ImportExport.png )

Tu zdefiniuj podstawowe parametry dla importu i eksportu do różnych formatów.



### Instalacja dodatkowej zawartości 

W miarę jak społeczność FreeCAD się rozwija, a możliwości dostosowywania rosną, pojawia się coraz więcej zewnętrznych wkładów i projektów pobocznych od członków społeczności i entuzjastów, które można znaleźć w Internecie. Wiele z tych projektów przyjmuje formę środowisk pracy lub makr, które możesz łatwo dodać do swojej skrzynki narzędziowej za pomocą [Menedżera dodatków](Std_AddonMgr/pl.md), dostępnego z menu Narzędzia. Menedżer dodatków otwiera świat możliwości, pozwalając na instalację różnych interesujących komponentów, takich jak:

![](images/FreeCAD_022_AddonsMenu.png )

1.  [Biblioteka części](https://github.com/FreeCAD/FreeCAD-library). Ta biblioteka to prawdziwa skarbnica użytecznych modeli lub fragmentów modeli stworzonych przez użytkowników FreeCAD. Wszystkie przedmioty w tej bibliotece są dostępne do swobodnego użytku w Twoich projektach i można je bezpośrednio uzyskać w Twojej konfiguracji FreeCAD.
2.  [Dodatkowe środowiska pracy](https://github.com/FreeCAD/FreeCAD-addons). Są to specjalistyczne rozszerzenia, które zwiększają funkcjonalność FreeCAD w określonych zadaniach. Przykładowe aplikacje obejmują animowanie części modeli lub zarządzanie konkretnymi procesami konstrukcyjnymi, takimi jak składanie blachy czy BIM (Modelowanie Informacji o Budynku). Szczegółowe informacje o każdym środowisku pracy, w tym przegląd narzędzi, które zawiera, dostępne są na stronie każdego dodatku, do której można przejść za pomocą odpowiedniego linku w menedżerze dodatków.
3.  Szeroka gama [makr](https://github.com/FreeCAD/FreeCAD-macros) jest również dostępna do pobrania. Mogą one znacznie uprościć Twoją pracę, a szczegółową dokumentację na temat ich użycia można znaleźć na [wiki programu FreeCAD](Macros_recipes/pl.md).

Od wersji FreeCAD v0.17.9940 zalecaną metodą instalacji wszystkich powyższych narzędzi jest wbudowany Menedżer dodatków. Jednak jeśli z jakiegoś powodu ta opcja nie jest dostępna, zawsze możliwa jest instalacja ręczna. Więcej informacji można znaleźć na stronie [dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons).

**Więcej informacji:**

-   [Więcej możliwości pobierania](Download/pl.md)
-   [FreeCAD PPA dla Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [dodatki FreeCAD PPA dla Ubuntu](https://launchpad.net/freecad-extras)
-   [Samodzielna kompilacja FreeCAD](Compiling/pl.md)
-   [tłumaczenie GUI FreeCAD](https://crowdin.com/project/freecad)
-   [GitHub dla FreeCAD](https://github.com/FreeCAD)
-   [Menadżer dodatków](Std_AddonMgr/pl.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/pl
