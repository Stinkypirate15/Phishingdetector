import language_tool_python
import urllib
import re
import requests
import json
import time
import pandas as pd 
import os

def main(N):
    printFish(N)
    print("Welcome to the phising detector")
    time.sleep(2)
    while True:
        user_choice= input(f"\nplease input which tool you would like to use the tools avalible are \n url validator \n grammar checker\n quit\n enter your choice here: ").lower()
        if user_choice == "url validator":
         url_checker()
              
        elif user_choice=="grammar checker":
         grammarcheck()
        elif user_choice=="quit":
            break
        else: print("Please input a valid choice")
    
       


def url_checker():
    try:
        url_input = input("Please enter the URL you would like to check: ")  # Prompts user to input their URL

        encoded_url = urllib.parse.quote(url_input, safe='')
        api_url = f"insert your personal api line here (i use ip quality score){url_input}"  # Uses the API to check if the URL is safe or not
        response = requests.get(api_url + encoded_url)
        data = response.json()  # Parse the JSON response

        # Print the JSON response for the user
        print(json.dumps(data, indent=4))

        # Flatten the JSON data for better readability
        flattened_data = {}
        for key, value in data.items():
            if isinstance(value, dict):  # If the value is a nested dictionary, flatten it
                for sub_key, sub_value in value.items():
                    flattened_data[f"{key}_{sub_key}"] = sub_value
            else:
                flattened_data[key] = value

        # Ask the user if they want to save the information to a file
        while True:
            user_input = input("Would you like to save the info to a file? (Y or N): ").strip().lower()
            if user_input == "y":
                # Convert the flattened JSON data into a DataFrame
                df = pd.DataFrame([flattened_data])  # Wrap the flattened data in a list to create a single-row DataFrame
                # Save the DataFrame to a CSV file
                csv_filename = f"url.csv"  # Replace slashes in the URL to avoid file path issues
                file_exists = os.path.isfile(csv_filename)#checks to see if file exist
                df.to_csv(csv_filename, mode='a', index=False, header=not file_exists)  # Append to the file if it exists
                print(f"Data saved to {csv_filename}")
                break  # Exit the loop
            elif user_input == "n":
                print("Data not saved.")
                break  # Exit the loop
            else:
                print("Please input a valid choice (Y or N).")

        time.sleep(3)  # Pause for a moment before returning to the main loop

    except json.JSONDecodeError:  # Handles JSON decoding errors
        print("Error: Unable to decode the JSON response. Please check the API or the URL.")
        time.sleep(3)
    except requests.exceptions.RequestException as e:  # Handles general request-related errors
        print(f"Error: A request error occurred - {e}")
        time.sleep(3)
    except Exception as e:  # Handles any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        time.sleep(3)
    
        
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
                time.sleep(3)

    except FileNotFoundError:
        print(f"Error: File '{user_text}' not found.")
        time.sleep(3)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        time.sleep(3)
    






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
