# Copying Objects/it
## Panoramica

Come molti altri programmi per computer, FreeCAD ha la capacità di tagliare, copiare e incollare oggetti. Gli oggetti di un [documento](Document_structure/it.md) possono essere copiati liberamente all\'interno di un stesso documento o tra documenti utilizzando i comandi <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Copia](Std_Copy/it.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Incolla](Std_Paste/it.md) e [Duplica l\'oggetto selezionato](Std_DuplicateSelection/it.md).

![](images/Copy_past_duplicate.png )

Si tenga presente che gli oggetti copiati-incollati sono scollegati dall\'originale. Se si desiderano cloni collegati, utilizzare <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> [Clone dell\'Ambiente Draft](Draft_Clone/it.md) o <img alt="" src=images/PartDesign_Clone.svg  style="width:24px;"> [Clone dell\'Ambiente Part Design](PartDesign_Clone/it.md). Se non si ha bisogno né di un clone dipendente né di una replica parametrica, si può anche utilizzare <img alt="" src=images/Part_SimpleCopy.svg  style="width:24px;"> [ Crea una copia semplice dell\'Ambiente Part](Part_SimpleCopy/it.md). Per i cloni con motivi, esaminare la sezione [Altri metodi](Copying_Objects/it#Altri_metodi.md) di questa pagina.



## Copia di oggetti collegati 

Se un oggetto da copiare ha collegamenti a oggetti non presenti nella selezione, FreeCAD chiederà se gli oggetti non selezionati devono essere inclusi nell\'operazione di copia.



## Trovare e posizionare gli oggetti incollati 

Dopo un\'operazione di copia-incolla, potrebbe non essere ovvio dove si trovano i nuovi oggetti nella [vista 3D](3D_view/it.md). Questo perché i nuovi oggetti hanno la stessa proprietà [Placement](Placement/it.md) degli originali. Attivare/disattivare la proprietà Visibilità (**Barra spaziatrice**) per nascondere gli originali e quindi spostare le copie nella posizione corretta, ad esempio utilizzando <img alt="" src=images/Std_TransformManip.svg  style="width:24px;"> [Trasforma](Std_TransformManip/it.md) o <img alt="" src=images/Std_Placement.svg  style="width:24px;"> [Posizionamento](Std_Placement/it.md).



## Altri metodi 

Come per la maggior parte delle operazioni, anche per fare le copie, in FreeCAD ci sono molti modi. Per ulteriori idee, vedere:

-   PartDesign: [Rifletti](PartDesign_Mirrored/it.md), [Schiera lineare](PartDesign_LinearPattern/it.md), [Schiera polare](PartDesign_PolarPattern/it.md), [Multi Trasformazione](PartDesign_MultiTransform/it.md)
-   Part: [Specchia](Part_Mirror/it.md), [Crea semplice copia](Part_SimpleCopy/it.md)
-   Draft: [Offset](Draft_Offset/it.md), [Scala](Draft_Scale/it.md), [Schiera](Draft_OrthoArray/it.md), [PathArray](Draft_PathArray/it.md), [Clona](Draft_Clone/it.md), [Simmetria](Draft_Mirror/it.md)



---
⏵ [documentation index](../README.md) > Copying Objects/it
