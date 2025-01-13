---
 GuiCommand:
   Name: Arch CurtainWall
   Name/it: Facciata continua
   MenuLocation: Arch , Facciata continua
   Workbenches: Arch_Workbench/it
   Shortcut: **C** **W**
   Version: 0.19
   SeeAlso: Arch_Wall/it, Arch_Grid/it
---

# Arch CurtainWall/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea una [facciata continua](https://en.wikipedia.org/wiki/Curtain_wall_(architecture)) suddividendo una faccia di base in facce quadrangolari, quindi creando montanti verticali sui bordi verticali, montanti orizzontali sui bordi orizzontali e riempiendo gli spazi tra i montanti con dei pannelli.


</div>

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Le facciate continue possono essere create da qualsiasi tipo di oggetto esistente, in questo caso tutte le facce dell\'oggetto saranno suddivise. Funziona quindi meglio se usato con un oggetto che ha solo una faccia. In genere, si crea prima una faccia, preferibilmente delimitata da 4 bordi, che rappresenta l\'area che si desidera riempire con una facciata continua, poi si applica lo strumento.

Le facciate continue possono anche essere costruite da un oggetto lineare, come una linea, un arco o una polilinea, come con un normale [muro](Arch_Wall/it.md).

Anche le facce con doppia curvatura o le facce con più di 4 spigoli funzionano, ma il risultato è meno prevedibile.

Le facce vengono divise in faccette quadrangolari. Se i 4 punti della faccetta sono complanari, viene creata una faccetta quadrata. In caso contrario, la faccetta viene divisa in due triangoli e viene aggiunto un montante diagonale.

Nel caso in cui sia necessaria una suddivisione non regolare, è anche possibile creare il proprio oggetto suddiviso, ad esempio utilizzando una [Griglia](Arch_Grid/it.md) di Arch, e impostando le suddivisioni verticale e orizzontale della facciata continua su 1.

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

-   Le facciate continue condividono le proprietà e i comportamenti comuni di tutti i [Componenti di Arch](Arch_Component/it.md)
-   I montanti per le facciate continue possono essere realizzati da un profilo quadrato automatico (impostare le proprietà **Dimensione del montante**) o da un profilo personalizzato (impostare la proprietà **Profilo del montante**). I montanti possono essere centrati su qualsiasi bordo o posizionati in relazione al punto (0,0,0) disattivando la proprietà **Profilo centrato**. Ad esempio, se si desidera posizionare un profilo leggermente dietro i pannelli, si deve disegnare il profilo leggermente spostato dal punto di origine (0,0,0)
-   Le facciate continue supportano i [Multimaterial](Arch_MultiMaterial/it.md). All\'interno del multimateriale, per i montanti verrà utilizzato lo strato **Telaio** e lo strato **Pannello di vetro** per i pannelli, oppure **Pannello solido** se non è presente alcun pannello di vetro nel multi-materiale.
-   Le facciate continue possono essere basate su un oggetto lineare come una linea, un arco o una polilinea. In tal caso, internamente, verrà costruita una superficie di base estrudendo l\'oggetto lineare lungo la direzione data dalla proprietà **Direzione verticale**, per la lunghezza data dalla proprietà **Altezza**.



## Proprietà

Gli oggetti di facciata continua ereditano le proprietà dei [Componenti](Arch_Component/it.md) e hanno anche le seguenti proprietà extra:


<div class="mw-translate-fuzzy">

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


</div>



## Realizzare pareti con telaio 

Le facciate continue sono convenienti da utilizzare insieme a [walls](Arch_Wall/it.md) per creare muri con telaio (muri in cui uno strato strutturale interno è costituito da una serie di telai, solitamente in legno o metallo, invece che di un materiale omogeneo come cemento o mattoni).

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

La procedura descritta di seguito crea un muro e una facciata continua riferita alla stessa linea di base, quindi crea un muro multimateriale che lascia uno spazio vuoto, dove viene posizionata la facciata continua:

1.  Creare un [Muro ad arco](Arch_Wall/it.md) normale, facendo clic su due punti o su un oggetto lineare esistente
2.  Selezionare l\'oggetto alla base del muro ad arco appena creato
3.  Premere il pulsante **<img src="images/Arch_CurtainWall.svg" width=16px> [Facciata continua](Arch_CurtainWall/it.md)**, oppure premere i tasti **C** e quindi **W** per creare una facciata continua dalla stessa linea di base del muro
4.  Assicurarsi che sia il muro che la facciata continua abbiano lo stesso valore di **Height**
5.  Impostare il numero di **horizontal sections** della facciata continua su zero se si desiderano solo telai verticali
6.  Impostare **horizontal mullion width** e **horizontal mullion height** desiderati (o utilizzare un profilo del montante)
7.  Preparare due (o più) [materiali](Arch_SetMaterial/it.md), uno per i pannelli e uno per il vuoto dove verrà posizionata la cornice
8.  Creare un [multi-materiale](Arch_MultiMaterial/it.md), utilizzando uno strato del materiale del pannello, uno strato del materiale vuoto con un valore di larghezza negativo (che lo renderà non disegnato) corrispondente all\'altezza del montante verticale della facciata continua, ed un altro strato di materiale del pannello
9.  Attribuire il multimateriale al muro
10. Impostare la proprietà **Host** della facciata continua sul muro creato nel primo punto



## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Facciata continua può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


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


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch CurtainWall/it
