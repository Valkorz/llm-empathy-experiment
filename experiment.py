from source.model.handlers.personality_handler import PersonalityHandler
from source.model.handlers.model_handler import ModelHandler
from sentence_transformers import SentenceTransformer
from source.experiments.bribing_experiment import exec_bribingExperiment
# from source.experiments.bribing_experiment import executeBribingExperimentThought
import matplotlib.pyplot as plt
import chromadb
import numpy as np
    
models = ["deepseek-r1-distill-qwen-1.5b", "dolphin-2.9-llama3-8b"]
exec_bribingExperiment(output_name="test", sampling_count=20, models=models)