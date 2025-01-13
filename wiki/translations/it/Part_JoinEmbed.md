---
 GuiCommand:
   Name: Part JoinEmbed
   Name/it: Part Incorpora
   MenuLocation: Part , Giunzione , Incorpora oggetto
   Workbenches: Part_Workbench/it
   Version: 0.16
   SeeAlso: Part_JoinConnect/it, Part_JoinCutout/it, Part_Boolean/it, Part_Thickness/it
---

# Part JoinEmbed/it



## Descrizione

Lo strumento <img alt="" src=images/Part_JoinEmbed.svg  style="width:24px;"> **Part Incorpora oggetto**, incorpora un oggetto con pareti (es. un tubo) in un altro oggetto con pareti.

![600px](images/JoinFeatures_Embed.png)



## Utilizzo

1.  Selezionare prima l\'oggetto base, quindi l\'oggetto da incorporare. L\'ordine di selezione è importante. È sufficiente selezionare una sottoforma di ciascun oggetto (ad esempio facce).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Part_JoinEmbed.svg" width=16px> [Incorpora oggetto](Part_JoinEmbed/it.md)**.
    -   Selezionare l\'opzione **Part → Giunzione → <img src="images/Part_JoinEmbed.svg" width=16px> Incorpora oggetto** dal menu.
3.  Viene creato un oggetto Part JoinFeature, con la modalità impostata su \"Embed\" (incorporato). Gli oggetti originali vengono nascosti e il risultato dell\'incorporamento viene mostrato nella [Vista 3D](3D_view/it.md).

## Properties


{{TitleProperty|Base}}

-    **Base**: Riferisce l\'oggetto di base (l\'oggetto in cui si vuole incorporare l\'altro oggetto). L\'oggetto deve essere un solido unico.

-    **Tool**: Riferisce l\'oggetto da usare come utensile (l\'oggetto da incorporare). L\'oggetto può essere un solido unico, oppure un [composto valido](Part_Compound/it.md) di solidi.

-    **Mode**: Stabilisce la modalità dell\'operazione di Giunzione, che in questo caso è uguale a \'Connect\' (cambiando modalità si trasforma lo strumento in uno strumento Giunzione diverso). Il valore \'bypass\' può essere usato per disabilitare temporaneamente i lunghi calcoli (in questo caso, viene creato un oggetto Composto formato dagli oggetti Base e Tool , che è un\'operazione veloce).

-    **Refine**: Stabilisce se alla forma finale deve essere applicata l\'operazione [Affina](Part_RefineShape/it.md), oppure no. Il valore di default è stabilito dalla casella di controllo \'Affina automaticamente la forma dopo l\'operazione booleana\' nelle preferenze di PartDesign. Quando la proprietà Mode è impostata su \'bypass\', Affina viene ignorato (Refine non è mai applicato).



## Esempio

1.  Creare un tubo applicando uno [Spessore](Part_Thickness/it.md) a un [cilindro](Part_Cylinder/it.md):
    <img alt="" src=images/JoinFeatures_Example_step1.png  style="width:320px;">
2.  Creare un nuovo tubo di diametro inferiore e [posizionarlo](Placement/it.md) in modo da perforare la parete del primo tubo:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Selezionare il primo tubo, poi il secondo tubo (l\'ordine di selezione è importante), infine selezionare l\'opzione \'Incorpora\' dalla barra degli strumenti a discesa degli strumenti Giunzione.
    ![320px](images/JoinFeatures_Example_step3_Embed.png)
4.  Per visualizzare gli interni, utilizzare uno degli strumenti di sezione: [Piano di taglio](Std_ToggleClipPlane/it.md) del menu Visualizza, [Piano di sezione](Arch_SectionPlane/it.md) di Arch, o [Piano di taglio](Arch_CutPlane/it.md) di Arch. Nell\'immagine seguente, è stato utilizzato il Piano di sezione di Arch.
    ![320px](images/JoinFeatures_Example_step4_Embed.png)



## Algoritmo

Gli algoritmi sottostanti agli strumenti di Giunzione sono abbastanza semplici, ed è importante comprenderli per utilizzarli correttamente.

1\. L\'oggetto Base viene [tagliato](Part_Cut/it.md) dall\'oggetto Tool con una operazione booleana. La forma risultante è un [composto](Part_Compound/it.md), cioè un insieme di solidi non intersecanti (tipicamente, due).

2\. Il composto risultante viene filtrato e viene conservato solo il solido più grande.

3\. Il solido più grande viene [unito](Part_Fuse/it.md) con l\'oggetto Tool tramite una operazione booleana.

4\. Se la proprietà Refine è impostata su true, la forma risultante viene [affinata](Part_RefineShape/it.md).
![800px](images/JoinFeatures-Algo-Embed.png)



### Note

-   Se dopo il passaggio 1, l\'oggetto rimane ancora in un pezzo unico, il risultato dell\'incastro è equivalente a una [unione booleana](Part_Fuse/it.md) di Base con Tool, ma richiede più tempo per il calcolo.
-   Attualmente, quando viene fornito un composto come Base lo strumento produce un risultato inaspettato. Questo potrà essere modificato in futuro.
-   Poiché il pezzo più grande è determinato confrontando i volumi, lo strumento può funzionare solo con i solidi. Questo potrà essere modificato in futuro.



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



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinEmbed/it
