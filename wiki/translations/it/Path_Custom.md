# Path Custom/it
---
- GuiCommand:   Name:Path Custom   Name/it:Personalizza   Workbenches:[[Path Workbench/it   Path]]|MenuLocation:Path - Comandi parziali - Personalizza   Shortcut:   SeeAlso:---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento inserisce un oggetto tracciato che è costituito da codice G personalizzato e codificato a mano.


</div>


<div class="mw-translate-fuzzy">

Poiché il comando personalizzato del codice G non fornisce alcun collegamento a un controller degli strumenti, se uno strumento viene utilizzato dal codice G personalizzato, è necessario scrivere l\'indice dello strumento, nonché il codice M di avvio, in modo che sia trasmesso al post-processore. Ciò garantisce che le modifiche allo strumento e all\'avvio siano generate correttamente.


</div>


<div class="mw-translate-fuzzy">

Ad esempio, per passare al postprocessore che l\'utensile utilizzato nell\'operazione di codice G personalizzato ha indice 6 e una velocità del mandrino è di 10.000, inserire il seguente codice all\'inizio dell\'operazione di codice G personalizzato:


</div>

(T6: 4mm Endmill)

M6 T6

M3 S10000


<div class="mw-translate-fuzzy">

Notare che le velocità di avanzamento sono generate correttamente dal postprocessore, solo se le velocità di avanzamento del codice G personalizzato sono scritte in unità al secondo.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Path_Custom.png" width=16px> [Personalizza](Path_Custom/it.md)
**
2.  Scrivere il Codice G personalizzato nella proprietà **G Code** dell\'oggetto appena creato. Consultare la pagina [Script di Path](Path_scripting/it.md) per conoscere i comandi G-Code supportati.


</div>



## Proprietà


<div class="mw-translate-fuzzy">

-    **G Code**: I comandi G-Code personali per costruire il percorso


</div>





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Custom/it
