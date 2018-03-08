'''
    Author: Kyle Ong
    Date: 03/05/2018

    Unit Tests for Zendesk Ticket Viewer Application 
'''

import unittest
import sys

from os.path import dirname,abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from AppView.appView import View
from AppModel.appModel import Model

class TestView(unittest.TestCase):
    '''
            Author: Kyle Ong
            Date: 03/05/2018 

            View happy path tests for Zendesk Ticket Viewer Application
    '''
    def test_view(self):
        view = View()
        self.assertEqual(view.display_welcome_messsage(),0)
        self.assertEqual(view.display_menu(), 0)
        self.assertEqual(view.display_exit_process_message(), 0)
        self.assertEqual(view.display_bad_request_error_message(), 0)
        self.assertEqual(view.display_invalid_command_error_message(), 0)

class TestModel(unittest.TestCase):
    '''
            Author: Kyle Ong
            Date: 03/05/2018 

            Model happy path tests for Zendesk Ticket Viewer Application
    '''
    def test_get_ticket_(self):
        model = Model()
        ticket = model.get_ticket(1)
        self.assertEqual(len(ticket),1)
        self.assertEqual(ticket['ticket']['id'],1)

    def test_get_all_tickets(self):
        model = Model()
        ticket_list = model.get_all_tickets()
        self.assertEqual(len(ticket_list),1)


if __name__ == '__main__':
    unittest.main()
