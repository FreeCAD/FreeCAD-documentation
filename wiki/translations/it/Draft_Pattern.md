# Draft Pattern/it
## Descrizione

Gli oggetti [Draft](Draft_Workbench/it.md) con una proprietà **Make Face** possono visualizzare un modello SVG invece di un colore a tinta unita della faccia.

![](images/DraftPatternSample.png ) 
*Un'ellisse e un poligono con un modello SVG*



## Utilizzo

1.  Assicurarsi che gli oggetti siano chiusi e planari e non si intersechino.
2.  Per chiudere una [Draft Polilinea](Draft_Wire/it.md), una [Draft BSpline](Draft_BSpline/it.md), una [Draft Curva di Bézier cubica](Draft_CubicBezCurve/it.md) o una \[\[Draft_BezCurve/it\|Draft Curva di Bézier

\]\] impostare la sua proprietà **Closed** su `True`.

1.  Per chiudere un [Draft Cerchio](Draft_Circle/it.md) o una [Draft Ellisse](Draft_Ellipse/it.md) impostare le sue proprietà **First Angle** e **Last Angle** sullo stesso valore.
2.  Selezionare gli oggetti.
3.  Passare alla scheda **Visualizza** dell\'[Editor di proprietà](Property_editor.md).
4.  La **Modalità di visualizzazione** deve essere impostata su {{Value|Flat Lines}}.
5.  Selezionare un **Pattern**.
6.  Facoltativamente, modificare la **Pattern Size**. Si noti che un valore più elevato determina un modello più denso.
7.  Il motivo non viene visualizzato quando gli oggetti vengono selezionati. Deselezionarli per verificare il risultato.
8.  Facoltativamente riselezionare gli oggetti per modificare le proprietà del modello.



## Campiture Disponibili 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Note

-   I modelli SVG sono archiviati nei file **.SVG**. È possibile utilizzare i propri modelli personalizzati. Vedere [Preferenze](#Preferenze.md).
-   I modelli stessi non vengono salvati nel documento di FreeCAD. Gli oggetti il ​​cui **Pattern** non può essere trovato vengono invece visualizzati con un colore della faccia a tinta unita.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare la **Pattern Size** utilizzata per i nuovi oggetti: **Modifica → Preferenze... → Draft → Visualizzazione → Dimensione della campitura SVG**.
-   Per specificare una directory con campiture SVG aggiuntive: **Modifica → Preferenze... → Draft → Visualizzazione → Posizione aggiuntiva delle campiture SVG**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/it
