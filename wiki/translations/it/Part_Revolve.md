# Part Revolve/it
---
 GuiCommand:   Name: Part_Revolve   Name/it: Rivoluziona   MenuLocation: Parte , Rivoluziona...   Workbenches: Part_Workbench/it   Parte|SeeAlso: ---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Ruota l\'oggetto selezionato e crea una rivoluzione intorno a un dato asse. Si possono ruotare i seguenti tipi di oggetti che producono le corrispondenti forme ([Vedere Note di eccezioni](#Note.md)):


</div>

  Forma originale    Forma prodotta
   
  Vertice            Bordo
  Bordo              Superficie
  Wire (polilinea)   Shell (guscio)
  Faccia             Solido
  Shell              Solido composto (Compsolid)


<div class="mw-translate-fuzzy">

I solidi o i solidi composti non sono ammessi come forme di ingresso. I solidi composti, attualmente, non sono ancora utilizzabili. Le versioni future verificheranno le forme effettive e il tipo di oggetto composto.


</div>

![](images/Dialog-revolve_it.png )


<div class="mw-translate-fuzzy">

L\'argomento Angolo specifica di quanto deve essere ruotato l\'oggetto. Le coordinate spostano l\'origine dell\'asse di rotazione, rispetto all\'origine delle coordinate del sistema.


</div>


<div class="mw-translate-fuzzy">

Quando si seleziona un asse definito dall\'utente, i numeri definiscono la direzione dell\'asse di rotazione rispetto alle coordinate del sistema: se Z è 0 e Y e X non sono zero, allora l\'asse si trova nel piano XY. Il suo angolo è tale che la tangente è il rapporto tra le coordinate X e Y date.


</div>

## Notes


<div class="mw-translate-fuzzy">

### Note

-   Se la versione di FreeCAD ha la casella di controllo per Solid nella finestra di dialogo Revolve, è possibile creare dei solidi anche da Polilinee chiuse e da Bordi, Wires e Edges.
-   Se la Rivoluzione viene eseguita utilizzando un asse che interseca la faccia da ruotare, e si desidera creare un solido, il risultato potrebbe non essere valido. Questo può accadere per diversi motivi, di auto-incrocio, direzione, etc.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/it
