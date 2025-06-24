# FastAPI LINE Bot Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

一個生產級、高度模組化的 LINE Bot 專案範本。基於 FastAPI、Docker 和 Cloudflared 打造，專為快速啟動、本地偵錯和輕鬆擴充業務邏輯而設計。

---

## ✨ 核心特色

- **🚀 高效能框架**: 基於現代、高效能的 **FastAPI**。
- **🐳 完全容器化**: 使用 **Docker** 和 **Docker Compose** 提供一致、隔離的開發與運行環境。
- **穿透測試**: 內建 **Cloudflared** 服務，一鍵將本地開發伺服器安全地暴露到公網，方便直接用手機 LINE App 進行真實測試。
- **🔌 可插拔架構**: 將核心框架 (`app`) 與業務邏輯 (`services`) 徹底分離，新增功能只需專注於 `services` 目錄。
- **🔧 現代化開發流程**:
    - 採用 `src` 佈局，結構清晰，避免導入問題。
    - 支援 VS Code **中斷點偵錯**，可直接在容器中運行的程式碼上進行偵錯。
    - 使用 `.env` 檔案管理所有機密金鑰，安全可靠。
- **📝 最佳實踐**:
    - 使用 `python:3.12-slim` 作為基礎映像檔，兼顧了體積與兼容性。
    - 提供 `.roocodeignore` 檔案，優化 AI 輔助工具的上下文，節省 Token 並提高準確度。
    - 異常處理流程清晰，區分客戶端錯誤 (4xx) 與伺服器錯誤 (5xx)。

---

## 📂 專案結構

```
.
├── .vscode/
│   └── launch.json         # VS Code 偵錯設定檔
├── src/
│   └── app/                # 核心應用程式包
│       ├── main.py         # FastAPI 進入點，處理 Webhook 路由
│       ├── event_handler.py# 將 LINE 事件路由到對應的 Service
│       └── services/       # <-- 你的業務邏輯都寫在這裡
├── .env.example            # 環境變數範本
├── .env                    # [本地使用] 存放你的金鑰
├── .gitignore
├── .roocodeignore          # RooCode AI 助手的忽略檔案
├── docker-compose.yml      # Docker Compose 指揮中心
├── Dockerfile              # 應用程式 Docker 映像檔藍圖
├── LICENSE
├── README.md
└── requirements.txt        # Python 依賴列表
```

---

## 🚀 快速上手

### 前置準備

1.  [**Docker Desktop**](https://www.docker.com/get-started) - 確保已安裝並正在運行。
2.  **啟用 WSL 整合**: 在 Docker Desktop 設定中 -> Resources -> WSL Integration，確保你的 WSL 發行版（如 Ubuntu）已啟用整合。
3.  **LINE Developers 帳號**:
    *   建立一個 Messaging API Channel。
    *   取得 `Channel Secret` 和 `Channel Access Token`。
4.  **VS Code** 及推薦擴充套件：
    *   `ms-python.python` (Python)
    *   `ms-azuretools.vscode-docker` (Docker)

### 安裝與設定

1.  **克隆專案**:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **設定環境變數**:
    ```bash
    cp .env.example .env
    ```
    然後編輯 `.env` 檔案，填入你的 `LINE_CHANNEL_SECRET` 和 `LINE_CHANNEL_ACCESS_TOKEN`。

---

## 🛠️ 開發與運行

本專案提供兩種開發模式：**Docker 模式 (推薦)** 和 **本地虛擬環境模式**。

### 模式一：使用 Docker Compose (推薦)

這是最推薦的模式，它能提供最接近生產環境的一致性。

#### 運行

在專案根目錄下，執行一個指令即可啟動所有服務（FastAPI App + Cloudflared）：
```bash
docker compose up --build
```
*   `--build` 參數在第一次啟動或修改 `Dockerfile`/`requirements.txt` 後需要加上。

#### 串接 LINE Webhook

1.  觀察 `docker compose` 的日誌，找到 `cloudflared` 輸出的公開 URL，格式為 `https://<some-name>.trycloudflare.com`。
2.  前往你的 LINE Developer Console，將 **Webhook URL** 設定為：
    `https://<some-name>.trycloudflare.com/webhook`
3.  點擊 "Verify"，應該會顯示成功。
4.  啟用 "Use webhook"。
5.  現在，用你的手機發訊息給 Bot，它應該就會有回應了！

#### 在 Docker 中偵錯 (中斷點)

1.  保持 `docker compose up` 運行。
2.  在 VS Code 左側的 Docker 擴充套件面板中，找到 `linebot_app` 容器。
3.  在容器上按右鍵，選擇 **「附加 Visual Studio Code」(Attach Visual Studio Code)**。
4.  VS Code 會在容器的環境中開啟一個新視窗。
5.  在這個新視窗中，打開「執行與偵錯」面板，選擇 `Python: FastAPI` 配置，然後按 **F5**。
6.  現在，你可以在 `src` 目錄下的任何程式碼中設置中斷點，並透過手機發送訊息來觸發它。

---

### 模式二：本地虛擬環境 (用於快速測試與語法檢查)

1.  **建立虛擬環境**:
    ```bash
    python3 -m venv .venv
    ```
2.  **啟用虛擬環境**:
    ```bash
    source .venv/bin/activate
    ```
3.  **安裝依賴**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **配置 VS Code 解釋器**:
    *   按 `Ctrl+Shift+P`，選擇 `Python: Select Interpreter`。
    *   選擇你的 `.venv` 環境。
5.  **啟動本地偵錯**:
    *   打開「執行與偵錯」面板。
    *   選擇 `Python: FastAPI` 配置，按 **F5** 即可開始偵錯。
    *   服務將運行在 `http://127.0.0.1:8000`。你可以使用 `curl` 或 API 工具進行測試。

---

## 📝 擴充你的 Bot

要新增或修改 Bot 的功能，你只需要專注於 `src/app/services/` 目錄。

#### 範例：修改文字訊息的回應

1.  打開 `src/app/services/text_handler.py`。
2.  修改 `handle()` 函式內的邏輯。
3.  如果你正在使用 Docker 模式，儲存檔案後，`--reload` 功能會自動重啟伺服器，變更立即生效。

#### 範例：新增處理圖片訊息的功能

1.  建立新檔案 `src/app/services/image_handler.py` 並撰寫處理邏輯。
2.  打開 `src/app/event_handler.py`。
3.  匯入你的新處理器和對應的事件類型 (`ImageMessage`)。
4.  新增一個新的事件處理器來註冊它：
    ```python
    from linebot.models import ImageMessage
    from .services import image_handler

    @handler.add(MessageEvent, message=ImageMessage)
    def handle_image_message(event):
        image_handler.handle(event)
    ```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.