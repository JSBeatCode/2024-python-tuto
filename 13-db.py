# pip install psycopg2 flask

from flask import Flask, jsonify, request
import psycopg2  # PostgreSQL 연결을 위한 라이브러리

# Flask 애플리케이션 생성
app = Flask(__name__)

# PostgreSQL 연결 정보
DB_CONFIG = {
    "dbname": "postgres",  # 데이터베이스 이름
    "user": "postgres",   # 사용자 이름
    "password": "qwer1234",  # 비밀번호
    "host": "localhost",       # 호스트 주소 (로컬 호스트)
    "port": "5432"             # PostgreSQL 기본 포트
}


def get_db_connection():
    """
    PostgreSQL 데이터베이스 연결을 생성하는 함수.
    """
    try:
        # psycopg2를 사용해 데이터베이스 연결 생성
        connection = psycopg2.connect(**DB_CONFIG)
        connection.set_client_encoding('utf-8')
        return connection
    except Exception as e:
        # 연결 실패 시 오류 출력
        print("Database connection error:", e)
        return None


@app.route("/api/data", methods=["GET"])
def get_data_from_db():
    """
    PostgreSQL 데이터베이스에서 데이터를 가져와 API 응답으로 반환.
    """
    connection = get_db_connection()
    if not connection:
        # 데이터베이스 연결 실패 시 오류 반환
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        # 데이터베이스 커서 생성
        # cursor는 데이터베이스 연결 객체에서 제공하는 인터페이스로, 데이터베이스와의 상호작용(쿼리 실행 및 결과 처리)을 관리하는 역할을 합니다.
        # cursor는 데이터베이스와 애플리케이션 간의 다리 역할을 하며, SQL 쿼리 실행과 결과를 관리하는 중요한 객체입니다.
        cursor = connection.cursor()

        # SQL 쿼리 실행 (예: 테이블 이름이 'sample_table'이고 컬럼은 'id'와 'name')
        query = "SELECT id, code, detail, sub_model FROM demo;"
        cursor.execute(query)
        # INSERT 쿼리 실행
        # cursor.execute(
        #     "INSERT INTO employees (name, position) VALUES (%s, %s)", 
        #     ("Alice", "Engineer")
        # )

        # # 변경 사항 저장
        # connection.commit()
        
        column_names = [desc[0] for desc in cursor.description]  # ('id', 'name', 'detail', 'sub_model')



        # 결과 가져오기
        
        rows = cursor.fetchall()

        # 결과를 JSON 형태로 변환
        result = []
        for row in rows:
            result.append({column: value for column, value in zip(column_names, row)})

        # 결과 반환
        return jsonify(result), 200
    except Exception as e:
        # 쿼리 실행 중 예외 처리
        print("Query execution error:", e)
        return jsonify({"error": "Failed to fetch data"}), 500
    finally:
        # 연결 종료
        cursor.close()
        connection.close()


if __name__ == "__main__":
    """
    Flask 서버 실행
    """
    # Flask 앱 실행
    app.run(host="0.0.0.0", port=3010)
