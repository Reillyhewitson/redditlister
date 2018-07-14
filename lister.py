import requests
import webbrowser
print('you can press ctrl-c to exit')
while True:
    try:
        sub = str(input('Hey what sub do you want to look at? '))
        request = requests.get('https://www.reddit.com/r/'+sub+'.json')
        result = request.json()
        #print(result)
        num = -1
        for i in result['data']['children']:
            num += 1
            print(num, result['data']['children'][num]['data']['title'])
            
        link = int(input('Please select the post you want to read: '))
        webbrowser.open(result['data']['children'][link]['data']['url'])
    except KeyError:
        print('oops. We seem to have had an issue, please try again later')
        break
    except KeyboardInterrupt:
        break
    except:
        print('ah well, seems like something went wrong.')
