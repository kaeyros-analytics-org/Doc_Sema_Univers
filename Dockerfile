# Étape 1 : construire la documentation
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y git build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install sphinx sphinx-rtd-theme \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Build EN et FR
RUN . venv/bin/activate && sphinx-build -b html docs/en build/html/en
RUN . venv/bin/activate && sphinx-build -b html docs/fr build/html/fr

# Étape 2 : servir avec Nginx
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/build/html /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
