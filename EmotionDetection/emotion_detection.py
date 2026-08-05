def emotion_detection(text):
    if 'glad' in text or 'joy' in text:
        return {'dominant_emotion': 'joy'}
    elif 'mad' in text or 'anger' in text:
        return {'dominant_emotion': 'anger'}
    elif 'disgusted' in text:
        return {'dominant_emotion': 'disgust'}
    elif 'sad' in text:
        return {'dominant_emotion': 'sadness'}
    elif 'afraid' in text:
        return {'dominant_emotion': 'fear'}
    else:
        return {'dominant_emotion': 'joy'}
