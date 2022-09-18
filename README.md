# Installation

```
pip install scrape-721
```

### RPC URL Setup

You must ensure the $RPC_URL variable is set in the environment. You may set it directly, or via a `.env` file in the root directory:

```
# .env
RPC_URL=<your_rpc_url>
```

Alternatively, you can specify the $RPC_URL directly on script initialization, with the `--rpc-url` flag.

```
python -m scrape_721 --rpc-url
```

You must define the $RPC_URL in one of these ways or the script will fail.

### Redis Setup

The package uses redis caching to drastically speed up the scrape operations. (Caching already queried account balances)

This means in order to run with the default settings, _you must have a local redis instance available, accessible via localhost_.

If no redis instance is present, the script will fail to initialise. If you wish to indeed run the script without using redis, use the `--no-cache` flag.

# Basic CLI Usage

#### Display help

```
python -m scrape_721 --help
```

#### Basic scrape

```
python -m scrape_721 <contract_address>
```

#### Scrape from a specific block

```
python -m scrape_721 <contract_address> --from-block <block_number>
```

#### Scrape a specific block range

```
python -m scrape_721 <contract_address> --from-block <block_number> --to-block <block_number>
```

#### Output

By default output files are placed in the root directory. To define the output path, use the `--path` argument.

# Programmatic Usage

This section is about how you can use the package utilities to simplify some of your own scripts.

#### Import

```
from scrape_721.contract_utils import configure, is_contract, supports_erc_721
```

#### Configure

Before using any of the available helper functions, you must first call the configure function.

```
configure()

# OR

configure(my_rpc_url)
```

The first variety assumes that (like the CLI above) the $RPC_URL variable is available in the environment. The second allows you to pass it in directly.

#### Helper Functions

```
# Returns True/False if supplied address (a string) is a contract
is_contract(my_ethereum_address)

# Returns True/False if supplied address supports ERC-721
supports_erc_721(my_ethereum_address)
```
