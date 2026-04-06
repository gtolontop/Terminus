# Sources et ce qu'elles apportent

Date de consultation principale : `2026-04-06`

## Sources locales

### Build du jeu

- fichier : `Terminus.html`
- utilite : source de verite principale du build local
- apport : noms exacts des salles, objets, textes, logique de progression, mot de passe final

### Build lent

- fichier : `Terminus_lent.html`
- utilite : variante locale du build
- apport : confirmation que le jeu local est bien complet

### PDF localises dans le depot

- fichier : `external-terminus-corrige.pdf`
- apport : tableau des commandes + plan synthetique

- fichier : `external-terminus-mcoilhac.pdf`
- apport : ordre conseille des lieux et indices de resolution

## Sources web

### Corrige Frederic Junier

- URL : <https://frederic-junier.gitlab.io/parc-nsi/chapitre9/terminus/corrige/terminus.html>
- apport : confirmation qu'il existe bien un corrige pedagogique rattache au TP

### Enonce / activite Terminus

- URL : <https://frederic-junier.gitlab.io/parc-nsi/chapitre9/terminus/terminus/>
- apport : contexte du TP et rattachement a l'activite de cours

### Page qkzk

- URL : <https://qkzk.xyz/docs/nsi/cours_premiere/os/7_terminus/>
- apport : formulation claire du travail demande, rappel de plusieurs commandes, exigence de faire un plan du jeu

### PDF Glassus

- URL : <https://glassus.github.io/premiere_nsi/T3_Architecture_materielle/3.5_Decouverte_des_commandes_Linux/data/Terminus-corrige.pdf>
- apport : liste des commandes et plan du jeu

### PDF M. Coilhac

- URL : <https://mcoilhac.forge.apps.education.fr/term/processus/a_telecharger/Terminus.pdf>
- apport : ordre de visite recommande pour ne pas se bloquer

### Jeu en ligne / demo

- URL : <https://luffah.xyz/bidules/Terminus/>
- apport : reference publique du jeu

## Source amont du code

### Depot GitHub upstream

- URL : <https://github.com/luffah/Terminus>
- apport :
  - `game/terminus/map.txt` pour la carte
  - `game/terminus/webroot/tests/autoexplore.js` pour l'arborescence
  - `game/terminus/webroot/tests/test_academy.js` pour la resolution de l'academie
  - scripts d'objets / personnages pour verifier les debloquages

## Conclusion

La solution finale du dossier repose surtout sur :

1. le build local du jeu
2. les scripts upstream
3. les deux PDF pedagogiques

Les pages web servent surtout a confirmer le contexte scolaire et la provenance du TP.
