# Macro MeasureCircle/it
{{Macro/it
|Name=Macro MeasureCircle
|Icon=Macro_MeasureCircle.png
|Translate=Misura cerchio
|Description=Calcola il raggio di un cerchio da 3 punti o da uno spigolo circolare
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_MeasureCircle.png ToolBar Icon]
}}

## Descrizione

Questa macro calcola e riporta il raggio e il centro di un cerchio dati 3 punti o uno spigolo circolare. Traccia una linea dal centro del cerchio al primo vertice, che può essere utilizzato per misurazioni future.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro}}

## Uso

Copiare la macro nella propria cartella delle macro ed eseguirla (per maggiori dettagli vedere [Come installare le macro](How_to_install_macros/it.md)).

Basta selezionare i vertici e il risultato viene mostrato nel pannello Report. I bordi sono selezionabili e valgono come due vertici. Può anche essere selezionato un bordo circolare. Se sono selezionati due bordi, il vertice finale del secondo bordo non viene utilizzato nel calcolo.

È possibile selezionare gli elementi e poi lanciare la macro oppure lanciare la macro senza selezione e poi selezionare gli elementi dopo il lancio. Se non ci sono abbastanza elementi selezionati prima di lanciare la macro, è necessario selezionare gli elementi mancanti.

## Codice

L\'ultima versione della macro si trova in [MeasureCircle.FCMacro](https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro) ma il modo più semplice per installare questa macro è tramite [Addon Manager](Std_AddonMgr/it.md).

ToolBar Icon ![](images/Macro_MeasureCircle.png )

**Macro_MeasureCircle.FCMacro**



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro MeasureCircle/it
