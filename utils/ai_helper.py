# In Fasttrack's utils/ai_helper.py (create if needed)
import requests

class AIAssistant:
    def __init__(self):
        self.base_url = "http://localhost:8000"
    
    def get_editing_suggestions(self, video_description):
        """Get AI suggestions for video editing"""
        response = requests.post(
            f"{self.base_url}/api/generate/text",
            json={
                "prompt": f"As a professional video editor, suggest improvements for: {video_description}",
                "model": "mistral",
                "system_prompt": "You are an expert video editor with 20 years experience."
            }
        )
        return response.json()
    
    def analyze_scene(self, image_path):
        """Use LLaVA to analyze a video frame"""
        # You'll need to implement image encoding
        with open(image_path, "rb") as f:
            image_data = f.read()
        
        response = requests.post(
            f"{self.base_url}/api/analyze/image",
            json={
                "image_data": image_data.hex(),  # Or use base64
                "prompt": "Describe this scene for video editing purposes"
            }
        )
        return response.json()