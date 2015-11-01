import re
import codecs
import numpy as np
from os import path
import wordcloud as wc


fileList = ['transcripts/democrats_10_13_2015', 'transcripts/republicans_10_28_2015']
speakerOutputNames = ['trump', 'fiorina', 'sanders', 'clinton', 'carson', 'o\'malley', 'kasich']
speaker_words = {}

# read transcript contents into dictionary
for fi in fileList:
	transcript_file = codecs.open(fi, 'rb', 'utf-8')
	current_line = transcript_file.readline()
	while current_line != '':
		if re.search(r'[A-Z]+\:', current_line):
			current_line = current_line.replace('\n', ' ').replace('\u', '')
			split_line = current_line.split(": ")
			if split_line[0].lower() in speaker_words:
				speaker_words[split_line[0].lower()] += split_line[1]
			else:
				speaker_words[split_line[0].lower()] = split_line[1]
			current_line = transcript_file.readline().replace('/n', ' ').replace('\u', '')
			while not re.search(r'[A-Z]+\:', current_line):
				speaker_words[split_line[0].lower()] += current_line
				current_line = transcript_file.readline().replace('/n', ' ').replace('\u', '')
				if current_line == '':
					break

for name in speakerOutputNames:
	# take relative word frequencies into account, lower max_font_size
	wordcloud = wc.WordCloud(max_font_size=40).generate(speaker_words[name])
	image = wordcloud.to_image()
	image.show()
