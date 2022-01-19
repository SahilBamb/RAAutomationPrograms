import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os.path


def DrawID(fn, ln, typeKind, count, let=True):

	df2 = pd.read_csv("IDTypes.csv",index_col='ID')
	data = {}
	for index, row in df2.iterrows():
		allNames = 'Inst InstSub MemberType templateName logoFile lx1 lx2 lx3 lx4 profilefileName px1 px2 px3 px4 is1 is2 isMain1 isMain2 mt1 mt2'
		allNames = allNames.split()
		dictTemp = {colName:row[colName] for colName in allNames}
		data[row['Inst']] = dictTemp

	inst = data[typeKind]['Inst']
	instSub = data[typeKind]['InstSub']
	logoPath =  data[typeKind]['logoFile']
	MemberType = data[typeKind]["MemberType"]
	profilefileName = data[typeKind]["profilefileName"]
	templateName = data[typeKind]["templateName"]

	isx = data[typeKind]['is1']
	isy = data[typeKind]['is2']

	template = Image.open(f"{templateName}")
	draw = ImageDraw.Draw(template)

	isMainx = data[typeKind]['isMain1']
	isMainy = data[typeKind]['isMain2']

	#Name of the Institution
	font = ImageFont.truetype("DAYROM__.ttf", size=180)
	draw.text((isMainx,isMainy), inst, font = font, fill='black')

	#Name of the Institution subtitle
	font = ImageFont.truetype("DAYROM__.ttf", size=120)
	draw.text((isx,isy), instSub, font = font, fill='black')

	x1 = int(data[typeKind]['lx1'])
	y1 = int(data[typeKind]['lx2'])
	x2 = int(data[typeKind]['lx3'])
	y2 = int(data[typeKind]['lx4'])

	#Logo Pasted
	pic = Image.open(logoPath).resize((x2-x1, y2-y1), Image.ANTIALIAS)
	template.paste(pic, (x1, y1, x2, y2))
	fileName = f"{profilefileName}{count}.jpg"

	x1 = int(data[typeKind]['px1'])
	y1 = int(data[typeKind]['px2'])
	x2 = int(data[typeKind]['px3'])
	y2 = int(data[typeKind]['px4'])

	#Profile Pasted
	pic = Image.open(fileName).resize((x2-x1, y2-y1), Image.ANTIALIAS)
	template.paste(pic, (x1, y1, x2, y2))

	#Writing the Name
	font = ImageFont.truetype("University.otf", size=70)
	if let:
		draw.text((70,815), fn+' '+ln, font = font, fill='black')

	mt1 = int(data[typeKind]['mt1'])
	mt2 = int(data[typeKind]['mt2'])

	#Writing the Title (Student)
	font = ImageFont.truetype("University.otf", size=140)
	draw.text((mt1,mt2), MemberType, font = font, fill='white')

	#ID Card Tag
	#font = ImageFont.truetype("Bebas-Regular.ttf", size=100)
	#draw.text((1333,1075), 'ID Card', font = font, fill='red')

	#Save the Image
	finalFileName = f'{fn} {ln}.jpg'
	template.save(finalFileName)
	print(f'Wrote the ID for {fn}')

df = pd.read_csv("students.csv",index_col='ID')

let = True
count = 0
for index, row in df.iterrows():
	count+=1
	fn = row['First Name'] 
	ln = row['Last Name'] 
	if row['First Name']==' ' and row['Last Name']==' ':
		fn = str(count)
		ln = ' '
		let = False
		
	#os.path.exists(path_to_file)
	
	if count<12: DrawID(fn, ln, 'Hotel', count,let)
	elif count<23: DrawID(fn, ln, 'Monster', count-11,let)
	elif count<37: DrawID(fn, ln, "Shrek's", count-22,let)
	else: DrawID(fn, ln, "Hotel", count-34,let)
	
