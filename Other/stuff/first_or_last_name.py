# If user has his entire fist name and last name saved in only one field then use the field 
# that has the information,
#  else use both fields 

users = [
    {"user": 5, "firstname" : "Rade", "lastname" : "Koncar"},
    {"user": 7, "firstname" : "Rei Ayanami", "lastname" : ""},
    {"user": 8, "firstname" : "", "lastname" : "Guts Berserk"},
    {"user": 18, "firstname" : "", "lastname" : ""},
    {"user": 7, "firstname" : "Ivo", "lastname" : "Lola Ribar"}
]
result = ""

for user in users:
    #print(user)
    #print(user["firstname"])
    if len(user["firstname"]) == 0:
        if len(user["lastname"]) > 2:
            result = user["lastname"]
        else:
            result = "user {} has no first and last name" .format(user["user"])

    else:
        if len(user["lastname"]) == 0:
            result = user["firstname"]
        else:
            result = user["firstname"] + " " + user["lastname"]

    print(result)
