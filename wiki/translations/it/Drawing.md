# Drawing/it
## Introduzione

In FreeCAD la parola \"[Drawing](Drawing/it.md)\" (Disegno tecnico) viene normalmente utilizzata per fare riferimento a una proiezione 2D di un [modello 3D](model/it.md). Generalmente viene creato con l\'ambiente [TechDraw ](TechDraw_Workbench/it.md).



## Utilizzo

1.  Iniziare con un [modello 3D](model/it.md) già creato, creato ad esempio con [PartDesign](PartDesign_Workbench/it.md). In realtà, funziona con qualsiasi oggetto che ha una [Forma](Shape/it.md), inclusi gli oggetti 2D.
2.  Passare in [TechDraw](TechDraw_Workbench/it.md).
3.  Premere il pulsante **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [Nuovo disegno standard](TechDraw_PageDefault/it.md)** o **[<img src=images/TechDraw_PageTemplate.svg style="width:16px"> [Nuovo disegno da modello](TechDraw_PageTemplate/it.md)** per creare una pagina.
4.  Selezionare il modello esistente, quindi premere **[<img src=images/TechDraw_View.svg style="width:16px"> [Vista di oggetto](TechDraw_View/it.md)** o **[<img src=images/TechDraw_ProjectionGroup.svg style="width:16px"> [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)**.
5.  Viene creata una proiezione 2D sulla pagina. Ora è possibile regolare le sue proprietà, ad esempio **Scala**, **Rotazione**, e **Direzione**.
6.  Quando il disegno è pronto, è possibile premere **[<img src=images/TechDraw_ExportPageSVG.svg style="width:16px"> [Esporta pagina in SVG](TechDraw_ExportPageSVG/it.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width:16px"> [Esporta pagina in DXF](TechDraw_ExportPageDXF/it.md)**, o usare [Esporta](Std_Export/it.md), per esportare la pagina in formato SVG, DXF o PDF per un ulteriore utilizzo in un altro software o per la stampa.



## Note

Nell\'uso informale, un \"Disegno\"può essere qualsiasi figura geometrica che è visibile nel [vista 3D](3D_view/it.md), e quindi il suo concetto può essere confuso con quello di \"[Corpo](Body/it.md)\", \"[Parte](Part/it.md)\", o \"[modello](Model/it.md)\".

Tuttavia, quando è richiesta maggiore precisione, è necessario fare distinzione.

-   Un \"[Corpo](Body/it.md)\" ([Corpo o Body di PartDesign](PartDesign_Body/it.md)) è un oggetto derivato da una [Part Feature](Part_Feature/it.md) (classe `Part::Feature`), creato con [PartDesign](PartDesign_Workbench/it.md).
-   Una \"[Parte](Part/it.md)\" ([App Part](App_Part.md)) è usato per raggruppare diversi \"[Corpi](Body/it.md)\" per formare un assemblaggio.
-   Un \"Disegno\" è una proiezione 2D di un \"Corpo\" o di una \"Parte\".


{{TechDraw Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/it
