# src/app/services/follow_handler.py

from linebot.models import FollowEvent, UnfollowEvent, TextSendMessage
from ..line_bot import line_bot_api

def handle_follow(event: FollowEvent):
    """
    當使用者將 Bot 加為好友時觸發。
    """
    user_id = event.source.user_id
    print(f"User {user_id} has followed the bot.")
    
    # 可以在這裡取得使用者個資並存入資料庫
    # profile = line_bot_api.get_profile(user_id)
    # print(profile.display_name)
    # print(profile.picture_url)
    
    reply_text = "感謝您加我為好友！這是一個使用 FastAPI 建立的 Line Bot 範本。"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

def handle_unfollow(event: UnfollowEvent):
    """
    當使用者封鎖或刪除 Bot 時觸發。
    """
    user_id = event.source.user_id
    print(f"User {user_id} has unfollowed or blocked the bot.")
    # 在這裡可以處理用戶取消關注的邏輯，例如更新資料庫中的狀態