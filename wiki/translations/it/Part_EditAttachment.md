---
 GuiCommand:
   Name: Part Attachment
   Name/it: Part Allegato
   MenuLocation: Part , Allegato...
   Workbenches: Part_Workbench/it, PartDesign_Workbench/it
   Version: 0.17
   SeeAlso: Placement/it, Basic_Attachment_Tutorial/it, Part_Part2DObject/it
---

# Part EditAttachment/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

**Allegato** è un\'utilità per allegare un oggetto a un altro. L\'oggetto allegato è collegato all\'altro oggetto, il che significa che se il posizionamento di quest\'ultimo viene cambiato in seguito, l\'oggetto allegato si aggiornerà alla sua nuova posizione.


</div>

## Attach engines 

The attachment of an object is controlled by one of four attach engines. The default engine that is used for an object depends on its type.

The four engines are:

-   [Attacher::AttachEnginePoint](#Attacher:_AttachEnginePoint.md)
-   [Attacher::AttachEngineLine](#Attacher:_AttachEngineLine.md)
-   [Attacher::AttachEnginePlane](#Attacher:_AttachEnginePlane.md)
-   [Attacher::AttachEngine3D](#Attacher:_AttachEngine3D.md)

The rest of this page focuses on the AttachEngine3D. The modes of the other engines are only listed. Note that the modes of AttachEnginePlane are in fact identical to those of AttachEngine3D.



## Utilizzo


<div class="mw-translate-fuzzy">

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


</div>

## Change attach engine 

It is possible to manually change the attach engine of an object:

1.  Select the object.
2.  Right-click in the [Property editor](Property_editor.md) and select **Show all** from the context menu.
3.  Edit the **Attacher Type** property of the object.

## Attachment modes 


<div class="toccolours mw-collapsible mw-collapsed">

### Attacher::AttachEnginePoint


<div class="mw-collapsible-content">

-   Deactivated
-   Object\'s origin
-   Focus1
-   Focus2
-   On edge
-   Center of curvature
-   Center of mass
-   Vertex
-   Proximity point 1
-   Proximity point 2


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Attacher::AttachEngineLine


<div class="mw-collapsible-content">

-   Deactivated
-   Object\'s X
-   Object\'s Y
-   Object\'s Z
-   Axis of curvature
-   Directrix1
-   Directrix2
-   Asymptote1
-   Asymptote2
-   Tangent
-   Normal to edge
-   Binormal
-   Through two points
-   Proximity line
-   1st principal axis
-   2nd principal axis
-   3rd principal axis
-   Normal to surface


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Attacher::AttachEnginePlane


<div class="mw-collapsible-content">

-   Deactivated
-   Translate origin
-   Object\'s XY
-   Object\'s XZ
-   Object\'s YZ
-   Plane face
-   Tangent to surface
-   Normal to edge
-   Frenet NB
-   Frenet TN
-   Frenet TB
-   Concentric
-   Revolution Section
-   Plane by 3 points
-   Normal to 3 points
-   Folding
-   Inertia 2-3
-   Align O-N-X
-   Align O-N-Y
-   Align O-X-Y
-   Align O-X-N
-   Align O-Y-N
-   Align O-Y-X


</div>


</div>

### Attacher::AttachEngine3D


<div class="mw-translate-fuzzy">

![](images/Part_Offset_Tasks_it.png )


</div>



#### Disattivato

Attachment is disabled. The object can be moved by editing its [Placement](Placement.md) property.



#### Traduci l\'origine 


<div class="mw-translate-fuzzy">

L\'origine dell\'oggetto è allineata al vertice corrispondente. L\'orientamento è controllato dalla proprietà [Posizionamento](Placement/it.md).


</div>

:; Combinazioni di riferimenti:

:   Vertice.




<div class="mw-translate-fuzzy">

#### XY dell\'oggetto 


</div>


<div class="mw-translate-fuzzy">

Il piano è allineato al piano locale XY dell\'oggetto collegato.


</div>


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.


</div>




<div class="mw-translate-fuzzy">

#### XZ dell\'oggetto 


</div>


<div class="mw-translate-fuzzy">

Il piano è allineato al piano locale XZ dell\'oggetto collegato.


</div>


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.


</div>




<div class="mw-translate-fuzzy">

#### YZ dell\'oggetto 


</div>


<div class="mw-translate-fuzzy">

Il piano è allineato al piano locale YZ dell\'oggetto collegato.


</div>


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Qualsiasi, Conico.


</div>




<div class="mw-translate-fuzzy">

#### Piano della faccia 


</div>


<div class="mw-translate-fuzzy">

Il piano è allineato in modo da coincidere con la faccia planare.


</div>

:; Combinazioni di riferimenti:

:   Piano




<div class="mw-translate-fuzzy">

#### Tangente a superficie 


</div>


<div class="mw-translate-fuzzy">

Il piano è reso tangente alla superficie nel vertice.


</div>

:; Combinazioni di riferimenti:

:   Faccia, Vertice
:   Vertice, Faccia




<div class="mw-translate-fuzzy">

#### Normale a bordo 


</div>


<div class="mw-translate-fuzzy">

L\'oggetto è reso perpendicolare al bordo. Riferimento facoltativo ad un vertice definisce la posizione.


</div>

If no vertex is linked the **Map Path Parameter** property determines the point.

:; Combinazioni di riferimenti:

:   Bordo
:   Bordo, Vertice
:   Vertice, Bordo




<div class="mw-translate-fuzzy">

#### Frenet NB 


</div>

<img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">


<div class="mw-translate-fuzzy">

Il piano è impostato su assi normali-binormali (NB) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice (o definito dalla proprietà MapPathParameter, se il vertice non è riferito). L\'origine dell\'oggetto viene traslata nel vertice se il vertice è il primo riferimento, o mantenuta sulla curva se il bordo è il primo riferimento. Questa modalità è simile a \"Normale a bordo\", eccetto che l\'asse X è ben definito.


</div>

If no vertex is linked the **Map Path Parameter** property determines the point. The object\'s origin is translated to the vertex if the vertex is first, or kept at the curve if the curve is first.

*Frenet NBT* is similar to *Z tangent to edge*, except that the X axis is well-defined.


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Curva
:   Curva, Vertice
:   Vertice, Curva
:   <img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">


</div>




<div class="mw-translate-fuzzy">

#### Frenet TN 


</div>

<img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">


<div class="mw-translate-fuzzy">

Il piano è impostato sugli assi tangente-normali (TN) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice (o definito dalla proprietà MapPathParameter, se il vertice non è referenziato). L\'origine dello schizzo è traslata nel vertice se il vertice è il primo riferimento, o mantenuto alla curva se il bordo è il primo riferimento. In effetti, se la curva è planare, il piano dello schizzo è il piano della curva.


</div>

See [Frenet NBT](#Frenet_NBT.md).




<div class="mw-translate-fuzzy">

#### Frenet TB 


</div>

<img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">


<div class="mw-translate-fuzzy">

Il piano è impostato su assi tangenti-binormali (TB) dalle [Frenet-Serret coordinates](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) nel punto del bordo della curva più vicino al vertice ( o definito dalla proprietà MapPathParameter, se il vertice non è referenziato). L\'origine dello schizzo è traslata nel vertice se il vertice è il primo riferimento, o mantenuto alla curva se il bordo è il primo riferimento.


</div>

See [Frenet NBT](#Frenet_NBT.md).



#### Concentrico


<div class="mw-translate-fuzzy">

Allinea al piano del cerchio osculatore di un bordo. Un riferimento opzionale ad un vertice definisce dove.


</div>

If no vertex is linked the **Map Path Parameter** property determines the point.

:; Combinazioni di riferimenti:

:   Curva
:   Cerchio
:   Curva, Vertice
:   Cerchio, Vertice
:   Vertice, Curva
:   Vertice, Cerchio



#### Sezione di rivoluzione 


<div class="mw-translate-fuzzy">

Il piano è perpendicolare al bordo e l\'asse Y è abbinato all\'asse del cerchio osculatore. Un riferimento opzionale ad un vertice definisce dove.


</div>

See [Concentric](#Concentric.md).




<div class="mw-translate-fuzzy">

#### Piano da 3 punti 


</div>


<div class="mw-translate-fuzzy">

Allinea il piano XY attraverso tre vertici.


</div>

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Linea, Vertice
:   Vertice, Linea
:   Linea, Linea




<div class="mw-translate-fuzzy">

#### Normale a 3 punti 


</div>


<div class="mw-translate-fuzzy">

Allinea il piano attraverso i primi due vertici e perpendicolare al piano che passa attraverso 3 vertici.


</div>

See [XY plane by 3 points](#XY_plane_by_3_points.md).



#### Pieghevole

<img alt="" src=images/Attacher_mode_Folding.png  style="width:250px;">


<div class="mw-translate-fuzzy">

Modalità speciale per piegare i poliedri. Selezionare 4 bordi nell\'ordine: bordo pieghevole, linea di piegatura, altra linea di piegatura, altro bordo pieghevole. Il piano è allineato per piegare il primo bordo. Nell\'immagine seguente, non è necessario che entrambe le foglie da piegare siano uguali.


</div>


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Linea, Linea, Linea, Linea
:   ![ 250px](images/Attacher_mode_Folding.png )


</div>




<div class="mw-translate-fuzzy">

#### Inerzia 2-3 


</div>


<div class="mw-translate-fuzzy">

L\'oggetto viene collegato a un piano che passa attraverso il secondo e il terzo asse principale di inerzia (passa attraverso il centro di massa).


</div>

:; Combinazioni di riferimenti:

:   Qualsiasi
:   Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi, Qualsiasi




<div class="mw-translate-fuzzy">

#### Allinea O-N-X 


</div>


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento, poi allinea la sua normale e l\'asse del piano orizzontale verso il vertice/la linea.


</div>

See [Align O-X-Y Type Attachment Modes](O-X-Y_Type_Attachment_Modes.md) for more details.


<div class="mw-translate-fuzzy">

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Edge
:   Vertice, Vertice, Vertice
:   Vertice, Bordo, Bordo
:   Vertice, Vertice
:   Vertice, Bordo


</div>




<div class="mw-translate-fuzzy">

#### Allinea O-N-Y 


</div>


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea la sua normale e l\'asse verticale del piano verso il vertice/la linea.


</div>

See [Align O-Z-X](#Align_O-Z-X.md).



#### Allinea O-X-Y 


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea i suoi assi orizzontali e verticali del piano verso il vertice/la linea.


</div>

See [Align O-Z-X](#Align_O-Z-X.md).




<div class="mw-translate-fuzzy">

#### Allinea O-X-N 


</div>


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice referenziato e allinea il suo asse del piano orizzontale e la normale al vertice/alla linea.


</div>

See [Align O-Z-X](#Align_O-Z-X.md).




<div class="mw-translate-fuzzy">

#### Allinea O-Y-N 


</div>


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice referenziato e allinea il suo asse del piano verticale e la normale al vertice/alla linea.


</div>

See [Align O-Z-X](#Align_O-Z-X.md).



#### Allinea O-Y-X 


<div class="mw-translate-fuzzy">

Fa corrispondere l\'origine dell\'oggetto con il primo vertice di riferimento e allinea i suoi assi del piano verticale e orizzontale verso il vertice/la linea.


</div>

See [Align O-Z-X](#Align_O-Z-X.md).




<div class="mw-translate-fuzzy">

### Allegato Spostamento 


</div>


<div class="mw-translate-fuzzy">

Allegato Spostamento viene utilizzato per applicare uno spostamento lineare o rotatorio dall\'oggetto di riferimento. Ciò significa che gli spostamento sono relativi al sistema di coordinate \"locale\", non al sistema globale. Diventa attivo quando è stata selezionata una modalità di associazione diversa da \"Disattivato\".


</div>


<div class="mw-translate-fuzzy">

-   **X**: imposta una distanza di spostamento sull\'asse X dell\'oggetto di riferimento.


</div>


<div class="mw-translate-fuzzy">

-   **Y**: imposta una distanza di spostamento nell\'asse Y dell\'oggetto di riferimento.


</div>


<div class="mw-translate-fuzzy">

-   **Z**: imposta una distanza di spostamento nell\'asse Z dell\'oggetto di riferimento. Questa coordinata deve essere utilizzata nel caso frequente in cui si desidera spostare uno schizzo in direzione perpendicolare al piano.


</div>


<div class="mw-translate-fuzzy">

-   **Rollio**: ruota l\'oggetto associato lungo l\'asse X dell\'oggetto di riferimento.


</div>


<div class="mw-translate-fuzzy">

-   **Beccheggio**: ruota l\'oggetto associato lungo l\'asse Y dell\'oggetto di riferimento.


</div>


<div class="mw-translate-fuzzy">

-   **Imbardata**: ruota l\'oggetto associato lungo l\'asse Z dell\'oggetto di riferimento.


</div>


<div class="mw-translate-fuzzy">

-   **Capovolgi le facce**: se selezionato, l\'oggetto collegato viene invertito sul suo piano XY.


</div>



## Limitazioni


<div class="mw-translate-fuzzy">

-   I contenitori [Part](Std_Part/it.md) e [Corpo](PartDesign_Body/it.md) non sono supportati. Mentre è possibile usare Allegato per allinearli, l\'allegato non sarà collegato parametricamente.
-   Se selezionando due linee si ottiene un traceback con \"i punti sono collineari. Non si può fare un piano\", prova invece a selezionare tre punti [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).


</div>

!!FUZZY!!


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/it
