class DNSResolver:
    def __init__(self):
        # Initialize an empty dictionary to store domain-IP mappings
        self.hash_map = {}

    def addDomain(self, domain: str, ip: str):
        """
        Adds a domain and its corresponding IP address to the resolver.

        :param domain: The domain name to add.
        :param ip: The IP address associated with the domain.
        """
        self.hash_map[domain] = ip

    def getIP(self, domain: str) -> str:
        """
        Retrieves the IP address associated with the given domain name.

        :param domain: The domain name to look up.
        :return: The IP address if found, otherwise "Domain not found".
        """
        return self.hash_map.get(domain, "Domain not found")
