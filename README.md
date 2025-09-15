# Reflex User Management App

A modular web application for managing users with interactive charts.

## Setup

```bash
# Install Reflex
pip install reflex

# Initialize database
reflex db init && reflex db migrate

# Run the app
reflex run
```

## Open App

```bash
"$BROWSER" http://localhost:3000
```

## Project Structure

```
reflex_app/
├── models/           # User data models
├── state/            # State management  
├── components/       # UI components
├── pages/            # App pages
└── reflex_app.py     # Main app
```

## Features

- Add/view/delete users
- Gender distribution charts
- Modern responsive UI
- Modular architecture

## Development

```bash
# Development mode with auto-reload
reflex run --env dev

# Export for production
reflex export
```

Built with [Reflex](https://reflex.dev) 🚀

