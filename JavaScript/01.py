links = list()
aquott = 0

url = ''

while url != 'exit':
    url = input('Enter the URL you want to add, or type exit: ')
    links.append(url)
else:
    print("""
function generate(){
var aquote = new Array;
""")
    for url in links:
        print('aquote[' + str(aquott) + ']="\\ '+ url + '";')
        aquott +=1

    print("""
rdmQuote = Math.floor(Math.random()*aquote.length);
document.getElementById("generate-box").value=aquote[rdmQuote];
}
""")
