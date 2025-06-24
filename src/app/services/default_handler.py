# src/app/services/default_handler.py

from linebot.models import Event
import logging

def handle(event: Event):
    """
    處理所有未被捕獲的事件類型。
    """
    logging.info(f"Received an unhandled event: {event}")
    print(f"Received an unhandled event: {event}")
    # 這裡可以選擇不回應，或者發送一個通用訊息
    # from ..line_bot import line_bot_api
    # from linebot.models import TextSendMessage
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text="抱歉，我還不支援這種訊息類型。")
    # )