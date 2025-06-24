# Dockerfile

# 1. 使用官方 Python 3.12 的輕量級映像檔作為基礎
FROM python:3.12-slim

# 2. 設定容器內的工作目錄
WORKDIR /code

# 3. 將 requirements.txt 複製進去
COPY ./requirements.txt /code/requirements.txt

# 4. 在容器內安裝所有 Python 依賴
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. 將你所有的原始碼 (src 目錄) 複製到容器的工作目錄下
COPY ./src /code

# 6. 指定容器啟動時要執行的預設命令
#    注意：這裡我們只用最基礎的啟動命令
#    --host 0.0.0.0 是讓容器外部可以訪問
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]