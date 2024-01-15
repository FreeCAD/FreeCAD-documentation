---
 GuiCommand:
   Name: Draft Drawing
   Name/it: Disegno
   Workbenches: Drawing_Workbench/it, Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: TechDraw_DraftView/it
---

# Draft Drawing/it



## Descrizione

Il comando <img alt="" src=images/Draft_Drawing.svg  style="width:24px;"> **Draft Drawing** inserisce viste degli oggetti selezionati in una pagina [drawing](Drawing_Workbench/it.md).

Questo comando è simile al comando [Draft View](Drawing_View/it.md) ma è ottimizzato per gli oggetti [Draft](Draft_Workbench/it.md). Contrariamente a quel comando, può gestire oggetti specifici come [Draft Quote](Draft_Dimension/it.md) e [Draft Testi](Draft_Text/it.md), e può eseguire il rendering delle facce.

Questo comando è ormai obsoleto. Utilizzare invece l\' [Ambiente TechDraw](TechDraw_Workbench/it.md) e il comando [TechDraw Vista di Draft](TechDraw_DraftView/it.md).

<img alt="" src=images/Draft_drawing_example.jpg  style="width:640px;"> 
*A sinistra gli oggetti Draft selezionati. A destra le viste del disegno create.*



## Utilizzo

1.  Per utilizzare questo comando in FreeCAD versione 0.19 e successive è necessario aggiungere un pulsante ad una barra degli strumenti personalizzata. Vedere [Personalizzazione dell\'interfaccia](Interface_Customization/it.md).
2.  Selezionare uno o più oggetti. Verrà creata una vista separata per ciascun oggetto.
3.  Facoltativamente aggiungere una pagina [Drawing](Drawing_Workbench/it.md) alla selezione. In caso contrario, la vista verrà inserita nella prima pagina del documento. Se nel documento non sono presenti pagine, viene creata prima una nuova pagina.
4.  Premere il pulsante **<img src="images/Draft_Drawing.svg" width=16px> [Draft Drawing](Draft_Drawing/it.md)**.
5.  C\'è un bug nella versione 0.19 del comando di FreeCAD. Il valore iniziale della proprietà **Direction** è {{Value|[0, 0, 0]}} che non è consentito. Per gli oggetti su un piano parallelo al piano XY del sistema di coordinate globale dovrebbe essere modificato in {{Value|[0, 0, 1]}}. Dopo aver modificato questa proprietà, potrebbe essere necessario [ricalcolare](Std_Refresh/it.md) la pagina e la vista.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Drawing/it
