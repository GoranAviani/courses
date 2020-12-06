#The Test in one of Big 5

#Inspiration from:
#https://dev.to/albinotonnina/how-to-lose-a-it-job-in-10-minutes-35pi

#['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris']
#// YOUR ALGORITHM
#[
#    [ 'Tokyo', 'Kyoto' ],
#    [ 'London', 'Donlon' ],
#    [ 'Rome' ],
#    [ 'Paris' ]
#]
#That’s it.* If you rotate the letters of each city you may or may not match
#another city. In case you do, put them together in a array on their own.*


def rotate_word(userInput, cities):

    userInputChange = ""
    userinputStage = userInput
    result = []

    for x in range(len(userInput)):
        userInputChange = userinputStage[x::] + userinputStage[:x]
        for y in cities:
            if userInputChange.lower() in y.lower():
                if userInputChange.lower() not in result:
                    result.append(userInputChange[:1].upper() + userInputChange[1:].lower())
                    #result.append(userInputChange.lower())
                #print(userInputChange)
    return (result)

def main():
    cities = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris']

    userInput = input("Enter city name: ")
    result = rotate_word(userInput, cities)
    print(result)

if __name__ == "__main__":
    main()


