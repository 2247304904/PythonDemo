from modelscope.pipelines import pipeline

classifier = pipeline('zero-shot-classification', 'damo/nlp_structbert_zero-shot-classification_chinese-large')

labels = ['家居', '旅游', '科技', '军事', '游戏', '故事']
sentence = '世界那么大，我想去看看'
classifier(sentence, candidate_labels=labels)
# {'labels': ['旅游', '故事', '游戏', '家居', '军事', '科技'],
#  'scores': [0.2843151092529297,
#   0.20308202505111694,
#   0.14530399441719055,
#   0.12690572440624237,
#   0.12382000684738159,
#   0.11657321453094482]}
#   预测结果为 "旅游"

classifier(sentence, candidate_labels=labels, multi_label=True)
# {'labels': ['旅游', '故事', '游戏', '科技', '军事', '家居'],
#  'scores': [0.7894195318222046,
#   0.5234490633010864,
#   0.41255447268486023,
#   0.2873048782348633,
#   0.27711278200149536,
#   0.2695293426513672]}
#   如阈值设为0.5，则预测出的标签为 "旅游" 及 "故事"