# Create the Ollama client
cat > utils/ollama_client.py << 'EOF'
import requests
import json
import base64

class OllamaClient:
    def __init__(self, host="localhost", port=11434):
        self.base_url = f"http://{host}:{port}/api"
    
    def generate(self, model, prompt, system=None, images=None):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.7}
        }
        
        if system:
            payload["system"] = system
        
        if images:
            payload["images"] = [self._encode_image(img) for img in images]
        
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json=payload,
                timeout=60
            )
            return response.json()
        except Exception as e:
            return {"error": str(e), "response": ""}
    
    def _encode_image(self, image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    
    def list_models(self):
        try:
            response = requests.get(f"{self.base_url}/tags", timeout=10)
            return response.json().get("models", [])
        except:
            return []
EOF