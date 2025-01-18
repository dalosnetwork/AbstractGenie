from wallet import Wallet
from abstract_genie.contract import Contract

Wallet = Wallet()
Contract = Contract()

async def create_new_env(constructor_params):

    contract_name = ["EntryPoint.sol", "Factory.sol", "Paymaster.sol"]

    if not contract_name:
        raise "Contract name is required."

    try:
        bytecode = Wallet.generate_bytecode(contract_name, constructor_params)

        return bytecode

    except Exception as e:
        raise f"Error in /get_bytecode: {str(e)}"

async def deploy_multiple_contracts(signed_bytecodes):
    contract_names = ["EntryPoint.sol", "Factory.sol", "Paymaster.sol"]

    result = Wallet.deploy_multiple_contracts(signed_bytecodes, contract_names)

    return result

async def generate_function_call_bytecode(contract_address, function_name, params, abi):
    try:
        # Gerekli kontrol
        if not contract_address or not function_name or not abi:
            raise "contract_address, function_name, and abi are required."

        result = Wallet.generate_function_call_bytecode(contract_address, function_name, params, abi)

        return result
    except Exception as e:
        raise f"Error generating bytecode: {str(e)}"

async def deploy_signed_bytecodes(signed_bytecodes):
    try:
        if not signed_bytecodes or not isinstance(signed_bytecodes, list):
            raise "A list of signed bytecodes is required."

        result = Wallet.deploy_signed_bytecodes(signed_bytecodes)

        return result

    except Exception as e:
        raise f"Error deploying bytecodes: {str(e)}"