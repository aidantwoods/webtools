import time, re, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fileoutput", help="Output cookie JSON to file", action="store_true")
parser.add_argument("-c", "--secure", help="Set secure flag", action="store_true")
parser.add_argument("-t", "--httponly", help="Set httpOnly flag", action="store_true")
parser.add_argument("-o", "--hostonly", help="Set hostOnly flag", action="store_true")
parser.add_argument("-s", "--session", help="Set session flag", action="store_true")
parser.add_argument("-p", "--path", help="Set cookie path", default="/")
parser.add_argument("-n", "--outputname", help="Set output cookie JSON file name", default="cookies.json")
parser.add_argument("domain", help="Assign Cookies to (eg: '.example.com')")
parser.add_argument("-e", "--expire", help="Seconds after current time to expire cookies", type=int, default=60*60*24*90)

args = parser.parse_args()

file_output = args.fileoutput
output_name = args.outputname

domain = args.domain
expire = str(int(time.time() + args.expire))

secure = session = httpOnly = hostOnly = "false"

if args.secure:
    secure = "true"
if args.session:
    session = "true"
if args.httponly:
    httpOnly = "true"
if args.hostonly:
    hostOnly = "true"

path = args.path

st = input("Cookie Delimited Format: ")
st = re.sub(r'([^;=]+)(?:=)([^;]*)', r'\1",\n"value": "\2', st)

i=0
while st.find("; ") > 0:
    i+=1
    st = st.replace("; ",
                    "\",\n\"domain\": \"" + domain +
                    "\",\n\"id\": " + str(i) +
                    ",\n\"expirationDate\": " + expire +
                    ",\n\"hostOnly\": " + hostOnly +
                    ",\n\"httpOnly\": " + httpOnly +
                    ",\n\"path\": \"" + path +
                    "\",\n\"secure\": " + secure +
                    ",\n\"storeId\": \"0\","
                    "\n\"session\": " + session +
                    "\n},\n{\n\"name\": \"", 1)

st = st.replace("Cookie: ", "[\n{\n\"name\": \"", 1)
st = st + \
    "\",\n\"domain\": \"" + domain + \
    "\",\n\"id\": " + str(i + 1) + \
    ",\n\"expirationDate\": " + expire + \
    ",\n\"hostOnly\": " + hostOnly + \
    ",\n\"httpOnly\": " + httpOnly + \
    ",\n\"path\": \"" + path + \
    "\",\n\"secure\": " + secure + \
    ",\n\"storeId\": \"0\"," \
    "\n\"session\": " + session + "\n}\n]"

if file_output:
    out = open(output_name, 'w')
    out.write(st)
    out.close()
else:
    print(st)