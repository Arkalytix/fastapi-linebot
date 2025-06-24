# src/app/event_handler.py

from linebot.models import (
    MessageEvent, TextMessage, StickerMessage,
    FollowEvent, UnfollowEvent, Event
)

from .line_bot import handler
from .services import text_handler, follow_handler, default_handler

# 註冊文字訊息事件，並將其導向 services.text_handler
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event: MessageEvent):
    text_handler.handle(event)

# 註冊關注事件
@handler.add(FollowEvent)
def handle_follow(event: FollowEvent):
    follow_handler.handle_follow(event)

# 註冊取消關注事件
@handler.add(UnfollowEvent)
def handle_unfollow(event: UnfollowEvent):
    follow_handler.handle_unfollow(event)

# 註冊貼圖訊息事件 (作為擴充範例)
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event: MessageEvent):
    # 這裡可以直接回覆或導入另一個處理器
    from .line_bot import line_bot_api
    from linebot.models import TextSendMessage
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="這是一個可愛的貼圖！")
    )

# 預設處理器，處理所有未被明確處理的事件
@handler.default()
def handle_default(event: Event):
    default_handler.handle(event)