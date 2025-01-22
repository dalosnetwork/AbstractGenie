from wallet import Wallet
from abstract_genie.contract import Contract

Wallet = Wallet()
Contract = Contract()

async def create_new_env(constructor_params, provider):

    contract_name = ["EntryPoint.sol", "Factory.sol", "Paymaster.sol"]

    if not contract_name or not provider:
        raise "Contract name and provider are required."

    try:
        bytecode = Wallet.generate_bytecode(contract_name, constructor_params, provider)

        return bytecode

    except Exception as e:
        raise f"Error in /get_bytecode: {str(e)}"

async def deploy_multiple_contracts(signed_bytecodes, provider):
    contract_names = ["EntryPoint.sol", "Factory.sol", "Paymaster.sol"]

    if not signed_bytecodes or not provider:
        raise "Signed bytecode and provider are required"

    result = Wallet.deploy_multiple_contracts(signed_bytecodes, contract_names, provider)

    return result

async def generate_function_call_bytecode(contract_address, function_name, params, abi, provider):
    try:
        # Gerekli kontrol
        if not contract_address or not function_name or not abi or not provider:
            raise "contract_address, function_name, abi and provider are required."

        result = Wallet.generate_function_call_bytecode(contract_address, function_name, params, abi, provider)

        return result
    except Exception as e:
        raise f"Error generating bytecode: {str(e)}"

async def deploy_signed_bytecodes(signed_bytecodes, provider):
    try:
        if not signed_bytecodes or not isinstance(signed_bytecodes, list) or not provider:
            raise "A list of signed bytecodes and provider are required."

        result = Wallet.deploy_signed_bytecodes(signed_bytecodes, provider)

        return result

    except Exception as e:
        raise f"Error deploying bytecodes: {str(e)}"