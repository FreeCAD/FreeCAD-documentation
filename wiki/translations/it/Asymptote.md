# Asymptote/it
## Descrizione

[Asymptote](https://asymptote.sourceforge.io/) è un linguaggio vettoriale per la computer grafica 2D e 3D. Il codice Asymptote può essere incluso nei documenti [LaTeX](https://www.latex-project.org/) o utilizzato per generare [PostScript](https://en.wikipedia.org/wiki/PostScript), [PDF](PDF/it.md) , [SVG](SVG/it.md), [WebGL](https://www.khronos.org/webgl/) e [PRC](https://en.wikipedia.org/wiki/PRC_(file_format)). I file PDF 3D interattivi creati dal codice Asymptote richiedono Acrobat Reader versione 9 o successiva.

Il supporto per Asymptote è stato aggiunto nella versione 0.19 di FreeCAD.



## Esportazione

1.  Facoltativamente, assegnare i colori alle facce dell\'oggetto che si desidera esportare con il comando <img alt="" src=images/Part_ColorPerFace.svg  style="width:24px;"> [Part: Colore per faccia](Part_ColorPerFace/it.md).
2.  Passare a <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh](Mesh_Workbench/it.md).
3.  Creare una mesh dall\'oggetto con il comando <img alt="" src=images/Mesh_FromPartShape.svg  style="width:24px;"> [Mesh: Crea mesh da una forma](Mesh_FromPartShape/it.md).
4.  Selezionare il nuovo oggetto mesh.
5.  Richiamare il comando <img alt="" src=images/Mesh_Export.svg  style="width:24px;"> [Mesh: Esporta mesh](Mesh_Export/it.md).
6.  Selezionare il formato file ***.asy** nella finestra di dialogo.
7.  Inserire un nome di file.
8.  Premere il pulsante **Salva**.



## Conversione

È necessario il [compilatore Asymptote](https://sourceforge.net/projects/asymptote/) per convertire i file ***.asy**. Per convertire in PDF è necessario anche un sistema [1](https://www.latex-project.org/get/LaTeX).

Il compilatore è uno strumento da riga di comando. Per convertire in PDF puoi usare questa sintassi: 
```pythonPathToAsyExecutable/asy -f pdf AsymptoteFileName.asy```



## Correlati

-   [Importa Esporta](Import_Export/it.md)



## Tutorial video 

I seguenti video sono in spagnolo:

-   [Un modo per generare file pdf-3D interattivi. (1/3) (Da FreeCAD, MeshLab e LaTeX)](https://www.youtube.com/watch?v=U0m3643Vb1Q)
-   [Un modo per generare file pdf-3D interattivi. (2/3) (Da Asymptote e LaTex)](https://www.youtube.com/watch?v=PhVNvDZIerM)
-   [Un modo per generare file pdf-3D interattivi. (3/3) (Da FreeCAD, Asymptote e LaTeX)](https://www.youtube.com/watch?v=Q_ufaCN2hb4)


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Mesh](Category_Mesh.md) > Asymptote/it
