---
- GuiCommand:
   Name: Part Offset2D
   Name/it: Offset 2D
   MenuLocation: Parte - Offset 2D...
   Workbenches: [Parte](Part_Workbench/it.md)
   Version: 0.17
   SeeAlso: [Part Offset 3D](Part_Offset/it.md), [Part Spessore](Part_Thickness/it.md), [Offset di Draft](Draft_Offset/it.md)
---

# Part Offset2D/it


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Offset 2D di Parte costruisce un contorno, parallelo al contorno originale, ad una data distanza da esso. Oppure ingrandisce o restringe una faccia piana, in modo simile.


</div>

La faccia del contorno deve essere planare. In un oggetto ci possono essere più contorni, non necessariamente complanari.

![600px](images/Part_Offset2D_Demo.png)

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare un oggetto 2D
2.  Premere il pulsante **[<img src=images/Part_Offset2D.svg style="width:24px">** **Offset 2D\...** di Parte.
3.  Impostare l\'offset nel [Pannello delle azioni](Task_Panel/it.md).
4.  Premere **OK**.


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 

## Problemi noti 

-   La maggior parte delle modalità non predefinite funziona solo con OCC 7.0.0 o superiori.

-   Questo strumento può mandare in crash FreeCAD (vedere il punto successivo). In Windows, questi incidenti vengono convertiti in eccezioni e in genere non causano la chiusura di FreeCAD; su altri OS può capitare. Quindi, si consiglia di salvare i progetti prima di tentare di utilizzare lo strumento. Neanche le ellissi vengono gestite.

-   Allargando delle facce con fori circolari di una quantità sufficiente a chiudere i fori, si verifica un crash (OCC 7.0.0). Il problema sembra essere specifico per cerchi; le altre forme sembrano chiudersi in modo corretto.


<div class="mw-translate-fuzzy">

-   quando si applica l\'offset a cerchi che hanno un posizionamento diverso da zero, il risultato può essere posizionato in modo sbagliato. (OCC 7.0.0)


</div>


<div class="mw-translate-fuzzy">

-   quando si applica l\'offset ai cerchi, a volte essi sono scalati in direzione inattesa (per esempio verso l\'interno anziché verso l\'esterno). (OCC 7.0.0)


</div>

-   Fill=\"true\" non funziona quando si trattano collettivamente dei contorni aperti in modalità \"Skin\"

-   La modalità di unione \"Tangent\" non funziona (OCC 7.0.0)

-   L\'offeset di contorni composti da un singolo segmento non è supportato (perché un segmento non definisce un piano). I contorni composti da una singola linea non possono neanche essere trattati in un offset collettivo.

## Proprietà

-    **Source**: Link alla forma originale


<div class="mw-translate-fuzzy">

-    **Value**La distanza a cui allargare la faccia del contorno. Se è negativa, la faccia del contorno si restringe.


</div>

-    **Mode**(\"Pipe\" or \"Skin\"): Imposta il modo in cui vengono elaborati i contorni non chiusi. Se \"Pipe\", il contorno è delineato come se fosse un contorno chiuso estremamente sottile. Se \"Skin\", viene creato un contorno aperto.

:   ![600px](images/Part_Offset2D_Mode.png)

-    **Join**(\"Arc\", \"Tangent\", \"Intersection\"): Imposta il comportamento nelle pieghe. Se \"Arc\", i segmenti dell\'offset sono collegati con un arco di cerchio, centrato nel vertice. \"Tangent\" non è supportato con OCC7.0.0. \"Intersection\": i segmenti dell\'offset sono estesi fino a quando non si intersecano.

:   ![600px](images/Part_Offset2D_Join.png)

-    **Intersection**(\"false\", \"true\"): stabilisce se più contorni vengono trattate collettivamente o in modo indipendente. Se \"false\", i contorni sono trattati in modo indipendente, le intersezioni tra i contorni risultanti vengono ignorate. Se \"true\", i contorni sono trattati in modo collettivo.

:   ![600px](images/Part_Offset2D_Intersection.png)





:   Sono accoppiati solo i contorni all\'interno di un composto. Ad esempio, se la struttura è composto simile a (wire1, wire2, compound(wire3, wire4)), wire1 e wire2 sono trattati collettivamente, ma indipendentemente da wire3 e wire4. Allo stesso modo, wire3 e wire4 sono trattati collettivamente, ma indipendentemente da wire1+wire2.





:   Inoltre, in modalità collettiva, le direzioni dei contorni sono importanti, e la direzione influenza l\'offset. Questo è in stretto rapporto con il modo in cui vengono trattati i fori nelle facce.





:   I contorni da trattare collettivamente devono essere complanari. I contorni da trattare in modo indipendente possono anche non essere complanari.

-    **Fill**(\"false\", \"true\"): se \"true\", lo spazio tra la faccia del contorno primitivo e l\'offset viene riempito con una faccia.

:   ![600px](images/Part_Offset2D_Fill.png)

## Script


<div class="mw-translate-fuzzy">

Lo strumento può essere utilizzato nelle [macro](macros/it.md) e dalla console python utilizzando la seguente funzione:


</div>


{{code|code=
f = App.ActiveDocument.addObject("Part::Offset2D", "Offset2D")
f.Source =  #some object
f.Value = 10.0
}}

Offset 2D è anche disponibile come metodo di Part.Shape. Esempio: {{code|code=
import Part
circle = Part.Circle().toShape()
enlarged_circle = circle.makeOffset2D(10.0)
Part.show(circle)
Part.show(enlarged_circle)
# makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection = false)
# 
# * offset: distance to expand the shape by. 
# 
# * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
# intersection
# 
# * fill: if true, the output is a face filling the space covered by offset. If
# false, the output is a wire/face.
# 
# * openResult: True for "Skin" mode; False for Pipe mode. 
# 
# * intersection: collective offset
# 
# Returns: result of offsetting (wire or face or compound of those). Compounding
# structure follows that of source shape.
}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset2D/it
