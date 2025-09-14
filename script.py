import os
import sys
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from rich.console import Console
from rich.theme import Theme


class Menu:
    def __init__(self, prompt_char=">"):
        self.prompt = prompt_char
        self.prompt_char = prompt_char
        self.network_file_path = None
        self.banner_file_path = "./banner.txt"
        self.inquirer_keybindings = {
            "answer": [{"key": "enter"}, {"key": "right"}],
            "skip": [{"key": "left"}, {"key": "escape"}],
        }
        self.menu_theme = Theme({"banner": "blue_violet"})
        self.console = Console(theme=self.menu_theme)
        self._init()

    # Open banner file and print
    def _printBanner(self):
        with open(self.banner_file_path) as bannerFile:
            self.console.print(
                bannerFile.read(), style="banner", markup=False, highlight=False
            )

    def _return_to_menu(self):
        return "return"

    # Change the message of the prompt
    def _change_prompt_msg(self, msg):
        self.prompt = f"[{msg}] " + self.prompt_char

    # Main menu where categories can be selected
    def main(self):
        while True:
            menu_options = ["FILE", "QUIT"]

            if self.network_file_path is not None:
                menu_options = ["FILE", "STATS", "HTTP", "DNS", "EXTRACT", "QUIT"]

            action = inquirer.select(
                message=self.prompt,
                choices=menu_options,
                keybindings=self.inquirer_keybindings,
                mandatory=False,
            ).execute()

            # Exit if selection is skipped
            if action == None:
                break

            # Execute method according to the selected action
            getattr(self, action.lower())()

    def file(self):
        options = ["OPEN", "CLOSE", "RETURN"]

        # Get file path to be opened
        def open_file():
            self.network_file_path = inquirer.filepath(
                message="Path: ",
                default=os.getcwd(),
                validate=PathValidator(is_file=True, message="Not a file"),
            ).execute()
            self._change_prompt_msg(os.path.basename(self.network_file_path))
            return "return"

        # Clear var where file path is stored
        def close_file():
            if self.network_file_path == None:
                print("[ERROR] NO FILE OPEN")
                return "continue"
            else:
                print(f"[*] FILE ({self.network_file_path}) CLOSED SUCCESSFULLY")
                self.network_file_path = None
                self._change_prompt_msg("NO FILE")
                return "return"

        # Directory mapping each action to its function
        actions = {
            "OPEN": open_file,
            "CLOSE": close_file,
            "RETURN": self._return_to_menu,
        }

        while True:
            action = inquirer.select(
                message=self.prompt,
                choices=options,
                keybindings=self.inquirer_keybindings,
                mandatory=False,
            ).execute()

            # Return to main menu if skipped
            if action == None:
                return

            # Call corresponding function in the dictionary
            result = actions[action]()

            # Return or continue according to the return value of the function
            if result == "return":
                return

            if result == "continue":
                continue

    def stats(self):
        options = ["GENERAL", "IPs", "IPINFO", "CONVO", "PROTO", "RETURN"]

        def general_stats():
            return "return"

        def get_ips():
            return "return"

        def get_ip_info():
            return "return"

        def get_conversations():
            return "return"

        def get_protocols():
            return "return"

        actions = {
            "GENERAL": general_stats,
            "IPs": get_ips,
            "IPINFO": get_ip_info,
            "CONVO": get_conversations,
            "PROTO": get_protocols,
            "RETURN": self._return_to_menu,
        }

        action = inquirer.select(
            message=self.prompt,
            choices=options,
            keybindings=self.inquirer_keybindings,
            mandatory=False,
        ).execute()

        if action == None:
            return

        result = actions[action]()

        if result == "return":
            return

    def http(self):
        options = ["DOMAINS", "METHODS", "PATHS", "SEARCH", "RETURN"]

        def get_domains():
            return "return"

        def get_methods():
            return "return"

        def get_paths():
            return "return"

        def http_search():
            return "return"

        actions = {
            "DOMAINS": get_domains,
            "METHODS": get_methods,
            "SEARCH": http_search,
            "PATHS": get_paths,
            "RETURN": self._return_to_menu,
        }

        action = inquirer.select(
            message=self.prompt,
            choices=options,
            keybindings=self.inquirer_keybindings,
            mandatory=False,
        ).execute()

        if action == None:
            return

        result = actions[action]()

        if result == "return":
            return

    def dns(self):
        options = ["QUERIES", "RETURN"]

        def get_queries():
            return "return"

        actions = {"QUERIES": get_queries, "RETURN": self._return_to_menu}

        action = inquirer.select(
            message=self.prompt,
            choices=options,
            keybindings=self.inquirer_keybindings,
            mandatory=False,
        ).execute()

        if action == None:
            return

        result = actions[action]()

        if result == "return":
            return

    def extract(self):
        options = ["HTTP", "FTP", "RETURN"]

        def extract_http():
            return "return"

        def extract_ftp():
            return "return"

        actions = {
            "HTTP": extract_http,
            "FTP": extract_ftp,
            "RETURN": self._return_to_menu,
        }

        action = inquirer.select(
            message=self.prompt,
            choices=options,
            keybindings=self.inquirer_keybindings,
            mandatory=False,
        ).execute()

        if action == None:
            return

        result = actions[action]()

        if result == "return":
            return

    def quit(self):
        sys.exit(0)

    # Initialize the menu with default parameters
    def _init(self):
        self._printBanner()
        self._change_prompt_msg("NO FILE")
        self.main()


menu = Menu()
