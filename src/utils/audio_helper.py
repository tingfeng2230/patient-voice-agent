import os
import base64
import uuid
from typing import Tuple


def save_audio_from_base64(audio_base64: str, audio_format: str = "webm") -> Tuple[str, str]:
    """
    将Base64编码的音频数据保存到临时文件
    
    Args:
        audio_base64: Base64编码的音频数据
        audio_format: 音频格式（默认为webm）
    
    Returns:
        Tuple[str, str]: (文件路径, 文件URL)
    """
    # 生成唯一文件名
    filename = f"audio_{uuid.uuid4().hex}.{audio_format}"
    
    # 使用/tmp目录保存临时文件
    temp_dir = "/tmp"
    filepath = os.path.join(temp_dir, filename)
    
    # 解码Base64数据并保存
    audio_data = base64.b64decode(audio_base64)
    with open(filepath, 'wb') as f:
        f.write(audio_data)
    
    # 返回文件路径和本地文件URL（使用file://协议）
    file_url = f"file://{filepath}"
    
    return filepath, file_url


def cleanup_audio_file(filepath: str):
    """
    清理临时音频文件
    
    Args:
        filepath: 要删除的文件路径
    """
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        # 即使删除失败也不影响主流程
        print(f"Warning: Failed to cleanup audio file {filepath}: {e}")
