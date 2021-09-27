# Material/it
}


<div class="mw-translate-fuzzy">

Questa pagina riguarda il sistema di dati dei materiali in FreeCAD.

Nel piano di sviluppo è contenuto il [Modello di dati dei materiali](http://www.freecadweb.org/wiki/index.php?title=Material_data_model/it)


</div>


{{TOCright}}

This page is about the Material data system in FreeCAD.


<div class="mw-translate-fuzzy">

## Introduzione

Poiché è difficile, se non impossibile, definire un insieme rigido o completo delle proprietà dei materiali, procediamo nel modo più aperto. Ogni oggetto che in FreeCAD ha a che fare con un materiale avrà una proprietà denominata \"Material\", che è una lista di chiavi o valori che può contenere un numero indefinito di proprietà dei materiali. Dato che questo è un sistema molto aperto ed estensibile per trattare tali dati, esso contiene anche il pericolo di creare caos. Pertanto questa pagina definisce alcune regole e le proprietà di base per trattare queste mappe-di-proprietà-dei-materiali (material-property-maps).


</div>

## Regole

Ogni set di proprietà ha un solo ingresso obbligatorio che è \"Name\" (Nome, univoco). Questa è la chiave primaria del materiale. Le rimanenti proprietà del materiale sono facoltative o possono essere recuperate da un DataBase dei materiali.

I nomi delle proprietà (chiavi) sono ordinati per stringhe separate da trattini. La prima sottostringa è definita dall\'applicazione o è standard, la successiva può essere utilizzata per un ulteriore gruppo di proprietà. I valori possono anche essere raggruppati con il segno di sottolineatura, come ad esempio, per distinguere i diversi tipi di acciaio. Esempio:

-   Name=Steel\_Cast
-   SpecificWeight=7.85 (a 20° in kg/dm³)
-   EN10027\_name = S235JR+AR (acciaio standard EN 10027-1)
-   FEM\_YoungsModulus = xx in mm−1·kg·s−2
-   FEM\_YoungsModulus\_Z
-   FEM\_YoungsModulus\_X


<div class="mw-translate-fuzzy">

Ogni proprietà ha una descrizione in linguaggio umano in questa pagina del Materiale, con eventuali link a ulteriori informazioni (ad esempio a Wikipedia).


</div>

Per ogni proprietà deve essere definita una unità di misura, in base al sistema di unità interno mm-kg-s di FreeCAD! Ciò consente un utilizzo e una traduzione coerenti.

La chiave (nome) e i valori delle proprietà utilizzano solo caratteri ASCII (7 bit). Le chiavi sono scritte in [Camel-Case](http://it.wikipedia.org/wiki/Notazione_a_cammello) (maiuscole anche all\'interno della parola), ma interpretate come case-insensitive (non sensibili alle maiuscole).

La sottolineatura (separazione delle parole con il carattere di sottolineatura) consente poi una vista ad albero delle proprietà per editarle o visualizzarle raggruppate.

## Strumenti

Ci sono alcune buone risorse esterne per gestire più facilmente i materiali:

-   [Units calculater](http://www.dimensionengine.com/) per informazioni sul materiale nell\'unità necessaria per FreeCAD
-   [<http://www.matweb.com/>](http://www.matweb.com/) [free of charge](http://matweb.com/reference/terms.aspx) database gratuito con migliaia di dati sui materiali

## Database dei materiali 

Dato per scontato che lo standard di cui sopra sia stato implementato, è sciocco ripetere la memorizzazione di tutte le proprietà per ogni oggetto. Fondamentalmente siamo in grado di costruire un DataBase dei Materiali con il nome come chiave primaria. Quindi, se non ci sono esigenze particolari, per un materiale è sufficiente definire, ad esempio, Name = Acciaio e FreeCAD può recuperare tutte le proprietà dal DB. Ogni ulteriore proprietà impostata nella mappa sovrascrive quella del DB.

In futuro possiamo ospitare questo DB da qualche parte nel web e costruire un DB OpenSource generale dei materiali.

Al momento penso a una lista compilata con un mini set di dati per una serie di materiali \"di base\" e le loro proprietà di base e a una versione completa basata su SQLite.


<div class="mw-translate-fuzzy">

## Material.py

Dato che la manipolazione delle proprietà-dei-materiali è un lavoro noioso dovremmo implementare un modulo Python front-end, il modulo per l\'acquisizione dei dati di ingresso, chiamato Material.py. Questo sarà il luogo per implementare tutti i tipi di metodi di supporto per la manipolazione dei materiali.

-   Calcolo della massa da volume e densità
-   Traduzione in diverse unità di misura
-   Calcoli necessari in speciali applicazioni (es. FEM)
-   e qualsiasi altra cosa che ancora non sappiamo\...


</div>

Il modulo implementato in questo modo può essere eseguito in FreeCAD o indipendentemente dalla riga di comando (la mappa-proprietà-dei-materiali deve essere data come mappa python).


<div class="mw-translate-fuzzy">

## Formato dei file della cartella dei materiali di FreeCAD 

Lavorare con i materiali significa spesso importare o esportare delle definizioni-di-materiali. È quindi necessario stabilire un formato dei file. Dal momento che abbiamo solo la forma chiave o valore, possiamo utilizzare un formato di file semplice, facile da leggere e da analizzare. Quindi viene scelto il formato [ini-file](http://en.wikipedia.org/wiki/INI_file). È standardizzato e ci sono già dei parser disponibili. Ad esempio il [Config parser module in python](http://docs.python.org/2/library/configparser.html).


</div>


<div class="mw-translate-fuzzy">

Ogni definizione di materiale risiede in un file con l\'estensione .FCMat. Alcuni di questi file sono parte del sorgente di FreeCAD e sono compilati nel binario. Questo per salvarli come risorsa aggiuntiva della distribuzione e averne accesso. Ma i file possono anche essere posizionati e cercati in posti diversi per consentire la definizione di materiali aggiuntivi, non standard.


</div>


<div class="mw-translate-fuzzy">

### Esempi

; last modified 1 April 2001 by John Doe
Name=Steel_Cast
Father=Steel
Source=Some material book everyone knows (or not) ;Some comment
 
[EN10027]
; steel standard EN 10027-1
Name=S235JR+AR      
[Graphic]
Color_Emissiv = 255,255,255


</div>

## Proprietà del materiale 

Ecco ora la descrizione delle proprietà-dei-materiali concordate. Sentitevi liberi di aggiungere una sottosezione per le proprietà-del-materiale del vostro campo di competenza.

### Generale


<div class="mw-translate-fuzzy">

  Nome della proprietà   Descrizione                                                                                                                                                                                                                                                                                        Unità/Tipo di Dati
  ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------
  Name                   Nome univoco della proprietà, seguendo le regole descritte sopra                                                                                                                                                                                                                                   stringa ASCII 7-bit
  Father                 Nome del gruppo di materiali a cui appartiene questo materiale. Se è definito questo materiale eredita tutte le proprietà del genitore. Per le proprietà non definite saranno utilizzate le proprietà del genitore.                                                                                ASCII string 7-bit
  Description            Un segnaposto per una descrizione più lunga del materiale                                                                                                                                                                                                                                          ASCII string 7-bit
  SpecificWeight         Il peso specifico è il peso per unità di volume del materiale in kg-peso/m³. Nel [Sistema Internazionale](http://it.wikipedia.org/wiki/Sistema_internazionale) l\'unità di misura è il newton/m³ Forse si intende Densità. Vedere: [Peso specifico](http://it.wikipedia.org/wiki/Peso_specifico)   kg-peso/m³
  Vendor                 Consente di specificare la marca o il fornitore del materiale                                                                                                                                                                                                                                      ASCII string 7-bit
  ProductURL             Un URL dove trovare ulteriori informazioni sul materiale                                                                                                                                                                                                                                           ASCII string 7-bit
  SpecificPrice          Il prezzo per unità di questo materiale. Le unità possono variare molto (USD/m³, EUR/piece, etc\...)                                                                                                                                                                                               ASCII string 7-bit

  : Proprietà generali del materiale


</div>

**Da fare:** aggiungere alcune proprietà con un sistema di ordinazione dei materiali (metalli, leghe, minerali, legno, \....)

### Meccanica

  Nome della proprietà                            Descrizione                                                                                                                                                                                                                                                                                                                                                                                           Unità/Tipo di Dati
  ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------
  Modulo di Young                                 Il Modulo di Young, noto come modulo di elasticità longitudinale, è la misura della rigidità di un materiale elastico ed è un valore usato per caratterizzare i materiali. Vedere: [Modulo di elasticità](http://it.wikipedia.org/wiki/Modulo_di_elasticit%C3%A0)                                                                                                                                     kg\*mm\^-1\*s\^-2 (kPa)
  Rapporto di Poisson                             La contrazione laterale dei materiali in tensione come frazione del loro allungamento. Vedere: [Rapporto di Poisson](https://it.wikipedia.org/wiki/Coefficiente_di_Poisson)                                                                                                                                                                                                                           Adimensionale (-)
  Tensione di snervamento                         Lo stress a cui un materiale duttile (come l\'acciaio) inizia a sviluppare una deformazione plastica (irreversibile). Vedere: [Tensione di snervamento](https://it.wikipedia.org/wiki/Tensione_di_snervamento)                                                                                                                                                                                        N\'\*mm\^-2 (MPa)
  Carico di rottura (UTS)                         Lo stress a cui il materiale si rompe. Per materiali duttili, ciò potrebbe verificarsi dopo aver subito una significativa deformazione plastica (vedere Tensione di snervamento). Per un materiale fragile, la resistenza allo snervamento e il carico di rottura coincidono. Vedere: [Carico di rottura](https://it.wikipedia.org/wiki/Carico_di_rottura)                                            N\'\*mm\^-2 (MPa)
  Incrudimento                                    Utilizzato in un oggetto materiale non lineare FEM per descrivere una curva di deformazione con sforzo unidirezionale di un materiale duttile. I valori sono immessi come tuple (tensione di snervamento, deformazione plastica), dove la prima combinazione è (Tensione di snervamento, 0) e l\'ultima (UTS, Carico di rottura) Vedere: [Incrudimento](https://it.wikipedia.org/wiki/Incrudimento)   (N\'\*mm\^-2 (MPa), adimensionale (-)
  Resistenza alla compressione uniassiale (FCK)   La resistenza alla compressione del calcestruzzo, definita come la resistenza di un cubo di dimensioni 150 mm testata a 28 giorni. Vedere [FCK](http://eurocodes.jrc.ec.europa.eu/doc/WS2008/EN1992_1_Walraven.pdf)                                                                                                                                                                                   N\'\*mm\^-2 (MPa)
  Friction Angle (PHI)                            L\'angolo di attrito interno di un materiale granulare come sabbia o cemento, come usato nel criterio di Mohr-Coulomb. Vedere [PHI](https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory)                                                                                                                                                                                                        gradi (-)
  Durezza                                         Des\...                                                                                                                                                                                                                                                                                                                                                                                               
  EN-10027-1                                      Se il materiale è un acciaio la sua [designazione](http://it.wikipedia.org/wiki/Acciaio_%28sistemi_di_designazione%29) è definita secondo lo [Standard Europeo](http://it.wikipedia.org/wiki/Comitato_europeo_di_normazione) No. 10027-1.                                                                                                                                                             string ASCII 7-bit

  : Proprietà dei materiali utilizzati in ingegneria meccanica o strutturale

**Da fare:** aggiungere ulteriori proprietà necessarie per la progettazione meccanica.

### Grafica

Questa sezione definisce le proprietà relative all\'aspetto visivo del materiale.


<div class="mw-translate-fuzzy">

  Nome della proprietà   Descrizione                                                                                               Unità/Tipo di Dati
  ---------------------- --------------------------------------------------------------------------------------------------------- ----------------------------------
  AmbientColor           Colore dell\'ambiente nel modello di colore Coin3D                                                        float,float,float range: 0.0-1.0
  DiffuseColor           Colore diffuso nel modello di colore Coin3D                                                               float,float,float range: 0.0-1.0
  SpecularColor          Colore speculare nel modello di colore Coin3D                                                             float,float,float range: 0.0-1.0
  EmissiveColor          Colore emissivo nel modello di colore Coin3D                                                              float,float,float range: 0.0-1.0
  Shininess              Colore dell\'ambiente nel modello di colore Coin3D                                                        float range: 0.0-1.0
  Transparency           Colore dell\'ambiente nel modello di colore Coin3D                                                        float range: 0.0-1.0
  VertxShader            Programma Vertex shader come definito in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)     Multi line string ASCII 7-bit
  FragmentShader         Programma Fragment shader come definito in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)   Multi line string ASCII 7-bit

  : L\'aspetto visivo


</div>

### Termico

  Nome della proprietà                 Descrizione                                                                                                                                                               Unità / Tipo di dati
  ------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------
  Conduttività termica                 La [conduttività termica](http://it.wikipedia.org/wiki/Conducibilit%C3%A0_termica) (coefficiente R o λ o k) che indica la capacità di un materiale di trasferire calore   W/m²K
  Coefficiente di espansione termica                                                                                                                                                                             
  Calore specifico                                                                                                                                                                                               

  : Proprietà termiche

### Architettura e Modello di Informazioni di un Edificio [BIM](http://it.wikipedia.org/wiki/Building_Information_Modeling) 


<div class="mw-translate-fuzzy">

  Nome della proprietà   Descrizione                                                                                                                                        Unità/Tipo di Dati
  ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  StandardFormat         Il sistema di standard utilizzato in questo materiale (ASTM, MasterFormat, CSI, OmniClass, etc\...)                                                String ASCII 7-bit
  StandardCode           Il codice specifico di questo materiale nel formato standard prima                                                                                 String ASCII 7-bit
  FireStandard           Lo standard per la valutazione della resistenza al fuoco utilizzato per il materiale                                                               String ASCII 7-bit
  FireClass              La [classe di resistenza al fuoco](http://en.wikipedia.org/wiki/Fire-resistance_rating) del materiale secondo lo standard indicato in precedenza   String ASCII 7-bit
  SoundTransmission      Il coefficiente di trasmissione del suono di questo materiale                                                                                      ?
  Finish                 Il tipo di finitura o rivestimento di questo materiale                                                                                             String ASCII 7-bit
  Color                  Il colore di questo materiale                                                                                                                      String ASCII 7-bit
  UnitsArea              Il numero di unità di questo materiale necessarie per riempire una certa area                                                                      String ASCII 7-bit

  : Proprietà dei materiali utilizzati nella progettazione architettonica

**Da fare:** aggiungere le proprietà di sostenibilità, di efficienza energetica e di impronta ecologica degli edifici [LEED](http://it.wikipedia.org/wiki/Leadership_in_Energy_and_Environmental_Design)


</div>

## TODO

-   add sustainability & LEED properties

 {{FEM Tools navi}} 

_ _ _ _ _

---
[documentation index](../README.md) > [Developer](Category_Developer.md) > Material/it
