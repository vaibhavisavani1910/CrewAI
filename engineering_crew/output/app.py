
# app.py
import gradio as gr
from accounts import Account, InsufficientFundsError, InsufficientSharesError, get_share_price

# Initialize the account
account = Account("user1")

def create_account(initial_deposit):
    global account
    try:
        initial_deposit = float(initial_deposit)
        if initial_deposit < 0:
            return "Initial deposit must be non-negative", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
        account = Account("user1", initial_deposit)
        return f"Account created with initial deposit: {initial_deposit}", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

    except ValueError:
        return "Invalid initial deposit amount.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

def deposit(amount):
    try:
        amount = float(amount)
        account.deposit(amount)
        return f"Deposited: {amount}", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except ValueError:
        return "Invalid deposit amount.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

def withdraw(amount):
    try:
        amount = float(amount)
        account.withdraw(amount)
        return f"Withdrew: {amount}", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except ValueError:
        return "Invalid withdrawal amount.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except InsufficientFundsError:
        return "Insufficient funds.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

def buy_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.buy_shares(symbol, quantity, get_share_price)
        return f"Bought {quantity} shares of {symbol}", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except ValueError:
        return "Invalid quantity.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except InsufficientFundsError:
        return "Insufficient funds to buy shares.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

def sell_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.sell_shares(symbol, quantity, get_share_price)
        return f"Sold {quantity} shares of {symbol}", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except ValueError:
        return "Invalid quantity.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()
    except InsufficientSharesError:
        return "Insufficient shares to sell.", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

def get_account_info():
    return "Account information updated", account.balance, account.get_portfolio_value(get_share_price), account.get_profit_loss(get_share_price), account.get_holdings(), account.get_transactions()

with gr.Blocks() as iface:
    gr.Markdown("## Simple Trading Account")

    with gr.Row():
        initial_deposit_input = gr.Number(label="Initial Deposit")
        create_account_button = gr.Button("Create Account")

    with gr.Row():
        deposit_input = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")

        withdraw_input = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")

    with gr.Row():
        symbol_input = gr.Textbox(label="Symbol")
        quantity_input = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy Shares")
        sell_button = gr.Button("Sell Shares")

    message = gr.Textbox(label="Message")
    balance_output = gr.Number(label="Balance")
    portfolio_value_output = gr.Number(label="Portfolio Value")
    profit_loss_output = gr.Number(label="Profit/Loss")
    holdings_output = gr.JSON(label="Holdings")
    transactions_output = gr.JSON(label="Transactions")
    
    update_button = gr.Button("Update Account Info")

    create_account_button.click(create_account, inputs=initial_deposit_input, outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])
    deposit_button.click(deposit, inputs=deposit_input, outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])
    withdraw_button.click(withdraw, inputs=withdraw_input, outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])
    buy_button.click(buy_shares, inputs=[symbol_input, quantity_input], outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])
    sell_button.click(sell_shares, inputs=[symbol_input, quantity_input], outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])
    update_button.click(get_account_info, outputs=[message, balance_output, portfolio_value_output, profit_loss_output, holdings_output, transactions_output])


iface.launch()
