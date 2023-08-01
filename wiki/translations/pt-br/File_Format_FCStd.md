# File Format FCStd/pt-br
{{TOCright}}



## Visão geral 

O formato de arquivo **FreeCAD Standard** (**.FCStd**) é o principal formato de arquivo do FreeCAD. É um formato composto, que suporta a compactação e a incorporação de diferentes tipos de dados.



## Parte interna dos arquivos .FCStd 

FCStd é um [arquivo zip padrão que contém um ou mais a quivos em uma estrutura específica](#Estrutura_típica.md). Dessa forma, é possível descompactar um arquivo **.FCStd** usando uma ferramenta de descompactação zip comum, mas é preciso ter cuidado ao compactar o conteúdo de um arquivo **.FCStd**. O FreeCAD contém um \"Utilitário de Projeto\" para reempacotar arquivos **.FCStd**; seu uso é descrito em [Alterar a origem do arquivo .FCStd](#Alterar_a_origem_do_arquivo_.FCStd.md) abaixo.

### Document.xml

Este é o arquivo principal **.xml** que descreve todos os objetos em um documento do FreeCAD, ou seja, apenas a definição geométrica e paramétrica dos objetos, não sua representação visual. Se o FreeCAD for executado no modo console (sem a GUI), apenas esse **Document.xml** será usado.



#### Exemplo de Documento.xml 


{{Code|lang=xml|code=
 <?xml version='1.0' encoding='utf-8'?>
 
 <Document SchemaVersion="4">
    <Properties Count="9">
       <Property name="Comment" type="App::PropertyString">
          <String value=""/>
       </Property>
       <Property name="Company" type="App::PropertyString">
          <String value=""/>
       </Property>
       <Property name="CreatedBy" type="App::PropertyString">
          <String value=""/>
       </Property>
       <Property name="CreationDate" type="App::PropertyString">
          <String value="Fri Jan 29 15:14:38 2010 "/>
       </Property>
       <Property name="FileName" type="App::PropertyString">
          <String value="/tmp/test.FCStd"/>
       </Property>
       <Property name="Id" type="App::PropertyString">
          <String value="201b746f-a1ed-4297-bf3d-65d5ec11abe0"/>
       </Property>
       <Property name="Label" type="App::PropertyString">
          <String value="names"/>
       </Property>
       <Property name="LastModifiedBy" type="App::PropertyString">
          <String value=""/>
       </Property>
       <Property name="LastModifiedDate" type="App::PropertyString">
          <String value="Fri Jan 29 15:15:21 2010 "/>
       </Property>
    </Properties>
    <Objects Count="2">
       <Object type="Mesh::Cube" name="Cube" />
       <Object type="Part::Box" name="Box" />
    </Objects>
    <ObjectData Count="2">
       <Object name="Cube">
          <Properties Count="7">
             <Property name="Height" type="App::PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
             <Property name="Label" type="App::PropertyString">
                <String value="Cube"/>
             </Property>
             <Property name="Length" type="App::PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
             <Property name="Mesh" type="Mesh::PropertyMeshKernel">
                <Mesh file="MeshKernel.bms"/>
             </Property>
             <Property name="Placement" type="App::PropertyPlacement">
                <PropertyPlacement Px="0" Py="0" Pz="0" Q0="0" Q1="0" Q2="0" Q3="1"/>
             </Property>
             <Property name="Pos" type="App::PropertyPlacementLink">
                <Link value=""/>
             </Property>
             <Property name="Width" type="App::PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
          </Properties>
       </Object>
       <Object name="Box">
          <Properties Count="7">
             <Property name="Height" type="App::PropertyLength">
                <Float value="10"/>
             </Property>
             <Property name="Label" type="App::PropertyString">
                <String value="Box2"/>
             </Property>
             <Property name="Length" type="App::PropertyLength">
                <Float value="10"/>
             </Property>
             <Property name="Placement" type="App::PropertyPlacement">
                <PropertyPlacement Px="0" Py="0" Pz="0" Q0="0" Q1="0" Q2="0" Q3="1"/>
             </Property>
             <Property name="Pos" type="App::PropertyPlacementLink">
                <Link value=""/>
             </Property>
             <Property name="Shape" type="Part::PropertyPartShape">
                <Part file="PartShape.brp2"/>
             </Property>
             <Property name="Width" type="App::PropertyLength">
                <Float value="10"/>
             </Property>
          </Properties>
       </Object>
    </ObjectData>
 </Document>
}}

### GuiDocument.xml

Essa é a contraparte da GUI (Interface gráfica do usuário) do arquivo **Document.xml**. Para cada objeto descrito em **Document.xml**, há um objeto correspondente em **GuiDocument.xml**, que descreve a representação visual desse objeto (cor, largura da linha etc.).

### Thumbnails/thumbnail.png

Esta é uma imagem em miniatura de 128x128 pixels do documento, que é uma captura de tela da visualização 3D no momento do salvamento. As miniaturas são geradas somente se a opção correspondente estiver ativada nas preferências do FreeCAD.

### \*.brep

Essas são as formas [B-rep](wikipedia_Boundary_representation.md) de todos os objetos que têm uma forma de peça no **Document.xml**. Cada objeto, mesmo que seja paramétrico, tem sua forma armazenada como um arquivo **.brep** individual, de modo que possa ser acessado por componentes sem a necessidade de recalcular a forma.

### \*.svg

Esses são os arquivos svg de modelo usados nas páginas do [TechDraw](TechDraw_Workbench/pt-br.md).



### Estrutura típica 

Estrutura de um arquivo **.FCStd** típico. A extensão pode ser alterada para **.zip** para explorá-lo como um diretório normal. Os arquivos **Document.xml** e **GuiDocument.xml** estão na raiz do arquivo, juntamente com qualquer número de arquivos **.brp** (BREP). Um subdiretório pode conter a miniatura e outro os modelos SVG usados pelo [TechDraw](TechDraw_Workbench/pt-br.md).

    File.FCStd (File.zip)
      |
      |--thumbnails/
      |  |
      |  :--Thumbnail.png
      |
      :--Document.xml
      :--GuiDocument.xml
      :--Shape1.brp
      :--Shape2.brp
      :--MyPage.svg
      :--etc.



## Incorporação de outros arquivos 

Para incorporar outros tipos de arquivo em um arquivo FCStd, primeiro crie um [Objetos com Script](Scripted_objects/pt-br.md) no [console Python](Python_console/pt-br.md) e dê a ele uma propriedade `App::PropertyFileIncluded`.

Em seguida, no [editor de propriedades](Property_editor/pt-br.md), você pode ir até a propriedade adicionada e escolher um arquivo no computador. Depois que o arquivo FCStd for salvo, o arquivo atribuído à propriedade **PropertyFileIncluded** será compactado dentro do `.FCStd`. Quando o documento for restaurado, o mesmo arquivo será restaurado com a propriedade **PropertyFileIncluded**.


```python
custom_obj = App.ActiveDocument.addObject("App::FeaturePython", "CustomObject")
custom_obj.addProperty("App::PropertyFileIncluded", "AttachedFile")
```

Consulte o tópico do fórum, [PDF inside the project](https://forum.freecadweb.org/viewtopic.php?t=38201).



## Alterar a origem do arquivo .FCStd 

-   Consulte [Std ProjectUtil](Std_ProjectUtil/pt-br.md).



## Outros

-   Um utilitário conversor de arquivos [ImageConv](ImageConv/pt-br.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/pt-br
