---
 GuiCommand:
   Name: FEM SolverMystran
   Name/pl: Solver Mystran
   MenuLocation: Rozwiąż , Solver Mystran
   Workbenches: FEM_Workbench/pl
   Shortcut: **S** **M**
   Version: 0.20
   SeeAlso: FEM_tutorial/pl
---

# FEM SolverMystran/pl



## Opis

Polecenie **SolverMystran** umożliwia używanie solvera [MYSTRAN](https://www.mystran.com). Można z niego skorzystać do:

1.  Ustawienia parametrów analizy.
2.  Wybrania katalogu roboczego.
3.  Uruchamiania solvera MYSTRAN.



## Instalacja

### Windows

Plik wykonywalny solvera Mystran dla Windows można znaleźć [w serwisie GitHub](https://github.com/MYSTRANsolver/MYSTRAN). Wskaż folder, w którym jest **mystran.exe** (plik wykonywalny musi się dokładnie tak nazywać - usuń pozostałą część domyślnej nazwy) w zmiennej PATH systemu Windows lub po prostu umieść plik w katalogu **FreeCAD\bin**. Jeśli to konieczne, wybierz go w **Preferencje → MES → Mystran**.

**Solver Mystran** wymaga też dwóch innych pakietów:

-   [pyNastran](https://github.com/SteveDoyle2/pyNastran) - do zapisywania pliku przypadku analizy.
-   [hfcMystran](https://github.com/ceanwang/hfcMystran) - do odczytywania plliku wyników NEU Mystrana.

pyNastran można zainstalować poprzez pip:

1.  Otwórz wiersz poleceń w Twoim folderze **FreeCAD\bin**.
2.  Wprowadź: {{Incode|python -m pip install pyNastran}}
3.  Zostanie zainstalowany w folderze **FreeCAD\bin\lib\site-packages**.

hfcMystran można pobrać z jego strony GitHub jako plik zip (*Code \--\> Download ZIP*). Wypakuj go i umieść w folderze **FreeCAD\Mod**.

### Linux

Instalacja w systemie Linux jest podobna, ale są pewne różnice.

Po pobraniu pliku wykonywalnego Mystrana, zmień jego nazwę jak wyjaśniono powyżej, pozwól na jego uruchamianie (*prawy przycisk myszy → Properties → Permissions → Allow executing file as program*) i umieść go w katalogu **usr/bin** programu FreeCAD.

Aby zainstalować pyNastran, wprowadź następujące polecenia w [konsoli Pythona](Python_console/pl.md) w programie FreeCAD:


```python
import subprocess
subprocess.run(['pip', 'install', 'pyNastran'])
```

Wreszcie, pobierz i rozpakuj hfcMystran i umieść go w katalogu **usr/Mod** programu FreeCAD.



## Szybki test 

Po instalacji możesz wybrać **Narzędzia → Otwórz przykłady** w środowisku pracy MES. Pod **Solver → Mystran** znajdziesz kilka działających przykładów.



## Użycie

1.  Po utworzeniu <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Kontenera analizy](FEM_Analysis/pl.md), skorzystaj z jednej z następujących możliwości:
    -   Wybierz opcję **Rozwiąż → <img src="images/FEM_SolverMystran.svg" width=x16px> Solver Mystran** z menu.
    -   Wciśnij klawisz **S** a następnie **M**.
2.  Dwukrotnie kliknij na obiekcie <img alt="" src=images/FEM_SolverMystran.svg  style="width:" height="16px;"> SolverMystran.
3.  Wciśnij przycisk **Zapisz**.
4.  Wciśnij przycisk **Uruchom**.



## Ograniczenia

-   Obecnie tylko przemieszczenia są dostępne jako wykresy konturowe z analiz z tym solverem. Aby zobaczyć naprężenia, przełącz się do środowiska pracy hfMystran, otwórz swój przypadek i jego plik F06. Do tworzenia wykresów wszystkich wyników można skorzystać z GUI pyNastran.
-   Tylko następujące typy elementów są obecnie wspierane: czworościany pierwszego i drugiego rzędu, trójkątne i czworokątne elementy powłokowe pierwszego rzędu oraz elementy belkowe pierwszego rzędu. Jeśli inne elementy zostały wygenerowane przy pomocy Gmsh, solver Mystran wyświetli błąd.



## Funkcja plików 

Pod Mod\\Fem\\femsolver\\mystran są następujące plikiː


```python
add_con_displacement.py
add_con_fixed.py
add_con_force.py
add_femelement_geometry.py
add_femelement_material.py
add_mesh.py
add_solver_control.py
writer.py
solver.py
tasks.py
```

Funkcja każdego pliku toː

writer.py - główny plik kontrolny


```python
model = BDF()
model = add_solver_control.add_solver_control(pynasf, model, self)
model = add_femelement_geometry.add_femelement_geometry(pynasf, model, self)
model = add_mesh.add_mesh(pynasf, model, self)
model = add_femelement_material.add_femelement_material(pynasf, model, self)
model = add_con_fixed.add_con_fixed(pynasf, model, self)
model = add_con_displacement.add_con_displacement(pynasf, model, self)
model = add_con_force.add_con_force(pynasf, model, self)
```

BDF() - Utwórz pusty plik przypadku.


```python
$pyNastran: version=msc
$pyNastran: punch=False
$pyNastran: encoding=utf-8
$pyNastran: nnodes=0
$pyNastran: nelements=0
ENDDATA
```

add_solver_control.py - Dodawanie EXECUTIVE CONTROL DECK i CASE CONTROL DECK.


```python
$EXECUTIVE CONTROL DECK
SOL 101
CEND
$CASE CONTROL DECK
ECHO = NONE
TITLE = pyNastran for generating solverinput for for Mystran
SUBCASE 1
    DISPLACEMENT(SORT1,REAL) = ALL
    LOAD = 1
    SPC = 1
    SPCFORCES(SORT1,REAL) = ALL
    STRESS(SORT1,REAL,VONMISES,BILIN) = ALL
    SUBTITLE = Default
BEGIN BULK
$PARAMS
PARAM       POST      -1
```

add_femelement_geometry.py - Dodawanie kart GRID

add_mesh.py - Dodawanie kart elementów

add_femelement_material.py - Dodawanie karty MAT1

add_con_fixed.py - Dodawanie kart SPCADD i SPC1

add_con_displacement.py - Dodawanie kart SPCADD i SPC1

add_con_force.py - Dodawanie kart FORCE





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverMystran/pl
