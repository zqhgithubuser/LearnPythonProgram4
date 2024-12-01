import configparser

config = configparser.ConfigParser()

print(config.read("config.ini"))  # ['config.ini']
print(
    config.sections()
)  # ['owner', 'database', 'database.primary', 'database.secondary']
print(config.items("database"))

print(config["database"])  # <Section: database>
print(dict(config["database"]))
print(config["DEFAULT"]["host"])  # 192.168.1.1
