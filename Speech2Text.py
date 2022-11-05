from transformers import pipeline
from Conversation import Conversation
import torch
import os

class Speech2Text():
    def __init__(self):
        self.model = pipeline(
            "automatic-speech-recognition",
            model="facebook/wav2vec2-large-960h",
            feature_extractor="facebook/wav2vec2-large-960h",
            device = 0 if torch.cuda.is_available() else -1
        )
        self.conversation = Conversation()

    def run_speech2text(self, foldername:str) -> Conversation:
        ''' Run speech2text on audio file and return transcribed conversation '''
        conversation = Conversation()
        # order files by name
        files = sorted(os.listdir(foldername))
        for filename in files:
            with open(f"{foldername}/{filename}", "rb") as f:
                print(f"running speech2text on {filename}...")
                audio = f.read()
                text = self.model(audio)
                print(text)
                conversation.add(filename[2:-4].lower(), text["text"].lower())                
                
        return conversation
    
if __name__=="__main__":
            
    speech2Text = Speech2Text()    
    results = speech2Text.run_speech2text("diarization")
    print(results)

