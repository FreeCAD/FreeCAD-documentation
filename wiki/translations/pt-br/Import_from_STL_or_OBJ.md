# Import from STL or OBJ/pt-br
{{TutorialInfo
|Topic=Importar STL ou OBJ
|Level=Iniciante
|Time= 30 minutos
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}



## Introdução

Neste tutorial, cobriremos como importar arquivos STL/OBJ no FreeCAD. Como o formato de malha STL/OBJ é sem dimensões, o FreeCAD assumirá, ao importar, que as unidades usadas no modelo são milímetros. Se isso não for verdade, você precisará redimensionar seu modelo no aplicativo em que foi criado (antes de exportá-lo) ou redimensionar seu modelo no FreeCAD após a importação e conversão em um sólido.

## Peça de Exemplo 

Para este tutorial, você pode usar seu próprio arquivo STL ou criar um arquivo de demonstração fazendo o seguinte:

-   Abra o FreeCAD
-   Crie um novo documento
-   Mude para a bancada de trabalho de malha (Mesh)
-   Insira um toro clicando no menu **Malhas** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Sólido regular...**, escolhendo configurações como:
    -   Raio1: 10 mm
    -   Raio2: 2 mm
    -   Amostragem: 50
-   Clique em **Criar** e depois em **Fechar**
-   Salve seu arquivo com **Arquivo** → **Salvar** para obter um arquivo FreeCAD contendo um objeto de malha

Para importar um arquivo STL ou OBJ no FreeCAD, crie um novo documento no FreeCAD e escolha **Arquivo** → **Importar** no menu superior.

## Limpeza e Reparo do Arquivo STL/OBJ para Preparar a Importação 

Basicamente, o FreeCAD importaria qualquer arquivo STL/OBJ. Mas nosso objetivo é ter um sólido que possa ser medido e modificado (adicionar cortes, furos etc). Para uma conversão bem-sucedida de malha para sólido, precisamos garantir que a malha esteja \"selada\" (não tenha buracos) ou não tenha outros erros.

O objetivo do FreeCAD não é ser um bom modelador de malhas; ele é projetado para ser um modelador de sólidos. O FreeCAD possui algumas capacidades para operações de malha na bancada de trabalho de malha (Mesh) e na bancada de trabalho do OpenSCAD (algumas operações exigem que o OpenSCAD esteja instalado e configurado nas preferências do FreeCAD).

Alguns usuários preferem usar software de terceiros para limpar e reparar malhas, por exemplo:

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - gratuito para uso pessoal (reparo automático de malha disponível)
-   [Meshlab](http://meshlab.sourceforge.net/) (Windows/Linux/Mac) - Código Aberto

Neste tutorial, usaremos a bancada de trabalho de malha dentro do FreeCAD para limpar/reparar/verificar a malha do nosso arquivo de exemplo.

### Teste e Reparo Automáticos 

-   Abra o FreeCAD e o arquivo FreeCAD de exemplo que contém o objeto de malha
-   Mude para a bancada de trabalho Mesh
-   Certifique-se de que seu objeto de malha esteja selecionado na visualização de árvore
-   Escolha **Malhas** → **Analisar** → **Analisar e consertar malha...** no menu superior
-   Certifique-se de que o menu suspenso no canto superior direito exiba o nome do seu objeto de malha
-   Com o último ponto na lista lendo \"Todos os testes acima juntos\", clique em **Analisar**
-   Os textos ao lado das caixas de seleção mudarão para refletir os resultados dos diferentes testes
-   Se erros tiverem sido detectados, as caixas de seleção correspondentes serão marcadas e você poderá selecionar **Reparar**
-   Escolha **Fechar** para fechar o menu

### Harmonização de Normais 

A harmonização de normais de um objeto de malha pode ser feita da seguinte forma:

-   Selecione o objeto de malha na visualização em árvore.
-   Escolha **Malhas** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Harmonizar normais** no menu superior.

Dica: Ao selecionar o objeto de malha na visualização em árvore, vá para a guia de visualização na visualização de propriedades e altere \"Iluminação\" de \"Dois Lados\" para \"Um Lado\" para identificar triângulos com normais invertidas. Se as normais apontarem para dentro da malha, o triângulo será exibido em preto.

### Fechando Buracos 

Você também pode fechar manualmente buracos em seu objeto de malha da seguinte maneira:

-   Selecionando seu objeto de malha na visualização de árvore
-   Escolha **Malhas** → **Preencher buracos...** no menu superior
-   Especifique o número máximo de arestas a serem preenchidas (3 é o padrão)
-   Como STL e OBJ são malhas compostas por triângulos, o número padrão de arestas deve ser suficiente

Outro método para fechar manualmente buracos em seu objeto de malha seria:

-   Selecionando seu objeto de malha na visualização de árvore
-   Escolha **Malhas** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Fechar furo** no menu superior
-   Selecione uma das arestas do buraco no objeto de malha na visualização 3D
-   Clique com o botão direito na visualização 3D e escolha **Sair do modo de preenchimento de buraco** para sair do comando

## Conversão de Malha para Sólido 

-   Mude para a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Bancada de Trabalho Part](Part_Workbench/pt-br.md)
-   Certifique-se de que seu objeto de malha esteja selecionado na visualização de árvore; caso contrário, selecione-o
-   Escolha **Part** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Criar uma forma a partir de uma malha...** no menu superior
-   Especifique a tolerância para a costura da forma (0,1 é o padrão)
-   Um novo objeto será criado na visualização de árvore (com um ícone de forma azul, em vez de um ícone de malha verde)
-   Selecione o objeto recém-criado na visualização de árvore
-   Escolha **Part** → **Criar uma cópia** → **<img src="images/Part_RefineShape.svg" width=32px> Refinar forma** no menu superior
-   Um novo objeto será criado na visualização de árvore e o anterior ficará invisível
-   Selecione o objeto recém-criado na visualização de árvore
-   Escolha **Part** → **Converter em sólido** no menu superior
-   Um novo objeto será criado na visualização de árvore, com \"(Sólido)\" em seu nome, indicando que é um sólido

Como o sólido criado não possui histórico nem recursos editáveis (como uma cópia simples no FreeCAD), você pode excluir todos os objetos anteriores na visualização de árvore. Isso manteria o tamanho do seu arquivo pequeno\...

## Links

-   [Exportar STL ou OBJ](Export_to_STL_or_OBJ/pt-br.md)
-   [Importar Exportar](Import_Export/pt-br.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/pt-br
