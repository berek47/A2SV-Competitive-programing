class UnionFind:
    def __init__(self, emails):
        self.email_owner = dict()
        for email in emails:
            self.email_owner[email] = email

    def find(self, email):
        if self.email_owner[email] != email:
            self.email_owner[email] = self.find(self.email_owner[email])
        return self.email_owner[email]
    
    def union(self, email1, email2):
        owner1 = self.find(email1)
        owner2 = self.find(email2)
        if owner1 != owner2:
            self.email_owner[owner2] = owner1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unique_emails = set()
        email_to_name = dict()
        
        for account in accounts:
            unique_emails |= set(account[1:])
            for email in account[1:]:
                email_to_name[email] = account[0]

        union_find = UnionFind(unique_emails)

        for account in accounts:
            name, emails = account[0], account[1:]
            for i in range(1, len(emails)):
                union_find.union(emails[i-1], emails[i])
        
        email_roots = [email for email in unique_emails if union_find.find(email) == email]
        merged_accounts = []
        
        for root in email_roots:
            merged_emails = []
            for key, val in union_find.email_owner.items():
                if val == root:
                    merged_emails.append(key)
            merged_accounts.append([email_to_name[root]] + sorted(merged_emails))
        
        return merged_accounts
