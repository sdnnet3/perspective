# services/mailchimp_service.py

from mailchimp3 import MailChimp
from django.conf import settings

class MailchimpService:
    def __init__(self):
        self.client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user='your-username')
        self.list_id = settings.MAILCHIMP_EMAIL_LIST_ID

    def subscribe_user(self, email, first_name='', last_name=''):
        data = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": first_name,
                "LNAME": last_name,
            }
        }
        return self.client.lists.members.create(self.list_id, data)