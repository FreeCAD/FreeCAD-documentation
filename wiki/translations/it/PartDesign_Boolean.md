---
- GuiCommand:/it
   Name:PartDesign Boolean
   Name/it:Operazioni booleane
   MenuLocation:Part Design → Operazioni booleane
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   Version:0.17
---

# PartDesign Boolean/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

**PartDesign Booleane** importa uno o più [Corpi PartDesign](PartDesign_Body.md) o [Cloni PartDesign](PartDesign_Clone.md) (designati come \"tool bodies\") nel corpo PartDesign attivo e applica un\'operazione booleana (fusione, taglio o comune).


</div>

![](images/PartDesign_Boolean_example.png )



*A sinistra il corpo attivo (A) con i corpi utensile (B) e (C); a destra il risultato dopo un taglio booleano.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Attivare il corpo che deve ricevere l\'operazione booleana. ***Nota**: È importante che né il corpo attivo né alcuna delle caratteristiche in esso contenute siano selezionati!*
2.  Premere il pulsante **<img src="images/PartDesign_Boolean.svg" width=24px> '''Booleana'''**.
3.  In **Parametri Booleana**, cliccare sul pulsante **Aggiungi corpo**. Il corpo attivo scompare temporaneamente dalla vista 3D per facilitare la selezione del corpo utensile.
4.  Nella vista 3D, selezionare il corpo da usare nella funzione booleana. Ripetere per aggiungere altri corpi.
5.  Selezionare il tipo di operazione booleana nel menu a discesa (Fuse, Cut o Common)
6.  Cliccare su **OK**.

In alternativa, è possibile selezionare uno o più Corpi prima di premere il pulsante Booleana; essi vengono aggiunti automaticamente.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   **Fuse:** unisce il corpo strumento o i corpi al corpo attivo.
-   **Cut:** sottrae il corpo strumento o i corpi dal corpo attivo.
-   **Common:** estrae l\'intersezione del corpo strumento o dei corpi con il corpo attivo.
-   Premere il pulsante **Rimuovi corpo** per rimuovere un corpo, selezionandolo nella vista 3D.


</div>

## Proprietà

-    {{PropertyData/it|Type}}: imposta l\'operazione booleana (Fuse, Cut, Common)

-    {{PropertyData/it|Label}}: nome dato all\'operazione, questo nome può essere cambiato a piacere.

-    {{PropertyData/it|Group}}: elenca i corpi strumento.

-    {{PropertyView/it|Display}}: imposta la visualizzazione tra 2 modalità:

    -   Result (default): visualizza il risultato della funzione booleana. In questa modalità, i Corpi degli strumenti non possono essere visualizzati nel loro stato originale, anche quando viene attivata la loro visibilità.
    -   Tools: visualizza i Corpi utensile nel loro stato originale. Questa modalità è utile quando è necessario modificare i corpi strumento.

-    {{PropertyView/it|Selectable}}: true o false. Se impostato su false, la funzione non può essere selezionata nella vista 3D.

-    {{PropertyView/it|Visibility}}: true o false. Attiva / disattiva la visibilità della funzione nella vista 3D.

## Limitazioni

-   Affinché Common funzioni con più di un corpo utensile, tutti i corpi devono intersecarsi tra loro e con il Corpo attivo.
-   I corpi utensile adottano l\'origine locale del corpo attivo. Se il corpo attivo non si trova in (0,0,0) nel sistema di coordinate globali, la posizione dei corpi utensile deve essere relativa al corpo attivo. Potrebbe essere più semplice lasciare il posizionamento del Corpo attivo nell\'origine prima di applicare l\'operazione booleana, e poi cambiare la sua posizione dopo l\'operazione.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Boolean/it
