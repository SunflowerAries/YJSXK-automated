本文档介绍 CRNN 模型的训练流程，目前整个训练流程还稍显繁琐，后续会进一步调整。

## 准备数据

CRNN 模型训练只需训练集与测试集数据，目前训练集对应 alldata 目录下的图片以及 log-train 中的标注（按照图片名称字典序依次标注），测试集则为 alldata-val 以及 log-val 中的标注。

需先通过

```bash
python3 new_data.py
```

生成 lmdb 文件夹（new_data.py 中第 3、7、11 行分别对应数据集的标注、数据集、以及数据集生成的 lmdb 文件夹）

接着运行

```bash
python3 train.py --trainroot trainset_lmdb --valroot valset_lmdb --pretrained data/crnn.pth
```

进行训练，其中 trainroot、valset_lmdb 分别对应上一步生成的训练集和测试集 lmdb 文件夹，pretrained 为预训练模型，可以在 [Baidu Netdisk](https://pan.baidu.com/s/1pLbeCND) 获得，训练参数可见 train.py，包括 learning rate、batchsize 等。

**经初步验证，基于预训练模型的 finetune 正确率显著低于预训练模型（13% 左右）**，请对本项目感兴趣且有深度学习背景者通过 sunflowerinaries@gmail.com 联系开发者，共同提升模型性能。