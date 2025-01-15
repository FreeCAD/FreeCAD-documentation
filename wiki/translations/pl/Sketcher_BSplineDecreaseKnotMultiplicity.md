---
 GuiCommand:
   Name: Sketcher BSplineDecreaseKnotMultiplicity
   Name/pl: Szkicownik: Zwiększ krotność węzła krzywej złożonej
   MenuLocation: Szkic , Narzędzia szkicownika krzywej złożonej , Zwiększ krotność węzła krzywej złożonej
   Workbenches: Sketcher_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_BSplineIncreaseKnotMultiplicity/pl
---

# Sketcher BSplineDecreaseKnotMultiplicity/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:24px;"> **Zmniejsz krotność węzła krzywej złożonej** zmniejsza krotność węzła [krzywej złożonej](B-Splines/pl.md).



## Użycie

1.  Wybierz węzeł krzywej złożonej.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> '''Zmniejsz stopień krzywej złożonej'''**.
    -   Wybierz z menu **Szkic → Narzędzia szkicownika krzywej złożonej → <img src="images/Sketcher_BSplineDecreaseKnotMultiplicity.svg" width=16px> Zmniejsz stopień krzywej złożonej**.



## Przykład

Zapoznaj się z informacjami na stronie: [Zwiększ krotność węzłów krzywej złożonej](Sketcher_BSplineIncreaseKnotMultiplicity/pl#Użycie.md)



## Uwagi

Zmniejszenie krotności węzła do zera powoduje jego zniknięcie. W sensie matematycznym pojawia się on wtedy zero razy w wektorze węzłów, co oznacza, że nie ma już funkcji bazowej. Aby to zrozumieć, potrzeba trochę matematyki, ale będzie to również jasne, jeśli spojrzysz na krotność. Na przykład węzeł o krotności 0 na krzywej zlożonej o stopniu 3 oznacza, że w miejscu węzła dwie części Béziera są połączone ciągłością „C^3^". Zatem trzecia pochodna powinna być równa po obu stronach węzła. Jednak w przypadku sześciennej krzywej Béziera oznacza to, że obie strony muszą być częścią tej samej krzywej. W rzeczywistości nie ma już węzła łączącego dwie krzywe Béziera.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/pl
