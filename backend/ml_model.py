from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.packet_counts = []

    def add_data(self, packet_count):
        self.packet_counts.append([packet_count])
        if len(self.packet_counts) > 10:  # Train after collecting enough data
            self.train()

    def train(self):
        self.model.fit(self.packet_counts)

    def predict(self, packet_count):
        if len(self.packet_counts) < 10:
            return 0  # Not enough data
        prediction = self.model.predict([[packet_count]])
        return prediction[0]  # -1 for anomaly, 1 for normal
