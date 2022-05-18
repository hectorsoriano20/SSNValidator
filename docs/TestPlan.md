
# SSN Validator - Tests

## Table of contents
1. [Test case 1](#test-1)
2. [Test case 2](#test-2)
3. [Test case 3](#test-3)
4. [Test case 4](#test-4)
5. [Test case 5](#test-5)

## Test 1
| Concept | Description |
| ----- | ----- |
| Test type | Passing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter valid social security number (SSN). |
| Input | 600-22-9991 |
| Steps | <ol><li>Execute the application</li><li>Enter the valid SSN.</li><li>Press ENTER.</li></ol>
| Expected result | Valid SSN. |
| Actual result | El SSN es valido. |

## Test 2
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Entered SSN is empty. |
| Input | Empty |
| Steps | <ol><li>Execute the application</li><li>Do not enter any SSN, whether valid or invalid.</li><li>Press ENTER.</li></ol> |
| Expected result | Invalid SSN |
| Actual result | El SSN es invalido. |

## Test 3
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter social security number (SSN) with incorrect format. |
| Input | 4444-22-332 |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad format.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN |
| Actual result | El SSN es invalido.|

## Test 4
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter valid social security number (SSN) with 000 in first part. |
| Input | 000-75-0993 |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad first part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN |
| Actual result | El SSN es invalido. |

## Test 5
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with 00 in second part. |
| Input | 064-00-9872
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad second part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN|
| Actual result | El SSN es invalido.|

## Test 6
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with 666 in first part. |
| Input | 666-00-9872
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad second part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN|
| Actual result | El SSN es invalido.|
