# GenAI Toolbox Setup for Database Queries

This project uses [genai-toolbox](https://github.com/googleapis/genai-toolbox) (MCP Toolbox for Databases) to query BigQuery and Postgres databases.

## Setup Steps

### 1. Download genai-toolbox

Download the toolbox binary for your platform:

```bash
# For Linux AMD64
export OS="linux/amd64"
curl -O https://storage.googleapis.com/genai-toolbox/v0.20.0/$OS/toolbox
chmod +x toolbox

# For macOS AMD64
export OS="darwin/amd64"
curl -O https://storage.googleapis.com/genai-toolbox/v0.20.0/$OS/toolbox
chmod +x toolbox

# For macOS ARM64 (Apple Silicon)
export OS="darwin/arm64"
curl -O https://storage.googleapis.com/genai-toolbox/v0.20.0/$OS/toolbox
chmod +x toolbox
```

### 2. Configure tools.yaml

Edit `tools.yaml` and replace `YOUR_PROJECT_ID` with your actual Google Cloud project ID:

```yaml
sources:
  campaign-bigquery:
    kind: bigquery
    project: your-actual-project-id  # Replace this
    location: us  # Or asia-southeast1 for Thailand
```

### 3. Authenticate with Google Cloud

```bash
gcloud auth application-default login
```

Ensure your credentials have BigQuery permissions:
- `roles/bigquery.dataViewer` (to read data)
- `roles/bigquery.jobUser` (to run queries)

### 4. Start the Toolbox Server

**Option A: HTTP Mode (Recommended for POC)**

```bash
./toolbox --tools-file tools.yaml
```

The server will start on `http://127.0.0.1:5000` by default. Keep this running in a separate terminal.

**Option B: Stdio Mode (Alternative)**

If you prefer stdio mode (toolbox runs as subprocess), set:
```bash
export TOOLBOX_USE_STDIO=true
```

Then ensure the toolbox binary is in your PATH.

### 5. Verify Setup

The internal_data_agent uses ADK's `MCPToolset` to automatically connect to the toolbox server and load tools. When you run `adk web`, the agent will:
- Connect to the toolbox server (HTTP or stdio based on configuration)
- Discover all tools defined in `tools.yaml`
- Make them available to the agent

The tool name will match what's defined in `tools.yaml` (e.g., `bigquery-execute-sql`).

## Troubleshooting

- **Connection refused**: Make sure the toolbox server is running
- **Authentication errors**: Run `gcloud auth application-default login` again
- **Permission denied**: Check your GCP IAM permissions for BigQuery
- **Tool not found**: Verify the tool name in `tools.yaml` matches what's used in `internal_data_agent/agent.py`

## References

- [genai-toolbox GitHub](https://github.com/googleapis/genai-toolbox)
- [BigQuery Source Configuration](https://googleapis.github.io/genai-toolbox/resources/sources/bigquery/)
- [BigQuery SQL Tool](https://googleapis.github.io/genai-toolbox/resources/tools/bigquery/bigquery-sql/)

