# src/app/main.py (最終推薦版本)

from fastapi import FastAPI, Request, HTTPException
from linebot.exceptions import InvalidSignatureError

from .line_bot import handler
from . import event_handler

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    """
    LINE Webhook 主入口。
    驗證簽名並將事件分派給對應的處理器。
    """
    # 1. 從標頭取得簽名
    signature = request.headers.get("X-Line-Signature")
    if signature is None:
        raise HTTPException(status_code=400, detail="X-Line-Signature header not found")

    # 2. 取得請求的 body
    body = await request.body()

    # 3. 交給 line-bot-sdk 的 handler 進行驗證和處理
    try:
        handler.handle(body.decode('utf-8'), signature)
    except InvalidSignatureError:
        # 簽名驗證失敗，回傳 400
        raise HTTPException(status_code=400, detail="Invalid signature. Please check your channel secret and access token.")
    except Exception as e:
        # 其他所有未預期的錯誤，回傳 500
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # 4. 如果一切順利，回傳 200 OK
    return "OK"

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI LINE Bot Template!"}