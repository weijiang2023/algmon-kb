import json

def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

file_path = "../format/ch_single_choice_constructed_5K/ch_single_choice_train_3K.jsonl"
data = read_jsonl_file(file_path)
print(data[0]["qid"])
print(data[0]["problem"])
print(data[0]["answer_analysis"])
print(data[1])