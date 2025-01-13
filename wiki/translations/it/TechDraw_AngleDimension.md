---
 GuiCommand:
   Name: TechDraw AngleDimension
   Name/it: TechDraw Quota angolare
   MenuLocation: TechDraw , Quotatura , Inserisci Quota angolare
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_3PtAngleDimension/it
---

# TechDraw AngleDimension/it



## Descrizione

Lo strumento **TechDraw Quota angolare** aggiunge una quota angolare ad una Vista. La quota mostra l\'angolo interno tra due bordi diritti.

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Quotatura dell'angolo tra due bordi diritti*



## Utilizzo

1.  Selezionare due bordi dritti. La geometria può essere selezionata nella [Vista 3D](3D_view/it.md) o nel disegno.
2.  Se si ha selezionato la geometria nella vista 3D: aggiungere la Vista TechDraw corretta alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
3.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](TechDraw_Preferences/it#Dimensions.md) degli **Strumenti di quotatura** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/TechDraw_AngleDimension.svg" width=16px> Inserisci quota angolare** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Inserisci quota angolare](TechDraw_AngleDimension/it.md)** .

    -   Selezionare l\'opzione **TechDraw → Quotatura → <img src="images/TechDraw_AngleDimension.svg" width=16px> Inserisci Quota angolare** dal menu.
4.  Una quota viene aggiunta alla Vista.
5.  La quota può essere trascinata nella posizione desiderata.
6.  Se necessario, aggiungere tolleranze come descritto in [questa pagina](TechDraw_Geometric_dimensioning_and_tolerancing/it#Tolleranze.md).



### Visualizzazione quotatura 3D 

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Display_3D_measurement.md).



### Cambiare le proprietà 

Per modificare le proprietà di un oggetto quota, fare doppio clic su di esso nel disegno o nella [Vista ad albero](Tree_view/it.md). Si aprirà la [Finestra di dialogo Quota](TechDraw_LengthDimension/it#Finestra_di_dialogo_Quota.md).



## Limitazioni

Gli oggetti Quota sono vulnerabili al \"[problema di denominazione topologica](Topological_naming_problem/it.md)\". Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it.md).



## Note

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Note.md).



## Proprietà

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Proprietà.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/it
