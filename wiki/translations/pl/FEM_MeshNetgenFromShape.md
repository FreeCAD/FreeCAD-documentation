---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MeshNetgenFromShape
   Name/pl: Siatka MES z kształtu przy pomocy generatora Netgen
   MenuLocation: Siatka , Siatka MES z kształtu przy pomocy generatora Netgen
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM MeshNetgenFromShape/pl



## Opis

Do analizy metodą elementów skończonych konieczna jest dyskretyzacja geometrii do [siatki MES](FEM_Mesh/pl.md). To narzędzie korzysta z programu [Netgen](https://www.ngsolve.org/) *(który musi być zainstalowany w systemie)* do generowania siatki. Siatki Netgen nie są wspierane przez [Elmer](FEM_SolverElmer/pl.md).

W zależności od Twojego systemu operacyjnego i pakietu instalacyjnego, Netgen może być dołączony do programu FreeCAD lub nie. Więcej informacji można znaleźć na stronie [Instalacja środowiska MES](FEM_Install/pl.md).



## Użycie

1.  Wybierz kształt, których chcesz analizować. Dla objętości, musi to być bryła pojedyncza lub złożona. To drugie jest konieczne jeśli część jest wykonana z różnych materiałów *(bryłę złożoną można utworzyć przy pomocy narzędzia [Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md))*.
2.  Aktywuj narzędzie na jeden z następujących sposobów:
    -   Wciśnij przycisk **<img src="images/FEM_MeshNetgenFromShape.svg" width=16px> '''Siatka MES z kształtu przy pomocy generatora Netgen'''**.
    -   Wybierz opcję **Siatka → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> Siatka MES z kształtu przy pomocy generatora Netgen** z menu.
3.  Opcjonalnie, ustaw maksymalny/minimalny rozmiar elementów (domyślne ustawienie zwykle tworzy zbyt rzadkie siatki) i rząd elementów (używając pola *Elementy drugiego rzędu*).
4.  Opcjonalnie, zmień *Stopień zagęszczenia* na jedno z gotowych ustawień lub wybierz *Zdefiniowane przez użytkownika* i ręcznie ustaw parametry.
5.  Wciśnij przycisk **Zastosuj**, aby utworzyć siatkę. {{Version/pl|1.0}}: Opcjonalnie, użyj przycisku **Anuluj** aby zatrzymać generowanie siatki jeśli używasz nowej implementacji Netgen.
6.  Wciśnij przycisk **OK** aby wygenerować siatkę i zamknąć okno dialogowe. Możesz też kliknąć **Anuluj** aby anulować zmiany lub tworzenie obiektu siatki.



## Właściwości

-    **Max. Size**: Maksymalny rozmiar elementu w mm.

-    **Min. Size**: {{Version/pl|1.0}}: Minimalny rozmiar elementu w mm.

-    **Second order**: Elementy drugiego rzędu - mają więcej węzłów. Zwykle wystarczy użycie rzadszej siatki aby uzyskać taką samą dokładność jak przy pomocy elementów pierwszego rzędu,

    -   
        {{true/pl}}
        
        *(domyślnie)* elementy drugiego rzędu *(kwadratowe)*,

    -   
        {{false/pl}}
        
        elementy pierwszego rzędu *(liniowe)*.

-    **Fineness**: Predefiniowane poziomy gęstości siatki.

-    **Growth Rate**: Definiuje jak bardzo sąsiednie elementy będzie się różniły rozmiarem.

-    **Nb. Segs per Edge**: Definiuje minimalną liczbę segmentów siatki na krawędź.

-    **Nb. Segs per Radius**: Definiuje minimalną liczbę segmentów siatki na promień.

-    **Optimize**:

    -   
        {{true/pl}}
        
        *(domyślnie)* stosuje algorytm optymalizacji do poprawy jakości siatki,

    -   
        {{false/pl}}
        
        .





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshNetgenFromShape/pl
