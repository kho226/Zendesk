'''
    Author: Kyle Ong
    Date: 03/04/2018

    AppModel for Zendesk Ticket Viewer

    AppModel:

        self.org
        self.user_name
        self.password
        self.url
        self.ticket
        self.ticket_list
        self.ticket_limit
        self.ticket_id

        get_ticket()
        get_all_tickets()
        calculate_num_pages()
        paginate_tickets()
        
    https://developer.zendesk.com/rest_api/docs/core/tickets#content
'''

import requests

class Model:
    def __init__(self):
        self.org = "kyleong"
        self.user_name = "kho226@nyu.edu"
        self.password = "password"
        self.url = ""
        self.ticket = []
        self.ticket_list = []
        self.ticket_limit = 20
        self.ticket_id = ""
    
    def get_ticket(self,id):
        self.url = "https://{0}.zendesk.com/api/v2/tickets/{1}.json".format(self.org,id)
        try:
            response = requests.get(self.url,auth=(self.user_name,self.password))
            status_code = response.status_code
            if (status_code != 200):
                return -1
            self.ticket = response.json()
        except (requests.exceptions.RequestException):
            return -1
        ret = self.ticket
        return ret
    

    def get_all_tickets(self):
        self.url = "https://{0}.zendesk.com/api/v2/tickets.json".format(self.org)
        if (self.ticket_list is None or not self.ticket_list):
            while self.url:
                try:
                    response = requests.get(self.url,auth=(self.user_name,self.password))
                    status_code = response.status_code
                    if (status_code != 200):
                        print("{0}".format(status_code))
                        return -1
                    data = response.json();
                    self.ticket_list.extend(data['tickets'])
                    self.url = data['next_page']
                except (requests.exceptions.RequestException):

                    return -1
        ret = self.ticket_list
        return ret

    def calculate_num_pages(self,ticket_list):
        num_pages = -(-len(ticket_list) // self.ticket_limit)
        return num_pages
    
    def paginate_tickets(self,ticket_list,num_pages):
        page_dict = {}
        page_list = [ticket_list[i:i + self.ticket_limit] for i in range(0,len(ticket_list),self.ticket_limit)]
        for p in range(1,num_pages+1):
            page_dict[p] = page_list[p - 1]
        return page_dict
    