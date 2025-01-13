# Compile on MinGW/pt-br
Este guia percorrerá as etapas necessárias para construir o FreeCAD no Windows usando o ambiente MSYS2/MinGW. A familiaridade básica com os comandos do shell Bash será útil para entender o que cada etapa faz, mas seguir o guia mecanicamente deve resultar em uma construção funcional, mesmo que você não entenda exatamente o que fez para obtê-la.



### Antes de começar 

Baixe e instale [MSYS2](https://www.msys2.org) se ainda não o fez. Ao iniciar o MSYS2, use o tempo de execução \"MSYS2 MinGW 64 bits\", a menos que você saiba o que está fazendo e tenha um motivo específico para não fazê-lo. Se você usar o console UCRT, certifique-se de adaptar sua instalação para usar os pacotes UCRT.

    pacman -Syu

e então relançar e executar

    pacman -Su

antes de proceder.



### Instale ferramentas básicas de desenvolvimento 

Em todas as etapas a seguir, quando solicitado pelo shell do MSYS2, aceite as instalações padrão de tudo pressionando "Enter" quando solicitado.

Primeiro, instale o conjunto de ferramentas mingw-w64 GCC:

    pacman -S --needed base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja

Provavelmente levará vários minutos para ser concluído, pois o conjunto de ferramentas do compilador é bastante grande.

Instale o git:

    pacman -S git

Feche a janela do console atual e reinicie o console MSYS2 MinGW 64 (em uma instalação padrão, isso estará no menu Iniciar na pasta MSYS2).



### Confira as fontes do FreeCAD 

Para obter o código-fonte do FreeCAD, clone-o do repositório git principal:

    git clone https://github.com/FreeCAD/FreeCAD

Se você não quiser compilar o HEAD mais recente, assim que tiver o código-fonte você pode verificar uma tag específica:

    cd FreeCAD
    git checkout tags/1.0 -b releases/FreeCAD-1-0

Ou uma solicitação pull específica (neste exemplo, PR 1234):

    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234

Observe que nem todas as versões podem ser compiladas no MSYS2, várias alterações foram necessárias para habilitá-lo e estas não estavam presentes nas versões 0.19 ou anteriores. Por exemplo, a tag 0.19.3 não será compilável.



### Instale as bibliotecas necessárias 

O FreeCAD depende de muitas bibliotecas de terceiros para sua funcionalidade. Eles podem ser instalados individualmente ou como um único comando unificado.

Agora, instale as seguintes dependências necessárias usando o pacman:

-   mingw-w64-x86_64-opencascade
-   mingw-w64-x86_64-xerces-c
-   mingw-w64-x86_64-qt5
-   mingw-w64-x86_64-med
-   mingw-w64-x86_64-swig
-   mingw-w64-x86_64-qtwebkit
-   mingw-w64-x86_64-coin
-   mingw-w64-x86_64-python-pivy
-   mingw-w64-x86_64-python-ply
-   mingw-w64-x86_64-python-six
-   mingw-w64-x86_64-python-yaml
-   mingw-w64-x86_64-python-numpy
-   mingw-w64-x86_64-python-matplotlib
-   mingw-w64-x86_64-pyside2-qt5
-   mingw-w64-x86_64-python-markdown
-   mingw-w64-x86_64-python-pygit2

A seguir está um único comando para instalar tudo na lista acima:

    pacman -S mingw-w64-x86_64-opencascade mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-markdown mingw-w64-x86_64-python-pygit2



### Construir FreeCAD 

Crie um diretório para a compilação: observe que normalmente não é um subdiretório do diretório de origem (geralmente é útil poder excluir o diretório de origem ou de compilação de forma independente).

    mkdir FreeCAD-build
    cd FreeCAD-build

Execute cMake:

    cmake ../FreeCAD

E finalmente:

    cmake --build ./



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MinGW/pt-br
