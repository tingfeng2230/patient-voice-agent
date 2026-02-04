# Render 部署指南

本项目支持一键部署到 Render 平台。

## 部署步骤

### 1. 推送代码到 GitHub

```bash
git init
git add .
git commit -m "Initial commit: Patient voice recording agent"
git branch -M main
git remote add origin https://github.com/你的用户名/项目名.git
git push -u origin main
```

### 2. 在 Render 创建 Web Service

1. 登录 [Render Dashboard](https://dashboard.render.com/)
2. 点击 **New +** → **Web Service**
3. 连接 GitHub 仓库
4. 配置以下信息：

#### 基础配置
- **Name**: `patient-voice-agent`（自定义）
- **Region**: 选择离你最近的区域
- **Branch**: `main`
- **Runtime**: `Python`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT`

#### 环境变量（自动配置）
以下环境变量由平台自动注入，无需手动配置：
- `COZE_WORKLOAD_IDENTITY_API_KEY`
- `COZE_INTEGRATION_MODEL_BASE_URL`
- `COZE_BUCKET_ENDPOINT_URL`
- `COZE_BUCKET_NAME`

5. 点击 **Create Web Service**

### 3. 等待部署

Render 会自动：
- 克隆代码
- 安装依赖
- 启动服务
- 分配公网URL

### 4. 访问应用

部署完成后，你会得到一个 URL：
```
https://patient-voice-agent.onrender.com
```

访问页面：
- 实时语音识别：`https://patient-voice-agent.onrender.com/static/recorder-realtime.html`

### 5. 配置环境变量（如需要）

如果需要额外的配置：

1. 在 Render Dashboard 进入你的服务
2. 点击 **Environment**
3. 添加环境变量
4. 点击 **Save Changes**
5. 服务会自动重启

## 注意事项

### 1. WebSocket 支持

Render 支持 WebSocket，无需额外配置。

### 2. 免费版限制

- 免费版会自动休眠（15分钟无访问后）
- 首次访问可能需要等待唤醒（30-60秒）
- 每月有运行时间限制

### 3. 付费版

如需生产使用，建议升级到付费版：
- 无休眠限制
- 更好的性能
- 更多资源

## 故障排除

### 问题：部署失败

检查：
- requirements.txt 是否完整
- Procfile 是否正确
- 代码语法是否有误

### 问题：访问超时

可能原因：
- 服务正在休眠，等待30-60秒唤醒
- 构建失败，查看日志

### 问题：WebSocket 连接失败

检查：
- 是否使用 HTTPS
- 是否正确配置了端口

## 域名配置（可选）

如需自定义域名：

1. 在 Render Dashboard 点击 **Domains**
2. 添加自定义域名
3. 配置 DNS 记录
4. 等待 SSL 证书生成

## 更新部署

代码更新后自动部署：

```bash
git add .
git commit -m "Update"
git push
```

Render 会自动检测并重新部署。
