




A maneira mais fácil de instalar o FreeCAD no Windows é correndo o programa de instalação seguinte:


{{DownloadWindowsStable}}

Depois de transferir o ficheiro .msi (instalador da Microsoft), faça duplo-clique para iniciar o processo de instalação.

Em baixo encontra mais informação sobre opções técnicas. Se lhe parecer complicado, não se preocupe! A maioria dos utilizadores Windows não precisam de mais do que o ficheiro de instalação .msi para instalar o FreeCAD e **[ Começar](Getting_started/pt.md)**.

### Instalação simples 

A maneira mais fácil de instalar o **FreeCAD no Windows** é usando o instalador acima. Esta página descreve as funcionalidades do **Instalador Windows** para mais opções de instalação.

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

Se quiser fazer a transferência da versão 64 bits ou a versão de desenvolvimento instável, veja a página dos [Transferências](Download/pt.md).

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Instalação a partir da linha de comandos 

Com a ferramenta da linha de comandos *msiexec.exe* há mais funcionalidades disponíveis, como instalção não-interativa e instalação administrativa.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### Instalação Não-Interativa 

Com a linha de comandos

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

a instalação pode ser iniciada programaticamente. Podem ser passados parâmetros adicionais no fim da linha de comandos, como


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Interfaces limitados 

A quantidade de diálogos que o instalador mostra pode ser controlado com opções /q, em particular:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - Sem interface
-   /qb - Interface básico - mostra apenas um pequeno diálogo indicando o progresso
-   /qb! - Como /qb, mas esconde o botão Cancel
-   /qr - Interface reduzido - mostra todos os diálogos que não requerem interação com o utilizador
-   /qn+ - Como /qn, mas mostra o diálogo \"Completed\" no fim
-   /qb+ - Como /qn, mas mostra o diálogo \"Completed\" no fim


</div>

#### Pasta de destino 

A propriedade TARGETDIR determina a pasta raiz da instalação FreeCAD. Por exemplo, pode ser especificado um disco de instalação diferente com

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

O TARGETDIR por defeito é \[WindowsVolume\\Programm Files\\\]FreeCAD.

#### Instalação para Todos os Utilizadores 

Adicionando

Adding


```python
ALLUSERS=1
```

leva à instalação para todos os utilizadores. Por defeito, a instalação não interativa instala o programa para o utilizador atual, e a instalação interativa oferece um diálogo que seleciona \"todos os utilizadores\" por defeito, se o utilizador atual tiver privilégios suficientes.

#### Seleção de Funcionalidades 

Há um número de propriedades que permitem a seleção das funcionalidades a serem instaladas, reinstaladas, ou removidas. O conjunto de funcionalidades do instalador do FreeCAD é

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - instala o software propriamente dito, mais as bibliotecas base
-   Documentation - instala a documentação
-   SourceCode - instala o código fonte
-   \... a fazer

Adicionalmente, ALL especifica todas as funcionalidades. Todas as funcionalidades dependem da DefaultFeature, instalar qualquer uma das outras implica a instalação desta. As seguintes propriedades controlam as funcionalidades a serem instaladas ou removidas

-   ADDLOCAL - lista de funcionalidades a serem instaladas na máquina local
-   REMOVE - lista de funcionalidades a remover
-   ADDDEFAULT - lista de funcionalidades adicionadas na sua configuração por defeito (que é local para todas as funcionalidades do FreeCAD)
-   REINSTALAR - lista de funcionalidades a reinstalar/reparar
-   ADVERTISE - lista de funcionalidades para as quais se vai fazer uma instalação anunciada

Há algumas propriedades adicionais disponíveis; ver a documentação MSDN para mais detalhes.

Com estas opções, adicionar


```python
ADDLOCAL=Extensions
```

instala o intérprete e regista as extensões, mas não instala mais nada.

### Desinstalação

Com

With


```python
msiexec /x FreeCAD<version>.msi
```

o FreeCAD pode ser desinstalado. Não é necessário ter o ficheiro MSI disponível para a desinstalação; alternativamente, o código do pacote ou produto pode ser especificado. Pode encontrar o código do produto procurando nas propriedades do atalho de desinstalação que o FreeCAD instala no menu Iniciar.

### Instalação Administrativa 

Com

With


```python
msiexec /a FreeCAD<version>.msi
```

pode ser iniciada uma rede de instalação \"administrativa\" (em rede). Os ficheiros são descomprimidos para a pasta de destino (que deve ser uma pasta na rede); não são feitas mais modificações ao sistema local. Adicionalmente, é gerado um outro ficheiro msi (mais pequeno) na pasta de destino, que os clientes podem usar para fazer uma instalação local (versões futuras poderão oferecer a possibilidade de manter algumas funcionalidades na rede).

Neste momento não há interface gráfico para instalações administrativas, por isso a pasta de destino tem de ser indicada na linha de comandos.

Não há um procedimento de desinstalação especifico para uma instalação administrativa - basta apagar a pasta de destino se não houver mais nenhum cliente a usá-la.

### Advertise

Com

With


```python
msiexec /jm FreeCAD<version>.msi
```

seria possível, em principio, \"anunciar\" (advertise) o FreeCAD a uma máquina (com /ju para um utilizador). Isto faria com que os ícones aparecessem no menu Iniciar, e com que as extensões fossem registadas, sem que o programa fosse efetivamente instalado. A primeira utilização de uma funcionalidade faria com que a funcionalidade fosse instalada.

Neste momento o instalador do FreeCAD o anúncio das entradas no menu Iniciar, mas não o de atalhes.

### Instalação Automática num Grupo de Máquinas 

Com o Windows Group Policy, é possível instalar automaticamente o FreeCAD num grupo de máquinas. Para o fazer, siga os seguintes passos:

1.  Fazer login no domain controller
2.  Copie o ficheiro MSI para uma pasta partilhada a que todas as máquinas do grupo tenham destino.
3.  Abrir o snpin MMC \"Active Directory users and computers\"
4.  Navegar até ao grupo de computadores que precisam do FreeCAD
5.  Abrir as Propriedades
6.  Abrir Políticas do Grupo
7.  Adicionar uma nova política, e modifique-a
8.  Em Configuração do Computador/Instalação de Programas, escolher Novo/Pacote
9.  Selecionar o ficheiro MSI a partir da pasta de rede
10. Opcionalmente, selecionar que quer que o FreeCAD seja desinstalado se o computador deixar o âmbito do grupo.

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Normalmente a propagação das politicas de grupo demora algum tempo - para se certificar que o programa é instalado adequadamente, todas as máquinas devem ser reiniciadas.

### Instalação em Linux usando o *Crossover Office* 

Pode instalar a versão de Windows do FreeCAD num sistema Linux usando o *CXOffice 5.0.1*. Corra *msiexec* a partir da linha de comandos do CXOffice, assumindo que o pacote de instalação é colocado na pasta \"programas\" que é mapeada na drive \"Y:\":

.msi

O FreeCAD está a correr, mas ha informação de que a imagem do OpenGL não funciona, tal como os outros programas a correr no [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav/pt|[Lista de funcionalidades](Feature_list/pt.md)|[Install on Unix](Install_on_Unix/pt.md)}}


</div>



