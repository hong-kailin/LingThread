from striprtf.striprtf import rtf_to_text


def split_text_by_line(text, max_length=6000):
    """
    按换行符分割文本，并确保每段不超过指定长度

    参数:
    text (str): 需要分割的原始文本
    max_length (int): 每段的最大字符数，默认为1500

    返回:
    list: 分割后的文本段落列表
    """
    if not text:
        return []

    paragraphs = []
    current_paragraph = ""

    # 按行分割文本
    lines = text.split('\n')

    for line in lines:
        # 如果添加当前行后会超过最大长度，则将当前段落添加到结果中并开始新段落
        if len(current_paragraph) + len(line) + 1 > max_length:  # +1 是为换行符
            if current_paragraph:  # 避免添加空段落
                paragraphs.append(current_paragraph)
            current_paragraph = line
        else:
            # 否则将当前行添加到当前段落，并添加换行符
            if current_paragraph:
                current_paragraph += '\n' + line
            else:
                current_paragraph = line  # 处理第一个段落

    # 添加最后一个段落
    if current_paragraph:
        paragraphs.append(current_paragraph)

    return paragraphs


with open(
        r"C:\Users\1\Desktop\哈利波特（英文版电子书）\格式： rtf\1 - Harry Potter and the Philosopher's Stone.rtf") as infile:
    content = infile.read()
    text = rtf_to_text(content)

long_text = text.replace('‘', '\'').replace('’', '\'')

segments = split_text_by_line(long_text, max_length=6000)

# 打印每段的长度和内容
for i, segment in enumerate(segments):
    print(f"段落 {i + 1} (长度: {len(segment)}):")
    print(segment)
    print("-" * 50)
