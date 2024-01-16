def check_answer(answer, input_line):
    # answerから特殊文字を削除
    answer = delete_special_char(answer)
    # 全て小文字に変換
    answer = answer.lower()
    # 改行を削除
    answer = answer.replace('\n', '')
    
    # input_lineから特殊文字を削除
    input_line = delete_special_char(input_line)
    # 全て小文字に変換
    input_line = input_line.lower()
    # 改行を削除
    input_line = input_line.replace('\n', '')
    
    if answer == input_line:
        return True
    else:
        return False


def delete_special_char(original_string):
    original_string = original_string.replace('\n', '')
    cleaned_list = [char for char in original_string if char.isalnum()]
    cleaned_string = "".join(cleaned_list)
    return cleaned_string


if __name__ == "__main__":
    with open('./last_exam.txt') as f:
        for line in f:
            if line == "\n":
                continue
            
            print(">> ", end="")
            input_line = input()
            if check_answer(line, input_line):
                print("Correct!")
            else:
                print("Incorrect!")
                print("Answer:\n " + line)
                print("Your answer:\n " + input_line)