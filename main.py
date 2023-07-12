# -*- coding: utf-8 -*-
from Embedding import *
from NonDiacritics import removeDiacritics
from Diacritics import addDiacritics

sentence = """‌‌المبحث الثاني: حياته العلمية.
بداية طلبه للعلم:
بَكَّر الإمام أحمد رحمه الله في الطّلب، وقد بدأ بالاختلاف إلى الكُتّاب، ثم إلى الدّيوان وهو لم يتجاوز الخامسة عشر من عمره، وطلب الحديث وأكثر منه.
قال المرّوذي: قال لي أبو عبد الله: "اختلفت إلى الكتّاب ثم اختلفت إلى الديوان، وأنا ابن أربع عشرة سنة".
قال عبد الله بن أحمد رحمه الله: "وأول شيء طلب الحديث في سنة تسع وسبعين، في السنة التي مات فيها مالك وحماد بن زيد" .
وقال المرّوذي: "طلبت الحديث سنة تسع وسبعين، فسمعت بموت حماد بن زيد وأنا في مجلس هشيم، وقال: سمعت من علي بن هاشم بن البريد سنة تسع وتسعين في أول سنة طلبت الحديث".
وكذلك كتب في هذه السنة عن علي بن ثابت الجزري، فقد قال عبد الله ابنه: سمعت أبي يقول في سنة تسع وعشرين ومائتين: "كتب عن علي بن ثابت منذ خمسين سنة" """


#removeDiacritics(sentence)
addDiacritics(sentence)
#obtainSimmilarWords('قلب')

# word2Vectector("فتح",'"فَتَحَ"')