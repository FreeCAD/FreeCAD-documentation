# Part Helix/it
---
- GuiCommand:/it   Name:Part_Helix   Name/it:Elica   MenuLocation:Parte → [Workbenches:[[Part_Workbench/it   Parte](Part_CreatePrimitives/it___Crea_primitive]]_→_Elica.md),  [OpenSCAD](OpenSCAD_Workbench/it.md)|SeeAlso:[Crea Primitive](Part_CreatePrimitives/it.md)---


</div>

## Descrizione

La primitiva geometrica **[<img src=images/Part_Helix.svg style="width:16px"> [Elica](Part_Helix/it.md)** crea una forma ad elica, definita da un raggio, un passo e un\'altezza totale.

Un uso comune della primitiva elica è per [creare delle filettature](Thread_for_Screw_Tutorial/it.md) insieme a un profilo chiuso e all\'operazione **<img src="images/Part_Sweep.svg" width=16px> [Sweep](Part_Sweep/it.md)**. Questo processo funziona essenzialmente allo stesso modo in [PartDesign](PartDesign_Workbench/it.md) utilizzando lo strumento **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [Sweep additivo ](PartDesign_AdditivePipe/it.md)**.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Attivare l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md).
2.  Il dialogo Crea primitive può essere avviato in uno dei seguenti modi:
    -   Premere il pulsante **[<img src=images/Part_Primitives.svg style="width:16px"> [Primitive](Part_Primitives/it.md)** nella barra degli strumenti di Parte.
    -   Usare la voce **Part → [<img src=images/Part_Primitives.svg style="width:16px"> [Crea primitive](Part_Primitives/it.md) → Elica** nel menu di Parte.


</div>

![](images/PartHelixPrimitivesOptions_en.png )

#### Parametri


<div class="mw-translate-fuzzy">

-    {{Parameter|Pitch:}}il passo corrisponde allo spazio tra due \"giri\" consecutivi dell\'elica misurata lungo l\'asse principale dell\'elica.

-    {{Parameter|Height:}}l\'altezza corrisponde all\'altezza complessiva dell\'elica misurata lungo l\'asse principale dell\'elica.

-    {{Parameter|Radius:}}il raggio corrisponde al raggio del cerchio costruito dall\'elica visualizzando l\'elica dall\'alto o dal basso.

-    {{Parameter|Angle}}: per impostazione predefinita, l\'elica è costruita su un cilindro immaginario. Con questa opzione è possibile costruire l\'elica su un cono immaginario. Questo angolo corrisponde all\'angolo del cono. Il valore deve essere compreso tra 0 e +90 gradi.

-    {{Parameter|Right-handed or Left-handed:}}questo parametro specifica il [verso](https://en.wikipedia.org/wiki/Screw_thread) dell\'elica.


</div>

#### Posizione

-    {{Parameter|X:}}l\'asse principale dell\'elica è traslato lungo l\'asse x del valore indicato in questo campo.

-    {{Parameter|Y:}}l\'asse principale dell\'elica è traslato lungo l\'asse y del valore indicato in questo campo.

-    {{Parameter|Z:}}l\'asse principale dell\'elica è traslato lungo l\'asse z del valore indicato in questo campo.

-    {{Parameter|Direction:}}per impostazione predefinita, l\'asse principale dell\'elica è l\'asse z. Qui è possibile modificare l\'asse principale dell\'elica. Selezionando il parametro \"definito dall\'utente \...\", viene chiesto di indicare l\'asse principale dell\'elica inserendo le coordinate del suo vettore.

-    {{Parameter|3D View:}}consente di selezionare il centro nella vista 3D

## Opzioni

### Proprietà

Dopo aver creato l\'elica, è possibile modificare i suoi parametri.

+----------------------------------------------------------+-----------------------------------------------------------------------------------+
| ![](images/PartHelixProperty_en.png ) | I parametri in questo menu sono simili a quelli descritti sopra.                  |
|                                                          | **Base**                                                        |
|                                                          | \* {{Parameter|Placement:}} consente di spostare o ruotare l\'elica |
|                                                          |                                                                                   |
|                                                          | -                                                                  |
|                                                          |     {{Parameter|Angle:}}                                                          |
|                                                          |                                                                                |
+----------------------------------------------------------+-----------------------------------------------------------------------------------+

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Helix/it
