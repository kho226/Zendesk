'''
    Author: Kyle Ong
    Date: 03/04/2018

    View for Zendesk Ticket Viewer

    AppView:

        - [x] display_welcome_messsage(self) 
        - [x] display_menu(self)
        - [x] display_exit_process_message(self)
        - [x] display_search_menu(self)

        - [x] display_invalid_command_error_message(self)
        - [x] display_bad_request_error_message(self)

        - [x] display_ticket(self, ticket, ticket_list)
        - [] display_tickets_list(self,current_page,paginated_ticket_list)
       

       
        
'''
class View:
    def __init__(self):
        pass


    def display_welcome_messsage(self):
        '''
            Author: Kyle Ong
            Date: 03/05/2018

            Displays welcome message for Zendesk Ticket Viewer App
        '''
        self.display_header("Zendesk Ticket Viewer")
        print("1.) Type 'View' to view a list of tickets\n" )
        print("2.) Type 'Search' to search for an individual ticket by id. \n")
        print("3.) Type 'exit' to exit the process. \n")
        print("Type your choice: \n")
        return 0

    def display_menu(self):
        '''
            Author: Kyle Ong
            Date: 03/05/2018

            Displays the menu for Zendesk Ticket Viewer App
        '''
        self.display_header("menu")
        print("1.) Type 'view' to view a list of tickets\n" )
        print("2.) Type 'search' to search for an individual ticket by id. \n")
        print("3.) Type 'exit' to search exit the process. \n")
        print("Type your choice: \n")
        return 0

    def display_exit_process_message(self):
        ''' 
            Author: Kyle Ong
            Date:03/05/2018

            Displays exit process message for Zendesk Ticket Viewer App
        '''
        print("\nExiting process...\n")
        print("See you soon! \n")
        return 0

    def display_invalid_command_error_message(self):
        '''
            Author: Kyle Ong
            Date: 03/05/2018

            Displays invalid command message for Zendesk Ticket Viewer App

        '''
        print("Invalid command. \n")
        return 0;

    def display_bad_request_error_message(self):
        '''
            Author: Kyle Ong
            Date: 03/05/2018

            Displays bad request error message for Zendesk Ticket Viewer App

        '''
        print("Service is temporarily unaivalable...\n")
        self.display_menu()
        return 0;

    def display_search_menu(self, ticket_list):
        '''
            Author: Kyle Ong
            Date: 03/05/2018

            Displays search menu for Zendesk Ticket Viewer App

            type: ticket_list: list[ticket]
        '''
        self.display_header("search")
        print("Type a ticket id between 1 and {0}.\n".format(len(ticket_list)))
        print("Type your choice here: \n")

    def display_ticket(self,ticket,ticket_list):
        '''
            Author:Kyle Ong
            Date: 03/05/2018

            Displays an individual ticket from ticket_list for the Zendesk Ticket Viewer App
        '''

        data = ticket['ticket'];
        id = data['id']
        status = data['status']
        priority =  data['priority']
        description = data['description']
        subject = data['subject']
        author = data['requester_id']
        created_at = data['created_at']
        assignee = data['assignee_id']
        submitter = data['submitter_id']

   
        self.display_header("ticket: {0}".format(id))
        print("Created At: {0}\n".format(created_at))
        print("Ticket ID: {0}\n".format(id))
        print("Submitted By: {0}\n".format(submitter))
        print("Requested By: {0}\n".format(author))
        print("Assigned To: {0}\n".format(assignee))
        print("Priority: {0}\n".format(priority))
        print("Status: {0}\n".format(status))
        print("Description:\n{0}\n".format(description)) 
        print("Type 'menu' to see a list of options.\n")
        print("Type 'exit to exit the process. \n")
    

    def display_ticket_list(self, current_page,num_pages, paginated_ticket_list):
        '''
            Author: Kyle Ong
            Date: 03/05/3018

            Displays a paginated list of tickets for the Zendesk Ticket Viewer App

            type: current_page: int
            type: num_pages: int
            type: paginated_ticket_list: list[ticket]

         '''
        for ticket in paginated_ticket_list:

            id = ticket['id']
            
            self.display_header("Ticket:{0}".format(id))

            status = ticket['status']
            priority =  ticket['priority']
            description = ticket['description']
            subject = ticket['subject']
            author = ticket['requester_id']
            created_at = ticket['created_at']
            assignee = ticket['assignee_id']
            submitter = ticket['submitter_id']

            print("Created At: {0}\n".format(created_at))
            print("Ticket ID: {0}\n".format(id))
            print("Submitted By: {0}\n".format(submitter))
            print("Requested By: {0}\n".format(author))
            print("Assigned To: {0}\n".format(assignee))
            print("Priority: {0}\n".format(priority))
            print("Status: {0}\n".format(status))
            print("Description:\n{0}\n".format(description)) 

        print("Page {0} / {1}\n".format(current_page,num_pages))

    def display_ticket_list_menu(self):
        '''
            Author: Kyle Ong
            Date:03/08/2018

            Displays the menu for viewing a list of tickets for Zendesk Ticket Viewer App

        '''
        self.display_header("menu")
        print("Type 'previous' to see the previous page.\n")
        print("Type 'next' to see the next page.\n" )
        print("Type 'menu' to see a list of options.\n")
        print("Type 'exit' to exit the process. \n")


    def display_header(self,text):
        '''
            Author: Kyle Ong
            Date: 03/08/2018

            Displays header for Zendesk Ticket Viewer App
        '''
        print("------------------------------------ {0} ------------------------------------\n".format(text))