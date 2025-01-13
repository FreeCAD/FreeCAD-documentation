---
 GuiCommand:
   Name: FEM MeshGroup
   Name/pl: Grupa siatki
   MenuLocation:  Siatka , Grupa siatki MES
   Workbenches: FEM_Workbench/pl
   Shortcut: 
   SeeAlso: FEM_tutorial/pl
---

# FEM MeshGroup/pl



## Opis

Umożliwia tworzenie grup wierzchołków, krawędzi, powierzchni i elementów. Jest to przydatne gdy FreeCAD jest używany jako preprocessor do eksportu zorganizowanej i oznakowanej siatki. Siatka może być wtedy użyta przez zewnętrzne solvery, gdzie grupy siatki mogą być łatwiejsze w użyciu do definiowania warunków brzegowych i przypisywania właściwości związanych z solverem. Możliwe jest użycie nazwy obiektu grupy siatki lub etykiety jako nazwy grupy do eksportu siatki. Jeśli wybrana jest etykieta, należy uważać na znaki specjalne. Jeśli format eksportu ich nie wspiera, należy użyć nazwy obiektu grupy siatki.

To narzędzie umożliwia więc używanie programu FreeCAD z zewnętrznymi solverami *(lub przeglądarkami takimi jak ParaView)*, które nie są obecnie zaimplementowane we FreeCAD.



## Użycie

1.  Aby skorzystać z tego narzędzia, należy najpierw utworzyć <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [Siatkę MES z kształtu przy pomocy generatora Gmsh](FEM_MeshGmshFromShape/pl.md)
2.  Następnie należy zaznaczyć obiekt siatki w [widoku drzewa](Tree_view/pl.md) i
    -   wcisnąć przycisk **<img src="images/FEM_MeshGroup.svg" width=24px> '''Grupa siatki MES'''** lub
    -   wybrać opcję **Siatka → <img src="images/FEM_MeshGroup.svg" width=24px> Grupa siatki MES** z menu.
3.  Kolejnym krokiem jest wybór czy grupa ma korzystać z nazwy obiektu czy wprowadzonej etykiety
    -   Jeśli zaznaczona jest **Nazwa**, podczas eksportu zostanie użyta nazwa obiektu grupy siatki.
    -   Jeśli zaznaczona jest **Etykieta**, podczas eksportu zostanie użyta wprowadzona etykieta.
4.  Kliknij przycisk **Dodaj** i wybierz obiekt geometryczny *(bryłę, ścianę, krawędź lub wierzchołek)*. Można dodać więcej takich obiektów, ale muszą one być tego samego typu. Grupa siatki będzie składać się z podstawowych elementów siatki.
5.  Wciśnij przycisk **OK**.

    :   Rezultat: Powinieneś zobaczyć nowy obiekt `FEMMeshGroup` pod obiektem `FEMMeshGMSH` w aktywnym kontenerze analizy.
6.  Kliknij dwukrotnie na obiekcie `FEMMeshGMSH` w drzewie modelu i wciśnij przycisk **Zastosuj** aby wymusić ponowne przeliczenie/etykietowanie siatki.
7.  Zamknij okno dialogowe.



## Uwagi

-   Po utworzeniu siatki można zmienić etykietę przy pomocy [edytora właściwości](Property_editor/pl.md).
-   Po zmianie właściwości należy ponownie otworzyć okno dialogowe Gmsh i wcisnąć przycisk **Zastosuj** *(można pozostawić okno dialogowe otwarte podczas zmieniania właściwości)*.
-   Można utworzyć tyle grup siatki, ile potrzeba.
-   Domyślnie grupy siatek mogą być eksportowane tylko do formatów .med i .unv. Aby móc eksportować je do formatu .inp, należy włączyć opcję *Eksportuj dane grupy* w [preferencjach eksportu INP](Import_Export_Preferences/pl#INP.md).
    -   Ustawienie preferencji *Które elementy siatki wyeksportować* na *Najwyższe* lub *MES* zapewni, że elementy niższych rzędów nie używane w analizie (np. powłokowe w przypadku analizy na bryłach) nie będą eksportowane.
    -   Aby wyeksportować zestawy węzłów do tego formatu, właściwość **Groups Of Nodes** [obiektu siatki Gmsh](FEM_MeshGmshFromShape/pl.md) musi być ustawiona na {{true/pl}}.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM MeshGroup/pl
