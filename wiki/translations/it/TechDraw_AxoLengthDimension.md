---
 GuiCommand:
   Name: TechDraw AxoHorizontalDimension
   Name/it: TechDraw Quota lineare assonometrica
   MenuLocation: TechDraw , Annotazioni , Quota lineare assonometrica
   Workbenches: TechDraw_Workbench/it
   Version: 0.21
---

# TechDraw AxoLengthDimension/it



## Descrizione

Lo strumento **TechDraw Quota lineare assonometrica** aggiunge una quota lineare ad una vista assonometrica. La quota può essere la lunghezza di un bordo o la distanza tra due punti.

<img alt="" src=images/TechDraw_AxoLengthDimensionExample.png  style="width:300px;"> 
*Quote lineari assonometriche basate su un bordo (blu) e due punti (rosso)*



## Utilizzo

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare due bordi (e1 ed e2 nell\'immagine). Il primo bordo definisce la direzione della linea di misura e la distanza misurata. Il secondo bordo definisce la direzione delle linee di riferimento.
    -   Selezionare due bordi (e3 ed e4 nell\'immagine) e due punti (v1 e v2 nell\'immagine). Il primo bordo definisce la direzione della linea di misura. Il secondo bordo definisce la direzione delle linee di riferimento. I punti determinano la distanza misurata.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_AxoLengthDimension.svg" width=16px> [Quota lineare assonometrica](TechDraw_AxoLengthDimension/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Annotazioni → <img src="images/TechDraw_AxoLengthDimension.svg" width=16px> Quota lineare assonometrica** dal menu.
3.  Alla Vista viene aggiunta una quota assonometrica.
4.  La quota può essere trascinata nella posizione desiderata.
5.  Se necessario, aggiungere tolleranze come descritto in [questa pagina](TechDraw_Geometric_dimensioning_and_tolerancing/it#Tolleranze.md).



### Visualizzazione quotatura 3D 

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Display_3D_measurement.md).


{{VersionPlus/it|0.22}}

: Quando si quotano bordi paralleli agli assi del sistema di coordinate globali, il valore effettivo (3D) viene calcolato automaticamente e inserito nell\'etichetta della quota come testo.



### Cambiare le proprietà 

Per modificare le proprietà di un oggetto quota, fare doppio clic su di esso nel disegno o nella [Vista ad albero](Tree_view/it.md). Si aprirà la [Finestra di dialogo Quota](TechDraw_LengthDimension/it#Finestra_di_dialogo_Quota.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AxoLengthDimension/it
