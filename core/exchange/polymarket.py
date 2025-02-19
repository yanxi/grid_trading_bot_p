from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import Balances, Int, Liquidation, Num, Order, OrderBook, OrderSide, OrderType, Position, Str, Strings, Ticker
from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON
from py_clob_client.clob_types import BalanceAllowanceParams, AssetType

host = "https://clob.polymarket.com"
chain_id = POLYGON
key = "你的私钥"
funder = "你的资金地址"

class polymarket(Exchange):
    def __init__(self):
        client = ClobClient(
            host,
            key=key,
            chain_id=chain_id
        )
        client.set_api_creds(client.create_or_derive_api_creds())
        self.client = client

    async def watch_ticker(self, symbol: str, params={}) -> Ticker:
        market_price = self.client.get_price(token_id = symbol, side = "buy")
        return {
            'last': market_price["price"],
        }
    
    def close():
        pass

    async def fetch_balance(self, params={}) -> Balances:
        balance_info = self.client.get_balance_allowance(BalanceAllowanceParams(
            asset_type=AssetType.COLLATERAL
        ))
        return {
            'USDC': balance_info['balance'],
        }
    
    async def fetch_ticker(self, symbol: str, params={}) -> Ticker:
        market_price = self.client.get_price(token_id = symbol, side = "buy")
        return {
            'last': market_price["price"],
        }
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={}):
        pass

    async def fetch_order(self, id: str, symbol: Str = None, params={}) -> Order:
        pass

    async def cancel_order(self, id: str, symbol: Str = None, params={}):
        pass

