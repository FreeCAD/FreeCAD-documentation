




## Visão geral 


{{TOCright}}

A instalação do FreeCAD nos sistemas Linux mais populares já foi aprovada pela comunidade, e o FreeCAD deve estar diretamente disponível através do gerenciador de pacotes disponíveis em sua distribuição. A equipe do FreeCAD também oferece:

-   Pacotes \"oficiais\" quando novos lançamentos são feitos
-   Repositórios [Arquivo de pacotes pessoais](https://help.ubuntu.com/community/PPA) (PPA), [AppImages](AppImage/pt-br.md) e [Ubuntu Snaps](Ubuntu_Snap/pt-br.md) para testar as últimas características.


<div class="mw-collapsible mw-collapsed toccolours">

## Sistemas baseados em Ubuntu e Ubuntu 

Muitas distribuições Linux são baseadas no Ubuntu e compartilham seus repositórios. Além das variantes oficiais (Kubuntu, Lubuntu e Xubuntu), existem derivados não oficiais como Linux Mint, Voyager e outros. As opções de instalação abaixo devem ser compatíveis com estes sistemas.


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

### Oficial


</div>

O FreeCAD está disponível no repositório Ubuntu Universo, e pode ser instalado através do **Software Center** ou a partir do terminal:


```python
sudo apt install freecad
```


**Nota:**

O repositório Ubuntu pode estar desatualizado. O pacote pode ficar desatualizado do último código-fonte estável. Neste caso, sugere-se a instalação do pacote a partir do PPA `-estável` abaixo. Além disso, a instalação do pacote `-diário` pode ser feita para testar o ramo de desenvolvimento.


<div class="mw-translate-fuzzy">

### PPA Estável 


</div>

O arquivo de pacotes pessoais (PPA) para a versão estável do FreeCAD é mantido pela comunidade FreeCAD no Launchpad. O repositório Launchpad é chamado de [versões estáveis do FreeCAD](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable).

#### GUI

Instalar o PPA estável através da Interface Gráfica de Usuário (GUI):

:   1\. Navegue até {**Software Ubuntu → Software e atualizações → Fontes de software → Outros softwares.**}
:   2\. Clique em **Adicionar**, depois copie e cole a seguinte linha

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Adicione a fonte, feche o diálogo, e recarregue suas fontes de software, se solicitado

Agora você pode encontrar e instalar a última versão estável do FreeCAD a partir do **Ubuntu Software Center**.

#### CLI

Instalar o PPA estável através da Interface de Linha de Comando (CLI):

:   1\. Adicione o PPA às fontes de seu software:

    :   
        
```python
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        
```
        





:   2\. Recuperar as listas de pacotes atualizadas:

    :   
        
```python
        sudo apt update
        
```
        





:   3\. Em seguida, instale o FreeCAD juntamente com sua documentação offline:

    :   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Nota:**

Devido a problemas de empacotamento, em certas versões do Ubuntu o pacote `freecad-doc` colidiu com a instalação do FreeCAD ou de uma de suas dependências; se este for o caso, remova o pacote `freecad-doc` e instale apenas o pacote `freecad`. Se o pacote `freecad-doc` não existir, então ignore-o.

#### Verificação da instalação 

:   4\. Uma vez que você tenha o PPA estável adicionado a seus fontes usando um dos métodos acima, o pacote `freecad` instalará esta versão do PPA sobre a fornecida pelo repositório Ubuntu Universo. Você pode ver as versões disponíveis com o seguinte comando `apt-cache`:
:   
    
```python
    apt-cache policy freecad
    
```
    

A saída deve ser semelhante à seguinte (é claro que a informação da versão irá variar): 
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

5\. Execute a versão estável (PPA) do FreeCAD a partir do GUI ou através do CLI. O último método é o seguinte:

:   
    
```python
    ./freecad
    
```
    

### Desenvolvimento PPA (Diário) 

Como o FreeCAD está em constante desenvolvimento, você pode querer instalar o pacote **diário** para se manter atualizado com as últimas melhorias e correções de bugs. O repositório também é hospedado no Launchpad e é chamado de [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily)..

Esta versão é compilada diariamente a partir do repositório principal oficial. Cuidado, embora contenha novas características e correções de bugs, também pode ter bugs mais recentes e ser instável.

Adicione o PPA diário às fontes de seu software, atualize as listas de pacotes e instale o pacote diário: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Todos os dias você pode se atualizar com as últimas novidades diárias: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Nota:**

Em alguns casos, novos códigos ou dependências adicionados ao FreeCAD causarão erros de empacotamento. Se isto acontecer, o pacote diário não poderá ser gerado até que os mantenedores resolvam os problemas manualmente. Se você deseja continuar testando o código mais recente, você deve obter o código-fonte e compilar o FreeCAD diretamente; para instruções, veja a [compilação](compiling/pt-br.md).

Execute a versão diária (PPA) do FreeCAD

:   
    
```python
    freecad-daily
    
```
    


**Nota:**

É possível instalar tanto os pacotes {`-stable` como `-daily` no mesmo sistema. Isto é útil se você deseja trabalhar com uma versão estável, e ainda ser capaz de testar as últimas características em desenvolvimento. Observe que o executável para a versão diária é `freecad-daily`, mas para a versão estável é apenas `freecad`}.


</div>


</div>

## Debian e outros sistemas baseados no Debian 

=

Desde o Debian Lenny, o FreeCAD está disponível diretamente nos repositórios de software Debian e pode ser instalado via sináptica ou simplesmente com:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

O FreeCAD é normalmente instalado com o YAST (abbr. Mais uma ferramenta de configuração), a ferramenta de configuração e configuração do sistema operacional Linux, ou em qualquer terminal/console (direitos de raiz necessários) com:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Nota:**

Este procedimento cobre apenas a instalação de versões **estáveis** do programa FreeCAD oficialmente lançado, com base nos links instalados para os repositórios do pacote de programas para sua versão do sistema operacional. O pacote openSUSE \"pode estar desatualizado\" porque o pacote pode estar defasado em relação ao último código fonte estável. Neste caso, sugere-se a instalação manual do pacote a partir dos repositórios de origem listados abaixo (Expandir).


<div class="mw-collapsible-content">

É oferecido um extenso programa de lançamento para as versões do pacote FreeCAD. Por favor, visite para uma visão geral:

**[Levantamento dos repositórios no openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Geralmente, para selecionar a distribuição openSUSE correta, é necessário clicar no botão **Ver**.

### Estável

A versão estável do pacote: [Repositórios estáveis no openSUSE](https://software.opensuse.org/package/FreeCAD). A versão correta da distribuição do openSUSE deve ser selecionada na parte inferior da página da Web.

Nota: o openSUSE oferece várias opções ao fazer o download do FreeCAD. Para ver estas opções, visite a [Visão Geral de repositórios estáveis no openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Em desenvolvimento 

Últimos lançamentos de desenvolvimento AKA **instável**: [Lista de repositórios instáveis no openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

É recomendável obter os pacotes binários diretamente. Em seguida, selecione a distribuição apropriada para seu sistema operacional openSUSE instalado.


</div>


</div>

## Gentoo

O FreeCAD pode ser compilado ou instalado simplesmente com este comando:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

O FreeCAD está incluído nos pacotes oficiais do Fedora desde o Fedora 20. Ele pode ser instalado por linha de comando, fazendo:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

Nas versões anteriores do Fedora, isto era:


```python
sudo yum install freecad
```

Os gerenciadores de pacotes gui também podem ser usados. Busca por \"freecad\". A versão oficial do pacote de lançamento tende a estar bem distante dos lançamentos do FreeCAD. [Pacote: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) mostra as versões incluídas nos repositórios Fedora ao longo do tempo e das versões.

Versões mais atuais podem ser obtidas baixando uma das [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)versões do repositório github. Estes funcionam bem no Fedora.

Se você quiser se manter atualizado com os últimos avanços diários, o FreeCAD também está disponível em [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). Para instalar a versão, em um terminal, digite:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

Isso deixa o copr repositório ativo, portanto


```python
sudo dnf upgrade
```

ou equivalente, será atualizado no último FreeCAD build, juntamente com as atualizações de qualquer outro repositório ativo. Se você quiser algo um pouco mais estável, você pode desativar \@freecad/nightly novamente após a instalação inicial. O copr só mantém as construções das últimas 2 semanas. Esta não é uma solução se você quiser escolher uma versão antiga específica.


<div class="mw-translate-fuzzy">

Instruções também estão disponíveis em [Compilação no Linux/Unix](Compile_on_Linux/pt-br.md), incluindo um script especificamente para o Fedora. Com uma pequena modificação, para extrair o compromisso específico do git, qualquer versão desde FreeCAD 0.15 pode ser construída sobre qualquer distribuição da Fedora


</div>


</div>


</div>

## Arch

Instalação do FreeCAD no Arch Linux e derivados (ex. Manjaro):


```python
pacman -S freecad
```

## Outras

Se sua distribuição Linux oferece FreeCAD mas não está documentada nesta página, por favor nos informe no [fórum](http://forum.freecadweb.org/viewforum.php?f=21)!

Muitos pacotes FreeCAD alternativos e não-oficiais estão disponíveis na rede, por exemplo, para sistemas como slackware ou fedora. Uma busca na rede pode lhe dar rapidamente alguns resultados.

### Instalação manual em sistemas baseados em .deb 

Se por algum motivo você não puder usar nenhum dos métodos acima, você pode baixar um dos pacotes .deb disponíveis na página de [Download](Download/pt-br.md).
{{DownloadUnixStable}}

Uma vez que você tenha baixado o .deb para sua versão do sistema, se você tiver o pacote [Gdebi](wikipedia:Debian#GDEBI.md) instalado, basta ir até o local do arquivo baixado e clicar duas vezes sobre ele. Seu gerente de pacotes instalará automaticamente as dependências necessárias. Alternativamente, você também pode instalá-lo a partir do terminal, navegando até onde você baixou o arquivo, e digitar:


```python
sudo dpkg -i Name_of_your_FreeCAD_package.deb
```

mudando Nome\_do\_seu\_pacote\_FreeCAD.deb pelo nome do arquivo que você baixou.

Após instalar o FreeCAD, um ícone de inicialização será adicionado na seção \"Gráfico\" do seu Menu Iniciar.

### Instalando em outros sistemas Linux/Unix 

Muitas distros Linux comuns incluem agora um FreeCAD pré-compilado como parte dos pacotes padrão. Isto está freqüentemente desatualizado, mas é um lugar para se começar. Verifique os gerentes de pacotes padrão para o seu sistema. Uma das seguintes listas (parciais) de comandos poderia instalar a versão oficial do FreeCAD para sua distro do terminal. Estes provavelmente precisam de privilégios de administrador.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
```

O nome do pacote é sensível a maiúsculas e minúsculas, portanto tente \"FreeCAD\" e \"freecad\". Se isso não funcionar para você, ou porque seu gerente de pacotes não tem uma versão FreeCAD pré-compilada disponível, ou porque a versão disponível é muito antiga para suas necessidades, você pode tentar fazer o download de um dos pacotes [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) liberações do repositório github. Estes tendem a funcionar na maioria das distribuições Linux de 64 bits, sem nenhuma instalação especial. Apenas certifique-se de que o arquivo baixado esteja marcado como executável, depois execute-o.


<div class="mw-translate-fuzzy">

Se isso ainda não for suficiente, e você não puder localizar outra fonte de um pacote pré-compilado para sua situação, você precisará [compile você mesmo](Compile_on_Linux/pt-br.md).


</div>

### Instalando a versão Windows no Linux 

Veja a página [Instalando no Windows](Installing_on_Windows/pt-br.md).

## Próximo Passo 

Uma vez que você tenha o FreeCAD instalado, é hora de [Começar a usar](Getting_started/pt-br.md)!







[Category:Common Questions{{\#translation:}}](Category:Common_Questions.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
