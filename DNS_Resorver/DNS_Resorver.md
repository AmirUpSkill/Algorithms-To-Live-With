# Problem Statement

You’re tasked with implementing a simple DNS (Domain Name System) resolver. The resolver maps domain names to their corresponding IP addresses. Implement a class called `DNSResolver` that supports the following operations:

- `addDomain(domain, ip)`: Adds a domain name and its corresponding IP address to the resolver.
- `getIP(domain)`: Retrieves the IP address associated with the given domain name. If the domain doesn’t exist, returns `"Domain not found"`.

### Constraints

- Domain names consist of lowercase English letters, digits, and periods (`.`).
- IP addresses follow the format `"xxx.xxx.xxx.xxx"` where `xxx` is a number between 0 and 255.
- The total number of `addDomain` and `getIP` operations will not exceed 10.

### Example

```python
# Initialize the resolver
resolver = DNSResolver()

# Add domains
resolver.addDomain("example.com", "93.184.216.34")
resolver.addDomain("openai.com", "104.18.12.197")

# Retrieve IPs
print(resolver.getIP("example.com"))        # Output: "93.184.216.34"
print(resolver.getIP("openai.com"))         # Output: "104.18.12.197"
print(resolver.getIP("nonexistent.com"))    # Output: "Domain not found"
