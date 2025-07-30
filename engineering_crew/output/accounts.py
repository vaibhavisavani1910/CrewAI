
# accounts.py

from typing import Dict, List, Tuple

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class InsufficientSharesError(Exception):
    """Custom exception for insufficient shares."""
    pass


class Account:
    """
    Represents a user account for a trading simulation platform.
    """

    def __init__(self, account_id: str, initial_deposit: float = 0.0):
        """
        Initializes a new account.

        Args:
            account_id: Unique identifier for the account.
            initial_deposit: The initial deposit amount (default: 0.0).
        """
        self.account_id = account_id
        self.balance = initial_deposit
        self.holdings: Dict[str, int] = {}  # {symbol: quantity}
        self.transactions: List[Tuple[str, float, str, int, float]] = [] # (type, timestamp, symbol, quantity, price)
        self.initial_deposit = initial_deposit

    def deposit(self, amount: float) -> None:
        """
        Deposits funds into the account.

        Args:
            amount: The amount to deposit.

        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(("deposit", self._get_current_timestamp(), "deposit", 0, amount))


    def withdraw(self, amount: float) -> None:
        """
        Withdraws funds from the account.

        Args:
            amount: The amount to withdraw.

        Raises:
            ValueError: If the amount is not positive.
            InsufficientFundsError: If the account balance is insufficient.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(("withdraw", self._get_current_timestamp(), "withdraw", 0, amount))

    def buy_shares(self, symbol: str, quantity: int, get_share_price_func) -> None:
        """
        Buys shares of a given symbol.

        Args:
            symbol: The symbol of the share to buy.
            quantity: The number of shares to buy.
            get_share_price_func: A function to get the current share price.

        Raises:
            ValueError: If the quantity is not positive.
            InsufficientFundsError: If the account balance is insufficient.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        price_per_share = get_share_price_func(symbol)
        total_cost = price_per_share * quantity

        if self.balance < total_cost:
            raise InsufficientFundsError("Insufficient funds to buy shares.")

        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append(("buy", self._get_current_timestamp(), symbol, quantity, price_per_share))


    def sell_shares(self, symbol: str, quantity: int, get_share_price_func) -> None:
        """
        Sells shares of a given symbol.

        Args:
            symbol: The symbol of the share to sell.
            quantity: The number of shares to sell.
            get_share_price_func: A function to get the current share price.

        Raises:
            ValueError: If the quantity is not positive.
            InsufficientSharesError: If the account does not have enough shares.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise InsufficientSharesError("Insufficient shares to sell.")

        price_per_share = get_share_price_func(symbol)
        total_revenue = price_per_share * quantity

        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append(("sell", self._get_current_timestamp(), symbol, quantity, price_per_share))


    def get_portfolio_value(self, get_share_price_func) -> float:
        """
        Calculates the total value of the portfolio.

        Args:
            get_share_price_func: A function to get the current share price.

        Returns:
            The total value of the portfolio.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price_func(symbol) * quantity
        return total_value

    def get_profit_loss(self, get_share_price_func) -> float:
        """
        Calculates the profit or loss from the initial deposit.

        Args:
            get_share_price_func: A function to get the current share price.

        Returns:
            The profit or loss.
        """
        return self.get_portfolio_value(get_share_price_func) - self.initial_deposit

    def get_holdings(self) -> Dict[str, int]:
        """
        Returns the current holdings of the account.

        Returns:
            A dictionary of symbol: quantity.
        """
        return self.holdings.copy()

    def get_transactions(self) -> List[Tuple[str, float, str, int, float]]:
        """
        Returns the transaction history of the account.

        Returns:
            A list of transactions.
        """
        return self.transactions.copy()

    def _get_current_timestamp(self) -> float:
        """
        Returns the current timestamp.  Can be mocked for testing.

        Returns:
            The current timestamp as a float.
        """
        import time
        return time.time()



# Test implementation of get_share_price
def get_share_price(symbol: str) -> float:
    """
    Returns a fixed price for AAPL, TSLA, and GOOGL for testing purposes.

    Args:
        symbol: The symbol of the share.

    Returns:
        The price of the share.
    """
    if symbol == "AAPL":
        return 150.0
    elif symbol == "TSLA":
        return 700.0
    elif symbol == "GOOGL":
        return 2500.0
    else:
        return 100.0  # Default price
