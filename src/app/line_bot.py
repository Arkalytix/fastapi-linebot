# src/app/line_bot.py

from linebot import LineBotApi, WebhookHandler
from .config import settings

# 初始化 Line Bot API
# 用於主動發送訊息等操作
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

# 初始化 Webhook Handler
# 用於處理進來的 Webhook 事件
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)