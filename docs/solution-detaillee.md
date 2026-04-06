# Solution detaillee de Terminus

## Methode

Je n'ai pas simplement recopie un corrige trouve en ligne. J'ai croise quatre types de sources :

1. le build local fourni dans ce depot (`Terminus.html`)
2. les PDF d'aide / corrige
3. le depot source upstream de `luffah/Terminus`
4. les scripts de test et la carte `map.txt` du repo upstream

Le but etait de reconstruire une solution propre, verifiable, et expliquant pourquoi chaque commande marche.

## Conseils de jeu utiles pour le rendu

- faire `ls` a chaque nouvelle salle
- lire les personnages et objets avec `cat`
- utiliser `Tab` ou les boutons du jeu pour eviter de mal taper les accents
- les chemins relatifs (`..`, `.`, `~/`) font gagner du temps
- certaines salles caches apparaissent seulement apres une action precise

## Walkthrough complet

### Etape 1 - prise en main

Depuis `Départ`, commencer par regarder autour :

```bash
ls
cat Palourde
```

`Palourde` rappelle l'usage de `cd` et `ls`.

Ensuite aller dans `BoisDesLutins` et lire le panneau de retour :

```bash
cd BoisDesLutins
ls
cat RentreChezToi
```

Cette lecture apprend `pwd`.

### Etape 2 - academie et commande `mv`

Entrer dans l'academie, aller en cours, puis parler au professeur :

```bash
cd AcadémieDesBots
cd Cours
cat Professeur
```

On apprend `mv`.

Aller ensuite dans la salle d'entrainement :

```bash
cd ../SalleDEntrainement
ls
cat Note
```

La note dit de ne pas deplacer les piliers, donc evidemment l'enigme consiste a les deplacer.

Commande la plus efficace :

```bash
mv Pilier* ~/
```

Ce mouvement vide la salle des trois piliers et valide la zone academie.

### Etape 3 - prairie, montagne, aide et manuel

Retourner au depart puis a la prairie :

```bash
cd ~/
cd Prairie
cat Poney
```

La lecture de `Poney` debloque `Montagnes`.

Puis :

```bash
cd Montagnes
cat VieilHomme
cat Manuscrit
```

On y apprend `exit`, puis l'aide via `help` / `man`.

### Etape 4 - cave, cellier et tunnel

Entrer dans la cave puis aller jusqu'au cellier :

```bash
cd Cave
cd SombreCorridor
cd Cellier
ls
```

On y trouve le `Rocher` et le `PetitRenfoncement`.

Commande :

```bash
mv Rocher PetitRenfoncement
```

Effet : le `Tunnel` s'ouvre.

Continuer :

```bash
cd Tunnel
cd ChambreDePierre
cd Portail
cd PlaceDuVillage
```

On atteint alors le grand hub du niveau 2.

### Etape 5 - grand hub de PlaceDuVillage

L'ordre conseille par les indices et confirme par le code est :

1. `PlaceDuMarché`
2. `BoutiqueArtisanale`
3. `Bibliothèque`
4. `CheminEnPierres`
5. `PontCassé`

### Etape 6 - PlaceDuMarche : `unzip`, `mkdir`, `rm`

Aller au marche :

```bash
cd PlaceDuMarché
ls
cat SacÀDos
```

Le sac apprend `unzip` et devient un sac zippe.

Sortir son contenu :

```bash
unzip SacÀDos.zip
```

Cela fait apparaitre les deux "couts" necessaires aux achats.

Parler au vendeur une premiere fois et acheter `mkdir`, puis recommencer pour `rm`.

Le jeu propose un choix interactif, mais l'important pour le rendu est :

- premier achat utile : `mkdir`
- second achat indispensable : `rm`

### Etape 7 - Boutique artisanale : `touch` puis `cp`

Aller a la boutique :

```bash
cd ../BoutiqueArtisanale
cat Artisane
```

On apprend `touch`.

Creer le rouage demande :

```bash
touch rouage
```

Cela debloque `cp`.

Faire ensuite les cinq copies attendues :

```bash
cp rouage rouage1
cp rouage rouage2
cp rouage rouage3
cp rouage rouage4
cp rouage rouage5
```

La zone est alors validee.

### Etape 8 - Bibliotheque : levier et `grep`

Aller a la bibliotheque :

```bash
cd ../Bibliothèque
ls
```

Le levier est executable, donc on l'actionne avec `./`.

```bash
./IntrigantLevier
```

Cela fait apparaitre `PièceSecrète`.

Ensuite :

```bash
cd PièceSecrète
cat Grep
```

On apprend `grep`, commande indispensable pour la fin du jeu.

### Etape 9 - CheminEnPierres et ferme

Revenir au village puis aller au chemin en pierres :

```bash
cd ../CheminEnPierres
rm ÉnormeRocher
```

La `Ferme` s'ouvre.

Quete secondaire possible :

```bash
cd Ferme
cp EpisDeMais autreEpisDeMais
```

Cette action aide le fermier, mais elle n'est pas necessaire pour finir le jeu.

### Etape 10 - Pont casse, clairiere et maison

Aller au pont casse :

```bash
cd ../PontCassé
ls
```

Il manque une `Planche`, qu'il faut creer avec `touch` :

```bash
touch Planche
```

La `Clairière` devient franchissable.

Puis :

```bash
cd Clairière
mkdir Maison
```

La maison apparait et la zone est resolue.

### Etape 11 - Ronces et cave des trolls

Continuer vers le chemin inquietant :

```bash
cd CheminInquiétant
rm RoncesTordues
```

Les ronces disparaissent et ouvrent `CaveDesTrolls`.

Entrer :

```bash
cd CaveDesTrolls
ls
```

### Etape 12 - TrollMoche et liberation de l'enfant

Le plus simple pour ouvrir le toboggan est :

```bash
rm TrollMoche
```

Ensuite il faut liberer l'enfant de la cage, meme si on ne peut pas entrer dans la cage.

Une commande qui fonctionne depuis `CaveDesTrolls` est :

```bash
mv Cage/EnfantKidnapé .
```

Le script du jeu deplace ensuite automatiquement l'enfant vers `Clairière`.

### Etape 13 - Toboggan, FichiersNoyau, mot de passe

Aller maintenant vers la fin du jeu :

```bash
cd Toboggan
cd FichiersNoyau
ls
```

Dans cette salle il faut d'abord lire le prospectus :

```bash
cat Prospectus
```

On apprend `sudo`.

Puis lire les instructions :

```bash
cat Instructions
```

Elles disent que le mot de passe est cache dans `PlusDeFichiersNoyau`.

Aller dans cette salle :

```bash
cd PlusDeFichiersNoyau
grep pass *.txt
```

Le mot de passe trouve est :

```text
IHTFP
```

### Etape 14 - Certificat et Paradis

Revenir dans `FichiersNoyau` puis lire le certificat avec `sudo` :

```bash
cd ..
sudo cat Certificat
```

Quand le jeu demande le mot de passe, entrer :

```text
IHTFP
```

La lecture du certificat debloque `Paradis`.

Finir avec :

```bash
cd Paradis
ls
```

Le `ls` dans `Paradis` declenche la fin du jeu.

## Resume ultra compact des commandes clefs

```bash
cd BoisDesLutins
cat RentreChezToi
cd AcadémieDesBots/Cours
cat Professeur
cd ../SalleDEntrainement
mv Pilier* ~/
cd ~/Prairie
cat Poney
cd Montagnes
cat VieilHomme
cat Manuscrit
cd Cave/SombreCorridor/Cellier
mv Rocher PetitRenfoncement
cd Tunnel/ChambreDePierre/Portail/PlaceDuVillage
cd PlaceDuMarché
cat SacÀDos
unzip SacÀDos.zip
cat Vendeur
cat Vendeur
cd ../BoutiqueArtisanale
cat Artisane
touch rouage
cp rouage rouage1
cp rouage rouage2
cp rouage rouage3
cp rouage rouage4
cp rouage rouage5
cd ../Bibliothèque
./IntrigantLevier
cd PièceSecrète
cat Grep
cd ../..
cd CheminEnPierres
rm ÉnormeRocher
cd ../PontCassé
touch Planche
cd Clairière
mkdir Maison
cd CheminInquiétant
rm RoncesTordues
cd CaveDesTrolls
rm TrollMoche
mv Cage/EnfantKidnapé .
cd Toboggan
cd FichiersNoyau
cat Prospectus
cat Instructions
cd PlusDeFichiersNoyau
grep pass *.txt
cd ..
sudo cat Certificat
cd Paradis
ls
```
