from flask import Flask, request, jsonify
import requests  # HTTP 요청을 위한 라이브러리

# Flask 애플리케이션 생성
app = Flask(__name__)

# 기본 경로('/')에 대한 GET 요청 처리
@app.route("/", methods=["GET"])
def home():
    # 간단한 메시지를 반환
    return "Welcome to the server running on port 3010!"

# API 경로('/api/data')에 대한 POST 요청 처리
@app.route("/api/data", methods=["POST"])
def receive_data():
    """
    클라이언트로부터 JSON 데이터를 수신하고,
    데이터를 처리한 후 응답을 반환하는 API.
    """
    try:
        # 요청으로부터 JSON 데이터를 가져옴
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400  # 데이터 없을 시 400 오류 반환

        # 요청에서 받은 데이터를 처리(여기선 그대로 반환)
        processed_data = {"received_data": data, "message": "Data received successfully"}
        
        # 처리 결과를 JSON 형태로 반환
        return jsonify(processed_data), 200
    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        return jsonify({"error": str(e)}), 500

# API 경로('/api/send')에 대한 GET 요청 처리
@app.route("/api/send", methods=["GET"])
def send_data():
    """
    서버가 클라이언트 역할을 하여 localhost:3011로 데이터를 송신하는 API.
    """
    try:
        # 송신할 데이터 생성
        data_to_send = {
            "name": "Server Example",
            "timestamp": "2024-11-28T10:00:00",
            "status": "Active"
        }

        # localhost:3011로 POST 요청을 보냄
        response = requests.post("http://localhost:3011/api/data", json=data_to_send)

        # 요청 성공 여부 확인
        if response.status_code == 200:
            return jsonify({"message": "Data sent successfully", "response": response.json()}), 200
        else:
            return jsonify({"error": "Failed to send data", "status_code": response.status_code}), 500
    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        return jsonify({"error": str(e)}), 500


# 메인 함수
if __name__ == "__main__":
    """
    서버를 실행하며, 3010번 포트에서 요청을 대기.
    """
    # Flask 앱 실행
    app.run(host="0.0.0.0", port=3010)
