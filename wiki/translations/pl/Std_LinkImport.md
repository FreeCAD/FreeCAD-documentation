---
 GuiCommand:
   Name: Std LinkImport
   Name/pl: Std: Importuj łącza
   MenuLocation: brak
   Workbenches: wszystkie
   Version: 0.19
   SeeAlso: Std_LinkMake/pl, Std_LinkMakeRelative/pl, Std_LinkImportAll/pl
---

# Std LinkImport/pl



## Opis

Narzędzie **[<img src=images/Std_LinkImport.svg style="width:16px"> '''Importuj łącza'''** importuje właściwość **Połączony obiekt** z Łącza do bieżącego dokumentu, a następnie zmienia powiązanie do tego obiektu.

Operacja ta jest pomocna podczas pracy ze [złożeniami](Assembly/pl.md) w celu uporządkowania modeli wielokrotnie użytych, które mogą znajdować się w innych dokumentach.

Użyj narzędzia **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Importuj wszystkie łącza](Std_LinkImportAll/pl.md)**, aby zaimportować wszystkie połączone obiekty.



## Użycie

1.  Upewnij się, że masz dokument \"źródłowy\" z oryginalnym obiektem, powiedzmy **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)** i drugi dokument \"docelowy\" z Łączem do tego obiektu.
2.  Otwórz dokument docelowy i wybierz Łącze do obiektu; jego właściwość **Powiązany obiekt** powinna pokazywać coś w rodzaju {{Value|source#Part}}.
3.  Naciśnij **[<img src=images/Std_LinkImport.svg style="width:16px"> '''Importuj łącza'''**.

Kopia oryginału **[<img src=images/Std_Part.svg style="width:16px"> [Części](Std_Part/pl.md)** musi teraz znajdować się wewnątrz bieżącego dokumentu \"docelowego\". Właściwość **Powiązany obiekt** Łącza musi teraz wskazywać {{Value|Część}}, informując, że Łącze nie odnosi się już do obiektu {{Value|Części}} w \"źródle\", ale do {{Value|Części}} w bieżącym dokumencie *(\"docelowym\")*.

![](images/Std_Link_tree_import_1_example.png ) ![](images/Std_Link_tree_import_2_example.png )



*Z lewej: Łącze wskazuje na obiekt w dokumencie "źródłowym". Z prawej: oryginalny obiekt został zaimportowany ''(skopiowany)'' do dokumentu "docelowego", a istniejące łącze zostało zmienione, aby wskazywało na tę kopię, więc nie wskazuje już na obiekt w dokumencie "źródłowym".
Naciśnij **CTRL* + {{KEY|ENTER**", aby potwierdzić i przejść do następnej wiadomości, lub **ALT** + **SHIFT** + **D**, aby pominąć, lub **ALT** + **SHIFT** + **B**, aby podać opis zmian, lub przytrzymaj **ALT**, aby zobaczyć inne skróty.}}





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkImport/pl
