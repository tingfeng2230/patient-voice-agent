# 患者信息语音采集智能体

一个基于语音识别的智能患者信息采集系统，支持实时语音录入和跨设备同步。

## 功能特性

- 🎤 **实时语音识别**：边说边识别，自动填充表单
- 👤 **智能信息提取**：自动识别患者姓名和问诊记录
- 📱 **跨设备同步**：手机录音，电脑实时显示
- 💬 **Agent对话**：支持通过API调用智能体
- 🔌 **WebSocket支持**：实时双向通信

## 快速开始

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python -m src.main -m http -p 5000

# 访问
http://localhost:5000/static/recorder-realtime.html
```

### API调用

```bash
curl -X POST http://localhost:5000/run \
  -H "Content-Type: application/json" \
  -d '{
    "type": "query",
    "session_id": "test",
    "message": "你好",
    "content": {
      "query": {
        "prompt": [
          {
            "type": "text",
            "content": {"text": "你好"}
          }
        ]
      }
    }
  }'
```

## 页面说明

- **实时语音识别**：`/static/recorder-realtime.html`
- **手机录音端**：`/static/mobile-recorder.html`
- **电脑表单端**：`/static/desktop-form.html`
- **传统录音**：`/static/recorder.html`

## 环境变量

- `COZE_WORKLOAD_IDENTITY_API_KEY`: Coze API密钥（已自动配置）
- `COZE_INTEGRATION_MODEL_BASE_URL`: 模型基础URL（已自动配置）
- `COZE_BUCKET_ENDPOINT_URL`: 对象存储端点（已自动配置）
- `COZE_BUCKET_NAME`: 对象存储桶名（已自动配置）

## 技术栈

- **后端**: FastAPI + LangGraph
- **语音识别**: Web Speech API + Coze ASR
- **实时通信**: WebSocket
- **前端**: HTML5 + JavaScript

## 许可证

MIT
