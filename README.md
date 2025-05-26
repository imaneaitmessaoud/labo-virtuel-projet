# labo-virtuel-projet
Projet de laboratoire virtuel éducatif
#  Projet : Laboratoire Virtuel pour l'Éducation à Distance

##  Objectif
Concevoir un environnement de laboratoire virtuel accessible à distance, adapté aux cours pratiques (réseaux, programmation, IA, BD…).

##  Technologies utilisées
- VirtualBox + Ubuntu 22.04
- Python / VS Code
- GNS3 / Wireshark
- PostgreSQL
- Octave
- Serveur HTTP Python
- SSH (accès distant)

---

## TPs réalisés

###  TP1 – Réseau (Ping entre deux PC dans GNS3)

<img width="355" alt="image" src="https://github.com/user-attachments/assets/5d3147b2-3c0b-4b4a-a148-788c9a754b94" />

###  TP2 – Cybersécurité (Scan Nmap)
<img width="391" alt="image" src="https://github.com/user-attachments/assets/9a3e4af4-52be-4110-992b-c321e03f60f2" />


###  TP3 – Programmation Python
<img width="330" alt="image" src="https://github.com/user-attachments/assets/fbbbb514-a718-4765-afd9-44264f108b89" />
<img width="416" alt="image" src="https://github.com/user-attachments/assets/7b04b125-e170-402f-a996-5324a2e1baf4" />


###  TP4 – PostgreSQL : Requête SQL
<img width="322" alt="image" src="https://github.com/user-attachments/assets/ff51c89b-4e3e-4025-af83-7f9e66864daa" />

<img width="243" alt="image" src="https://github.com/user-attachments/assets/f05e1e91-a6ac-48c6-a4fc-75e9e059cb4c" />


###  TP5 – IA : Prédiction linéaire
<img width="416" alt="image" src="https://github.com/user-attachments/assets/6e49ebfc-5e3a-4e03-9862-9e31f41ad201" />


###  TP6 – Électronique (Octave)
<img width="415" alt="image" src="https://github.com/user-attachments/assets/99cc15c7-6fdc-430d-bff0-1c9c0e0c7ec8" />


### TP7 – Serveur Web local
<img width="415" alt="image" src="https://github.com/user-attachments/assets/fee0f01d-a4bd-42e8-a60d-79c4b4c28c05" />

### TP8 – Versionnage et publication du projet avec Git & GitHub
<img width="603" alt="image" src="https://github.com/user-attachments/assets/23390554-8973-48c4-9ab6-c0554a33b675" />
<img width="644" alt="image" src="https://github.com/user-attachments/assets/499a0c35-482e-40ec-98ce-3aa44a560918" />

### TP9 – Déploiement d’un serveur web local dans la VM Ubuntu

<img width="415" alt="image" src="https://github.com/user-attachments/assets/e8a207a0-41c3-49df-8d7a-61808c270654" />

 Objectif
Créer un service web pédagogique minimal (page HTML) hébergé dans la machine virtuelle Ubuntu, accessible depuis un poste distant (Windows) via navigateur, en simulant un laboratoire web.

###  Outils utilisés
Ubuntu 22.04 (VirtualBox)

Python 3 (http.server)

Navigateur (Chrome sous Windows)

Réseau VM en mode "ponté"

IP réelle de la VM : 192.168.100.68

###  Étapes réalisées
### Création de la page HTML :
mkdir ~/tp9_web
cd ~/tp9_web
nano index.html
### Contenu :
html
Copy
Edit
<h1>Bienvenue sur notre labo </h1>
<p>Ce site est hébergé sur une VM Ubuntu dans un labo virtuel.</p>

### Lancement du serveur web local :
python3 -m http.server 8080

### Accès à la page depuis Windows :
http://192.168.100.68:8080



##  TP10 – Connexion distante à la VM Ubuntu via VS Code Remote SSH

<img width="415" alt="image" src="https://github.com/user-attachments/assets/84fb74eb-d7df-43ba-ac79-b8be044b09f1" />


###  Objectif
Permettre à un étudiant de se connecter à une machine Ubuntu virtuelle à distance, depuis son poste Windows, via un environnement de développement professionnel (VS Code).

---

###  Outils utilisés
- Visual Studio Code (sous Windows)
- Extension officielle **Remote - SSH**
- VM Ubuntu 22.04 avec `openssh-server`
- Adresse IP de la VM : `192.168.100.68`

---

### 🛠 Étapes réalisées
1. Installation de l’extension **Remote - SSH** dans VS Code
2. Configuration de la connexion :
   ```bash
   Host vm-labo
       HostName 192.168.100.68
       User imane
       RemoteCommand bash


   
---

###  Tâche 3 – Connexion SSH à distance depuis Windows
<img width="415" alt="image" src="https://github.com/user-attachments/assets/b579e281-a727-4ad7-93b2-107411f33daa" />


---

##  Rapport
Le rapport final est disponible ici :
(https://cours.itformation.com/mod/assign/view.php?id=807)

---

## Réalisé par :
**Kaoutar Belail**

**Imane Ait Messaoud**

