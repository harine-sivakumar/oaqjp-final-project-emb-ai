from EmotionDetection import emotion_detector

def test_emotion_detector():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected_emotion in test_cases.items():
        response = emotion_detector(statement)
        detected_emotion = response["dominant_emotion"]

        if detected_emotion == expected_emotion:
            print("Passed")
        else:
            print("Failed")

test_emotion_detector()
