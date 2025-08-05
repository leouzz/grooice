# Grooice

Prototype grocery receipt tracker with a Django REST backend and React frontend.

## Open Data
- [Open Food Facts](https://world.openfoodfacts.org/) provides a large open database of food products, including many sold on the Italian market.

## Backend
Located in [`backend/`](backend/), the Django project exposes a basic `/api/items/` endpoint.

## Frontend
Located in [`frontend/`](frontend/), the React app is bootstrapped with Vite and styled with Tailwind CSS.
The demo component fetches items from the Django API and lists them.
