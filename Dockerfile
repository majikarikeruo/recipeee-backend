FROM python:3.11



# 作業ディレクトリを指定
WORKDIR /app

# 必要なPythonライブラリをインストール
COPY requirements.txt ./
RUN pip install -r requirements.txt

# アプリケーションのコードをコンテナにコピー
COPY . /app/


EXPOSE 8000


# FastAPIの起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
