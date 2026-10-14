# 00 — Synthèse exécutive

*Étude de marché myco-map, 14 octobre 2026. Six documents :
[01 Audit](01-audit-projet.md) · [02 Benchmark](02-benchmark-concurrentiel.md) ·
[03 Marché](03-etude-marche.md) · [04 Critique](04-critique-projet.md) ·
[05 Roadmap](05-roadmap-monetisation.md). Le contexte marketing réutilisable est dans
[`.agents/product-marketing.md`](../../.agents/product-marketing.md).*

## Cadre retenu par le porteur (décisions du 14/10/2026)

- **Ambition** : revenu d'appoint (quelques centaines à quelques milliers d'€/an), sans levée
  de fonds ni recrutement.
- **Produit** : une **carte de prospection** pour connaître les coins à champignons, et c'est
  tout. **Aucune identification**, même pédagogique. Bonnes pratiques de cueillette incluses.
- **Cible** : B2C, zones riches en champignons, **accessible aux novices**.
- **Modèle** : **payant d'abord**, gratuit très restreint ; **produit fini uniquement, pas de
  prévente**.
- **Temps** : développement intensif **jusqu'à la saison des morilles 2027**, puis **moins de
  15 h/semaine**.
- **Coûts** : **scénario minimal**, montée ligne par ligne ; relecture juridique non chiffrée.
- **Statut** : **micro-entreprise à créer** (régime classique).
- **Code** : **propriétaire** (pas d'open source) ; ODbL : **option A** (publier les couches
  dérivées d'OSM).
- **Nom** : « Myco Map » **écarté** ; shortlist proposée (05 §9).

## Les 10 constats clés

1. **Le projet** est un prototype technique solide et honnête (une semaine de développement,
   moteur explicable, relief 5 m, LIDAR HD, 14 jours de projection), limité à une emprise
   grenobloise. Il n'a **ni déploiement, ni utilisateurs, ni validation empirique, ni couche
   produit** (comptes, paiement, hors-ligne, juridique). → [01](01-audit-projet.md)
2. **Le marché est encombré.** On compte au moins 10 cartes françaises de prévision et de
   biotopes en 2026. Les prix vont de **0 €** (Champiscope, Waldschatzfinder, Boletik en 2026)
   à **1 €/mois** (Mapignon), **4,99–9,99 €/mois** (Mycora), **9,99 €/an** (Boletik 2027),
   **14,90 €/an par carte** (The Mycologist), **48 €/an** (Chasseurs de champignons) et
   **39,99 ou 59,99 €/an par région** (Champi, non vérifié). → [02](02-benchmark-concurrentiel.md)
3. **Trois trous réels mais étroits** : la **précision en montagne** (aucun concurrent observé ne
   revendique LIDAR HD ou un MNT à 5 m) ; la **preuve** (seul Boletik publie une validation, ×2,8
   sur GBIF) ; le **« ai-je le droit de cueillir ici ? »** (forêts publiques, arrêtés).
4. **Les zones riches, mesurées** : sur les occurrences GBIF des 5 taxons ciblés, les
   départements en tête sont le **Jura, les Hautes-Pyrénées et l'Isère (3ᵉ)**, puis le Doubs et
   la Savoie / Haute-Savoie. L'emprise actuelle est donc bien placée. Ces données mesurent
   l'effort d'observation, pas la productivité. → [03 §3](03-etude-marche.md)
5. **Taille** : SAM France ≈ **0,1 à 4 M€/an** (confiance faible). SOM réaliste pour les Alpes
   du Nord en solo ≈ **quelques centaines à quelques milliers d'€/an**, ce qui correspond à
   l'objectif. Attractivité **27/50 : « valider d'abord »**. → [03 §7–8](03-etude-marche.md)
6. **Bloquants avant de faire payer** : validation du score, **licences commerciales** (l'API
   Open-Meteo gratuite est non commerciale, les tuiles OSM interdisent le hors-ligne),
   **avertissement « la carte ne dit rien de la comestibilité »** et bonnes pratiques de
   cueillette, déploiement de production, paiement, hors-ligne.
   → [04](04-critique-projet.md)
7. **Le périmètre « prospection seule » est le bon** : l'identification par photo plafonne à
   35–49 % de réussite, l'Anses s'en méfie, et la 1ʳᵉ cause d'intoxication en 2024 est une
   confusion avec la girolle. Le produit ne donne aucun avis sur un champignon cueilli ; la
   promesse « novice » repose sur la simplicité de la carte et les bonnes pratiques.
   → [04 §5.1](04-critique-projet.md)
8. **Code fermé, deux conséquences.** (a) Le dépôt GitHub est **encore public sous MIT** : il faut
   le passer en privé **avant de pousser cette étude**. Le code déjà publié reste sous MIT pour
   qui l'a copié. (b) L'**ODbL** impose de publier les couches dérivées d'OpenStreetMap, ou leur
   méthode de dérivation, dès qu'un produit qui en est issu est public : **option A retenue**,
   on publie ces seules couches. → [04 §9](04-critique-projet.md)
9. **Coûts et micro-entreprise.** Scénario minimal retenu : **≈ 93 € HT/an** (VPS ~6 €/mois,
   SQLite, R2 gratuit, météo Météo-France ouverte, Protomaps auto-hébergé, services gratuits),
   soit **≈ 140 à 190 €/an payés** en ajoutant la TVA non récupérable (franchise) et le
   médiateur de la consommation obligatoire (30 à 80 €/an, non vérifié). Après Stripe et ~21 %
   de cotisations, un pass à 19 € rapporte **≈ 14,40 €** : **≈ 10 à 14 passes** couvrent les
   coûts. Scénario confort : ≈ 840 à 1 065 €/an (≈ 58 à 74 passes). Charge : **5 à 10 h/semaine
   en saison**, 1 à 3 h/semaine hors saison. → [05 §3.4 et §4](05-roadmap-monetisation.md)
10. **Nom** : 8 propositions avec domaines .fr et .com non enregistrés au 14/10/2026 ;
    recommandation **Le Bon Versant**, puis **La Bonne Pousse**. Les marques ne sont pas
    vérifiées à l'INPI. → [05 §9](05-roadmap-monetisation.md)

## Recommandation

**Positionnement** : dans la catégorie que les clients cherchent (« coins à champignons »),
être **la carte de prospection des massifs de montagne** ; un gros poisson dans une petite
mare (Alpes du Nord d'abord, puis un massif par an). Pas la France entière.

**Offre** : un secteur vitrine gratuit et un bulletin de pousse comme seul gratuit ; **Pass
Saison massif à 19 €** (à tester entre 15 et 25 €) ; **Pass tous massifs à 29 €** ; carte
imprimée hors saison à partir de 2028. Remboursement sous 14 jours, **pas de renouvellement
automatique par défaut**. **Lancement du produit fini** début avril 2027, sans prévente ni
remise « fondateur ».

**Roadmap** :

| Phase | Période | Contenu | Critère |
|---|---|---|---|
| 0 | Maintenant → mi-nov. 2026 | Dépôt privé + licence propriétaire, validation GBIF, 10 entretiens, choix du nom et des domaines, page d'attente sans paiement | Écart avec le hasard ≥ ~1,5, sinon re-calibrage |
| 1 | Mi-nov. 2026 → fév. 2027 | Produit fini : production en scénario minimal, tuiles statiques + météo planifiée, Météo-France, Protomaps, PWA hors-ligne, mode simple, bonnes pratiques et forêts publiques, conformité ODbL (A), Stripe, Alpes du Nord | 6 à 9 semaines de travail sur ~15 semaines calendaires |
| 1b | Mars 2027 | Bêta fermée gratuite du produit fini ; création de la micro-entreprise, médiateur, CGU/CGV, INPI | La moitié des testeurs paierait au prix annoncé |
| 2 | Avr.–mai 2027 | **Lancement**, saison des morilles ; passage sous 15 h/semaine | ≥ 15 passes au 31/05/2027, sinon revoir l'offre |
| 3 | Juin–nov. 2027 | Bulletin automatique, SEO par massif, expositions | ≥ 50 passes au 30/11/2027 ; < 20 → arrêter ou repositionner |
| 4 | 2028+ | +1 massif par an (Jura / Doubs, puis Pyrénées), carte imprimée | — |

## Questions encore ouvertes

1. **Budget de relecture juridique** (CGU/CGV, lecture de l'ODbL) : non chiffré.
2. **Choix final du nom** dans la shortlist, après recherche d'antériorité INPI.

## Incertitudes principales

- **Nombre de cueilleurs en France** : aucune statistique fiable (le chiffre « 3 M » n'est pas
  vérifié).
- **Volumes de recherche** et **métriques SEO** des concurrents : non disponibles (aucun outil
  connecté).
- **Chiffres d'affaires** concurrents : aucun n'est publié ; audiences auto-déclarées.
- **Prix** non vérifiés : Champi (39,99 ou 59,99 €/an), Sporecast en euros, Expert de
  Cueillette, Coins à champignons, domaine .fr (~7,79 € selon une source non officielle),
  médiateur de la consommation (30 à 80 €/an), dépôt INPI (~190 €), taux de cotisations
  (sources secondaires, à confirmer sur urssaf.fr). Les
  prix Hetzner viennent d'un comparateur tiers. Le prix Open-Meteo (29 $/mois) vient du blog
  de l'éditeur, la page de prix en ligne n'affichant pas les montants.
- **Licences** à confirmer : LIDAR HD (fiche produit), EcoDataCube, Charm-50 (source officielle),
  données ouvertes Météo-France, conditions hors-ligne des fonds IGN.
- **Efficacité du modèle** : inconnue tant que la validation de la phase 0 n'est pas faite.
- **Marques** : aucune recherche INPI ou EUIPO n'a pu être faite pour la shortlist de noms.

## Sources principales

**Concurrents et prix** (relevés du 13 au 14/10/2026)
- Mycora : <https://www.mycora.fr/>, <https://www.mycora.fr/pricing>, <https://www.mycora.fr/champignons-en-ce-moment>
- Champi : <https://champimap.com/>, <https://play.google.com/store/apps/details?id=com.champi>
- Chasseurs de champignons : <https://www.chasseursdechampignons.com/>, <https://www.chasseursdechampignons.com/blog/divers/les-avis-sur-chasseurs-de-champignons/>, <https://fr.trustpilot.com/review/www.chasseursdechampignons.com>
- Test terrain : <https://www.champignons-passion.com/conseils/avis-chasseursdechampignons-test-terrain-cartes-biotope/>
- The Mycologist : <https://themycologist.app/>, <https://themycologist.app/abonnement>
- Boletik : <https://boletik.fr/>
- Champiscope : <https://champiscope.fr/>, <https://champiscope.fr/carte-des-champignons>
- Mapignon : <https://mapignon.fr/>
- Waldschatzfinder : <https://waldschatzfinder.de/?lang=fr>
- Sporecast : <https://apps.apple.com/gb/app/sporecast-mushroom-map/id6745700034>
- Expert de Cueillette : <https://expertdecueillette.fr/>
- les-champignons.fr : <https://www.les-champignons.fr/ca-pousse/>
- Les Cartes Terroirs : <https://lescartesterroirs.fr/>
- Coins à champignons : <https://coins-a-champignons.fr/carte-champignons-gratuite/>
- champi-aix : <https://github.com/rgcomgraphic-13/champi-aix>
- Picture Mushroom : <https://apps.apple.com/FR/app/id1474578078>, <https://screensdesign.com/showcase/picture-mushroom-identifier>
- Champignouf : <https://apps.apple.com/fr/app/champignouf/id1227854971>, <https://www.presse-citron.net/telecharger/loisirs/science/champignouf.html>
- Shroomify : <https://apps.apple.com/us/app/shroomify-champignons/id1490594715?l=fr-FR>
- iNaturalist : <https://en.wikipedia.org/wiki/INaturalist>
- MycoDB : <https://www.mycodb.fr/>
- Iphigénie : <https://apps.apple.com/fr/app/iphig%C3%A9nie-la-carto-en-rando/id350346756>
- AllTrails : <https://apps.apple.com/app/id405075943> ; onX : <https://onxmaps.com/backcountry/app/pricing>

**Marché, santé, réglementation**
- Anses, intoxications : <https://www.anses.fr/fr/content/cueillette-des-champignons-vigilance-face-aux-risques-dintoxications>
- Fiabilité des applis (Hodgson et al. 2023) : <https://www.les-champignons.fr/champignons/application-reconnaissance-champignons/>
- UFC-Que Choisir : <https://www.quechoisir.org/actualite-cueillette-des-champignons-pourquoi-il-faut-eviter-les-applications-n172056/>
- ANCT : <https://lesbases.anct.gouv.fr/ressources/cueillette-des-champignons-bien-utiliser-cartes-et-applications-et-connaitre-leurs-limites>
- Pratique en Europe : <https://www.researchgate.net/publication/228427142_Participation_in_mushroom_picking_in_Finland>, <https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2024.1474624/full>
- Code forestier, réponse ministérielle : <https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE9341.pdf>
- Presse : <https://www.smry.fr/articles/157197-cartes-payantes-avec-la-promesse-de-trouver-des-kilos-de-champignons>, <https://www.consoglobe.com/?p=260958>
- GBIF (API publique, 14/10/2026) : <https://api.gbif.org/v1/occurrence/search>
- OpenObs : <https://openobs.mnhn.fr/redirect/inpn/taxa/29388?view=list>
- Taux de boisement : <https://www.data.gouv.fr/datasets/taux-de-boisement-1>
- LIDAR HD (MNH) : <https://www.data.gouv.fr/datasets/mnh-lidar-hd/informations>
- Forêts publiques ONF : <https://www.data.gouv.fr/datasets/forets-publiques-diffusion-publique/informations>

**Coûts (relevés du 14/10/2026)**
- Hetzner (tiers) : <https://costgoat.com/pricing/hetzner> ; OVHcloud : <https://blog.ovhcloud.com/en/posts/pricing-evolution-of-public-cloud-bare-metal-and-vps-at-ovhcloud/>
- Stripe : <https://stripe.com/fr/pricing> ; Cloudflare R2 : <https://developers.cloudflare.com/r2/pricing/> ; Bunny : <https://bunny.net/pricing/cdn/>
- Resend : <https://resend.com/pricing> ; UptimeRobot : <https://uptimerobot.com/pricing/> ; Sentry : <https://sentry.io/pricing/>
- MapTiler : <https://www.maptiler.com/cloud/pricing/> ; Protomaps : <https://docs.protomaps.com/basemaps/downloads>
- Scaleway (base managée) : <https://www.scaleway.com/fr/tarifs/managed-databases>
- Météo-France AROME (Licence Ouverte) : <https://data.gouv.fr/en/datasets/donnees-du-modele-atmospherique-arome-a-aire-limitee-a-haute-resolution>

**Micro-entreprise et marque**
- Cotisations : <https://www.portail-autoentrepreneur.fr/academie/statut-auto-entrepreneur/cotisations>
- Franchise de TVA : <https://comptabook.fr/tva/seuil-franchise-tva-2026/>
- Médiation de la consommation : <https://www.portail-autoentrepreneur.fr/academie/creation-auto-entreprise/mediation-consommation>
- Dépôt INPI : <https://www.captaincontrat.com/articles-creation-entreprise/cout-depot-marque-inpi>
- Registres de domaines (RDAP) : <https://rdap.nic.fr/>, <https://rdap.verisign.com/com/v1/>

**Licences et conformité**
- ODbL 1.0 : <https://opendatacommons.org/licenses/odbl/1-0/>
- Open-Meteo : <https://open-meteo.com/en/pricing>, <https://openmeteo.substack.com/p/api-subscriptions-for-commercial>
- Tuiles OSM : <https://operations.osmfoundation.org/policies/tiles/>
- Overpass : <https://wiki.openstreetmap.org/wiki/Overpass_API>
- Copernicus : <https://land.copernicus.eu/en/data-policy>
- Charm-50 : <https://data.gouv.fr/en/datasets/cartes-geologiques-departementales-a-1-50-000-bd-charm-50>
- IGN Licence Ouverte (2021) : <https://www.ffrandonnee.fr/s-informer/actualites/ign-les-donnees-desormais-libres-et-gratuites>
- CNIL, géolocalisation : <https://cnil.fr/fr/geolocalisation-applications-mobiles-quelles-regles>
