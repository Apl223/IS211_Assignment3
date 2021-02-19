# URL: http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
import argparse
import urllib.request
import csv
import re
from io import StringIO

def downloadData(url):
	csvData=urllib.request.urlopen(url).read().decode("ascii","ignore") 
	return csvData

dataDict=[]
dataDict2=[]

def processData(file):
	data=StringIO(file)

	# read csv file
	csv_reader = csv.reader(data, delimiter=',')

	for lines in csv_reader:
		dataDict.append(str(lines[0]))
		dataDict2.append(str(lines[2]))

	images = countimages(dataDict)
	browser = countbrowser(dataDict2)
	
	print(f"Image requests account for {images} % of all requests")
	print("Largest number is:", max(browser)) 

def countimages(data):
	#You need to make a counter variable for ever
	#image that is found and use that to calculate the percentage.
	linescounter = 0;
	counter = 0;
	counter2 = 0;
	counter3 = 0;
	counter4 = 0;
	counter5 = 0;

	for lines in data:
		linescounter += 1

	JPG = re.findall(".JPG", str(data))
	for x in JPG:
		counter += 1

	PNG = re.findall(".PNG", str(data))
	for x in PNG:
		counter2 += 1

	gif = re.findall(".gif", str(data))
	for x in gif:
		counter3 += 1

	GIF = re.findall(".GIF", str(data))
	for x in GIF:
		counter4 += 1

	jpg = re.findall(".jpg", str(data))
	for x in jpg:
		counter5 += 1

	imagetotal = counter + counter2 + counter3 + counter4 + counter5
	percentage = 100 * (imagetotal / linescounter)
	return percentage

def countbrowser(data):
	counter = 0;
	counter2 = 0;
	counter3 = 0;
	counter4 = 0;

	Firefox = re.findall("Firefox", str(data))
	for x in Firefox:
		counter += 1

	Chrome = re.findall("Chrome", str(data))
	for x in Chrome:
		counter2 += 1

	IE = re.findall("Internet Explorer", str(data))
	for x in IE:
		counter3 += 1

	Safari = re.findall("Safari", str(data))
	for x in Safari:
		counter4 += 1

	browsercounts = [counter,counter2,counter3,counter4]
	return browsercounts

def main(url):
	print(f"Running main with URL = {url}...")
	try:
		csvData=downloadData(args.url)
	except:
		print("An error has occured. Please try again")
		exit()

	personData=processData(csvData)

if __name__ == "__main__":
	"""Main entry point"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
	args = parser.parse_args()
	main(args.url)