---
 GuiCommand:
   Name: Part_Chamfer
   Name/it: Part Smussa
   MenuLocation: Parte , Smussa...
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Fillet/it
---

# Part Chamfer/it



## Descrizione

**Part Smussa** smussa il bordo(i) selezionato(i) di un oggetto. Una finestra di dialogo consente di scegliere su quale/i bordo/i lavorare e di modificare vari parametri dello smusso.

![Chamfer example](images/Chamfer-example.png )



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Chamfer.svg" width=16px> Smussa...**.
    -   Seleziona l\'opzione **Parte → Smussa...** dal menu.
2.  Selezionare la forma da smussare dalla finestra di dialogo.
3.  Selezionare i bordi da smussare selezionando la casella corrispondente nella finestra di dialogo dello smusso o selezionandoli direttamente sul modello.
4.  Modificare i parametri dello smusso.
5.  Premere **OK** per chiudere la finestra di dialogo dello smusso e applicare lo smusso.



## Opzioni

![Dialog-chamfer](images/Dialog-chamfer.png )

-   Quando si selezionano i bordi del modello, si ha la possibilità di selezionarli singolarmente o per facce. In molte situazioni la selezione per facce può essere più efficiente .
-   Smusso di larghezza costante o variabile.
    -   Uno smusso di larghezza costante crea una smusso con i bordi equidistanti al bordo iniziale, alla distanza specificata.
    -   Uno smusso variabile ha i bordi che possono essere impostati a distanze diverse dal bordo originale, e consente di creare uno smusso angolato a piacere.



## Proprietà

![Part Chamfer Properties](images/Part_Chamfer-Properties.png ) 


{{Properties_Title|Base}}

-    **Base**: La forma su cui lo smusso deve essere applicato.

-    **Placement**: Specifica l\'orientamento e la posizione della forma nello spazio 3D.

-    **Label**: L\'etichetta che attiva l\'oggetto. Modificabile secondo le esigenze.






## Limitazioni

Lo smusso potrebbe non fare nulla se il risultato tocca o attraversa il bordo adiacente successivo. Quindi, se non si ottiene il risultato atteso, provare con un valore inferiore. Lo stesso vale per <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Raccorda](Part_Fillet/it.md).

Notare inoltre che la funzione Smusso è soggetta al problema della [denominazione topologica](Topological_naming_problem/it.md) quando viene apportata una qualsiasi modifica a una fase di modellazione precedente nella catena che influenza il numero di sfaccettature o vertici. Ciò può causare risultati imprevedibili. Fino a quando ciò non viene risolto, si consiglia di applicare le operazioni di smusso e di [raccordo](Part_Fillet/it.md) negli ultimi passi della catena.



## Script

Lo strumento smusso può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) aggiungendo un oggetto smusso al documento.

**Esempio di Script:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Descrizione dell\'esempio:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Crea un cubo di 5 mm a cui applicare lo smusso dei bordi. Per una spiegazione del metodo makeBox vedere [Part_API](Part_API/it.md).


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Aggiunge al documento un nuovo oggetto di tipo Smusso (del modulo Parte) con l\'etichetta \"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Specifica che la forma base dell\'oggetto smusso è \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Crea un array \"myEdges\" vuoto e poi aggiunge l\'array con i parametri di smusso di ogni bordo.
-   Las Sintassi per ogni voce deve essere (edge#, chamfer start length, chamfer end length) (bordo#, larghezza iniziale, larghezza finale)


```python
chmfr.Edges = myEdges
```

-   Imposta l\'attributo dei bordi dell\'oggetto smusso secondo la matrice appena creata.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Questa riga nasconde semplicemente \"myCube\" in modo che l\'oggetto \"myChamfer\" appena creato sia l\'unico oggetto visibile.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Ricalcola tutti i componenti modificati e presenti sullo schermo e aggiorna la visualizzazione.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/it
