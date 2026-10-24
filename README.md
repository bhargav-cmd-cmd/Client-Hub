# ClientHub

A React client-management workspace with an existing FastAPI authentication service and PostgreSQL database.

## Run the website

```powershell
cd frontend
npm install
npm run dev
```

Open http://localhost:5173/demo. The demo works without Docker or an account. It starts empty and includes searchable lists, client and project creation, project status changes, document records, activity history, and JSON export. Changes are stored in this browser under `clienthub-workspace-v2`; they are not saved to PostgreSQL. Project progress is an illustrative value based on status.

The website uses a neutral white, grey, and charcoal palette throughout. Previous colour-demo URLs redirect to `/demo`.

## Run the complete existing stack

For local registration and login without Docker, run this from the project directory in a separate PowerShell terminal:

```powershell
.\start-backend.ps1
```

This runs the existing FastAPI account service at `http://127.0.0.1:8000` with a local SQLite database at `backend/clienthub-local.db`. Keep it running while signing up or logging in. Accounts persist across restarts. The Docker setup continues to use PostgreSQL; accounts in these databases are separate.

With Docker Desktop running, execute from this directory:

```powershell
docker compose up --build
```

- Website: http://localhost:5173
- Login: http://localhost:5173/login
- API documentation: http://localhost:8000/docs
- PostgreSQL: localhost:5432

Login and registration use the existing backend. Client, project, and document management currently use the browser workspace store, even after signing in; the backend currently exposes authentication/user routes only. Document records do not upload files. Local workspace data is shared by accounts using that browser and is unsuitable for sensitive records.

## Production build

```powershell
cd frontend
npm run build
```

Build output is written to `frontend/dist`. The Docker Compose configuration is for local development. No hosted deployment is configured.

The workspace contains no preloaded clients, projects, documents, or activity. The previous fictional demo records are removed automatically while preserving records you added. Projects and document records can be personal, without a client.
