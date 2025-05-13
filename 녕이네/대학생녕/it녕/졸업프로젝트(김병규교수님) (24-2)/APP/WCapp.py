import matplotlib
matplotlib.use('Agg')  # GUI 백엔드 비활성화

from flask import Flask, request, jsonify, send_file
from wordcloud import WordCloud
from konlpy.tag import Okt
import io
import matplotlib.pyplot as plt
import random

app = Flask(__name__)

# 형태소 분석기 초기화
okt = Okt()

# 불용어 리스트
stop_words = [
    '그리고', '그러나', '또는', '하지만', '그럼에도', '따라서', '이', '그', '저', '어떤', '모든',
    '수', '것', '위해', '하여', '때문', '및', '으로', '에서', '에게', '뿐', '안', '없이', '있다',
    '없다', '같다', '이다', '하다', '하지', '된', '하게', '되어', '하고', '하며', '함', '라', '로',
    '을', '를', '에', '와', '과', '의', '가', '나', '도', '은', '는', '정한', '그런', '할', '될',
    '대해', '따른', '한다', '되고', '된다', '또', '안에', '중에', '위의', '있으며', '있어서', '없으며'
]

# 글씨 색상을 흰색, 회색, 검정 계열로 설정하는 함수
def grayscale_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # 밝기 값 (명도)를 랜덤으로 선택 (20% ~ 100% 밝기)
    brightness = random.randint(20, 100)
    return f"hsl(0, 0%, {brightness}%)"  # Hue=0, Saturation=0 (회색조), Lightness=명도

@app.route('/generate-wordcloud', methods=['POST'])
def generate_wordcloud():
    try:
        # 요청에서 텍스트 데이터 가져오기 (리스트 형태)
        data = request.json
        text_list = data.get('text', None)  # 리스트로 받음

        if not text_list or not isinstance(text_list, list):  # 리스트인지 확인
            return jsonify({"error": "No valid text list provided"}), 400

        # 리스트의 텍스트를 하나로 합치기
        combined_text = " ".join(text_list)

        # 형태소 분석 및 명사 추출
        nouns = okt.nouns(combined_text)
        filtered_nouns = [word for word in nouns if word not in stop_words]
        cleaned_text = " ".join(filtered_nouns)

        # 워드 클라우드 생성
        wordcloud = WordCloud(
            font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf',
            width=300,
            height=300,
            background_color='black',  # 배경색을 검정으로 설정
            max_words=100,
            color_func=grayscale_color_func  # 글자 색상을 흰색, 회색, 검정 계열로 설정
        ).generate(cleaned_text)

        # 이미지를 메모리에 저장
        img_io = io.BytesIO()
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(img_io, format='PNG', bbox_inches='tight', pad_inches=0)
        img_io.seek(0)

        # 이미지를 반환
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
