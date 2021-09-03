 {{TOCright}}


<div class="mw-translate-fuzzy">

## Descrizione

Come nella maggior parte delle applicazioni è presente una funzionalità per duplicare gli oggetti (paragrafi, celle di fogli di calcolo, immagini, ecc.). Gli oggetti di un [documento](Document_structure/it.md) possono essere copiati liberamente all\'interno dello stesso documento o tra documenti diversi utilizzando i comandi **<img src="images/Std_Copy.svg" width=24px> [Copia](Std_Copy/it.md)**, **<img src="images/Std_Paste.svg" width=24px> [Incolla](Std_Paste/it.md)** e **[Duplica la selezione](Std_DuplicateSelection/it.md)**.


</div>

![](images/Copy_past_duplicate.png )

Ricordare che gli oggetti duplicati con copia-incolla non dipendono dall\'originale. Se si desiderano dei cloni dipendenti, utilizzare il <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Clone di Draft](Draft_Clone/it.md) o il <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;">[Clone di Part Design](PartDesign_Clone/it.md). Se non c\'è bisogno di un clone dipendente o di una replica parametrica, si può anche usare <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [Crea una copia semplice](Part_SimpleCopy/it.md) di Part. Per i cloni con motivi, consultare la sezione [Altri metodi](Copying_Objects/it#Altri_metodi.md) di questa pagina.


<div class="mw-translate-fuzzy">

## Copia di oggetti collegati 

Gli oggetti di un [Documento](Document_structure/it.md) possono essere collegati ad altri oggetti (ad esempio, una funzione di estrusione è legata al suo schizzo e una fusione è legata ai suoi componenti). Per questo gli oggetti da copiare vanno selezionati con attenzione.


</div>


<div class="mw-translate-fuzzy">

Se viene selezionato un oggetto senza selezionare i suoi figli, i figli non sono duplicati automaticamente dal comando Copia/Incolla o Duplica Selezione. In questo caso, l\'oggetto copiato può avere un comportamento imprevisto a causa dei collegamenti mancanti.


</div>

In general, recommended practice is to select all dependent objects when copying a parent object.


<div class="mw-translate-fuzzy">

In generale, durante la copia di un oggetto genitore si raccomanda di selezionare anche tutti gli oggetti dipendenti.

## Trovare e Posizionare un oggetto duplicato 

Dopo l\'operazione di copia/incolla, il nuovo oggetto può non essere visibile nella finestra del documento. Questo succede perché il nuovo oggetto ha la stessa proprietà [Placement](Placement/it.md) dell\'originale. Commutare la proprietà Visibility dell\'oggetto originale con la barra spaziatrice **Spazio** per nasconderlo. Quindi utilizzare la finestra di Posizionamento per spostare la copia nella sua posizione corretta.


</div>


<div class="mw-translate-fuzzy">

## Altri metodi 

Come per la maggior parte delle operazioni, anche per fare le copie, in FreeCAD ci sono molti modi. Per ulteriori idee, vedere:

-   PartDesign: [Rifletti](PartDesign_Mirrored/it.md), [Schiera lineare](PartDesign_LinearPattern/it.md), [Schiera polare](PartDesign_PolarPattern/it.md), [Multi Trasformazione](PartDesign_MultiTransform/it.md)
-   Part: [Specchia](Part_Mirror/it.md), [Crea semplice copia](Part_SimpleCopy/it.md)
-   Draft: [Offset](Draft_Offset/it.md), [Scala](Draft_Scale/it.md), [Schiera](Draft_Array/it.md), [PathArray](Draft_PathArray/it.md), [Clona](Draft_Clone/it.md), [Simmetria](Draft_Mirror/it.md)

## Note

-   Dalla versione 0.14, se un oggetto da copiare è collegato a oggetti non selezionati, FreeCAD chiede se gli oggetti non selezionati devono essere inclusi nell\'operazione di copia.


</div>

## Notes

-   If an object to be copied has links to object(s) not in the selection, FreeCAD will ask if the unselected objects should be included in the copy operation. <small>(v0.14)</small> 

## Altro

-   [Copia](Std_Copy/it.md)
-   [Incolla](Std_Paste/it.md)
-   [Duplica la selezione](Std_DuplicateSelection/it.md)



