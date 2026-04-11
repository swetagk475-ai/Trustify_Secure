from transformers import pipeline

class PhishingClassifier:
    def __init__(self):
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

if __name__ == "__main__":
    tester = PhishingClassifier()
    print(tester.analyze("Urgent: Your bank account has been locked. Click here to verify!"))