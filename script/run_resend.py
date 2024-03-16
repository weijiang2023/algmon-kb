import os
import resend

resend.api_key = "re_JHzRfmVq_Edbpcpa6Gj22aAEE2BeJY94B"

f = open(
  os.path.join(os.path.dirname(__file__), "./data/lookbook/001_CK_Gabriela-Hearst_S6471_F02_V2a.jpg"), "rb"
).read()

params = {
    "from": "admin@algmon.com",
    "to": ["weijiang2009@gmail.com"],
    "subject": "You have been promoted to become the CEO of algmon",
    "html": "<strong>hello, see the world with cold eyes!</strong>",
    "headers": {
      "X-Entity-Ref-ID": "123456789"
    },
    "attachments": [{"filename": "lookbook.jpg", "content": list(f)}],
}

email = resend.Emails.send(params)
print(email)
