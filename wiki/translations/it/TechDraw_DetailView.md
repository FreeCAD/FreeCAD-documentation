---
 GuiCommand:
   Name: TechDraw DetailView
   Name/it: TechDraw Vista dettaglio
   MenuLocation: TechDraw , Viste TechDraw , Vista dettaglio
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_View/it
---

# TechDraw DetailView/it



## Descrizione

Lo strumento **TechDraw Vista dettaglio** crea una vista di una piccola area di una vista esistente.

![](images/ViewDetail.png ) 
*Vista dettaglio con contorno circolare*



## Utilizzo

1.  Selezionare una vista di base per la vista di dettaglio.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_DetailView.svg" width=16px> [Inserisci Vista dettaglio](TechDraw_DetailView/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_DetailView.svg" width=16px> Inserisci Vista dettaglio** dal menu.
3.  Un contorno evidenziato viene aggiunto alla vista di base, una vista di dettaglio viene aggiunta alla pagina e si apre un pannello delle azioni.
4.  Per maggiore chiarezza è meglio spostare la vista di dettaglio in modo che non si sovrapponga più alla vista di base: tenere premuto il tasto sinistro del mouse sulla sua cornice o etichetta e trascinarla in una nuova posizione.
5.  Per modificare la posizione del contorno evidenziato, effettuare una delle seguenti operazioni:
    -   Spostare il contorno trascinando:
        1.  Premere il pulsante **Trascina evidenziazione**.
        2.  Il contorno viene contrassegnato sulla pagina e viene aggiunta un\'etichetta temporanea da *trascinare*.
        3.  Tenere premuto il pulsante sinistro del mouse sul contorno stesso o su quell\'etichetta e trascinare il contorno in una nuova posizione.
    -   Spostare il contorno inserendo le coordinate:
        1.  Cambiare le coordinate X e Y nel pannello delle attività. Le coordinate sono relative al centro della vista di base.
6.  Facoltativamente modificare il **Raggio** della vista di dettaglio.
7.  Facoltativamente modificare il **Tipo di scala** e il **Fattore di scala** della vista dettaglio. Vedere [Vista TechDraw](TechDraw_View/it#Proprietà.md) per ulteriori informazioni.
8.  Specificare un\'etichetta **Riferimento**. Questa etichetta verrà visualizzata vicino al contorno evidenziato.
9.  Premere il pulsante **OK**.



## Note

-   Per modificare una vista dettaglio, fare doppio clic su di essa nella [Vista ad albero](Tree_view/it.md).
-   I contorni delle viste di dettaglio possono essere rotondi o quadrati. Ciò è controllato dalla **Forma del contorno della vista di dettaglio** [preferenza](TechDraw_Preferences/it#Annotazione.md).
-   [Argomento del forum con una buona discussione sull\'impostazione dell\'ancoraggio.](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Nelle proprietà della **Base View** si può modificare l\'aspetto del contorno dei dettagli.

Una Vista di Dettaglio, formalmente un oggetto {{Incode|TechDraw::DrawViewDetail}}, è derivata da un oggetto [Part View](TechDraw_View#Properties_Part_View.md), formalmente un oggetto {{Incode|TechDraw::DrawViewPart}} ed eredita tutti le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Appearance}}

-    **Show Matting|Bool**: mostra o nasconde la cornice attorno alla Vista di Dettaglio. {{Version/it|1.0}}

-    **Show Highlight|Bool**: mostra o nasconde l\'evidenziazione dei dettagli nella vista sorgente. {{Version/it|1.0}}


{{TitleProperty|Detail}}

-    **Base View|Link**: la vista su cui si basa la vista di dettaglio.

-    **Anchor Point|Vector**: il centro della vista di dettaglio all\'interno di **Base View**.

-    **Radius|Float**: la dimensione dell\'area in **Base View** visualizzata nella vista dettaglio.

-    **Reference|String**: un identificatore per la vista di dettaglio in **Base View**.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/it
