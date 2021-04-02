Note VQR
===========

Summary
-------

In prima approssimazione, si tratta di scegliere articoli usciti su
riviste buone ma che abbiano contemporaneamente un *buon* numero di
citazioni, dove la definizione di *buon* dipende dai parametri di cui
sotto. Se il numero di citazioni ("valutazione bibliometrica") è
basso ma si vuole ugualmente inserire l'articolo, si può tentare la
sorte abilitando la "valutazione peer".


Le implicazioni del metodo sono sintetizzate
[qui](https://www.youtube.com/watch?v=_X_ymvtHaZw) (circa metà video)
e [qui](https://www.youtube.com/watch?v=t-oAAowFQuI) (minuto 15 in
poi) in dettaglio.



Liste e metriche
----------------


La selezione "ottimale" della combinazione di prodotti è non-banale. A
seconda di ogni articolo e delle citazioni ottenute occorre
ottimizzare la combinazione di aree di ricerca, indicatori migliori
tra i 4 proposti, ed aree ERC.

> Il primo passo per la valutazione di un dato l’articolo è
> l’individuazione della categoria di riferimento nota come
> SubjectCategory(SC) in WoS e AllScience Journal Classification
> (ASJC) in Scopus. La SC è in genere suggerita dalla struttura
> che ha selezionato una delle possibili opzioni in base
> all’associazione rivista-SC, ma esistono alcuni casi
> particolari: Se la rivista appartiene a più di una SC, si
> utilizza, ai fini dell’individuazione univoca della SC,
> l’indicazione della struttura che ha proposto l’articolo, o, se
> questa indicazione non è condivisa, l’eventuale modifica da
> parte del GEV. [...]


Il criterio apparentemente "esatto" è fare riferimento al sito
[ANVUR -> VQR 2011-2014 -> GEV](http://www.anvur.it/index.php?option=com_content&view=article&id=799&Itemid=597&lang=it)
-> AREA <nn>, in particolare *Metodi* e *Tabelle bibliometriche*. I
"metodi" sembrano analoghi tra i GEV.

Occorre fare attenzione a:

* Le liste non hanno logica evidente. Ad esempio: "Journal
  of Computational Physics", IF 2.43, è in categoria SCOPUS "Computer
  Science Applications", ma manca nella quasi sinonima "Applied
  Mathematics". La rivista "Computer Physics Communications", IF 3.11,
  è assente da entrambe!

  Di conseguenza, è possibile the "aree" diverse valutino in modo
  opposto lo stesso articolo.  Questa aleatorietà deriva
    1. dalle tabelle bibliometriche divise per area
    2. dalla proliferazione di indici
    3. dal potenziale "peer review".

* Le stesse liste vengono modificate periodicamente.


* Le quattro metriche (con i rispettivi venditori nelle colonne) sono:

   Keyword | SCOPUS   |  WOS cioè ISI
   -----|---------|-------------
   Popularity       | [IPP](http://www.journalmetrics.com/ipp.php): Impact per publication | 5YIF: 5-year impact factor
   Prestige         |  [SJR](http://www.journalmetrics.com/sjr.php): Scimago journal rank | AIS: article influence score



* Scelta del database di un certo venditore. Nel
  [Comunicato del GEV02 del 9 febbraio 2016](http://www.anvur.it/attachments/article/843/_Comunicato%20del%20GEV02%20del~.pdf)
  ad esempio si legge:

    > A seguito di prime analisi comparative delle soglie che emergono
    > dai due diversi database (Scopus e WoS) e dai diversi indicatori
    > (IPP e SJR per Scopus, e IF5Y e AIS per WoS ), si invitano i
    > colleghi a porre molta attenzione nella scelta del database e
    > degli indicatori. La scelta tradizionale WoS + IF5Y può non
    > risultare sempre ottimale.


Riviste multidisciplinari
------------------------

  * Nel
  [Comunicato del GEV02 del 9 febbraio 2016](http://www.anvur.it/attachments/article/843/_Comunicato%20del%20GEV02%20del~.pdf)
  si legge:

    > Ricordiamo inoltre che gli articoli pubblicati su riviste
    > multidisciplinari (es.  Phys.  Rev.  Lett., PNAS, Nature,
    > Science, ...)  vengono automaticamente assegnati alla subject
    > category più coerente con le citazioni e le referenze degli
    > articoli stessi.  Poiché essi preservano i propri parametri
    > bibliometrici, la scelta di questo genere di prodotti risulta
    > tipicamente vantaggiosa.


*  Altre "precisazioni" si trovano in
  [Precisazione sul trattamento...](http://www.anvur.org/index.php?option=com_content&view=article&id=995:precisazione-sul-trattamento-delle-riviste-multidisciplinari-come-nature,-science,-etc-nella-valutazione-bibliometrica-it&catid=78&Itemid=596&lang=it),
  [Documento di accompagnamento...](http://www.anvur.it/attachments/article/825/Documento%20di%20accompagname~.pdf)
  e ancora
  [Precisazioni sull’applicazione...](http://www.anvur.it/attachments/article/825/Precisazioni%20su%20algoritmo.pdf)



* Più utilmente nei commenti a
  [questo articolo su ROARS](http://www.roars.it/online/non-riuscite-ad-aprire-le-tabelle-vqr-di-area-09-scaricatele-da-roars/)
  si legge:

    > Essendo multidisciplinare PRL viene spacchettata. Per avere una
    > idea della classificazione, per esempio, di un articolo di
    > Meccanica Statistica pubblicato su PRL, bisogna andare sulla
    > tabella di Physics and Statistics, prendere una rivista con IPP
    > pari a quello di PRL (se sono tutte più basse, si prende la
    > prima per IPP) e confrontare le soglie citazionali di quella
    > rivista con le citazioni del lavoro in questione.



* Il significato di "Suggerisco di valutare questo prodotto tramite
  peer review" non è intuitivo. In particolare non è chiaro se vada
  marcato nel caso di riviste multidisciplinari, e che cambia se
  non lo è. 
  



Importazione
------------

Non tutti i prodotto di People sembrano elencati, a meno di non
disattivare il filtro. Potrebbe essere connesso al cambio di
istituto.

Inoltre, non è certo che l'importazione da People includa gli abstract
(conferenza) su rivista, nonostante nei
[Criteri GEV 02](http://www.anvur.it/attachments/article/843/Criteri%20GEV%2002.pdf)
si legga alla nota 4:

> La calibrazione dell’algoritmo bibliometrico è funzione della
> particolare SC nel particolare anno analizzato. L’algoritmo
> distingue inoltre la tipologia journal article
> [footnote 4: *Sono considerati in questa classe anche i conference papers pubblicati su rivista*]
> e letter da quella review, calcolando distribuzioni cumulative
> empiriche separate a causa del diverso numero di citazioni
> tipicamente ricevuto da questo tipo di pubblicazioni.





Altre fonti
-----


Tutorial Teramo:
[indicazioni_per_l_uso_di_Scopus](http://www.unite.it/UniTE/Engine/RAServeFile.php/f/vqr/tutorial_1-_indicazioni_per_l_uso_di_Scopus.pdf)
e
[indicazioni_per_la_scelta_del_prodotto](http://www.unite.it/UniTE/Engine/RAServeFile.php/f/vqr/tutorial_3_-_indicazioni_per_la_scelta_del_prodotto.pdf).

I codici SCOPUS sembrano corrispondere agli *All Science
Classification Codes (ASJC)*. 

Tabelle corrispondenza GEV-aree ASJC: [qui](http://www.unite.it/UniTE/Engine/RAServePG.php/P/314401UTE0104/M/20011UTE0104)

I dati SCOPUS si possono ottenere in maniera più strutturata nel sito
[Journal Metrics](http://www.journalmetrics.com/values.php) e
[Scimago](http://www.scimagojr.com/).

CWTS indicators: [qui](http://www.journalindicators.com/indicators).

