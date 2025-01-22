from abstract_genie.contract import Contract

Contract = Contract()

class Wallet():
    @staticmethod
    async def deploy_multiple_contracts(signed_bytecodes, contract_names, provider):
        result = Contract.deploy_multiple_contracts(signed_bytecodes, contract_names, provider)

        return result

    @staticmethod
    async def generate_bytecode(contract_name, constructor_params, provider):
        result = Contract.generate_bytecode(contract_name, constructor_params, provider)

        return result

    @staticmethod
    async def generate_function_call_bytecode(contract_address, function_name, params, abi, provider):
        result = Contract.generate_function_call_bytecode(contract_address, function_name, params, abi, provider)

        return result

    @staticmethod
    async def deploy_signed_bytecodes(signed_bytecodes, provider):
        result = Contract.deploy_signed_bytecodes(signed_bytecodes, provider)

        return result