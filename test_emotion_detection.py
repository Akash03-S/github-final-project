from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detection('I am glad this happened')['dominant_emotion'], 'joy')
        self.assertEqual(emotion_detection('I am really mad about this')['dominant_emotion'], 'anger')
        self.assertEqual(emotion_detection('I feel disgusted just hearing about this')['dominant_emotion'], 'disgust')
        self.assertEqual(emotion_detection('I am so sad about this')['dominant_emotion'], 'sadness')
        self.assertEqual(emotion_detection('I am really afraid that this will happen')['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
