from docx import Document


def get_text(text):
    text = text.strip().replace(" ", "").replace(u'\u3000', u' ').replace(u'\xa0', u' ')
    return text


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_que_title(text):
    texts = text.split("、")
    if texts and text[0] == "一":
        return True
    if len(texts) > 0 and is_number(text[0]):
        return True
    else:
        return False


def get_que_ans(para, que_item):
    # 1.判断被下划线标识的字段
    runs = para.runs
    if "ans" in que_item:
        ans = que_item['ans']
    else:
        ans = []
    for run in runs:
        if run.font.underline:
            ans.append(get_text(run.text))
    # 2.判断被括号包围的字段
    if "（" in para.text and "）" in para.text:
        an = para.text.split("（")[1].split("）")[0]
        if "A" in an or "B" in an or "C" in an or "D" in an:
            ans.append(an)
    if "(" in para.text and ")" in para.text:
        an = para.text.split("(")[1].split(")")[0]
        if "A" in an or "B" in an or "C" in an or "D" in an:
            ans.append(an)
    return ans


def config_que(que_item):
    if "。" in que_item['text']:
        content = que_item['text'].split("。")
        # print("content", content)
        que_item['title'] = que_item['text'].split("。")[0]
        que_item['options'] = que_item['text'].split("。")[1]
    if "）：" in que_item['text']:
        que_item['title'] = que_item['text'].split("）：")[0] + "）："
        que_item['options'] = que_item['text'].split("）：")[1]


if __name__ == '__main__':
    # 获得文档
    file = Document("resource/question.docx")
    que_num = 0
    que_item = None
    que_list = []
    # 按照段落读取文档内容
    for para in file.paragraphs:
        if not para.text: continue
        # if que_num==135:
        #     text=para.text
        #     print(que_num,text)
        if is_que_title(para.text):
            que_num = que_num + 1
            if que_item:
                que_list.append(que_item)
            que_item = {}
            que_item['num'] = que_num
            que_item['text'] = get_text(para.text)
            que_item['ans'] = get_que_ans(para, que_item)
        else:
            que_item['text'] = que_item['text'] + get_text(para.text)
            que_item['ans'] = get_que_ans(para, que_item)
            config_que(que_item)
        # print(que_item)
    for que in que_list:
        print(que)
        # if que and "ans" in que and len(que['ans']) <= 0:
        #     print(que)
        # if que and "options" in que and len(que['options']) <= 0:
        #     print(que)
