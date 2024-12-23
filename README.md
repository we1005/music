# 高中歌单备份
**prompt**：*我想要一个python脚本，检测当前路径下的文件，以生成上面格式的json。如果检测到一个mp3文件的话，就将其文件名（除了.mp3的后缀）写入到title，author一律为“高中”  url写成“https://raw.githubusercontent.com/we1005/music/main/”和文件名（包括.mp3后缀）的拼接。pic字段则是文件名（除了.mp3的后缀）加上.jpg的后缀，lrc字段是文件名（除了.mp3的后缀）加上.lrc的后缀*

```python
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
```





```python
def process_line(line):
    # 删除前两个双引号（如果它们存在）
    if line.startswith('""'):
        line = line[2:]
    
    # 查找第三和第四个双引号（索引从0开始，所以这是第4个字符和第7个字符的位置）
    # 注意：这里假设双引号之间是合法的字符，且不考虑转义字符的情况
    quote_count = 0
    for i in range(len(line)):
        if line[i] == '"':
            quote_count += 1
            if quote_count == 3:
                # 将第三个双引号替换为单引号
                line = line[:i] + "'" + line[i+1:]
            elif quote_count == 4:
                # 将第四个双引号替换为单引号（注意此时第三个双引号已被替换为单引号）
                # 但由于我们已经替换了第三个，这里实际上是在找原字符串中的“第四个位置”的双引号
                # 由于索引已经因为替换而移动，我们需要稍微调整逻辑
                # 但在这个特定情况下，由于我们只替换而不添加字符，所以索引仍然是正确的
                # 重要的是要意识到，在更复杂的替换场景中，可能需要更复杂的逻辑来处理索引
                line = line[:i] + "'" + line[i+1:]
                break  # 找到第四个后就停止查找，避免不必要的替换
    
    return line

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            processed_line = process_line(line.strip())  # 去除行尾的换行符并处理
            outfile.write(processed_line + '\n')  # 写回换行符

# 使用示例
input_filename = 'lala.txt'  # 输入文件名
output_filename = 'output.txt'  # 输出文件名，或者可以设置为与输入文件名相同以覆盖原文件

process_file(input_filename, output_filename)
```





```
		{
            name: '1111',
            artist: '高中',
            url: 'https://raw.githubusercontent.com/we1005/music/main/(Don't Go)_EXO.mp3',
            cover: 'https://raw.githubusercontent.com/we1005/music/main/(Don't Go)_EXO.jpg',
            lrc: 'https://raw.githubusercontent.com/we1005/music/main/(Don't Go)_EXO.lrc'
        }
```

