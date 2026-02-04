import base64
import os
from langchain.tools import tool
from langchain.tools import ToolRuntime
from coze_coding_dev_sdk import ASRClient
from coze_coding_utils.runtime_ctx.context import new_context


@tool
def voice_recognition(audio_url: str, runtime: ToolRuntime = None) -> str:
    """
    语音识别工具，将音频文件转换为文本。

    支持音频格式：MP3、WAV、OGG OPUS
    音频要求：时长≤2小时，大小≤100MB

    Args:
        audio_url: 音频文件的URL地址（支持HTTP/HTTPS链接）

    Returns:
        str: 识别出的文本内容

    Example:
        >>> voice_recognition(audio_url="https://example.com/audio.mp3")
        "患者张三说，我最近感觉头晕，已经持续三天了..."
    """
    ctx = runtime.context if runtime else new_context(method="voice.recognition")
    
    try:
        client = ASRClient(ctx=ctx)
        
        # 使用URL进行语音识别
        recognized_text, data = client.recognize(
            uid="patient_form_user",
            url=audio_url
        )
        
        return recognized_text
        
    except Exception as e:
        return f"语音识别失败: {str(e)}"


@tool
def voice_recognition_base64(audio_base64: str, runtime: ToolRuntime = None) -> str:
    """
    语音识别工具，将Base64编码的音频数据转换为文本。

    支持音频格式：MP3、WAV、OGG OPUS
    音频要求：时长≤2小时，大小≤100MB

    Args:
        audio_base64: Base64编码的音频数据字符串

    Returns:
        str: 识别出的文本内容

    Example:
        >>> voice_recognition_base64(audio_base64="UklGRiQAAABXQVZFZm10IBIA...")
        "患者李四说，我今天早上测量血压，高压是140，低压是90..."
    """
    ctx = runtime.context if runtime else new_context(method="voice.recognition")
    
    try:
        client = ASRClient(ctx=ctx)
        
        # 使用Base64数据进行语音识别
        recognized_text, data = client.recognize(
            uid="patient_form_user",
            base64_data=audio_base64
        )
        
        return recognized_text
        
    except Exception as e:
        return f"语音识别失败: {str(e)}"
