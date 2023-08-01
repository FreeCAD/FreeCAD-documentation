---
- GuiCommand:/it
   Name:Arch CurtainWall
   Name/it:Facciata continua
   MenuLocation:Arch → Facciata continua
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**C** **W**
   Version:0.19
   SeeAlso:[Muro](Arch_Wall/it.md), [Griglia](Arch_Grid/it.md)
---

# Arch CurtainWall/it


</div>



## Descrizione

Questo strumento crea una [facciata continua](https://en.wikipedia.org/wiki/Curtain_wall_(architecture)) suddividendo una faccia di base in facce quadrangolari, quindi creando montanti verticali sui bordi verticali, montanti orizzontali sui bordi orizzontali e riempiendo gli spazi tra i montanti con dei pannelli.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Le facciate continue possono essere create da qualsiasi tipo di oggetto esistente, in questo caso tutte le facce dell\'oggetto saranno suddivise. Funziona quindi meglio se usato con un oggetto che ha solo una faccia. In genere, si crea prima una faccia, preferibilmente delimitata da 4 bordi, che rappresenta l\'area che si desidera riempire con una facciata continua, poi si applica lo strumento.


<div class="mw-translate-fuzzy">

Le facciate continue possono anche essere costruite da un oggetto lineare, come una linea, un arco o una polilinea, come con un normale [muro](Arch_Wall/it.md).


</div>

Anche le facce con doppia curvatura o le facce con più di 4 spigoli funzionano, ma il risultato è meno prevedibile.

Le facce vengono divise in faccette quadrangolari. Se i 4 punti della faccetta sono complanari, viene creata una faccetta quadrata. In caso contrario, la faccetta viene divisa in due triangoli e viene aggiunto un montante diagonale.


<div class="mw-translate-fuzzy">

Nel caso in cui sia necessaria una suddivisione non regolare, è anche possibile creare il proprio oggetto suddiviso, ad esempio utilizzando una [Griglia](Arch_Grid/it.md) di Arch, e impostando le suddivisioni verticale e orizzontale della facciata continua su 1.


</div>

Si può anche usare lo strumento Facciata continua senza alcun oggetto selezionato, nel qual caso è possibile disegnare una linea di base, che verrà estrusa verticalmente per formare la faccia su cui sarà costruita la facciata continua.



## Utilizzo



### Disegnare una facciata continua dall\'inizio 


<div class="mw-translate-fuzzy">

1.  Assicurarsi che non sia selezionato nulla
2.  Premere il pulsante **<img src="images/Arch_CurtainWall.svg" width=16px> [Facciata continua](Arch_CurtainWall/it.md)
**, o premere i tasti **C** e poi **W**
3.  Fare clic su un primo punto nella vista 3D o digitare le coordinate
4.  Fare clic su un secondo punto nella vista 3D o digitare le coordinate
5.  Regolare le proprietà necessarie


</div>



### Creare una facciata continua da un oggetto selezionato 


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti di geometria di base (oggetto di Draft, schizzo, ecc.)
2.  Premere il pulsante **<img src="images/Arch_CurtainWall.svg" width=16px> [Facciata continua](Arch_CurtainWall/it.md)
**, o o i tasti **C** e poi **W**
3.  Regolare le proprietà necessarie


</div>



## Opzioni


<div class="mw-translate-fuzzy">

-   Le facciate continue condividono le proprietà e i comportamenti comuni di tutti i [Componenti di Arch](Arch_Component/it.md)
-   I montanti per le facciate continue possono essere realizzati da un profilo quadrato automatico (impostare le proprietà **Dimensione del montante**) o da un profilo personalizzato (impostare la proprietà **Profilo del montante**). I montanti possono essere centrati su qualsiasi bordo o posizionati in relazione al punto (0,0,0) disattivando la proprietà **Profilo centrato**. Ad esempio, se si desidera posizionare un profilo leggermente dietro i pannelli, si deve disegnare il profilo leggermente spostato dal punto di origine (0,0,0)
-   Le facciate continue supportano i [Multimaterial](Arch_MultiMaterial/it.md). All\'interno del multimateriale, per i montanti verrà utilizzato lo strato **Telaio** e lo strato **Pannello di vetro** per i pannelli, oppure **Pannello solido** se non è presente alcun pannello di vetro nel multi-materiale.
-   Le facciate continue possono essere basate su un oggetto lineare come una linea, un arco o una polilinea. In tal caso, internamente, verrà costruita una superficie di base estrudendo l\'oggetto lineare lungo la direzione data dalla proprietà **Direzione verticale**, per la lunghezza data dalla proprietà **Altezza**.


</div>



## Proprietà


<div class="mw-translate-fuzzy">

Gli oggetti di facciata continua ereditano le proprietà dei [Componenti](Arch_Component/it.md) e hanno anche le seguenti proprietà extra:


</div>

-    **Vertical Mullion Number**:Il numero di montanti verticali

-    **Vertical Mullion Alignment**: Se il profilo dei montanti verticali viene allineato o no alla superficie

-    **Vertical Sections**: Il numero di sezioni verticali di questa facciata continua

-    **Vertical Mullion Height**: L\'altezza del profilo dei montanti verticali, se non viene utilizzato alcun profilo

-    **Vertical Mullion Width**: La larghezza del profilo dei montanti verticali, se non viene utilizzato alcun profilo

-    **Vertical Mullion Profile**: Un profilo per i montanti verticali (disabilita le dimensioni dei montanti verticali)

-    **Horizontal Mullion Number**: Il numero di montanti orizzontali

-    **Horizontal Mullion Alignment**: Se il profilo dei montanti orizzontali viene allineato o meno alla superficie

-    **Horizontal Sections**: Il numero di sezioni orizzontali di questa facciata continua

-    **Horizontal Mullion Height**: L\'altezza del profilo dei montanti orizzontali, se non viene utilizzato alcun profilo

-    **Horizontal Mullion Width**: La larghezza del profilo dei montanti orizzontali, se non viene utilizzato alcun profilo

-    **Horizontal Mullion Profile**: Un profilo per i montanti orizzontali (disabilita la dimensione dei montanti orizzontali)

-    **Diagonal Mullion Number**: Il numero di montanti diagonali

-    **Diagonal Mullion Size**: La dimensione dei montanti diagonali, se presente, se non viene utilizzato alcun profilo

-    **Diagonal Mullion Profile**: Un profilo per i montanti diagonali, se presente (disabilita la dimensione dei montanti diagonali)

-    **Panel Number**: Il numero di pannelli

-    **Panel Thickness**: Lo spessore dei pannelli

-    **Swap Horizontal Vertical**: Scambia linee orizzontali e verticali

-    **Refine**: Esegue sottrazioni tra i componenti in modo che non ci siano sovrapposizioni

-    **Center Profiles**: Centra il profilo sui bordi o no

-    **Vertical Direction**: Il riferimento alla direzione verticale che verrà utilizzato da questo oggetto per dedurre le direzioni verticale / orizzontale. Tenerlo vicino alla direzione verticale effettiva della facciata continua

-    **Height**: L\'altezza di questa facciata continua, nel caso in cui sia basata su un oggetto lineare

-    **Host**: L\'ospite di questa facciata continua. La facciata continua apparirà incorporata nel suo oggetto host nella vista ad albero (non viene eseguita nessun\'altra azione)

## Making frame walls 

Curtain walls are convenient to use in conjunction with [walls](Arch_Wall.md) to create frame walls (walls where an inner, structural layer is made of frames, usually wooden or metal, instead of an homogeneous material such as concrete or brick).

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

The procedure described below creates a wall and a curtain wall based on a same baseline, then gives the wall a multi-material which leaves an empty space, where the curtain wall is placed:

1.  Create a normal [Arch Wall](Arch_Wall.md), either by clicking two points of from an existing linear object
2.  Select the base object of the newly created arch wall
3.  Press the **<img src="images/Arch_CurtainWall.svg" width=16px> [CurtainWall](Arch_CurtainWall.md)** button, or press the **C** then **W** keys to create a curtain wall from the same baseline as the wall
4.  Make sure both the wall and curtain wall have the same **Height**
5.  Set the number of **horizontal sections** of the curtain wall to zero if you wish only vertical frames
6.  Set the desired **horizontal mullion width** and **horizontal mullion height** (or use a mullion profile)
7.  Prepare two (or more) [materials](Arch_SetMaterial.md), one for the panels, one for the void where the frame will be
8.  Make one [multi-material](Arch_MultiMaterial.md), using one layer of the panel material, one layer of the void material with a negative width value (which will make it not drawn) corresponding to the vertical mullion height of the curtain wall, and another layer of panel material
9.  Attribute the multi-material to the wall
10. Set the **Host** property of the curtain wall to the wall we created in first point

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Facciata continua può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Esempio:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = FreeCAD.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CurtainWall/it
