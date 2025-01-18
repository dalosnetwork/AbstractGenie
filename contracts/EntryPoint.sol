// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EntryPoint {
    event UserOperationExecuted(address indexed user, bytes data);

    function executeUserOperation(address user, bytes memory data) public {
        // İşlem doğrulama ve yürütme mantığı
        (bool success,) = user.call(data);
        require(success, "User operation failed");
        emit UserOperationExecuted(user, data);
    }
}
