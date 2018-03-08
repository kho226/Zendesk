'''
    Author: Kyle Ong
    Date: 03/05/2018

    Unit Tests for Zendesk Ticket Viewer Application 
'''

import unittest
import sys

from os.path import dirname,abspath

from AppModel.appModel import Model
from AppController.AppController import Controller
from AppView.appView import View

class TestView(unittest.TestCase):
    '''
            Author: Kyle Ong
            Date: 03/05/2018 

            View happy path tests for Zendesk Ticket Viewer Application
    '''
    def test_view(self):
        view = View();
        self.assertEqual(view.display_welcome_message(), 0)
        self.assertEqual(view.display_menu(), 0)
        self.assertEqual(view.dispaly_exit_process_message(), 0)
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
        self.asssertEqual(len(ticket),1)
        self.assertEqual(ticket['ticket']['id'],1)

    def test_get_all_tickets(self):
        model = Model()
        ticket_list = model.get_all_tickets()
        self.assertEqual(len(ticket_list),101)


if __name__ == '__main__':
    unittest.main()
