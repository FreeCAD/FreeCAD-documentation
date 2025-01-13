# CAM SetupSheet/pl
## Opis

Użycie **Karty konfiguracji** pozwala użytkownikowi dostosować sposób, w jaki różne wartości właściwości dla operacji będą obliczane. Użytkownik zawsze ma możliwość nadpisania wartości z Karty konfiguracji jawnie podaną wartością lub zmiany sposobu obliczania tych wartości.

Ponieważ Karty konfiguracji są częścią zadania CAM, ich wartości nie zmieniają domyślnego zachowania środowiska CAM. Zamiast tego, zmieniają jedynie zachowanie w kontekście bieżącego zadania.

Karty konfiguracji są szczególnie przydatne po zapisaniu z [Szablonem zadania](CAM_ExportTemplate/pl.md).



## Właściwości

-    **VertRapid**: Ustawia szybkość pionowego ruchu w nowym kontrolerze narzędzia. (Używane w postprocessorach obsługujących dostosowywane szybkości ruchu)

-    **HorizRapid**: Ustawia szybkość poziomego ruchu w nowym kontrolerze narzędzia. (Używane w postprocessorach obsługujących dostosowywane szybkości ruchu)

-    **SafeHeightOffset**: Zastosowanie tego pola zależy od SafeHeightExpression (patrz poniżej)

-    **SafeHeightExpression**: Wynik tego wyrażenia zostanie użyty do ustawienia bezpiecznej wysokości operacji.

-    **ClearanceHeightOffset**: Zastosowanie tego pola zależy od ClearanceHeightExpression (patrz poniżej)

-    **ClearanceHeightExpression**: Wynik tego wyrażenia zostanie użyty do ustawienia wysokości oczyszczenia operacji.

-    **StartDepthExpression**: Wynik tego wyrażenia zostanie użyty do ustawienia właściwości głębokości początkowej operacji.

-    **FinalDepthExpression**: Wynik tego wyrażenia zostanie użyty do ustawienia właściwości ostatecznej głębokości operacji.

-    **StepDownExpression**: Wynik tego wyrażenia zostanie użyty do ustawienia właściwości kroku w dół operacji.



## Parametry operacji 

Oto wartości pobierane z:

-   OpFinalDepth - Wartość właściwości FinalDepth
-   OpStartDepth - Wartość właściwości StartDepth
-   OpToolDiameter - Wartość właściwości Średnica narzędzia kontrolera narzędzia, do którego odnosi się operacja



## Wartości karty konfiguracji 

Do innych wartości w karcie konfiguracji można się odwoływać bezpośrednio :

-   SetupSheet.ClearanceHeightOffset
-   SetupSheet.SafeHeightOffset

-   StartDepth
-   SafeHeightOffset
-   SafeHeightExpression
-   ClearanceHeightOffset
-   ClearanceHeightExpression
-   StartDepthExpression
-   FinalDepthExpression
-   StepDownExpression





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM SetupSheet/pl
