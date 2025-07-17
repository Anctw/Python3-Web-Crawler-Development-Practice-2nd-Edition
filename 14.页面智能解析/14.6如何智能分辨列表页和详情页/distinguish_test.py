from gerapy_auto_extractor import is_detail, is_list, probability_of_list, probability_of_detail
from gerapy_auto_extractor.helpers import content, jsonify

html1 = content('sample1.html')
print(probability_of_detail(html1), probability_of_list(html1))
print(is_detail(html1), is_list(html1))

html2 = content('sample2.html')
print(probability_of_detail(html2), probability_of_list(html2))
print(is_detail(html2), is_list(html2))
