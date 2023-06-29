import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import UserRepo, UserOut, UserIn, AccountOutWithPassword


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        users: UserRepo,
    ):
        # Use your repo to get the account based on the
        # username (which could be an email)
        return users.get_user(username)

    def get_account_getter(
        self,
        users: UserRepo = Depends(),
    ):
        # Return the accounts. That's it.
        return users

    def get_hashed_password(self, account: AccountOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: UserIn):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.username, UserOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])