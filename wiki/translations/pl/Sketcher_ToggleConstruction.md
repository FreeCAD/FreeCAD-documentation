---
 GuiCommand:
   Name: Sketcher ToggleConstruction
   Name/pl: Szkicownik: Przełącz geometrię konstrukcji
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Przełącz tryb konstrukcji
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **N**
   SeeAlso: 
---

# Sketcher ToggleConstruction/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:24px;"> **Przełącz tryb konstrukcji** albo przełącza narzędzia tworzenia geometrii do / z trybu konstrukcyjnego, albo przełącza wybraną geometrię do / z geometrii konstrukcyjnej.

Geometria konstrukcji jest oznaczona specjalnym [kolorem](Sketcher_Preferences/pl#Wygląd_zewnętrzny.md) *(domyślnie niebieskim)* i *({{Version/pl|1.0}})* typem linii. Geometria konstrukcyjna nie jest widoczna poza szkicem, a jej zadaniem jest pomoc w definiowaniu wiązań i innej geometrii wewnątrz samego szkicu. Linie konstrukcyjne mogą być jednak używane jako oś obrotu przez [Wyciągnij przez obrót](PartDesign_Revolution/pl.md).

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">



## Użycie



### Przełączanie narzędzi 

1.  Upewnij się, że nie ma żadnego zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> '''Przełącz tryb konstrukcji'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_ToggleConstruction.svg" width=16px> Przełącz tryb konstrukcji**.
    -   Kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md) i z menu kontekstowego wybierz opcję **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Przełącz tryb konstrukcji**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **N**.
3.  Tryb narzędzi do tworzenia geometrii jest przełączany:
    -   W trybie normalnym ich ikony w menu i na pasku narzędzi są białe i tworzą zwykłą geometrię *(domyślnie w kolorze białym)*. Ikona tego narzędzia to: <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;">.
    -   W trybie konstrukcyjnym ikony menu i paska narzędzi są niebieskie i tworzą geometrię konstrukcyjną *(domyślny kolor niebieski)*. Ikona tego narzędzia wygląda następująco: <img alt="" src=images/Sketcher_ToggleConstruction_Constr.svg  style="width:16px;">.



### Przełączanie geometrii 

1.  Wybierz jeden lub więcej elementów w szkicu.
2.  Wywołaj narzędzie w sposób opisany powyżej lub za pomocą następującej dodatkowej opcji:
    -   Kliknij prawym przyciskiem myszy w sekcji **Elementy** [Panelu zadań](Sketcher_Dialog/pl.md) i wybierz opcję **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Przełącz tryb konstrukcji** z menu kontekstowego.
3.  Wybrane elementy zostaną zmienione z normalnej geometrii na geometrię konstrukcyjną lub odwrotnie. Ich wygląd zmienia się odpowiednio.
4.  Tryb narzędzi do tworzenia geometrii nie ulega zmianie.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/pl
