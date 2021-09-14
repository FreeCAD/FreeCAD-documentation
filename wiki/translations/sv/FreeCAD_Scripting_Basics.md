# FreeCAD Scripting Basics/sv




{{TOCright}}


<div class="mw-translate-fuzzy">

## Python skript i FreeCAD 

FreeCAD är byggt från grunden att helt och hållet kunna kontrolleras av python skript. Nästan alla delar av FreeCAD som gränssnittet, sceninnehållet, och även representationen av detta innehåll i 3d vyerna kan kommas åt från den inbyggda pythontolken eller från dina egna skript. Resultatet av detta är att FreeCAD troligen är en av de mest anpassningsbara konstruktionsapplikationerna som finns idag.


</div>

FreeCAD is built from scratch to be totally controlled by Python scripts. Almost all parts of FreeCAD, such as the interface, the scene contents, and even the representation of this content in the 3D views, are accessible from the built-in Python interpreter or from your own scripts. As a result, FreeCAD is probably one of the most deeply customizable engineering applications available today.


<div class="mw-translate-fuzzy">

Om du inte kan något om python, så rekommenderar vi att du letar efter övningar på internet, och tar en snabbtitt på dess struktur. Python är ett mycket lättlärt språk, speciellt eftersom det kan köras inuti en tolk, där allt från enkla kommandon till kompletta program kan köras direkt, utan något bahov för kompilering. FreeCAD har en inbyggd tolk. Om du inte ser fönstret \"Rapportvy\", som visas nedan, så kan du få fram den genom att klicka på Vy -\> Vyer -\> Rapportvy.


</div>


<div class="mw-translate-fuzzy">

### Tolken

Från tolken så har du åtkomst till alla dina systeminstallerade pythonmoduler, såväl som FreeCAD\'s inbyggda moduler, och alla extra FreeCAD moduler som du installerat senare. Skärmdumpen nedan visar python tolken:


</div>

From the interpreter, you can access all your system-installed Python modules, as well as the built-in FreeCAD modules, and all additional FreeCAD modules you installed later. The screenshot below shows the Python interpreter:

![FreeCAD python tolken](images/screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

Från tolken kan du köra pythonkod, lista igenom tillgängliga klasser och funktioner. FreeCAD erbjuder en väldigt smidig klasslistare för utforskning av din nya FreeCAD värld: När du skriver namnet på en känd klass följt av en punkt (vilket innebär att du vill addera något från den klassen), så öppnas en klasslistare, där du kan navigera mellan tillgängliga underklasser och metoder. När du väljer något, så visas en associerad hjälptext (om den finns):


</div>

![FreeCAD klasslistare](images/screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

Så, starta här genom att skriva **App.** eller **Gui.** och se vad som händer. Ett annat mer allmänt python-sätt att utforska modul- och klassinnehåll är att använda print dir() kommandot. Till exempel, genom att skriva **print dir()** så kommer alla moduler som för närvarande är laddade i FreeCAD att listas. **print dir(App)** kommer att visa dig allt inuti App modulen, etc.


</div>


<div class="mw-translate-fuzzy">

En annan användbar egenskap hos tolken är möjligheten att backa i kommandohistorian och hämta en kod-rad som du skrivit tidigare. För att navigera i kommandohistorian, använd CTRL+UPP-PIL eller CTRL+NED-PIL.


</div>

Genom att högerklicka i tolkfönstret, så har du flera andra alternativ, som att kopiera hela historian (användbart för att göra en experimentskript, och sedan kunna spara det), eller att sätta in ett filnamn med full sökväg.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Python Hjälp 

I FreeCAD Hjälpmenyn, så hittar du en menypunkt som heter \"Python hjälp\", vilken kommer att öppna ett webbfönster som innehåller en komplett, realtidsgenererad dokumentation över alla python moduler som finns tillgänglig för FreeCAD tolken, inklusive python inbyggda FreeCAD moduler, system-installerade moduler, och extra FreeCAD moduler. Den dokumentation som fills tillgänglig där beror på hur mycket arbete varje modulutvecklare lägger på att dokumentera sin kod, men vanligtvis her pythonmoduler ett rykte om sig att vara ganska väldokumenterade. Ditt FreeCAD fönster måste vara öppet för att detta dokumentationssystem ska fungera.


</div>

In the FreeCAD **Help** menu, you\'ll find an entry labeled **Automatic python modules documentation**, which will open a browser window containing a complete, realtime-generated documentation of all Python modules available to the FreeCAD interpreter, including Python and FreeCAD built-in modules, system-installed modules, and FreeCAD additional modules. The documentation available there depends on how much effort each module developer put into documenting his code, but Python modules have a reputation for being fairly well documented. Your FreeCAD window must stay open for this documentation system to work. The entry **Python scripting documentation** will give you a quick link to the [Power users hub](Power_users_hub.md) wiki section.

[top](#top.md)


<div class="mw-translate-fuzzy">

## Inbyggda moduler 

Eftersom FreeCAD är designat för att kunna köras utan ett grafiskt användargränssnitt, så är nästan all dess funktionalitet uppdelat i två grupper: Kärnfunktioner, benämnda App, och gränssnittsfunktioner, benämnda Gui. Så våra två inbyggda FreeCAD huvudmoduler kallas för App och Gui. Dessa två moduler kan även kommas åt av skript utanför tolken, genom de respektive namnen FreeCAD och FreeCADGui.


</div>

Since FreeCAD is designed so that it can also be run without a Graphical User Interface (GUI), almost all its functionality is separated into two groups: Core functionality, named `App`, and GUI functionality, named `Gui`. These two modules can also be accessed from scripts outside of the interpreter, by the names `FreeCAD` and `FreeCADGui` respectively.


<div class="mw-translate-fuzzy">

-   I **App modulen**, så hittar du allt som är relaterat till själva applikationen, som metoder för att öppna eller stänga filer, och till dokumenten, som att ställa in det aktiva dokumentet eller lista dess innehåll.


</div>


<div class="mw-translate-fuzzy">

-   I **Gui modulen**, så hittar du verktyg för åtkomst och hantering av gränssnittselement, som arbetsbänkarna och dears verktygslådor, och mer intressant, den grafiska representationen av allt FreeCAD innehåll.


</div>


<div class="mw-translate-fuzzy">

Att lista allt innehåll av dessa moduler är en lite improduktiv uppgift, eftersom de växer ganska snabbt tillsammans med FreeCAD\'s utveckling. Men de två erbjudna listverktygen (klasslistaren och python hjälpen) ska alltid ge dig en komplett och uppdaterad dokumentation av dessa moduler.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### App och Gui objekten 

Som vi sade, så är allt i FreeCAD uppdelat mellan kärna och representation. Detta inkluderar även 3D objekten. Du kan komma åt objektens definierande egenskaper (kallade features i FreeCAD) via App modulen, och ändra det sätt som de representeras på skärmen via Gui modulen. Till exempel, en kub har egenskaper som definierar den, som bredd, längd, höjd som sparas i ett App objekt, och representationsegenskaper, som ytfärg, ritläge, som lagras i ett motsvarande Gui objekt.


</div>

As already mentioned, in FreeCAD everything is separated into core and representation. This includes the 3D objects. You can access defining properties of objects (called features in FreeCAD) via the `App` module, and change the way they are represented on screen via the `Gui` module. For example, a cube has properties that define it (like width, length, height) that are stored in an `App` object, and representation properties (like faces color, drawing mode) that are stored in a corresponding `Gui` object.

Detta sätt att göra det på tillåter ett mycket brett användningsområde, som att låta algoritmer endast arbeta på den definierande delen av objekten, utan att behöva bry sig om någon visuell del, eller även att skicka dokumentets innehåll till icke-grafiska applikationer, som listor, räkneark eller elementanalyser.


<div class="mw-translate-fuzzy">

För varje App objekt i ditt dokument, så existerar det ett motsvarande Gui objekt. Själva dokumentet har faktiskt också ett App och ett Gui objekt. Detta är förstås endast giltigt när du kör FreeCAD med dess fulla gränssnitt. I kommando-linje versionen, så existerar inget gränssnitt, så endast App objekt är tillgängliga. Notera att Gui delen av objekt genereras igen varje gång som ett App objekt är markerat som \"att omberäknas\" (till exempel när en av dess parametrar har ändrats), så ändringar som du har gjort direkt på Gui objektet kan förloras.


</div>


<div class="mw-translate-fuzzy">

För att komma åt App delen av något, så skriver du:


</div>


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

där \"ObjektNamn är namnet på ditt objekt. Du kan också skriva:


</div>


```python
myObject = App.ActiveDocument.ObjectName
```


<div class="mw-translate-fuzzy">

För att komma åt Gui delen av samma objekt, skriv:


</div>


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```


<div class="mw-translate-fuzzy">

där \"ObjektNamn är namnet på ditt objekt. Du kan också skriva:


</div>


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```


<div class="mw-translate-fuzzy">

Om vi inte har något gränssnitt (vi är till exempel i kommandoradsläge), så kommer den sista raden att returnera None.


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

### Dokument objekten 

I FreeCAD så finns allt ditt arbete i Dokument. Ett dokument innehåller din geometri och kan sparas till en fil. Flera dokument kan öppnas samtidigt. Dokumentet, som geometrin som finns i den, har App och Gui objekt. App objekt innehåller dina geometridefinitioner, medan Gui objekt innehåller ditt dokuments olika vyer Du kan öppna flera fönster, där varje fönster visar ditt arbete med en annan zoomfaktor eller synvinkel. Dessa vyer är en del av Gui objektet i ditt dokument.


</div>

In FreeCAD all your work resides inside documents. A document contains your geometry and can be saved to a file. Several documents can be opened at the same time. The document, like the geometry contained inside, has `App` and `Gui` objects. The `App` object contains your actual geometry definitions, while the `Gui` object contains the different views of your document. You can open several windows, each one viewing your work with a different zoom factor or from a different direction. These views are all part of your document\'s `Gui` object.


<div class="mw-translate-fuzzy">

För att komma åt App delen i det aktiva dokumentet, skriv:


</div>


```python
myDocument = App.ActiveDocument
```

För att skapa ett nytt dokument, skriv:


```python
myDocument = App.newDocument("Document Name")
```


<div class="mw-translate-fuzzy">

För att komma åt Gui delen i det aktiva dokumentet, skriv:


</div>


```python
myGuiDocument = Gui.ActiveDocument
```

För att komma åt nuvarande vy, skriv:


```python
myView = Gui.ActiveDocument.ActiveView
```

[top](#top.md)

## Using additional modules 

The `FreeCAD` and `FreeCADGui` modules are only responsible for creating and managing objects in the FreeCAD document. They don\'t actually do anything more such as creating or modifying geometry. This is because that geometry can be of several types, and therefore requires additional modules, each responsible for managing a certain geometry type. For example, the [Part Workbench](Part_Workbench.md), using the OpenCascade kernel, is able to create and manipulate [BRep](http://en.wikipedia.org/wiki/Boundary_representation) type geometry. Whereas the [Mesh Workbench](Mesh_Workbench.md) is able to build and modify mesh objects. In this manner FreeCAD is able to handle a wide variety of object types, that can all coexist in the same document, and new types can easily be added in the future.

[top](#top.md)

### Creating objects 

Each module has its own way of dealing with geometry, but one thing they usually all can do is create objects in the document. But the FreeCAD document is also aware of the available object types provided by the modules:


```python
FreeCAD.ActiveDocument.supportedTypes()
```

will list all possible objects you can create. For example, let\'s create a mesh (handled by the `Mesh` module) and a part (handled by the `Part` module):


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```

The first argument is the object type, the second the name of the object. Our two objects look almost the same: They don\'t contain any geometry yet, and most of their properties are the same when you inspect them with `dir(myMesh)` and `dir(myPart)`. Except for one thing, `myMesh` has a `Mesh` property and `myPart` has a `Shape` property. That is where the Mesh and Part data are stored. For example, let\'s create a `Part` cube and store it in our `myPart` object:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

You could try storing the cube inside the `Mesh` property of the `myMesh` object, but it will return an error. That is because each properties is made to store only a certain type. In a `Mesh` property, you can only save stuff created with the `Mesh` module. Note that most modules also have a shortcut to add their geometry to the document:


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```

[top](#top.md)

### Modifying objects 

Modifying an object is done in the same way:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Now let\'s change the shape by a bigger one:


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```

[top](#top.md)

### Querying objects 

You can always look at the type of an object like this:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

or check if an object is derived from one of the basic ones (Part Feature, Mesh Feature, etc):


```python
print(myObj.isDerivedFrom("Part::Feature"))
```

Now you can really start playing with FreeCAD! For a complete list of available modules and their tools, visit the [Category:API](:Category:API.md) section.

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
