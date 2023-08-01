---
- GuiCommand:
   Name:Part JoinEmbed
   Name/it:Incastro
   MenuLocation:Part → Congiungi → Incastra oggetto
   Workbenches:[[Part_Workbench/it   Part]]|Version:0.16.5069
   SeeAlso:[Congiunzione](Part_JoinConnect/it.md), [Asportazione](Part_JoinCutout/it.md), [Operazione booleana](Part_Boolean/it.md), [Spessore](Part_Thickness/it.md)
---

# Part JoinEmbed/it


</div>

## Descrizione

Lo strumento Incastra incorpora un oggetto vuoto internamente in un altro oggetto analogo, ad esempio, un tubo in un altro tubo.

![600px](images/JoinFeatures_Embed.png)

## Utilizzo

1.  Selezionare prima l\'oggetto Base, e poi l\'oggetto Tool da incastrare.
    L\'ordine di selezione è importante. È sufficiente selezionare una qualsiasi sotto-forma di ciascun oggetto (ad esempio, delle facce).
2.  Invocare il comando Incastra.

Viene creato un oggetto Parte JoinFeature, con la modalità, Mode, impostata su \'Embed\'. Nella vista 3D viene mostrato il risultato dell\'incastro, e gli oggetti originali sono nascosti.

## Properties


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

## Proprietà


{{TitleProperty|Base}}

-    **Base**: Riferisce l\'oggetto di base (l\'oggetto in cui si vuole incastrare l\'altro oggetto). L\'oggetto deve essere un solido unico.

-    **Tool**: Riferisce l\'oggetto da usare come utensile (l\'oggetto da incastrare). L\'oggetto può essere un solido unico, oppure un [composto valido](Part_Compound/it.md) di solidi.

-    **Mode**: Stabilisce la modalità dell\'operazione di Giunzione, che in questo caso è uguale a \'Connect\' (cambiando modalità si trasforma lo strumento in uno strumento Giunzione diverso). Il valore \'bypass\' può essere usato per disabilitare temporaneamente i lunghi calcoli (in questo caso, viene creato un oggetto Composto formato dagli oggetti Base e Tool , che è un\'operazione veloce).

-    **Refine**: Stabilisce se alla forma finale deve essere applicata l\'operazione [Affina](Part_RefineShape/it.md), oppure no. Il valore di default è stabilito dalla casella di controllo \'Affina automaticamente la forma dopo l\'operazione booleana\' nelle preferenze di PartDesign. Quando la proprietà Mode è impostata su \'bypass\', Affina viene ignorato (Refine non è mai applicato).


</div>

## Example


<div class="mw-translate-fuzzy">

## Esempio

1.  Creare un tubo applicando uno [Spessore](Part_Thickness/it.md) a un [cilindro](Part_Cylinder/it.md):
    <img alt="" src=images/JoinFeatures_Example_step1.png  style="width:320px;">
2.  Creare un nuovo tubo di diametro inferiore e [posizionarlo](Placement/it.md) in modo da perforare la parete del primo tubo:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Selezionare il primo tubo, poi il secondo tubo (l\'ordine di selezione è importante), infine selezionare l\'opzione \'Incastra\' dalla barra degli strumenti a discesa degli strumenti Giunzione.
    ![320px](images/JoinFeatures_Example_step3_Embed.png)
4.  Per visualizzare gli interni, utilizzare uno degli strumenti di sezione: [Piano di taglio](Std_ToggleClipPlane/it.md) del menu Visualizza, [Piano di sezione](Arch_SectionPlane/it.md) di Arch, o [Piano di taglio](Arch_CutPlane/it.md) di Arch. Nell\'immagine seguente, è stato utilizzato il Piano di sezione di Arch.
    ![320px](images/JoinFeatures_Example_step4_Embed.png)


</div>

## Algorithm


<div class="mw-translate-fuzzy">

## Algoritmo

Gli algoritmi sottostanti agli strumenti di Giunzione sono abbastanza semplici, ed è importante comprenderli per utilizzarli correttamente.


</div>

1\. L\'oggetto Base viene [tagliato](Part_Cut/it.md) dall\'oggetto Tool con una operazione booleana. La forma risultante è un [composto](Part_Compound/it.md), cioè un insieme di solidi non intersecanti (tipicamente, due).

2\. Il composto risultante viene filtrato e viene conservato solo il solido più grande.


<div class="mw-translate-fuzzy">

3\. Il solido più grande viene [unito](Part_Union/it.md) con l\'oggetto Tool tramite una operazione booleana.


</div>

4\. Se la proprietà Refine è impostata su true, la forma risultante viene [affinata](Part_RefineShape/it.md).
![800px](images/JoinFeatures-Algo-Embed.png)

### Notes


<div class="mw-translate-fuzzy">

### Note

-   Se dopo il passaggio 1, l\'oggetto rimane ancora in un pezzo unico, il risultato dell\'incastro è equivalente a una [unione booleana](Part_Union/it.md) di Base con Tool, ma richiede più tempo per il calcolo.
-   Attualmente, quando viene fornito un composto come Base lo strumento produce un risultato inaspettato. Questo potrà essere modificato in futuro.
-   Poiché il pezzo più grande è determinato confrontando i volumi, lo strumento può funzionare solo con i solidi. Questo potrà essere modificato in futuro.


</div>

## Script

Lo strumento Giunzione può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


```pythonJoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed')```

-   Crea una funzione Embed vuota (o altra funzione Join, secondo la modalità passata). Le proprietà Base e Tool devono essere assegnate in modo esplicito, in seguito.
-   Restituisce l\'oggetto appena creato.

Esempio:


{{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Lo strumento è implementato in Python, vedere **/Mod/Part/JoinFeatures.py** ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) in cui è installato FreeCAD.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinEmbed/it
