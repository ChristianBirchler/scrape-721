from scrape_721.constants import ERC_165_ABI, ERC_721_INTERFACE_ID


def is_contract(address, w3, block=None):
    address = w3.toChecksumAddress(address)
    code = (
        w3.eth.get_code(address) if block is None else w3.eth.get_code(address, block)
    )

    return True if code != b"" else False


def supports_erc_721(address, w3):
    address = w3.toChecksumAddress(address)
    contract_erc_165 = w3.eth.contract(address=address, abi=ERC_165_ABI)

    try:
        return contract_erc_165.functions.supportsInterface(ERC_721_INTERFACE_ID).call()
    except:
        return False


def find_contract_deploy(address, w3, start_block=0, end_block=None):
    # Do check if is contract in general
    # Do generatl if supports erc_721

    if end_block is None:
        end_block = w3.eth.get_block_number()

    mid_block = ((end_block - start_block) // 2) + start_block
    is_contract_at_mid = is_contract(address, w3, mid_block)

    if mid_block == start_block:
        if is_contract_at_mid:
            return start_block
        else:
            if is_contract(address, w3, end_block):
                return end_block
            else:
                raise Exception("Could not find contract deploy")

    if is_contract_at_mid:
        return find_contract_deploy(address, w3, start_block, mid_block)
    else:
        return find_contract_deploy(address, w3, mid_block, end_block)
