import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File to read from")
parser.add_argument("-o", "--output", help="If set, output will be supressed from console and written to file name specified")
parser.add_argument("-r", "--removetext", help="Set this option to remove String.fromCharCode(...) text, and just get encoded output", action="store_true", default=False)
parser.add_argument("-n", "--retainnewline", help="Set this option to retain trailing newlines at end of file", action="store_true", default=False)

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

while (not args.retainnewline) and s[-1] == '10':
	s.pop()

enc = ",".join(s)
if args.removetext:
	out = enc
else:
	out = "String.fromCharCode("+enc+")"

if args.output:
	o = open(args.output, 'w')
	o.write(out)
	o.close()
else:
	print(out)
