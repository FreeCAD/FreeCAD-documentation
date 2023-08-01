---
- GuiCommand:/it
   Name:Arch Nest
   Name/it:Nido
   MenuLocation:Arch → Strumenti pannello → Nido
   Workbenches:[Arch](Arch_Workbench/it.md)
   SeeAlso:[Pannello](Arch_Panel/it.md), [Foglio pannello](Arch_Panel_Sheet/it.md)
---

# Arch Nest/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Arch_Nest.svg  style="width:16px;"> Nido consente di selezionare una forma piatta destinata ad essere un contenitore e una serie di altre forme piatte da organizzare all\'interno dello spazio definito dalla forma del contenitore. Tipicamente questo è necessario per le operazioni CNC, in cui si desidera tagliare una serie di pezzi da un pannello di base e si devono organizzare tali pezzi nel modo più compatto possibile in modo che occupino meno spazio sul pannello.


</div>

L\'algoritmo sottostante allo strumento Nido è in continua evoluzione e al momento non è completamente ottimizzato. In futuro le prestazioni di questo strumento dovrebbero migliorare molto.

<img alt="" src=images/Arch_Nest_example.jpg  style="width:600px;">

*L\'immagine sopra mostra una serie di forme prima e dopo l\'operazione di annidamento.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Arch_Nest.svg" width=16px> [Arch Nido](Arch_Nest/it.md)**.
2.  Selezionare un oggetto destinato ad essere il contenitore. Questo oggetto deve essere piatto e, al momento, rettangolare.
3.  Cliccare sul pulsante **Pick container** per usare l\'oggetto come contenitore.
4.  Selezionare una serie di altri oggetti piatti che desidera posizionare all\'interno del contenitore. Questi oggetti devono essere tutti piatti e nello stesso piano del contenitore.
5.  Regolare le opzioni desiderate.
6.  Avviare il processo di calcolo.
7.  Alla fine del calcolo, fare clic sul pulsante **Anteprima** per creare un\'anteprima temporanea del risultato.
8.  Se si desidera applicare il risultato (spostare e ruotare effettivamente le forme nella posizione), fare clic su **OK**.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Nest_panel.jpg  style="width:800px;"> 
*Il pannello Azioni per lo strumento [Nido](Arch_Nest/it.md)*


</div>

## Note

-   Tutti gli oggetti devono avere una faccia
-   Al momento lo strumento funziona solo con oggetti piatti che hanno tutti lo stesso orientamento.
-   Al momento, il contenitore deve essere rettangolare.
-   Al momento, il margine o la spaziatura tra i pezzi non sono ancora implementati
-   Se ci sono tanti oggetti il calcolo può richiedere molto tempo. Questo sarà ottimizzato in futuro


<div class="mw-translate-fuzzy">


{{docnav/it
|[Foglio pannello](Arch_Panel_Sheet/it.md)
|[Carpenteria](Arch_Frame/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_Panel_Sheet.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Frame.svg
}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Nest/it
