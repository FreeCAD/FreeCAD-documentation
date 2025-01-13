# CAM Postprocessor Customization/pl
}









## Wprowadzenie

FreeCAD używa jako wewnętrznej reprezentacji dla generowanych ścieżek tzw. kodów G-code. Mogą one opisywać takie rzeczy jak: prędkość i szybkość posuwu, zatrzymywanie silnika itp. Jednak najważniejsze są ruchy, które opisują. Te ruchy są dość proste: mogą to być linie proste lub łuki okręgowe. Bardziej zaawansowane krzywe, takie jak krzywe złożone, są już przybliżane przez <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowisko pracy CAM](CAM_Workbench/pl.md) we FreeCAD.



## Co postprocesor może dla Ciebie zrobić 

Wiele frezarek używa kodów G-code do kontrolowania procesu frezowania. Mogą one wyglądać niemal identycznie jak kody wewnętrzne, ale mogą występować pewne różnice:

-   maszyna może mieć specjalną sekwencję uruchamiania
-   może mieć specjalną sekwencję zatrzymywania
-   łuki mogą być definiowane z względnym lub bezwzględnym środkiem
-   może wymagać numerów linii w określonym formacie
-   mogą być używane tzw. cykle gotowe do predefiniowanych podprocesów, takich jak wiercenie
-   możesz preferować wyjście kodu G-code w jednostkach metrycznych lub imperialnych
-   może być użyteczne wykonanie zestawu ruchów przed wezwaniem zmiany narzędzia, aby ułatwić pracę operatorowi
-   możesz chcieć dodać komentarze dla czytelności lub je pominąć, aby program był mały
-   możesz chcieć dodać niestandardowy nagłówek, aby zidentyfikować lub udokumentować program do przyszłego odniesienia
-   \...

Ponadto, są inne języki do kontroli frezarek, takie jak PGL, DXF i inne.

Postprocesor to program, który tłumaczy wewnętrzne kody na kompletne pliki, które można wgrać na obrabiarkę.



## Przygotowania do napisania własnego postprocesora 

Możesz zacząć od bardzo prostego modelu pokazującego jak Twoja obrabiarka czyta poste linie i łuki. Przygotuj go w dowolnym programie odpowiednim dla Twojej obrabiarki.

Plik dla takich ścieżek zaczynających się w (0,0,0) i idących ku Y byłby pomocny. Upewnij się, że to samo narzędzie porusza się wzdłuż tej ścieżki - że nie trzeba zastosować kompensacji promienia narzędzia.

![](images/Path_PostProcessorSketch.png )

Ścieżka we FreeCAD wyglądałaby tak. Zauważ małą niebieską strzałkę, która wskazuje kierunek początkowy. Dla pierwszej próby możesz zdefiniować tylko jeden poziom w płaszczyźnie XY.

![](images/Path_PostProcessorModel.png )

Możesz następnie przejrzeć plik i porównać go z wyjściem istniejących postprocesorów, takich jak **linux_cnc_post.py** lub **grbl_post.py**, i spróbować dostosować je samodzielnie lub przesłać swój postprocesor na [forum Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15), aby uzyskać pomoc.



## Konwencja nazewnictwa 

Postprocesor można umieścić w katalogu makr FreeCAD. Dla przedrostka **<filename>**, postprocesor powinien mieć nazwę **<filename>_post.py**. Należy pamiętać, że przyrostek i rozszerzenie, **_post.py**, muszą być napisane małymi literami.

Nowa nazwa powinna być uwzględniona na czele listy argumentów parsowania w pliku **<filename>_post.py**, np.:


{{Code|lang=text|code=
parser = argparse.ArgumentParser(prog="grbl", add_help=False)
}}

Jeśli testujesz, umieść go w katalogu makr. Jeśli działa poprawnie, rozważ udostępnienie go innym (opublikuj na forum FreeCAD Path/CAM), aby mógł być uwzględniony w przyszłych wersjach dystrybucji FreeCAD.



## Inne istniejące postprocesory 

Dla porównania możesz sprawdzić postprocesory, które są dostarczane z instalacją FreeCAD. Znajdują się one w katalogu /Mod/CAM/Path/Post/scripts. Szeroko używane są postprocesory dla [linuxcnc](http://linuxcnc.org/) i [grbl](https://github.com/grbl/grbl). Analiza ich kodu może dostarczyć przydatnych wskazówek.



## Programowanie własnego postprocesora 

Ten post omawia niektóre szczegóły wewnętrzne postprocessorów linuxcnc. Ta sama struktura jest używana również w innych postprocessorach.

Patrząc na linux_cnc_post.py, zauważysz funkcję eksportu (w wersji 0.19.20514 jest w linii 156)


```python
def export(objectslist, filename, argstring):
    # pylint: disable=global-statement
    ...
    gcode = ""
    ...
    ...
```

zbiera krok po kroku w zmiennej \"gcode\" przetworzone kody G-code i zarządza ogólnym eksportem obiektów do postprocesingu (operacje, narzędzia, zadania itp.). Eksport obsługuje elementy na wysokim poziomie, takie jak komentarze i chłodziwo, ale wszelkie obiekty, które mają wiele poleceń CAM (zmiany narzędzi i operacje), deleguje do funkcji parse (w wersji 0.19.20514 znajduje się w linii 288).


```python
def parse(pathobj):
    ...
    out = ""
    lastcommand = None
    ...
    ...
```

Podobnie jak funkcja \"export\", funkcja parse zbiera kody G-code w zmiennej \"out\". W zmiennej \"command\" przechowywane są polecenia, które są widoczne w funkcji \"inspect G-code\" w środowisku pracy CAM i mogą być analizowane w celu dalszego przetwarzania.


```python
        for c in pathobj.Path.Commands:

            command = c.Name
```

Rozpoznaje różne kody G, M, F, S i inne kody G-code. Zapamiętując ostatnie polecenie w zmiennej \"lastcommand\", może tłumić późniejsze powtórzenia poleceń modalnych.

Zarówno funkcje parse, jak i export zajmują się formatowaniem ciągów znaków i łączeniem ich w końcowe wyjście.

Obie funkcje wywołują również funkcję \"linenumber()\". Jeśli użytkownik chce numerów linii, funkcja linenumber zwraca ciąg znaków, który należy wstawić w odpowiednie miejsce, w przeciwnym razie zwraca pusty ciąg, więc nic nie jest dodawane.



## Powiązane

-   <img alt="" src=images/CAM_Post.svg  style="width:24px;"> [CAM: Przetwarzanie końcowe](CAM_Post/pl.md)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Postprocessor Customization/pl
