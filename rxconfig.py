import os

import reflex as rx

PORT_BACKEND = int(os.getenv("PORT", "8000"))          # backend
PORT_FRONTEND = int(os.getenv("FRONTEND_PORT", "3000"))  # frontend
IN_CODESPACES = os.getenv("CODESPACES") == "true"

API_URL = (
    # external URL that the browser should use to talk to the backend
    f"https://{os.environ['CODESPACE_NAME']}-{PORT_BACKEND}.app.github.dev"
    if IN_CODESPACES
    else f"http://localhost:{PORT_BACKEND}"
)

config = rx.Config(
    app_name="reflex_app",
    api_url=API_URL,              # <- important for websocket endpoint
    backend_host="0.0.0.0",       # <- listen on all interfaces inside container
    backend_port=PORT_BACKEND,
    frontend_host="0.0.0.0",
    frontend_port=PORT_FRONTEND,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url="sqlite:///reflex_app.db",
)
