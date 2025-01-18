// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Paymaster {
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute");
        _;
    }

    constructor(address _owner) {
        owner = _owner;
    }

    function payGasFee(address to, uint256 amount) public onlyOwner {
        (bool success,) = to.call{value: amount}("");
        require(success, "Gas fee payment failed");
    }

    receive() external payable {}
}
