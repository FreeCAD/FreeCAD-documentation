---
 GuiCommand:
   Name: Part Attachment
   Name/it: Part Associazione
   MenuLocation: Part , Associazione...
   Workbenches: Part_Workbench/it, PartDesign_Workbench/it
   Version: 0.17
   SeeAlso: Placement/it, Basic_Attachment_Tutorial/it
---

# Part EditAttachment/it



## Descrizione

Il comando <img alt="" src=images/Part_EditAttachment.svg  style="width:24px;"> **Part Associazione** associa un oggetto ad uno o più altri oggetti. L\'oggetto associato è collegato (linked) agli oggetti di riferimento, il che significa che se il [posizionamento](Std_Placement/it.md) o la geometria degli oggetti di riferimento viene modificato, il posizionamento dell\'oggetto collegato verrà aggiornato di conseguenza.



## Motori dell\'associazione 

L\'associazione di un oggetto è controllata da uno dei quattro motori di associazione. Il motore predefinito utilizzato per un oggetto dipende dal suo tipo. Il motore di associazione di un oggetto può essere modificato tramite la sua proprietà **Attacher Engine** ({{Version/it|1.0}}) o la sua proprietà [nascosta](Property_editor/it#Menu_contestuale.md) **Attacher Type**.

I motori disponibili sono elencati nella tabella sottostante. I motori di associazione controllano il **Placement** degli oggetti. Tutti i motori possono essere utilizzati per tutti gli oggetti che hanno questa proprietà. Ma i risultati degli ultimi tre hanno più senso se la forma dell\'oggetto corrisponde alla menzionata \"Forma Logica\".

  Motore di collegamento                     Tipo di associazione          Forma Logica
    
  [Engine 3D](#Engine_3D.md)         Attacher::AttachEngine3D      
  [Engine Plane](#Engine_Plane.md)   Attacher::AttachEnginePlane   Faccia planare coincidente con il piano XY del Posizionamento
  [Engine Line](#Engine_Line.md)     Attacher::AttachEngineLine    Bordo dritto collineare con l\'asse Z del Posizionamento
  [Engine Point](#Engine_Point.md)   Attacher::AttachEnginePoint   Vertice coincidente con l\'origine del Posizionamento

Il resto di questa pagina si concentra sull\'Engine 3D. Le modalità degli altri motori sono solo elencate. Da notare che le modalità di Engine Plane sono infatti identiche a quelle di Engine 3D.



## Utilizzo

1.  Selezionare l\'oggetto da associare.
2.  Effettuare una delle seguenti operazioni:
    -   Se l\'oggetto ha già una proprietà **Map Mode**: fare clic in quel campo nell\'[Editor di proprietà](Property_editor/it.md) e premere il pulsante **...** che appare.
    -   Selezionare l\'opzione **Parte → <img src="images/Part_EditAttachment.svg" width=16px> Associazione...** dal menu.
3.  Si apre il Pannello delle azioni **Associazione**.
4.  Nella parte superiore del pannello delle azioni è possibile leggere *Non associato*. Il primo pulsante etichettato **Selezione...** è evidenziato per indicare che è prevista una selezione nella [Vista 3D](3D_view/it.md).
5.  Selezionare un vertice, un bordo o una faccia/piano appartenente ad un altro oggetto.
6.  Nel campo di input a destra del pulsante vengono visualizzati l\'oggetto e il sottoelemento di riferimento. Ad esempio, se viene selezionata una faccia di un [Part Cubo](Part_Box/it.md), il campo potrebbe mostrare {{Value|Box:Face6}}. L\'etichetta del pulsante ora visualizza il tipo di sottoelemento.
7.  Le modalità disponibili vengono filtrate in base ai riferimenti selezionati e al loro ordine. Ad esempio, per le modalità da [Allinea O-Z-X](#Allinea_O-Z-X.md) a [Allinea O-Y-X](#Allinea_O-Y-X/it.md) il primo riferimento deve essere un vertice. Se il primo riferimento è un sottoelemento di tipo diverso, viene rimosso dall\'elenco.
8.  *Associato con la modalità * viene ora visualizzato nella parte superiore del pannello delle attività.
9.  Opzionalmente selezionare una diversa [Modalità di associazione](#Modalità_di_associazione.md) dall\'elenco. Per informazioni sulle modalità di collegamento, passa il mouse sopra di esse per visualizzare una descrizione comando.
10. A seconda della modalità selezionata, aggiungere fino a tre ulteriori riferimenti premendo i pulsanti **Riferimento2**, **Riferimento3** e **Riferimento4** e ripetendo il passaggio 5. È anche possibile per specificare tutti i riferimenti prima di selezionare una modalità di associazione.
11. Facoltativamente, imposta un [Offset associazione](#Offset_associazione.md).
12. Premere **OK**.
13. Se applicabile, facoltativamente modificare la proprietà **Map Path Parameter** nell\'[Editor proprietà](Property_editor/it.md).



## Modalità di associazione 

### Engine 3D 

![](images/Part_Offset_Tasks_it.png )



#### Disattivato

L\'associazione è disabilitata. L\'oggetto può essere spostato modificando la sua proprietà [Posizionamento](Placement/it.md).



#### Trasla l\'origine 

L\'origine corrisponde ad un vertice. L\'orientamento è ancora controllato dalla proprietà Placement dell\'oggetto associato.

:; Combinazioni riferimenti:

:   Vertice.



#### X Y Z dell\'oggetto 

Il Posizionamento viene reso uguale al Posizionamento di un oggetto associato.

:; Combinazioni riferimenti:

:   Qualsiasi
:   Conico



#### X Z Y dell\'oggetto 

Gli assi X, Y e Z corrispondono rispettivamente agli assi X, Z e -Y locali di un oggetto associato.

:; Combinazioni riferimenti:

:   Qualsiasi
:   Conico



#### Y Z X dell\'oggetto 

Gli assi X, Y e Z vengono abbinati rispettivamente agli assi Y, Z e X locali di un oggetto associato.

:; Combinazioni riferimenti:

:   Qualsiasi
:   Conico



#### XY su piano 

Il piano XY è allineato in modo da coincidere con una faccia planare.

:; Combinazioni riferimenti:

:   Piano



#### XY tangente a superficie 

Il piano XY viene reso tangente ad una faccia in corrispondenza di un vertice.

:; Combinazioni riferimenti:

:   Faccia, Vertice
:   Vertice, Faccia



#### Z tangente a bordo 

L\'asse Z è allineato in modo da essere tangente a un bordo. Un vertice opzionale definisce dove.

Se nessun vertice è associato, la proprietà **Map Path Parameter** determina il punto.

:; Combinazioni riferimenti:

:   Bordo
:   Bordo, Vertice
:   Vertice, Bordo

#### Frenet NBT 

<img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

Gli assi X e Y sono allineati agli assi normale (N) e binormale (B) del [Frenet-Serret coordinate system](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas) in un punto su un bordo curvo. Un vertice opzionale definisce dove.

Se nessun vertice è associato, la proprietà **Map Path Parameter** determina il punto. L\'origine dell\'oggetto viene traslata sul vertice se il vertice è il primo, o mantenuta sulla curva se la curva è la prima.

*Frenet NBT* è simile a *Z tangente al bordo*, tranne per il fatto che l\'asse X è ben definito.

:; Combinazioni riferimenti:

:   Curva
:   Curva, Vertice
:   Vertice, Curva

#### Frenet TNB 

<img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

Gli assi X e Y sono allineati agli assi tangente (T) e normale (N) del sistema di coordinate Frenet-Serret in un punto su un bordo curvo. Un vertice opzionale definisce dove.

Vedere [Frenet NBT](#Frenet_NBT.md).

#### Frenet TBN 

<img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

Gli assi X e Y sono allineati agli assi tangente (T) e binormale (B) del sistema di coordinate Frenet-Serret in un punto su un bordo curvo. Un vertice opzionale definisce dove.

Vedere [Frenet NBT](#Frenet_NBT.md).



#### Concentrico

Il piano XY è allineato al [cerchio osculatore](https://en.wikipedia.org/wiki/Osculating_circle) in un punto su un bordo. Un vertice opzionale definisce dove.

Se nessun vertice è associato, la proprietà **Map Path Parameter** determina il punto.

:; Combinazioni di riferimenti:

:   Curva
:   Cerchio
:   Curva, Vertice
:   Cerchio, Vertice
:   Vertice, Curva
:   Vertice, Cerchio



#### Sezione di rivoluzione 

L\'asse Y è allineato per corrispondere all\'asse del cerchio osculatore in un punto su un bordo. Un vertice opzionale definisce dove.

Vedere [Concentrico](#Concentrico.md).



#### Piano XY per 3 punti 

Il piano XY è allineato per passare attraverso tre vertici. L\'asse X passerà per i primi due vertici.

:; Combinazioni di riferimenti:

:   Vertice, Vertice, Vertice
:   Linea, Vertice
:   Vertice, Linea
:   Linea, Linea



#### Piano XZ per 3 punti 

Il piano XZ è allineato per passare attraverso tre vertici. L\'asse X passerà per i primi due vertici.

Vedere [Piano XY per 3 punti](#Piano_XY_per_3_punti.md).



#### Pieghevole

<img alt="" src=images/Attacher_mode_Folding.png  style="width:250px;">

Questa è una modalità speciale per ripiegare i poliedri. Selezionare quattro linee che condividono un punto comune in questo ordine: linea di contorno (1), linea di piega (2), altra linea di piega (3), altra linea di contorno (4). Per determinare il sistema di coordinate, le curve di contorno selezionate vengono rese coincidenti ruotando la linea 1 attorno alla linea 2, e la linea 4 attorno alla linea 3. L\'origine corrisponde al punto comune, l\'asse X corrisponde alla linea 2, l\'asse Y viene allineato verso la direzione delle curve di contorno coincidenti.

:; Combinazioni riferimenti:

:   Linea, Linea, Linea, Linea



#### Inerzia CS 

Gli assi X, Y e Z sono abbinati a quelli di un sistema di coordinate inerziali, costruito sugli assi principali di inerzia e sul centro di massa.

:; Combinazioni di riferimenti:

:   Qualsiasi
:   Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi
:   Qualsiasi, Qualsiasi, Qualsiasi, Qualsiasi



#### Allinea O-Z-X 

L\'origine è abbinata al primo vertice. Gli assi Z e X sono allineati verso un vertice o lungo una linea.

Vedere [Allinea le modalità di attacco del tipo O-X-Y](O-X-Y_Type_Attachment_Modes/it.md) per ulteriori dettagli.

:; Combinazioni riferimenti:

:   Vertice, Vertice, Vertice
:   Vertice, Vertice, Linea
:   Vertice, Linea, Vertice
:   Vertice, Linea, Linea
:   Vertice, Vertice
:   Vertice, Linea



#### Allinea O-Z-Y 

L\'origine è abbinata al primo vertice. Gli assi Z e Y sono allineati verso un vertice o lungo una linea.

Vedere [Allinea O-Z-X](#Allinea_O-Z-X.md).



#### Allinea O-X-Y 

L\'origine è abbinata al primo vertice. Gli assi X e Y sono allineati verso un vertice o lungo una linea.

Vedere [Allinea O-Z-X](#Allinea_O-Z-X.md).



#### Allinea O-X-Z 

L\'origine è abbinata al primo vertice. Gli assi X e Z sono allineati verso un vertice o lungo una linea.

Vedere [Allinea O-Z-X](#Allinea_O-Z-X.md).



#### Allinea O-Y-Z 

L\'origine è abbinata al primo vertice. Gli assi Y e Z sono allineati verso un vertice o lungo una linea.

Vedere [Allinea O-Z-X](#Allinea_O-Z-X.md).



#### Allinea O-Y-X 

L\'origine è abbinata al primo vertice. Gli assi Y e X sono allineati verso un vertice o lungo una linea.

Vedere [Allinea O-Z-X](#Allinea_O-Z-X.md).



#### XY parallelo al piano 


{{Version/it|1.0}}

Il piano XY è allineato per essere parallelo al piano XY del posizionamento di un oggetto collegato e passa attraverso un vertice. L\'origine corrisponde alla proiezione dell\'origine dell\'oggetto collegato sul piano XY.

Tenere presente che i deve selezionare un oggetto intero e non un sottoelemento come una faccia o un piano.

:; Combinazioni di riferimento:

:   Qualsiasi oggetto intero (con una proprietà **Placement**), Vertex


<div class="toccolours mw-collapsible mw-collapsed">

### Engine Plane 


<div class="mw-collapsible-content">

-   Disattivato
-   Trasla origine
-   XY dell\'oggetto
-   XZ dell\'oggetto
-   YZ dell\'oggetto
-   Faccia piana
-   Tangente alla superficie
-   Normale al bordo
-   Frenet NB
-   Frenet TN
-   Frenet TB
-   Concentrico
-   Sezione Rivoluzione
-   Piano per 3 punti
-   Normale a 3 punti
-   Pieghevole
-   Inerzia 2-3
-   Allinea O-N-X
-   Allinea O-N-Y
-   Allinea O-X-Y
-   Allinea O-X-N
-   Allinea O-Y-N
-   Allinea O-Y-X
-   XY parallelo al piano {{Version/it|1.0}}


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Engine Line 


<div class="mw-collapsible-content">

-   Disattivato
-   X dell\'oggetto
-   Y dell\'oggetto
-   Z dell\'oggetto
-   Asse di curvatura
-   Direttrice1
-   Direttrice2
-   Asintoto1
-   Asintoto2
-   Tangente
-   Normale al bordo
-   Binormale
-   Attraverso due punti
-   Intersezione {{Version/it|1.0}}
-   Linea di prossimità
-   1° asse principale
-   2° asse principale
-   3° asse principale
-   Normale alla superficie


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Engine Point 


<div class="mw-collapsible-content">

-   Disattivato
-   Origine dell\'oggetto
-   Focus1
-   Focus1
-   Sul bordo
-   Centro di curvatura
-   Centro di Massa
-   Vertice
-   Punto di prossimità 1
-   Punto di prossimità 2


</div>


</div>



### Offset dell\'associazione 

L\'offset dell\'associazione diventa attivo quando è stata selezionata una modalità di collegamento diversa da *Disattivato*. Viene utilizzato per applicare un offset lineare o rotatorio all\'interno del sistema di coordinate di associazione (ACS), come definito dalla modalità di associazione e dagli oggetti di riferimento.

-   **In direzione x**: imposta una distanza di offset lungo l\'asse X dell\'ACS.

-   **In direzione y**: imposta una distanza di offset lungo l\'asse Y dell\'ACS.

-   **In direzione z**: imposta una distanza di offset lungo l\'asse Z dell\'ACS.

-   **Intorno all\'asse x**: ruota l\'oggetto associato attorno all\'asse X dell\'ACS.

-   **Intorno all\'asse y**: ruota l\'oggetto associato attorno all\'asse Y dell\'ACS.

-   **Intorno all\'asse z**: ruota l\'oggetto associato attorno all\'asse Z dell\'ACS.

-   **Capovolgi lati**: se selezionato, l\'associazione viene invertita. Ciò equivale a ruotare l\'oggetto di 180° attorno all\'asse Y dell\'ACS.



## Limitazioni

-   Se selezionando due linee si ottiene un errore: \"I punti sono collineari. Impossibile creare un piano\", provare invece a selezionare tre vertici [#p473594](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/it
