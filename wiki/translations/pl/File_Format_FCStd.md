# File Format FCStd/pl
{{TOCright}}

## Informacje ogólne 

Standardowy format pliku FreeCAD *FreeCAD Standard file format* ({{FileName|.FCStd}}) jest głównym formatem pliku FreeCAD. Zawartość pliku jest złożona, obsługuje kompresję i osadzanie różnych rodzajów danych.

## Zawartość plików .FCStd 

FCStd jest [standardowym plikiem zip zawierającym jeden lub więcej plików](#Contents.md) o [specyficznej strukturze](#structure.md). Jako takie, możliwe jest rozpakowanie pliku {{FileName|.FCStd}} przy użyciu zwykłego narzędzia dekompresującego **zip**, ale należy zachować ostrożność podczas pakowania zawartości pliku {{FileName|.FCStd}}. FreeCAD zawiera **Project Utility** do ponownego pakowania plików {{FileName|.FCStd}}, jego użycie jest opisane w [Zmień źródło pliku .FCStd](#Change_the_source_of_the_file_.FCStd.md) poniżej.

### Document.xml

Jest to główny plik {{FileName|.xml}} opisujący wszystkie obiekty wewnątrz dokumentu FreeCAD, czyli tylko geometryczną i parametryczną definicję obiektów, a nie ich wizualną reprezentację. Jeżeli FreeCAD jest uruchomiony w trybie konsolowym *(bez GUI)*, to tylko ten {{FileName|Dokument.xml}} będzie użyty.

#### Przykład Dokumentu.xml 


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

Jest to odpowiednik GUI pliku {{FileName|Document.xml}}. Dla każdego obiektu opisanego w pliku {{FileName|Document.xml}} znajduje się jeden odpowiadający mu obiekt w pliku {{FileName|GuiDocument.xml}}, opisujący wizualną reprezentację tego obiektu *(kolor, szerokość linii itd.)*.

### Miniatury/thumbnail.png

Jest to miniatura przedstawiająca obraz dokumentu o wymiarach 128x128 pikseli, która jest zrzutem ekranu z widoku 3D w wybranym widoku z perspektywy czasu. Miniaturki są generowane tylko wtedy, gdy jest włączona odpowiednia opcja w preferencjach programu FreeCAD.

### \*.brep

Są to kształty [B-rep](wikipedia_Boundary_representation.md) wszystkich obiektów, które mają postać Part w {{FileName|Document.xml}}. Każdy obiekt, nawet jeśli jest parametryczny, ma swój kształt przechowywany jako indywidualny plik {{FileName|.brep}}, więc może być dostępny dla komponentów bez potrzeby ponownego obliczania kształtu.

### \*.svg

W folderze Templates przechowywane są pliki SVG szablonów używane na stronach [Rysunek Techniczny](TechDraw_Workbench/pl.md).

### Struktura

Struktura typowego pliku {{FileName|FCStd}}: Rozszerzenie można zmienić na {{FileName|.zip}}, aby eksplorować plik jak zwykły katalog. Pliki {{FileName|Document.xml}} i {{FileName|GuiDocument.xml}} znajdują się w katalogu głównym archiwum wraz z dowolną liczbą plików {{FileName|.brp}} *(BREP)*. Jeden podkatalog może zawierać miniaturę, a drugi szablony SVG używane przez Środowisko pracy [TechDraw](TechDraw_Workbench/pl.md).

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

## Osadzanie innych plików 

Aby osadzić inne typy plików w pliku FCStd, musisz najpierw utworzyć plik typu [obiekt skryptowy](Scripted_objects/pl.md) z [konsoli Python](Python_console/pl.md), i nadaj mu właściwość `App::PropertyFileIncluded`

Następnie w [edytorze właściwości](Property_editor/pl.md) możesz przejść do dodanej właściwości i wybrać plik na komputerze. Po zapisaniu pliku FCStd plik przypisany do właściwości {{PropertyData/pl|DataPropertyFileIncluded}} zostanie umieszczony w pliku `.FCStd`. Gdy dokument zostanie przywrócony, ten sam plik zostanie przywrócony z właściwością {{PropertyData/pl|PropertyFileIncluded}}.


```python
custom_obj = App.ActiveDocument.addObject("App::FeaturePython", "CustomObject")
custom_obj.addProperty("App::PropertyFileIncluded", "AttachedFile")
```

Zobacz wątek na forum, [PDF wewnątrz projektu](https://forum.freecadweb.org/viewtopic.php?t=38201).

## Zmień źródło pliku .FCStd 

-   Zobacz [Std ProjectUtil](Std_ProjectUtil.md).

## Pozostałe

-   Narzędzie konwertujące pliki [ImageConv](ImageConv.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/pl
