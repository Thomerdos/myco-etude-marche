# 03 — Étude de marché

*14 octobre 2026. Méthodes appliquées : `customer-research` (segmentation, voix des clients,
niveaux de confiance), `pricing` (métrique de valeur, paysage de prix) et `marketing-plan`
(référentiel *market-sizing* : fourchettes, au moins deux méthodes, grille d'attractivité).
Cadrage retenu (réponses du porteur, 14/10/2026) : **revenu d'appoint**, **payant d'abord**,
**B2C** orienté cueillette dans les zones riches en champignons, **accessible aux novices**.*

> **Règle de lecture.** Chaque estimation porte un niveau de confiance : **Élevée** (au moins
> deux sources indépendantes concordent), **Moyenne** (sources crédibles mais incomplètes),
> **Faible** (inférence peu étayée), **Inconnue** (donnée absente → tâche de validation). Aucune
> donnée de première main (entretiens, sondage, conversion) n'existe encore. Tout ce qui suit
> repose sur des sources publiques et des hypothèses étiquetées.

---

## 1. Définition du marché

**Marché visé** : accès numérique payant (abonnement, pass saison ou achat unique) à des cartes
de **prospection de champignons comestibles** (où et quand chercher), pour des **particuliers en
France métropolitaine**, en commençant par des massifs à forte densité fongique. Prix de
référence observé : 0 à 60 €/an (doc 02).

**Hors périmètre** : identification photo (doc 02 §7), culture de champignons, vente de
champignons, cueillette commerciale (anti-persona, §3), marchés hors de France.

## 2. Contexte de la demande

| Fait | Valeur | Source | Confiance |
|---|---|---|---|
| Récolte de champignons sauvages en France | ~5 000 t en bonne année, dont environ la moitié autoconsommée (attribué à l'ONF) | [Wikipédia, *Cueillette de champignons*](https://fr.wikipedia.org/wiki/Cueillette_de_champignons) ; chiffre ONF original non retrouvé | Faible |
| Nombre de cueilleurs en France | « plus de 3 millions » | Guide en ligne sans étude citée ([lemontagnard-outdoor.fr](https://www.lemontagnard-outdoor.fr/actualites/divers/guide-complet-du-debutant-initiation-a-la-cueillette-des-champignons-en-france)) | **Non vérifié** |
| Taux de pratique ailleurs en Europe | Finlande ~38 % des 15–74 ans ; Pologne ~¼ de la population ; 26 % des ménages européens récoltent des produits forestiers non ligneux (champignons et autres), en hausse d'ouest en est ; Danemark ~3 % | [ResearchGate (Finlande)](https://www.researchgate.net/publication/228427142_Participation_in_mushroom_picking_in_Finland), [Frontiers 2024](https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2024.1474624/full) | Moyenne (définitions hétérogènes, données anciennes) |
| Intoxications | 1 363 cas symptomatiques du 1/07 au 31/12/2024, 3,1 % graves, 3 décès ; ~500 cas du 1/07 au 25/09/2025. Confusion la plus fréquente en 2024 : **clitocybe de l'olivier pris pour une girolle ou une chanterelle** | [Anses](https://www.anses.fr/fr/content/cueillette-des-champignons-vigilance-face-aux-risques-dintoxications) | Élevée |
| Fiabilité de l'identification par appli | 35 à 49 % d'identifications correctes ; amanite phalloïde reconnue dans 27 à 67 % des cas | Hodgson et al., *Clinical Toxicology* 2023, résumé par [les-champignons.fr](https://www.les-champignons.fr/champignons/application-reconnaissance-champignons/) | Élevée |
| Profil des utilisateurs de cartes payantes | Sondage de 300 clients de Chasseurs de champignons : 62 % ont plus de 5 ans d'expérience, 18 % moins de 2 ans | [Page de l'éditeur](https://www.chasseursdechampignons.com/blog/divers/les-avis-sur-chasseurs-de-champignons/) (auto-déclaré) | Faible |
| Saisonnalité | Morilles en avril–mai ; cèpes de juin à octobre, girolles de juin à novembre (ordre de grandeur) | Sources générales | Moyenne |

**Lecture.** La demande existe et elle est visible (au moins 10 offres en 2026, une communauté
Facebook revendiquée à 220 000+ membres). Mais **aucune statistique fiable du nombre de
cueilleurs en France n'a été trouvée**. C'est l'inconnue n°1 du dimensionnement.

## 3. Où sont les zones riches ? (cible géographique, version factuelle)

**Aucun classement publié des « régions fongiques » n'a été trouvé.** Les « meilleurs coins »
cités par la presse (Périgord, Vallespir, Fontainebleau…) relèvent de l'avis d'expert ou de
l'accessibilité. Nous avons donc mesuré un indicateur reproductible : les **occurrences géolocalisées
GBIF** des 5 taxons ciblés en France, interrogées sur l'API GBIF le 14/10/2026
(`api.gbif.org/v1/occurrence/search`, `country=FR`, `hasCoordinate=true`, facettes GADM).

| Taxon (clé GBIF) | Total FR | Départements en tête |
|---|---|---|
| Cèpe *B. edulis* (5954958) | 2 760 | Hautes-Pyrénées 230, **Isère 186**, Nord 152, Haute-Savoie 114, Savoie 113 |
| Girolle *C. cibarius* (5249504) | 2 154 | Jura 194, **Isère 170**, Pas-de-Calais 159, Hautes-Pyrénées 134, Haut-Rhin 103 |
| Trompette *C. cornucopioides* (2554662) | 1 462 | Jura 229, Doubs 115, **Isère 93**, Hautes-Pyrénées 70, Haute-Savoie 57 |
| Morilles *Morchella* (genre, 2594601) | 981 | Hautes-Pyrénées 172, **Isère 78**, Haute-Savoie 52, Ariège 50, Oise 50 |
| Pied-de-mouton *H. repandum* (2554716) | 2 568 | Jura 353, Doubs 215, Hautes-Pyrénées 202, Pas-de-Calais 190, **Isère 134** |

**Cumul des 5 taxons, par département** : Jura 844 · Hautes-Pyrénées 808 · **Isère 661** ·
Pas-de-Calais 533 · Doubs 466 · Haute-Savoie 374 · Savoie 371 · Nord 340 · Haute-Garonne 298 ·
Haut-Rhin 258 · Aveyron 237.
**Par région** : Occitanie 2 122 · Bourgogne-Franche-Comté 1 818 · **Auvergne-Rhône-Alpes
1 755** · Hauts-de-France 1 261 · Grand Est 701.

**Limites (importantes)** : GBIF mesure l'**effort d'observation**, pas la productivité. Le Nord
et le Pas-de-Calais doivent leur rang à des réseaux naturalistes actifs ; la Nouvelle-Aquitaine
(274 occurrences, Périgord compris) est probablement sous-représentée. Confiance : **Moyenne**
pour « l'arc montagneux Jura – Alpes du Nord – Pyrénées est bien documenté », **Faible** pour
tout classement fin.

**Conséquences pour myco-map** :
1. L'emprise actuelle (Isère, Savoie, Drôme) se trouve **dans le trio de tête** des
   départements les mieux documentés. Ce n'est pas un mauvais point de départ.
2. Extensions les plus cohérentes avec la force technique (relief fin, LIDAR) : **Savoie et
   Haute-Savoie** (Alpes du Nord complètes), puis le **Jura et le Doubs** (massif jurassien,
   n°1 pour girolle, trompette et pied-de-mouton), puis les **Hautes-Pyrénées**.
3. Ces occurrences constituent **un jeu de validation gratuit** : environ 660 points en Isère pour
   mesurer si le score concentre les observations, comme l'a fait Boletik (doc 02 §2.5).
4. Le taux de boisement varie de 12 % (Pays de la Loire) à 62 % (Corse) et monte en montagne
   ([data.gouv, *Taux de boisement*](https://www.data.gouv.fr/datasets/taux-de-boisement-1)).
   C'est cohérent avec ce ciblage.
5. Couverture LIDAR HD : objectif « France métropolitaine d'ici 2026 » ; un MNH à 50 cm est
   diffusé, une version à 5 m est annoncée ([data.gouv, *MNH LiDAR HD*](https://www.data.gouv.fr/datasets/mnh-lidar-hd/informations)).
   **L'état réel de couverture en octobre 2026 n'a pas été vérifié.**

## 4. Segmentation et personas provisoires (`customer-research`)

*Personas construits **sans données de première main**, à partir de sources indirectes :
avis concurrents, sondage éditeur, test terrain, presse. Chacun est étiqueté avec sa source et
doit être remplacé par des entretiens (§9).*

| Segment | Profil | Tâche à accomplir (JTBD) | Douleurs | Disposition à payer | Taille relative | Confiance |
|---|---|---|---|---|---|---|
| **S1 — Cueilleur confirmé local** | Plus de 5 ans de pratique, connaît ses coins, cherche à en trouver d'autres | « Trouver de nouveaux secteurs et savoir quand y aller après la pluie, sans perdre mes soirées sur Géoportail » | Coins épuisés ou partagés, temps de prospection, poussées ratées | **Prouvée** chez les concurrents (pass de 48 €, 40–60 €/an/région) | Le cœur du payant actuel (62 % chez Chasseurs) | Moyenne |
| **S2 — Novice motivé** | Randonneur, famille, néo-montagnard ; ne sait ni où ni quand ; a peur de s'intoxiquer | « Réussir une première cueillette sans risque et rentrer avec quelque chose » | Ne sait pas où chercher ; peur des confusions ; ne connaît pas les règles | **Non prouvée** ; faible a priori (gratuits : Champiscope, Géoportail) | Large mais volatile | Faible |
| **S3 — Montagnard randonneur équipé** | Paye déjà Iphigénie (24,99 €/an) ou AllTrails ; utilise des GPX | « Combiner sortie montagne et cueillette, avec un itinéraire fiable » | Approche hors sentier, temps de marche, pente | Habitude d'abonnement outdoor | Niche | Faible |
| **Anti-persona — Cueilleur commercial** | Prélève en volume pour vendre | Maximiser les kilos | — | Élevée, mais **risque légal et réputationnel** (au-delà de 10 L = délit ; vente interdite en forêt domaniale) | — | Élevée (cadre légal) |

**Arbitrage avec le cadrage « novice-friendly »** : S1 paie (preuve concurrente), S2 est la
promesse demandée par le porteur. Les deux sont compatibles si le **produit payant vise S1/S3**
(précision, temps gagné) et que la **couche novice** (sécurité, règles, pédagogie) est incluse
dans le pass. C'est l'angle de Champi : 200 fiches et un annuaire des sociétés mycologiques.
Vendre principalement à S2 serait plus fragile : faible disposition à payer et alternatives
gratuites.

### 4.1 Voix des clients — citations exactes

| Thème | Citation | Source | Confiance du thème |
|---|---|---|---|
| Gain de temps et nouveaux secteurs | « Très utile pour analyser et découvrir de nouveau spot » | Trustpilot, 2/06/2026 ([lien](https://fr.trustpilot.com/review/www.chasseursdechampignons.com)) | **Élevée** (Trustpilot + test terrain + sondage éditeur) |
| | Test terrain : 10 zones générées en ~6 min « contre une soirée d'analyse manuelle » (paraphrase) | [Champignons Passion](https://www.champignons-passion.com/conseils/avis-chasseursdechampignons-test-terrain-cartes-biotope/) | |
| Biotope ≠ coin | « ne sont pas des cartes de spots. Ce sont des cartes de biotopes. » | idem | **Élevée** (plusieurs sources : ANCT, test, Boletik) |
| | « Un 80 % ne veut pas dire que vous avez 80 % de chance de remplir votre panier. » | idem | |
| Méfiance commerciale | « Impossible de se désabonner sur le site » ; « une liste (très) restreint de 3 champignons » | Trustpilot, 07/2026 et 09/2026 | Moyenne (un seul acteur) |
| Ergonomie | « L'ergonomie est très agréable, facile à suivre pour se balader » | Trustpilot, 30/08/2026 | Faible |
| Culture du secret | Un commentateur reproche aux cartes de réduire le « mystère » ; en 2016, des cueilleurs ont vandalisé une carte collaborative de coins | [Page éditeur](https://www.chasseursdechampignons.com/blog/divers/les-avis-sur-chasseurs-de-champignons/), [Consoglobe 2016](https://www.consoglobe.com/?p=260958) | Moyenne |
| Prix comme frein | « certains » jugent le prix bloquant ; 10 % doivent acheter plusieurs cartes en limite de zones | Sondage éditeur (auto-déclaré) | Faible |
| Limite scientifique | « le déterminisme du milieu permet la pousse des champignons, mais ne l'impose pas » (M.-A. Selosse, cité par l'éditeur) | Page éditeur | — |

### 4.2 Les quatre forces du changement (JTBD)

- **Poussée** (pourquoi quitter le statu quo) : coins épuisés, pluie ou sécheresse imprévisibles,
  soirées perdues sur Géoportail, peur de se tromper (S2).
- **Attraction** (vers myco-map) : précision de montagne, « pourquoi ici » explicable, fenêtre
  de pousse par espèce, itinéraire et GPX.
- **Habitude** : mes coins connus, le bouche-à-oreille, un concurrent déjà payé, des outils
  gratuits jugés « suffisants ».
- **Anxiété** : « ça va encore me vider le portefeuille sans rien trouver », abonnement
  difficile à résilier, peur d'exposer ses propres coins (vie privée).

## 5. Grille problème : taille × fréquence (`marketing-plan`)

| | Fréquence faible | Fréquence élevée |
|---|---|---|
| Problème important | | |
| **Problème modéré** | **← myco-map** (loisir à forte charge affective et gastronomique, ressenti quelques dizaines de jours par an) | |

**Conséquences** : quadrant faible. Un **abonnement mensuel colle mal** à l'usage. Le **pass
saison ou annuel** correspond à la fréquence réelle. La rétention passe par des déclencheurs
(alertes après pluie) et non par l'usage quotidien. Les revenus hors saison doivent venir
d'objets (carte imprimée, cadeau). La pente d'acquisition restera **saisonnière** : deux fenêtres
par an, au printemps (morilles) et en été–automne.

## 6. Modèles économiques et tarification (`pricing`)

### 6.1 Paysage des prix observés (doc 02, relevé du 14/10/2026)

| Format | Acteurs | Prix |
|---|---|---|
| Gratuit | Champiscope, Waldschatzfinder, les-champignons.fr, Boletik (2026) | 0 € (affiliation, dons, publicité) |
| Mensuel bas | Mapignon | 1 €/mois |
| Mensuel | Mycora | 4,99 € et 9,99 €/mois |
| Adhésion + mensuel | Chasseurs de champignons | 28 € + 5 €/mois |
| **Pass annuel / saison** | Boletik (2027), Chasseurs | **9,99 €/an** (6,99 € pour les fondateurs) ; **48 €/an** par groupe d'espèces |
| **Par zone** | The Mycologist ; Champi | **14,90 €/an** par espèce × zone ; 9,99 €/mois, 39,99 ou 59,99 €/an (non vérifié), 149,99 € les 5 ans par région |
| Objet physique | Les Cartes Terroirs | **69,99 €** la carte A1 ; sur mesure dès 100 € |
| Référence outdoor | Iphigénie ; AllTrails ; onX | 24,99 €/an ; 35,99 $/an ; 29,99 $/an |
| Identification (autre problème) | Picture Mushroom ; Champignouf ; Shroomify | ~29,99 €/an ; 4,99 à 29,99 € ; 5,99 $ en achat unique |

### 6.2 Métrique de valeur

Question du skill : « quand le client consomme plus de [métrique], reçoit-il plus de valeur ? »

| Métrique candidate | Alignement avec la valeur | Verdict |
|---|---|---|
| Durée (mois) | Faible : la valeur se concentre sur quelques semaines | Rejeté comme métrique principale |
| **Zone géographique (massif / région)** | **Fort** : on paie la forêt qu'on arpente (Champi, The Mycologist) ; coût de calcul par zone pour l'éditeur | **Retenu** |
| **Saison** (printemps / automne / année) | **Fort** : correspond à la fréquence réelle | **Retenu, combiné à la zone** |
| Espèce | Moyen : Chasseurs et The Mycologist l'utilisent, mais cela multiplie les SKU et frustre (« 3 espèces ») | Secondaire |
| Fonctions (hors-ligne, J+14, GPX) | Moyen : sert à différencier deux paliers | Palier |

**Proposition de métrique** : **pass annuel par massif ou région**, toutes espèces comprises,
avec un palier qui ajoute les fonctions terrain. Elle est détaillée dans le doc 05.

### 6.3 Plancher, plafond, zone de prix

- **Plancher (meilleure alternative gratuite)** : 0 € (Champiscope, Géoportail, Waldschatzfinder).
  Un simple indice météo **ne peut pas** être vendu.
- **Ancre basse payante** : 9,99 €/an (Boletik 2027), voire 1 €/mois (Mapignon). Une **course
  vers le bas** est déjà engagée.
- **Plafond observé** : 48 € (pass Chasseurs), 40–60 €/an par région (Champi), 70 € pour un objet
  papier.
- **Zone de test cohérente** : **15 à 30 €/an par massif ou région**, au-dessus de l'ancre basse
  (justifié par la précision de montagne, l'explicabilité et l'itinéraire) et sous le plafond
  des acteurs installés. Confiance **Faible** : à confirmer par un sondage Van Westendorp
  (4 questions) auprès de 30 à 100 cueilleurs (§9).
- **À éviter** (`pricing`, « piège du 9 $ ») : s'aligner sur 1 €/mois ou 6,99 €/an. Cela attire
  des inscriptions qui ne valident rien et rend toute hausse ultérieure difficile.

### 6.4 Coûts à couvrir (incertitudes)

*Chiffrage détaillé en scénarios « minimal » et « confort » : doc 05 §4.*

Budget **non précisé** par le porteur. Le modèle est raisonné « à coût quasi nul hors hébergement
minimal ». Postes identifiés, **montants non vérifiés** sauf mention :

| Poste | Obligation | Prix relevé |
|---|---|---|
| Météo Open-Meteo **commerciale** | L'API gratuite est réservée au **non-commercial** ; tout usage payant exige un abonnement ([open-meteo.com/en/pricing](https://open-meteo.com/en/pricing)) | Montants non affichés lors du relevé ; une annonce ancienne citait 29 $/mois (Standard) ([Substack](https://openmeteo.substack.com/p/api-subscriptions-for-commercial)) — **non vérifié aujourd'hui** |
| Fonds de carte | Les tuiles OSM « peuvent être retirées à tout moment » pour un service commercial et le hors-ligne est **interdit** ([OSMF](https://operations.osmfoundation.org/policies/tiles/)) ; Esri : conditions commerciales non clarifiées | Non vérifié |
| Hébergement | Serveur et domaine | Non chiffré |
| Paiement | Stripe en web ; stores : commission (programmes « small business » à 15 %, **non revérifié ici**) | — |
| Juridique | CGU, CGV, mentions, politique de confidentialité | Non chiffré |

## 7. Dimensionnement (TAM / SAM / SOM)

**Méthodes** : ascendante (*bottom-up*), par les concurrents, par les canaux. Méthode par la
recherche **non réalisée** : aucun outil de volumes de mots-clés n'est connecté (→ §9).

### 7.1 Ascendante — France

| Étape | Hypothèse | Valeur |
|---|---|---|
| Adultes en France | ~54 M (ordre de grandeur INSEE, non revérifié) | 54 M |
| Part de cueilleurs | **4 à 10 %**, encadré par le Danemark (3 %) et la Pologne (25 %), Europe de l'Ouest plus basse ; cohérent avec le « 3 M » non vérifié | 2,2 à 5,4 M |
| Part « engagée » (plusieurs sorties par saison, cherche des outils) | 5 à 15 % | 110 k à 800 k |
| Part payant un outil (toutes offres) | 5 à 15 % des engagés | 5 k à 120 k payants |
| Panier annuel | 15 à 35 € | **SAM France ≈ 0,1 à 4 M€/an** |

*Confiance : **Faible**. L'écart d'un facteur 40 vient surtout de la part de cueilleurs (inconnue)
et du taux de passage au payant. Hypothèse la plus influente : la part de cueilleurs engagés.*

### 7.2 Par les concurrents (contrôle de cohérence)

Aucun concurrent ne publie de chiffre d'affaires. Inférence sur le plus visible : groupe Facebook
de 220 000+ membres (déclaré) × 2 à 5 % de payants × 48 à 88 €/an → **~0,2 à 1 M€/an**
(*inféré, confiance Faible*). Picture Mushroom (identification, monde entier) : ~35 k$/mois selon
un tiers (*Faible*). Les ~10 acteurs français semblent être de petites équipes. Le marché est
**plutôt de l'ordre du million d'euros que de la dizaine de millions**, ce qui est cohérent avec
la moitié basse du SAM.

### 7.3 Par les canaux — SOM myco-map (1 à 3 ans, solo, < 15 h/semaine)

| Scénario | Base | Calcul | Revenu annuel |
|---|---|---|---|
| **A. Alpes du Nord seules** (Isère, Savoie, Haute-Savoie, Drôme ; ~3,1 M habitants, non revérifié, plus les visiteurs de l'agglomération lyonnaise) | 100 k à 250 k cueilleurs × 10 à 20 % d'engagés = 10 k à 50 k | 1 à 5 % de captation → **100 à 2 500 payants** × 15 à 25 € | **~1,5 à 60 k€/an** |
| **B. Arc montagneux** (Alpes du Nord + Jura/Doubs + Hautes-Pyrénées) | Environ 2 à 3 fois A | Mêmes taux | ~4 à 150 k€/an |

**Recoupement** : la méthode par les canaux et la méthode ascendante se recouvrent sur la partie
basse. **Fourchette de travail : quelques centaines à quelques milliers d'euros par an pour le
scénario A dans ses deux premières saisons.** C'est exactement l'objectif « revenu d'appoint »
du porteur. Dépasser 10 k€/an demanderait le scénario B **et** une preuve de valeur (validation
publiée, bouche-à-oreille). Confiance : **Faible**. Le levier qui ferait le plus bouger le
chiffre est le **taux de conversion visite → pass**, mesurable dès la première saison
commerciale.

## 8. Attractivité du marché (grille sur 50)

| Facteur | Note | Justification |
|---|---|---|
| Clarté de la demande | 3 | Offres nombreuses, sondages éditeurs, recherche visible ; pas de volumes mesurés |
| Budget disponible | 2 | Loisir B2C, alternatives gratuites crédibles |
| Faiblesse concurrentielle | 2 | Marché encombré ; trous réels mais étroits (montagne, preuve, droit de cueillir) |
| Atteignabilité | 3 | Sociétés mycologiques, groupes Facebook, presse locale, SEO saisonnier |
| Faisabilité des canaux | 3 | SEO et communautés testables sans budget |
| Urgence | 3 | Déclenchée par la pluie, mais un loisir |
| Preuve disponible | 3 | Validation GBIF faisable (660 points en Isère) |
| Risque d'exécution | 2 | Licences commerciales, responsabilité, solo |
| Vitesse du signal | 2 | Deux fenêtres par an ; prochain test payant au printemps 2027 |
| Adéquation stratégique | 4 | Actif technique fort, données de montagne déjà en place |
| **Total** | **27 / 50** | **« Valider d'abord »** : les 90 premiers jours doivent être un sprint de validation avec critères d'arrêt |

## 9. Niches saturées, trous et validations à mener

**Saturé** : identification photo ; « carte de biotopes + indice météo France entière » ;
indice départemental gratuit.

**Trous plausibles** (doc 02 §8) : précision montagne ; preuve publiée et explicabilité ;
« ai-je le droit de cueillir ici ? » (forêt publique ou privée, arrêtés) ; itinéraire et sécurité
en montagne ; produit honnête sur la facturation (résiliation en un clic, pass sans
renouvellement piège).

**Tâches de validation** (de la moins chère à la plus chère) :

1. **Volumes de recherche** : Google Keyword Planner (gratuit avec un compte Ads) sur
   « champignons + massif / département », « carte champignons », « coins à champignons ».
   Remplace l'inconnue de la méthode par la recherche.
2. **Validation GBIF / OpenObs** du score sur l'Isère (part des observations capturée par les
   10 % de mailles les mieux notées). Elle sert à la fois de preuve et de contenu marketing.
3. **10 entretiens** de cueilleurs (sociétés mycologiques de la FMBDS Dauphiné-Savoie, groupes
   locaux) selon `customer-research` : rester informel, chercher à se réfuter, finir par « qui
   d'autre devrais-je appeler ? ».
4. **Sondage Van Westendorp** (30 à 100 réponses) sur le prix du pass massif.
5. **Pré-vente fondateurs** (liste d'attente plus paiement anticipé) avant le printemps 2027 :
   la seule preuve qui compte, quelqu'un paie.

---

### Sources principales

Voir les URLs en ligne et le doc 02. Données GBIF : API publique `api.gbif.org` (comptages de
recherche, pas un téléchargement DOI), interrogée le 14/10/2026 ; à citer via un téléchargement
DOI en cas de publication.
