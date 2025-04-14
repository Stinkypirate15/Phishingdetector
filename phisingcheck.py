import language_tool_python
import urllib
import re
import requests
import json
import time

def main(N):
    printFish(N)
    print("Welcome to the phising detector")
    time.sleep(2)
    while True:
        user_choice= input(f"please input which tool you would like to use the tools avalidble are \n url validator \n grammar chcecker\n quit\n enter your choice here: ")
        if user_choice == "url validator":

            url_checker()
            # grammarcheck(user_text)
            if url_checker():  # Call url_checker without arguments
                print("This is a valid url but be cautious")
            else:
                print("No this is not a valid url")
        if user_choice=="grammar checker":
            grammarcheck()
        if user_choice=="quit":
            break
        else: print("Please input a valid choice")
    
       


def url_checker():
    try:
        url_input = input("please enter the url you would like to check: ")  # Prompts user to input their URL
    
   
        encoded_url = urllib.parse.quote(url_input, safe='')
        api_url = f"insert your personal api line here (i use ip quality score){url_input}"#uses the api to check if the url is safe or not
        data = requests.get(api_url + encoded_url)
        print(json.dumps(data.json(), indent=4))#prints out the information regarding if the url is safe or not and the information in relation
    except json.JSONDecodeError:  # Handles JSON decoding errors
        print("Error: Unable to decode the JSON response. Please check the API or the URL.")
    except requests.exceptions.RequestException as e:  # Handles general request-related errors
        print(f"Error: A request error occurred - {e}")
        url_checker()
    except Exception as e:  # Handles any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    main()
        
def grammarcheck():
    user_text = input("please enter the name of your document or text file: ")
    try:
        tool = language_tool_python.LanguageToolPublicAPI('en-US')  # Initializes LanguageTool
        with open(user_text, "r", encoding="utf-8") as external_text:#opens the document provided
            text_content = external_text.read()
            matches = tool.check(text_content)

            print(f"Number of grammar issues found: {len(matches)}")#prints out the number of grammar issues found
            for match in matches:
                print(f"Error: {match.ruleId} - {match.message}")
                print(f"Context: {match.context}")

    except FileNotFoundError:
        print(f"Error: File '{user_text}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    main()

def printFish(N) :#prints fish
 
    spaces1 = ""; spaces2 = "";
    stars1 = "*"; stars2 = "";
    for i in range(N) :
        spaces1 += ' ';
 
    spaces2 = spaces1;
 
    for i in range( 2 * N + 1) :
        # For upper part
        if (i < N) :
            print(spaces1,end="");
            print(stars1,end="");
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);
            spaces1 = spaces1[:-1]
            stars1 += "**";
            stars2 += "*";
 
        # For middle part
        if (i == N) :
            print(spaces1,end="");
            print(stars1,end="");
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);
 
        # For lower part
        if (i > N) :
            spaces1 += ' ';
            stars1 = stars1[:-1];
            stars1 = stars1[:-1];
            stars2 = stars2[:-1];
             
            print(spaces1,end="");
            print(stars1,end="")
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);
if __name__ == "__main__" :
 
    N = 5;
    main(N);
