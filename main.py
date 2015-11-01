import re
import codecs
import pywordcloud as pyw


fileList = ['transcripts/democrats_10_13_2015', 'transcripts/republicans_10_13_2015']
speakerOutputNames = ['trump', 'fiorina', 'sanders', 'clinton', 'carson', 'o\'malley', 'kasich']
speaker_words = {}

# read transcript contents into dictionary
for fi in fileList:
	transcript_file = codecs.open(fi, 'rb', 'utf-8')
	current_line = transcript_file.readline()
	while current_line != '':
		if re.search(r'[A-Z]+\:', current_line):
			current_line = current_line.replace('\n', ' ')
			split_line = current_line.split(": ")
			if split_line[0].lower() in speaker_words:
				speaker_words[split_line[0].lower()] += split_line[1]
			else:
				speaker_words[split_line[0].lower()] = split_line[1]
			current_line = transcript_file.readline().replace('/n', ' ')
			while not re.search(r'[A-Z]+\:', current_line):
				speaker_words[split_line[0].lower()] += current_line
				current_line = transcript_file.readline().replace('/n', ' ')
				if current_line == '':
					break

for name in speakerOutputNames:
	pyw.create(speaker_words[name],
			outfile="output/" + name + ".html",
			uppercase=False,
			showfreq=False,
			frequency=100,
			removepunct = True,
			minfont = 1,
			maxfont = 8, 
	        hovercolor="green", 
	        showborder=False, 
	        fontfamily='calibri', 
	        width="1100px", 
	        height="400px"
	        )