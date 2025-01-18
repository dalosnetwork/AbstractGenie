import os
from web3 import Web3
from solcx import compile_source

class Contract():
    @staticmethod
    def deploy_multiple_contracts(signed_bytecodes, contract_names):
        """
        Birden fazla kontratın imzalanmış bytecode'unu deploy eder ve adreslerini döndürür.
        :param signed_bytecodes: İmzalanmış bytecode'ların listesi.
        :param contract_names: Kontratların isimlerinin listesi.
        :return: {contractName: contractAddress} formatında bir sözlük.
        """
        web3 = Web3(Web3.HTTPProvider("PROVIDER"))  # TODO: Sağlayıcı URL'si
        deployed_contracts = {}

        try:
            for i, signed_bytecode in enumerate(signed_bytecodes):
                if i >= len(contract_names):
                    raise ValueError("Contract names list is shorter than bytecodes list.")

                # İmzalı işlemi gönder
                tx_hash = web3.eth.send_raw_transaction(bytes.fromhex(signed_bytecode))

                # Transaction'ı bekle ve kontrat adresini al
                receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
                contract_address = receipt.contractAddress

                # Kontrat adını ve adresini kaydet
                deployed_contracts[contract_names[i]] = contract_address

            return {
                "message": "Contracts deployed successfully.",
                "deployed_contracts": deployed_contracts,
            }

        except Exception as e:
            return {
                "message": f"An error occurred: {str(e)}",
                "deployed_contracts": deployed_contracts,
            }

    @staticmethod
    def generate_bytecode(contract_names, constructor_params_list, contracts_directory="./contracts",
                                   provider="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"):
        try:
            combined_bytecode = "0x"
            web3 = Web3(Web3.HTTPProvider(provider))

            for idx, contract_name in enumerate(contract_names):
                # Her kontrat için kaynak kodu oku
                contract_path = os.path.join(contracts_directory, f"{contract_name}.sol")

                if not os.path.exists(contract_path):
                    raise FileNotFoundError(f"Contract file {contract_name}.sol not found in {contracts_directory}")

                with open(contract_path, "r") as file:
                    solidity_source = file.read()

                # Kaynak kodu derleme
                compiled_sol = compile_source(solidity_source, output_values=["abi", "bin"])

                # ABI ve Bytecode alma
                contract_interface = compiled_sol[f"<stdin>:{contract_name}"]
                bytecode = contract_interface["bin"]
                abi = contract_interface["abi"]

                # Constructor parametrelerini encode etme
                constructor_params = constructor_params_list[idx] if idx < len(constructor_params_list) else {}
                contract = web3.eth.contract(abi=abi, bytecode=bytecode)
                encoded_bytecode = contract.constructor(**constructor_params).buildTransaction({})["data"]

                # Kombine bytecode oluşturma
                combined_bytecode += encoded_bytecode[2:]  # "0x" kısmını çıkarıyoruz

            return combined_bytecode

        except Exception as e:
            print(f"Error generating combined bytecode: {str(e)}")
            return False

    @staticmethod
    def generate_function_call_bytecode(contract_address, function_name, params, abi):
        """
           Bir kontrat fonksiyonunu çalıştırmak için gerekli bytecode'u döner.
           """
        try:
            web3 = Web3(Web3.HTTPProvider("PROVIDER"))  # TODO: Sağlayıcı URL'si

            # Kontrat instansı oluştur
            contract = web3.eth.contract(address=web3.toChecksumAddress(contract_address), abi=abi)

            # Fonksiyon çağrısı için bytecode oluştur
            if not hasattr(contract.functions, function_name):
                return False

            function_call = getattr(contract.functions, function_name)(*params)
            bytecode = function_call.buildTransaction({"chainId": 1})["data"]

            return {"bytecode": bytecode}

        except Exception as e:
            return False

    @staticmethod
    def deploy_signed_bytecodes(signed_bytecodes):
        web3 = Web3(Web3.HTTPProvider("PROVIDER"))  # TODO: Sağlayıcı URL'si

        transaction_hashes = []

        for signed_bytecode in signed_bytecodes:
            try:
                # İmzalı işlemi gönder
                tx_hash = web3.eth.send_raw_transaction(bytes.fromhex(signed_bytecode))

                # Transaction hash'i kaydet
                transaction_hashes.append(web3.toHex(tx_hash))
            except Exception as e:
                transaction_hashes.append(f"Error for bytecode {signed_bytecode[:10]}: {str(e)}")

        return {
            "message": "Transactions sent to the network.",
            "transaction_hashes": transaction_hashes,
        }