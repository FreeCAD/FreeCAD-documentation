# Part JoinCutout/it
---
- GuiCommand:/it   Name:Part JoinCutout   Name/it:Asportazione   MenuLocation:Part → Congiungi → Asporta oggetto   Workbenches:[Version:0.16.5069   SeeAlso:[[Part_JoinConnect/it|Congiunzione](Part_Workbench/it___Part]].md), [Incastro](Part_JoinEmbed/it.md), [Operazioni booleane](Part_Boolean/it.md), [Spessore](Part_Thickness/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Asporta](Part_JoinCutout/it.md) crea un ritaglio in un oggetto vuoto internamente per adattarlo a un altro oggetto dello stesso tipo, ad esempio, in una tubazione per creare una nuova derivazione.


</div>

![600px](images/JoinFeatures_Cutout.png)

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare prima l\'oggetto di base, e poi l\'oggetto con cui si vuole definire il ritaglio.
    L\'ordine di selezione è importante. È sufficiente selezionare una qualsiasi sotto-forma di ciascun oggetto (ad esempio, delle facce).
2.  Invocare il comando Asporta oggetto.


</div>


<div class="mw-translate-fuzzy">

Viene creato un oggetto Parte JoinFeature, con la modalità, Mode, impostata su \'Cutout\'. Nella vista 3D viene mostrato il risultato dell\'asportazione, e gli oggetti originali sono nascosti.


</div>

## Proprietà


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Base}}

-    **Base**: Riferisce l\'oggetto di base (quello da cui si vuole asportare una porzione). L\'oggetto deve essere un solido unico.

-    **Tool**: Riferisce l\'oggetto da usare come utensile (l\'oggetto che crea il ritaglio). L\'oggetto può essere un solido unico, oppure un [composto valido](Part_Compound/it.md) di solidi.

-    **Mode**: Stabilisce la modalità dell\'operazione di Giunzione, che in questo caso è uguale a \'Cutout\' (cambiando modalità si trasforma lo strumento in uno strumento Giunzione diverso). Il valore \'bypass\' può essere usato per disabilitare temporaneamente i lunghi calcoli (in questo caso, viene creato un oggetto Composto formato dagli oggetti Base e Tool , che è un\'operazione veloce).

-    **Refine**: Stabilisce se alla forma finale deve essere applicata l\'operazione [Affina](Part_RefineShape/it.md), oppure no. Il valore di default è stabilito dalla casella di controllo \'Affina automaticamente la forma dopo l\'operazione booleana\' nelle preferenze di PartDesign. Quando la proprietà Mode è impostata su \'bypass\', Affina viene ignorato (Refine non è mai applicato).


</div>

## Esempio

1.  Creare un tubo applicando uno [Spessore](Part_Thickness/it.md) a un [cilindro](Part_Cylinder/it.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Creare un nuovo tubo di diametro inferiore e [posizionarlo](Placement/it.md) in modo da perforare la parete del primo tubo:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Selezionare il primo tubo, poi il secondo tubo (l\'ordine di selezione è importante), infine selezionare l\'opzione \'Asporta oggetto\' dalla barra degli strumenti a discesa degli strumenti Giunzione.
    ![320px](images/JoinFeatures_Example_step3_Cutout.png)

## Algoritmo

Gli algoritmi sottostanti agli strumenti di Giunzione sono abbastanza semplici, ed è importante comprenderli per utilizzarli correttamente.


<div class="mw-translate-fuzzy">

1\. L\'oggetto Base viene [tagliato](Part_Cut/it.md) dall\'oggetto Tool con una operazione booleana. La forma risultante è un [composto](Part_Compound/it.md), cioè un insieme di solidi non intersecanti (tipicamente, due).


</div>

2\. Il composto risultante viene filtrato e viene conservato solo il solido più grande.


<div class="mw-translate-fuzzy">

3\. Se la proprietà Refine è impostata su true, la forma risultante viene [affinata](Part_RefineShape/it.md).
![800px](images/JoinFeatures-Algo-Cutout.png)


</div>

### Note


<div class="mw-translate-fuzzy">

-   Se dopo il passaggio 1, l\'oggetto rimane ancora in un pezzo unico, il risultato dell\'asportazione è equivalente a un [taglio booleano](Part_Cut/it.md) di Base con Tool.
-   Attualmente, quando viene fornito un composto come Base lo strumento produce un risultato inaspettato. Questo potrà essere modificato in futuro.
-   Poiché il pezzo più grande è determinato confrontando i volumi, lo strumento può funzionare solo con i solidi. Questo potrà essere modificato in futuro.


</div>

## Script

Lo strumento Giunzione può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Crea una funzione Cutout vuota (o altra funzione Join, secondo la modalità passata). Le proprietà Base e Tool devono essere assegnate in modo esplicito, in seguito.
-   Restituisce l\'oggetto appena creato.

Esempio: {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Lo strumento è implementato in Python, vedere {{FileName|/Mod/Part/JoinFeatures.py}} ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) in cui è installato FreeCAD.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/it
