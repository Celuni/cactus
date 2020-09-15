import Account as ac


class Client:
    def __init__(self, account):

        self.account = account

        self.login_url = "https://auth.riotgames.com/token"
        self.login_body = ""
        self.login_headers = {
            "User-Agent": "RiotClient/17.1.0 (rso-auth)",
            "Accept": "*/*",
            "Content-type": "application/x-www-form-urlencoded"
        }

        self.purchase_info_url = ""
        self.purchase_info_headers = {}

        self.name_check_url = ""
        self.name_check_headers = {}

        self.change_name_url = ""
        self.change_name_body = ""
        self.change_name_referer = ""
        self.change_name_headers = {}

    def Build(self):
        self.login_body = (
            'client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-'
            'bearer&client_assertion=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczpcL1wvYXV0aC5yaW90'
            'Z2FtZXMuY29tXC90b2tlbiIsInN1YiI6ImxvbCIsImlzcyI6ImxvbCIsImV4cCI6MTYwMTE1MTIxNCwia'
            'WF0IjoxNTM4MDc5MjE0LCJqdGkiOiIwYzY3OThmNi05YTgyLTQwY2ItOWViOC1lZTY5NjJhOGUyZDcifQ'
            '.dfPcFQr4VTZpv8yl1IDKWZz06yy049ANaLt-AKoQ53GpJrdITU3iEUcdfibAh1qFEpvVqWFaUAKbVIxQ'
            'otT1QvYBgo_bohJkAPJnZa5v0-vHaXysyOHqB9dXrL6CKdn_QtoxjH2k58ZgxGeW6Xsd0kljjDiD4Z0CR'
            'R_FW8OVdFoUYh31SX0HidOs1BLBOp6GnJTWh--dcptgJ1ixUBjoXWC1cgEWYfV00-DNsTwer0UI4YN2TD'
            'mmSifAtWou3lMbqmiQIsIHaRuDlcZbNEv_b6XuzUhi_lRzYCwE4IKSR-AwX_8mLNBLTVb8QzIJCPR-MGa'
            f'PL8hKPdprgjxT0m96gw&grant_type=password&username={self.account.region}%7C'
            f'{self.account.username}&password={self.account.password}&scope=openid%20offline_'
            'access%20lol%20ban%20profile%20email%20phone'
        )

        # NEW ENDPOINT POSSIBLY?
        if self.account.region == "NA1":
            self.purchase_info_url = "https://na.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"
        elif self.account.region == "EUN1":
            self.purchase_info_url = "https://eun.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"
        elif self.account.region == "EUW1":
            self.purchase_info_url = "https://euw.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"

        if self.account.region == "NA1":
            self.name_check_url = (
                f'https://na.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}'
            )
        elif self.account.region == "EUN1":
            self.name_check_url = (
                f'https://eun.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}'
            )
        elif self.account.region == "EUW1":
            self.name_check_url = (
                f'https://euw.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}'
            )

        if self.account.region == "NA1":
            self.change_name_url = "https://store.na2.lol.riotgames.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = "https://store.na2.lol.riotgames.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion=na2&selectedItems=&page=featured&recipientSummonerId="
        elif self.account.region == "EUN1":
            self.change_name_url = "https://eun.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = (
                f'https://eun.store.leagueoflegends.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion='
                f'{self.account.region}&selectedItems=&page=featured&recipientSummonerId='
            )
        elif self.account.region == "EUW1":
            self.change_name_url = "https://euw.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = (
                f'https://euw.store.leagueoflegends.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion='
                f'{self.account.region}&selectedItems=&page=featured&recipientSummonerId='
            )

    def UpdateAccountID(self):
        self.change_name_body = "{\"summonerName\":\""
        self.change_name_body += self.account.alias
        self.change_name_body += "\",\"accountId\":"
        self.change_name_body += self.account.account_id
        self.change_name_body += ",\"items\":[{\"inventoryType\":\"SUMMONER_CUSTOMIZATION\",\"itemId\":1,\"ipCost\":13900,\"rpCost\":null,\"quantity\":1}]}"

    def UpdateAccessToken(self):
        self.purchase_info_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token
        }

        self.name_check_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token
        }

        self.change_name_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.account.access_token,
            "Referer": self.change_name_referer
        }
