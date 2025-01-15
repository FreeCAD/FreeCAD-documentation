---
 GuiCommand:
   Name: FCGear CycloidRack
   Name/it: Cremagliera cicloidale
   MenuLocation: Gear , Cycloid Rack
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: 1.0
   SeeAlso: FCGear_CycloidGear/it
---

# FCGear CycloidRack/it



## Descrizione

<img alt="" src=images/FCGear_CycloidRack-01.png  style="width:200px;">



*Cremagliere cicloidali da sinistra a destra: ingranaggio dritto, ingranaggio elicoidale, ingranaggio elicoidale doppio*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_CycloidRack.svg style="width:16px"> [Cycloid Rack](FCGear_CycloidRack/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_CycloidRack.svg style="width:16px"> Cycloid Rack** dal menu.
3.  Modificare il parametro dell\'ingranaggio alle condizioni richieste (vedi [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear CycloidRack deriva da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: Il valore predefinito è {{value|15}}. Numero di punti per la spline.


{{Properties_Title|base}}

-    **add_endings|bool**: Se {{True}} (predefinito), la lunghezza totale della cremagliera è denti \* passo. Se {{False}}, la cremagliera inizia con un fianco dentellato.

-    **height|Length**: Il valore predefinito è {{value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **teeth|Integer**: Il valore predefinito è {{value|15}}. Numero di denti.

-    **thickness|Length**: Il valore predefinito è {{value|5 mm}}. Spessore della parte non lavorata della cremagliera.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (sola lettura) Inclinazione nel piano trasversale.


{{Properties_Title|cycloid}}

-    **inner_diameter|Float**: Il valore predefinito è {{value|7.5}}. Diametro del cerchio rotante dell\'ipocicloide, normalizzato dal **module** (vedere [Note](FCGear_CycloidGear/it#Note.md)).

-    **outer_diameter|Float**: Il valore predefinito è {{value|7.5}}. Diametro del cerchio di rotolamento dell\'epicicloide, normalizzato dal **module** (vedere [Note](FCGear_CycloidGear/it#Note.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Il valore predefinito è {{value|0}}.

-    **root_fillet|Float**: Il valore predefinito è {{value|0}}.


{{Properties_Title|helical}}

-    **beta|Angle**: L\'impostazione predefinita è {{value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio elicoidale (valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra).

-    **double_helix|Bool**: L\'impostazione predefinita è {{false}}, {{true}} crea un ingranaggio a doppia elica (vedere [Note](FCGear_CycloidGear/it#Note.md)).


{{Properties_Title|involute}}

-    **module|Length**: Il valore predefinito è {{value|1 mm}}. Per le cremagliere il modulo è uguale al passo e lo stesso vale per la distanza tra i punti corrispondenti sui denti adiacenti (vedere [Note](FCGear_CycloidGear/it#Note.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: L\'impostazione predefinita è {{false}}. Se {{true}} la cremagliera viene disegnata con un numero costante di denti per evitare la ridenominazione topologica.


{{Properties_Title|tolerance}}

-    **clearance|Float**: Il valore predefinito è {{value|0.25}} (vedere [Note](FCGear_CycloidGear/it#Note.md)).

-    **head|Float**: Il valore predefinito è {{value|0}}. Lunghezza aggiuntiva sulla testa dei denti, normalizzata da **module**.


{{Properties_Title|version}}

-    **version|String**:



## Note

Vedere [Ingranaggio cicloidale](FCGear_CycloidGear/it#Notes.md).



## Formule utili 

Vedere [Ingranaggio cicloidale](FCGear_CycloidGear/it#Formule_utili.md).



## Script



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear CycloidRack/it
