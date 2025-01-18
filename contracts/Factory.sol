// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./WalletLogic.sol";

contract Factory {
    event WalletDeployed(address indexed wallet, address indexed owner);

    function deployWallet(address owner, bytes32 salt) public returns (address) {
        WalletLogic wallet = new WalletLogic{salt: salt}(owner);
        emit WalletDeployed(address(wallet), owner);
        return address(wallet);
    }
}
