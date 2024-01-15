---
 GuiCommand:
   Name: Part Revolve
   Name/it: Part Rivoluziona
   MenuLocation: Parte , Rivoluziona...
   Workbenches: Part_Workbench/it
---

# Part Revolve/it



## Descrizione

Crea una rivoluzione dell\'oggetto selezionato attorno a un determinato asse. Sono consentiti i seguenti tipi di forma che portano alle forme di output elencate:

  Forma originale    Forma prodotta
   
  Vertice            Bordo
  Bordo              Superficie
  Wire (polilinea)   Shell (guscio)
  Faccia             Solido
  Shell              Solido composto (Compsolid)

È possibile utilizzare anche uno [Schizzo](Sketcher_Workbench/it.md). Solidi o solidi composti non sono consentiti come forme di input. Attualmente non sono ammessi nemmeno i composti normali.

![](images/Dialog-revolve_it.png )

L\'argomento Angolo specifica di quanto deve essere ruotato l\'oggetto. Le coordinate spostano l\'origine dell\'asse di rivoluzione, rispetto all\'origine del sistema di coordinate.

Se si seleziona un asse definito dall\'utente, i numeri definiscono la direzione dell\'asse di rotazione rispetto al sistema di coordinate: Se la coordinata Z è 0 e le coordinate Y e X sono diverse da zero, l\'asse giacerà sul piano X-Y. Il suo angolo è tale che la sua tangente è il rapporto tra le coordinate X e Y date.



## Note

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati possono essere utilizzati anche come forme e per specificare l\'asse. {{Version/it|0.20}}
-   Se l\'oggetto da rivoluzionare interseca l\'asse di rotazione, nella maggior parte dei casi l\'operazione fallirà.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/it
