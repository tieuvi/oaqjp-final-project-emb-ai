import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Chuyển đổi phản hồi văn bản thành dictionary
    formatted_response = json.loads(response.text)
    
    # Trích xuất tập hợp các cảm xúc và điểm số từ cấu trúc JSON trả về
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Tìm cảm xúc có điểm số cao nhất (dominant emotion)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Trả về kết quả theo đúng định dạng yêu cầu
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }