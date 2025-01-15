# Compile on Docker/pl
}









## Informacje ogólne 

Wśród opcji kompilacji i instalacji FreeCAD istnieje możliwość użycia Dockera. Ta metoda jest przydatna przede wszystkim dla programistów FreeCAD korzystających z komputerów z systemem Linux lub Mac OS.



### Korzyści

Wszystkie zależności FreeCAD są już zainstalowane, kompatybilne ze sobą i odpowiednio skonfigurowane, co pozwala na bardzo szybkie rozpoczęcie programowania.

-   Zależności są zawarte w kontenerze docker, co zapobiega zanieczyszczeniu stacji roboczej niechcianymi pakietami i kolizji wersji.
-   Kod źródłowy i katalogi kompilacji znajdują się poza kontenerem docker. Pozwala to na korzystanie z preferowanych edytorów, systemów wersjonowania, narzędzi deweloperskich itp. bez konieczności konfigurowania ich w kontenerze docker. Możesz po prostu używać ich normalnie, bezpośrednio ze stacji roboczej. *(Oznacza to również, że nie musisz odbudowywać kontenera docker za każdym razem, gdy chcesz skompilować FreeCAD)*.
-   Dla tych, którzy używają niejasnych dystrybucji \*nix i [instrukcje nie są dostępne](Compile_on_Linux/pl#Pobranie_zależności.md) do pobierania zależności, wszystko, co musisz zainstalować na swojej stacji roboczej, to docker, który jest dość powszechnie dostępny w wielu dystrybucjach.
-   Zapewnia on statyczne, niezmienne środowisko programistyczne. Osobiście uważam to za przydatne podczas programowania, aby zmniejszyć liczbę potencjalnych zmiennych, które mogą powodować problemy. Wiesz, że nie zmieniłeś czegoś ezoterycznego w środowisku między kompilacjami. W przypadku deweloperów współpracujących ze sobą i korzystających z tego samego kontenera docker, można mieć pewność, że obaj pracują w tym samym środowisku, co zmniejsza liczbę błędów komunikacyjnych spowodowanych różnicami w środowisku.



## Repozytorium Docker 

-   Oryginał: <https://gitlab.com/daviddaish/freecad_docker_env>
-   Oficjalny: <https://GitHub.com/FreeCAD/Docker>



## Wymagania wstępne 

-   10 GB wolnej przestrzeni dyskowej.
-   Docker.



## Instalacja



### Pobieranie źródła 

Najlepszym sposobem na uzyskanie kodu źródłowego FreeCAD jest sklonowanie repozytorium [Git](https://github.com/FreeCAD/FreeCAD). W tym celu potrzebny jest program `git`, który można łatwo zainstalować w większości dystrybucji systemów Linux i Mac OS, a także można go uzyskać z [oficjalnej strony internetowej Git](http://git-scm.com/).

Poniższe polecenie umieści kopię najnowszej wersji kodu źródłowego programu FreeCAD w nowym katalogu o nazwie `freecad-source`.


{{Code|lang=bash|code=
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
}}

Więcej informacji na temat używania środowiska Git i wnoszenia kodu do projektu można znaleźć na stronie [Zarządzanie kodem źródłowym](Source_code_management/pl.md).



### Utwórz katalog kompilacji 

Utwórz katalog do przechowywania skompilowanego źródła FreeCAD.


{{Code|lang=bash|code=
mkdir ~/my_code/freecad_build
}}



### Ściągnij obraz Docker 

Ściągnij obraz Docker. *(Oficjalny obraz wkrótce)*.


{{Code|lang=bash|code=
docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



## Zezwól na dostęp do menedżera okien 

Aby FreeCAD mógł uruchomić swój graficzny interfejs użytkownika z poziomu kontenera Docker, należy nadać Dockerowi uprawnienia dostępu do menedżera okien. W większości dystrybucji Linuksa jest to system okien X. Możesz użyć poniższego polecenia, aby zezwolić Dockerowi na dostęp do X, aż do ponownego uruchomienia lub wylogowania komputera.


{{Code|lang=bash|code=
xhost +
}}

Jeśli jesteś połączony z niezaufanymi systemami, na przykład przez `ssh`, sprawi to, że będziesz podatny na złośliwy kod. Zamknij wszystkie połączenia `ssh` lub sprawdź bezpieczniejsze uprawnienia xhost, co wykracza poza zakres tego samouczka.



#### Użytkownicy systemu Mac OS 

Dla tych, którzy używają Mac OS, system okien X może nie być zainstalowany. Projekt XQuartz to długo działający projekt open source, który pozwoli ci dodać go do twojego komputera. [Można go znaleźć na stronie domowej](https://www.xquartz.org/).



### Uruchomienie obrazu docker 

Przypisz zmienne środowiskowe, aby kontener Docker zamontował kod źródłowy FreeCAD i katalog kompilacji. Ponadto możesz zamontować dodatkowy katalog zawierający dowolne pliki, których chcesz użyć do celów testowych. W poniższym fragmencie pozostawiliśmy go jako katalog domowy jako proste ustawienie domyślne.


{{Code|lang=bash|code=
fc_source=~/my_code/freecad_source
fc_build=~/my_code/freecad_build
other_files=~/
}}

Uruchom obraz Docker.


{{Code|lang=bash|code=
docker run -it --rm \
-v $fc_source:/mnt/source \
-v $fc_build:/mnt/build \
-v $other_files:/mnt/files \
-e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



### Kompilacja FreeCAD 

Możesz zbudować FreeCAD za pomocą zainstalowanego skryptu kompilacji lub przy użyciu preferowanej metody.


{{Code|lang=bash|code=
/root/build_script.sh
}}



### Uruchomienie FreeCAD 

Po zbudowaniu FreeCAD można go uruchomić w normalny sposób.


{{Code|lang=bash|code=
/mnt/build/bin/FreeCAD
}}

Dołączone katalogi można znaleźć w katalogu `/mnt`.



## Dyskusja

-   [Kontener kompilacji środowiska Docker](https://forum.freecadweb.org/viewtopic.php?f=4&t=42954)
-   [Konfiguracja VSCode z Dockerem (1)](https://forum.freecadweb.org/viewtopic.php?f=10&t=48266)
-   [Konfiguracja VSCode z Dockerem (2)](https://forum.freecadweb.org/viewtopic.php?p=427812#p427812)



## Powiązane

-   [AppImage](AppImage/pl.md)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Compile on Docker/pl
