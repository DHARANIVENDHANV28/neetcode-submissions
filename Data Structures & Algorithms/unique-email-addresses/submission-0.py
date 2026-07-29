class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = []
        for e in emails:
            local = e.split('@')[0]
            domain = e.split('@')[1]

            local = "".join(local.split("."))
            local = local.split("+")[0]

            if local+domain not in unique:
                unique.append(local+domain)
        
        return len(unique)

        