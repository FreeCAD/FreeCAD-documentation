---
- GuiCommand:/it
   Name:Arch Roof
   Name/it:Tetto
   MenuLocation:Arch → Tetto
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**R** **F**
   SeeAlso:[Struttura](Arch_Structure/it.md), [Muro](Arch_Wall/it.md)
---

# Arch Roof/it

## Descrizione

Lo strumento **<img src="images/Arch_Roof.svg" width=16px> [Tetto](Arch_Roof/it.md)** consente di creare un tetto inclinato selezionando un contorno. L\'oggetto Tetto creato in questo modo è parametrico e mantiene le sue relazioni con l\'oggetto base. Si basa sul principio che ad ogni bordo viene assegnata una falda del tetto (con le caratteristiche di pendenza, larghezza coperta, sbalzo, spessore).

**Nota:** Questo strumento è ancora in sviluppo e potrebbe non funzionare correttamente con le forme molto complesse.

<img alt="" src=images/RoofExample.png  style="width:600px;"> 
*Vista dall'alto di un modello di edificio che mostra il tetto in trasparenza*

## Utilizzo

1.  Creare un contorno seguendo il senso antiorario e selezionarlo.

    :   <img alt="" src=images/CounterclockwiseWire.png  style="width:600px;">

2.  Premere il pulsante **<img src="images/Arch_Roof.svg" width=16px> [Tetto](Arch_Roof/it.md)**, o premere i tasti **R** e poi **F**.

3.  Se l\'oggetto tetto di default ha una forma strana è perché lo strumento non possiede tutte le informazioni necessarie.

4.  Dopo aver creato il tetto di default, fare doppio clic sull\'oggetto nella vista ad albero per accedere alla modifica di tutte le sue proprietà. Angolo deve essere compreso tra 0 e 90.

    :   ![](images/RoofTable.png )

5.  Ogni riga corrisponde ad una falda del tetto. Quindi è possibile impostare le proprietà desiderate per ogni falda del tetto.

6.  Per aiutarvi, è possibile impostare `Angle` o `Run` a `0` e definire un `Relative Id`, questo rende automatici i calcoli per trovare i dati relativi a `Relative Id`.

7.  Funziona in questo modo:
    1.  Se `Angle &#61; 0` e `Run &#61; 0` allora il profilo è identico al profilo relativo.
    2.  Se `Angle &#61; 0` allora `Angle` viene calcolato in modo che l\'altezza sia la stessa del profilo relativo.
    3.  Se `Run &#61; 0` allora `Run` è calcolato in modo che l\'altezza sia la stessa del profilo relativo.

8.  Alla fine, impostare un angolo di 90° per creare un frontone, una parete di tamponamento.

    :   <img alt="" src=images/RoofProfil.png  style="width:600px;">

9.  
    **Nota**: per una migliore comprensione, vedere questo [youtube clip](https://www.youtube.com/watch?v=4Urwru71dVk).

## Opzioni

-   Gli elementi Tetto condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)

## Proprietà

-    {{PropertyData/it|Angles}}: Angolo di pendenza di ogni falda (un angolo per ciascun lato del contorno di base).

-    {{PropertyData/it|Runs}}: Proiezione orizzontale della lunghezza della falda (un Run per ciascun lato del contorno di base).

-    {{PropertyData/it|IdRel}}: Elenco delle relazioni Id dell\'angolo di inclinazione del tetto.

-    {{PropertyData/it|Thickness}}: Spessore della falda (uno spessore per ciascun lato del contorno di base).

-    {{PropertyData/it|Overhang}}: Sbalzo della falda, in proiezione orizzontale (uno sbalzo per ciascun lato del contorno di base).

-    {{PropertyData/it|Face}}: L\'indice della faccia dell\'oggetto di base da utilizzare (non ancora usato)

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Tetto può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione: 
```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```

-   Crea un oggetto `Roof` dal `baseobj` dato, che può essere un contorno chiuso o un oggetto solido.
    -   Se `baseobj` è un contorno, è possibile fornire elenchi per `angles`, `run`, `idrel`, `thickness`, e `overhang`, per ciascun bordo del contorno per definire la forma del tetto.
    -   Gli elenchi vengono completati automaticamente per corrispondere al numero di spigoli del contorno.

Esempio:


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Roof/it
