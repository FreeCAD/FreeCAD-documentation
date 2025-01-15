# LGTM/it
## Descrizione




[LGTM](https://www.lgtm.com) è uno strumento di analisi del codice che può essere integrato in più sistemi di controllo della versione del software online e supporta diverse lingue. È un eccellente controllore della qualità del codice, che identifica i problemi del codice che spesso non vengono individuati da altri controllori del codice e linters.

LGTM è adatto come strumento di analisi del codice per lo sviluppo di ambienti di lavoro di FreeCAD in Python e altri progetti di dimensioni medio-piccole. Questa pagina offre una panoramica di come iniziare a usare LGTM con un ambiente di lavoro di FreeCAD in Python.



## Per iniziare 

Il modo in cui iniziare con LGTM dipende dalla piattaforma di controllo della versione online che si sta utilizzando. La documentazione LGTM per [revisione automatica del codice](https://lgtm.com/help/lgtm/about-automated-code-review) fornisce una buona panoramica di come integrare LGTM nel progetto per diverse piattaforme.

Inoltre su LGTM è possibile eseguire una vasta gamma di analisi approfondite del codice, che va oltre lo scopo di questo tutorial. Si possono leggere ulteriori informazioni al riguardo nella documentazione LGTM su [configuring code analysis](https://lgtm.com/help/lgtm/configuring-lgtm-analysis-project).



## Ottenere i Risultati 

Dopo aver configurato LGTM e fornito l\'accesso ai repository di codice, le analisi vengono in genere eseguite quotidianamente sul repository. Pertanto, le modifiche inviate non daranno risultati immediati. È possibile fare in modo che LGTM analizzi le pull requests nel momento in cui vengono inviate, come descritto nella documentazione LGTM.

Per rivedere i risultati è sufficiente accedere alla dashboard LGTM e selezionare il progetto desiderato. Da lì, l\'analisi del codice fornirà un elenco di problemi (come bug, pratiche di codifica deprecate, codice inutile/irrilevante/non utilizzato, ecc.) da esaminare. Inoltre LGTM fornisce \"classificazioni\" complessive del codice (A, B, C, D) a seconda del numero di problemi riscontrati rispetto alla dimensione complessiva del progetto.

Probabilmente, il modo più utile e immediato per gestire i risultati dell\'analisi del codice è semplicemente filtrare i file del progetto che non si desidera analizzare. Cioè, supponiamo che si stia sviluppando un nuovo codice parziale, mantenendo il codice legacy che altrimenti non verrebbe utilizzato o che si stia testando molto codice che non necessita di analisi. LGTM fornisce [classificazione dei file](https://lgtm.com/help/lgtm/file-classification), un modo semplice per filtrare tali file in modo che non inquinino i risultati dell\'analisi.

### Creazione di un file .lgtm.yml 

Per abilitare la classificazione dei file, creare prima un file denominato \".lgtm.yml\" nella directory più in alto del proprio progetto. Quindi, in quel file, aggiungere alcune classificazioni.

Di seguito è riportato un esempio tratto dall\'ambiente di lavoro Python di FreeCAD Trails:


```python
path_classifiers:
  template:
    - freecad/trails/resources
    - freecad/trails/project/commands/command_template.py
    - freecad/trails/init_gui.py
 
  test:
    - freecad/trails/project/commands/spiral_test.py
    - freecad/trails/TestFPO.py
 
  legacy:
    - freecad/trails/corridor/loft
    - freecad/trails/alignment/VerticalAlignment.py
    - freecad/trails/alignment/VerticalCurve.py
    - freecad/trails/alignment/GenerateVerticalAlignment.py
    - freecad/trails/alignment/ImportVerticalCurve.py
    - freecad/trails/corridor/template/TemplateLibrary.py
```

Tenere presente che i livelli di rientro sono importanti in LGTM. Un rientro errato comporterà una classificazione del file non riuscita.

Inoltre, alcune classificazioni (come \"template\" e \"test\") vengono utilizzate da LGTM per query e altri componenti di analisi. Si può anche definire i propri tag personalizzati, che filtreranno il codice e forniranno ulteriori risultati interrogabili.



## Link utili 

-   [Continuous Integration](Continuous_Integration/it.md)
-   LGTM [FreeCAD forum discussion thread](https://www.forum.freecadweb.org/viewtopic.php?f=10&t=40228)
-   FreeCAD .lgtm.yml file on [Github](https://github.com/FreeCAD/FreeCAD/blob/master/lgtm.yml)
-   freecad.trails .lgtm.yml on [Github](https://github.com/joelgraff/freecad.trails/blob/dev/.lgtm.yml)



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Testing](Category_Testing.md) > LGTM/it
