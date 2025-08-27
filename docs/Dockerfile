# Étape 1 : construire la documentation
FROM python:3.12-slim AS builder

# Installer pip et dépendances système
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier du projet
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Créer un environnement virtuel et installer Sphinx
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install sphinx sphinx-rtd-theme \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Générer la documentation HTML
RUN . venv/bin/activate && sphinx-build -b html docs/ build/html

# Étape 2 : servir la doc avec Nginx
FROM nginx:alpine

# Supprimer le contenu par défaut
RUN rm -rf /usr/share/nginx/html/*

# Copier la doc générée
COPY --from=builder /app/build/html /usr/share/nginx/html

# Exposer le port
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
