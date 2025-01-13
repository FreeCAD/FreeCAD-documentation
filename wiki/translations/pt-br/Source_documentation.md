# Source documentation/pt-br
## Visão geral 

O código-fonte do FreeCAD é comentado para permitir a geração automática de documentação de programação usando o [Doxygen](Doxygen/pt-br.md), um popular sistema de documentação de código-fonte. O Doxygen pode documentar as partes C++ e Python do FreeCAD, resultando em páginas HTML com hiperlinks para cada função e classe documentada.

A documentação está hospedada on-line no [site da API FreeCAD](https://freecad.github.io/SourceDoc/). Por favor, note que esta documentação pode nem sempre estar atualizada; se você precisar de mais detalhes, baixe o código fonte mais recente do FreeCAD e compile a documentação você mesmo. Se você tiver perguntas urgentes sobre o código, por favor, pergunte na seção de desenvolvedores do [fórum FreeCAD](https://forum.freecadweb.org/index.php).

A compilação da documentação da API segue os mesmos passos gerais que a compilação do executável FreeCAD, conforme indicado na página [Compilar no Linux](Compile_on_Linux/pt-br.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Fluxo de trabalho geral para compilar a documentação de programação do FreeCAD. Os pacotes Doxygen e Graphviz devem estar no sistema, assim como o próprio código-fonte do FreeCAD. O CMake configura o sistema para que, com uma única instrução make, a documentação de todo o projeto seja compilada em muitos arquivos HTML com diagramas.*



## Compilar documentação de origem 



### Documentação completa 

Se você tiver o Doxygen instalado, é muito fácil construir a documentação. Também instale o [Graphviz](https://www.graphviz.org/) para ser capaz de produzir diagramas mostrando as relações entre diferentes classes e bibliotecas no código FreeCAD. O Graphviz também é usado pelo [gráfico de dependência](Std_DependencyGraph/pt-br.md) do FreeCAD para mostrar as relações entre diferentes objetos. 
```python
sudo apt install doxygen graphviz
```

Em seguida, siga os mesmos passos que você faria para compilar o FreeCAD, conforme descrito na página de [compilação no Linux](Compile_on_Linux/pt-br.md), e resumido aqui por conveniência.

-   Obtenha o código fonte do FreeCAD e coloque-o em seu próprio diretório `freecad-source`.
-   Crie outro diretório `freecad-build` no qual você compilará o FreeCAD e sua documentação.
-   Configure os códigos-fonte com o `cmake`, certificando-se de indicar o diretório de origem e especifique as opções necessárias para sua compilação.
-   Acione a criação da documentação usando o `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

Enquanto você estiver dentro do diretório de compilação, emita a instrução a seguir para criar somente a documentação. 
```python
make -j$(nproc --ignore=2) DevDoc
``` Como mencionado na [compilação (Acelerada)](Compiling_(Speeding_up)/pt-br.md), a opção `-j` define o número de núcleos de CPU usados para compilação. Os arquivos de documentação resultantes aparecerão no diretório 
```python
freecad-build/doc/SourceDocu/html/
```

O ponto de entrada para a documentação é o arquivo `index.html`, que você pode abrir com um navegador da web: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```

O alvo `DevDoc` irá gerar uma quantidade significativa de dados, cerca de 5 GB de novos arquivos, particularmente devido aos diagramas criados pelo Graphviz.



### Documentação reduzida 

A documentação completa usa cerca de 3Gb de espaço em disco. Uma versão alternativa e menor da documentação, que leva apenas cerca de 600 MB, pode ser gerada com um destino diferente. Esta é a versão exibida no [site da API FreeCAD](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

A documentação no [site da API FreeCAD](https://freecad.github.io/SourceDoc/) é produzida automaticamente a partir do <https://github.com/FreeCAD/SourceDoc> . Qualquer pessoa pode reconstruí-lo e enviar uma solicitação pull:

-   Ramificação do repositório em <https://github.com/FreeCAD/SourceDoc>
-   em sua máquina: clone o código FreeCAD (se você ainda não o fez), crie um diretório de compilação para o doc e clone o repositório SourceDoc acima. Esse SourceDoc será atualizado quando você recriar o documento, e você poderá confirmar & push os resultados depois:


```python
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Acesse a sua cópia do repositório online e crie uma solicitação de pull.

## Outras versões 

[Documentação de desenvolvimento do FreeCAD 0.19](https://iesensor.com/FreeCADDoc/0.19/) construída por [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).



## Integrar documentação Coin3D 

Em sistemas Unix é possível vincular a documentação de origem Coin3D com FreeCAD\'s. Isso permite uma navegação mais fácil e diagramas de herança completos para classes derivadas de Coin.

-   Instale o `libcoin-doc`, `libcoin80-doc`, ou pacote com nome semelhante.
-   Descompacte o arquivo `coin.tar.gz` localizado em `/usr/share/doc/libcoin-doc/html`; Os arquivos podem já estar descompactados em seu sistema.
-   Gere novamente a documentação de origem.

Se você não instalar o pacote de documentação para Coin, os links serão gerados para acessar a documentação on-line no [BitBucket](https://coin3d.bitbucket.io/Coin/). Isso acontecerá se um arquivo de marca Doxygen puder ser baixado no momento da configuração com o `wget`.



## Usando Doxygen 

Consulte a página [Doxygen](Doxygen/pt-br.md) para obter uma explicação extensa sobre como comentar o código-fonte C++ e Python para que ele possa ser processado pelo Doxygen para criar automaticamente a documentação.

Essencialmente, um bloco de comentários, começando com `/**` ou `///` para C++, ou `##` para Python, precisa aparecer antes de cada definição de classe ou função, para que seja captado pelo Doxygen. Muitos [comandos especiais](Doxygen/pt-br#Doxygen_markup.md), que começam com `\` ou `@`, podem ser usados para definir partes do código e formatar a saída. A [sintaxe de Markdown](Doxygen/pt-br#Markdown_support.md) também é entendida dentro do bloco de comentários, o que torna conveniente enfatizar certas partes da documentação. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/pt-br
