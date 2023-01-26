# hrtoxpred

## Requirements
* Python >= 3.6
* torch >= 1.1
* six >= 1.12.0
* argparse
* packaging
* rdkit 2022.9.2
* scikit-learn 1.1.3

## Run Script
```
python -u run_classifier_chem.py \
--pretrained_model_path pretrained_model/hrmolbert.bin \
--vocab_path corpora/vocab.txt \
--train_path finetune_data/BACE/BACE_fp_rad2_addhs_train.txt \
--dev_path finetune_data/BACE/BACE_fp_rad2_addhs_dev.txt \
--test_path finetune_data/BACE/BACE_fp_rad2_addhs_test.txt \
--seq_length 512 \
--epochs_num  32 \
--batch_size 8 \
--tokenizer space \
--embedding word_pos_seg \
--encoder transformer \
--mask fully_visible \
--finetune_target BACE
```
The pretrained model hrmolbert.bin is available from https://drive.google.com/file/d/13PHT4krOuV4A7cwJWdEnRb-69vZjYs3K/view?usp=share_link
### The full code will be released after our paper is accepted
