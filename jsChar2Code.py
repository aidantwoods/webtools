import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File to read from")
parser.add_argument("-o", "--output", help="If set, output will be supressed from console and written to file name specified")

args = parser.parse_args()

if args.file:
	i = open(args.file, 'r')
	a = i.read()
	i.close()
else:
	a = input("")

s = []
for l in a:
	s.append(str(ord(l)))

while s[-1] == '10':
	s.pop()

out = "String.fromCharCode("+",".join(s)+")"

if args.output:
	o = open(args.output, 'w')
	o.write(out)
	o.close()
else:
	print(out)
