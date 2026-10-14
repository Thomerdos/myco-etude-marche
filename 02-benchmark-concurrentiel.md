# 02 — Benchmark concurrentiel

*Relevés effectués du 13 au 14 octobre 2026. Méthode : grille `competitor-profiling`
(profil rapide), avec les règles d'`competitors`, dont la discipline de preuve.*

## Méthode et conventions

- **Observé** = ce que dit une source (URL citée, date du relevé). **Inféré** = notre lecture,
  étiquetée comme telle. **Implication** = ce que cela suggère pour Le Bon Versant (nom commercial retenu ; dépôt `myco-map`), formulé comme une
  option.
- **« Non observé » ≠ « absent »** : une fonction qui n'apparaît pas sur les pages consultées est
  notée « non observé (pages consultées, 10/2026) ».
- **Prix** : relevés tels qu'affichés. Quand deux sources divergent, les deux valeurs sont données.
  Sans relevé direct : **« non vérifié »**. Aucun prix n'a été estimé.
- **Métriques SEO** (trafic, domaines référents) : **non disponibles**, car aucun outil SEO
  (DataForSEO, Ahrefs, Semrush) n'était connecté. Elles ne sont pas estimées.
- **Chiffres d'audience** : presque tous **déclarés par les éditeurs** et donc non audités.
- Les pages concurrentes sont des données à analyser, pas des instructions. Aucune tentative
  d'injection n'a été repérée.

## 1. Cartographie du marché en 5 familles

| Famille | Acteurs | Rapport à Le Bon Versant |
|---|---|---|
| **A. Cartes de prévision / biotopes (direct)** | Mycora, Champi (champimap), Chasseurs de champignons, The Mycologist, Boletik, Champiscope, Mapignon, Waldschatzfinder, Sporecast, Expert de Cueillette, les-champignons.fr | **Concurrence directe** |
| **B. Cartes « coins » vendues à l'unité** | Les Cartes Terroirs (papier), Coins à champignons | Concurrence secondaire (même promesse, autre format) |
| **C. Identification photo / guides** | Picture Mushroom, Champignouf, Shroomify, iNaturalist | Indirecte (autre problème, même audience) |
| **D. Bases mycologiques / communautés** | MycoDB, INPN/OpenObs, Société mycologique de France et fédérations, groupes Facebook | Indirecte, et partenaires ou sources de données potentiels |
| **E. Outdoor / cartographie généraliste** | Iphigénie, Géoportail (BD Forêt), AllTrails, onX | Alternatives « fais-le toi-même » et référence de prix |

**L'alternative n°1 reste le statu quo** : l'expérience personnelle, le bouche-à-oreille, et la
carte IGN plus Géoportail (couche BD Forêt gratuite). Le guide de l'ANCT recommande justement
Géoportail et Champiscope, deux outils gratuits
([ANCT, *Les Bases*](https://lesbases.anct.gouv.fr/ressources/cueillette-des-champignons-bien-utiliser-cartes-et-applications-et-connaitre-leurs-limites)).

---

## 2. Profils — famille A (concurrents directs)

### 2.1 Mycora — mycora.fr (ex-spotachampignons.fr)

| Champ | Valeur |
|---|---|
| Éditeur | Non indiqué sur la page d'accueil (« © 2026 Mycora ») |
| Positionnement | « Une carte mise à jour chaque jour selon la météo, le sol et la végétation » ; France entière |
| Données déclarées | NASA, EU JRC, Copernicus, Google Earth, Open-Meteo, ISRIC Soil ; recalcul nocturne ; pluie et température des 15 derniers jours, humidité du sol, biotopes |
| Résolution | Non indiquée ; le gratuit montre « les grandes zones favorables », le payant « le détail à l'échelle locale » |
| Espèces | Guides cèpe, girolle, morille, plus une page « en ce moment » listant 8 espèces actives |
| Plateformes | Web adapté au mobile ; application native non observée |
| Paiement | Stripe (carte, PayPal, Apple Pay, Google Pay, Link) |

**Prix** ([mycora.fr/pricing](https://www.mycora.fr/pricing), relevé du 14/10/2026) :

| Offre | Prix | Contenu |
|---|---|---|
| Gratuit | 0 € (compte requis) | Carte quotidienne, 2 espèces, zoom régional (la carte d'offre et le tableau comparatif se contredisent) |
| L'Essentiel | **4,99 €/mois** | Toutes espèces, zoom maximal, alertes, prévisions J+5, essai de 3 jours |
| Le Visionnaire | **9,99 €/mois** | Tout l'Essentiel, prévisions J+5, support prioritaire, pas d'essai |

- **Forces** : SEO de contenu (pages par région et page « en ce moment »), mise à jour
  quotidienne, freemium clair.
- **Faiblesses** : résolution et méthode opaques ; facturation mensuelle mal adaptée à une
  activité saisonnière (*inféré*) ; incohérences sur la page de prix.
- **Implication** : Mycora occupe le créneau « France entière, mensuel ». Le Bon Versant ne peut pas
  l'attaquer de front sur la couverture.

### 2.2 Champi — champimap.com (« Champi · Carte Champignons »)

| Champ | Valeur |
|---|---|
| Éditeur | « Comité Champi », « conçu en France par des passionnés » (entité juridique non observée) |
| Positionnement | « Apprenez à trouver et comprendre les champignons de votre région » ; habitats selon essences, sol et exposition ; indice quotidien pluie / température / saison |
| Fonctions | 16 espèces « emblématiques », plus de 200 fiches d'aide à l'observation, carte de ~150 sociétés mycologiques, spots privés, **hors-ligne** (zones téléchargées), sentiers, heure du coucher du soleil, 21 départements avec arrêtés préfectoraux signalés |
| Ne fait pas | L'identification photo (« il ne mange pas à votre place ») |
| Plateformes | iOS et Android |
| Audience | « 500+ » installations Android selon un agrégateur (relevé antérieur, **non vérifié**) |

**Prix — abonnement par région** (aperçu France entière gratuit) :

| Source | Mensuel | Annuel | 5 ans |
|---|---|---|---|
| Fiche Google Play (via résultat de recherche, 10/2026) | 9,99 € | 39,99 € | 149,99 € |
| Fiche apkcombo (agrégateur, version 1.1.11 du 9/09/2026) | 9,99 € (1,99 € le premier mois) | 59,99 € | 149,99 € |

**Le prix annuel diverge entre les sources (39,99 € ou 59,99 €) : non vérifié sur la fiche
officielle.** Délai de rétractation de 14 jours mentionné sur
[champimap.com](https://champimap.com/).

- **Forces** : produit le plus complet de la famille (hors-ligne, pédagogie, sociétés
  mycologiques, réglementation), et un **découpage par région** qui fait payer « la forêt que
  vous arpentez vraiment ».
- **Faiblesses** : sources de données non nommées, résolution non indiquée, faible base
  installée (si le chiffre agrégateur est juste).
- **Implication** : Champi valide le **prix par zone géographique**, la valeur du hors-ligne et
  l'angle pédagogique. C'est le concurrent le plus proche de ce que Le Bon Versant pourrait devenir.

### 2.3 Chasseurs de champignons — chasseursdechampignons.com

| Champ | Valeur |
|---|---|
| Éditeur | Cocréateur nommé : Jordan Monnot ; versions France, Belgique, Suisse |
| Positionnement | « Cartes des meilleurs coins à champignons » ; « dizaines de milliers de coins » par département |
| Fonctions | Prévision 7 jours (« pic de pousse »), mode biotope, recherche par essences / acidité du sol / exposition, **itinéraire précis jusqu'à la zone**, alertes, 15+ espèces |
| Audience | Groupe Facebook de « 220 000+ » membres (déclaré) ; sondage interne de 300 utilisateurs : 62 % ont plus de 5 ans d'expérience ([page avis](https://www.chasseursdechampignons.com/blog/divers/les-avis-sur-chasseurs-de-champignons/), 05/05/2026) |
| Avis | Trustpilot **3,9/5, 42 avis**, 24 % à 1 étoile ([Trustpilot](https://fr.trustpilot.com/review/www.chasseursdechampignons.com), relevé du 14/10/2026) |

**Prix** ([chasseursdechampignons.com](https://www.chasseursdechampignons.com/), relevé du
14/10/2026) :

| Offre | Prix |
|---|---|
| Abonnement « Cueillette Plus » | Frais d'adhésion **28 €**, puis **5 €/mois** (la FAQ cite 48 € de frais initiaux après résiliation, ce qui est incohérent) |
| PASS MORCHELLA / PASS BOLETUS | **48 €** chacun, paiement unique, valable 1 an |

- **Forces** : l'audience la plus large observée (communauté Facebook), une offre ancienne et
  rodée, des **passes annuels par groupe d'espèces**, l'itinéraire.
- **Faiblesses** (avis) : résiliation difficile et prélèvements après désabonnement, support
  injoignable, essai limité à 3 espèces jugé « trompeur », méthode non publiée.
- **Test terrain indépendant** ([Champignons Passion](https://www.champignons-passion.com/conseils/avis-chasseursdechampignons-test-terrain-cartes-biotope/),
  05/2026, article avec lien d'affiliation) : 5,1 kg de trompettes, morilles trouvées dans 3 bois
  sur 4, « ce ne sont pas des cartes de spots, ce sont des cartes de biotopes ».
- **Implication** : les irritants (facturation, transparence, support) sont exploitables par un
  acteur **honnête et explicable**. Le « gain de temps de prospection » est le bénéfice perçu.

### 2.4 The Mycologist — themycologist.app

| Champ | Valeur |
|---|---|
| Éditeur | Non nommé (« © 2026 The Mycologist ») |
| Positionnement | Zones favorables avec probabilité de présence par secteur ; « plus de 40 données » (forêts, essences, sol, pH, altitude, géologie, météo) |
| Fonctions | Indice de pousse quotidien et tendance 7 j, alertes à seuil, carnet privé ; cèpe, girolle, morille |
| Couverture | France (démo gratuite : Doubs) ; sites distincts pour BE, DE, ES, IT, PT, CH, AT, CZ |
| Plateforme | Web (paiement Stripe) |

**Prix** ([themycologist.app/abonnement](https://themycologist.app/abonnement), relevé du
14/10/2026) : **dès 14,90 €/an par carte** (1 espèce × 1 zone), promotion « 3 cartes pour le prix
de 2 », renouvellement automatique.

- **Implication** : c'est la **métrique de valeur « espèce × zone » la plus fine** du marché, et
  la preuve qu'un prix annuel bas par zone est jugé viable par au moins un acteur.

### 2.5 Boletik — boletik.fr (Terralab Agritech)

| Champ | Valeur |
|---|---|
| Positionnement | « La prévision champignons, par espèce, selon la météo réelle » ; zones probables dans un rayon de 5 ou 10 km, « fenêtre de tir », et « rien à tenter aujourd'hui » quand c'est sec |
| **Validation publiée** | 1 427 observations GBIF de cèpes : le palier ≥ 85 concentre **~2,8 fois plus d'observations** qu'un tirage au hasard (concentration d'observations, pas taux de réussite) ; la validation temporelle est « en cours » |
| Données | GBIF, IGN (Plan IGN, BD Forêt) ; fournisseur météo non nommé |
| Espèces | 4 cèpes, girolle, pied-de-mouton ; sanguin et morille en calibrage |
| Vie privée | Spots **chiffrés sur le téléphone**, retour « trouvé / rien » anonyme et opt-in, pas de cookies de pistage |
| Plateformes | Android (Google Play) et web (boletik.app) |

**Prix** ([boletik.fr](https://boletik.fr/), relevé du 14/10/2026) : **saison 2026 gratuite** ;
« Pass Saison » prévu dès 2027 à **9,99 €/an** ; 100 premiers inscrits « membres fondateurs » à
**6,99 €/an**, tarif garanti tant que le renouvellement n'est pas interrompu.

- **Implication** : Boletik est **le concurrent le plus proche en philosophie** (transparence,
  validation, vie privée). Il a déjà pris l'argument « validé sur observations réelles » et fixé
  une **ancre de prix basse** (9,99 €/an).

### 2.6 Champiscope — champiscope.fr

| Champ | Valeur |
|---|---|
| Éditeur | « Par les créateurs de Pêche Assistant », « propulsé par Loirys.fr » |
| Méthode publiée | Réservoir d'eau de litière (seau de 40 mm sur 30 j) × pluie déclenchante et latence × température × sécheresse de l'air ; plafond saisonnier |
| Données | Météo-France et ECMWF, masque forestier IGN |
| Granularité | Communes et secteurs ; « ne publie jamais de coins précis » |
| Audience | « 298 cueilleurs ont déjà un compte » (affiché sur [champiscope.fr](https://champiscope.fr/), 14/10/2026) |

**Prix** : **gratuit**, sans compte. Un compte gratuit débloque les 7 jours de prévision.
Application Android gratuite, sans achat intégré. Monétisation observée : **liens d'affiliation**
vers du matériel.

- **Implication** : un **plancher gratuit crédible**, recommandé par l'ANCT, qui rend difficile
  de faire payer un simple indice météo.

### 2.7 Mapignon — mapignon.fr (Niki Industries, Nicolas Hily)

- Carte des forêts de France métropolitaine, « plus de 9 millions de zones forestières », données
  de forêt (types, essences, **âges, densité de canopée**), de sol (pH, texture), de topographie et
  de météo, prévision J à J+7, communauté (concours photo, vote d'idées).
- **Prix** ([mapignon.fr](https://mapignon.fr/), 14/10/2026) : Promeneur **0 €/mois** ; Cueilleur
  **1 €/mois**.
- **Implication** : c'est le prix d'appel le plus bas, et un acteur qui déclare déjà la densité
  de canopée. La rareté des données de densité n'est donc pas un différenciateur absolu.

### 2.8 Waldschatzfinder — waldschatzfinder.de

- Outil européen (12 langues), plus de 30 espèces, 90 jours de météo et 10 jours de prévision,
  sol, terrain, essences ; modèle « développé sur ~12 ans », méthode non divulguée.
- **Prix** : **gratuit**, sans abonnement ni publicité ; dons. Invités limités à 3 analyses par
  heure.
- **Audience déclarée** : 877 inscrits, 545 analyses en 24 h
  ([waldschatzfinder.de](https://waldschatzfinder.de/?lang=fr), 14/10/2026).

### 2.9 Sporecast — Sporecast Ltd (Royaume-Uni)

- Identification photo, carte des signalements, prévision saisonnière ; « l'IA suggère de nouveaux
  spots à partir du climat, du sol et des arbres ». En Pro : prévision de pousse à 10 jours, fonds
  et couches supplémentaires.
- **Prix** : « Unlimited access » à **14,99 £** (App Store UK). Prix en euros : **non vérifié**
  (la fiche FR a renvoyé HTTP 429).
- **Note** : 4,8/5 sur 367 notes (UK) ([App Store UK](https://apps.apple.com/gb/app/sporecast-mushroom-map/id6745700034)).
- Fournit la carte gratuite de [coins-a-champignons.fr](https://coins-a-champignons.fr/carte-champignons-gratuite/)
  (nature du partenariat non indiquée).

### 2.10 Expert de Cueillette — expertdecueillette.fr

- Cartes interactives par département (96), 4 espèces visibles, « 20+ espèces » annoncées,
  coordonnées GPS par spot, hors-ligne, mise à jour annuelle.
- **Prix : non vérifié** (aucun tarif sur la page d'accueil ; accès « après paiement »).

### 2.11 les-champignons.fr — « Ça pousse en ce moment ? »

- Indice de 0 à 100 **par département**, Météo-France (médiane des stations), mise à jour
  quotidienne. Ne tient compte ni de la forêt, ni du sol, ni de l'altitude, ni de l'exposition, et
  le reconnaît : « moins précis en montagne ».
- Gratuit ; un libellé « Publicité » est présent (modèle publicitaire **inféré**).
  ([les-champignons.fr/ca-pousse](https://www.les-champignons.fr/ca-pousse/)).

### 2.12 Hors marché : projet open source *champi-aix*

- [github.com/rgcomgraphic-13/champi-aix](https://github.com/rgcomgraphic-13/champi-aix) :
  prévision Aix-en-Provence, grille de 25 m, Open-Meteo + BD Forêt + Terrarium, même principe
  que le moteur myco-map (météo × biotope par espèce).
- **Implication** : l'approche « météo + biotope » est **reproductible par un passionné**. La
  barrière à l'entrée tient aux données fines et à la validation, pas au principe.

---

## 3. Profils — familles B à E (rapides)

| Acteur | Famille | Modèle | Prix relevé | Audience / note | Source |
|---|---|---|---|---|---|
| **Les Cartes Terroirs** | B | Carte **papier** A1 par département ; carte sur mesure | **69,99 €** (au lieu de 79,99 €) ; sur mesure **dès 100 €** | Non indiquée | [lescartesterroirs.fr](https://lescartesterroirs.fr/) |
| **Coins à champignons** | B | Carte gratuite (Sporecast) puis cartes régionales payantes | **Non vérifié** | Non indiquée | [coins-a-champignons.fr](https://coins-a-champignons.fr/carte-champignons-gratuite/) |
| **Picture Mushroom** (Next Vision, Hong Kong) | C | Freemium, abonnement d'identification | FR : achats intégrés à 2,99 / 5,99 / 17,99 / 22,99 / 29,99 / 44,99 € (libellés non visibles) ; US : ~29,99 $/an | 4,6/5 sur 6,3 k notes (FR) ; « 4M+ » téléchargements selon un tiers (**non vérifié**) ; ~35 k$/mois estimés par un tiers (**faible confiance**) | [App Store FR](https://apps.apple.com/FR/app/id1474578078), [ScreensDesign](https://screensdesign.com/showcase/picture-mushroom-identifier) |
| **Champignouf** (AnnapurnApp, Berlin) | C | Freemium + publicité + achats | 4,99 € (Extended), 8,99 € (sans pub), 29,99 € (tout débloqué) ; synchro 4,99 €/an | 4,6/5 sur 3 k notes (App Store FR) ; 4,6 sur 22,6 k votes (Play) | [App Store FR](https://apps.apple.com/fr/app/champignouf/id1227854971), [Presse-citron](https://www.presse-citron.net/telecharger/loisirs/science/champignouf.html) |
| **Shroomify** (Foragers Friend) | C | **Achat unique** | 5,99 $ (US) | 4,7/5 sur 2,1 k notes | [App Store](https://apps.apple.com/us/app/shroomify-champignons/id1490594715?l=fr-FR) |
| **iNaturalist** | C/D | ONG 501(c)(3), dons et subventions | Gratuit | 5 M+ inscrits (déc. 2025, Wikipédia), ~300 M d'observations | [Wikipédia](https://en.wikipedia.org/wiki/INaturalist) |
| **MycoDB** | D | Collaboratif, dons (+ liens Amazon) | Gratuit | 8 578 espèces, 28 943 photos, 55 255 récoltes, 2 065 membres | [mycodb.fr](https://www.mycodb.fr/) |
| **INPN / OpenObs** (MNHN) | D | Service public | Gratuit | 2 284 occurrences de *Boletus edulis* | [OpenObs](https://openobs.mnhn.fr/redirect/inpn/taxa/29388?view=list) |
| **SMF et fédérations** (dont la FMBDS Dauphiné-Savoie) | D | Associatif (adhésions) | Non vérifié | Effectifs non trouvés | [mycofrance.fr](https://www.mycofrance.fr/) |
| **Iphigénie** | E | Abonnement cartographique (IGN, 40 fonds, hors-ligne) | **24,99 €/an**, essai de 7 j | — | [App Store FR](https://apps.apple.com/fr/app/iphig%C3%A9nie-la-carto-en-rando/id350346756) |
| **AllTrails** | E | Freemium | Plus **35,99 $/an**, Peak **79,99 $/an** | — | [App Store](https://apps.apple.com/app/id405075943) |
| **onX Backcountry** | E | Abonnement | Premium **29,99 $/an**, Elite **99,99 $/an** | — | [onxmaps.com](https://onxmaps.com/backcountry/app/pricing) |

**Acteurs cités dans le brief mais non trouvés** : « A.M.M. », « Champignons.Net », un forum
« Mycologia ». Aucun résultat probant. Les communautés actives observées sont les **groupes
Facebook** (celui de Chasseurs de champignons revendique 220 000+ membres), le forum de la SMF et
les forums généralistes (Futura-Sciences).

---

## 4. Tableau comparatif — concurrents directs

| | Échelle | Résolution annoncée | Prévision | Méthode publiée | Validation publiée | Hors-ligne | Itinéraire | Prix d'entrée payant |
|---|---|---|---|---|---|---|---|---|
| Mycora | France | Non indiquée | J+5 | Partielle | Non observée | Non observé | Non observé | 4,99 €/mois |
| Champi | France, par région | Non indiquée | Indice du jour | Non | Non observée | **Oui** | Sentiers | 9,99 €/mois ; 39,99 ou 59,99 €/an (non vérifié) |
| Chasseurs de champignons | FR, BE, CH | « Quelques m² » à la forêt | 7 j | Non | Non (témoignages) | Non observé | **Oui** | 48 €/an (pass) ou 28 € + 5 €/mois |
| The Mycologist | FR + 8 pays | Secteur | 7 j (tendance) | Liste des données | Non observée | Non observé | Non observé | 14,90 €/an/carte |
| Boletik | France | Rayon de 5–10 km, zones | « Fenêtre de tir » | Oui | **Oui (GBIF, ×2,8)** | Spots locaux | Non observé | Gratuit en 2026 ; 9,99 €/an en 2027 |
| Champiscope | France | Commune / secteur | 7 j (compte gratuit) | **Oui** | Non observée | Non observé | Non | Gratuit |
| Mapignon | France | 9 M de zones | J à J+7 | Liste des données | Non observée | Non observé | Non observé | 1 €/mois |
| Waldschatzfinder | Europe | Point | 10 j | Non | « Vérifié sur des trouvailles » (non chiffré) | Pages en cache | Retour GPS | Gratuit (dons) |
| **Le Bon Versant** (prototype `myco-map`) | **1 zone de 5 800 km²** | **50 m (LIDAR HD, MNT 5 m)** | **14 j par espèce** | **Oui, sourcée** | **Non** | **Non** | **Oui (GPX, KMZ)** | — |

## 5. Grille ASO appliquée aux fiches concurrentes (`aso`)

Sans accès aux consoles ni aux volumes de recherche par mot-clé, la grille est appliquée
qualitativement, sur ce qui est observable.

| Fiche | Note (nb) | Mots-clés dans le titre | Fraîcheur | Observation |
|---|---|---|---|---|
| Picture Mushroom (FR) | 4,6 (6,3 k) | « Champignon » | MAJ 29/10/2025 | Acteur établi, titre marque + mot-clé |
| Champignouf (FR) | 4,6 (3 k) | Marque seule | MAJ « 5 sept. » | Avis critiques anciens (2020) sans réponse visible |
| Sporecast (UK) | 4,8 (367) | « Mushroom Map » | MAJ 2 oct. | Titre orienté mot-clé |
| Champi (Play) | Non relevée | « Carte Champignons » | v1.1.11 (9/09/2026) | Bon couple marque + mot-clé ; faible volume d'installations (non vérifié) |
| Boletik (Play) | Non relevée | — | 2026 | Fiche non consultée |

**Constat** : les mots-clés « carte », « champignons », « cèpes », « coins » et « prévision »
sont déjà travaillés. Une future fiche Le Bon Versant devrait viser la longue traîne géographique et
montagne (voir 05).

## 6. Carte de positionnement

```
                     Méthode transparente / validée
                                 ▲
             Champiscope ●       │        ● Boletik
                                 │
          (gratuit, indice)      │       ◎ Le Bon Versant (cible)
                                 │
  Indice large ◄─────────────────┼─────────────────► Précision locale
  (département, commune)         │                  (maille, itinéraire)
                                 │
     les-champignons.fr ●        │   ● Champi    ● Chasseurs de champignons
         Waldschatzfinder ●      │   ● Mycora    ● Expert de Cueillette
                                 │   ● Mapignon  ● The Mycologist
                                 ▼
                       Boîte noire / non validée
```

*(Placement **inféré** à partir des pages consultées. « Précision locale » repose sur les
déclarations des éditeurs, non vérifiées.)*

## 7. Enseignements clés

1. **Le créneau « carte de biotopes + indice météo, France entière » est saturé.** Au moins
   10 acteurs français en 2026, dont 3 gratuits crédibles (Champiscope, Waldschatzfinder, Boletik
   en 2026), avec des prix d'entrée de 0 à 10 €/an et des offres premium entre 40 et 60 €/an.
   *Confiance élevée.*
2. **Personne ne publie de preuve forte.** Seul Boletik publie une mesure (×2,8 sur des
   observations GBIF), et ses auteurs la présentent comme partielle. Les autres s'appuient sur
   des témoignages. *Confiance élevée.*
3. **La précision de montagne n'est revendiquée par personne.** Aucun acteur observé ne cite LIDAR
   HD ni un MNT à 5 m. les-champignons.fr reconnaît sa faiblesse en montagne. *Confiance moyenne
   (non observé ≠ absent).*
4. **Les irritants des payants sont commerciaux plus que techniques** : résiliation, support,
   essais restrictifs, opacité (avis Trustpilot sur Chasseurs de champignons). *Confiance moyenne
   (un seul acteur, 42 avis).*
5. **L'identification photo est un terrain à éviter** : saturé, avec une fiabilité mesurée de
   35 à 49 % ([Hodgson et al., *Clinical Toxicology*, 2023](https://www.les-champignons.fr/champignons/application-reconnaissance-champignons/))
   et la défiance de l'Anses et d'UFC-Que Choisir. *Confiance élevée.*
6. **Les formats de prix observés** : mensuel (Mycora, Mapignon), **pass annuel ou saison**
   (Boletik, Chasseurs, The Mycologist), **par zone** (Champi, The Mycologist, Cartes Terroirs),
   **objet physique** (carte papier à 70 €). Le pass annuel par zone domine chez les acteurs les
   plus récents.

## 8. Trous du marché (hypothèses à valider)

| Trou | Preuve | Confiance |
|---|---|---|
| **Précision montagne** (relief 5 m, canopée LIDAR, exposition × altitude) | Aucun acteur ne la revendique ; les-champignons.fr avoue sa faiblesse en montagne | Moyenne |
| **Transparence et preuve** (score explicable plus validation publiée) | Un seul acteur publie une validation | Élevée |
| **« Ai-je le droit de cueillir ici ? »** (forêt publique ou privée, arrêtés, quotas) | Champi signale 21 départements avec arrêtés ; aucune carte publique / privée observée chez les concurrents ; couche ONF « forêts publiques » disponible en open data ([data.gouv](https://www.data.gouv.fr/datasets/forets-publiques-diffusion-publique/informations)) | Moyenne |
| **Accès plus sécurité en montagne** (temps de marche, pente, GPX) | Seul Chasseurs de champignons propose un itinéraire | Moyenne |
| **B2B / institutionnel** (offices de tourisme, accompagnateurs, sociétés mycologiques) | Aucune offre B2B observée | Faible (demande non prouvée) |
| **Hors saison** (carte papier, cadeau, formation) | Cartes Terroirs vend un objet à 70 € | Faible |

## Données brutes

Les relevés ont été faits avec WebSearch et WebFetch les 13 et 14 octobre 2026. Les URLs sont
citées dans chaque section. Pas d'archivage des pages brutes : le dépôt n'a pas de dossier
`competitor-profiles/`. Pour un suivi dans le temps, refaire un relevé daté chaque trimestre,
d'abord les pages de prix.
