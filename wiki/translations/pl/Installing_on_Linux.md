# Installing on Linux/pl
{{TOCright}}



## Przegląd

Instalacja FreeCAD na najbardziej znanych systemach Linux została teraz wsparta przez społeczność, a FreeCAD powinien być dostępny bezpośrednio poprzez menadżer pakietów dostępny w Twojej dystrybucji. Zespół FreeCAD dostarcza również kilka pakietów:

-   \"Oficjalne\" pakiety, gdy pojawiają się nowe wydania dostępne poprzez [pakiety Snap](Ubuntu_Snap/pl.md), [AppImages](AppImage/pl.md), [Flatpaks](Flatpak.md) i [PPA](Installing_on_Linux/pl#Wersja_stabilna_PPA.md).
-   Eksperymentalne lub \"najnowsze\" kompilacje dostępne w codziennym repozytorium [PPA](Installing_on_Linux/pl#Wersja_PPA_rozwojowa_.28dzienna.29.md), [AppImages](AppImage/pl.md), [Ubuntu Snaps](Ubuntu_Snap/pl.md).


<div class="mw-collapsible mw-collapsed toccolours">



## Ubuntu i systemy oparte na Ubuntu 

Wiele dystrybucji Linuksa opiera się na Ubuntu i udostępnia jego repozytoria. Oprócz oficjalnych wariantów *(Kubuntu, Lubuntu i Xubuntu)*, istnieją również dystrybucje pochodne, takie jak Linux Mint, Voyager i inne. Poniższe *(rozwiń)* opcje instalacji powinny być kompatybilne z tymi systemami.


<div class="mw-collapsible-content">



### Wersja oficjalna 

FreeCAD jest dostępny z uniwersalnych repozytoriów Ubuntu i może być zainstalowany poprzez **Centrum Oprogramowania** lub za pomocą tego polecenia w terminalu:


```python
sudo apt install freecad
```


**Note:**

pakiet Ubuntu Universe może być nieaktualny, ponieważ może pozostawać niezgodny z najnowszym stabilnym kodem źródłowym. W tym przypadku, sugeruje się zainstalowanie pakiet `-stable` PPA dostępny poniżej. Dodatkowo, instalacja pakietu `-daily` może być wykonana w celu przetestowania tej gałęzi rozwoju.



### Wersja stabilna PPA 

**Ostrzeżenie:** FreeCAD PPA jest obecnie nie utrzymywany i [poszukuje się ochotników](https://forum.freecadweb.org/viewtopic.php?f=42&t=69055&start=20). Proszę używać alternatywy *(snap, appimage)* do czasu naprawienia problemu!

Osobiste Archiwum Pakietów *(PPA)* dla stabilnego wydania FreeCAD jest utrzymywane przez społeczność FreeCAD na Launchpadzie. Repozytorium Launchpada nazywa się [FreeCAD Stable Releases](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable) .



#### GUI

Instalacja stabilnego PPA za pomocą graficznego interfejsu użytkownika *(GUI)*:

-   Przejdź do **Zainstaluj stabilne PPA za pomocą graficznego interfejsu użytkownika (GUI):**
-   Kliknij na **And**, a następnie skopiuj i wklej następującą linię

:   

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Dodaj źródło, zamknij okno dialogowe i ponownie załaduj źródła oprogramowania, jeśli zostaniesz o to poproszony.

Teraz możesz znaleźć i zainstalować ostatnią stabilną wersję FreeCAD z **Centrum oprogramowania Ubuntu**.



#### CLI

Instalacja stabilnego PPA za pomocą interfejsu wiersza poleceń (CLI):

:   1\. Dodaj PPA do swoich źródeł oprogramowania:

    :   
        
```python
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        
```
        





:   2\. Nie zapomnij pobrać zaktualizowanych list pakietów:

    :   
        
```python
        sudo apt update
        
```
        





:   3.Następnie zainstaluj FreeCAD wraz z dokumentacją offline:

    :   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Note:**

Z powodu problemów z pakowaniem, w niektórych wersjach Ubuntu pakiet `freecad-doc` kolidował z instalacją pakietu FreeCAD lub jednej z jego zależności; jeśli tak jest, usuń pakiet `freecad-doc` i instaluj tylko pakiet `freecad`. Jeśli pakiet `freecad-doc` nie istnieje, to go zignoruj.



#### Weryfikacja instalacji 

:   4\. Po dodaniu stabilnego PPA do źródeł, pakiet `freecad` zainstaluje tę wersję PPA nad zamiast wersji dostarczonej przez repozytorium Ubuntu Universe. Możesz zobaczyć dostępne wersje za pomocą polecenia `apt-cache`.
:   
    
```python
    apt-cache policy freecad
    
```
    





:   Wynik powinien wyglądać podobnie do poniższego *(oczywiście informacje o wersji będą się różnić)*:


```python
freecad:
  Installed: (none)
  Candidate: 2:0.18.4+dfsg1~201911060029~ubuntu18.04.1
  Version table:
     2:0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
        500 http://ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
     0.16.6712+dfsg1-1ubuntu2 500
        500 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
ubuntu@ubuntu:~$ apt-cache policy freecad-doc
```


:   5\. Wywołaj stabilną *(PPA)* wersję programu FreeCAD z GUI lub CLI. Ta ostatnia metoda jest następująca:
:   
    
```python
    ./freecad
    
```
    



### Wersja PPA rozwojowa *(dzienna)* 

Ponieważ FreeCAD jest ciągle rozwijany, możesz chcieć zainstalować pakiet **daily**, aby być na bieżąco z najnowszymi ulepszeniami i poprawkami błędów. Repozytorium jest również hostowane na Launchpadzie i nazywa się [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

Ta wersja jest codziennie kompilowana z oficjalnego repozytorium Master. Należy pamiętać, że chociaż będzie ona zawierać nowe funkcje i poprawki błędów, może mieć nowsze błędy i być niestabilna.

Dodaj PPA daily do źródeł oprogramowania, zaktualizuj listę pakietów i zainstaluj pakiet daily: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Każdego dnia możesz wykonać aktualizacje do najnowszej wersji daily za pomocą: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Note:**

W niektórych przypadkach nowy kod lub zależności dodane do FreeCAD powodują błędy w pakietach. Jeśli tak się stanie, pakiet daily może nie zostać wygenerowany, dopóki opiekunowie nie rozwiążą problemów ręcznie. Jeśli chcesz kontynuować testowanie najnowszego kodu, powinieneś otrzymać kod źródłowy i skompilować FreeCAD bezpośrednio. Instrukcje znajdują się na stronie [kompilacja](compiling.md).

Uruchamianie wersji *daily (PPA)* FreeCAD:

:   
    
```python
    freecad-daily
    
```
    


**Note:**

Możliwe jest zainstalowanie pakietów `-stable` i `-daily` w tym samym systemie. Jest to użyteczne, jeśli chcesz pracować z wersją stabilną i nadal być w stanie testować najnowsze funkcje w rozwoju. Zauważ, że plik wykonywalny dla wersji dziennej to `freecad-daily`, ale dla wersji stabilnej jest to po prostu `freecad`.


</div>


</div>



## Debian i inne systemy pokrewne 

Od czasu Debiana Lenny, FreeCAD jest dostępny bezpośrednio z repozytoriów oprogramowania Debiana i może być zainstalowany poprzez synaptic lub po prostu za pomocą:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD jest zazwyczaj instalowany z YAST *(skrót od \"Jeszcze jedno narzędzie konfiguracyjne\")*, narzędzia do instalacji i konfiguracji systemu operacyjnego Linux, lub też za pomocą dowolnego terminala *(wymagane są prawa administratora)*:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Uwaga:**

Ta procedura obejmuje tylko instalację oficjalnie wydanych **stabilnych**\' wersji programu FreeCAD, w zależności od zainstalowanych linków do repozytoriów pakietów programu w Twojej wersji systemu operacyjnego. Pakiet openSUSE może być przestarzały, ponieważ jego pakiety mogą być opóźnione w stosunku do najnowszego stabilnego kodu źródłowego. W takim przypadku sugeruje się ręczną instalację pakietu z poniżej wskazanych *(Rozwiń)* repozytoriów źródłowych.


<div class="mw-collapsible-content">

Oferowany jest obszerny program wydawniczy dla pakietów FreeCAD. Zapraszamy na stronę w celu przeprowadzenia ankiety:

**[Ankieta dotycząca repozytoriów na openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Ogólnie rzecz biorąc, aby wybrać odpowiednią dystrybucję openSUSE, należy kliknąć przycisk **View**.



### Wersja stabilna 

Wersja pakietu stabilnego: [Stabilne repozytoria na openSUSE](https://software.opensuse.org/package/FreeCAD). W dole strony internetowej należy wybrać właściwą wersję dystrybucji openSUSE.

Uwaga: openSUSE ma kilka opcji do wyboru przy pobieraniu programu FreeCAD. Aby zobaczyć te opcje, odwiedź [Badanie stabilnych repozytoriów na openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).



### Wersja rozwojowa 

Najnowsze wydania rozwojowe AKA **unstable**: [Listy repozytoriów unstable na openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD).

Zaleca się, aby bezpośrednio pobrać pakiety binarne. Następnie wybierz właściwą dystrybucję dla zainstalowanego openSUSE OS.


</div>


</div>

## Gentoo

FreeCAD może być zbudowany/zainstalowany po prostu przez wykonanie:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD jest włączany do oficjalnych pakietów Fedory od czasów Fedory 20. Może być zainstalowany z linii poleceń za pomocą:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

Na starszych wydaniach Fedory, tak to było:


```python
sudo yum install freecad
```

Można również używać menedżerów pakietów gui. Szukaj \"freecad\". \"freecad\". Oficjalna wersja wydania ma tendencję do pozostawania daleko w tyle za wydaniami FreeCAD. [Package: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) pokazuje wersje zawarte w repozytoriach Fedory z czasem i z wersjami.

Więcej aktualnych wersji można uzyskać, pobierając obraz [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)z repozytorium Githuba. Działają one dobrze na Fedorze.

Jeśli chcesz być na bieżąco z najnowszymi codziennymi kompilacjami, FreeCAD jest również dostępny na [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). Aby zainstalować kompilację stamtąd, w sesji terminala wpisz:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

Pozostaje jeszcze copr repozytorium aktywne, więc


```python
sudo dnf upgrade
```

lub odpowiednik, zaktualizuje do najnowszej wersji FreeCAD wraz z aktualizacjami z innych aktywnych repozytoriów. Jeśli chcesz, aby było coś bardziej stabilnego, możesz wyłączyć \@freecad/nightly ponownie po wstępnej instalacji. copr W repozytorium przechowuje się tylko kompilacje z ostatnich 2 tygodni. Rozwiązanie to nie jest wystarczające, jeśli chcesz wybrać konkretną starszą wersję.

Instrukcje są również dostępne na stronie [Kompilacja w systemie Linux](Compile_On_Linux/pl.md), w tym skrypt specjalnie dla Fedory. Z drobną zmianą, aby sprawdzić konkretny *commit* z Git, każda wersja od czasu FreeCAD 0.15 może być zbudowana na dowolnej dystrybucji od Fedory 21.


</div>


</div>

## Arch

Instalacja FreeCAD na Arch Linux i jego pochodnych *(np. Manjaro)*:


```python
pacman -S freecad
```



## Pozostałe

Jeśli dowiesz się, że Twój system posiada FreeCAD, a nie jest to udokumentowane na tej stronie, powiedz nam o tym na forum [1](http://forum.freecadweb.org/viewforum.php?f=21)!

Wiele alternatywnych, nieoficjalnych pakietów FreeCAD jest dostępnych w sieci, na przykład dla systemów takich jak Slackware lub Fedora. Wyszukiwanie w sieci może szybko przynieść oczekiwane rezultaty.



### Instalacja w systemach pokrewnych Linux / Unix 

Wiele popularnych dystrybucji Linuksa zawiera teraz prekompilowany FreeCAD jako część standardowych pakietów. Jest on często nieaktualne, jednak jest to dobre na początek. Sprawdź standardowe menadżery pakietów swojego systemu. Jedna z poniższych *(częściowych)* list poleceń może zainstalować z terminala oficjalną wersję FreeCAD dla twojej dystrybucji. Prawdopodobnie potrzebują one uprawnień administratora.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
pacman -Sy freecad
```

Nazwa pakietu uwzględnia wielkość liter, więc spróbuj zarówno {{Incode|FreeCAD}} jak i {{Incode|freecad}}. Jeśli to nie przyniesie oczekiwanych rezultatów, to prawdopodobnie dlatego, że twój menedżer pakietów nie posiada prekompilowanej wersji FreeCAD. Albo dlatego, że dostępna wersja jest zbyt stara względem oczekiwań. Wtedy możesz możesz spróbować zainstalować pakiety [Flatpak](Flatpak/pl.md) lub [Snap](Ubuntu_Snap/pl.md) *(działają one na większości dystrybucji Linuksa x86_64)* lub spróbować pobrać jedną z następujących wersji: [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) z repozytoriów Githuba. Działają one na większości x86_64 dystrybucji Linuksa, bez żadnej specjalnej instalacji. Upewnij się tylko, że pobrany plik jest oznaczony jako wykonywalny, a następnie uruchom go.

Jeśli to nadal nie jest satysfakcjonujące, a nie możesz znaleźć innego źródła prekompilowanego pakietu spełniającego Twoje wymagania, będziesz musiał [skompilować FreeCAD sam](Compile_on_Linux/pl.md).



## Następny krok 

Po zainstalowaniu FreeCAD, nadszedł czas na [rozpoczęcie pracy](Getting_started.md)!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Developer Documentation](Category_Developer Documentation.md) > Installing on Linux/pl
