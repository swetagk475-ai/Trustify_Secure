<<<<<<< HEAD
from transformers import pipeline
=======
import asyncio
from modules.nlp.phishing_classifier import PhishingClassifier # We will build these next
from modules.url.url_classifier import URLClassifier
from evidence.hasher import generate_evidence_hash
>>>>>>> 60078cb2b4a6cfbe4fe0393a7916b6355e4b8cac

class Orchestrator:
    def __init__(self):
<<<<<<< HEAD
        self.model_name = "mrm8488/bert-tiny-finetuned-sms-spam-detection"
        try:
            self.classifier = pipeline("text-classification", model=self.model_name)
            print(f"[*] NLP Model '{self.model_name}' loaded successfully.")
        except Exception as e:
            print(f"[!] Error loading NLP model: {e}")
            self.classifier = None

    def analyze(self, text):
        if not self.classifier:
            return {"score": 0.0, "label": "Error", "details": "Model not loaded"}

        truncated_text = text[:512]
        raw_prediction = self.classifier(truncated_text)
        
        # Flatten the result to handle nested lists
        prediction = raw_prediction
        while isinstance(prediction, list):
            prediction = prediction
        
        label = prediction.get('label') or prediction.get('LABEL')
        score = prediction.get('score') or prediction.get('SCORE')

        # Translate the model's labels to something human-readable
        # LABEL_1 usually means SPAM/PHISHING in this model
        friendly_label = "Malicious/Spam" if label == "LABEL_1" else "Safe/Ham"

        return {
            "module": "NLP_Engine",
            "prediction": friendly_label,
            "confidence": round(score * 100, 2) if score else 0.0,
            "raw_score": score
        }
=======
        # Initialize our models here
        self.nlp_model = None 
        self.url_model = None

    async def run_analysis(self, user_input, input_type):
        """
        Runs NLP, URL, and Vision analysis in parallel.
        """
        print(f"[*] Starting Multimodal Analysis for: {input_type}")
        
        # Create tasks to run concurrently
        tasks = []
        if input_type == "URL / Website Link":
            tasks.append(self.analyze_url(user_input))
            tasks.append(self.analyze_nlp(user_input)) # Analyze the text of the URL too
        else:
            tasks.append(self.analyze_nlp(user_input))
>>>>>>> 60078cb2b4a6cfbe4fe0393a7916b6355e4b8cac

        # Wait for all models to return results
        results = await asyncio.gather(*tasks)
        
        # Combine results into a single report
        final_report = self.fuse_results(results)
        
        # Generate the digital seal (Hash)
        final_report['evidence_hash'] = generate_evidence_hash(final_report)
        
        return final_report

    async def analyze_nlp(self, text):
        await asyncio.sleep(1) # Simulate AI processing time
        return {"module": "nlp", "score": 0.85, "label": "Phishing"}

    async def analyze_url(self, url):
        await asyncio.sleep(1) # Simulate URL feature extraction
        return {"module": "url", "score": 0.92, "label": "Malicious"}

    def fuse_results(self, results):
        # Basic weighted average logic (this will move to fusion.py later)
        return {"final_risk": 88.5, "breakdown": results}

# --- For Testing ---
if __name__ == "__main__":
<<<<<<< HEAD
    tester = PhishingClassifier()
    print(tester.analyze("Urgent: Your bank account has been locked. Click here to verify!"))
=======
    orch = Orchestrator()
    report = asyncio.run(orch.run_analysis("http://fake-login.com", "URL / Website Link"))
    print(f"[+] Analysis Complete: {report}")
>>>>>>> 60078cb2b4a6cfbe4fe0393a7916b6355e4b8cac
