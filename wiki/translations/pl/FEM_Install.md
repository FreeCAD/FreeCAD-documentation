# FEM Install/pl
## Wprowadzenie

Aby móc przeprowadzić analizę metodą elementów skończonych *(MES)* w ramach środowiska pracy <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [MES](FEM_Workbench/pl.md), FreeCAD korzysta z dwóch zewnętrznych programów: jeden służy do generowania [siatek](FEM_Mesh/pl.md), a drugi do numerycznego rozwiązywania właściwej analizy. Możesz sprawdzić, czy Twoja instalacja FreeCAD jest gotowa do przeprowadzenia analizy metodą elementów skończonych, uruchamiając przykład [MES CalculiX - wspornik 3D](FEM_CalculiX_Cantilever_3D/pl.md), który jest dołączany do każdej instalacji FreeCAD od wersji 0.17.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;"> 
*Przepływ pracy w środowisku MES. Środowisko to wywołuje dwa zewnętrzne środowiska w celu wykonania siatkowania obiektu bryłowego oraz rozwiązania problemu metodą elementów skończonych.*



### Solver MES 

Domyślny solver do symulacji MES to [CalculiX](FEM_CalculiX/pl.md), prosty solver do analiz strukturalnych. FreeCAD zapisuje plik wejściowy CalculiX\'a, uruchamia solver i odczytuje wyniki, które mogą być zaprezentowane graficznie w rzutni programu. Oznacza to, że plik wykonywalny solvera CalculiX jest niezależny od programu FreeCAD. Ponieważ istnieje wiele programów do generowania siatek, **zalecane jest najpierw zainstalowanie solvera i upewnienie się, że działa prawidłowo**.

Jeśli solver jest poprawnie zainstalowany, możesz uruchomić pojedynczą komendę `ccx` w wierszu poleceń aby uzyskać krótką odpowiedź:


{{SystemInput|User@PC:~$ ccx}}


```python
Usage: CalculiX.exe -i jobname
```

Jeśli solver jest zainstalowany, upewnij się, że środowisko pracy MES może znaleźć jego plik wykonywalny - przejdź do **Edycja → Preferencje ... → MES → CalculiX → Szukaj w znanych katalogach bin**. Jeśli sam skompilowałeś solver, odznacz tę opcję i podaj prawidłową ścieżkę do pliku wykonywalnego. Informacje dotyczące innych solverów, które mogą być używane z FreeCAD, można znaleźć na stronie [MES: Solver](FEM_Solver/pl.md).



### Generowanie siatki MES 

Aby utworzyć [siatkę MES](FEM_Mesh/pl.md), FreeCAD korzysta z programu [Gmsh](http://gmsh.info/) jako domyślnego generatora siatek. W zależności od Twojego systemu operacyjnego i instalacji FreeCAD, Gmsh może być dołączony do plików instalacyjnych FreeCAD. Jeśli tak nie jest, możesz go zainstalować niezależnie i skorzystać z opcji **Edycja → Preferencje → MES → Gmsh** aby ustawić ścieżkę do pliku *gmsh.exe*.

Jeśli program jest poprawnie zainstalowany, możesz uruchomić komendę `gmsh` w wierszu poleceń aby otworzyć jego środowisko graficzne. To środowisko nie jest używane przez FreeCAD, ale pokazuje, że program jest zainstalowany.


{{SystemInput|User@PC:~$ gmsh -info}}


```python
Version          : 3.0.6
License          : GNU General Public License
Build OS         : Linux64
Build date       : 20171107
Build host       : lgw01-amd64-034
Build options    : 64Bit Ann Bamg Bfgs Blas(Generic) Blossom C++11 Cgns Chaco DIntegration Dlopen Fltk Gmm Jpeg Kbipack Lapack(Generic) LinuxJoystick MPI MathEx Med Mesh Mmg3d Mpeg NativeFileChooser Netgen ONELAB ONELABMetamodel OpenCASCADE OpenGL OptHom Parser Plugins Png Post Python Solver TetGen/BR Tetgen Voro3D Zlib
FLTK version     : 1.3.4
OCC version      : 6.9.1
MED version      : 3.0.6
Packaged by      : buildd
Web site         : http://gmsh.info
Mailing list     : gmsh@onelab.info
```

Jeśli zainstalowany jest generator siatek, upewnij się, że środowisko pracy MES może znaleźć jego plik wykonywalny - przejdź do **Edycja → Preferencje → MES → Gmsh → Szukaj w znanych katalogach bin**. Jeśli sam skompilowałeś generator siatek, odznacz tę opcję i podaj prawidłową ścieżkę do pliku wykonywalnego. Zobacz stronę [MES: Siatka](FEM_Mesh/pl.md) aby poznać różne możliwości uzyskiwania siatek do analiz.



### Netgen

Do utworzenia siatki MES możesz również skorzystać z generatora *Netgen*, jako alternatywy dla *Gmsh*. W zależności od Twojego systemu operacyjnego i instalacji FreeCAD, Netgen może być dołączony do plików instalacyjnych FreeCAD.

Jeśli program jest poprawnie zainstalowany, możesz uruchomić komendę `netgen` w wierszu poleceń Linux aby otworzyć jego środowisko graficzne.


{{SystemInput|User@PC:~$ netgen -V}}


```python
NETGEN-6.2-dev
Developed by Joachim Schoeberl at
2010-xxxx Vienna University of Technology
2006-2010 RWTH Aachen University
1996-2006 Johannes Kepler University Linz
Including OpenCascade geometry kernel
Run parallel Netgen with 'mpirun -np xy netgen'
NETGENDIR = .
Tcl header version = 8.6.8
Tcl runtime version = 8.6.8 
using internal Tcl-script
optfile ./ng.opt does not exist - using default values
togl-version : 2
OCC module loaded
```



## Instalacja w środowisku Windows 

Paczki z programem FreeCAD dostępne na stronie [pobierania](Download/pl.md) zawierają już Netgen i CalculiX, więc nie jest wymagana instalacja żadnego dodatkowego oprogramowania. Linki z informacjami gdzie znaleźć lepsze pliki wykonywalne solvera CalculiX niż te dołączone do FreeCAD, można znaleźć w [tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=58792&start=10#p506164)


<div class="mw-collapsible mw-collapsed toccolours">



## Instalacja w środowisku Linux 

Dystrybucje Linuxa mają różne sposoby instalowania oprogramowania. Wiele z nich posiada repozytoria oprogramowania i menedżery paczek. Przed skompilowaniem kodu źródłowego poszukaj w swoim menedżer paczek haseł `netgen`, `gmsh`, `calculix-ccx` lub `ccx` i zainstaluj te programy zgodnie z instrukcjami dla Twojej dystrybucji.


<div class="mw-collapsible-content">



### Instalacja w środowisku Ubuntu PPA 

Archiwa PPA [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) i [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) zapewniają nowszą wersję programu FreeCAD niż ta dostępna w oficjalnych repozytoriach Ubuntu. Te PPA zawierają też najnowsze paczki `netgen`, `gmsh` i `calculix-ccx`. Zobacz stronę [Instalacja na Linux](Installing_on_Linux/pl.md) aby uzyskać więcej informacji o ustawianiu repozytoriów.

Jeśli PPA jest już dodane do Twojego systemu, zainstaluj paczki jak opisano poniżej


```python
sudo apt-get install netgen
sudo apt-get install gmsh
sudo apt-get install calculix-ccx
```

PPA [freecad-community](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) również zapewnia paczki `netgen`, `gmsh` i `calculix-ccx` do testowania. Jeśli są one wystarczająco stabilne, można je dodać do repozytoriów daily lub stable. Pliki wykonywalne dla ccx 2.14 działają w OS Debian Stretch, ale nie w Debian Buster ze względu na problemy z zależnościami.


**Uwaga:**

wątek [Ubuntu Repository](http://forum.freecadweb.org/viewtopic.php?f=18&t=10393) na forum omawia tworzenie paczek Ubuntu PPA. W momencie jego tworzenia, CalculiX nie był uwzględniony w repozytoriach Debiana, więc było kilka osobistych paczek w Launchpad. Tylko jedna paczka powinna być zainstalowana.



### Instalacja w środowisku Arch Linux 

Uzyskaj paczkę CalculiX z [repozytorium AUR](https://aur.archlinux.org/packages/calculix/).



### Instalacja w środowisku Debian 

-   Debian 9 Buster: paczki w [repozytorium](https://packages.debian.org/buster/calculix-ccx) są nieaktualne, ale możesz skorzystać z paczek z Ubuntu PPA (`freecad-community`). Zobacz [ten wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p279925).
-   Debian 8 Stretch: paczki w [repozytorium](https://packages.debian.org/stretch/calculix-ccx) są nieaktualne, ale możesz skorzystać z paczek z Ubuntu PPA (`freecad-community`). Zobacz[ten wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&p=279925#p260872).
-   Debian 7 Jessie: zainstaluj paczki z Debian 8 Stretch używając `dpkg`. Zobacz [ten wątek na forum](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597).



### Instalacja w środowisku openSUSE 

-   [openSUSE:Science Math](https://en.opensuse.org/openSUSE:Science_Math#Mesh_Generation_and_Related_Tools)
-   [netgen automatyczny generator siatek 3D czworościennych](https://software.opensuse.org/package/netgen)
-   [gmsh generator siatek MES 3D](https://software.opensuse.org/package/gmsh)
-   [ccx Otwarty pakiet MES](https://software.opensuse.org/package/ccx)

Dodatkowe paczki są zwykle instalowane z YAST *(Yet another Setup Tool)*, narzędziem do ustawiania i konfiguracji systemu operacyjnego Linux lub w dowolnym wierszu poleceń / konsoli *(wymagane prawa dostępu)* z:

:   
    
```python
    zypper install netgen
    zypper install gmsh
    zypper install ccx
    
```
    



### Pliki wykonywalne CalculiX 

Twórcy solvera CalculiX zapewniają gotowe pliki wykonywalne dla systemu Linux, można je pobrać ze [strony twórców](http://www.dhondt.de/). Jednak, ponieważ różne dystrybucje Linuxa mają różne ścieżki bibliotek, najprawdopodobniej ten plik wykonywalny nie będzie działać bez pewnych poprawek.

Aby używać pliku wykonywalnego z Fedora 21, zobacz [ten wątek na forum](http://forum.freecadweb.org/viewtopic.php?f=18&t=10140). Dla nowszych wersji Fedora, powinieneś sam skompilować CalculiX.

Jeśli korzystasz z tego pliku wykonywalnego, upewnij się, że jest on typu .exe, jest w wykonywalnej ścieżce `$PATH` Twojego systemu i masz wymaganą wersję bibliotek (`libgfortran`, `liblapack`, `libblas`, itd.), z którymi był on kompilowany. Jest to wspomniane w [tym wątku na forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=11830&start=20#p95741).

Skorzystaj z polecenia `ldd` aby zobaczyć biblioteki, do których odwołuje się plik wykonywalny. Zainstaluj wszelkie brakujące zależności.


{{SystemInput|User@PC:~$ ldd /usr/bin/ccx}}


```python
linux-vdso.so.1 (0x00007fffbabdc000)
 libspooles.so.2.2 => /usr/lib/x86_64-linux-gnu/libspooles.so.2.2 (0x00007fe9bd042000)
 libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe9bce23000)
 libarpack.so.2 => /usr/lib/x86_64-linux-gnu/libarpack.so.2 (0x00007fe9bcbd9000)
 liblapack.so.3 => /usr/lib/x86_64-linux-gnu/liblapack.so.3 (0x00007fe9bc353000)
 libgfortran.so.4 => /usr/lib/x86_64-linux-gnu/libgfortran.so.4 (0x00007fe9bbf74000)
 libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe9bbbd6000)
 libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe9bb7e5000)
 libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe9bb5cd000)
 libmpi.so.20 => /usr/lib/x86_64-linux-gnu/libmpi.so.20 (0x00007fe9bb2db000)
 /lib64/ld-linux-x86-64.so.2 (0x00007fe9bdaa9000)
 libblas.so.3 => /usr/lib/x86_64-linux-gnu/libblas.so.3 (0x00007fe9bb080000)
 libopenblas.so.0 => /usr/lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007fe9b8dda000)
 libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fe9b8b9a000)
 libopen-rte.so.20 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.20 (0x00007fe9b8912000)
 libopen-pal.so.20 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.20 (0x00007fe9b8660000)
 librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fe9b8458000)
 libhwloc.so.5 => /usr/lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007fe9b821b000)
 libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe9b8017000)
 libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fe9b7e14000)
 libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007fe9b7c09000)
 libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fe9b79ff000)
```



### Kompilacja CalculiX 

Ponieważ CalculiX jest niezależnym środowiskiem, możesz zainstalować paczkę dla Twojej dystrybucji lub samemu go skompilować. Każda wersja CalculiX od 2.7.x w górę powinna działać z FreeCAD a ponieważ kod nie był znacząco zmieniany w ostatnich latach, starsze wersje niż 2.7.x również mogą działać.

Kompilacja solvera CalculiX jest zadaniem dla doświadczonych użytkowników, wymagającym edycji plików Makefiles i opcji budowania na różnych platformach. Zobacz następujące informacje:

-   Debian: [paczka źródłowa Debian dla CalculiX](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&start=10), [paczka Gmsh 4 do testowania w Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p260506), [Kompilacja CalculiX ccx w systemach Fedora, Ubuntu i Debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Fedora 27, 28, 29: [Kompilacja CalculiX ccx w systemach Fedora, Ubuntu i Debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Dostępna jest wersja CMake paczki źródła w [repozytorium GitHub](https://github.com/ricortiz/CalculiX-cmake), ale na forum FreeCAD nikt nie potwierdził, że działa.



### Kompilacja Netgen 

Netgen był pierwotnie związany z FreeCAD gdy FreeCAD korzystał z OCE, społecznościowego forku OpenCascade (OCCT). Gdy OCE było opóźnione w rozwoju w stosunku do OCCT, FreeCAD powrócił do OCCT. Zepsuło to powiązanie z Netgenem, który mógł się łączyć tylko z OCCT 6.9 lub OCE 0.18 i starszymi. Ponieważ wersje OCCT 7.x usprawniły działanie rdzenia programu FreeCAD, podjęto decyzję o porzuceniu wsparcia dla Netgena na rzecz Gmsh.

Od tego czasu osiągnięto pewien sukces z naprawianiem i łączeniem nowszych wersji Netgena z OCCT 7.x. Niemniej jednak, dołączanie Netgena do programu FreeCAD nadal jest problematyczne.


</div>


</div>



### Instalacja w środowisku MacOSX 


**Te informacje mogą być nieaktualne. Jeśli jesteś użytkownikiem OSX, prosimy o sprawdzenie i aktualizację tej sekcji**

[Paczki rozwojowe OSX](https://github.com/FreeCAD/FreeCAD/releases) programu FreeCAD mogą zawierać Netgen, ale mogą nie zawierać solvera CalculiX.

Zobacz [ten wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&p=198652#p198642) aby uzyskać informacje o instalacji solvera CalculiX oraz [zaktualizowany post](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p273746) aby uzyskać nowsze informacje.

CalculiX:

-   [instalacja solvera CalculiX z brew](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p508724)

Następujące posty mogą być nieaktualne:

-   [MES na Mac OSX, post 1](http://forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [użytkownicy MacPort: prośba o test portu CalculiX](http://forum.freecadweb.org/viewtopic.php?f=8&t=14497)



## Dodatkowe informacje 

[Środowisko pracy MES](FEM_Workbench/pl.md) jest stale rozwijane. Najnowsze informacje można znaleźć na [forum programu FreeCAD](http://www.forum.freecadweb.org/).

Jeśli napotkasz problemy z instalacją programów Netgen, Gmsh lub CalculiX bądź innych zewnętrznych narzędzi, przeszukaj najpierw forum:

-   [netgen site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=netgen+site:forum.freecadweb.org)
-   [gmsh site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=gmsh+site:forum.freecadweb.org)
-   [calculix site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=calculix+site:forum.freecadweb.org)


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Install/pl
