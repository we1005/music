import os
import json

# 定义GitHub原始内容的基础URL
base_url = "https://raw.githubusercontent.com/we1005/music/main/"

# 初始化一个空列表来存储音乐信息
music_list = []

# 获取当前工作目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 检查文件是否以.mp3结尾
    if filename.endswith(".mp3"):
        # 提取文件名（去除.mp3后缀）
        title = os.path.splitext(filename)[0]
        
        # 构建各个字段的值
        author = "高中"
        url = f"{base_url}{filename}"
        pic = f"{base_url}{title}.jpg"
        # 注意：这里假设.lrc文件可能不存在，但在JSON中仍然包含该字段的占位符
        lrc = f"{base_url}{title}.lrc"
        
        # 将音乐信息添加到列表中
        music_list.append({
            name: title,
            artist: author,
            url: url,
            cover: pic,
            lrc: lrc
        })

# 将音乐信息列表转换为JSON格式的字符串，并写入outcome.json文件
with open("outcome.json", "w", encoding="utf-8") as f:
    json.dump({"audio": music_list}, f, indent=4, ensure_ascii=False)

print("JSON数据已写入outcome.json文件")