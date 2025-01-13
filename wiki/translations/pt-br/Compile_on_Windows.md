# Compile on Windows/pt-br
Esta página explica passo a passo como compilar o FreeCAD 0.19 ou mais recente no Windows usando o compilador MSVC da Microsoft. Para obter informações sobre como usar MSYS2/MinGW, consulte [Compilar no MinGW](Compile_on_MinGW/pt-br.md). Para outras plataformas, consulte [Compilação](Compiling/pt-br.md).



## Pré-requisitos 

Compilar o FreeCAD no Windows requer várias ferramentas e bibliotecas.



### Obrigatório

-   Um compilador. O FreeCAD é testado com o Visual Studio (MSVC) --- outros compiladores podem funcionar, mas as instruções de uso não estão incluídas aqui. Para obter mais detalhes, consulte a seção [Compilador](#Compiler.md) abaixo.

-   [Git](http://git-scm.com/) (Há também frontends de GUI disponíveis para o Git, consulte a próxima seção.)

-   [CMake](https://cmake.org/download/)versão 3.11.x ou mais recente.

*Dica*: Escolher a opção *Adicionar CMake ao PATH do sistema para todos os usuários* ao instalar o CMake tornará o CMake acessível a partir do prompt de comando do Windows, o que pode ser útil.

-   O [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). Este é um único pacote contendo todas as bibliotecas necessárias para compilar o FreeCAD no Windows. Baixe a versão do LibPack que corresponde à versão do FreeCAD que você deseja compilar. Para compilar o FreeCAD 0.20 baixe o [LibPack versão 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6), para o FreeCAD 0.19 baixe o [LibPack versão 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Extraia o LibPack para um local conveniente. (Se o computador não reconhecer a extensão .7z, você deve instalar o programa [7-zip](https://www.7-zip.org).)

**Nota**: É altamente recomendável compilar o FreeCAD com a versão do compilador para a qual o LibPack foi projetado. Por exemplo, você pode ter problemas ao compilar o FreeCAD 0.20 usando o MSVC 2017 porque o LibPack foi projetado para ser criado com o MSVC 2019 ou mais recente. Para atualizar seu LibPack mais tarde, consulte a seção [Atualizando o LibPack](#Updating_the_LibPack.md).



### Programas opcionais 

-   Um frontend GUI para Git. Existem vários frontends disponíveis, veja [esta lista](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). O principal benefício de um frontend é que você não precisa aprender os comandos do Git para obter o código-fonte do FreeCAD ou enviar patches para o repositório GitHub do FreeCAD.

A seguir, descrevemos o tratamento do código-fonte usando o frontend [TortoiseGit](https://tortoisegit.org/). Este frontend se integra diretamente ao explorador de arquivos do Windows e tem uma grande comunidade de usuários para obter ajuda caso você tenha problemas.

-   O [NSIS](http://sourceforge.net/projects/nsis/) é usado para gerar o instalador do FreeCAD Windows.



### Código fonte 

Agora você pode obter o código fonte do FreeCAD:



#### Usando um frontend 

Ao usar o [frontend Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Crie uma nova pasta onde o código-fonte será baixado.
2.  Clique com o botão direito do mouse nesta pasta no explorador de arquivos do Windows e selecione Git Clone no menu de contexto.
3.  Uma caixa de diálogo será exibida. Nele, insira a URL do repositório Git do FreeCAD

*<https://github.com/FreeCAD/FreeCAD.git>*

e clique em **OK**.

O código fonte mais recente será baixado do repositório FreeCAD Git e a pasta será rastreada pelo Git.



#### Usando a linha de comando 

Para criar uma ramificação de rastreamento local e baixar o código-fonte, abra um terminal (prompt de comando) e alterne para o diretório desejado e digite:


```python
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
```



### Compilador

O compilador padrão (recomendado) é o MS Visual Studio (MSVC). Embora possa ser possível usar outros compiladores, por exemplo, gcc via Cygwin ou MinGW, ele não é testado ou abordado aqui.

Você pode obter uma versão gratuita do MSVC (para uso individual) baixando a edição [*comunitária* do MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Para aqueles que querem evitar a instalação do enorme MSVC com o mero propósito de ter um compilador, consulte [ CompileOnWindows - Reduzindo o espaço ocupado pelo disco](CompileOnWindows_-_Reducing_Disk_Footprint/pt-br.md).

**Nota**: Embora a edição **comunitária** do MSVC seja gratuita, para usar o IDE por mais de 30 dias de avaliação, você deve criar uma conta da Microsoft. Se você só compilar usando a linha de comando, você não precisa do IDE e, portanto, nenhuma conta da Microsoft.

Como um IDE alternativo livre e OpenSource você pode usar o [KDevelop](https://www.kdevelop.org/download). Você pode usar o KDevelop para modificar e escrever código C++, mas deve usar a linha de comando para compilar.



### Configuração opcional do caminho do sistema 

Opcionalmente, você pode incluir os caminhos para algumas pastas para a variável PATH do sistema. Isso é útil se você quiser acessar programas nessas pastas a partir da linha de comando/powershell ou se quiser que programas especiais sejam encontrados pelo compilador ou CMake. Além disso, adicionar pastas ao PATH pode ser necessário se você não usou as opções correspondentes ao instalar o programa.

-   Você pode incluir a pasta do seu LibPack na variável PATH do sistema. Isso é útil se você planeja criar várias configurações/versões do FreeCAD.
-   Se você não usou a opção para adicionar o CMake ao PATH durante a instalação, adicione sua pasta de instalação

*C:\\Arquivos de Programas\\CMake\\bin* para o PATH.

-   Se você não usou a opção de adicionar TortoiseGit ao PATH durante a instalação, adicione sua pasta de instalação

*C:\\Arquivos de Programas\\TortoiseGit\\bin* para o PATH.

Para adicionar caminhos de pasta à variável PATH:

1.  No menu Iniciar do Windows, clique com o botão direito do mouse em Computador e escolha Propriedades.
2.  Na caixa de diálogo exibida, clique em Configurações avançadas do sistema.
3.  Outra caixa de diálogo será aberta. Clique lá na aba Avançado em **Variáveis de Ambiente**.
4.  Novamente, outra caixa de diálogo será aberta. Selecione então a variável *Path* e clique em **Edit**.
5.  E novamente outra caixa de diálogo será aberta. Clique lá em **Novo** e adicione ao caminho para a pasta do Git ou do LibPack.
6.  Finalmente, pressione **OK** e feche todas as caixas de diálogo pressionando **OK** também.



## Configuração

Depois de ter todas as ferramentas, bibliotecas e código-fonte do FreeCAD necessários, você está pronto para começar o processo de configuração e compilação. Este processo prosseguirá em cinco etapas:

1.  Execute o CMake uma vez para examinar seu sistema e iniciar o progresso da configuração (isso informará que ele falhou).
2.  Ajuste as configurações necessárias do CMake para definir os locais do LibPack e ativar o Qt5.
3.  Execute novamente o CMake para finalizar a configuração (desta vez ele deve ter êxito).
4.  Use o CMake para gerar o sistema de compilação do Visual Studio.
5.  Use o Visual Studio para criar o FreeCAD.

### CMake

Primeiro, configure o ambiente de compilação usando o CMake:

1.  Abra a GUI do CMake
2.  Especifique a pasta de origem do FreeCAD.
3.  Especifique uma pasta de compilação. Isso pode ser **compilado** na pasta que você clonou o repositório porque esse caminho é ignorado pelo git. Não use a pasta de origem. O CMake criará essa pasta se ela não existir.
4.  Clique em **Configurar**.
5.  Na caixa de diálogo exibida, especifique o gerador que deseja usar: na maioria dos casos, você usará os padrões nesta caixa de diálogo. Para o MS Visual Studio padrão, use o *Visual Studio xx 2yyy* onde xx é a versão do compilador e 2yyy o ano de seu lançamento. É recomendável usar a opção padrão *Usar compiladores nativos padrão*.

**Nota**: É importante especificar a variante de bit correta. Se você tiver a variante de 64 bits do LibPack, você também deve usar o compilador x64.

Isso iniciará a configuração e *falhará* devido à falta de configurações. Isso é normal, você ainda não especificou o local do LibPack. No entanto, existem outras falhas que podem ocorrer que exigem alguma ação adicional de sua parte.

Se ele falhar com a mensagem que Visual Studio não pôde ser encontrado, o suporte CMake no MSVC ainda não está instalado. Para fazer isso:

1.  Abra o IDE do MSVC
2.  Use o menu Ferramentas → Obter ferramentas e recursos
3.  Na guia *Cargas de trabalho*, habilite o *desenvolvimento* de área de trabalho com C++
4.  No lado direito, agora você deve ver que o componente *Visual C++ tools for CMake* será instalado.
5.  Instale-o.

Se ele falhar com uma mensagem sobre a versão errada do Python ou Python ausente, então:

1.  Use a caixa \"Pesquisa:\" no CMake para procurar a cadeia de caracteres \"Python\"
2.  Se você vir um caminho como *C:/Program Files/Python38/python.exe*, o CMake reconheceu o Python que já está instalado no seu PC, mas essa versão não é compatível com o LibPack. Como o LibPack inclui uma versão compatível do Python, modifique as seguintes configurações do Python no CMake para seus caminhos (supondo que o LibPack esteja na pasta *D:/FreeCAD-build/FreeCADLibs_2_8_x64_VC2019*):

![](images/CMake_Python_settings.png )

Se não houver nenhum erro sobre o Visual Studio ou Python, tudo está bem, mas o CMake ainda não sabe todas as configurações necessárias. Portanto, agora:

1.  Pesquise no CMake a variável **FREECAD_LIBPACK_DIR** e especifique o local da pasta LibPack que você baixou anteriormente.
2.  (*Se construir FreeCAD 0.19*) Procure a **variável BUILD_QT5** e habilite essa opção.
3.  (*Se estiver planejando executar diretamente da pasta de compilação, como para depuração*) Procure e habilite as seguintes opções:
    -   **FREECAD_COPY_DEPEND_DIRS_TO_BUILD**
    -   **FREECAD_COPY_LIBPACK_BIN_TO_BUILD**
    -   **FREECAD_COPY_PLUGINS_BIN_TO_BUILD**
4.  Clique em **Configurar** novamente.

Agora não deve haver erros. Se você continuar a encontrar erros que você não pode diagnosticar, visite o fórum [instalação/compilação](https://forum.freecadweb.org/viewforum.php?f=4) no site do fórum FreeCAD. Se o CMake procedeu corretamente, clique em Gerar. Depois que isso for feito, você pode fechar o CMake e iniciar a compilação do FreeCAD usando o Visual Studio. No entanto, para a primeira compilação, mantenha-a aberta caso queira ou precise alterar algumas opções para o processo de compilação.



### Opções para o processo de compilação 

O sistema de compilação CMake oferece controle sobre alguns aspectos do processo de compilação. Em particular, você pode ativar e desativar alguns recursos ou módulos usando variáveis CMake.

Aqui está uma descrição de algumas dessas variáveis:

  Nome da variável                    Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Padrão
    
  BUILD_XXX                           Construa o FreeCAD com o componente XXX. Se você não quiser/precisar compilar, por exemplo, o workbench *OpenSCAD*, desative a variável *BUILD_OPENSCAD*. FreeCAD então não terá esta bancada. **Nota**: Alguns componentes são necessários para outros componentes. Se, por exemplo, você desmarcar *BUILD_ROBOT* CMake irá informá-lo que, em seguida, o componente *Path* não pode ser compilado corretamente. Portanto, verifique a saída do CMake depois de alterar uma opção BUILD_XXX!                                                                                                                                                                                                       Depende
  BUILD_ENABLE_CXX_STD                A versão do padrão de linguagem C++. **C++14** é o mais alto possível para o FreeCAD 0.19, enquanto pelo menos **C++17** é necessário para o FreeCAD 0.20. Consulte também a nota na seção [Criando com o Visual Studio 15 (2017) e 16 (2019)](#Release_Build.md)                                                                                                                                                                                                                                                                                                                                                                                                                           Depende
  BUILD_DESIGNER_PLUGIN               Para criar o plugin Qt Designer, consulte [esta seção abaixo](Compile_on_Windows#Qt_Designer_plugin/pt-br.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               OFF
  BUILD_FLAT_MESH                     Necessário ter uma compilação que inclua o [recurso CreateFlatMesh](MeshPart_CreateFlatMesh.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             OFF
  CMAKE_INSTALL_PREFIX                A pasta de saída ao criar o INSTALL de destino, consulte também a seção [Executando e instalando o FreeCAD](#Running_and_installing_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Pasta de instalação de programas padrão do Windows
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Copia as bibliotecas dependentes necessárias para executar o FreeCAD.exe para a pasta de compilação. Consulte também a seção [Executando e instalando o FreeCAD](#Running_and_installing_FreeCAD.md). **Nota**: as opções só FREECAD_COPY_XXX aparecer se as bibliotecas ainda não tiverem sido copiadas. Se você só precisa atualizar/alterar para outra versão do LibPack, consulte a seção [Atualizando o LibPack](#Updating_the_LibPack.md). Se você quiser trazer de volta as opções por algum motivo, você precisa excluir todas as pastas em sua pasta de compilação, exceto a pasta LibPack. No CMake, exclua o cache e inicie como se você compilasse pela primeira vez.   OFF
  FREECAD_COPY_LIBPACK_BIN_TO_BUILD   Copia os binários LibPack necessários para executar o FreeCAD.exe para a pasta de compilação. Consulte também a seção [Executando e instalando o FreeCAD](#Running_and_installing_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Copia os arquivos de plug-in do Qt necessários para executar o FreeCAD.exe para a pasta de compilação. Consulte também a seção [Executando e instalando o FreeCAD](#Running_and_installing_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     OFF
  FREECAD_LIBPACK_USE                 Ative ou desative o uso do FreeCAD LibPack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ON
  FREECAD_LIBPACK_DIR                 Diretório onde está a LibPack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       FreeCAD\'s source code folder
  FREECAD_RELEASE_PDB                 Crie bibliotecas de depuração (\*.pdb) também para compilações de versão. Ele não afeta a velocidade (como uma compilação de depuração real faria) e pode ser muito útil para localizar falhas no código FreeCAD. Caso o FreeCAD trave, será criado um arquivo *crash.dmp* que pode ser carregado com o MSVC e se você tiver os arquivos PDB correspondentes mais o código-fonte dessa versão, você poderá depurar através do código. Sem os arquivos PDB não é possível depurar o código e tudo o que o depurador mostra é o nome da DLL onde a falha ocorreu.                                                                                                                                     ON
  FREECAD_USE_MP_COMPILE_FLAG         Adiciona a opção /MP (multiprocessador) aos projetos do Visual Studio, habilitando acelerações em CPUs de vários núcleos. Isso pode acelerar muito as compilações em processadores modernos. **Nota**: Se você desativar FREECAD_USE_PCH, a compilação pode sobrecarregar rapidamente o espaço de heap, mesmo se você tiver 16 GB de RAM.                                                                                                                                                                                                                                                                                                                                                           ON
  FREECAD_USE_PCH                     [Pré-compila os cabeçalhos](https://en.wikipedia.org/wiki/Precompiled_header) para economizar tempo de compilação.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ON
  FREECAD_USE_PYBIND11                Inclui a biblioteca [PyBind11](https://github.com/pybind/pybind11). Necessário ter uma compilação que inclua o [recurso CreateFlatMesh](MeshPart_CreateFlatMesh.md). **Nota**: depois de ativá-lo, você pode receber um erro de configuração. Basta configurar novamente e o problema deve desaparecer.                                                                                                                                                                                                                                                                                                                                                                                     OFF



## Construindo o FreeCAD 

Dependendo do seu compilador, o processo para construir o FreeCAD será ligeiramente diferente. Nas seções a seguir, fluxos de trabalho conhecidos são descritos. Se você estiver construindo com o Qt Creator, pule para [Construindo com o Qt Creator (desatualizado)](#Building_with_Qt_Creator_.28outdated.29.md), caso contrário, prossiga diretamente:



### Compilando a partir de cmd.exe linha de comando 

Se você quiser compilar a partir da linha de comando, a saída do CMake mostrará o comando apropriado a ser executado (que depende do diretório de versão configurado). Mas este comando produzirá uma compilação de *depuração* que não funciona no Windows e resulta em um erro de importação Numpy no FreeCAD (que é um problema conhecido, mas difícil de corrigir). Você precisa especificar a opção *\--config Release* para forçar uma compilação de *Release*:


```python
cmake --build E:/release --config Release
```

Observe que a configuração de variáveis CMake como *CMAKE_BUILD_TYPE* não tem nenhum efeito, apenas especificar a opção \--config como mostrado acima funciona.


<div class="mw-collapsible mw-collapsed toccolours">



### Criando com o Visual Studio 15 (2017) ou mais recente 


<div class="mw-collapsible-content">

 Compilação de versão

1.  Inicie o IDE do Visual Studio. Isso pode ser feito pressionando o botão Open Project na GUI do CMake ou clicando duas vezes no FreeCAD.sln de arquivo que você encontra em sua pasta de compilação.
2.  Na barra de ferramentas do IDE MSVC certifique-se de que você use para a primeira versão de compilação.
3.  Há uma janela chamada Gerenciador de Soluções. Ele lista todos os possíveis destinos de compilação. Para iniciar uma compilação completa, clique com o botão direito do mouse no **ALL_BUILD** de destino e escolha **Compilar**.

Isso vai demorar bastante.

Para compilar um FreeCAD pronto para uso, compile o INSTALL de destino, consulte a seção [Executando e instalando o FreeCAD](#Running_and_installing_FreeCAD.md).

Se você não receber nenhum erro, você está feito. **Parabéns!** Você pode sair do MSVC ou mantê-lo aberto.

**Importante**: Desde o Visual Studio 17.4, você não pode usar a otimização de código que está ativada por padrão para o **SketcherGui** de destino. Se você fizer isso, as restrições de ângulo serão deslocadas nos esboços. Para corrigir isso, clique com o botão direito do mouse nesse destino no gerenciador de soluções do MSVC e selecione a última entrada **Propriedades** no menu de contexto. Na caixa de diálogo exibida, vá para C/C++ → Optimization e lá desabilite a configuração **Optimization**. Finalmente, construa o **ALL_BUILD** alvo novamente.



### Compilação de depuração 

Para uma compilação de depuração é necessário que seja usado o Python que está incluído no LibPack. Para garantir isso:

1.  Procure \"Python\" na GUI do CMake
2.  Se você vir um caminho como *C:/Program Files/Python38/python.exe*, o CMake reconheceu o Python que está instalado no seu PC e não o do LibPack. Nesse caso, adapte essas diferentes configurações do Python no CMake para isso (supondo que o LibPack esteja na pasta *D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17*):

![](images/CMake_Python_settings.png )

Como pré-requisito para a compilação de depuração, você precisa fazer o seguinte:

1.  Copie o conteúdo da pasta LibPack para a pasta *bin* da pasta de compilação do FreeCAD (substitua os arquivos existentes).
2.  Copie o conteúdo da pasta *LibPack libd* para a pasta *lib* da pasta de compilação do FreeCAD.

Agora você pode compilar:

1.  Inicie o IDE do Visual Studio. Isso pode ser feito pressionando o botão *Open Project* na GUI do CMake ou clicando duas vezes no FreeCAD.sln de arquivo que você encontra em sua pasta de compilação.
2.  Na barra de ferramentas do IDE MSVC certifique-se de que você use para a primeira compilação *Debug*.
3.  Há uma janela chamada *Gerenciador de Soluções*. Ele lista todos os possíveis destinos de compilação. Para iniciar uma compilação completa, clique com o botão direito do mouse no **ALL_BUILD** de destino e escolha **Construir** no menu de contexto.

Isso vai demorar bastante.

Se não houver erros de compilação e se as opções **FREECAD_COPY\_\*** mencionadas na etapa [Configuração do CMake](#CMake.md) acima estiverem habilitadas, você poderá iniciar a compilação de depuração:

1.  Clique com o botão direito do mouse no **FreeCADMain** de destino e escolha **Definir como Projeto de Inicialização** no menu de contexto.
2.  Finalmente, clique na barra de ferramentas no botão com o triângulo verde chamado **Depurador Local do Windows**.

Isso iniciará a compilação de depuração do FreeCAD e você poderá usar o IDE do MSVC para depurá-lo.

#### Recurso de vídeo 

Um tutorial em inglês que começa com a configuração no CMake Gui e continua até o comando \'Build\' no Visual Studio 16 2019 está disponível no YouTube em [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Construindo com o Qt Creator (desatualizado) 


<div class="mw-collapsible-content">



#### Instalação e configuração do Qt Creator 

-   Baixe e instale o [Qt Creator](https://www.qt.io/offline-installers)
-   Ferramentas → Opções → Editor de Texto → guia Comportamento:
    -   Codificações de arquivo → codificações padrão:
    -   Definido para: **ISO-8859-1 /\... csISOLatin1** (Certos caracteres criam erros/avisos com o Qt Creator se forem deixados definidos como UTF-8. Isso parece corrigi-lo.)
-   Ferramentas → opções → Build & Executar:

Guia CMake

-   -   Preencha a caixa Executável com o caminho para cmake.exe
-   -   Guia Kits
        -   Nome: MSVC 2008
        -   Compilador: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Depurador: Auto detectado\...
        -   Versão Qt: Nenhum
    -   Guia Geral
        -   Desmarque: Sempre compile o projeto antes de implantá-lo
        -   Desmarque: sempre implantar o projeto antes de executá-lo



#### Importar projeto e construção 

-   Arquivo → Abrir arquivo ou projeto
-   Abra **CMakeLists.txt** que está no nível superior da fonte
-   Isso iniciará o CMake
-   Escolha o diretório de compilação e clique em Avançar
-   Gerador de conjunto para gerador **NMake (MSVC 2008)**
-   Clique em Executar CMake. Siga as instruções descritas acima para configurar o CMake ao seu gosto.

Agora o FreeCAD pode ser construído

-   Construir → construir tudo
-   Isso vai levar muito tempo\...

Uma vez concluído, ele pode ser executado: Há 2 triângulos verdes no canto inferior esquerdo. Uma delas é a depuração. A outra é executada. Escolha o que quiser.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Compilação de linha de comando 


<div class="mw-collapsible-content">

As etapas como compilar a partir da linha de comando depende do compilador. Para o MSVC 2017 as etapas são:

1.  No menu Iniciar do Windows, vá para **Visual Studio 2017 → Visual Studio Tools** e escolha **Prompt de comando do desenvolvedor para VS 2017**
2.  Altere para sua pasta de compilação.
3.  Execute o comando


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

ou


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```

Essas etapas também podem ser automatizadas. Aqui está, por exemplo, uma solução para o MSVC 2017:

1.  Baixe o script [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Renomeie-o para *compile-FC.bat*
3.  No explorador de arquivos do Windows, Shift+Clique com o botão direito do mouse em sua pasta de compilação e use no menu de contexto *Prompt de comando aqui*.
4.  Execute o comando


```pythoncompile-FC install```

Em vez de chamar **compile-FC** com a opção *install*, você também pode usar *debug* ou *release*:

*debug*   - compilar o FreeCAD na configuração de depuração

*release* - compilar o FreeCAD na configuração da versão

*install* - compilar o FreeCAD na configuração da versão e criar uma configuração de instalação


</div>


</div>



## Executando e instalando o FreeCAD 

Existem 2 métodos para executar o FreeCAD compilado:

*Método 1*: Executar o FreeCAD.exe que você encontrar em sua pasta de compilação no compartimento de subpasta *bin*

*Método 2*: Criar o destino *INSTALL*

O método 2 é o mais simples porque garante automaticamente que todas as bibliotecas necessárias para executar o FreeCAD.exe estão na pasta correta. O FreeCAD.exe e as bibliotecas serão gerados na pasta especificada na variável *CMake CMAKE_INSTALL_PREFIX*.

Para o Método 1, você precisa habilitar as opções **FREECAD_COPY\_\*** mencionadas na [etapa Configuração do CMake](#CMake.md) acima.



### Solucionando problemas 

Ao executar o FreeCAD, você pode encontrar DLLs ausentes ao usar determinadas bancadas de trabalho ou recursos de bancadas de trabalho. A mensagem de erro no console do FreeCAD não informará qual DLL está faltando. Para descobrir isso, você deve usar uma ferramenta externa:

-   Baixe a versão mais recente do programa **Dependências**: <https://github.com/lucasg/Dependencies/releases> (escolha o arquivo *Dependencies_x64_Release.zip*)
-   No [ console Python ](Python_console/pt-br.md) do FreeCAD execute estes comandos:

import os os.system(r\"\~\\DependenciesGui.exe\") **Nota**: Em vez do \~ você deve especificar o caminho completo para o *DependenciesGui.exe* em seu sistema.

-   Agora arraste o arquivo \*.pyd da bancada de trabalho com a qual você obtém DLLs ausentes relatadas.



## Atualizando a compilação 

FreeCAD é muito ativamente desenvolvido. Portanto, seu código-fonte muda quase diariamente. Novos recursos são adicionados e bugs são corrigidos. Para se beneficiar dessas mudanças no código-fonte, você deve reconstruir seu FreeCAD. Isso é feito em duas etapas:

1.  Atualizando o código-fonte
2.  Recompilação



### Atualizando o código-fonte 



#### Usando um frontend 

Ao usar o [frontend Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit: Clique com o botão direito do mouse na pasta de código-fonte do FreeCAD no explorador de arquivos do Windows e selecione **Pull** no menu de contexto. Uma caixa de diálogo será exibida. Selecione a ramificação de desenvolvimento que você deseja obter. **mestre** é o ramo principal. Portanto, use isso, a menos que você queira compilar um novo recurso especial de uma ramificação que ainda não foi mesclada ao *mestre*. (Para obter mais informações sobre ramificações do Git, consulte [Processo de desenvolvimento do Git](Source_code_management#Git_development_process.md).)

Por fim, clique em **OK**.



#### Usando a linha de comando 

Abra um terminal (prompt de comando) e alterne para o diretório de origem. Em seguida, digite:


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

onde *mestre* o nome do ramo de desenvolvimento principal. Se você quiser obter código de outra ramificação, use seu nome em vez de *mestre*.



### Recompilação

1.  Abra o IDE do MSVC clicando duas vezes no *FreeCAD.sln* de arquivo ou no *ALL_BUILD.vcxproj* de arquivo na pasta de compilação.
2.  Continue com a etapa 2 da seção [Criando com o Visual Studio 15 2017](#Building_with_Visual_Studio_15_.282017.29_or_newer.md).



## Atualizando o LibPack 

Se uma nova versão principal de uma dependência de terceiros, como o Open Cascade, for lançada, ou se uma dependência de terceiros tiver correções de bugs importantes, uma nova LibPack será lançada. Você pode encontrar a versão mais recente [aqui](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

Para atualizar seu LibPack, a seguinte receita é a prática recomendada:

1.  Exclua a pasta *bin* na pasta de compilação.
2.  Mude para a pasta LibPack local e exclua tudo lá.
3.  Extraia o conteúdo do novo arquivo ZIP LibPack para a pasta LibPack local existente, mas agora vazia.
4.  Abra o CMake e pressione o botão **Configurar** e, em seguida, o botão **Gerar**. Isso recria a pasta *bin* que você acabou de excluir e também copia os novos arquivos LibPack para ela.
5.  No CMake, clique no botão **Abrir projeto** e o IDE do MSVC será aberto.
6.  No IDE do MSVC, compile o *destino INSTALL*.



## Ferramentas

Para participar do desenvolvimento FreeCAD você deve compilar e instalar as seguintes ferramentas:



### Plugin Qt Designer 

FreeCAD usa [Qt](https://en.wikipedia.org/wiki/Qt_(software)) como kit de ferramentas para sua interface de usuário. Todas as caixas de diálogo são configuradas em arquivos de interface do usuário que podem ser editados usando o programa [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) que faz parte de qualquer instalação do Qt e também está incluído no LibPack. O FreeCAD tem seu próprio conjunto de widgets Qt para fornecer recursos especiais, como adicionar uma unidade aos campos de entrada e definir propriedades de preferências.



#### Compilação

O plugin não pode ser carregado pelo Qt Designer se ele foi compilado usando outra versão do Qt que não aquela em que seu Qt Designer/Qt Creator é baseado. Portanto, o plugin deve ser compilado junto com o FreeCAD:

-   Nas opções do CMake (consulte esta seção acima), habilite a opção BUILD_DESIGNER_PLUGIN e reconfigure.
-   abra o MSVC e crie o **FreeCAD_widgets** de destino

Como resultado, você obterá o arquivo de plugin **FreeCAD_widgets.dll** na pasta *\~\\src\\Tools\\plugins\\widget\\Release*



#### Instalação

Para instalar o plugin, copie a DLL para:

-   Se você usar o LibPack: para a pasta

*\~\\FreeCADLibs_2_8_x64_VC2019\\plugins\\designer*

-   Se você tiver uma instalação completa do Qt: poderá escolher entre a pasta

*C:\\Qt\\5.15.2\\msvc2019_64\\plugins\\designer* ou *C:\\Qt\\5.15.2\\msvc2019_64\\bin\\designer* (você deve primeiro criar a subpasta designer.) (adapte os caminhos à sua instalação!).

Finalmente (re)inicie o Qt Designer e verifique seu menu **Ajuda → Plugins**. Se o plugin **FreeCAD_widgets.dll** estiver listado como sendo carregado, agora você pode projetar e alterar os arquivos .ui do FreeCAD. Caso contrário, você deve [compilar](#Compilation.md) a DLL por si mesmo.

Se você preferir usar o [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) em vez do Qt Designer, o arquivo do plugin deve ser colocado nesta pasta:*C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer* Em seguida, (re)inicie o Qt Creator, alterne para o modo **Design** e, em seguida, verifique o menu **Ferramentas → Editor de Formulários → Sobre os plug-ins do Qt Designer**. Se o **FreeCAD_widgets.dll** do plugin estiver listado como sendo carregado, agora você pode projetar e alterar os arquivos .ui do FreeCAD. Caso contrário, você deve [compilar](#Compilation.md) a DLL por si mesmo.



### Provedor de miniaturas 

FreeCAD tem o recurso para fornecer miniaturas de visualização para \*. Arquivos FCStd. Isso significa que no explorador de arquivos do Windows \*. Os arquivos FCStd são mostrados com uma captura de tela do modelo que ele contém. Para fornecer esse recurso, o FreeCAD precisa ter o arquivo **FCStdThumbnail.dll** instalado no Windows.



#### Instalação 

A DLL é instalada desta forma:

1.  Baixe [este arquivo ZIP](https://forum.freecadweb.org/download/file.php?id=13404) e extraia-o.
2.  Abra um prompt de comando do Windows com privilégios de administrador (esses privilégios são um requisito).
3.  Mude para a pasta onde a DLL está.
4.  Execute este comando 
```pythonregsvr32 FCStdThumbnail.dll```

Portanto, verifique se funciona, certifique-se de que no FreeCAD a opção de preferências **[Salvar miniatura no arquivo de projeto](Preferences_Editor#Document.md)** ao salvar o documento esteja ativada e salve um modelo. Em seguida, exiba no Windows Explorer a pasta do modelo salvo usando um modo de exibição de símbolo. Agora você deve ver uma captura de tela do modelo na exibição de pasta.



#### Compilação 

Para compilar o FCStdThumbnail.dll

1.  Mude para a pasta de origem do FreeCAD*\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Abra a GUI do CMake
3.  Especifique como pasta de origem aquela em que você está atualmente.
4.  Use a mesma pasta que a pasta de compilação.
5.  Clique em **Configurar**
6.  Na caixa de diálogo exibida, especifique o gerador de acordo com o que você deseja usar. Para o MS Visual Studio padrão, use o *Visual Studio xx 2yyy* onde xx é a versão do compilador e 2yyy o ano de seu lançamento. É recomendável usar a opção padrão Usar compiladores nativos padrão.**Nota**: É importante especificar a variante de bits correta. Se você tiver a variante de 64 bits do LibPack, você também deve usar o compilador x64.
7.  Clique em **Gerar**.
8.  Agora você deve ter o arquivo **ALL_BUILD.vcxproj** na pasta *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Clique duas vezes nele e o IDE MSVC será aberto.
9.  Na barra de ferramentas do IDE MSVC certifique-se de que você use a versão de destino de compilação.
10. Há uma janela chamada *Gerenciador de Soluções*. Clique com o botão direito do mouse em **ALL_BUILD** e escolha **Compilar**.
11. Como resultado, agora você deve ter um **FCStdThumbnail.dll** na pasta *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* que você pode instalar conforme descrito acima.



## Compilando o Open Cascade 

O LibPack vem com uma versão do [Open Cascade](https://en.wikipedia.org/wiki/Open_Cascade) que é adequado para uso geral. No entanto, sob algumas circunstâncias, você pode querer compilar contra uma versão alternativa do Open Cascade, como um de seus lançamentos oficiais, ou um fork corrigido.

Ao compilar o Open Cascade para FreeCAD, observe que não há garantia de que o FreeCAD funcionará com todas as versões do Open Cascade. Observe também que quando você estiver usando a biblioteca Netgen, você deve usar a versão NetGen que ele aprovou para compilar com a versão Open Cascade que você gosta de compilar.

Para compilar:

-   Primeiro, obtenha o código-fonte do Open Cascade, diretamente do [repositório git do Open Cascade](https://github.com/Open-Cascade-SAS/OCCT) ou clonando o fork de outra pessoa, como [o fork \"blobfish\"](https://gitlab.com/blobfish/occt) mantido pelo membro do fórum FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

-   Em seguida, abra a GUI do CMake para configurar o sistema de compilação de maneira semelhante à compilação do FreeCAD. Estas opções do CMake têm de ser definidas (ou explicitamente não definidas):

  Nome da variável                   Descrição                                                                                                                                                                                                                                                                                                                Padrão
    
  3RDPARTY_DIR                       O caminho para os componentes 3rdparty. Recomenda-se usar a pasta como entrada onde está o LibPack usado. Deixe explicitamente este campo vazio.                                                                                                                                                                         vazio
  3RDPARTY_DOXYGEN_EXECUTABLE        O caminho para o executável do componente 3rdparty [Doxygen](https://en.wikipedia.org/wiki/Doxygen). Recomenda-se instalar o Doxygen. O CMake irá encontrá-lo automaticamente.                                                                                                                                           vazio
  3RDPARTY_FREETYPE_DIR              O caminho para o componente 3rdparty necessário [Freetype](https://en.wikipedia.org/wiki/FreeType). Recomenda-se usar a pasta como entrada onde está o LibPack usado.                                                                                                                                                    vazio
  3RDPARTY_RAPIDJSON_DIR             Disponível somente se **USE_RAPIDJSON** for usado. O caminho para o componente 3rdparty [RapidJSON](https://rapidjson.org/). Recomenda-se NÃO usar uma pasta LibPack existente como entrada. Você pode usar a pasta RapidJSOn de um LibPack, mas copie-a para uma nova pasta e use essa nova pasta como entrada.         vazio
  3RDPARTY_TCL_DIR                   O caminho para o componente 3rdparty necessário [TCL](https://en.wikipedia.org/wiki/Tcl). Recomenda-se NÃO usar uma pasta LibPack existente como entrada. Tomemos por exemplo uma [dessas versões](https://github.com/teclab-at/tcltk/releases), extraia-a e tome isso como pasta de entrada para o CMake.               vazio
  3RDPARTY_TK_DIR                    O caminho para o [TK](https://en.wikipedia.org/wiki/Tk_(software)) do componente 3rdparty necessário. Recomenda-se NÃO usar uma pasta LibPack existente como entrada. Tomemos por exemplo uma [dessas versões](https://github.com/teclab-at/tcltk/releases), extraia-a e tome isso como pasta de entrada para o CMake.   vazio
  3RDPARTY_VTK_DIR                   Disponível somente se **USE_VTK** for usado. O caminho para o [VTK](https://en.wikipedia.org/wiki/VTK) do componente 3rdparty necessário. Recomenda-se usar a pasta como entrada onde está o LibPack usado. Se você usar outra pasta, certifique-se de que não usa VTK 9.x ou mais recente.                              vazio
  BUILD_RELEASE_DISABLE_EXCEPTIONS   Desabilita o tratamento de exceções para compilações de versão. Para FreeCAD você deve defini-lo como **OFF**.                                                                                                                                                                                                           ON
  INSTALL_DIR                        A pasta de saída ao criar o *INSTALL* de destino. Se a compilação foi bem-sucedida, pegue os arquivos dessa pasta para atualizar seu LibPack.                                                                                                                                                                            Pasta de instalação do programa padrão do Windows
  INSTALL_DIR_BIN                    A subpasta de saída para a DLL ao criar o *INSTALL* de destino. Você deve alterá-lo para **bin**.                                                                                                                                                                                                                        win64/vc14/bin
  INSTALL_DIR_LIB                    A subpasta de saída para os arquivos .lib ao criar o *INSTALL* de destino. Você deve alterá-lo para **lib**                                                                                                                                                                                                              win64/vc14/lib
  USE_RAPIDJSON                      Para compilar o Open Cascade com suporte para RapidJSON. Habilitar isso é obrigatório para obter suporte para o formato de arquivo [glTF](https://en.wikipedia.org/wiki/Gltf).                                                                                                                                           OFF
  USE_VTK                            Para compilar o Open Cascade com suporte para VTK. Habilitar isso é o ideal. Você pode usar isso para construir a ponte VTK do Open Cascade.                                                                                                                                                                             OFF

-   Abra o projeto no Visual Studio e primeiro compile os destinos ALL_BUILD e, em seguida, INSTALL no modo de **versão**.
-   Repita a criação dos dois destinos no modo **Depurar**.

Para compilar o FreeCAD usando o Open Cascade auto-compilado, você deve fazer o seguinte:

-   Copie todas as pastas do INSTALL_DIR para a pasta LibPack (substitua os arquivos existentes)
-   Alterne para a pasta LibPack e vá lá para a subpasta *cmake*
-   Abra lá o arquivo *OpenCASCADEDrawTargets.cmake* com um editor de texto
-   Procure caminhos absolutos para sua pasta LibPack e remova-os. Assim, por exemplo, o caminho

absoluto *D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib* torna-se apenas *freetype.lib*

-   Faça o mesmo para o arquivo *OpenCASCADEVisualizationTargets.cmake*



## Compilando redes 

O LibPack vem com uma versão do [Netgen](https://ngsolve.org) que será testada para ser construída com a versão Open Cascade do LibPack. O problema é que cada nova versão do Netgen altera a API. Além disso, cada nova versão do Open Cascade faz o mesmo. Portanto, não se pode simplesmente mudar facilmente a versão Netgen.

No entanto, você pode criar Netgen no entanto. Esta é uma tarefa fácil:

-   Primeiro obtenha o código-fonte da Netgen, diretamente do [repositório git da Netgen](https://github.com/NGSolve/netgen).
-   Em seguida, abra a GUI do CMake para configurar o sistema de compilação de maneira semelhante à compilação do FreeCAD. Estas opções do CMake têm de ser definidas:

  Nome da variável       Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Padrão
    
  CMAKE_INSTALL_PREFIX   A pasta de saída ao criar o *INSTALL* de destino. Se a compilação foi bem-sucedida, pegue os arquivos dessa pasta para atualizar seu LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                C:/netgen
  OpenCasCade_DIR        O caminho para os arquivos CMake do Open Cascade. Se você criou o Open Cascade conforme descrito na seção [Compilando o Open Cascade](#Compiling_Open_Cascade.md), você pode usar a subpasta *cmake* da pasta que você usou como INSTALL_DIR. Caso contrário, use a subpasta *cmake* do seu LibPack. Observe aqui que o LibPack já deve conter uma compilação Open Cascade adequada. Independente da pasta que você usa, agora você também deve criar lá uma subpasta *lib* e copiar nos arquivos *freetype.lib* e *freetyped.lib* do seu LibPack.   vazio
  USE_GUI                defina-o como **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  USE_NATIVE_ARCH        defina-o como **OFF**; isso só é necessário para suportar CPUs mais antigas que não têm o conjunto de instruções [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)                                                                                                                                                                                                                                                                                                                                                                            ON
  USE_OCC                defina-o como **ON**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         OFF
  USE_PYTHON             defina-o como **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  USE_SUPERBUILD         defina-o como **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ON
  ZLIB_INCLUDE_DIR       O caminho para o componente 3rdparty necessário [zlib](https://en.wikipedia.org/wiki/Zlib). Recomenda-se usar a pasta como entrada onde está o LibPack usado.                                                                                                                                                                                                                                                                                                                                                                                                vazio
  ZLIB_LIBRARY_DEBUG     O caminho para o arquivo ZLib *zlibd.lib*. Ele está localizado na subpasta lib da sua pasta LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                         vazio
  ZLIB_LIBRARY_RELEASE   O caminho para o arquivo ZLib *zlib.lib*. Ele está localizado na subpasta lib da sua pasta LibPack.                                                                                                                                                                                                                                                                                                                                                                                                                                                          vazio

-   Além disso, você precisa adicionar uma nova entrada CMake:

nome: *CMAKE_DEBUG_POSTFIX*, tipo: *string*, **conteúdo: \_d** Isso garante que os nomes de arquivo das bibliotecas de depuração recebam outro nome que não as bibliotecas de versão e não possam ser trocados acidentalmente.

-   Pressione o botão *Configurar* no CMake para gerar os arquivos \*.cmake.
-   Somente necessário se houver suporte para CPU mais antiga que não tenha o conjunto de instruções AVX2:
    -   Pesquise na pasta de compilação do Netgen o arquivo *netgen-targets.cmake* e abra-o com um editor de texto. Remova a *configuração ;/arch:AVX2* na INTERFACE_COMPILE_OPTIONS Opção.
    -   Pressione o botão *Configurar* no CMake novamente.
-   Pressione o botão *Gerar* no CMake.
-   Abra o projeto no Visual Studio e primeiro compile os destinos ALL_BUILD e, em seguida, INSTALL no modo **de versão**.
-   Repita a criação dos dois destinos no modo **Depurar**.

Para compilar o FreeCAD usando o Netgen auto-compilado, você deve fazer o seguinte:

-   Copie todas as pastas do CMAKE_INSTALL_PREFIX para a pasta LibPack (substitua os arquivos existentes)



## Referências

Veja também

[Compilação - Acelerando](Compiling_(Speeding_up)/pt-br.md)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/pt-br
