# Compile on Linux/pt-br
**Há um contêiner experimental do FreeCAD Docker que está sendo testado para desenvolvimento em FreeCAD. Leia mais sobre isso em [Compilar no Docker](Compile_on_Docker/pt-br.md)**






## Visão geral 


<div class="mw-translate-fuzzy">

Nas distribuições recentes do Linux, o FreeCAD é geralmente fácil de construir, já que todas as dependências são geralmente fornecidas pelo gerenciador de pacotes. Envolve basicamente 3 etapas:

1.  Obtendo o código fonte do FreeCAD
2.  Obtendo as dependências ou pacotes dos quais o FreeCAD depende
3.  Configure com `cmake` e compile com `make`


</div>

Abaixo, você encontrará explicações detalhadas de todo o processo, alguns [build scripts](#Automatic_build_scripts.md) e particularidades que você pode encontrar. Se você encontrar algo errado ou desatualizado no texto abaixo (as distribuições Linux mudam frequentemente), ou se você usa uma distribuição que não está listada, discuta o assunto em [fórum](https://forum.freecadweb.org/index.php), e ajude-nos a corrigi-lo.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">



*Fluxo de trabalho geral para compilar o FreeCAD a partir do código-fonte. As dependências de terceiros devem estar no sistema, assim como o próprio código-fonte do FreeCAD. CMake configura o sistema para que com uma única instrução make todo o projeto seja compilado.*



## Obtendo a fonte 

### Git

A melhor maneira de obter o código é clonar o repositório Git somente leitura [Git](https://github.com/FreeCAD/FreeCAD). Para isso você precisa do programa `git` que pode ser facilmente instalado na maioria das distribuições Linux. Também pode ser obtido no [site oficial](http://git-scm.com/).

O Git pode ser instalado através do seguinte comando:


{{Code|lang=bash|code=
sudo apt install git
}}

O comando a seguir colocará uma cópia da versão mais recente do código-fonte do FreeCAD em um novo diretório chamado `freecad-source`.


{{Code|lang=bash|code=
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

Para obter mais informações sobre como usar o Git e contribuir com código para o projeto, consulte [Gerenciamento de código-fonte](Source_code_management/pt-br.md).



## Obtendo as dependências 

Para compilar o FreeCAD você deve instalar as dependências necessárias mencionadas em [Bibliotecas de Terceiros](Bibliotecas_de_Terceiros.md); os pacotes que contêm essas dependências estão listados abaixo para diferentes distribuições Linux. Observe que os nomes e a disponibilidade das bibliotecas dependerão da sua distribuição específica; se sua distribuição for antiga, alguns pacotes podem estar indisponíveis ou ter um nome diferente. Neste caso, consulte a seção [distribuições mais antigas e não convencionais](#Older_and_non-conventional_distributions.md) abaixo.

Depois de instalar todas as dependências, prossiga para [compilar o FreeCAD](#Compile_FreeCAD.md)

Observe que o código-fonte do FreeCAD tem cerca de 500 MB; pode ser três vezes maior se você clonar o repositório Git com todo o seu histórico de modificações. Obter todas as dependências pode exigir o download de 500 MB ou mais de novos arquivos; quando esses arquivos são descompactados, eles podem exigir 1.500 MB ou mais de espaço. Esteja ciente também de que o processo de compilação pode gerar até 1.500 MB de arquivos adicionais à medida que o sistema copia e modifica todo o código-fonte. Portanto, certifique-se de ter espaço livre suficiente no disco rígido, pelo menos 4 GB, ao tentar compilar.


<div class="mw-collapsible mw-collapsed toccolours">



### Debian e Ubuntu 


<div class="mw-collapsible-content">

Em sistemas baseados no Debian (Debian, Ubuntu, Mint, etc.), é muito fácil instalar todas as dependências necessárias. A maioria das bibliotecas está disponível por meio do `apt` ou do gerenciador de pacotes Synaptic.

Se você já instalou o FreeCAD a partir dos repositórios oficiais, poderá instalar suas dependências de compilação com esta única linha de código em um terminal:


```python
sudo apt build-dep freecad
```

Alternativamente, substitua `freecad` por `freecad-daily` para instalar as dependências de construção para o branch de desenvolvimento principal. Você precisará ter os [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pt-br#Development_PPA_(Daily).md) adicionados às suas fontes de software.

Porém, se a versão do FreeCAD nos repositórios for antiga, as dependências podem ser erradas para compilar uma versão recente do FreeCAD. Portanto, verifique se você instalou os seguintes pacotes.

Esses pacotes são essenciais para o sucesso de qualquer tipo de compilação:

-    `build-essential`, instala os compiladores C e C++, as bibliotecas de desenvolvimento C e o programa `make`.

-    `cmake`, ferramenta essencial para configurar a fonte do FreeCAD. Você também pode instalar `cmake-gui` e `cmake-curses-gui` para uma opção gráfica.

-    `libtool`, ferramentas essenciais para produzir bibliotecas compartilhadas.

-    `lsb-release`, o utilitário de relatório base padrão normalmente já está instalado em um sistema Debian e permite distinguir programaticamente entre uma instalação Debian pura ou uma variante, como Ubuntu ou Linux Mint. Não remova este pacote, pois muitos outros pacotes do sistema podem depender dele.

A compilação do FreeCAD usa a linguagem Python e também é usada em tempo de execução como linguagem de script. Se você estiver usando uma distribuição baseada em Debian, o interpretador Python normalmente já está instalado.

-    `python3`
    

-    `swig`, a ferramenta que cria interfaces entre o código C++ e Python.

Verifique se você tem o Python 3 instalado. Python 2 ficou obsoleto em 2019, portanto, novos desenvolvimentos no FreeCAD não são testados com esta versão da linguagem.

As bibliotecas Boost precisam ser instaladas:

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

As bibliotecas Coin precisam ser instaladas:

-    `libcoin80-dev`, para Debian Jessie, Stretch, Ubuntu 16.04 a 18.10, ou

-    `libcoin-dev`, para Debian Buster, Ubuntu 19.04 e mais recente, bem como para Ubuntu 18.04/18.10 com os [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pt-br#Development_PPA_(Daily).md) adicionados para suas fontes de software.

Diversas bibliotecas que tratam de matemática, superfícies trianguladas, classificação, malhas, visão computacional, projeções cartográficas, visualização 3D, sistema X11 Window, análise XML e leitura de arquivos Zip:

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk9-dev`, `libvtk8-dev`, `libvtk7-dev` or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libyaml-cpp-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



#### Python 2 e Qt4 

Isso não é recomendado para instalações mais recentes, pois tanto o Python 2 quanto o Qt4 são obsoletos. A partir da versão 0.20, o FreeCAD não os suporta mais.


<div class="mw-collapsible-content">

Para compilar o FreeCAD para Debian Jessie, Stretch, Ubuntu 16.04, usando Python 2 e Qt4, instale as seguintes dependências.

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>



#### Python 3 e Qt5 

Para compilar o FreeCAD para Debian Buster, Ubuntu 19.04 e mais recente, bem como Ubuntu 18.04/18.10 com os [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pt-br#Development_PPA_(Daily).md) adicionados às suas fontes de software, instale a seguinte dependência

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `qtwebengine5-dev`
    

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-packaging`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2.qtnetwork`
    

-    `python3-pyside2.qtwebengine`
    

-    `python3-pyside2.qtwebenginecore`
    

-    `python3-pyside2.qtwebenginewidgets`
    

-    `python3-pyside2.qtwebchannel`
    

-    `python3-pyside2uic`(not required on Ubuntu 20.04 and later)



#### Kernel OpenCascade 

O kernel OpenCascade é a principal biblioteca gráfica para criar formas 3D. Existe em uma versão oficial OCCT e em uma versão comunitária OCE. A versão comunitária não é mais recomendada, pois está desatualizada.

Para Debian Buster e Ubuntu 18.10 e mais recentes, bem como Ubuntu 18.04 com os [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pt-br#Development_PPA_(Daily).md) adicionados às suas fontes de software, instale os pacotes oficiais.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

Para Debian Jessie, Stretch, Ubuntu 16.04 e mais recente, instale os pacotes da edição comunitária.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

Você pode instalar as bibliotecas individualmente ou usando a expansão Asterisk. Troque `occ` por `oce` se desejar instalar as bibliotecas da comunidade.


```python
sudo apt install libocct*-dev
```



#### Pacotes opcionais 

Opcionalmente, você também pode instalar estes pacotes extras:

-    `libsimage-dev`, para fazer com que o Coin suporte formatos de arquivo de imagem adicionais.

-    `doxygen`e `libcoin-doc` (ou `libcoin80-doc` para sistemas mais antigos), se você pretende gerar documentação de código-fonte.

-    `libspnav-dev`, para suporte a [dispositivos de entrada 3D](dispositivos_de_entrada_3D.md), como o 3Dconnexion \"Space Navigator\" ou \"Space Pilot\".

-    `checkinstall`, se você pretende registrar seus arquivos instalados no gerenciador de pacotes do seu sistema, para poder desinstalá-lo mais tarde.



#### Comando único para Python 3 e Qt5 

Requer Pyside2 disponível no Debian buster e nos [freecad-stable/freecad-daily PPAs](Installing_on_Linux/pt-br#Official_Ubuntu_repository.md).


{{Code|lang=bash|code=
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev qtwebengine5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-packaging python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig libyaml-cpp-dev
}}

NOTA: Em algumas versões do Ubuntu e algumas versões do Qt, você receberá um erro informando que python3-pyside2uic não pode ser encontrado - nesses sistemas você pode omiti-lo com segurança. No Ubuntu 20.04 você precisará adicionar `pyqt5-dev-tools`. Mais informações podem ser encontradas em [este fórum de discussão](https://forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">



#### Comando único para Python 2 e Qt4 

Isso não é recomendado para instalações mais recentes, pois tanto o Python 2 quanto o Qt4 são obsoletos.


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
}}

Usuários do Ubuntu 16.04, consulte também a discussão sobre compilação no fórum: [Compilar no Linux (Kubuntu): CMake não consegue encontrar VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Follow the same steps as in Debian and Ubuntu.

There are problems reported when trying to compile in Raspberry PI OS 32-bit with Python 3 and Qt5, but the combination Python 3 and Qt4 seems to work for older versions of FreeCAD (with minor issues).

For newer versions of FreeCAD (\>= 0.20) the compilation with Py3/Qt5 is successful if the operating system installed is Raspberry Pi OS 64-bit or Ubuntu 20.04.

Due to different issues with Qt, in Ubuntu 20.04 the normal PySide tools won\'t be found. {{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

In this case, we can install the packages from PyQt and create symbolic links to the needed tools. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Now compilation may proceed. {{Code|lang=bash|code=
cd build/
cmake ../ -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

The `-j` option to `make` should not be more than 3 because the Raspberry Pi has limited memory. It will take several hours to compile, so it is better to do it overnight.

More information, [FreeCAD and Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

There is a bug in cmake distributed by Fedora 34/35 which results in cmake failing to find the opencascade libraries. This can easily be fixed by making one minor change to the top level cmake file of opencascade installed on Fedora. Details here: <https://bugzilla.redhat.com/show_bug.cgi?id=2083568>.

Near the top of the file **OpenCASCADEConfig.cmake**, change the following line to use {{Incode|REAL_PATH()}}. This fixes a bug introduced by the use of a symlink from {{Incode|/lib}} to {{Incode|/usr/lib}} of Fedora, which causes cmake to fail.

This file is usually installed in **/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake**.


{{Code|lang=bash|code=
get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
}}

change this to:


{{Code|lang=bash|code=
file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
}}

This trivial change needs to be made inside the build directory once cmake has been run and failed. Re-running cmake will then correctly detect the OCCT libraries in the normal way.

#### Fedora38/39

Now install Python 3.11. This includes a notable change in how Python initializes when running a program. As a result FreeCAD fails to find OpenCamLib, meaning [3D Surface](CAM_Surface.md) and [Waterline](CAM_Waterline.md) are not available in the [CAM Workbench](CAM_Workbench.md). This was fixed in the master branch on 20th Mar 2024 ([Pull request #13059](https://github.com/FreeCAD/FreeCAD/pull/13059)).

You need the following packages:

-    {{Incode|gcc-c++}}(or possibly another C++ compiler?)

-    {{Incode|cmake}}
    

-    {{Incode|doxygen}}
    

-    {{Incode|swig}}
    

-    {{Incode|gettext}}
    

-    {{Incode|dos2unix}}
    

-    {{Incode|desktop-file-utils}}
    

-    {{Incode|libXmu-devel}}
    

-    {{Incode|freeimage-devel}}
    

-    {{Incode|mesa-libGLU-devel}}
    

-    {{Incode|opencascade-devel}}
    

-    {{Incode|openmpi-devel}}
    

-    {{Incode|python3}}
    

-    {{Incode|python3-devel}}
    

-    {{Incode|python3-pyside2}}
    

-    {{Incode|python3-pyside2-devel}}
    

-    {{Incode|pyside2-tools}}
    

-    {{Incode|boost-devel}}
    

-    {{Incode|tbb-devel}}
    

-    {{Incode|eigen3-devel}}
    

-    {{Incode|qt-devel}}
    

-    {{Incode|qt5-qtwebengine-devel}}
    

-    {{Incode|qt5-qtxmlpatterns}}
    

-    {{Incode|qt5-qtxmlpatterns-devel}}
    

-    {{Incode|qt5-qtsvg-devel}}
    

-    {{Incode|qt5-qttools-static}}
    

-    {{Incode|ode-devel}}
    

-    {{Incode|xerces-c}}
    

-    {{Incode|xerces-c-devel}}
    

-    {{Incode|opencv-devel}}
    

-    {{Incode|smesh-devel}}
    

-    {{Incode|Coin3}}
    

-    {{Incode|Coin3-devel}}
    

-    {{Incode|yaml-cpp}}
    

(April 2021, Coin4 and Coin4-devel are available) (if coin2 is the latest available for your version of Fedora, use packages from <http://www.zultron.com/rpm-repo/>)

-    {{Incode|SoQt-devel}}
    

-    {{Incode|freetype}}
    

-    {{Incode|freetype-devel}}
    

-    {{Incode|vtk}}
    

-    {{Incode|vtk-devel}}
    

-    {{Incode|med}}
    

-    {{Incode|med-devel}}
    

And optionally:

-    {{Incode|libspnav-devel}}(for 3Dconnexion devices support like the Space Navigator or Space Pilot)

-    {{Incode|python3-pivy}}(https://bugzilla.redhat.com/show_bug.cgi?id=458975 Pivy is not mandatory but needed for the Draft Workbench)

-    {{Incode|python3-markdown}}(for the Addon Manager to display native markdown)

-    {{Incode|python3-GitPython}}(for the Addon Manager to use git to checkout and update workbenches and macros)

To install all dependencies at once (tested on fedora 36 and 37):


{{Code|lang=bash|code=
sudo dnf install gcc-c++ cmake doxygen swig gettext dos2unix desktop-file-utils libXmu-devel freeimage-devel mesa-libGLU-devel opencascade-devel openmpi-devel python3 python3-devel python3-pyside2 python3-pyside2-devel pyside2-tools boost-devel tbb-devel eigen3-devel qt-devel qt5-qtwebengine-devel qt5-qtxmlpatterns qt5-qtxmlpatterns-devel qt5-qtsvg-devel qt5-qttools-static ode-devel xerces-c xerces-c-devel opencv-devel smesh-devel Coin3 Coin3-devel SoQt-devel freetype freetype-devel vtk vtk-devel med med-devel libspnav-devel python3-pivy python3-markdown python3-GitPython yaml-cpp
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Easiest way to check which packages are needed to compile FreeCAD is to check via portage:

emerge -pv freecad

This should give a nice list of extra packages that you need installed on your system.

If FreeCAD is not available on portage, it is available on the [waebbl overlay](https://github.com/waebbl/waebbl-gentoo). The issue tracker on the waebbl overlay Github may help guide through some issues you may come across. The overlay provides freecad-9999, which you can choose to compile, or simply use to get the dependencies.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

The following commands will install the packages required for building FreeCAD with Qt5 and Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel yaml-cpp
```

The following command will install Qt Creator and the GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

If any packages are missing, then you can check the Tumbleweed [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD).

Also, check to see if there are any patches you need to apply (such as [0001-find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

If there is a difference between the available packages on Tumbleweed and Leap, then you can read the Leap [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https://build.opensuse.org/) to determine the required packages.

See [piano_jonas unofficial \"Compile On openSUSE\" guide](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

Você precisará das seguintes bibliotecas dos repositórios oficiais:

-    `boost`
    

-    `cmake`
    

-    `coin`
    

-    `curl`
    

-    `desktop-file-utils`
    

-    `eigen`
    

-    `gcc-fortran`
    

-    `git`
    

-    `glew`
    

-    `hicolor-icon-theme`
    

-    `jsoncpp`
    

-    `libspnav`
    

-    `med`
    

-    `nlohmann-json`
    

-    `opencascade`
    

-    `pyside2-tools`
    

-    `pyside2`
    

-    `python-matplotlib`
    

-    `python-netcdf4`
    

-    `python-packaging`
    

-    `python-pivy`
    

-    `qt5-svg`
    

-    `qt5-tools`
    

-    `qt5-webengine`
    

-    `shared-mime-info`
    

-    `shiboken2`
    

-    `swig`
    

-    `utf8cpp`
    

-    `verdict`
    

-    `xerces-c`
    

-    `yaml-cpp`
    


```python
sudo pacman -S --needed --asdeps boost cmake coin curl desktop-file-utils eigen gcc-fortran git glew hicolor-icon-theme jsoncpp libspnav med nlohmann-json opencascade python-matplotlib python-netcdf4 python-packaging python-pivy qt5-svg qt5-tools qt5-webengine shared-mime-info swig utf8cpp xerces-c yaml-cpp 
```

FreeCAD currently uses QT5. This requires packages which have been moved from the official repositories to the AUR. These packages will be compiled by source and may take a long time depending on the available hardware.


```python
yay -S --needed --asdeps pyside2 pyside2-tools shiboken2
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Distribuições mais antigas e não convencionais 


<div class="mw-collapsible-content">

Em outras distribuições, temos muito poucos comentários dos usuários, portanto, pode ser mais difícil encontrar os pacotes necessários.

Tente primeiro localizar as bibliotecas necessárias mencionadas em [bibliotecas de terceiros](Third_Party_Libraries/pt-br.md) em seu gerenciador de pacotes. Cuidado, pois alguns deles podem ter um nome de pacote ligeiramente diferente; procure por `name`, mas também `libname`, `name-dev`, `name-devel` e similares. Se isso não for possível, tente compilar você mesmo essas bibliotecas.

O FreeCAD requer a versão do compilador GNU g++ igual ou superior a 3.0.0, já que o FreeCAD é escrito principalmente em C++. Durante a compilação alguns scripts Python são executados, portanto o interpretador Python deve funcionar corretamente. Para evitar problemas de vinculador, também é uma boa ideia ter os caminhos da biblioteca na variável `LD_LIBRARY_PATH` ou no arquivo `ld.so.conf`. Isso já é feito em distribuições Linux modernas, mas pode precisar ser configurado em distribuições mais antigas.


</div>


</div>

### Pivy


<div class="mw-translate-fuzzy">

[Pivy](Pivy/pt-br.md) (wrappers Python para Coin3d) não é necessário para construir o FreeCAD ou para iniciá-lo, mas é necessário como uma dependência de tempo de execução pela [bancadas de trabalho Draft](Draft_Workbench/pt-br.md). Se você não for usar este ambiente de trabalho, não precisará do Pivy. No entanto, observe que o Draft Workbench é usado internamente por outras bancadas de trabalho, como [Arch](Arch_Workbench/pt-br.md) e [BIM](BIM_Workbench/pt-br.md), então o Pivy precisa ser instalado para usar essas bancadas de trabalho também.


</div>

Em novembro de 2015, a versão obsoleta do Pivy incluída no código-fonte do FreeCAD não será mais compilada em muitos sistemas. Isso não é um grande problema, pois normalmente você deve obter o Pivy no gerenciador de pacotes da sua distribuição; se você não conseguir encontrar o Pivy, talvez seja necessário compilá-lo sozinho, consulte [Instruções de compilação do Pivy](Extra_python_modules/pt-br#Pivy.md).



### Símbolos de depuração 

Para solucionar falhas no FreeCAD, é útil ter os símbolos de depuração de bibliotecas de dependência importantes, como o Qt. Para isso, tente instalar os pacotes de dependência que terminam com `-dbg`, `-dbgsym`, `-debuginfo` ou similar, dependendo da sua distribuição Linux.

Para Ubuntu, pode ser necessário habilitar repositórios especiais para poder ver e instalar esses pacotes de depuração com o gerenciador de pacotes. Consulte [Pacotes de símbolos de depuração](https://wiki.ubuntu.com/Debug_Symbol_Packages) para obter mais informações.



## Compilar FreeCAD 


**Construir o FreeCAD 0.20 requer pelo menos Python3.6 e Qt 5.9.**

O FreeCAD usa o CMake como seu principal sistema de compilação, pois ele está disponível em todos os principais sistemas operacionais. A compilação com o CMake é geralmente muito simples e ocorre em duas etapas.

1.  O CMake verifica se todos os programas e bibliotecas necessários estão presentes em seu sistema e gera um `Makefile` que é configurado para a segunda etapa. O FreeCAD tem várias opções de configuração para escolher, mas ele vem com padrões sensatos. Algumas alternativas estão detalhadas abaixo.
2.  A compilação em si, que é feita com o programa `make`, que gera os executáveis do FreeCAD.

Como o FreeCAD é um aplicativo grande, a compilação de todo o código-fonte pode levar de 10 minutos a uma hora, dependendo da sua CPU e do número de núcleos de CPU usados para a compilação.



### Construção

Para compilar, basta criar um diretório de compilação, `build`. Em seguida, a partir desse diretório de compilação, aponte `cmake` para a pasta de código-fonte correta. Você também pode usar `cmake-gui` ou `ccmake` em vez de `cmake` nas instruções abaixo. Quando `cmake` terminar de configurar o ambiente, use `make` para iniciar a compilação.


{{Code|lang=bash|code=
# from your freecad-source folder:
mkdir build
cd build
cmake ../
make -j$(nproc --ignore=2)
}}

A opção `-j` do `make` controla quantos trabalhos (arquivos) são compilados em paralelo. O programa `nproc` imprime o número de núcleos de CPU em seu sistema; ao usá-lo juntamente com a opção `-j`, você pode optar por processar tantos arquivos quantos forem os núcleos existentes, a fim de acelerar a compilação geral do programa. No exemplo acima, ele usará todos os núcleos do sistema, exceto dois; isso manterá o computador responsivo para outros usos enquanto a compilação é feita em segundo plano. O executável do FreeCAD será exibido no diretório `build/bin`. Consulte também [Compilação (Acelerada)](Compiling_(Speeding_up)/pt-br.md) para melhorar a velocidade de compilação.



### Resolvendo problemas do cmake 

Se você já fez uma compilação antes e ficou preso em uma dependência que não é reconhecida ou que parece não poder ser resolvida, tente o seguinte:

-   Exclua o conteúdo do diretório de compilação antes de executar o cmake novamente. O FreeCAD é um alvo que se move rapidamente e você pode estar tropeçando em informações do cmake armazenadas em cache que apontam para uma versão mais antiga do que o novo repositório pode usar. Limpar o cache pode permitir que o cmake se recupere e reconheça a versão de que você realmente precisa.

-   Se o cmake reclamar da falta de um arquivo específico, use uma ferramenta como o \"apt-file search\", ou seu equivalente em outros sistemas de pacotes, para descobrir a qual pacote esse arquivo pertence e instalá-lo. Lembre-se de que é provável que você precise da versão -dev do pacote que contém arquivos de cabeçalho ou de configuração necessários para que o FreeCAD use o pacote.



### Compilando contra GNU libc 2.34 e posterior 

A GNU libc 2.34 introduz uma alteração na biblioteca que pode fazer com que as compilações em alguns sistemas Linux falhem com um erro do tipo:


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

Para resolver isso, um link simbólico deve ser criado manualmente a partir do libdl.so.\* instalado no sistema (agora vazio) para o local em que o compilador diz que está procurando o arquivo. Por exemplo (se a cópia atual instalada do libdl.so em seu sistema for /usr/lib/x86_64-linux-gnu/libdl.so.2):


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Adapte o comando à estrutura do seu sistema procurando por libdl.so\* e vinculando-o ao local apropriado.



### Como reparar seu diretório de código-fonte 

Se você executou acidentalmente uma compilação dentro do diretório do código-fonte ou adicionou arquivos estranhos e deseja restaurar o conteúdo apenas para o código-fonte original, execute as etapas a seguir.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

A primeira linha limpa o arquivo `.gitignore`. Isso garante que os comandos clean e reset a seguir afetarão tudo no diretório e não ignorarão os itens que correspondem às expressões em `.gitignore`. A segunda linha exclui todos os arquivos e diretórios que não são rastreados pelo repositório git; em seguida, o último comando redefinirá todas as alterações nos arquivos rastreados, incluindo o primeiro comando que limpou o arquivo `.gitignore`.

Se você não limpar o diretório de origem, as execuções subsequentes de `cmake` poderão não capturar novas opções para o sistema se o código for alterado.



### Configuração

Ao passar diferentes opções para `cmake`, você pode alterar a forma como o FreeCAD é compilado. A sintaxe é a seguinte.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Onde `$SOURCE_DIR` é o diretório que contém o código-fonte. O `<type>` pode ser omitido na maioria dos casos. O espaço após a opção `D` também pode ser omitido.

Por exemplo, para evitar a criação do [Bancada de trabalho FEM](FEM_Workbench/pt-br.md):


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../
cmake -DBUILD_FEM=OFF ../
}}

Todas as variáveis possíveis estão listadas no arquivo `InitializeFreeCADBuildOptions.cmake`, localizado no diretório `cMake/FreeCAD_Helpers`. Nesse arquivo, procure a palavra `option` para acessar as variáveis que podem ser definidas e ver seus valores padrão.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Como alternativa, use o comando `cmake -LH` para listar a configuração atual e, portanto, todas as variáveis que podem ser alteradas. Você também pode instalar e usar `cmake-gui` para iniciar uma interface gráfica que mostre todas as variáveis que podem ser modificadas. Nas próximas seções, listamos algumas das opções mais relevantes que você pode querer usar.



#### Para uma compilação de depuração 

Crie uma compilação `Debug` para solucionar falhas no FreeCAD. Tenha em atenção que com esta construção o [Sketcher](Sketcher_Workbench/pt-br.md) fica muito lento com esboços complexos.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../
}}



#### Para uma compilação de versão 

Crie uma compilação `Release` para testar o código que não trava. Uma compilação `Release` será executada muito mais rapidamente do que uma compilação `Debug`.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../
}}



#### Compilação com Python 3 e Qt5 

O suporte ao Python 2 e ao Qt4 foi removido no FreeCAD 0.20 e não é necessário habilitar explicitamente o Qt5 e o Python 3 se estiver compilando as versões mais recentes. O suporte ao Qt6 está em desenvolvimento e ainda não funciona. A menos que planeje ajudar no esforço de migração para o Qt6, FREECAD_QT_VERSION deve ser deixado em \"Auto\" (o padrão) ou explicitamente definido como \"5\".

Para 0.20 e 0.21_dev: {{Code|lang=bash|code=
cmake ../
}}

Observe que, ao alternar entre as compilações 0.20 e 0.21_dev, pode ser necessário excluir o CMakeCache.txt antes de executar o cmake.



#### Compilação para uma versão específica do Python 

Se o executável `python` padrão em seu sistema for um link simbólico para Python 2, `cmake` tentará configurar o FreeCAD para esta versão. Você deve então escolher outra versão do Python, fornecendo o caminho para um executável específico:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../
}}

Se isso não funcionar, talvez seja necessário definir variáveis ​​adicionais apontando para as bibliotecas Python desejadas e incluir diretórios:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../
}}

É possível ter várias versões independentes do Python no mesmo sistema, portanto, os locais e os números de versão dos seus arquivos Python dependerão da sua distribuição Linux específica. Use `python3 -V` para exibir a versão do Python que você está usando atualmente; apenas os dois primeiros números são necessários; por exemplo, se o resultado for `Python 3.6.8`, você precisará especificar os diretórios relacionados à versão 3.6. Se você não conhece os diretórios corretos, tente procurá-los com o comando `locate`.


```python
locate python3.6
```

Você pode usar `python3 -m site` em um terminal para determinar o diretório `site-packages`, ou `dist-packages` para sistemas Debian.

Alguns componentes do FreeCAD, como o PySide, tentam detectar automaticamente a versão mais recente do Python instalada em seu sistema, o que pode falhar se ela for diferente da que você inseriu acima. Adicionar a seguinte opção do cMake pode resolver o problema:


{{Code|lang=bash|code=
-DPython3_FIND_STRATEGY=LOCATION
}}



#### Compilação com o Qt Creator em Python 3 e Qt5 

1\. Inicie o Qt Creator.

2\. Clique em **Abrir Projeto**.

3\. Navegue até o diretório onde está o código-fonte, `freecad-source/`, e escolha o arquivo `CMakeLists.txt` mais alto.

4\. Ao selecionar o arquivo, ele executará automaticamente `cmake` nele, mas poderá falhar se as opções apropriadas não estiverem definidas corretamente.

5\. Vá para **Projetos → Construir e Executar → Kit Importado → Construir → Configurações de Construção → CMake**. Defina o diretório de compilação apropriado, `build/`.

6\. Defina as variáveis ​​apropriadas na caixa de diálogo Key-Value, dos tipos `String` e `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
```

7\. Caso as variáveis ​​não carreguem o projeto corretamente, talvez seja necessário ir em **Projetos → Gerenciar Kits → Kits → Padrão (ou Kit Importado ou similar) → Configuração do CMake**. Em seguida, pressione **Change** e adicione a configuração apropriada conforme descrito acima. Talvez seja necessário adicionar mais variáveis ​​sobre os caminhos do Python, se o sistema Python não for encontrado. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
```

7.1. Pressione **Aplicar** e depois **OK**.

7.2. Certifique-se de que o resto das opções estejam definidas corretamente, por exemplo, **Qt version** deve ser uma versão atual instalada no sistema, como `Qt 5.9.5 in PATH (qt5)`.

Pressione **Apply** e depois **OK** para fechar a configuração.

O programa `cmake` deverá ser executado automaticamente novamente e deverá preencher toda a caixa de diálogo Key-Value com todas as variáveis ​​que podem ser configuradas.

8\. Vá para **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** e escolha `FreeCADMain` para compilar a versão gráfica do FreeCAD, ou ` FreeCADMainCMD` para compilar apenas a versão da linha de comando.

9\. Por fim, vá ao menu **Build → Build Project "FreeCAD"**. Se esta for uma nova compilação, deverá levar vários minutos, inclusive horas, dependendo do número de processadores disponíveis.



#### Plugin do designer Qt 

Se você deseja desenvolver código Qt para FreeCAD, você precisará do plugin Qt Designer que fornece todos os widgets personalizados do FreeCAD.

Entre em um diretório auxiliar do código fonte e execute `qmake` com o arquivo de projeto indicado para criar um `Makefile`; então execute `make` para compilar o plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Se você estiver compilando para Qt5, certifique-se de que o binário `qmake` seja o desta versão, para que o `Makefile` resultante contenha as informações necessárias para Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

onde `$QT_DIR` é o diretório que armazena bibliotecas binárias Qt, por exemplo, `/usr/lib/x86_64-linux-gnu/qt5`.

A biblioteca criada é `libFreeCAD_widgets.so`, que precisa ser copiada para `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}



#### Pivy externo ou interno 

Anteriormente, uma versão do Pivy era incluída no código-fonte do FreeCAD (interno). Se você quisesse usar a cópia do Pivy do seu sistema (externa), você precisava usar -DFREECAD_USE_EXTERNAL_PIVY=1.

O uso do Pivy externo tornou-se o padrão durante o desenvolvimento do FreeCAD 0.16, portanto, essa opção não precisa mais ser definida manualmente.



#### Documentação do Doxygen 

Se você tiver o Doxygen instalado, poderá criar a documentação do código-fonte. Consulte [documentação fonte](source_documentation/pt-br.md) para obter instruções.



### Documentação adicional 

O código-fonte do FreeCAD é muito extenso e, com o CMake, é possível configurar muitas opções. Aprender a usar o CMake por completo pode ser útil para escolher as opções certas para suas necessidades específicas.

-   [Documentação de referência do CMake](https://cmake.org/documentation/) da Kitware.
-   [How to Build a CMake-Based Project](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) por Preshing sobre programação.
-   [Aprenda a linguagem de script do CMake em 15 minutos](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) by Preshing on programming.



### Criando um pacote debian 

Se você planeja construir um pacote Debian a partir dos fontes, você precisa instalar alguns pacotes primeiro:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Vá para o diretório FreeCAD e chame


{{Code|lang=bash|code=
debuild
}}

Depois que o pacote for compilado, você pode usar `lintian` para verificar se o pacote contém erros


{{Code|lang=bash|code=
lintian freecad-package.deb
}}



#### pacote \*.deb com checkinstall 

O script Debian `checkinstall` permite criar um pacote \*.deb que pode ser instalado e removido com os comandos padrão `dpkg`. Pode ser necessário instalá-lo primeiro (no Ubuntu, use `sudo apt install checkinstall`). É interativo e solicita as informações necessárias, fornecendo padrões úteis. Durante o processo o pacote é instalado e um arquivo \*.deb e um arquivo de backup são criados.

É uma boa ideia definir um nome e uma breve descrição para o pacote. O nome deve ser digitado para desinstalá-lo novamente e a descrição será listada por `dpkg -l`. O nome padrão \"build\" não é muito informativo.

Exemplo:


{{Code|lang=bash|code=
cd freecad-source/build
cmake ..
make
sudo checkinstall                                  # e.g. name=freecad-test1
}}

O resultado é um arquivo \*.deb na pasta build. `checkinstall` instalará a compilação por padrão. É assim que você pode instalá-lo ou desinstalá-lo:


{{Code|lang=bash|code=
cd freecad-source/build
ls <nowiki>|</nowiki> grep freecad
        freecad-test1_20220814-1_amd64.deb
sudo dpkg -i freecad-test1_20220814-1_amd64.deb   # install
dkpg -l <nowiki>|</nowiki> grep freecad                            # find by name
sudo dpkg -r freecad-test1                        # uninstall by name
}}



## Atualizando o código-fonte 

O sistema CMake permite que você atualize o código-fonte de forma inteligente e recompile apenas o que foi alterado, tornando as compilações subsequentes mais rápidas.

Vá até o local onde o código-fonte do FreeCAD foi baixado pela primeira vez e extraia o novo código:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Em seguida, vá para o diretório de compilação onde o código foi compilado inicialmente e execute `cmake` especificando o diretório atual (indicado por um ponto); depois, acione a recompilação com `make`.


{{Code|lang=bash|code=
cd build
cmake ../
make -j$(nproc --ignore=2)
}}



## Desinstalação do código-fonte 

Caso o código-fonte compilado tenha sido instalado com `sudo make install` (para Debian), os arquivos foram copiados para a pasta **/usr/local** em várias subpastas. Para a desinstalação, o arquivo **install_manifest.txt** pode ser usado. Ele foi criado na pasta de compilação durante a compilação e contém todos os arquivos instalados. Enquanto esse arquivo existir, a instalação poderá ser desinstalada.


{{Code|lang=bash|code=
cd freecad-source/build
xargs sudo rm < install_manifest.txt
}}



## Solução de problemas 



### Para sistemas de 64 bits 

Ao compilar o FreeCAD para 64 bits, há um problema conhecido com o pacote OpenCASCADE (OCCT) de 64 bits. Para que o FreeCAD seja executado corretamente, talvez seja necessário executar o script `configure` e definir `CXXFLAGS` adicionais:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Para sistemas baseados no Debian, essa opção não é necessária quando se usa os pacotes OpenCASCADE pré-construídos, pois eles definem internamente o `CXXFLAGS` adequado.



## Scripts de compilação automática 

Aqui está tudo o que você precisa para uma compilação completa do FreeCAD. É uma abordagem de script único e funciona em uma distribuição Linux recém-instalada. Os comandos solicitarão a senha de root para a instalação de pacotes e novos repositórios on-line. Esses scripts devem ser executados em versões de 32 e 64 bits. Eles foram escritos para diferentes versões, mas também podem ser executados em uma versão posterior, com ou sem grandes alterações.

Se você tiver um script desse tipo para sua distribuição preferida, discuta-o no [FreeCAD forum](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) para que possamos incorporá-lo.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Esses scripts fornecem uma maneira confiável de instalar o conjunto correto de dependências necessárias para compilar e executar o FreeCAD no Ubuntu. Eles usam os arquivos de pacotes pessoais do Ubuntu (PPA) e devem funcionar em qualquer versão do Ubuntu visada pelo PPA. O [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) PPA tem como alvo as versões recentes do Ubuntu, enquanto o [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA tem como alvo as versões oficialmente suportadas do Ubuntu.

Esse script instala o snapshot compilado diariamente do FreeCAD e suas dependências. Ele adiciona o repositório diário, obtém as dependências para compilar essa versão e instala os pacotes necessários. Em seguida, ele extrai o código-fonte para um diretório específico, cria um diretório de compilação e faz alterações nele, configura o ambiente de compilação com `cmake` e, por fim, compila o programa inteiro com `make`. Salve o script em um arquivo, torne-o executável e execute-o, mas não use `sudo`; os privilégios de superusuário serão solicitados apenas para comandos selecionados.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-source/build
cd freecad-source/build
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../
make -j$(nproc --ignore=2)
}}

Se desejar, você pode desinstalar a versão pré-compilada do FreeCAD (`freecad-daily`) e deixar as dependências no lugar; no entanto, deixar esse pacote instalado permitirá que o gerenciador de pacotes mantenha suas dependências atualizadas também; isso é útil principalmente se você pretende acompanhar o desenvolvimento do FreeCAD e atualizar e compilar constantemente os códigos-fonte do repositório Git.

O script anterior pressupõe que você deseja compilar a versão mais recente do FreeCAD e, portanto, está usando o repositório \"daily\" para obter as dependências. No entanto, em vez disso, você pode obter as dependências de compilação da versão \"estável\" do seu lançamento atual do Ubuntu. Se esse for o caso, substitua a parte superior do script anterior pelas instruções a seguir. Para o Ubuntu 12.04, omita `--enable-source` do comando.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Quando você instalar o pacote `freecad` do repositório `freecad-stable`, ele substituirá o executável do FreeCAD disponível no repositório Universe Ubuntu. O nome do executável será simplesmente `freecad`, e não `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

Nenhum repositório externo é necessário para compilar o FreeCAD. No entanto, existe uma incompatibilidade com python3-devel que precisa ser removida. FreeCAD pode ser compilado a partir do GIT


</div>


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Como você está usando o git, da próxima vez que desejar compilar você não precisa clonar tudo, apenas extraia do git e compile mais uma vez


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Debian Squeeze 


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora 27/28/29 


<div class="mw-collapsible-content">

Postado pelo usuário [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) no fórum.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Arch usando AUR 


<div class="mw-collapsible-content">

O [Arch User Repository (AUR)](https://aur.archlinux.org/) é uma coleção de receitas criadas por usuários para criar pacotes que não são oficialmente suportados pelos mantenedores da distribuição/comunidade. Em geral, elas são seguras. Você pode ver quem mantém o pacote e por quanto tempo o fez. Recomenda-se verificar os arquivos de construção. Também há softwares de código-fonte não aberto disponíveis nessa área, mesmo que sejam mantidos pela empresa proprietária oficial.

Pré-requisito: git

Etapas :

1.  Abra um terminal. Opcionalmente, crie um diretório, por exemplo, {{incode | mkdir git}}. Opcionalmente, altere o diretório, por exemplo, `cd git`.
2.  Clonar o repositório AUR: `git clone https://aur.archlinux.org/freecad-git.git`
3.  Entre na pasta do repositório do AUR : `cd freecad-git`
4.  Compilar usando [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. O sinalizador -s ou \--syncdeps também instalará as dependências necessárias.
5.  Instale o pacote criado: `makepkg --install` ou clique duas vezes no pkgname-pkgver.pkg.tar.xz em seu navegador de arquivos.

Para atualizar o FreeCAD para a versão mais recente, basta repetir a partir da etapa 3. Atualize o repositório AUR quando houver alguma alteração significativa na receita ou novos recursos usando `git checkout -f` dentro da pasta.


</div>


</div>



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/pt-br
