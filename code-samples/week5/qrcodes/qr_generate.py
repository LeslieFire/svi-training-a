import csv
import pyqrcode
import os
import glob
import qrtools

def csv_convert(file):
	'''
	convert csv to list.
	'''

	with open(file, 'rb') as f:
		reader = csv.reader(f)
		your_list = list(reader)

	my_list = [i[0] for i in your_list]

	return my_list[1:]

def qr_create(my_list):
	'''
	to create qr codes from productcode.
	'''

	for i in my_list:
		#version specifies the size and data capacity of the code,
		#version defaults to the minimum possible value but for
		#the sake of uniformity, we assign it a set value of 2.
		code = pyqrcode.create(str(i),version=2)
		print code
		filename = 'QR_' + str(i) + '.png'

		#scale dictates how large the qr code is, for the sake of
		#uniformity, we gave it a value of 3.
		code.png(filename, scale=3)

def test_if_correct(productcode_lists,outpath):
	'''
	check qr codes for errors.
	'''

	print 'checking qr code for errors...'
	os.chdir(outpath)
	image_list = os.listdir(outpath)

	productcode_one_list = []

	for i in productcode_lists:
		productcode_one_list.extend(i)

	count = 0
	for image in image_list:
		qr = qrtools.QR()
		qr.decode(image)

		if qr.data not in productcode_one_list:
			count += 1
			print qr.data, 'not in list'

	if count == 0:
		print 'all qr codes are correct.'

if __name__ == '__main__':

#	product_list = csv_convert('Maxalto.csv')
	csv_list = glob.glob(os.path.join(os.getcwd(),'*.csv'))
	productcode_lists = [csv_convert(x) for x in csv_list]

	if not os.path.exists('out'):
		os.makedirs('out')
	outpath = os.path.join(os.getcwd(), 'out')	
	os.chdir(outpath)

	for productcode_list in productcode_lists:
		qr_create(productcode_list)

	test_if_correct(productcode_lists,outpath)
