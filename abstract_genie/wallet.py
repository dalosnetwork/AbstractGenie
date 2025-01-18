from abstract_genie.contract import Contract

Contract = Contract()

class Wallet():
    @staticmethod
    async def deploy_multiple_contracts(signed_bytecodes, contract_names):
        result = Contract.deploy_multiple_contracts(signed_bytecodes, contract_names)

        return result

    @staticmethod
    async def generate_bytecode(contract_name, constructor_params):
        result = Contract.generate_bytecode(contract_name, constructor_params)

        return result

    @staticmethod
    async def generate_function_call_bytecode(contract_address, function_name, params, abi):
        result = Contract.generate_function_call_bytecode(contract_address, function_name, params, abi)

        return result

    @staticmethod
    async def deploy_signed_bytecodes(signed_bytecodes):
        result = Contract.deploy_signed_bytecodes(signed_bytecodes)

        return result