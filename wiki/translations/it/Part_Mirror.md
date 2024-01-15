---
 GuiCommand:
   Name: Part Mirror
   Name/it: Part Specchia
   MenuLocation: Parte , Specchia...
   Workbenches: Part_Workbench/it
---

# Part Mirror/it



## Descrizione

**Part Specchia** crea un nuovo oggetto (immagine) che è un riflesso dell\'oggetto originale (sorgente). L\'oggetto immagine viene creato dietro un piano speculare. Il piano dello specchio può essere un piano standard (**XY**, **YZ** o **XZ**), qualsiasi piano parallelo a un piano standard o ({{Version/it|0.22}}) qualsiasi piano arbitrario utilizzando un oggetto di riferimento.

Esempio:

![](images/PARTMirrorBeforev11.png )



*Prima*

![](images/PARTMirrorAfterv11.png )



*Dopo aver specchiato attraverso il piano YZ*



## Utilizzo

![](images/PartMirroring_Scr1.png )

1.  Facoltativamente selezionare uno o più oggetti di origine.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Mirror.svg" width=16px> [Specchia...](Part_Mirror/it.md)**.
    -   Selezionare l\'opzione **Parte → <img src="images/Part_Mirror.svg" width=16px> Specchia...** dal menu.
3.  Se non si ha ancora selezionato oggetti o si desidera modificare la selezione: scegliere uno o più oggetti dall\'elenco **Forme**.
4.  Effettuare una delle seguenti operazioni:
    -   Selezionare un **Piano di specchiatura** standard dall\'elenco a discesa.
    -   Selezionare un oggetto di riferimento nella [Vista ad albero](Tree_view/it.md) o nella [Vista 3D](3D_view/it.md). L\'oggetto di riferimento può essere qualsiasi faccia planare o bordo circolare.
5.  Premere il pulsante **OK**.
6.  Per ciascun oggetto sorgente viene creato un oggetto Part Specchio separato.

Quando l\'etichetta del pulsante di selezione dice **Selecting** ci si trova in modalità di selezione dei riferimenti ed è attivo un portale di selezione, che non consente la selezione di oggetti di riferimento non supportati. Fare clic sul pulsante per disattivare il portale di selezione, l\'etichetta del pulsante cambia in **Seleziona il riferimento**.

Il piano di specchiatura è definito da un **Normal** (direzione) e da un **Base** (posizione). Quando la proprietà **Mirror Plane** contiene un oggetto di riferimento, queste proprietà vengono rese di sola lettura poiché vengono quindi calcolate in base a tale oggetto. Il piano è infinito anche se l\'oggetto di riferimento non lo è.

Un oggetto di riferimento può essere una faccia planare, ad esempio la faccia di un [Part Cubo](Part_Box/it.md), un bordo circolare, un [Datum Plane](PartDesign_Plane/it.md), un [piano di origine](App_OriginGroupExtension/it.md) di un contenitore [Part](Std_Part/it.md) o qualsiasi oggetto con una singola faccia planare o un singolo bordo circolare. C\'è anche il supporto per [collegamenti (Links)](App_Link/it.md). Si noti, tuttavia, che le superfici B-spline, come [superfici rigate](Part_RuledSurface/it.md) o [facce loft](Part_Loft/it.md) non sono supportate.



## Opzioni

Se viene selezionato un piano standard invece di un oggetto di riferimento, è possibile utilizzare le caselle **Punto base** per spostarlo. Solo una delle caselle **X**, **Y** o **Z** è efficace per un dato piano standard.

  Piano standard   Punto base     Effetto
    
  **XY**           **Z**          Sposta il piano lungo l\'asse **Z**.
  **XY**           **X**, **Y**   Nessun effetto.
  **XZ**           **Y**          Sposta il piano lungo l\'asse **Y**.
  **XZ**           **X**, **Z**   Nessun effetto.
  **YZ**           **X**          Sposta il piano lungo l\'asse **X**.
  **YZ**           **Y**, **Z**   Nessun effetto.



## Note

-   Gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno possono essere utilizzati anche come oggetti di origine. {{Version/it|0.20}}
-   Dopo aver selezionato un piano di specchiatura standard, **Normal** e **Base** dell\'oggetto Part Specchio possono essere modificati su qualsiasi valore. In questo modo anche senza oggetto di riferimento non siete limitati ai piani standard.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/it
