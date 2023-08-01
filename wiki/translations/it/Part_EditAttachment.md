---
- GuiCommand:
   Name: Part Attachment
   Name/it: Part Allegato
   MenuLocation: Part - Allegato...
   Workbenches: [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md)
   Version: 0.17
   SeeAlso: [Posizionamento](Placement/it.md), [Tutorial di base sugli allegati](Basic_Attachment_Tutorial/it.md), [Part Parte2DOggetto](Part_Part2DObject/it.md)
---

# Part EditAttachment/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

**Allegato** è un\'utilità per allegare un oggetto a un altro. L\'oggetto allegato è collegato all\'altro oggetto, il che significa che se il posizionamento di quest\'ultimo viene cambiato in seguito, l\'oggetto allegato si aggiornerà alla sua nuova posizione.


</div>

## Utilizzo

1.  Seleziona l\'oggetto da allegare.
2.  Andare al menu **Parte → Allegato\...**.

    :   **Nota**\': quando si lavora in [PartDesign](PartDesign_Workbench/it.md) e si creano schizzi, geometrie di riferimento o primitive, i passi 1 e 2 non sono necessari: il dialogo allegato si apre automaticamente.
3.  Sotto i parametri **Allegato**, si può leggere *Non allegato*. Il primo pulsante sotto è etichettato **Selecting...** per indicare che si aspetta una selezione nella vista 3D.
4.  Seleziona un elemento topologico sull\'oggetto da attaccare: vertice, bordo o faccia/piano. Sono selezionabili anche i dati geometrici dai contenitori [Part](Std_Part.md).
5.  L\'etichetta del primo pulsante ora adotta il tipo di topologia selezionata. Nel campo bianco alla sua destra, viene aggiunto l\'oggetto di riferimento e il suo elemento. Per esempio, se viene selezionata una faccia su un cubo primitivo, il campo mostrerà Box:Face6.
6.  Seleziona un [Modo di allegato](#Modo_di_allegato.md) nella lista. Le modalità disponibili sono filtrate dai riferimenti selezionati. *Allegato con modalità * verrà visualizzato sotto l\'intestazione *Allegato*.

    :   Per informazioni dal vivo sulle modalità di allegato, passa il mouse sopra una delle modalità nella lista per far apparire un punta dell'utensile .
7.  Facoltativamente, aggiungi fino a 3 ulteriori riferimenti premendo i pulsanti **Riferimento2**, **Riferimento3**, e **Riferimento4** e ripetendo il passo 4.
8.  Imposta opzionalmente un [Allegato Spostamento](#Attachment_Offset/it.md).
9.  Premi **OK**.

## Opzioni


<div class="mw-translate-fuzzy">

![](images/Part_Offset_Tasks_it.png )


</div>

### Modalità di allegato 

#### Disattivato

Predefinito, nessun riferimento selezionato.

#### Normale a bordo 

L\'oggetto è reso perpendicolare al bordo. Riferimento facoltativo ad un vertice definisce la posizione.

:; Combinazioni di riferimenti:

:   Bordo
:   Bordo, Vertice
:   Vertice, Bordo

See [Align O-X-Y type attachment modes](O-X-Y_type_attachment_modes.md) for more details on the following modes:


<div class="mw-translate-fuzzy">

#### Allinea O-N-X 


</div>

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento, poi allinea la sua normale e l\'asse del piano orizzontale verso il vertice/la linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Edge
:   Vertice, Vertice, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo


<div class="mw-translate-fuzzy">

#### Allinea O-N-Y 


</div>

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea la sua normale e l\'asse verticale del piano verso il vertice/la linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Edge
:   Vertice, Vertice, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo

#### Allinea O-X-Y 

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea i suoi assi orizzontali e verticali del piano verso il vertice/la linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Bordo
:   Vertice, Vertice, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo


<div class="mw-translate-fuzzy">

#### Allinea O-X-N 


</div>

Fa corrispondere l\'origine dell\'oggetto con il primo vertice referenziato e allinea il suo asse del piano orizzontale e la normale al vertice/alla linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Bordo
:   Vertice, Bordo, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo


<div class="mw-translate-fuzzy">

#### Allinea O-Y-N 


</div>

Fa corrispondere l\'origine dell\'oggetto con il primo vertice referenziato e allinea il suo asse del piano verticale e la normale al vertice/alla linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Bordo
:   Vertice, Bordo, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo

#### Allinea O-Y-X 

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea i suoi assi del piano verticale e orizzontale verso il vertice/la linea.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Bordo
:   Vertice, Bordo, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo

#### Traduci l\'origine 

L\'origine dell\'oggetto è allineata al vertice corrispondente. L\'orientamento è controllato dalla proprietà [Posizionamento](Placement/it.md).

:; Combinazioni di riferimenti:

:   Vertice.

#### XY dell\'oggetto 

Il piano è allineato al piano locale XY dell\'oggetto collegato.

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.

#### XZ dell\'oggetto 

Il piano è allineato al piano locale XZ dell\'oggetto collegato.

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.

#### YZ dell\'oggetto 

Il piano è allineato al piano locale YZ dell\'oggetto collegato.

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.

#### Piano della faccia 

Il piano è allineato in modo da coincidere con la faccia planare.

:; Combinazioni di riferimenti:

:   Piano

#### Tangente a superficie 

Il piano è reso tangente alla superficie nel vertice.

:; Combinazioni di riferimenti:

:   Faccia, Vertice
:   Vertice, Faccia

#### Frenet NB 

Il piano è impostato su assi normali-binormali (NB) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice (o definito dalla proprietà MapPathParameter, se il vertice non è riferito). L\'origine dell\'oggetto viene traslata nel vertice se il vertice è il primo riferimento, o mantenuta sulla curva se il bordo è il primo riferimento. Questa modalità è simile a \"Normale a bordo\", eccetto che l\'asse X è ben definito.

:; Combinazioni di riferimenti:

:   Curva
:   Curva, Vertice
:   Vertice, Curva
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

#### Frenet TN 

Il piano è impostato sugli assi tangente-normali (TN) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice (o definito dalla proprietà MapPathParameter, se il vertice non è referenziato). L\'origine dello schizzo è traslata nel vertice se il vertice è il primo riferimento, o mantenuto alla curva se il bordo è il primo riferimento. In effetti, se la curva è planare, il piano dello schizzo è il piano della curva.

:; Combinazioni di riferimenti:

:   Curva
:   Curva, Vertice
:   Vertice, Curva
:   <img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

#### Frenet TB 

Il piano è impostato su assi tangenti-binormali (TB) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice ( o definito dalla proprietà MapPathParameter, se il vertice non è referenziato). L\'origine dello schizzo è traslata nel vertice se il vertice è il primo riferimento, o mantenuto alla curva se il bordo è il primo riferimento.

:; Combinazioni di riferimenti:

:   Curva
:   Curva, Vertice
:   Vertice, Curva
:   <img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

#### Concentrico

Allinea al piano del cerchio osculatore di un bordo. Un riferimento opzionale ad un vertice definisce dove.

:; Combinazioni di riferimenti:

:   Curva
:   Cerchio
:   Curva, Vertice
:   Cerchio, Vertice
:   Vertice, Curva
:   Vertice, Cerchio

#### Sezione di rivoluzione 

Il piano è perpendicolare al bordo e l\'asse Y è abbinato all\'asse del cerchio osculatore. Un riferimento opzionale ad un vertice definisce dove.

:; Combinazioni di riferimenti:

:   Curva
:   Cerchio
:   Curva, Vertice
:   Cerchio, Vertice
:   Vertice, Curva
:   Vertice, Cerchio

#### Piano da 3 punti 

Allinea il piano XY attraverso tre vertici.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Linea, Vertice
:   Vertice, Linea
:   Linea, Linea

#### Normale a 3 punti 

Allinea il piano attraverso i primi due vertici e perpendicolare al piano che passa attraverso 3 vertici.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Linea, Vertice
:   Vertice, Linea
:   Linea, Linea

#### Pieghevole


<div class="mw-translate-fuzzy">

Modalità speciale per piegare i poliedri. Selezionare 4 bordi nell\'ordine: bordo pieghevole, linea di piegatura, altra linea di piegatura, altro bordo pieghevole. Il piano è allineato per piegare il primo bordo. Nell\'immagine seguente, non è necessario che entrambe le foglie da piegare siano uguali.


</div>

:; Combinazioni di riferimenti:

:   Linea, Linea, Linea, Linea
:   ![ 250px](images/Attacher_mode_Folding.png )

#### Inerzia 2-3 

L\'oggetto viene collegato a un piano che passa attraverso il secondo e il terzo asse principale di inerzia (passa attraverso il centro di massa).

:; Combinazioni di riferimenti:

:   Qualsiasi
:   Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi, Qualsiasi

### Allegato Spostamento 

Allegato Spostamento viene utilizzato per applicare uno spostamento lineare o rotatorio dall\'oggetto di riferimento. Ciò significa che gli spostamento sono relativi al sistema di coordinate \"locale\", non al sistema globale. Diventa attivo quando è stata selezionata una modalità di associazione diversa da \"Disattivato\".

-   **X**: imposta una distanza di spostamento sull\'asse X dell\'oggetto di riferimento.

-   **Y**: imposta una distanza di spostamento nell\'asse Y dell\'oggetto di riferimento.

-   **Z**: imposta una distanza di spostamento nell\'asse Z dell\'oggetto di riferimento. Questa coordinata deve essere utilizzata nel caso frequente in cui si desidera spostare uno schizzo in direzione perpendicolare al piano.

-   **Imbardata**: ruota l\'oggetto associato lungo l\'asse Z dell\'oggetto di riferimento.

-   **Beccheggio**: ruota l\'oggetto associato lungo l\'asse Y dell\'oggetto di riferimento.

-   **Rollio**: ruota l\'oggetto associato lungo l\'asse X dell\'oggetto di riferimento.

-   **Capovolgi le facce**: se selezionato, l\'oggetto collegato viene invertito sul suo piano XY.

## Limitazioni

-   I contenitori [Part](Std_Part/it.md) e [Corpo](PartDesign_Body/it.md) non sono supportati. Mentre è possibile usare Allegato per allinearli, l\'allegato non sarà collegato parametricamente.
-   Se selezionando due linee si ottiene un traceback con \"i punti sono collineari. Non si può fare un piano\", prova invece a selezionare tre punti [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).

!!FUZZY!!


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/it
