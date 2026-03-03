from openai import OpenAI
import json
import os

#Handles model initialization and usage.
#api_key is not needed if the model is hosted locally.
class ModelHandler:
    port : int
    api_key : str 
    personality_core : any

    def __init__(self, _port : int, _personality_name : str, _api_key : str = "none"):
        self.port = _port
        self.api_key = _api_key
        
        #Parse personality cores JSON
        try:
            path = os.path.join("personality-cores", f"{_personality_name}.json")
            with open(path) as f:
                self.personality_core = json.load(f)
        except FileNotFoundError:
            print(f"{_personality_name}.json not found.")
            self.personality_core = None
        pass

    def prompt(message : str):
        pass