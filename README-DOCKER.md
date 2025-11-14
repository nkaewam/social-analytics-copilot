# Docker Setup for Postgres

This project includes a Docker Compose configuration to run a local Postgres database for development and testing.

## Quick Start

1. **Set environment variables** (or use defaults):
   ```bash
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5432
   export POSTGRES_DB=campaign_db
   export POSTGRES_USER=campaign_user
   export POSTGRES_PASSWORD=campaign_password
   ```

2. **Start the Postgres container**:
   ```bash
   docker-compose up -d
   ```

3. **Verify it's running**:
   ```bash
   docker-compose ps
   ```

4. **Load sample data** (optional):
   ```bash
   # Copy CSV files into the container or use psql from your host
   docker-compose exec postgres psql -U campaign_user -d campaign_db -c "\COPY campaigns FROM '/path/to/sample_data/postgres_campaigns.csv' WITH CSV HEADER;"
   ```

## Environment Variables

The docker-compose.yml uses these environment variables (with defaults shown):

- `POSTGRES_HOST` (default: `localhost`) - Database host
- `POSTGRES_PORT` (default: `5432`) - Database port
- `POSTGRES_DB` (default: `campaign_db`) - Database name
- `POSTGRES_USER` (default: `campaign_user`) - Database user
- `POSTGRES_PASSWORD` (default: `campaign_password`) - Database password

**Note**: For production, use a `.env` file or set these as environment variables with secure values.

## Database Schema

The database schema is automatically initialized when the container is first created. The init script (`init-db/01-init-schema.sql`) creates:

- `campaigns` - Campaign operational data
- `creatives` - Creative metadata and approval status
- `campaign_status` - Real-time campaign status

See `sample_data/README.md` for detailed schema information.

## Loading Sample Data

After starting the container, you can load the sample CSV files:

```bash
# Connect to the database
docker-compose exec postgres psql -U campaign_user -d campaign_db

# Or load data directly
docker-compose exec postgres psql -U campaign_user -d campaign_db -c "\COPY campaigns FROM STDIN WITH CSV HEADER;" < sample_data/postgres_campaigns.csv
```

Alternatively, copy the CSV files into the container first:

```bash
docker cp sample_data/postgres_campaigns.csv campaign-postgres:/tmp/
docker-compose exec postgres psql -U campaign_user -d campaign_db -c "\COPY campaigns FROM '/tmp/postgres_campaigns.csv' WITH CSV HEADER;"
```

## Connecting from Host

You can connect to the database from your host machine:

```bash
psql -h localhost -p 5432 -U campaign_user -d campaign_db
```

Or using a connection string:
```
postgresql://campaign_user:campaign_password@localhost:5432/campaign_db
```

## Stopping the Container

```bash
# Stop the container
docker-compose down

# Stop and remove volumes (WARNING: deletes all data)
docker-compose down -v
```

## Data Persistence

Data is persisted in a Docker volume named `postgres_data`. This means your data will survive container restarts. To completely remove all data, use `docker-compose down -v`.

## Troubleshooting

### Container won't start
- Check if port 5432 is already in use: `lsof -i :5432`
- Check Docker logs: `docker-compose logs postgres`

### Connection refused
- Ensure the container is running: `docker-compose ps`
- Check the health status: `docker-compose ps` should show "healthy"
- Verify environment variables match your configuration

### Permission errors
- Ensure the init script has proper permissions: `chmod +x init-db/*.sql`
- Check Docker volume permissions

