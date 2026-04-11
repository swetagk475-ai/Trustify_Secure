from transformers import pipeline
import torch

class PhishingClassifier:
    def __init__(self):
        # We use a model specifically fine-tuned for detecting malicious text/spam
        # This will download the model the first time you run it (approx 260MB)
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

        # Truncate text to 512 tokens (BERT limit)
        truncated_text = text[:512]
        prediction = self.classifier(truncated_text)
        
        # Format the result for our Orchestrator
        return {
            "module": "NLP_Engine",
            "label": prediction['label'],
            "confidence": round(prediction['score'] * 100, 2),
            "raw_score": prediction['score']
        }

if __name__ == "__main__":
    # Quick Test
    tester = PhishingClassifier()
    print(tester.analyze("Urgent: Your bank account has been locked. Click here to verify!"))