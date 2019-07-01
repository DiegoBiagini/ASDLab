# ASDLab
All the necessary files for the course "Laboratorio di Algoritmi e Strutture Dati" will be put here.  
The three exercises I decided to develop are the following.

N1
=====

**Valutazione performance Python**   

Questo deve essere consegnato per l’esame e deve essere discusso con il docente (al ricevimento) secondo le tempistiche indicate sul sito di e-learning.  

Scrivere uno o più programmi Python che permettono di: 
  
  * Generare un vettore casuale e/o con caratteristiche opportune
  * Implementare l’algoritmo Insertion_sort() 
  * Implementare a scelta Quick_sort() o Merge_sort() 

Scrivere un programma che esegua dei test misurando i tempi di esecuzione degli algoritmi precedenti su:  
  
  * Dati di dimensione crescente (array con 10,1000,1000,... dati) 
  * Arrestandosi quando il tempo di esecuzione è maggiore di alcuni minuti 
  * Usando dati causali e dati che costituiscano il caso migliore/peggiore per un algoritmo 

Scrivere una relazione in cui si descrivono gli esperimenti svolti (riportando i risultati sperimentali ottenuti) e si analizzano i risultati alla luce della teoria.  


N2
==

**Edit distance**

Vogliamo studiare l’algoritmo di Edit Distance e come si possa utilizzare per trovare parole vicine ad una query Q in un lessico L E’ possibile scaricare lessici di parole dal Web (esempio: https://github.com/napolux/paroleitaliane).   

Per fare questo dovremo scrivere programmi Python che:
 * Implementano l’edit distance
 * Costruiscono indici di n-gram di parole (si può scegliere il modo in cui si costruiscono gli indici)
 * Data una query Q trovano la parola più vicina
 * Eseguono un insieme di test che ci permettano di comprendere vantaggi e svantaggi dell’utilizzo di indici di n-gram per eseguire le query 
 
 Scrivere una relazione che descriva quanto fatto.  
 
 N3
 ==
 
 **Componenti connesse e MST**

Per studiare gli algoritmi per trovare le componenti connesse si scrivano i seguenti programmi: 
 * Generazione di graﬁ casuali con un numero di nodi a scelta ed una determinata probabilità di presenza di archi tra vertici (es. partire da una matrice di adiacenza con tutti 0 e poi cambiare archi ad 1 con una certa probabilità )
 * Generazione di graﬁ pesati casuali
 * Ricerca delle componenti connesse 
 * Algoritmo di Kruscal 
  * Struttura dati UNION-FIND
 * In altrenativa algoritmo di Prim 
  * Struttura dati coda con priorità (con min-hash) 
 * Un programma che permetta di condurre esperimenti su graﬁ casuali con dimensione crescente e con probabilità di presenza di archi crescente. 

Scrivere inoltre una relazione che descriva quanto fatto

