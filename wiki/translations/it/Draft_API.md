# Draft API/it
**(Novembre 2018) Queste informazioni potrebbero essere incomplete e obsolete. Per l'ultima API, vedere la pagina [https://www.freecadweb.org/api Documentazione API autogenerata].**

Queste funzioni fanno parte dell\'ambiente [Draft](Draft_Workbench/it.md) e possono essere usate nelle [macro](macros/it.md) e nella console [Python](Python/it.md) dopo che il modulo `Draft` è stato importato.

Esempio: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction/it|cut|FreeCAD.Object, FreeCAD.Object|Restituisce un oggetto Taglio prodotto dalla differenza dei 2 oggetti dati. Gli oggetti originali vengono nascosti.|L'oggetto appena creato}}


{{APIFunction/it|extrude|FreeCAD.Object, Vector|Estrude un oggetto dato nella direzione data dal vettore. L'oggetto originale viene nascosto.|L'oggetto appena creato}}


{{APIFunction/it|formatObject|FreeCAD.Object, [FreeCAD.Object]|Questa funzione applica all'oggetto obiettivo dato le proprietà correnti che sono impostate nella barra degli strumenti di Draft (colore e lo spessore della linea), o copia le proprietà di un secondo oggetto, se questi viene fornito. Esso pone anche l'oggetto nel gruppo "In costruzione", se il pulsante "Costruzione" viene premuto.|Nulla}}


{{APIFunction/it|fuse|FreeCAD.Object, FreeCAD.Object|Restituisce un oggetto Fusione prodotto dall'unione dei 2 oggetti dati. Se gli oggetti sono complanari, è usata una polilinea Draft speciale, in caso contrario l'oggetto finale è una fusione standard di parti.|L'oggetto appena creato}}


{{APIFunction/it|getDraftPath|[string]|Restituisce il percorso dell'utente o del sistema in cui è in esecuzione il modulo Draft. Se viene fornito un sottoindirizzo o un nome di file, viene restituito il percorso completo del sottoindirizzo all'interno del modulo Draft.|Il percorso di un file}}


{{APIFunction/it|getGroupContents|list|Esegue la scansione in modo ricorsivo della lista di gruppi indicata. Se i gruppi sono individuati, i loro contenuti vengono aggiunti alla lista.|Un elenco di oggetti di FreeCAD}}


{{APIFunction/it|getRealName|string|Rimuove i numeri indicati da un nome di un oggetto.|Il nome spogliato dell'oggetto.}}


{{APIFunction/it|getSelection| |Restituisce la selezione corrente di FreeCAD.|La selezione corrente di FreeCAD.}}


{{APIFunction/it|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Crea un oggetto Cerchio di raggio dato. Se si indica una posizione, essa viene utilizzata. Se facemode è False, il cerchio è mostrato come una polilinea, altrimenti come una faccia. Se startAngle e endAngle sono indicati (in gradi), essi vengono utilizzati e l'oggetto appare come un arco.|L'oggetto appena creato.}}


{{APIFunction/it|makeDimension|Vector, Vector, [Vector] o FreeCAD.Object, int, int, [Vector]|Crea un oggetto Dimensione (Quota) misurando la distanza tra primo e il secondo vettore, con la linea di quota passante attraverso un terzo vettore se questo viene indicato.  Sono utilizzati la larghezza di linea e il colore correnti impostati nella barra di Draft. Invece di 2 vettori, si può anche passare un oggetto FreeCAD, o due numeri interi (e facoltativamente un vettore per cui deve passare la linea di quota). In tal caso, la dimensione è associata all'oggetto, e misura due dei suoi vertici, indicati dai due numeri di indice.|L'oggetto appena creato.}}


{{APIFunction/it|makeLine|Vector, Vector|Crea una Linea tra i due vettori dati. Sono utilizzati la larghezza di linea e il colore correnti impostati nella barra di Draft.|L'oggetto appena creato.}}


{{APIFunction/it|makeRectangle|length, width, [placement], [facemode]|Crea un oggetto Rettangolo con la lunghezza in direzione X e l'altezza in direzione Y. Se è indicata una posizione, essa viene utilizzata. Se facemode è False, il rettangolo è mostrato come una polilinea, altrimenti come una faccia. Sono utilizzati la larghezza di linea e il colore correnti impostati nella barra di Draft.|L'oggetto appena creato.}}


{{APIFunction/it|makeText|string o list, [Vector], [screenmode]|Crea un oggetto Testo, nel punto indicato se si fornisce un vettore, contenente la stringa o le stringhe riportate nell'elenco, una stringa per riga. Sono utilizzati il colore corrente dalla barra degli strumenti Draft e l'altezza del testo e il tipo di carattere specificati nelle preferenze. Se screenmode è True, il testo è sempre rivolto nella direzione della vista, altrimenti si trova sul piano XY.|L'oggetto appena creato.}}


{{APIFunction/it|makeWire|list o Part.Wire, [closed], [placement], [facemode]|Crea un oggetto Wire (Polilinea) dalla lista di vettori indicati o dalla polilinea indicata. Se closed è True o se il primo e l'ultimo punto sono identici, la polilinea è chiusa. Se facemode è True (e la polilinea è chiusa), la polilinea appare riempita. Sono utilizzati la larghezza di linea e il colore correnti impostati nella barra di Draft.|L'oggetto appena creato.}}


{{APIFunction/it|move|FreeCAD.Object o list, Vector, [copymode]|Sposta l'oggetto dato o gli oggetti contenuti nella lista fornita nella direzione e alla distanza indicata dal vettore dato. Se CopyMode è True, gli oggetti attuali non vengono spostati, ma vengono invece create delle copie.|L'oggetto o gli oggetti (o loro copie se CopyMode era True).}}


{{APIFunction/it|precision| |Restituisce il valore della precisione secondo le impostazioni dell'utente in Draft.|Un intero.}}


{{APIFunction/it|rotate|FreeCAD.Object o list, angle, [center], [axis] ,[copymode]|Ruota l'oggetto dato o gli oggetti contenuti nella lista fornita con un determinato angolo attorno al centro dato, se previsto, con axis come asse di rotazione. Se axis viene omesso, la rotazione avviene attorno all'asse verticale Z. Se CopyMode è True, gli oggetti reali non vengono spostati, ma vengono invece create delle copie.|L'oggetto (o sue copie).}}


{{APIFunction/it|scale|FreeCAD.Object o list, vector, [center], [copymode]|Ridimensiona l'oggetto dato o gli oggetti contenuti nella lista data con i fattori di scala definiti dal vettore dato (nelle direzioni X, Y e Z) intorno al centro, se viene indicato. Se CopyMode è True, gli oggetti reali non vengono spostati, ma vengono invece create delle copie.|L'oggetto (o sue copie).}}


{{APIFunction/it|select|FreeCAD.Object|Deseleziona tutto e seleziona solo l'oggetto passato|Nulla.}}


{{APIFunction/it|shapify|FreeCAD.Object|Trasforma un oggetto parametrico in una forma non-parametrica.|L'oggetto appena creato.}}


{{APIFunction/it|draftify|FreeCAD.Object o list|Trasforma l'oggetto dato o ogni oggetto della lista data in polilinee parametriche.|Nulla.}}


{{APIFunction/it|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Crea una rappresentazione SVG dell'oggetto dato. L'attributo linemodifier è un fattore di scala (in percentuale) per la larghezza della linea, e textmodifier per la dimensione del testo. Inoltre è anche possibile fornire una tupla di vettori per definire un piano di proiezione, altrimenti la geometria viene proiettata sul piano XY.|una stringa contenente una rappresentazione SVG dell'oggetto dato.}}


 




[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > [Draft](Draft_Workbench.md) > Draft API/it
