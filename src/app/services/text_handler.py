# src/app/services/text_handler.py

from linebot.models import MessageEvent, TextSendMessage
from ..line_bot import line_bot_api

def handle(event: MessageEvent):
    """
    處理文字訊息的核心邏輯。
    """
    # 實現一個簡單的鸚鵡機器人
    reply_text = f"你說了：{event.message.text}"
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )