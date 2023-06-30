import os
from typing import Optional
from pydantic import BaseModel
from psycopg_pool import ConnectionPool
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class DuplicateAccountError(BaseException):
    pass

class AccountIn(BaseModel):
    email: str
    username: str
    password: str

class AccountOut(BaseModel):
    id: int
    email: str
    username: str

class AccountOutWithPassword(AccountOut):
    hashed_password: str

class AccountRepo(BaseModel):
    def create(self, account: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (
                            email,
                            username,
                            hashed_password
                        )
                    VALUES
                    (%s,%s,%s)
                    RETURNING id, email, username, hashed_password
                    """,
                    [
                    account.email,
                    account.username,
                    hashed_password
                    ]
                )
                acct = result.fetchone()
                # print(acct)
                account = AccountOutWithPassword(
                    id=acct[0],
                    email=acct[1],
                    username=acct[2],
                    hashed_password=acct[3]
                )
                return account


    def get_account(self, username: str) -> Optional[AccountOut]:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    SELECT id, email, username FROM accounts
                    WHERE username=%s
                    """,
                    [username]
                )
                print(result)
                acct = result.fetchone()
                print(acct)
                account = AccountOut(
                    id=acct[0],
                    email=acct[1],
                    username=acct[2]
                )
                return account

    def get_all_accounts(self) -> AccountOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    SELECT id, email, username FROM accounts
                    """
                )
                accts = []
                for acct in result:
                    account = AccountOut(
                        id=acct[0],
                        email=acct[1],
                        username=acct[2],
                    )
                    accts.append(account)
                return accts





    # def create(self, info: UserIn, hashed_password: str) -> AccountOutWithPassword | dict:
    #     try:
    #         user = None

    #         if row is not None:
    #             user = {}
    #             user_fields = [
    #                 'id',
    #                 'email',
    #                 'username',
    #                 'hashed_password'
    #             ]
    #             for i, column in enumerate(description):
    #                 if column.name in user_fields:
    #                         user[column.name] = row[i]

    #         return {"message": "succcess"}

    #     except Exception:
    #         return {"message": "couldn't create account"}