# Manual:Creating parametric objects/it
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Nel [precedente capitolo](Manual:Creating_and_manipulating_geometry/it.md), abbiamo visto come creare una geometria Parte, e come visualizzarla sullo schermo, collegandola ad un document object \"muto\" (non parametrico). Questo è noioso quando vogliamo cambiare la forma di tale oggetto. Dovremmo creare una nuova forma, poi attribuirla di nuovo al nostro oggetto.


</div>


<div class="mw-translate-fuzzy">

Ma, in tutti i capitoli precedenti di questo manuale abbiamo visto anche quanto sono potenti gli oggetti parametrici. Basta cambiare una loro proprietà, e la forma viene ricalcolata al volo.


</div>


<div class="mw-translate-fuzzy">

Internamente, gli oggetti parametrici non fanno nulla di diverso da quello che abbiamo appena fatto: essi ricalcolano i contenuti delle loro proprietà Shape, più e più volte, ogni volta che viene cambiata una proprietà.


</div>

-   Declares the necessary properties for the object.
-   Defines the behavior when any of these properties are modified.

The structure of such a parametric object is as simple as this:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```


<div class="mw-translate-fuzzy">

FreeCAD fornisce un sistema molto vantaggioso per costruire questi oggetti parametrici completamente in Python. Esso consiste in una semplice classe Python, che definisce tutte le proprietà di cui l\'oggetto ha bisogno, e che cosa succede quando una di queste proprietà cambia. La struttura di questo oggetto parametrico è semplice come questa:


</div>

-   Store the class itself in the **Proxy** attribute of the FreeCAD document object:

By assigning **self** to the **Proxy** attribute of the FreeCAD document object, we link the logic of our Python class to the FreeCAD object. This means the document object will \"carry\" the Python class code inside itself, allowing it to behave according to the logic defined in the class. This connection enables FreeCAD to know how to interact with and recalculate the parametric object.

-   Create all the properties the object needs:

Using the **addProperty** method, we define the custom properties required by the object. Properties act as parameters or variables for the object and can be accessed, modified, and displayed in FreeCAD\'s property editor. In the example, we add a floating-point property named **MyLength**. This property will later influence the shape or behavior of the object.

class myParametricObject:

  def __init__(self,obj):
    obj.Proxy = self
    obj.addProperty("App::PropertyFloat","MyLength")
    ...
       
  def execute(self,obj):
    print ("Recalculating the shape...")
    print ("The value of MyLength is:")
    print (obj.MyLength)
    ...


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```


<div class="mw-translate-fuzzy">

Tutte le classi Python di solito hanno un metodo \_\_init\_\_. Ciò che è all\'interno di tale metodo viene eseguito quando tale classe viene istanziata (il che significa, in gergo di programmazione, che da quella classe è stato creato un Object Python. Pensate a una classe come a un \"modello\" per creare copie dal vivo di esso). Nella nostra funzione \_\_init\_\_ qui facciamo due cose importanti: 1- memorizzare la nostra classe stessa nell\'attributo \"Proxy\" del nostro oggetto del documento di FreeCAD, vale a dire, l\'oggetto documento FreeCAD conterrà questo codice al suo interno, and 2- creare tutte le proprietà necessarie all\'oggetto. Sono disponibili molti tipi di proprietà, è possibile ottenere l\'elenco completo digitando questo codice:


</div>

FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"dummy\").supportedProperties()

-   The **execute** method is called whenever the object needs to be updated.
-   It is responsible for recalculating the shape and assigning it to the object\'s **Shape** attribute.
-   The **obj** argument gives access to the FreeCAD document object, enabling you to make changes programmatically.

With this system, FreeCAD handles the rest---ensuring that the object is properly updated in the document and displayed correctly in the graphical interface.


<div class="mw-translate-fuzzy">

Quindi, la seconda parte importante è il metodo execute. Tutto il codice contenuto in questo metodo viene eseguito quando l\'oggetto viene contrassegnato per il ricalcolo, il che avviene quando si modifica una proprietà. Questo è tutto quello che c\'è da fare. All\'interno di execute, è necessario fare tutto ciò che deve essere fatto, vale a dire, calcolare una nuova forma e attribuirla all\'oggetto stesso con qualcosa di simile a obj.Shape = myNewShape. Ecco perché il metodo execute prende un argomento \"obj\", che sarà il FreeCAD document object stesso, e in questo modo possiamo manipolarlo all\'interno del nostro codice Python.


</div>


<div class="mw-translate-fuzzy">

Un\'ultima cosa importante da ricordare: se si creano questi oggetti parametrici in un documento di FreeCAD, quando si salva il file, il codice Python di cui sopra non viene memorizzato nel file. Questo viene fatto per motivi di sicurezza. Se un file di FreeCAD contenesse del codice, sarebbe possibile che qualcuno distribuisca dei file di FreeCAD contenenti del codice dannoso che potrebbe danneggiare i computer di altri. Quindi, se si distribuisce un file che contiene degli oggetti realizzati con il codice di cui sopra, tale codice deve essere presente anche sul computer che apre il file. Il modo più semplice per raggiungere questo obiettivo è di solito quello di salvare il codice di cui sopra in una macro, e poi distribuire la macro insieme con il file FreeCAD o condividere la macro nel [FreeCAD macros repository](Macros_recipes/it.md) dove chiunque può scaricarlo.


</div>

Ora faremo un piccolo esercizio, costruiremo un oggetto parametrico composto da una semplice faccia rettangolare parametrica. Esempi più complessi sono disponibili negli [esempi di oggetti parametrici](Scripted_objects/it.md) e nello stesso [codice sorgente di FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py).


<div class="mw-translate-fuzzy">

Diamo al nostro oggetto due proprietà: Length e Width, che useremo per costruire un rettangolo. Poi, dato che l\'oggetto ha già una proprietà Placement pre-costruita (tutti gli oggetti geometrici ne hanno una di default, quindi non è necessario aggiungerla), collochiamo il rettangolo nella posizione e rotazione impostata in Placement, per fare in modo che l\'utente possa poi essere in grado di spostare il rettangolo ovunque desideri modificando solo la proprietà Placement.


</div>


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```


<div class="mw-translate-fuzzy">

Invece di incollare il codice precedente nella console Python, è meglio salvarlo da qualche parte, in modo da poterlo riutilizzare e modificare in un secondo tempo. Per esempio in una nuova macro (menu Strumenti -\> Macro -\> Crea). Dargli un nome, ad esempio, \"ParamRectangle\". Le macro FreeCAD vengono salvate con estensione .FCMacro, che però Python non riconosce quando si utilizza l\'importazione. Quindi, prima di utilizzare il codice di cui sopra, bisogna rinominare il file ParamRectangle.FCMacro in ParamRectangle.py. Questo può essere fatto semplicemente, navigando con il file explorer nella cartella delle macro indicata nel menu Strumenti -\> Macro.


</div>

Dopo, nella console Python possiamo fare questo:


```python
import ParamRectangle
```

Esplorando i contenuti di ParamRectangle, possiamo verificare che contenga la nostra classe ParamRectangle.


<div class="mw-translate-fuzzy">

Per creare un nuovo oggetto parametrico utilizzando la nostra classe ParametricRectangle, usiamo il seguente codice. Notare che usiamo Part::FeaturePython invece di Part::Feature che abbiamo usato nei capitoli precedenti (The Python version allows to define our own parametric behaviour):


</div>


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"Rectangle\")

ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # this is mandatory unless we code the ViewProvider too
FreeCAD.ActiveDocument.recompute()

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Creates a new **Part::FeaturePython** object named **Rectangle** in the active FreeCAD document. This object is specifically designed for custom parametric behavior, allowing Python-defined logic to manage its properties and behavior.

-   **ParamRectangle.ParametricRectangle(myObj)**: Initializes the object by associating it with the **ParametricRectangle** class from the **ParamRectangle** module or script. This links the custom Python-defined logic to the object, enabling it to act as a parametric object.

-   **myObj.ViewObject.Proxy = 0**: Resets the **ViewObject.Proxy** attribute to 0, ensuring that the object uses FreeCAD's default view handling. This step is required unless you define a custom ViewProvider to manage the visual representation of the object.

-   **FreeCAD.ActiveDocument.recompute()**: Recomputes the document to update the geometry and reflect changes in the FreeCAD graphical interface, making the new object fully visible and functional


<div class="mw-translate-fuzzy">

Sullo schermo non appare ancora nulla perché le proprietà lunghezza e larghezza sono 0, e questo attiva la condizione \"do-nothing\" (non fare nulla) dentro execute. Basta cambiare i valori di lunghezza e larghezza, e magicamente appare il nostro oggetto ricalcolato al-volo.


</div>


<div class="mw-translate-fuzzy">

Naturalmente è noioso dover digitare queste 4 righe di codice Python ogni volta che si vuole creare un nuovo rettangolo parametrico. Un modo molto semplice per risolvere questo consiste nel mettere le 4 righe di cui sopra all\'interno del file ParamRectangle.py, alla fine, dopo la fine della classe ParametricRectange (Possiamo farlo dall\'editor delle Macro).


</div>


<div class="mw-translate-fuzzy">

Ora, quando si digita import ParamRectangle, viene automaticamente creato un nuovo rettangolo parametrico. Ancora meglio, siamo in grado di aggiungere un pulsante della barra degli strumenti che faccia proprio questo:


</div>


<div class="mw-translate-fuzzy">

-   Aprire il menu **Strumenti -\> Personalizza**
-   Nella scheda \"Macro\", selezionare la macro ParamRectangle.py, compilare la descrizione come si desidera, e premere \"Aggiungi\":

![](images/Exercise_python_04.jpg )


</div>

![](images/FreeCAD_python_macroRec.png )

-   Nella scheda Barra degli strumenti, creare una nuova barra degli strumenti personalizzata in un ambiente a scelta (o in quello globale), selezionare la macro e aggiungerla alla barra degli strumenti:

![](images/FreeCAD_python_toolbarCus.png )

-   Questo è tutto, ora nella barra degli strumenti abbiamo un nuovo pulsante che, se cliccato, crea un rettangolo parametrico.


<div class="mw-translate-fuzzy">

Ricordare che se si desidera distribuire a terzi i file creati con questo nuovo strumento, i riceventi devono anche avere la macro ParamRectangle.py installata sul proprio computer.


</div>

**Approfondimenti**

-   [Il repositorio delle macro di FreeCAD](Macros_recipes/it.md)
-   [Esempi di oggetti parametrici](Scripted_objects/it.md)
-   [Altri esempi nel codice di FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating parametric objects/it
