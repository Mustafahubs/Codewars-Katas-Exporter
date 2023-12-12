from requests import session
from lxml.html import fromstring
from time import sleep
import requests
import csv,json,os,sys

class Codewars_Scraper():
    def __init__(self):
        self.headers = {
            'authority': 'www.codewars.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.codewars.com',
            'referer': 'https://www.codewars.com/users/sign_in',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        }

    def Read_cred(self):
        with open('config.json') as json_data_file:
            config = json.load(json_data_file)

        email = config['email']
        password = config['password']
        return email,password
    
    def get_authenticity_token(self,sess):
        login_page_resp = sess.get('https://www.codewars.com/users/sign_in')
        login_page = fromstring(login_page_resp.text)
        authenticity_token = login_page.xpath('//input[@name="authenticity_token"]/@value')[0]
        return authenticity_token
    
    def login_Process(self,sess,authenticity_token,email,password):
        data = {
        'utf8': '\u2713',
        'authenticity_token': str,
        'user[email]': str,
        'user[password]': str,
        'user[remember_me]': 'true'
        }
        data['authenticity_token'] = authenticity_token
        data['user[email]'] = email
        data['user[password]'] = password
        login_resp = sess.post('https://www.codewars.com/users/sign_in', headers=self.headers, data=data)
        if login_resp.status_code == 200:
            print(f'[INFO] Login Response:- {login_resp.status_code}')
            User_SoupTree = fromstring(login_resp.text)
            userName = User_SoupTree.xpath('//a[@id="header_profile_link"]')[0].get('href')
            return userName
        else:
            print(f'[INFO] Login Reponse Error:- {login_resp.status_code}!')
    
    def Solution_Header(self):
        headers = {
            'authority': 'www.codewars.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
            'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY0M2NiNTMyN2JlN2MyMDAzMTMzZTBhMiIsImV4cCI6MTcwMzI0NjQ5M30.iIixj1aXxfXRPDJz5FpeiCgAF4Q-0VfiBqJF0EiVgag',
            'referer': 'https://www.codewars.com/users/Ahmad786profan/completed_solutions',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-csrf-token': 'BuGs1bDZ7LeVq/CUTPpqlXPX8VMvEa63QqyoLr86aDN+0C1EaXnC16WlxkBQ2NpXjg5eG0qFPWd8sJNfI5J8TQ==',
            'x-requested-with': 'XMLHttpRequest',
        }
        return headers
    
    def solution_Resp(self,sess,userName,page):
        params = {
            'page': str(page),
        }
        response = sess.get(
            f'https://www.codewars.com{userName}/completed_solutions',
            params=params,
            headers= self.Solution_Header()
        )
        if response.status_code == 200:
            soupTree = fromstring(response.text)
            kata_items = soupTree.xpath('//div/div[@class="list-item-solutions"]')
            return kata_items
        else:
            print(f'[INFO] Response Error.{response.status_code}')

    def get_all_Solution(self,kata_itemsTag):
        kata_items = kata_itemsTag
        codewar_domain = 'https://www.codewars.com'
        for item in kata_items:
            title_tag = item.find('./div[@class="item-title"]//a')
            title = title_tag.text
            kata_url = codewar_domain + title_tag.get('href')
            kata_Id = kata_url.split('/')[-1].strip()
            description = self.description(kata_Id)
            code = item.find('./div[2]//code').text
            get_Kyu = item.find('./div[@class="item-title"]//span').text
            language = item.find('./h6').text.split(':')[0]
            print(f'[INFO] Getting Kata Name:- {title}')
            self.save_data(get_Kyu,title,language,description,code)
    
    def description(self,challenge):
        response = requests.get(f'https://www.codewars.com/api/v1/code-challenges/{challenge}')
        json_chalange_resp = response.json()
        description = json_chalange_resp['description']
        return description
    
    def save_data(self, Kyu_Name_folder, Kata_title, languageName, description, code):
        solution_folder = 'Solutions'
        location = os.getcwd()

        # Sanitize folder names to make them valid
        Kyu_Name_folder = self.sanitize_folder_name(Kyu_Name_folder)
        Kata_title = self.sanitize_folder_name(Kata_title)
        languageName = self.sanitize_folder_name(languageName)

        # Make all required paths
        mainFolderPath = os.path.join(location, solution_folder)
        subFolderPath = os.path.join(mainFolderPath, Kyu_Name_folder)
        nestedFolderPath = os.path.join(subFolderPath, Kata_title)
        InnerFolderPath = os.path.join(nestedFolderPath, languageName)

        # Check if the main_folder exists
        if solution_folder not in os.listdir(location):
            os.makedirs(mainFolderPath)

        # Check if the subfolder exists
        if Kyu_Name_folder not in os.listdir(mainFolderPath):
            os.makedirs(subFolderPath)

        # Check if the kata folder exists
        if Kata_title not in os.listdir(subFolderPath):
            os.makedirs(nestedFolderPath)

        # Check if the language folder exists
        if languageName not in os.listdir(nestedFolderPath):
            os.makedirs(InnerFolderPath)

        # Make the README.md file
        file_path = os.path.join(InnerFolderPath, 'README.md')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(description)

        # Make the solution.py file
        file_path = os.path.join(InnerFolderPath, 'solution.py')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)

    def sanitize_folder_name(self, folder_name):
        # Remove trailing spaces and replace invalid characters with underscores
        return "".join(c if c.isalnum() or c in {'_', ' '} else '_' for c in folder_name).rstrip()

    
    def run(self):
        sess = session()
        sess.headers.update(self.headers)
        # get email and password for login 
        email,password = self.Read_cred()
        # get authenticity_token for login
        authenticity_token = self.get_authenticity_token(sess)
        # login the website
        userName = self.login_Process(sess,authenticity_token,email,password)
        # get solution reponse
        page = 1
        while True:
            print(f'[INFO] Page No:- {page}')
            kata_items = self.solution_Resp(sess,userName,page)
            if kata_items:
                # get all solution and save into the files
                self.get_all_Solution(kata_items)
                page += 1
            else:
                break

if __name__ == '__main__':
    Scraper_Class = Codewars_Scraper()  
    Scraper_Class.run()
