from django.conf import settings
import requests

class MailchimpService:
    def __init__(self):
        self.api_key = settings.MAILCHIMP_API_KEY
        self.list_id = settings.MAILCHIMP_LIST_ID
        self.base_url = 'https://<dc>.api.mailchimp.com/3.0/'  # Replace <dc> with your data center

    def subscribe_user(self, email, first_name, last_name):
        url = f'{self.base_url}lists/{self.list_id}/members'
        data = {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': first_name,
                'LNAME': last_name
            }
        }
        response = requests.post(url, json=data, auth=('apikey', self.api_key))
        if response.status_code == 400:
            error_detail = response.json().get('detail', '')
            if 'is already a list member' in error_detail:
                raise Exception('User already exists.')
        response.raise_for_status()
