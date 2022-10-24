from multiprocessing.dummy import Array
from operator import truediv
from transformers import pipeline, AutoTokenizer
from Conversation import Conversation
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pyannote.audio import Pipeline
from pydub import AudioSegment
import os
import shutil

class Diarization():
    def __init__(self):
        self.model = Pipeline.from_pretrained("pyannote/speaker-diarization@2022.07", device="cuda" if torch.cuda.is_available() else "cpu")

    def run_diarization(self, filename:str) -> bool:
        ''' Run diarization on audio file and return True if successful '''
        
        try:
            diarization = self.model(filename)
            song = AudioSegment.from_wav(filename)
            i = 0
                        
            folder = "diarization"
            if os.path.exists(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)
            
            for turn, _, speaker in diarization.itertracks(yield_label=True):                
                print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
                song[turn.start*1000:turn.end*1000].export(f"diarization/audio_{speaker}_{i}.wav", format="wav")
                i += 1
            return True        
        except:
            return False        
    
if __name__=="__main__":
    
    diarization = Diarization()    
    diarization.run_diarization("test.wav")