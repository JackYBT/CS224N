# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

eval_corpus_path = "../birth_dev.tsv"

total, correctLondon = utils.evaluate_places(
    eval_corpus_path, ['London' for _ in open(eval_corpus_path, encoding='utf-8')])
print("total", total)
print("correctLondon", correctLondon)
print(
    f"Accuracy of baseline that predicts 'London' for every example: {correctLondon/total}")
