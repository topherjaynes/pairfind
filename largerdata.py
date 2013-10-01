import codecs
"""
used to generate larger date from basefile 
"""

file_of_artists = codecs.open('larger.txt', 'rb', encoding="UTF-8")
w = open('largest.txt', 'w')

for a in file_of_artists:
     for i in range(10):
             w.write(a.encode("utf-8"))