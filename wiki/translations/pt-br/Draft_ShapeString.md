---
 GuiCommand:  
   Name: Draft ShapeString  
   MenuLocation: Drafting , Forma a partir de texto<br>Anotação , Forma a partir de texto  
   Workbenches: Draft_Workbench/pt-br, BIM_Workbench/pt-br  
   Shortcut:   
   Version: 0.14  
   SeeAlso: Draft_Text/pt-br, Draft_Label/pt-br, Part_Extrude/pt-br  
---

# Draft ShapeString/pt-br



## Descrição

O comando <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft ShapeString** gera uma forma composta baseada em uma sequência de texto. Essa forma pode ser utilizada para criar letras em 3D utilizando o comando [Part Extrude](Part_Extrude/pt-br.md).

O comando Draft ShapeString não é adequado para criar anotações de texto padrão. Para essa finalidade, utilize os comandos [Draft Text](Draft_Text/pt-br.md) ou [Draft Label](Draft_Label/pt-br.md).

![](images/Draft_ShapeString_Example400.png ) 
*Um único ponto é necessário para posicionar o ShapeString*



## Utilização

Para usuários do Windows: por favor, leia primeiro o parágrafo [Seleção de arquivos de fonte no Windows](#Font_file_selection_on_Windows/pt-br.md).

1.  Existem várias maneiras de invocar o comando:
    -   Pressione o **<img src="images/Draft_ShapeString.svg" width=16px> [Forma a partir de texto](Draft_ShapeString/pt-br.md)** botão.
    -   [Draft](Draft_Workbench/pt-br.md): Selecione a opção **Desenho → <img src="images/Draft_ShapeString.svg" width=16px> Forma a partir de texto** no menu.
    -   [BIM](BIM_Workbench/pt-br.md): Selecione a opção **Anotação → <img src="images/Draft_ShapeString.svg" width=16px> Forma a partir de texto** no menu.
2.  O painel **ShapeString** será aberto.
3.  Clique em um ponto na [vista 3D](3D_view/pt-br.md) ou insira as coordenadas.
4.  Opcionalmente, pressione o **Redefinir Ponto** botão para redefinir o ponto para a origem.
5.  Insira uma **String** (texto).
6.  Especifique a **Altura**.
7.  Para selecionar uma fonte, escolha uma das opções:
    -   Insira um caminho de arquivo no campo **Arquivo de fonte**.
    -   Pressione o **...** botão e selecione um arquivo.
8.  Pressione o **OK** botão para finalizar o comando.
9.  Opcionalmente, altere a **Justificação** do ShapeString. Consulte [Propriedades](#Properties/pt-br.md).



## Opções

#\* Pressione a tecla **Esc** ou o botão **Cancelar** para abortar o comando.



## Caminho relativo da fonte 


{{Version/pt-br|1.1}}

É possível especificar um caminho relativo para o arquivo de fonte. Para isso, o documento do FreeCAD deve ter sido salvo pelo menos uma vez.

Alguns exemplos:

-    **./SomeFont.ttf**: O arquivo de fonte está no mesmo diretório que o documento.

-    **./MyDirectory/SomeFont.ttf**: O arquivo de fonte está no subdiretório **MyDirectory** dentro do diretório do documento.

-    **../SomeFont.ttf**: O arquivo de fonte está no diretório pai do diretório do documento.



## Seleção de arquivo de fonte no Windows 

No Windows, o acesso à pasta padrão de fontes é restrito. Isso afeta a seleção de arquivos de fonte para ShapeStrings. Há três casos no FreeCAD em que é possível especificar um arquivo de fonte para ShapeStrings: no painel de tarefas ShapeString, ao alterar a propriedade **Arquivo de Fonte** de um ShapeString e ao especificar o arquivo de fonte padrão nas [Preferências da Bancada Draft](Draft_Preferences/pt-br#Texts_and_dimensions.md).

1.  Pressionar o botão **...** e selecionar um arquivo da pasta padrão de fontes do Windows não é possível ao usar a caixa de diálogo de arquivo nativa. Existem algumas soluções alternativas:
    -   Certifique-se de que **DontUseNativeFontDialog** está configurado como {{True}}, que é o valor padrão para essa preferência. Isso abrirá uma caixa de diálogo de arquivo não nativa ao pressionar o botão **...** no painel de tarefas ShapeString. Com essa caixa de diálogo, é possível acessar a pasta padrão de fontes do Windows.
    -   Altere **DontUseNativeDialog** para {{True}}. Isso instruirá o FreeCAD a sempre usar a caixa de diálogo de arquivo não nativa.
    -   Especifique o arquivo de fonte diretamente no campo de entrada. Você pode digitar o caminho completo ou copiar e colar o caminho do Explorador de Arquivos do Windows. Outra opção é inserir {{Value|C:\}}; uma lista suspensa aparecerá. Selecione {{Value|Windows}} da lista, adicione {{Value|\F}}, selecione {{Value|Fonts}} da nova lista suspensa, adicione {{Value|\}} e insira as primeiras letras do arquivo de fonte para selecioná-lo na lista suspensa.
    -   Crie uma pasta personalizada para seus arquivos de fonte.

Consulte o parágrafo [Preferências](#Preferences/pt-br.md) abaixo para localizar as preferências mencionadas.



## Notas

#\* Um Draft ShapeString pode ser editado clicando duas vezes nele na [Vista em Árvore](Tree_view/pt-br.md).

#\* As fontes suportadas incluem TrueType (**.ttf**), OpenType (**.otf**) e Type 1 (**.pfb**).

#\* O comando é restrito a textos da esquerda para a direita. Textos da direita para a esquerda e de cima para baixo não são suportados.

#\* Alturas de texto muito pequenas podem resultar em formas de caracteres deformadas devido à perda de detalhes no escalonamento.

#\* Fontes podem gerar geometria problemática, pois os contornos das fontes podem se sobrepor ou apresentar pequenos espaços. Essas condições são consideradas erros em fios usados para definir faces.

#\* Draft ShapeStrings também podem ser criados com a [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/pt-br.md).

#\* Para criar Draft ShapeStrings dispostos em um formato circular, utilize a [Macro FCCircularText](Macro_FCCircularText/pt-br.md).



## Tutoriais

1.  [Tutorial de Draft ShapeString](Draft_ShapeString_tutorial/pt-br.md): extruda um ShapeString, posicione-o no espaço 3D e crie uma gravação em outro corpo.
2.  [Como usar ShapeStrings no PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)



## Preferências

1.  Veja também: [Editor de Preferências](Preferences_Editor/pt-br.md), [Preferências da Bancada Draft](Draft_Preferences/pt-br.md) e [Parâmetro de Diálogo Padrão](Std_DlgParameter/pt-br.md).

-   O arquivo de fonte padrão pode ser alterado nas preferências: **Editar → Preferências... → Draft → Textos e dimensões → Arquivo de fonte padrão para ShapeString**.
-   Para usuários do Windows:

 ** Defina **Ferramentas → Editar parâmetros... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** como {{True}} para usar o seletor de arquivos não nativo ao escolher um arquivo de fonte no painel de tarefas do ShapeString.  
 ** Alternativamente, defina **Ferramentas → Editar parâmetros... → BaseApp → Preferences → Dialog → DontUseNativeDialog** como {{True}} para sempre usar o seletor de arquivos não nativo.



## Propriedades

Veja também: [Editor de Propriedades](Property_editor/pt-br.md).

1.  Um objeto Draft ShapeString é derivado de um [Part Part2DObject](Part_Part2DObject/pt-br.md) e herda todas as suas propriedades. Ele também possui as seguintes propriedades adicionais:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Font File|File**: Nome do arquivo da fonte.

-    **Fuse|Bool**: Funde as faces caso haja sobreposição entre elas, geralmente não é necessário (pode ser muito lento). Ignorado se **Make Face** estiver `False`. <small>(v1.0)</small> 

-    **Justification|Enumeration**: Alinhamento horizontal e vertical. Opções: {{value|Top-Left}}, {{value|Top-Center}}, {{value|Top-Right}}, {{value|Middle-Left}}, {{value|Middle-Center}}, {{value|Middle-Right}}, {{value|Bottom-Left}}, {{value|Bottom-Center}}, {{value|Bottom-Right}}. <small>(v1.0)</small> 

-    **Justification Reference|Enumeration**: Referência de altura usada para o alinhamento. Opções: {{value|Cap Height}}, {{value|Shape Height}}. A altura da forma depende dos caracteres no **String**. <small>(v1.0)</small> 

-    **Keep Left Margin|Bool**: Mantém a margem esquerda e os espaços em branco iniciais quando o alinhamento é à esquerda. <small>(v1.0)</small> 

-    **Make Face|Bool**: Preenche as letras com faces.

-    **Oblique Angle|Angle**: Ângulo de inclinação. Deve estar no intervalo de -80° a +80°. <small>(v1.0)</small> 

-    **Scale To Size|Bool**: Ajusta para garantir que a altura do topo das letras seja igual ao tamanho definido. Se configurado como `False`, dependendo da fonte, a altura do topo das letras pode não corresponder exatamente ao **Size**. <small>(v1.0)</small> 

-    **Size|Length**: Altura do texto.

-    **String|String**: Sequência de texto. Um ShapeString só pode exibir uma única linha de texto.

-    **Tracking|Distance**: Espaçamento entre caracteres. O tipo dessa propriedade foi atualizado (<small>(v1.0)</small> ).


</div>

<img alt="" src=images/Draft_ShapeString_Justification.png  style="width:200px;"> 
*A altura do retângulo vermelho (linha contínua) é igual à altura do topo das letras (cap height).<br>  
A altura do retângulo verde (linha tracejada) é igual à altura da forma (shape height).<br>  
Os cantos, os pontos médios das bordas e o centro dos retângulos<br>  
correspondem às 9 opções de alinhamento: de Superior-Esquerdo a Inferior-Direito.*

## Scripting

Veja também: [Documentação de API Gerada Automaticamente](https://freecad.github.io/SourceDoc/) e [Noções Básicas de Script no FreeCAD](FreeCAD_Scripting_Basics/pt-br.md).

Para criar um \*\*Draft ShapeString\*\*, utilize o método `make_shapestring` (<small>(v0.19)</small> ) do módulo \*\*Draft\*\*. Este método substitui o método obsoleto `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Cria uma forma composta `shapestring` usando a `String` especificada e o caminho completo de um `FontFile` compatível.

-    `Size`é a altura do texto resultante em milímetros.

-    `Tracking`é o espaçamento entre os caracteres em milímetros.

A posição do \*\*ShapeString\*\* pode ser alterada sobrescrevendo seu atributo `Placement`, ou individualmente sobrescrevendo os atributos `Placement.Base` e `Placement.Rotation`.

Exemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/pt-br
