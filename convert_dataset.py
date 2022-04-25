import re

import pandas as pd


def convert_train(path):
    labels = []
    contents = []
    with open(path, encoding="utf-8") as f:
        data = f.read()
    data = re.split('train_[0-9][0-9][0-9][0-9][0-9][0-9]', data)
    data = [d.strip() for d in data if len(d) != 0]
    for ele in data:
        temp = ele.split('\n')
        temp = [t for t in temp if len(t) != 0]
        label = int(temp[-1])
        content = ' '.join(temp[0:len(temp) - 1])
        contents.append(content)
        labels.append(label)
    df = pd.DataFrame({'Content': contents,
                       'Label': labels})
    return df


def convert_test(path):
    with open(path, encoding="utf-8") as f:
        data = f.read()
    data = re.split('test_[0-9][0-9][0-9][0-9][0-9][0-9]', data)
    data = [d.strip()[1:len(d) - 1] for d in data if len(d) != 0]
    labels = [None for _ in range(len(data))]
    df = pd.DataFrame({'Content': data,
                       'Label': labels})
    return df


if __name__ == "__main__":
    data_frame = convert_test(r"D:\pycharm\Sentiment-Analysis-With-Pseudo-Labeling\data\test.crash")
    data_frame.to_csv("D:\pycharm\Sentiment-Analysis-With-Pseudo-Labeling\data\data_csv\data_without_label.csv",
                      index=False)
