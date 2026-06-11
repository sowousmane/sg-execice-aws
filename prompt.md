Agis comme un Staff DevOps / Platform Engineer spécialisé AWS, Docker, GitHub Actions et observabilité.

Contexte :

* Application Web FastAPI
* Base de données PostgreSQL
* Reverse proxy Traefik
* Observabilité : Grafana, Loki, Promtail
* Hébergement sur une instance EC2 AWS
* Domaine géré par Cloudflare (DNS uniquement)
* Code source sur GitHub
* Images Docker stockées sur Docker Hub

Objectifs :

1. Définir une architecture de production simple mais professionnelle.
2. Définir une architecture CI/CD GitHub Actions.
3. Exécuter les tests Pytest en local et dans la CI.
4. Vérifier la qualité du Dockerfile (lint).
5. Scanner les images Docker après build et push.
6. Déployer automatiquement sur EC2 après validation sur la branche main.
7. Éviter toute intervention manuelle du type :

   * ssh EC2
   * git pull
   * docker compose up
8. Prévoir la gestion des secrets.
9. Prévoir les sauvegardes PostgreSQL.
10. Prévoir les logs et métriques applicatives.

Contraintes :

* Docker Compose uniquement (pas Kubernetes).
* Coût minimal.
* Une seule instance EC2.
* Déploiement automatique via GitHub Actions.
* Rolling update ou redéploiement avec interruption minimale.
* Possibilité future de migrer vers ECS.

Livrables attendus :

1. Diagramme d'architecture ASCII.
2. Structure du dépôt.
3. docker-compose.production.yml.
4. GitHub Actions CI.
5. GitHub Actions CD.
6. Gestion des secrets.
7. Monitoring et alerting.
8. Plan de sauvegarde PostgreSQL.
9. Recommandations sécurité.
10. Schéma complet du workflow développeur → production.
