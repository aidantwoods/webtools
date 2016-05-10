import time, re

file_output = False
output_name = "cookies.json"

domain = input("Assign Cookies to (eg: '.example.com'): ")
expire = str(int(time.time() + 60*60*24*90)) #expire in 90 days
secure = "false"
session = "false"
httpOnly = "true"
hostOnly = "true"
path = "/"

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