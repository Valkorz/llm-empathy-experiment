from openai import OpenAI
import json
import os
from .personality_handler import PersonalityHandler

#Handles model initialization and usage.
#api_key is not needed if the model is hosted locally.
class ModelHandler:
    port : int
    api_key : str 
    personality_core : any
    personality_handler : PersonalityHandler

    def __init__(self, _port : int, _personality_name : str, _api_key : str = "none"):
        self.port = _port
        self.api_key = _api_key
        
        #Parse personality cores JSON
        try:
            path = os.path.join("personality-cores", f"{_personality_name}.json")
            with open(path) as f:
                self.personality_core = json.load(f)
                self.personality_handler = PersonalityHandler(self.personality_core)
        except FileNotFoundError:
            print(f"{_personality_name}.json not found.")
            self.personality_core = None
        pass

    def prompt(self, message : str, scenario : int):
        #Load data for building a prompt
        persona = self.personality_handler.ToJson()
        with open("scenarios/scenarios.json") as f:
            scenarios = json.load(f)
            scenario = scenarios[f"scenario_{scenario}"]

        # question = f"Your persona: {persona}\nScenario: {scenario}\nSituation: {message}\n Provide your internal thought process and your final decision."
        # print(question)
        question = f"""
        SETTING: High-stakes life or death moment.

        YOUR PERSONA: {persona}

        TASK: {message}. Provide your internal thought process and your final decision.
        """
        client = OpenAI(base_url=f"http://localhost:{self.port}/v1", api_key=self.api_key)

        completion = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": scenario},
                {"role": "user", "content": question}
            ],
            temperature=0.8, 
            response_format={"type": "json_object"} 
        )
        
        print(completion.choices[0].message.content)
        response_content = completion.choices[0].message.content
        print(f"Agent {self.personality_handler.name} responded: {response_content}")
        return response_content