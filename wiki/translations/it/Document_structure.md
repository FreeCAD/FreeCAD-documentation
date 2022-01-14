# Document structure/it
{{TOCright}}

![](images/Screenshot_treeview.jpg ) Un documento FreeCAD contiene tutti gli oggetti della scena. Può contenere i gruppi e gli oggetti realizzati con qualsiasi ambiente di lavoro. Si possono quindi alternare gli ambienti pur continuando a lavorare sullo stesso documento. Il documento è ciò che viene salvato sul disco quando si salva il proprio lavoro. Inoltre, in FreeCAD è possibile aprire più documenti contemporaneamente, e aprire diverse viste dello stesso documento.

All\'interno del documento, gli oggetti possono essere raggruppati, e avere un unico nome. La gestione dei gruppi, degli oggetti e dei nomi degli oggetti avviene prevalentemente nella [vista a albero](Tree_view/it.md). **Nota:** Naturalmente, queste operazioni, come tutto in FreeCAD, si possono eseguire anche tramite interprete [Python](Python/it.md).

Nella [vista a albero](Tree_view/it.md), è possibile creare dei <img alt="" src=images/Std_Group.svg  style="width:16px;"> [gruppi](Std_Group/it.md), spostare gruppi di oggetti, eliminare oggetti o gruppi, facendo clic destro nella [vista a albero](Tree_view/it.md) o su un oggetto, oppure rinominare gli oggetti facendo doppio clic sui loro nomi, o eventualmente eseguire altre operazioni, attinenti l\'ambiente di lavoro attivo.

Un documento FreeCAD può contenere oggetti di diversi tipi. Ogni ambiente di lavoro crea oggetti di tipo specifico, per esempio <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh](Mesh_Workbench/it.md) crea oggetti Mesh , <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Parte](Part_Workbench/it.md) crea oggetti Parte, <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/it.md) crea disegni e anche oggetti Parte, ecc.

In FreeCAD può essere attivo un solo documento alla volta. Il documento attivo è quello che viene visualizzato nella vista 3D corrente ed è il documento in lavorazione.

## Applicazione e Interfaccia utente 

Come per quasi tutto il resto, in FreeCAD, la parte interfaccia grafica utente (GUI) è separata dalla parte applicazione (App). Questo vale anche per i documenti.

I documenti sono composti da due parti: il documento **Applicazione**, che contiene gli oggetti, e il documento **Visualizzazione**, che contiene la rappresentazione degli oggetti sullo schermo.

Pensate a due spazi in cui sono definiti gli oggetti. I loro parametri costruttivi (si tratta di un cubo? di un cono? quanto misura?) sono memorizzati nel documento *Applicazione*, mentre la loro rappresentazione grafica (è disegnata con linee nere? con le facce blu?) sono memorizzati nel documento *Visualizzazione*. Questo permette di utilizzare FreeCAD anche senza interfaccia grafica, ad esempio all\'interno di altri programmi, e di manipolare gli oggetti, anche senza disegnare nulla sullo schermo.

Il documento Visualizzazione contiene anche le viste 3D. Un documento può avere contemporaneamente diverse viste aperte, in modo da poterlo controllare da diversi punti di vista. Ad esempio, si può visualizzare allo stesso tempo una vista dall\'alto e una vista frontale. Tutte le viste dello stesso progetto vengono memorizzate nel documento Visualizzazione. La produzione di nuove viste o la chiusura di viste attive si può fare dal menu Visualizza o facendo clic destro su una scheda di visualizzazione.

## Script

Tramite l\'interprete [ Python](Python/it.md), si può facilmente accedere, creare o modificare i documenti. Ad esempio: 
```python
FreeCAD.ActiveDocument
``` Restituisce il documento corrente (attivo) 
```python
FreeCAD.ActiveDocument.Blob
``` Accede ad un oggetto chiamato \"Blob\" all\'interno del documento 
```python
FreeCADGui.ActiveDocument
``` Restituisce il documento associato al documento corrente 
```python
FreeCADGui.ActiveDocument.Blob
``` Accede alla rappresentazione grafica (visualizza) l\'oggetto \"Blob\" 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Restituisce la vista corrente

---
[documentation index](../README.md) > Document structure/it
