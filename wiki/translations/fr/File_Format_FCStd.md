# File Format FCStd/fr
## Présentation

Le **format de fichier** (**.FCStd**) est le format de fichier principal de FreeCAD. Il s'agit d'un format conteneur prenant en charge la compression et l'incorporation de différents types de données.



## Contenu d\'un fichier .FCStd 

FCStd est un [fichier zip standard contenant un ou plusieurs fichiers](#Structure_typique.md) dans une [structure spécifique](#Structure.md). En tant que tel, il est possible de décompresser un fichier **.FCStd** à l\'aide d\'un outil de décompression zip, mais des précautions doivent être prises lors de la reconstruction du fichier **.FCStd**. FreeCAD possède un \"Utilitaire de projet\" pour reconstruire les fichiers **.FCStd**, dont l\'utilisation est décrite dans [Modifier le code source du fichier .FCStd](#Modifier_le_code_source_du_fichier_.FCStd.md) ci-dessous.

### Document.xml

C\'est le fichier **.xml** principal, décrivant tous les objets à l\'intérieur d\'un document FreeCAD, c\'est-à-dire la définition géométrique et les paramètres des objets, mais pas leur représentation visuelle. Si FreeCAD est exécuté en mode console (sans l\'interface graphique), c\'est ce **Document.xml** qui sera utilisé.



#### Exemple de Document.xml 


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

Il s\'agit de l\'équivalent **GUI** (Graphique User Interface) du fichier **Document.xml**. Pour chaque objet décrit dans le **Document.xml**, il y a un objet correspondant dans **GuiDocument.xml**, qui décrit la représentation visuelle de l\'objet (couleur, largeur, etc.).



### Thumbnails/thumbnail.png

Il s\'agit d\'une image miniature (thumbnail) du document de 128 x 128 pixels, qui représente une capture d\'écran de la vue 3D pour gagner du temps. Les vignettes sont uniquement générées, si l\'option correspondante est activée dans les préférences de FreeCAD.



### \*.brep

Ce sont les formes [B-Rep](wikipedia:fr:B-Rep.md) de tous les objets, qui ont une forme dans le **Document.xml**. Même s\'il est paramétrique, chaque objet a sa forme stockée comme un fichier individuel **.brep**, on y accède donc par des composants sans devoir recalculer la forme.

### \*.svg

Ce sont les fichiers svg modèles utilisés dans les pages de [TechDraw](TechDraw_Workbench/fr.md).



### Structure typique 

Structure typique d\'un fichier **.FCStd**. L\'extension peut être modifiée en **.zip** pour l\'explorer comme un répertoire normal. Les **Document.xml** et **GuiDocument.xml** sont à la racine de l\'archive, avec un nombre illimité de fichiers **.brp** (B-REP). Un sous-répertoire peut contenir la miniature et un autre les modèles SVG utilisés par [TechDraw](TechDraw_Workbench/fr.md).

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



## Incorporation d\'autres fichiers 

Pour incorporer d\'autres types de fichiers dans un fichier FCStd, vous devez d\'abord créer un [objet scripté](Scripted_objects/fr.md) à partir de la [console Python](Python_console/fr.md) et lui donner une propriété `App::PropertyFileIncluded`.

Ensuite, dans l\'[éditeur de propriétés](Property_editor/fr.md), vous pouvez accéder à la propriété ajoutée et choisir un fichier sur l\'ordinateur. Une fois le fichier FCStd enregistré, le fichier affecté à la propriété {{PropertyData/fr|PropertyFileIncluded}} sera mis dans le `.FCStd`. Lorsque le document est restauré, le même fichier sera restauré avec la propriété {{PropertyData/fr|PropertyFileIncluded}}.


```python
custom_obj = App.ActiveDocument.addObject("App::FeaturePython", "CustomObject")
custom_obj.addProperty("App::PropertyFileIncluded", "AttachedFile")
```

Voir le fil du forum [PDF inside the project](https://forum.freecadweb.org/viewtopic.php?t=38201).



## Modifier le code source du fichier .FCStd 

-   Voir [Std Utilitaire de projet](Std_ProjectUtil/fr.md).



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/fr
