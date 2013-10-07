import urllib2
from bs4 import BeautifulSoup
import xlsxwriter

def open_file_html(file_name):
	f = open(file_name, 'r')
	a = f.read()
	return a


def output_data(html):
	workbook = xlsxwriter.Workbook('demo.xlsx')
	worksheet = workbook.add_worksheet()
	bold = workbook.add_format({'bold': 1})
	worksheet.write('A1', '#', bold)
	worksheet.write('B1', 'APOS ID', bold)
	worksheet.write('C1', 'Posting Date', bold)
	worksheet.write('D1', 'Position Title', bold)
	worksheet.write('E1', 'Posted From TTMS', bold)
	worksheet.write('F1', 'Location', bold)
	worksheet.write('G1', 'Division', bold)
	worksheet.write('H1', 'Status', bold)
	worksheet.write('I1', 'End Date', bold)
	worksheet.write('J1', 'Posted By', bold)


	i=1
	while i <= 20:
		soup = BeautifulSoup(html, "lxml")

		class_name = "TR" + str(i%2 + 1)
		k = (i-1)/2
		

		name = soup('tr', {'class': class_name})[k] 

		all_td = name.find_all('td')
		js_id = all_td[0].text
		apos_id = all_td[1].text
		posting_date = all_td[2].text
		position_title = all_td[3].table.form.tr.td.a.text

		if '|' in position_title:
			ttms = 'YES'
		else:
			ttms = 'NO' 

		if all_td[3].table.form.tr.td.i:
			location = all_td[3].table.form.tr.td.i.text

		division = location.split(',')[0]
		status = all_td[-3].text
		end_date = all_td[-2].text
		posted_by = all_td[-1].text

		worksheet.write(i, 0, js_id[:-1])
		worksheet.write(i, 1, apos_id)
		worksheet.write(i, 2, posting_date)
		worksheet.write(i, 3, position_title)
		worksheet.write(i, 4, ttms)
		worksheet.write(i, 5, location)
		worksheet.write(i, 6, division)
		worksheet.write(i, 7, status)
		worksheet.write(i, 8, end_date)
		worksheet.write(i, 9, posted_by)

		i+=1
	return

# test.txt is a HTML file of the Jobstreet Advertisement page to be scrapped. This file is currently created, copied/pasted manually. 
output_data(open_file_html("test.txt"))