#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client
account_sid = 'AC106e47c71964da787ffb98dc59371b2a' 
auth_token = 'edb51cdddc2b41b52f81fcb1f0454f27'


# In[32]:


client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886', 
                              body='Mask Up App Alert!!! \n Student is entering without a face mask. \n See in camera to recognize student. \n Please advise to Mask Up!!',
                              media_url = 'http://6f470b37db77.ngrok.io/tmp/nomask1.jpeg',
                         
                              to='whatsapp:+263784323479'
                              )
                              


# In[ ]:





# In[ ]:




