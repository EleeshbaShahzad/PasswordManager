import hashlib
import json
import os
from collections import deque

class CryptoEngine:
    SALT = "FAANG_SECURE"

    def hash_password(self, password):
        return hashlib.sha256((password + self.SALT).encode()).hexdigest()


class DataStore:
    FILE = "db.json"

    def __init__(self):
        self.users = {}
        self.logs = deque()
        self.load()

    def load(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.users, f, indent=4)


class VaultService:

    def __init__(self):
        self.store = DataStore()
        self.crypto = CryptoEngine()

    def register(self, u, p):
        if u in self.store.users:
            return "User exists"

        self.store.users[u] = self.crypto.hash_password(p)
        self.store.save()
        return "Registered"

    def login(self, u, p):
        if u not in self.store.users:
            return "Not found"

        if self.store.users[u] == self.crypto.hash_password(p):
            self.store.logs.append(u + " logged in")
            return "Success"

        return "Failed"

    def get_logs(self):
        return list(self.store.logs)