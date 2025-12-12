import requests

class AIAssistant:
    def __init__(self, base_url="http://192.168.1.42:8000"):
        self.base_url = base_url
    
    def get_editing_suggestions(self, video_description):
        """Get AI suggestions for video editing"""
        response = requests.post(
            f"{self.base_url}/api/generate/text",
            json={
                "prompt": f"As a video editor, suggest improvements: {video_description}",
                "model": "mistral",
                "system_prompt": "You are an expert video editor."
            }
        )
        return response.json()
    
    def test_connection(self):
        """Test if AI framework is available"""
        try:
            response = requests.get(f"{self.baseURL}/health", timeout=5)
            return response.json()
        except:
            return {"status": "disconnected"}