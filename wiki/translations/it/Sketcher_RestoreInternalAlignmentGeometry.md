---
- GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/it: Mostra/Nascondi la geometria interna
   MenuLocation: Sketch - Strumenti - Mostra/Nascondi la geometria interna
   Workbenches: [Sketcher](Sketcher_Workbench/it.md)
   Shortcut: Ctrl+Shift+E
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/it



## Descrizione

Il comando elimina gli elementi di allineamento della geometria interna inutilizzati, o ricrea quelli mancanti.



## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare un elemento di uno schizzo che supporta l\'allineamento interno (attualmente solo Ellisse o Arco di ellisse e B-spline).
-   Richiamare il comando cliccando sul pulsante <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.png  style="width:24px;"> della barra degli strumenti, o scegliendo la voce del menu ** Sketch** → **Strumenti** → **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.png" width=24px> Mostra/Nascondi la geometria interna **, o utilizzando la scorciatoia da tastiera.
    -   Se nell\'elemento selezionato ci sono dei posti liberi per l\'allineamento (ad esempio, è stato cancellato un diametro) , viene creata una nuova geometria di costruzione e viene allineata nei posti disponibili.
    -   Se tutti i posti di allineamento sono occupati, la geometria interna inutilizzata viene eliminato (l\'elemento viene trattato come inutilizzato se non è vincolato a nient\'altro).


</div>



## Esempio


<div class="mw-translate-fuzzy">

1.  Creare una nuova ellisse. Le nuove ellissi sono sempre costruite in modo completo, con tutti gli elementi. Vedrete una ellisse e un gruppo di geometrie di costruzione: diametro maggiore, diametro minore e i fuochi.
2.  Selezionare la linea del diametro minore e premere **Canc**. Il diametro sparisce, ma l\'ellisse rimane. Come recuperare il diametro?
3.  Selezionare l\'ellisse e invocare il comando **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.png" width=24px>**. Il diametro viene ripristinato.
4.  Ora, vincolare il diametro maggiore dell\'ellisse a una certa lunghezza. Selezionare l\'ellisse e invocare il comando **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.png" width=24px>**.

**Risultato:** Il diametro minore e i fuochi vengono eliminati, ma il diametro maggiore viene mantenuto, perché partecipa ad altri vincoli. Anche il centro dell\'ellipse rimane, perché è inerente, come il centro di un cerchio.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/it
