# This module reads configuration properties from a config.ini file
import configparser

config = configparser.RawConfigParser() # Create a RawConfigParser object to read properties files
config.read(".//configuration//config.ini") # Read the properties file located at .//configuration//config.ini

# Create a class to read properties from the config.ini file
class ReadConfig:
    @staticmethod   # Call this method without creating an instance (object) of ReadConfig
    def get_base_url():
        url = config.get('login info', 'base_URL') # Get value of 'base_URL' from the 'login info' section
        return url

    @staticmethod
    def get_username():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('login info', 'invalid_username')
        return invalid_username