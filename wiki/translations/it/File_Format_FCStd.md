# File Format FCStd/it
## Introduzione

Il **Formato nativo dei file di FreeCAD** (FreeCAD Standard file format) **.FCStd** è il formato principale dei file di FreeCAD. Si tratta di un formato composto che supporta la compressione e l\'incorporamento di diversi tipi di dati.



## Contenuto di un file .FCStd 

FCStd è un [file zip standard contenente uno o più file in una struttura specifica](#Struttura_tipica.md). Come tale, è possibile decomprimere un file **.FCStd** utilizzando un normale strumento di decompressione zip, mentre invece si deve stare attenti a impacchettare il contenuto di un file **.FCStd**. FreeCAD contiene una \"Project Utility\" per \'ripacchettare\' i file **.FCStd**, il suo uso è descritto nel paragrafo sootttostante [Modificare il codice sorgente del file .FCStd](#Modificare_il_codice_sorgente_del_file_.FCStd.md).

### Document.xml

Questo è il file **.xml** principale che descrive tutti gli oggetti contenuti in un documento di FreeCAD. Descrive solo la definizione geometrica e parametrica degli oggetti, ma non la loro rappresentazione visiva. Se FreeCAD viene eseguito in modalità console (senza GUI), viene utilizzato solo questo **Document.xml**.



#### Esempio di Document.xml 


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

Questa è la controparte GUI del file **Document.xml**. Per ogni oggetto descritto nel **Document.xml**, c\'è un corrispondente oggetto in **GuiDocument.xml** il quale descrive la rappresentazione visiva di quell\'oggetto (colore, larghezza di linea, ecc.)

### Thumbnails/thumbnail.png

Si tratta di un\'immagine di anteprima di 128x128 pixel del documento, che è uno screenshot della vista 3D in fase di salvataggio. Le miniature vengono generate solo quando, nelle preferenze di FreeCAD, è attivata la corrispondente opzione.

### \*.brep

Queste sono le forme [B-rep](wikipedia_Boundary_representation.md) di tutti gli oggetti che hanno una forma Parte in **Document.xml**. Ogni oggetto, anche se è parametrico, ha la sua forma memorizzata in un file **.brep** individuale, in modo che si può accedere ai suoi componenti senza la necessità di ricalcolarne la forma.

### \*.svg

Questi sono i file svg modello utilizzati nelle pagine di [TechDraw](TechDraw_Workbench/it.md).



### Struttura tipica 

Struttura di un tipico file **.FCStd**. L\'estensione può essere modificata in **.zip** per esplorarla come una normale directory. **Document.xml** e **GuiDocument.xml** si trovano nella radice dell\'archivio, insieme a tutti i file **.brp** (BREP). Una sottodirectory può contenere la miniatura e un\'altra i modelli SVG utilizzati da [TechDraw](TechDraw_Workbench/it.md).

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



## Incorporare altri file 

Per incorporare altri tipi di file all\'interno di un file FCStd, bisogna prima creare un [oggetto da script](Scripted_objects/it.md) dalla [console Python](Python_console/it.md) e assegnargli una proprietà `App::PropertyFileIncluded`.

Quindi nell\'[editor delle proprietà](Property_editor/it.md) si può andare alla proprietà aggiunta e scegliere un file nel computer. Una volta salvato il file FCStd, il file assegnato alla proprietà **PropertyFileIncluded** verrà compresso all\'interno di `.FCStd`. Quando il documento viene ripristinato, lo stesso file verrà ripristinato con la proprietà **PropertyFileIncluded**.


```python
custom_obj = App.ActiveDocument.addObject("App::FeaturePython", "CustomObject")
custom_obj.addProperty("App::PropertyFileIncluded", "AttachedFile")
```

Vedere nel forum la discussione [PDF inside the project](https://forum.freecadweb.org/viewtopic.php?t=38201).



## Modificare il codice sorgente del file .FCStd 

-   Vedere [Utilità di progetto](Std_ProjectUtil/it.md).



## Altri link 

Un utile programma convertitore: [ImageConv](ImageConv/it.md).



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/it
