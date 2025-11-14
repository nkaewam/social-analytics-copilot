# Configuration Guide

This document explains how to configure and run the Insight Copilot multi-agent system.

## Prerequisites

1. **Python 3.13+**
2. **Google ADK** (installed via dependencies)
3. **genai-toolbox** server (for database queries)
4. **Google Cloud credentials** (for BigQuery access)

## Installation

```bash
# Install dependencies
pip install -e .

# Or using uv (recommended)
uv sync
```

## Configuration Steps

### 1. Set Up genai-toolbox

See `TOOLBOX_SETUP.md` for detailed instructions.

Quick setup:
```bash
# Download toolbox binary
export OS="darwin/arm64"  # Adjust for your OS
curl -O https://storage.googleapis.com/genai-toolbox/v0.20.0/$OS/toolbox
chmod +x toolbox

# Configure tools.yaml (edit YOUR_PROJECT_ID)
# Then start server (HTTP mode - recommended)
./toolbox --tools-file tools.yaml

# Or use stdio mode (alternative)
export TOOLBOX_USE_STDIO=true
```

**Note:** The internal_data_agent uses ADK's `MCPToolset` to connect to genai-toolbox. It automatically discovers and loads tools from the MCP server.

### 2. Configure Google Cloud Authentication

```bash
gcloud auth application-default login
```

Ensure your account has BigQuery permissions:
- `roles/bigquery.dataViewer`
- `roles/bigquery.jobUser`

### 3. Set Environment Variables (Optional)

```bash
# Toolbox server URL (default: http://127.0.0.1:5000)
export TOOLBOX_SERVER_URL="http://127.0.0.1:5000"

# Google API Key (for Gemini models and google_search)
export GOOGLE_API_KEY="your-api-key"
```

### 4. Configure tools.yaml

Edit `tools.yaml` and replace:
- `YOUR_PROJECT_ID` with your GCP project ID
- `location` if needed (e.g., `asia-southeast1` for Thailand)

## Running the Agent

### Option 1: ADK Web UI (Recommended for POC)

```bash
adk web
```

Then select the `insight_copilot` agent from the UI.

### Option 2: Programmatic Access

```python
from orchestrator.agent import insight_copilot

# Use the agent in your code
response = insight_copilot.run("What's trending on smart home in Thailand?")
```

## Agent Architecture

The system consists of:

1. **InsightCopilot** (root agent) - `orchestrator/agent.py`
   - Coordinates all sub-agents
   - Exported as `root_agent` for ADK UI

2. **SocialMediaAgent** - `social_media_agent/agent.py`
   - Uses `google_search` tool
   - Analyzes Thai social media trends

3. **InternalDataAgent** - `internal_data_agent/agent.py`
   - Uses genai-toolbox for BigQuery queries
   - Analyzes campaign performance

4. **CreativeAgent** - `creative_agent/agent.py`
   - Analyzes ad images using Gemini multimodal
   - Extracts visual patterns

## Database Schema

Ensure your BigQuery/Postgres has these tables:

- `campaigns` (campaign_id, name, brand, objective, tags, start_date, end_date)
- `campaign_metrics_daily` (campaign_id, date, impressions, clicks, spend, conversions, roas, platform, audience_segment)
- `creatives` (creative_id, campaign_id, image_url, platform, format, audience_segment)

See `POC_SCOPE.md` for detailed schema.

## Troubleshooting

### Toolbox Server Connection Error

```
Error: Could not connect to genai-toolbox server
```

**Solution:**
1. **For HTTP mode:**
   - Check if toolbox server is running: `./toolbox --tools-file tools.yaml`
   - Verify URL matches `TOOLBOX_SERVER_URL` environment variable (default: http://127.0.0.1:5000)
   - Check firewall/network settings
   - Verify the server is accessible: `curl http://127.0.0.1:5000/health` (if health endpoint exists)

2. **For stdio mode:**
   - Ensure `TOOLBOX_USE_STDIO=true` is set
   - Verify toolbox binary is in PATH: `which toolbox`
   - Check that `tools.yaml` path is correct (relative to where agent runs)

### BigQuery Authentication Error

```
Error: Could not authenticate with BigQuery
```

**Solution:**
1. Run `gcloud auth application-default login`
2. Verify project ID in `tools.yaml` matches your GCP project
3. Check IAM permissions for BigQuery

### Image Analysis Not Working

**Solution:**
1. Ensure image URLs are publicly accessible
2. Check that Gemini API key has vision capabilities enabled
3. Verify image format is supported (JPEG, PNG, etc.)

## Testing

Run a simple test:

```python
from orchestrator.agent import insight_copilot

# Test query
response = insight_copilot.run(
    "What's trending on smart home in Thailand right now?"
)
print(response)
```

## Next Steps

1. Set up your database with sample campaign data
2. Configure image URLs for creatives
3. Test each demo journey from `POC_DEMO_JOURNEYS.md`
4. Customize prompts based on your specific use cases

