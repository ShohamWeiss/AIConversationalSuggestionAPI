from transformers import AutoTokenizer
from pyannote.audio import Pipeline
from pydub import AudioSegment
import os
import shutil

class Diarization():
    def __init__(self):        
        self.model = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",                                    
                                    use_auth_token="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")

    def run_diarization(self, filename:str) -> bool:
        ''' Run diarization on audio file and return True if successful '''
        
        try:
            with open(filename, "rb") as f:
                diarization = self.model(filename)
            # example result: {{speaker_01: [0.00sec, 0.05sec], speaker_02: [0.06sec, 0.10sec]}}
            song = AudioSegment.from_wav(filename)            
                        
            folder = "diarization"
            if os.path.exists(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)
            i = 0
            for turn, _, speaker in diarization.itertracks(yield_label=True):                
                print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
                song[turn.start*1000:turn.end*1000].export(f"diarization/{i}_{speaker}.mp3", format="wav")
                i += 1          
            return True        
        except:
            return False
    
if __name__=="__main__":
    
    diarization = Diarization()
    print("running diarization on audio file...")
    diarization.run_diarization("audio.wav")