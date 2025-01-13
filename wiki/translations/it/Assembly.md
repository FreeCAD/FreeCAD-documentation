# Assembly/it
## Introduzione




In FreeCAD il termine \"[Assemblaggio](Assembly/it.md)\" è normalmente usato per riferirsi a un [modello 3D](Model/it.md) che è composto da diverse parti distinte, assemblate assieme in modo da creare un oggetto funzionale, proprio come sono fatti i prodotti nel mondo reale.

Ad esempio, un bullone, una ranella e un dado sono tre corpi separati che, quando messi assieme, compongono un assemblaggio.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*A sinistra: tre solidi contigui separati, ognuno dei quali modellato da un [corpo di PartDesign](PartDesign_Body/it.md). A destra: i corpi separati uniti assieme in una [Parte](Std_Part/it.md) per creare un assemblaggio.*



## Utilizzo



### Assemblaggio manuale 

In termini generali, non c\'è bisogno di strumenti particolari per creare assemblaggi; è sufficiente avere diversi [corpi](Body/it.md) organizzati in qualche maniera.

Per posizionare i corpi dove li si vuole, si può

-   usare lo strumento [Trasforma](Std_TransformManip/it.md), oppure
-   usare il dialogo di <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Posizionamento](Std_Placement/it.md), oppure
-   modificare direttamente la proprietà [Placement](Placement/it.md) nell\'[Editore delle proprietà](Property_editor/it.md).

Si può usare uno degli [ambienti complementari](External_workbenches/it.md) pseudo-assembly, come Lattice2, Manipulator, Part-o-magic, o WorkFeature, per avere un aiuto nel trovare intersezioni, misurare distanze e distribuire gli oggetti nel modo desiderato.

In generale, l\'oggetto <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Parte](Std_Part/it.md) era progettato per servire come blocco costruttivo basilare per creare assemblaggi. Questo oggetto è usato per raggruppare insieme diversi [corpi](Body/it.md) e muoverli insieme come un\'unità, ovvero come un sotto-asseblaggio. Successivamente questo sotto-assemblaggio può essere posto vicino a un altro sotto-assemblaggio (o usato al suo interno) in modo da creare l\'assemblaggio finale.



### Assemblaggio regolamentato 

È inoltre possibile utilizzare l\'[Ambiente Assembly](Assembly_Workbench/it.md) integrato o le sue controparti aggiuntive, come <img alt="" src=images/A2p_workbench.svg  style="width:16px;"> [A2plus](A2plus_Workbench/it.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench/it.md), o <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:16px;"> [Assembly4](Assembly4_Workbench/it.md). Si noti che [Assembly2](Assembly2_Workbench/it.md) non è mantenuto; il suo uso è fortemente sconsigliato per i nuovi modelli.

Gli ambienti di assemblaggio usano vincoli ed espressioni per creare relazioni tra i pezzi del modello, in modo da legare matematicamente gli oggetti sul posto; per esempio, \"questa faccia dovrebbe attaccarsi a questa altra faccia\", \"questo cilindro dovrebbe essere concentrico a questo cerchio\", \"questo punto dovrebbe seguire questo bordo\", ecc.

Questo è un uso avanzato del software che normalmente è usato in complessi sistemi meccanici. Se il [modello](Model/it.md) non è troppo complesso, usare un ambiente di assemblaggio può non essere necessario.



## Note

-   A partire da FreeCAD 1.0, esiste un [Ambiente Assemblatore](Assembly_Workbench/it.md) ufficiale incluso per impostazione predefinita nel sistema.

-   Si noti che gli ambienti di assemblaggio sono in genere incompatibili tra loro. Se si crea un assemblaggio con uno di questi ambienti, si dovrebbe rimanere fedeli ad esso, e non usare un altro ambiente di assemblaggio per lavorare sullo stesso documento.


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/it
