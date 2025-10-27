import pandas as pd


def find_unsent_emails():
    to_send = pd.read_csv('recipients.csv')
    sent = pd.read_csv('sent.csv')
    unique_emails = to_send[~to_send['EMAIL'].isin(sent['EMAIL'])]
    result = unique_emails.groupby('NAME')['EMAIL'].apply(list).to_dict()
    return result


def update_email_list(company_name, emails):

    new_sent_emails = {'NAME': [company_name]*len(emails), 'EMAIL': emails}
    new_sent_emails_df = pd.DataFrame(new_sent_emails)

    sent = pd.read_csv('sent.csv')

    updated_list = sent.append(new_sent_emails_df, ignore_index=True)
    updated_list = updated_list.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    updated_list.drop_duplicates(inplace=True)

    updated_list.to_csv("sent.csv", index=False)


def read_body(role):
    with open(f"{role}.html") as file:
        return file.read()


def read_default_txt():
    with open("body.txt") as file:
        return file.read()
