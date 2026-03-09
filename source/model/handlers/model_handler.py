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

    def prompt(self, user_message : str, use_persona : bool, system_message : str = "") -> dict:
        try:
            if use_persona and self.personality_core is None:
                return "No personality core loaded."
        
            #Load data for building a prompt
            if use_persona:
                persona = self.personality_handler.ToJson()

            context = system_message
            if use_persona:
                context = f"""
                PERSONA: {persona}

                INFO: {system_message}
                """

            client = OpenAI(base_url=f"http://localhost:{self.port}/v1", api_key=self.api_key)

            completion = client.chat.completions.create(
                model="local-model",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.8, 
                    response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "reasoning_response",
                        "strict": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "thought_process": {"type": "string"},
                                "final_decision": {"type": "string"}
                            },
                            # "required": ["thought_process", "final_decision"],
                            "required": ["final_decision"],
                            "additionalProperties": False
                        }
                    }
                }
            )

            # print(completion.choices[0].message.content)
            response_content = completion.choices[0].message.content
            # print(f"Agent {self.personality_handler.name} responded: {response_content}")
            response_dict = json.loads(response_content)
            return response_dict
        except Exception as e:
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {e}")
            return "An unknown error occured."