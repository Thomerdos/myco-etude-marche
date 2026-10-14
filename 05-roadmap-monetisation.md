# 05 — Recommandations et roadmap de monétisation

*14 octobre 2026. Skills appliqués : `product-marketing` (positionnement), `marketing-council`
(arbitrage), `pricing` et `offers` (packaging, offre), `marketing-plan` (AARRR, phasage,
critères d'arrêt), `aso` (si passage aux stores).*

## 0. Cadre fixé par le porteur

| Paramètre | Réponse (14/10/2026) | Conséquence de conception |
|---|---|---|
| Ambition à 2–3 ans | Revenu d'appoint (quelques centaines à quelques milliers d'€/an), sans levée de fonds ni recrutement | Viser **100 à 300 passes par an**, pas la France entière |
| Temps | **Développement intensif jusqu'à la saison des morilles (printemps 2027)**, puis **moins de 15 h/semaine** | Phase 1 (6 à 9 semaines de travail) logée de novembre 2026 à mars 2027 ; tout ce qui tourne en saison doit être **automatique** |
| Périmètre | **Prospection seule** : connaître les coins à champignons ; **aucune identification**, même pédagogique | Carte + calendrier de pousse + bonnes pratiques de cueillette ; avertissement « pas d'avis sur la comestibilité » (doc 04 §5.1) |
| Cible | B2C, zones riches en champignons, **accessible aux novices** | Simplicité de la carte et bonnes pratiques ; précision de montagne pour les confirmés |
| Modèle | **Payant d'abord**, gratuit très restreint ; **produit fini uniquement, pas de prévente** | Démo minimale ; lancement commercial quand le produit est complet (§5) |
| Open source | **Non** : code, modèles et données préparées propriétaires | Dépôt à passer en privé ; **option A** retenue pour l'ODbL (doc 04 §9) |
| Coûts | **Scénario minimal** au départ, montée ligne par ligne si besoin ; relecture juridique **non chiffrée** | §4 |
| Statut | **Micro-entreprise en création** (régime classique) | Franchise de TVA, cotisations sur le chiffre d'affaires, médiateur obligatoire (doc 04 §5.8) |
| Nom | « Myco Map » **écarté** | Shortlist au §9 ; le choix final revient au porteur |

---

## 1. Positionnement (chaîne de Dunford, via `product-marketing`)

| Maillon | Contenu pour myco-map |
|---|---|
| **Alternatives réelles** | (1) Expérience et bouche-à-oreille ; (2) Géoportail (BD Forêt) + carte IGN, gratuits ; (3) indices gratuits (Champiscope, les-champignons.fr) ; (4) cartes payantes France entière (Mycora, Champi, Chasseurs de champignons) |
| **Attributs uniques** | Relief 5 m et canopée LIDAR HD à 50 m en montagne ; « pourquoi ici » par maille ; fenêtre de pousse à 14 jours par espèce ; itinéraire parking → zone avec temps de marche ; **validation publiée** (résultats chiffrés, pas le code, à produire) |
| **Valeur** | Moins de soirées de prospection, des secteurs nouveaux qu'on comprend, le bon jour pour y aller, un retour à la voiture sans se perdre, et ne pas cueillir là où c'est interdit |
| **Clients qui y tiennent le plus** | Cueilleurs des **massifs alpins** (S1), randonneurs-montagnards équipés (S3), et novices (S2) qui veulent une carte simple et les règles du jeu |
| **Catégorie** | **Côté recherche** : les mots des clients, « coins à champignons », « carte champignons » (SEO, stores). **Côté positionnement** : dans cette catégorie, *la carte de prospection des massifs de montagne*, et pas une promesse de « kilos » |
| **Style** | **Gros poisson dans une petite mare** : dominer quelques massifs, pas concurrencer Mycora sur la France |

**Promesse de travail** (à tester, pas un slogan définitif) :
*« Où et quand chercher dans votre massif cette semaine, expliqué maille par maille, avec le
chemin depuis la voiture. »*

**Messages de preuve** (ne les utiliser que lorsqu'ils sont vrais) : « X % des observations
GBIF de cèpes en Isère tombent dans les 10 % de mailles les mieux notées » ; « résiliation en
un clic, pas de renouvellement surprise ».

**Mots à éviter** (`offers`, vocabulaire banni) : « coins secrets », « kilos garantis »,
« révolutionnaire », « IA qui trouve les champignons », toute probabilité de trouver, et **tout
vocabulaire d'identification** (« reconnaître », « comestible », « sans risque »).

## 2. Conseil marketing (simulation)

> *Conseil simulé : chaque avis est construit à partir des cadres publiés de chaque conseiller,
> pas d'un avis réel de ces personnes sur ce projet.*

**Question posée** : comment faire payer quelques centaines de cueilleurs par an, en solo, sur
un marché encombré, avec une carte de prospection accessible aux novices et sans
identification ?
**Siègent** : April Dunford (positionnement), Seth Godin (plus petite audience viable),
Alex Hormozi (offre), et Byron Sharp, **contradicteur désigné**, qui se méfie de la
différenciation et de la niche.

**Dunford — positionnement contre les vraies alternatives.** Sa première question : que ferait
le client si myco-map n'existait pas ? Réponse : Géoportail le soir, ou Champi. Les attributs
qu'aucune alternative n'a sont la précision de montagne, l'explication et l'itinéraire. Ils ne
valent quelque chose que pour ceux qui cherchent dans des **terrains raides et variés**. Elle
choisirait le style « gros poisson, petite mare » et refuserait de créer une catégorie.
*En résumé : vendre la meilleure carte de prospection des Alpes du Nord, pas une carte de
France de plus.*

**Godin — plus petite audience viable.** À qui est-ce destiné, et à quoi ça sert ? Quelques
centaines de cueilleurs alpins qui se reconnaissent dans « les gens comme nous préparent leur
sortie sérieusement et respectent la forêt ». Il demanderait la permission avant de vendre : un
**bulletin de pousse par massif**, attendu après chaque orage. Il mettrait en garde contre la
course vers le bas de Mapignon et Boletik.
*En résumé : servir une petite tribu de façon remarquable, et la laisser en parler.*

**Hormozi — équation de valeur.** Il noterait les quatre leviers :
résultat rêvé 6/10 (nouveaux secteurs, panier) ; **probabilité perçue 3/10** (aucune preuve) ;
délai 7/10 (fenêtre J+14, alertes) ; effort 4/10 (interface experte). Le levier le plus faible
est la probabilité perçue. Il faut donc une validation publiée et une garantie, pas une baisse
de prix. Il refuserait de concurrencer à 6,99 € et vendrait **plus cher avec plus de valeur
empilée** : hors-ligne, itinéraire, alertes, calendrier de pousse, règles de cueillette.
*En résumé : ne pas baisser le prix ; augmenter la certitude et réduire l'effort.*

**Sharp — contradicteur.** Les acheteurs perçoivent rarement la différenciation. Ils achètent
ce dont ils se souviennent et ce qu'ils trouvent facilement. Une niche de quelques centaines
d'acheteurs aura aussi moins de fidélité (« double peine »). Il demanderait d'être présent à
**tous** les moments d'entrée dans la catégorie (« ça pousse ? » après la pluie, « champignons
+ nom du massif ») avec des signes distinctifs constants (nom, couleur, carte reconnaissable),
plutôt que de compter sur la loyauté.
*En résumé : une niche, d'accord, mais être partout où l'on cherche dans cette niche, avec une
identité constante.*

**Où le conseil diverge**

1. **Différenciation contre disponibilité** (Dunford et Hormozi face à Sharp). Le vrai arbitrage
   est le suivant : investir dans la preuve de précision, ou dans la présence SEO et
   communautaire ? *Ce qui trancherait* : la validation GBIF. Si l'écart avec le hasard est net,
   la différenciation est démontrable et vaut d'être mise en avant. S'il est faible, Sharp a
   raison et il faut miser sur la présence.
2. **Prix plus élevé et plus de valeur, ou prix d'appel** (Hormozi face à la tentation Boletik).
   Ce qui trancherait : un sondage Van Westendorp auprès des inscrits au bulletin, puis la
   conversion réelle des premières semaines de vente (pas de prévente, choix du porteur).
3. **Permission ou vente directe** (Godin face au « payant d'abord »). Compromis : le bulletin
   gratuit est **éditorial** (au niveau du massif, sans carte détaillée). Il construit la
   permission sans transformer le produit en freemium.

**Synthèse du président**

- **À faire** : (1) publier la validation avant d'ouvrir les ventes ; (2) un bulletin de pousse par
  massif comme seul gratuit récurrent ; (3) un pass saison à valeur empilée, sans prix
  plancher ; (4) une présence constante sur les recherches « champignons + massif ».
- **Signal d'alerte** (Sharp) : si moins de 2 % des abonnés au bulletin achètent un pass en
  saison, la niche est trop petite ou mal servie ; il faut élargir à d'autres massifs avant
  d'ajouter des fonctions.
- **Exécution** : `pricing`, `offers`, `copywriting`, `content-strategy`, `emails`.

## 3. Offre et packaging (`pricing` + `offers`)

### 3.1 Gamme proposée (deux paliers, une seule métrique : la zone)

| Produit | Contenu | Prix de test | Logique |
|---|---|---|---|
| **Découverte** (gratuit, très restreint) | 1 **secteur vitrine fixe** (environ 10 × 10 km), semaine en cours, mode simple, sans export, sans hors-ligne, sans compte ; plus le **bulletin de pousse par massif** par e-mail | 0 € | Démonstration et permission, conforme au « gratuit très restreint ». Ce n'est pas un freemium : aucune zone personnelle |
| **Pass Saison — 1 massif** | 12 mois, toutes espèces, carte complète du massif, J+14, « pourquoi ici », itinéraires GPX/KMZ, **hors-ligne**, alertes après orage, calendrier de pousse par espèce, **bonnes pratiques et règles de cueillette**, couche forêts publiques | **19 €** (fourchette à tester : 15–25 €) | Métrique zone × saison (doc 03 §6.2) ; au-dessus de l'ancre Boletik, sous Champi et Chasseurs |
| **Pass Saison — Tous massifs** | Idem, sur tous les massifs couverts (Alpes du Nord, puis Jura…) | **29 €** (à tester) | Répond à la plainte « je suis à la frontière de deux zones » (10 % chez Chasseurs) ; permet de monter en gamme à mesure que la couverture s'étend |
| **Carte imprimée du massif** (achat unique, hors saison, **à partir de 2028**) | Carte A1 du potentiel d'habitat du massif, légende de prospection, règles de cueillette | À fixer entre 39 et 59 € (coût d'impression à la demande **non vérifié** ; vente de biens à un autre taux de cotisations, doc 04 §5.8) | Revenu de novembre à mars, cadeau de fin d'année ; Les Cartes Terroirs valide le format à 69,99 € |

**Pourquoi pas de paliers par fonctionnalité** : chaque palier supplémentaire, c'est du
support et des cas limites. À moins de 15 h/semaine, **une seule métrique (la zone)** est plus
simple à maintenir et à expliquer.

**Pourquoi pas de mensuel** : l'usage tient à quelques semaines par an (doc 03 §5). Un mensuel
pousse à résilier après la poussée ; c'est le problème vécu chez Chasseurs de champignons.

### 3.2 Les six composantes de l'offre (`offers`)

| Composante | Proposition |
|---|---|
| **Cœur** | Le Pass Saison du massif |
| **Bonus** (réels, pas gonflés) | Calendrier de pousse par espèce et par massif ; export GPX vers l'appli de randonnée de l'utilisateur ; règles de cueillette du département (quotas, propriété, arrêtés) ; guide des bonnes pratiques (prélèvement, respect du milieu, sécurité en montagne) |
| **Garantie** | **Remboursement intégral sous 14 jours, sans justification** ; **pas de renouvellement automatique par défaut** (rappel par e-mail, renouvellement en un clic). C'est le contre-pied direct des avis négatifs sur Chasseurs de champignons. *Conditions à relire juridiquement (droit de rétractation sur contenu numérique).* |
| **Urgence réelle** | **Pas de prévente ni de passes fondateurs** (choix du porteur). La seule urgence est **la saison elle-même** : le pass s'achète quand la pluie annonce une poussée, et le bulletin le rappelle. Pas de faux compte à rebours, pas de rareté inventée |
| **Nom** | « Pass Saison [nom du massif] » ; nom de marque à choisir dans la shortlist du §9 |
| **Prix et paiement** | Paiement unique annuel via Stripe Checkout ; Customer Portal pour factures et remboursements ; mention « TVA non applicable » tant que la franchise s'applique (micro-entreprise, doc 04 §5.8) |

### 3.3 Arbitrages assumés

| Option | Gain | Coût | Choix |
|---|---|---|---|
| Prix bas (≤ 10 €), comme Boletik | Conversion facile | Piège du 9 € ; course vers le bas ; ~200 passes pour 2 k€ | ❌ |
| Prix moyen (19–29 €) | Couvre les coûts avec peu d'acheteurs ; cohérent avec la valeur empilée | Exige une preuve (validation) | ✅ à tester |
| Abonnement mensuel | Revenu récurrent apparent | Inadapté à la saisonnalité ; résiliations ; support | ❌ |
| Freemium généreux | Audience | Contraire au choix du porteur ; coûts serveur et météo | ❌ |
| Appli native sur les stores | Visibilité ASO | Commission, revue, double maintenance | ⏸ plus tard (§7) |
| B2B (offices de tourisme, accompagnateurs) | Revenus plus gros par client | Vente active, hors cible B2C | ⏸ option 2028+ |
| Identification (photo **ou pédagogique**) | Attente des novices | Responsabilité, 35–49 % de fiabilité en photo, marché saturé ; **hors périmètre par décision du porteur** | ❌ définitif |
| Prévente / passes fondateurs | Trésorerie et preuve d'achat avant la fin du développement | Engagement de livraison ; refusé par le porteur | ❌ |

### 3.4 Économie unitaire (micro-entreprise en franchise de TVA)

- **Stripe** : **1,5 % + 0,25 €** par carte de l'EEE, sans abonnement ; les frais ne sont pas
  rendus en cas de remboursement ([stripe.com/fr/pricing](https://stripe.com/fr/pricing),
  relevé du 14/10/2026).
- **Cotisations sociales** : **21,2 %** du prix encaissé (prestations de services BIC), plus
  ~0,2 % de formation professionnelle. Sources secondaires, **à confirmer sur urssaf.fr**. ACRE
  ignorée ici, par prudence.
- **TVA** : non facturée (franchise jusqu'à 37 500 €) ; le prix affiché est le prix encaissé.

| Produit | Prix | Stripe | Cotisations (~21,4 %) | **Net avant impôt** |
|---|---|---|---|---|
| Pass Saison — 1 massif | 19 € | 0,54 € | 4,07 € | **≈ 14,40 €** |
| Pass Saison — tous massifs | 29 € | 0,69 € | 6,21 € | **≈ 22,11 €** |
| Moyenne (mix) | 22 € | 0,58 € | 4,71 € | **≈ 16,71 €** |

L'impôt sur le revenu (barème, ou versement libératoire optionnel de 1,7 %) n'est pas déduit.
Les coûts récurrents et le nombre de passes nécessaires sont au §4.

## 4. Coûts récurrents : estimations chiffrées

*Prix relevés les 13 et 14/10/2026 sur les sources citées, **hors TVA** sauf mention. « Tiers »
= relevé sur un site comparateur et non sur la page du fournisseur : à confirmer dans la console
avant de s'engager. « Non vérifié » = aucune source fiable trouvée. Les montants en dollars ne
sont pas convertis à un taux précis : on prend 0,85 à 0,95 € par dollar, taux **non vérifié**.*

### 4.1 Hypothèses de dimensionnement

| Hypothèse | Valeur retenue | Base |
|---|---|---|
| Zone servie | Alpes du Nord (Isère, Savoie, Haute-Savoie, Drôme) ≈ 24 000 km² | Surfaces départementales en ordre de grandeur, non revérifiées |
| Mailles de 50 m | ≈ 9,7 M (environ 4 fois l'emprise actuelle) | Calcul |
| Base SQLite | ≈ 0,6 à 0,8 Go | Extrapolation linéaire de 150–205 Mo pour 2,35 M mailles (doc 01) |
| Tuiles d'habitat (6 espèces, zooms 10 à 15) | ≈ 2 à 4 Go | Hypothèse : ~32 000 tuiles par espèce × 10–20 Ko |
| Fond de carte hors-ligne (extrait Protomaps de la zone) | 0,5 à 2 Go | **Non mesuré** ; la taille double à chaque niveau de zoom ([docs Protomaps](https://docs.protomaps.com/basemaps/downloads)) |
| Données brutes de travail (LIDAR, MNT…) | ~13 Go, **restent sur la machine de développement** | Doc 01 ; inutiles en production |
| Payants en saison | Jusqu'à 300 | Haut de l'objectif (§3.4) |
| Trafic sortant | 300 × 2 à 4 téléchargements hors-ligne de 100–200 Mo ≈ **60 à 240 Go par saison**, plus la navigation | Hypothèse |
| Météo | Grille fixe de 169 points par région, rafraîchie toutes les 1 à 3 h, **indépendante du trafic** (doc 04 §3.3) → ~42 000 à 126 000 requêtes par mois et par région, multipliées par ~2 à 3 selon les règles de pondération d'Open-Meteo (plus de 2 semaines d'historique ou plus de 10 variables comptent plusieurs appels, [open-meteo.com/en/pricing](https://open-meteo.com/en/pricing)) → **~80 000 à 380 000 appels/mois** | Calcul ; le décompte des requêtes multi-points n'est pas précisé par Open-Meteo |

### 4.2 Hébergement : options chiffrées

| Brique | Option | Prix relevé | Source | Remarque |
|---|---|---|---|---|
| **Serveur** | Hetzner Cloud **CX23** (2 vCPU, 4 Go, 40 Go, 20 To de trafic) | **5,49 €/mois + 0,50 € d'IPv4** = 5,99 €/mois | Tiers : [costgoat.com](https://costgoat.com/pricing/hetzner) (MAJ du 05/09/2026) | Allemagne / Finlande seulement ; hausse de prix le 15/06/2026 ; un relevé de septembre signale une indisponibilité ponctuelle |
| | Hetzner **CX33** (4 vCPU, 8 Go, 80 Go) | **8,49 € + 0,50 €** = 8,99 €/mois | Tiers, idem | Confort |
| | OVHcloud **VPS-1** | **6,49 €/mois** (66,19 €/an en prépaiement, tiers) | [Blog OVHcloud](https://blog.ovhcloud.com/en/posts/pricing-evolution-of-public-cloud-bare-metal-and-vps-at-ovhcloud/) | Hébergeur français ; spécifications non listées sur le blog (4 vCPU, 8 Go, 75 Go selon un tiers) |
| | OVHcloud **VPS-2** | **9,99 €/mois** | Idem | Confort |
| **Sauvegardes** | Sauvegardes Hetzner | **20 % du prix du serveur** (7 conservées) | Tiers, idem | Soit ~1,10 € à 1,70 €/mois |
| **Base de données** | **SQLite sur le serveur** (en lecture seule pour l'habitat) | 0 € | — | **Recommandé** : la donnée est précalculée, pas besoin d'un SGBD managé |
| | PostgreSQL managé Scaleway DB-DEV-S | ~0,0156 €/h, soit **~11,40 €/mois** (calcul à partir du tarif horaire, non publié comme tel) + stockage | [Scaleway](https://www.scaleway.com/fr/tarifs/managed-databases) via résultat de recherche | **Non recommandé** : coût sans bénéfice pour ce produit |
| **Stockage des tuiles et paquets hors-ligne** | Cloudflare **R2** | **10 Go/mois gratuits**, puis **0,015 $/Go-mois** ; **sortie gratuite** | [developers.cloudflare.com/r2/pricing](https://developers.cloudflare.com/r2/pricing/) | La sortie gratuite neutralise le coût des téléchargements hors-ligne |
| | Disque du serveur (40 à 80 Go) | Inclus | — | Suffisant au départ ; 20 To de trafic inclus chez Hetzner |
| **CDN** (optionnel) | Bunny CDN | **0,01 $/Go** en Europe, **minimum 1 $/mois** | [bunny.net/pricing/cdn](https://bunny.net/pricing/cdn/) | Utile seulement si la latence pose problème |
| **Fond de carte** | Extrait **Protomaps** auto-hébergé (PMTiles) | 0 € hors stockage | [docs Protomaps](https://docs.protomaps.com/basemaps/downloads) | « Œuvre produite » ODbL : attribution OSM obligatoire ; autorise le hors-ligne puisqu'on l'héberge soi-même |
| | MapTiler Cloud **Flex** | **30 $/mois** ; l'offre gratuite vise le « non-commercial » | [maptiler.com/cloud/pricing](https://www.maptiler.com/cloud/pricing/) | Droits hors-ligne **non précisés** sur la page |
| | Géoplateforme IGN (Plan IGN, orthophotos) en ligne | Gratuit selon des retours d'usagers | Conditions commerciales et hors-ligne **non vérifiées** | À confirmer avant usage |

### 4.3 Maintenance et services : coûts récurrents

| Poste | Option « coût minimal » | Option « confort » | Sources |
|---|---|---|---|
| **Météo** | **Données ouvertes Météo-France** (AROME, Licence Ouverte) : 0 € ; ingestion GRIB à développer (3 à 5 jours estimés) ; conditions de l'API du portail Météo-France non vérifiées | **Open-Meteo API Standard : 29 $/mois** (1 M d'appels, licence commerciale incluse) ; Professional 99 $/mois | [data.gouv AROME](https://data.gouv.fr/en/datasets/donnees-du-modele-atmospherique-arome-a-aire-limitee-a-haute-resolution) ; [blog Open-Meteo](https://openmeteo.substack.com/p/api-subscriptions-for-commercial) (la page de prix en ligne n'affiche pas les montants) |
| **Domaine** | .fr : **~7,79 € HT/an** | Idem (+ .com, non vérifié) | Source non officielle, **non vérifié** sur la boutique OVHcloud France |
| **E-mails** (liens magiques, reçus, alertes, bulletin) | **Resend gratuit** : 3 000/mois, **100/jour** au plus | **Resend Pro : 20 $/mois** (50 000/mois, sans plafond journalier) | [resend.com/pricing](https://resend.com/pricing) |
| **Paiement** | Stripe : **1,5 % + 0,25 €** par carte de l'EEE, sans abonnement ; Checkout inclus | Idem ; Stripe Tax en option : 0,5 % par transaction (no-code) | [stripe.com/fr/pricing](https://stripe.com/fr/pricing) |
| **Sauvegardes** | Sauvegardes Hetzner (20 %) ou copie vers R2 (gratuit sous 10 Go) | Les deux | Voir §4.2 |
| **Supervision** | UptimeRobot **gratuit** (50 sondes, 5 min ; décrit comme « pour projets hobby et non-profit », usage commercial **non confirmé**) + Sentry **Developer gratuit** (1 utilisateur, 5 000 erreurs/mois) | UptimeRobot **Solo : 9 €/mois** en annuel (108 €/an) ; Sentry Team (26 $/mois) jugé superflu | [uptimerobot.com/pricing](https://uptimerobot.com/pricing/), [sentry.io/pricing](https://sentry.io/pricing/) |
| **Stores** (plus tard, §7) | — | Apple : ~99 $/an ; Google Play : ~25 $ une fois | Sources secondaires ([splitmetrics](https://splitmetrics.com/blog/google-play-apple-app-store-fees/)), **à confirmer** |
| **Relecture juridique** (CGU/CGV, lecture de l'ODbL) | **Non chiffré** | **Non chiffré** | Pas de budget fixé par le porteur |
| **Médiateur de la consommation** (obligatoire en B2C) | **30 à 80 €/an** | Idem | Source commerciale, **non vérifié** ([portail-autoentrepreneur.fr](https://www.portail-autoentrepreneur.fr/academie/creation-auto-entreprise/mediation-consommation)) |
| **Cotisations sociales** (micro-entreprise) | ~21,4 % du chiffre d'affaires (déjà déduit dans le net par pass, §3.4) | Idem | Sources secondaires, à confirmer sur urssaf.fr |
| **TVA** | Franchise : rien à reverser, mais la TVA payée sur les dépenses n'est **pas récupérable** → coûts comptés TTC ci-dessous | Idem | Doc 04 §5.8 |
| **Dépôt de marque INPI** (ponctuel, pas récurrent) | ~190 € pour une classe, valable 10 ans | Idem (+40 € par classe) | Sources secondaires, à confirmer sur inpi.fr |
| **CFE, comptabilité, banque** | **Non instruit** | **Non instruit** | À vérifier à la création |

### 4.4 Deux scénarios annuels — **minimal retenu** au départ

| Ligne | **Coût minimal (retenu)** | **Confort** |
|---|---|---|
| Serveur | Hetzner CX23 + IPv4 : 71,88 € HT | Hetzner CX33 + IPv4 : 107,88 € HT |
| Sauvegardes | 20 % : 13,18 € HT | 20 % : 20,38 € HT |
| Base de données | SQLite : 0 € | SQLite : 0 € |
| Stockage et sortie | R2 gratuit (≤ 10 Go) : 0 € | R2 ~30 Go : ~3,60 $ |
| CDN | — | Bunny : ~12 à 15 $ |
| Fond de carte | Protomaps auto-hébergé : 0 € | Idem : 0 € |
| Météo | Météo-France ouvert : 0 € | Open-Meteo Standard : 348 $ |
| E-mails | Resend gratuit : 0 € | Resend Pro : 240 $ |
| Supervision | Gratuit : 0 € | UptimeRobot Solo : 108 € HT |
| Domaine | ~7,79 € HT (non vérifié) | ~7,79 € HT (non vérifié) |
| Médiateur de la consommation | 30 à 80 € (non vérifié) | 30 à 80 € (non vérifié) |
| Relecture juridique | Non chiffré | Non chiffré |
| **Total HT (hors médiateur)** | **≈ 93 €** | **≈ 244 € + ~606 $ ≈ 760 à 820 €** |
| **Total payé (TVA non récupérable + médiateur)** | **≈ 140 à 190 €/an** | **≈ 840 à 1 065 €/an** (selon la TVA appliquée par les fournisseurs hors UE) |
| **Passes à 19 € pour couvrir** (net ≈ 14,40 € après Stripe et cotisations) | **≈ 10 à 14 passes** | **≈ 58 à 74 passes** |

**Montée ligne par ligne** (décision du porteur) : la première ligne à ajouter, si l'ingestion
Météo-France s'avère trop coûteuse en temps, est **Open-Meteo Standard**. Le total passe alors
à **≈ 440 à 590 €/an**, soit **≈ 31 à 41 passes**. Ensuite viennent Resend Pro, si le bulletin
dépasse 100 envois par jour, puis la supervision payante.

**Ponctuel** : dépôt de marque INPI ~190 € (≈ 13 passes, une fois pour 10 ans).
**Non compris** : relecture juridique, impôt sur le revenu, CFE, temps passé, matériel, stores.

### 4.5 Résultat selon les ventes (après Stripe et cotisations, avant impôt sur le revenu)

| Passes vendus par an | Net (Stripe + cotisations déduits) | − coût minimal (140–190 €) | − confort (840–1 065 €) |
|---|---|---|---|
| 50 (19 €) | ≈ 720 € | **≈ 530 à 580 €** | **≈ −120 à −345 €** (perte) |
| 150 (22 € en moyenne) | ≈ 2 507 € | **≈ 2 317 à 2 367 €** | **≈ 1 442 à 1 667 €** |
| 300 (22 € en moyenne) | ≈ 5 013 € | **≈ 4 823 à 4 873 €** | **≈ 3 948 à 4 173 €** |

**Lecture** : en scénario minimal, l'activité couvre ses coûts dès **une quinzaine de passes**.
Le confort fait perdre de l'argent sous ~60 passes et ne se justifie qu'au-delà d'une centaine
de passes par an, ou si le temps gagné vaut plus que ~700 €/an. Le revenu net reste dans la
fourchette « revenu d'appoint » visée (quelques centaines à quelques milliers d'euros).

### 4.6 Charge de travail récurrente (objectif : moins de 15 h/semaine)

| Tâche | Fréquence | Charge estimée |
|---|---|---|
| Support (questions, remboursements) | En saison | 1 à 3 h/semaine |
| Supervision et incidents | Alertes automatiques | ~1 h/semaine en saison |
| Mises à jour de sécurité (système, PHP, dépendances) | Mensuelle | 1 à 2 h/mois |
| Bulletin de pousse | Généré automatiquement après un épisode pluvieux, puis relu | ~30 min par envoi, 1 à 2 par semaine en saison |
| Contenu, SEO, présence communautaire | En saison | 2 à 4 h/semaine |
| Comptabilité, rapprochement Stripe | Mensuelle | ~1 h/mois |
| Précalcul annuel des données | Janvier–février | 2 à 3 jours/an |
| Nouveau massif | Une fois par an, hors saison | 1 à 2 semaines/an |
| Revue des prix et licences des fournisseurs | Annuelle | ~½ journée/an |
| **Total** | | **≈ 5 à 10 h/semaine en saison ; 1 à 3 h/semaine en moyenne hors saison**, plus les blocs annuels |

**Condition** : cela suppose la refonte « habitat statique + météo planifiée » (doc 04 §3.3).
Sans elle, la charge et les coûts croissent avec le trafic.

## 5. Roadmap par phases

*Les efforts sont des ordres de grandeur pour un développeur seul qui connaît le code. L'impact
est noté sur l'objectif « revenu d'appoint ». Le calendrier suit les deux fenêtres de saison.*

### Calendrier d'ensemble

```
oct.–mi-nov. 2026   Phase 0  validation, entretiens, décisions (fin de saison d'automne)
mi-nov. 2026–fév. 2027  Phase 1  construction du produit fini (dev intensif, 6 à 9 semaines de travail)
mars 2027           Phase 1b bêta fermée gratuite du produit fini + mise en place légale et paiement
début avril 2027    LANCEMENT du produit fini (ouverture des ventes, saison des morilles)
avril–mai 2027      Phase 2  première saison payante, puis passage sous 15 h/semaine
juin–nov. 2027      Phase 3  saison principale
2028+               Phase 4  un massif de plus par an
```

### Phase 0 — Validation et décisions (maintenant → mi-novembre 2026, fin de la saison d'automne)

| Action | AARRR | Effort | Impact | Critère de succès / d'arrêt |
|---|---|---|---|---|
| **Passer le dépôt GitHub en privé avant tout push**, remplacer la licence MIT par « tous droits réservés », mettre à jour README / `ATTRIBUTION.md` / `AGENTS.md` (doc 04 §9.1) | — | < 1 h | 🔥 Protège la stratégie et le code futur | Fait **avant** de pousser cette étude |
| **Validation GBIF / OpenObs** du score sur l'Isère (doc 04 §4) | Revenu (preuve) | ~2 j | 🔥 Élevé | Écart avec le hasard ≥ ~1,5 pour au moins le cèpe ou la girolle, sinon **re-calibrage avant de construire la suite** |
| **10 entretiens** de cueilleurs (expositions mycologiques d'octobre, sociétés de la FMBDS, groupes locaux) | Toutes étapes | ~10 h | 🔥 Élevé | Phrases exactes sur les douleurs, prix évoqués, et les 3 fonctions jugées indispensables |
| **Choix du nom** dans la shortlist (§9), réservation des domaines .fr et .com, recherche d'antériorité INPI | Acquisition | ~½ j | Moyen | Nom retenu, domaines réservés |
| Volumes de recherche (Keyword Planner) : « coins à champignons + massif » | Acquisition | ~2 h | Moyen | Volume par massif connu |
| Héberger localement Inter et Leaflet (RGPD) | — | < 1 h | Faible, mais sans regret | — |
| Page d'attente : promesse, **inscription au bulletin et à la liste de lancement, sans paiement** | Acquisition | ~1 j | Élevé | ≥ 100 inscrits avant le lancement d'avril 2027 |

### Phase 1 — Construction du produit fini (mi-novembre 2026 → fin février 2027, développement intensif)

Environ **15 semaines calendaires** pour **6 à 9 semaines de travail** estimées : la marge
absorbe les fêtes de fin d'année et les imprévus.

| Ordre | Action | Effort | Raison |
|---|---|---|---|
| 1 | Déploiement de production minimal (PHP-FPM ou FrankenPHP, TLS, `prod`) sur un VPS **scénario minimal** (Hetzner CX23 ou OVH VPS-1, SQLite, R2) | 2–3 j | Doc 04 §3.1, §4.4 |
| 2 | **Habitat statique en tuiles + météo planifiée** par grille fixe | ~1 sem | Coût et charge ≈ constants ; condition des moins de 15 h/semaine |
| 3 | Météo : **ingestion Météo-France** (0 €, 3–5 j). Repli : Open-Meteo Standard (29 $/mois, ~½ j) si l'ingestion déborde | ½–5 j | Doc 04 §5.2 |
| 4 | Fonds de carte : **extrait Protomaps auto-hébergé** (hors-ligne autorisé, attribution OSM) | 1–2 j | Doc 04 §5.3 |
| 5 | **PWA hors-ligne** par massif acheté | 1–2 sem | 🔥 Justifie le pass |
| 6 | **Mode simple + onboarding mobile d'abord** (« où chercher cette semaine ») | 1–2 sem | 🔥 Conversion des novices |
| 7 | Forêts publiques ONF + « marche estimée » + plafond de pente en mode novice ; **bonnes pratiques et règles de cueillette** ; avertissement « pas d'avis sur la comestibilité » | 3–4 j | Doc 04 §5.1, §5.5–5.6 |
| 8 | Calendrier de pousse par espèce et pages de prospection par massif (sans identification) | 2–3 j | Contenu du pass et SEO |
| 9 | Extension aux **Alpes du Nord** complètes (Savoie, Haute-Savoie), calcul en tâche de fond | 3–5 j | Doc 03 §3 |
| 10 | **Conformité ODbL, option A** : page de téléchargement des couches dérivées d'OSM, ou de leur algorithme | ~½ j | Doc 04 §9.2 |
| 11 | Stripe Checkout + Portal, passes par zone, lien magique | 3–5 j | Doc 04 §3.2 |
| 12 | Tests de non-régression du score | 1–2 j | Doc 04 §7 |

### Phase 1b — Bêta du produit fini et mise en route légale (mars 2027)

- **Bêta fermée gratuite** de 15 à 30 testeurs (recrutés en phase 0) sur le produit **complet**.
  C'est un test qualité, **pas une prévente** : aucun paiement.
- **Création de la micro-entreprise**, adhésion à un **médiateur de la consommation**, mentions
  légales, CGU/CGV (relecture juridique si un budget est dégagé), Stripe en mode réel.
- Dépôt de la marque à l'INPI (~190 €, à confirmer).
- **Critère de passage au lancement** : aucun bug bloquant, et au moins la moitié des testeurs
  disent qu'ils paieraient le pass au prix annoncé.

### Lancement et Phase 2 — Première saison payante (avril–mai 2027 : morilles)

- **Ouverture des ventes du produit fini** début avril, annoncée au bulletin et à la liste de
  lancement. Aucune remise « fondateur ». Le prix affiché est le prix de la saison.
- Petite saison (morilles : 78 observations GBIF en Isère, 52 en Haute-Savoie). C'est un **test
  grandeur nature** à faible enjeu.
- Mesurer : visites → secteur vitrine → pass ; remboursements ; usage hors-ligne ; ouverture des
  alertes.
- **Sondage Van Westendorp** auprès des inscrits pour confirmer le prix d'automne.
- **Fin du développement intensif** : passage au régime de **moins de 15 h/semaine**.
- **Critère d'arrêt** : **moins de 15 passes vendus au 31 mai 2027** (seuil de couverture du
  scénario minimal) **ou** conversion des inscrits inférieure à 2 % → revoir prix, offre ou
  positionnement avant l'automne.

### Phase 3 — Saison principale (juin–novembre 2027)

- Bulletin de pousse **automatique** après chaque épisode déclenchant (le moteur `FlushClock`
  le détecte déjà) : rétention et permission sans travail manuel.
- Contenu saisonnier par massif (« Champignons en Chartreuse : où et quand ») : une page par
  massif et par espèce, rédigée une fois et mise à jour par les données.
- Présence aux expositions mycologiques d'automne et dans la presse locale (angle : « une carte
  qui publie sa précision »).
- Régime de croisière : **moins de 15 h/semaine**, surtout support et contenu.
- **Critère de réussite** : **≥ 50 passes vendus au 30 novembre 2027**, soit environ 530 à 580 €
  net après coûts en scénario minimal : l'objectif « revenu d'appoint » est atteint. **Moins de
  20** → arrêter ou repositionner.

### Phase 4 — Consolidation (2028 et après)

- **Un massif de plus par an**, choisi sur la densité d'observations : Jura et Doubs, puis
  Hautes-Pyrénées (doc 03 §3).
- Précalcul annuel scripté (janvier–février).
- Carte imprimée en vente pour la fin d'année.
- Options à réévaluer **uniquement si les chiffres le justifient** : application sur les
  stores (§7), offre pour accompagnateurs en montagne ou offices de tourisme, Suisse et Italie
  alpines.

### Ce que l'on ne fait pas, et pourquoi

| Idée | Raison |
|---|---|
| France entière | Incompatible avec moins de 15 h/semaine ; dilue l'avantage montagne ; marché encombré |
| Identification (photo ou pédagogique) | Hors périmètre par décision du porteur ; responsabilité ; fiabilité de 35 à 49 % en photo |
| Prévente, passes fondateurs | Refusé par le porteur : on vend le produit fini |
| Migration OSM → BD TOPO | Option B écartée (option A retenue) ; à reconsidérer seulement si l'ODbL devient une gêne |
| Publicité payante | Budget non précisé ; saisonnalité ; coût d'acquisition inconnu |
| Communauté de partage de coins | Culture du secret (vandalisme en 2016) ; modération chronophage |
| Applis natives dès le départ | Double maintenance ; la PWA suffit pour valider |

## 6. Plan marketing allégé (`marketing-plan`, adapté à un solo sans budget)

| Étape AARRR | Actions | Indicateur avancé |
|---|---|---|
| **Acquisition** | Pages SEO par massif et espèce ; bulletin de pousse ; sociétés mycologiques (FMBDS) ; presse locale après un orage ; publication de la validation ; présence ponctuelle dans les groupes Facebook (selon leurs règles) | Inscrits au bulletin par semaine en saison |
| **Activation** | Secteur vitrine en mode simple ; premier bénéfice en moins de 60 s ; démo « pourquoi ici » | % de visiteurs qui ouvrent le détail d'une maille |
| **Rétention** | Alertes automatiques après orage ; rappel de renouvellement ; fiches saisonnières | Taux d'ouverture des alertes ; renouvellement d'une année sur l'autre |
| **Recommandation** | Pass cadeau ; carte imprimée offerte ; « partagez un secteur vitrine » | Part des achats issus d'un cadeau ou d'un lien |
| **Revenu** | Pass massif, Pass tous massifs, carte imprimée | Passes vendus par saison ; prix moyen ; taux de remboursement |

**Indicateur principal** : **nombre de passes actifs pendant la saison d'automne**.
**Décisions ouvertes liées au plan** : coût d'acquisition inconnu (pas de données) ; budget
non précisé.

## 7. Si l'on passe aux stores un jour (`aso`)

*À ne considérer qu'après une saison réussie en PWA. Grille ASO appliquée en prévision ;
aucune fiche n'existe encore.*

- **Google Play** : publier la PWA via une *Trusted Web Activity*, à moindre coût.
  **Apple** : un simple emballage web risque un refus au titre de la règle 4.2 (« fonctionnalité
  minimale ») ; prévoir des fonctions natives (hors-ligne, géolocalisation).
- **Titre (≤ 30 car.)** : marque + mot-clé, par exemple « Le Bon Versant : champignons » (28 car.) si ce nom est retenu (§9).
  Sous-titre Apple (≤ 30) : « Prévision cèpes et girolles » (27 car.). Champ de mots-clés Apple
  (100 octets, sans répéter le titre) : `alpes,chartreuse,vercors,belledonne,savoie,morilles,cueillette,coins,pousse,randonnee`.
- **Captures** : les 3 premières disent tout. (1) « Où chercher cette semaine dans votre
  massif » ; (2) « Pourquoi ici : versant frais, hêtraie, sol neutre » ; (3) « Le chemin depuis
  la voiture, même hors réseau ».
- **Notes** : solliciter un avis après une sortie réussie (3 demandes par an maximum sur iOS) ;
  répondre à tous les avis négatifs, ce que Champignouf n'a pas fait en 2020.

## 8. Décisions prises et questions restantes

**Décidé le 14/10/2026** :

| Sujet | Décision |
|---|---|
| Open source | Non : tout reste propriétaire |
| Scénario de coûts | Minimal, montée ligne par ligne |
| Temps | Développement intensif jusqu'au printemps 2027, puis moins de 15 h/semaine |
| Identification | Supprimée du périmètre : prospection et bonnes pratiques uniquement |
| Statut | Micro-entreprise à créer (régime classique) |
| Nom | « Myco Map » écarté ; choix dans la shortlist du §9 |
| Prévente | Non : lancement du produit fini |
| ODbL | Option A : publier les couches dérivées d'OSM |

**Restant ouvert** :

1. **Budget de relecture juridique** (CGU/CGV, lecture de l'ODbL) : non chiffré à ce jour.
2. **Choix final du nom** parmi la shortlist du §9, après une recherche d'antériorité INPI.

## 9. Nom de marque : shortlist

**Méthode** : des noms français, distincts du paysage concurrentiel (Mycora, Champi,
Champiscope, Chasseurs de champignons, The Mycologist, Mapignon, Boletik, MycoDB, Sporecast,
Mushroom Map, Coins à champignons, Expert de Cueillette) et cohérents avec le positionnement
« prospection en montagne ».

- **Domaines** : statut d'enregistrement interrogé le 14/10/2026 sur les registres officiels,
  en RDAP (`rdap.nic.fr` pour .fr, `rdap.verisign.com` pour .com). « Non enregistré » signifie
  que le registre ne connaît pas le domaine ; cela ne garantit ni le prix ni l'absence de
  réservation entre-temps. Contrôle : `google.fr` répond « enregistré », un nom aléatoire
  répond « non enregistré ».
- **Usage existant** : recherche web sur le nom exact ; aucun usage commercial n'a été trouvé
  pour les candidats retenus.
- **Marque** : la base INPI et EUIPO n'a **pas** pu être interrogée → **« non vérifié »**
  partout. Une recherche d'antériorité sur data.inpi.fr est nécessaire avant tout dépôt.

| # | Nom | Connotation | Risque de confusion | .fr | .com | Marque INPI |
|---|---|---|---|---|---|---|
| 1 | **Le Bon Versant** | Montagne, « le bon côté » où chercher ; écho familier et positif | Faible avec les concurrents ; **clin d'œil à « leboncoin »** : légitime, mais à faire valider (marque notoire) | `lebonversant.fr` non enregistré | `lebonversant.com` non enregistré | Non vérifié |
| 2 | **La Bonne Pousse** | Timing de la poussée, vocabulaire de cueilleur | Faible ; « pousse » est aussi très utilisé en jardinage et alimentation (Pousse Pousse, Les Petites Pousses) | `labonnepousse.fr` non enregistré | `labonnepousse.com` non enregistré | Non vérifié |
| 3 | **Boletopo** | Bolet + topo : terrain, carte de relief | Faible ; centré sur les bolets alors que le produit couvre aussi trompettes, girolles et morilles | `boletopo.fr` non enregistré | `boletopo.com` non enregistré | Non vérifié |
| 4 | **Combe à Cèpes** | Terroir, combes humides des massifs ; poétique | Faible ; restreint au cèpe | `combeacepes.fr` non enregistré | `combeacepes.com` non enregistré | Non vérifié |
| 5 | **Cueilloir** | Mot français existant (outil pour cueillir) : simple, mémorisable | Faible avec les concurrents ; **nom commun**, donc marque potentiellement peu distinctive | `cueilloir.fr` non enregistré | `cueilloir.com` non enregistré | Non vérifié |
| 6 | **Fongitop** | « Fongi » (fonge) + « top » (topographie, ou « le top ») | Faible ; sonorité moins française | `fongitop.fr` non enregistré | `fongitop.com` non enregistré | Non vérifié |
| 7 | **Trouvecèpes** | Direct, très SEO (« cèpes ») | Faible ; mais **promesse de résultat** contraire au vocabulaire honnête retenu (§1), et restreint au cèpe | `trouvecepes.fr` non enregistré | `trouvecepes.com` non enregistré | Non vérifié |
| 8 | **Sylvacoin** | Sylve (forêt) + coin | Faible avec les concurrents ; **« coin » se lit « crypto-monnaie » en anglais** | `sylvacoin.fr` non enregistré | `sylvacoin.com` non enregistré | Non vérifié |

**Écartés au filtre des domaines** (les deux extensions déjà enregistrées) : *Versant*,
*Versant Nord*, *Poussée*, *Sporée*, *Combe*, *Humus*, *Litière*, *Mousseron*, *Fongeo*,
*Cépéo*, *Prospecteur*. *Sous-Bois* a son .fr libre mais son .com pris.
**Écarté au filtre de la confusion** : *MycoTopo* (domaines libres, mais le préfixe « Myco »
rapproche de Mycora et MycoDB, et du nom déjà écarté).

**Recommandation (non décisionnelle)** : **Le Bon Versant** en premier choix. Il incarne le
positionnement montagne, se retient, n'emprunte rien aux concurrents, et laisse la place aux
mots-clés dans les titres (titre de store en 28 caractères : « Le Bon Versant : champignons »). Second choix : **La
Bonne Pousse**, qui parle du timing, l'autre moitié de la promesse. **Le choix final revient au
porteur**, après recherche d'antériorité INPI. Aucun fichier ni dépôt n'a été renommé.
