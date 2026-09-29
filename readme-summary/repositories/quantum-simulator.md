# quantum-simulator

**Summary**

The *quantum-simulator* repository provides a complete, ready‑to‑run configuration for exposing the BestBrain application via Nginx on a custom domain. The core purpose is to automate the generation of an Nginx server block from environment variables defined in `.env`, allowing users to control:

- **Domain name** (`<DOMAIN>`) – sourced from `NGINX_DOMAIN` → `DOMAIN` → `CLUSTER_DOMAIN` (defaulting to `localhost` if none are set).
- **Application port** (`<APP_PORT>`) – sourced from `NGINX_APP_PORT` → `PORT` → `CLUSTER_PORT` (defaulting to `8080`).

The rendered configuration is saved as `<domain>.conf` in the `nginx/` directory, making it modular and easy to update by simply re‑running:

```bash
python -m nginx.render_nginx_conf
```

Installation steps include:

1. Installing Nginx and Certbot on Ubuntu/Debian.
2. Configuring site files (`sites-available/bm`) via the provided `startup.sh --init` script, which automatically copies the generated config to `/etc/nginx/sites-enabled`.
3. Verifying with `sudo nginx -t` and reloading Nginx.

TLS certificates are obtained using Certbot’s Nginx plugin:

```bash
sudo certbot --nginx -d bestbrain.tech -d www.bestbrain.tech
```

Additional features covered in the README are:

- Extended request timeouts (600 s) for handling long‑running operations.
- WebSocket support via a `/qf-sim/` location block, enabling real‑time communication with Daphne/Uvicorn servers on the configured port.
- A reload sequence after deployments to ensure all services restart correctly.

**KEYWORDS:** quantum simulator, Nginx configuration, environment variables, domain/port control, Certbot TLS setup, WebSocket support, deployment scripts.
