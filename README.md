# Adapter Insight Copilot

A multi-agent AI system that combines internal campaign data, external Thai social media insights, and creative analysis to provide comprehensive marketing campaign intelligence.

## Overview

This system uses Google's Agent Development Kit (ADK) to orchestrate three specialized agents:

1. **Social Media Agent** - Analyzes trends and sentiment from Thai social platforms (Facebook, YouTube, TikTok, Pantip, X)
2. **Internal Data Agent** - Queries campaign performance metrics from BigQuery/Postgres via genai-toolbox
3. **Creative Agent** - Analyzes ad images to extract visual patterns and style insights

The **Insight Copilot** orchestrator coordinates these agents to answer complex marketing questions that require both internal and external context.

## Features

- **Pre-launch Planning**: Understand market trends + past performance + creative guidance
- **Live Campaign Health Checks**: Diagnose performance issues using metrics + market sentiment + creative fit
- **Post-campaign Analysis**: Comprehensive reviews combining performance + market alignment + creative patterns
- **Creative Pattern Mining**: Identify what visual styles work best for specific audiences

## Quick Start

### 1. Install Dependencies

```bash
pip install -e .
# Or using uv
uv sync
```

### 2. Set Up genai-toolbox

See `TOOLBOX_SETUP.md` for detailed instructions.

```bash
# Download toolbox
export OS="darwin/arm64"  # Adjust for your OS
curl -O https://storage.googleapis.com/genai-toolbox/v0.20.0/$OS/toolbox
chmod +x toolbox

# Configure and start server
./toolbox --tools-file tools.yaml
```

### 3. Configure

1. Edit `tools.yaml` - Replace `YOUR_PROJECT_ID` with your GCP project ID
2. Authenticate: `gcloud auth application-default login`
3. Set API key: `export GOOGLE_API_KEY="your-key"`

### 4. Run

```bash
adk web
```

Select the `insight_copilot` agent and start asking questions!

## Example Questions

- "What's trending on smart home in Thailand right now, and what performance can we expect based on past campaigns?"
- "How is our 'Summer Sale' campaign performing compared to market trends?"
- "What visual styles work best for Gen Z audiences based on our historical campaigns?"

See `POC_DEMO_JOURNEYS.md` for detailed demo scenarios.

## Architecture

```
InsightCopilot (Root Agent)
├── SocialMediaAgent (google_search)
├── InternalDataAgent (genai-toolbox → BigQuery)
└── CreativeAgent (multimodal image analysis)
```

## Documentation

- `POC_SCOPE.md` - POC scope, data schemas, assumptions
- `POC_DEMO_JOURNEYS.md` - Detailed demo scenarios and expected flows
- `CONFIGURATION.md` - Setup and configuration guide
- `TOOLBOX_SETUP.md` - genai-toolbox setup instructions
- `PROJECT_HIGHLEVEL.md` - High-level design and architecture

## Requirements

- Python 3.13+
- Google Cloud Project with BigQuery access
- genai-toolbox server running
- Google API Key for Gemini models

## License

[Your License Here]

