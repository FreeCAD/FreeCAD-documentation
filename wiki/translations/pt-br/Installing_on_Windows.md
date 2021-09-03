




Você pode instalar o FreeCAD no Windows baixando um dos instaladores abaixo:


{{DownloadWindowsStable}}

Após baixar o arquivo .exe (NSIS Installer), clique duas vezes nele para iniciar o processo de instalação.

Abaixo estão mais informações sobre algumas opções técnicas. No entanto, a maioria dos usuários não precisa mais do que os arquivos .exe acima. Vá para [Introdução](Getting_started/pt-br.md) após completar a instalação.

## Instalação simples do instalador NSIS {#instalação_simples_do_instalador_nsis}

A maneira mais fácil de **instalar o FreeCAD no Windows** é usando o arquivo de instalação para download acima. Esta página descreve o uso e as características do *Instalador NSIS* para mais opções de instalação.

Se você quiser baixar a versão de desenvolvimento (que pode ser instável), veja a página [Download](Download/pt-br.md).

## Chocolatey

Entretanto, é altamente recomendado que você use um gerenciador de pacotes como o Chocolatey para manter seu software atualizado. Você pode instalar Chocolatey seguindo [estas instruções](https://chocolatey.org/install) e depois abrir um terminal PowerShell como administrador e executar:


```python
choco install freecad
```

de vez em quando, você pode atualizar seu software com


```python
choco upgrade freecad
```

para obter a última versão disponível no repositório Chocolatey. Se houver algum problema com o pacote Chocolatey, você pode entrar em contato com os mantenedores em [esta página](https://chocolatey.org/packages/freecad).

## Instalação usando a linha de comando {#instalação_usando_a_linha_de_comando}

Com o utilitário de linha de comando *msiexec.exe*, recursos adicionais como a instalação não interativa e a instalação administrativa estão disponíveis. Veja os exemplos abaixo.

### Instalação não interativa {#instalação_não_interativa}

Com a linha de comando


```python
msiexec /i FreeCAD<version>.msi
```

a instalação pode ser iniciada programaticamente. Parâmetros adicionais podem ser passados no final da linha de comando, por exemplo


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Interface de usuário limitada {#interface_de_usuário_limitada}

A quantidade de ajustes de operação permitida pelo instalador pode ser controlada com as opções /q:


<div class="mw-translate-fuzzy">

-   /qn - Sem interface
-   /qb - Interface básica - exibir apenas um diálogo de progresso com o botão Cancelar
-   /qb! - Como /qb, mas oculta o botão Cancelar
-   /qr - Interface reduzida - exibir todos os diálogos que não requerem interação do usuário (pular todos os diálogos modais)
-   /qn+ - Como /qn, mas exibe o diálogo \"Completado\" no final


</div>

### Diretório de destino {#diretório_de_destino}

A propriedade TARGETDIR determina o diretório raiz da instalação do FreeCAD. Por exemplo, um drive de instalação diferente pode ser especificado com


```python
TARGETDIR=R:\FreeCAD25
```

O TARGETDIR padrão é \[VolumeWindows\\Programm Files\]FreeCAD.

### Instalação para todos os usuários {#instalação_para_todos_os_usuários}

Adicionando


```python
ALLUSERS=1
```

causa uma instalação utilizável por todos os usuários. Por padrão, uma instalação não interativa (/i) torna o pacote utilizável apenas pelo usuário atual (aquele que realiza a instalação); uma instalação interativa apresenta um diálogo que, por padrão, é \"todos os usuários\", se o usuário que realiza a instalação possuir privilegio de administrador.

### Seleção de recursos {#seleção_de_recursos}

Diversas propriedades permitem a seleção de características a serem instaladas, reinstaladas ou removidas. O conjunto de parâmetros de instalação para o FreeCAD é

-   DefaultFeature - instalar propriamente o 'software', mais as bibliotecas básicas
-   Documentation - instalar a documentação
-   Source code - instala o codigo fonte
-   \... a fazer

Adicionalmente, ALL especifica todas as funcionalidades. Todas as funcionalidades dependem da DefaultFeature, instalar qualquer uma das outras implica a instalação desta. As seguintes propriedades controlam as funcionalidades a serem instaladas ou removidas

-   ADDLOCAL - lista de funcionalidades a serem instaladas na máquina local
-   REMOVE - lista de funcionalidades a serem removidas
-   ADDDEFAULT - lista de recursos adicionados em sua configuração padrão (sendo local para todos os recursos do FreeCAD)
-   REINSTALAR - lista de recursos a serem reinstalados/reparados
-   ADVERTISE - lista de funcionalidades para as quais se vai fazer uma instalação anunciada

Há algumas propriedades adicionais disponíveis; consulte a documentação MSDN para obter detalhes.

Com estas opções, adicionar


```python
ADDLOCAL=Extensions
```

instala o intérprete e regista as extensões, mas não instala mais nada.

## Desinstalação

Com


```python
msiexec /x FreeCAD<version>.msi
```

o FreeCAD pode ser desinstalado. Não é necessário ter o arquivo MSI para realizar a desinstalação; alternativamente, a embalagem ou o código do produto pode ser especificado. Você pode encontrar o código do produto verificando as propriedades do atalho de desinstalação que o FreeCAD instala no menu Iniciar.

## Instalação administrativa {#instalação_administrativa}

Com


```python
msiexec /a FreeCAD<version>.msi
```

uma instalação \"administrativa\" (rede) pode ser iniciada. Os arquivos são desempacotados no diretório de destino (que deve ser um diretório de rede), mas nenhuma outra modificação é feita no sistema local. Além disso, outro arquivo msi (menor) é gerado no diretório de destino, que os clientes podem então usar para realizar uma instalação local (versões futuras poderão oferecer a possibilidade de manter algumas funcionalidades na rede).

Neste momento não há interface gráfico para instalações administrativas, por isso a pasta de destino tem de ser indicada na linha de comandos.

Não há um procedimento de desinstalação específico para uma instalação administrativa - basta apagar a pasta de destino se não houver mais nenhum cliente a usá-la.

## Anúncio

Com


```python
msiexec /jm FreeCAD<version>.msi
```

É possível, em princípio, \"divulgar\" o FreeCAD a uma máquina (ou a um usuário com /ju). Os ícones aparecerão no menu Iniciar e as extensões serão registradas sem que o software seja instalado. O primeiro uso de um recurso levará à sua instalação.

O instalador do FreeCAD atualmente suporta apenas a divulgação de entradas do menu inicial, mas não a divulgação de atalhos.

## Instalação automática em um grupo de máquinas {#instalação_automática_em_um_grupo_de_máquinas}

Com o Windows Group Policy, é possível instalar automaticamente o FreeCAD em um grupo de máquinas. Para fazer isso, execute os seguintes passos:

1.  Logar no controlador de domínio
2.  Copie o arquivo MSI para uma pasta compartilhada com acesso concedido a todas as máquinas alvo.
3.  Abra o snap-in MMC \"Active Directory users and computers\".
4.  Navegue ate o grupo de computadores que necessitam do FreeCAD
5.  Abra Propriedades
6.  Abra Políticas do Grupo
7.  Adicione uma nova política, e edite-a
8.  Em Configuração de Computador/Intalação de Software, escolha Novo/Pacote
9.  Selecione o arquivo MSI através do caminho da rede
10. Opcionalmente, selecione que você deseja que o FreeCAD seja desinstalado se o computador deixar o escopo da política.

Normalmente a propagação das politicas de grupo demora algum tempo - para se certificar que o programa é instalado adequadamente, todas as máquinas devem ser reiniciadas.

## Instalação no Linux usando o Crossover Office {#instalação_no_linux_usando_o_crossover_office}

Você pode instalar a versão Windows do FreeCAD em um sistema Linux usando o *CXOffice 5.0.1*. Execute o *msiexec* a partir da linha de comando do CXOffice. Assumindo que o pacote de instalação esteja no diretório \"software\" no diretório \"Y:\":


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

O FreeCAD está rodando, mas foi relatado que a tela OpenGL não funciona, como com outros programas rodando sob [Wine](wikipedia:Wine_(software).md), ou seja, Google [SketchUp](wikipedia:SketchUp.md).






