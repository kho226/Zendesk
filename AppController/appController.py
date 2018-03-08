'''
    Author: Kyle Ong
    Date: 03/04/2018

    appController for Zendesk Ticket Viewer

    AppController:
    - [x] self.Model
    - [x] self.View
    - [x] self.current_page
    - [x] self.user_input
    - [x] self.paginated_ticket_list

    - [x] def get_user_input(self)
    - [x] def get_ticket_list(self)
    - [x] def handle_menu(self)
    - [x] def manage_menu(self)
    - [x] def start_process(self)
    - [x] def handle_search(self)
    - [x] def manage_search(self,ticket_list)
    - [x] def handle_view(self)
    - [x] def view_ticket_list(self,ticket_list)
    - [x] def manage_view(self,ticket_list,pages)
        
'''

import sys

from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from AppView.appView import View
from AppModel.appModel import Model

class Controller:
    '''
        Author: Kyle Ong
        Date: 03/07/2018

        Controller Class for Zendesk Ticket Viewer Application
    '''

    def __init__(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            initializer for Controller class
        '''
        self.model = Model()
        self.view = View()
        self.user_input = ""
        self.current_page = 1

    def get_user_input(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            get user input 
         '''
        self.user_input = input()

    def get_ticket_list(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            get ticket_list

            type: ticket_list: list[ticket]
        '''       
        ticket_list = self.model.get_all_tickets()
        if ticket_list == 0:
            self.view.display_bad_request_error_message()
        else:
            return ticket_list

    def handle_menu(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            handles main menu for Zendesk Ticket Viewer Application
         '''
        self.view.display_menu()
        self.manage_menu()

    def manage_menu(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            manages 'menu' for zendesk ticket viewer application
         '''
        while (True):
            self.get_user_input()
            if (self.user_input == "menu"):
                self.view.display_menu()
            elif (self.user_input == "view"):
                self.handle_view()
            elif (self.user_input == "search"):
                self.handle_search()
            elif (self.user_input == "exit"):
                sys.exit(self.view.display_exit_process_message())
            else:
                self.view.display_invalid_command_error_message()
                self.view.display_menu()
            self.user_input = ""

    def handle_search(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            handle 'search' for Zendesk Ticket Viewer Application
         '''
        ticket_list = self.get_ticket_list();
        self.manage_search(ticket_list)

    def manage_search(self,ticket_list):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            type: ticket_list: list[ticket]
         '''
        self.view.display_search_menu(ticket_list)
        while (True):
            self.get_user_input()
            if ((self.user_input).isdigit() and int(self.user_input) >= 1 and int(self.user_input) <= len(ticket_list)):
                ticket = self.model.get_ticket(self.user_input)
                self.view.display_ticket(ticket,ticket_list)
                self.view.display_search_menu(ticket_list)
            elif (self.user_input == "menu"):
                self.view.display_menu()
                self.handle_menu()
            elif (self.user_input == "exit"):
                sys.exit(self.view.display_exit_process_message())
            else:
                self.view.display_invalid_command_error_message()
                self.view.display_search_menu(ticket_list)
            self.user_input = ""

    def handle_view(self):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            handles view for Zendesk Ticket Viewer Application
         '''
        ticket_list = self.get_ticket_list()
        self.view_ticket_list(ticket_list)

    def view_ticket_list(self,ticket_list):
        num_pages = self.model.calculate_num_pages(ticket_list)
        page_dict = self.model.paginate_tickets(ticket_list,num_pages)
        paginated_ticket_list = page_dict[self.current_page]
        self.view.display_ticket_list(self.current_page,num_pages, paginated_ticket_list)
        self.view.display_ticket_list_menu()
        self.manage_view_ticket_list(ticket_list,num_pages)

    def manage_view_ticket_list(self,ticket_list,num_pages):
        '''
            Author: Kyle Ong
            Date: 03/07/2018

            type: ticket_list: list[ticket]
            type: num_pages: int
         '''
        while (True):
            self.get_user_input()
            if (self.user_input == "next"):
                if (self.current_page + 1 <= num_pages):
                    self.current_page += 1
                    self.view_ticket_list(ticket_list)
                    self.view.display_ticket_list_menu()
                else:
                    print("Page: {0} /  {1}".format(self.current_page,num_pages))
                    self.handle_menu()
            elif (self.user_input == "previous"):
                if (self.current_page - 1 >= 1):
                    self.current_page -= 1
                    self.view_ticket_list(ticket_list)
                    self.view.display_ticket_list_menu()
                else:
                    print("Page: {0} / {1}".format(self.current_page,num_pages))
                    self.handle_menu()
            elif (self.user_input == "menu"):
                self.handle_menu();
            elif (self.user_input == "exit"):
                sys.exit(self.view.display_exit_process_message())
            else:
                self.view.display_invalid_command_error_message()
                self.handle_menu()    





if __name__ == "__main__":
    c = Controller()
    c.handle_menu()