# Analyse exploratoire, descriptive et inférentielle de données

## 1. Présentation des données

Les données sont fournies dans le cadre d'une compétition Kaggle :
[Kaggle compétition](https://www.kaggle.com/datasets/annavictoria/speed-dating-experiment)

Ces données ont été collectées dans le cadre d'une recherche menée par Raymond Fisman et collaborateurs[^1] et dans laquelle les participants (des étudiants de l'université de Columbia) ont pris part à des évènements de speed dating expérimentaux entre 2002 et 2004 (21 vagues dont 14 utilisées dans l'analyse). Lors de ces rencontres, les participants avaient un premier rendez-vous de 4 minutes avec d'autres participants du sexe opposé. 

La principale variable était alors la volonté du participant de revoir la personne, de donner suite à ce premier rendez-vous. Un second rendez-vous était organisé si les 2 personnes étaient intéressées. 

Un grand nombre de variables secondaires ont été collectées, telles que : 

  * Des variables socio-démographiques
  * Le habitudes en termes de dating et plus généralement sur le lifestyle
  * L'auto-perception, l'auto-évaluation sur 6 attributs : Attractivité, Sincérité, Intelligence, Caractère amusant et Ambition
  * L'évaluation du partenaire sur 6 attributs : Attractivité, Sincérité, Intelligence, Caractère amusant, Ambition et Centres d'intérêt communs. 
  * Les croyances concernant ce que les autres valorisent chez un partenaire 

Les données étaient recueillies à différents temps de l'expérience : 

  * Avant le rendez-vous
  * Directement après le premier rendez-vous
  * Le lendemain matin 
  * 3 à 4 semaines plus tard

----

## 2. Objectif

L'objectif de ce travail est de comprendre, à l'aide d'une **analyse descriptive exploratoire**, les facteurs déterminants l'occurence d'un second rendez-vous (les deux partenaires ont souhaité donner suite).  

Cet objectif est décomposé en 2 questions principales : 

* Quelles sont les caractéristiques du décideur qui peuvent le rendre plus enclin à souhaiter un deuxième rendez-vous ? Autrement dit, est ce qu'il y a des facteurs qui nous "prédisposent" plus facilement à donner suite à un premier rendez-vous, "indépendamment" des partenaires ?
  * Quelles sont les caractéristiques du partenaire qui peuvent rendre le décideur plus enclin à souhaiter un deuxième rendez-vous ? Autrement dit, est ce qu'il y a des facteurs chez la personne que l'on rencontre qui sont prépondérants dans la volonté de donner suite à un premier rendez-vous ?

En objectif secondaire, une question annexe a été ajoutée : Le nombre de matchs obtenus influence-t-il ce qu'on l'on recherche chez un partenaire ? Autrement dit, est ce qu'une personne change ses critères de recherches, évolue quant aux caractéristiques importantes pour elle, parce qu'elle a obtenu de nombreux matchs ou au contraire très peu ? 
 
----

## 3. Comment procéder ?

### Pré-requis

Les librairies suivantes sont nécessaires : 
  * warnings
  * pandas 
  * seaborn 
  * numpy 
  * matplotlib.pyplot 
  * plotly
  * bioinfokit.analys 
  * mpl_toolkits.mplot3d 

### Les fichiers

  * Le fichier de données : Speed Dating Data.csv
  * Le dictionnaire des variables : Speed Dating Data Key.doc

Pour simplifier la navigation, un notebook indépendant est proposé pour chaque question :

  * Traitement de la question 1 : Q1-Decideur.ipynb
  * Traitement de la question 2 : Q2-Partenaire.ipynb
  * Traitement de la question 3 : Q3-Evolution.ipynb

----

## 4. Overview des principaux résultats

### Influence des caractéristiques du décideur

De manière globale, très peu de variables relatives aux décideurs émergent comme prépondérantes dans leur tendance à souhaiter donner suite au premier rendez-vous. On notera entre autres :
  * Son attractivité : Moins le décideur est perçu comme attractif par les personnes rencontrées, plus il est enclin à souhaiter un deuxième rendez-vous
  * Son genre : Les hommes ont tendance à davantage souhaiter un second rendez-vous que les femmes

Ces deux variables n'apparaissent pas interagir entre elles, la tendance liée à l'attractivité est la même pour les hommes et pour les femmes. 

![image](https://user-images.githubusercontent.com/38078432/185758122-c2611c8f-32ac-4269-a445-61077afe82ac.png)

### Influence des caractéristiques du partenaire

L'évaluation du partenaire sur différentes dimensions influence positivement le fait qu'on souhaite le revoir à la suite du premier rendez-vous. 
Plus un partenaire est perçu comme attrayant, drôle, partageant des centres d'intérêts, ambiteux, sincère et intelligent, plus il est susceptible de se voir proposer un second rdv. On notera que l'attractivité est l'élément fondamental alors que la sincérité et l'intelligence sont des caractéristiques plus annexes dans le déclenchement d'une envie d'aller plus loin. 

![image](https://user-images.githubusercontent.com/38078432/185758209-a44b647d-a850-411d-a9f0-2016e2ac8745.png)

Contrairement à ce que l'on pourrait attendre, plus le partenaire recherche un décideur sincère, et plus il recherche quelqu'un qui partage avec lui des centres d'intérêt, moins il a de chances de susciter un second rendez-vous. 

### Evolution des critères de recherche en fonction des matchs obtenus

Quand les personnes ont au moins un match, elles ont davantage tendance à renforcer l'importance de l'attractivité du partenaire (deviennent plus exigeantes) là où les personnes qui n'ont pas matché ont tendance à conserver la même importance de cette caractéristique. 

![image](https://user-images.githubusercontent.com/38078432/185758286-a30ab77f-f488-42ab-96a3-a6de65146c4f.png)

----

## 5. Informations

### Outils

Les notebooks ont été développés avec [Visual Studio Code](https://code.visualstudio.com/)

### Auteurs & contributeurs

  * Helene alias [@Bebock](https://github.com/Bebock)



[^1]: Raymond Fisman, Sheena S. Iyengar, Emir Kamenica, Itamar Simonson, Gender Differences in Mate Selection: Evidence From a Speed Dating Experiment, The Quarterly Journal of Economics, Volume 121, Issue 2, May 2006, Pages 673–697, https://doi.org/10.1162/qjec.2006.121.2.673
