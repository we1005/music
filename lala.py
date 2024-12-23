def remove_first_quote(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # 找到第一次出现的双引号的位置
                quote_index = line.find('"')
                if quote_index != -1:
                    # 删除第一次出现的双引号
                    line = line[:quote_index] + line[quote_index + 1:]
                outfile.write(line)
        print(f"Processed {input_file} and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用函数
input_file = 'haha.txt'
output_file = 'papa.txt'
remove_first_quote(input_file, output_file)