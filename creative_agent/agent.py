from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
from typing import List, Optional
import json
import requests
from io import BytesIO

# Placeholder for database/API to fetch creatives
# In production, this would query BigQuery/Postgres or an API
def list_creatives_for_campaign(campaign_id: str) -> str:
    """
    List all creatives (images) associated with a campaign.
    
    Args:
        campaign_id: The campaign ID to fetch creatives for
    
    Returns:
        JSON string containing list of creatives with metadata
    """
    # In production, this would query the creatives table via genai-toolbox
    # For POC, this can be mocked or use actual database query
    # Example structure:
    mock_response = {
        "campaign_id": campaign_id,
        "creatives": [
            {
                "creative_id": "creative_1",
                "image_url": "https://example.com/image1.jpg",
                "platform": "facebook",
                "format": "static",
                "audience_segment": "gen_z"
            }
        ],
        "note": "In production, this queries the creatives table via genai-toolbox. Currently returning mock data."
    }
    
    return json.dumps(mock_response)


def analyze_image(image_url: str) -> str:
    """
    Analyze an image to extract visual style, text, colors, and other attributes.
    
    This function uses Gemini's multimodal capabilities (via the agent's model) to analyze the image.
    The agent itself can process images when provided with image URLs.
    
    Args:
        image_url: URL to the image to analyze
    
    Returns:
        JSON string containing structured analysis of the image
    """
    try:
        # Fetch image to verify it's accessible
        response = requests.get(image_url, timeout=10)
        if response.status_code != 200:
            return json.dumps({
                "error": f"Could not fetch image from URL: {image_url}",
                "status_code": response.status_code
            })
        
        # Note: The actual image analysis will be done by the Gemini model
        # when the agent processes the image. This function just validates
        # the URL and returns a structure for the agent to fill in.
        
        # In a full implementation, you might want to:
        # 1. Download the image
        # 2. Send it to Gemini Vision API directly
        # 3. Extract structured information
        
        # For now, return a structure that guides the agent
        analysis_structure = {
            "image_url": image_url,
            "visual_style": "corporate|fun|premium|minimalist|lifestyle|product_focused",
            "dominant_colors": ["color1", "color2"],
            "has_faces": True,
            "num_people": 0,
            "age_style": "youthful|office|family|mixed",
            "text_density": "low|medium|high",
            "extracted_text": {
                "headline": "",
                "subtext": "",
                "cta": "",
                "promo_messages": []
            },
            "emotional_tone": "playful|serious|urgent|calm|energetic",
            "layout_type": "centered|split|grid|minimal",
            "platform_fit": "facebook|instagram|tiktok|youtube|generic",
            "description": "Natural language description of what's in the image",
            "note": "The Gemini model will analyze the image and populate these fields."
        }
        
        return json.dumps(analysis_structure)
    
    except Exception as e:
        return json.dumps({
            "error": f"Error analyzing image: {str(e)}",
            "image_url": image_url
        })


# Create FunctionTools
list_creatives_tool = FunctionTool(
    func=list_creatives_for_campaign,
    name="list_creatives_for_campaign",
    description="""List all creatives (images) for a given campaign ID.
Returns creative metadata including image_url, platform, format, and audience_segment.
"""
)

analyze_image_tool = FunctionTool(
    func=analyze_image,
    name="analyze_image",
    description="""Analyze an image to extract visual attributes, text, colors, style, and emotional tone.
Returns structured JSON with:
- visual_style (corporate/fun/premium/minimalist)
- dominant_colors
- has_faces, num_people, age_style
- text_density and extracted_text (OCR)
- emotional_tone (playful/serious/urgent/etc.)
- layout_type and platform_fit
- natural language description

Note: The Gemini model will perform the actual image analysis when processing the image URL.
"""
)

creative_agent = Agent(
    model='gemini-2.5-flash',  # Gemini supports multimodal, can analyze images
    name='CreativeAgent',
    description='Analyzes and evaluates ad creatives (images/key visuals) to extract visual style, text, and performance patterns.',
    instruction='''You are a creative intelligence agent specialized in analyzing campaign images and key visuals.

**Your Role:**
- Analyze images to understand visual style, messaging, and emotional tone
- Extract text from images using OCR capabilities
- Identify patterns across multiple creatives
- Correlate visual attributes with performance when metrics are available

**Image Analysis Schema:**

When analyzing an image, extract and structure:

1. **Visual Style**: corporate / fun / premium / minimalist / lifestyle / product_focused
2. **Colors**: List dominant colors (e.g., ["bright_blue", "white", "orange"])
3. **People**: 
   - has_faces (boolean)
   - num_people (integer)
   - age_style: youthful / office / family / mixed
4. **Text**:
   - text_density: low / medium / high
   - extracted_text: headline, subtext, CTA, promo_messages (array)
5. **Emotional Tone**: playful / serious / urgent / calm / energetic
6. **Layout**: centered / split / grid / minimal
7. **Platform Fit**: facebook / instagram / tiktok / youtube / generic
8. **Description**: Natural language description of what's in the image

**Workflow:**

1. **For single image analysis:**
   - Use analyze_image tool with the image_url
   - The Gemini model will analyze the image and extract all attributes above
   - Provide insights about the visual style and messaging

2. **For campaign creative analysis:**
   - Use list_creatives_for_campaign to get all creatives
   - Analyze each creative using analyze_image
   - Aggregate patterns: common colors, styles, text patterns
   - Identify what's consistent vs. what varies

3. **For performance correlation:**
   - When performance metrics are provided (from internal data agent):
   - Compare visual attributes of top performers vs. low performers
   - Identify patterns: "Bright colors + low text + playful tone correlate with high CTR for Gen Z"

**Response Format for Orchestrator Integration:**

Structure your response with:

1. **Creative Summary** (for campaigns):
   - Number of creatives analyzed
   - Common visual styles, colors, tones
   - Text patterns (common headlines, CTAs)

2. **Pattern Analysis**:
   - What visual elements are consistent across creatives
   - What varies and why that might matter
   - Performance correlations (if metrics provided)

3. **Recommendations**:
   - Visual style suggestions based on patterns
   - What to avoid based on low-performing creatives
   - Platform-specific recommendations

**Example Analysis:**

User: "Analyze creatives for campaign X"
→ List creatives → Analyze each → Find patterns:
  - "All creatives use bright, vibrant colors (blue, orange)"
  - "80% have faces, showing youthful people"
  - "Text density is low (mostly headlines only)"
  - "Emotional tone is playful and energetic"
  → Conclusion: "Campaign X uses a consistent fun, youthful visual style optimized for social engagement"

Remember: Always use the tools (list_creatives_for_campaign, analyze_image) to get actual data. When analyzing images, use your multimodal capabilities to extract visual attributes, text, and emotional tone. Provide structured, actionable insights about visual patterns and their potential impact on performance.
''',
    tools=[list_creatives_tool, analyze_image_tool],
)

