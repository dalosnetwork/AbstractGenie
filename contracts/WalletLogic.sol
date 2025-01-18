// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WalletLogic {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute");
        _;
    }

    function execute(address to, uint256 value, bytes memory data) public onlyOwner {
        (bool success,) = to.call{value: value}(data);
        require(success, "Transaction failed");
    }

    function changeOwner(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }

    receive() external payable {}
}
