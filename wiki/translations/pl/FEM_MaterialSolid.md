---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MaterialSolid
   Name/pl: Materiał dla bryły
   MenuLocation: Model , Materiały , Materiał dla bryły
   Workbenches: FEM_Workbench/pl
   Shortcut: **M** **S**
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Wszystkie
}}
---

# FEM MaterialSolid/pl



## Opis

Tworzy materiał dla ciała stałego.

![](images/FEMMaterialSolidProperties.png ) 
*Okno dialogowe materiału MES*



## Użycie

1.  Aby stworzyć nowy obiekt MaterialSolid, skorzystaj z jednego z następujących podejśćː
    -   Wciśnij przycisk **<img src="images/FEM_MaterialSolid.svg" width=16px> '''Materiał dla bryły'''**.
    -   Wybierz opcję **Model → Materiały → <img src="images/FEM_MaterialSolid.svg" width=16px> Materiał dla ciała stałego‏‎** z menu.
2.  Aby edytować istniejący obiekt MaterialSolid:
    -   Dwukrotnie kliknij na nim w [widoku drzewa](Tree_view/pl.md).
3.  Zostanie otwarte okno dialogowe materiału MES.
4.  Wybierz materiał z listy rozwijanej. Przykładowo, materiał *CalculiX-Steel* jest często używany do analiz mechanicznych.
5.  Opcjonalnie, zaznacz pole **Użyj tego panelu zadań** aby zmodyfikować właściwości materiału, takie jak gęstość, moduł Younga, współczynnik Poissona itp.
6.  Jeśli definiujesz materiał dla całego modelu, nie wybieraj żadnych obiektów geometrycznych *(zostaw pustą listę odniesień)*. Materiał zostanie automatycznie przypisany do całego modelu. W innym wypadku, przypisz materiały do wybranych obszarów ręcznie, poprzez wybieranie ich do poszczególnych definicji materiału, ale nie zostawiaj żadnej części modelu bez definicji materiału.
7.  Wciśnij przycisk **Zamknij** aby zamknąć okno dialogowe.



## Uwagi

1.  Materiał mechaniczny korzysta ze [słowa kluczowego \*MATERIAL w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/pl
