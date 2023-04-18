import resources
print('Enter your webpage url you want to clone:')
url = input()
obj1 = resources.CloneWebsite(url).clone()
print('Enter your redirect request url:')
redirectRequest = input()
obj3 = resources.WebsiteBuilder.build(redirectRequest)