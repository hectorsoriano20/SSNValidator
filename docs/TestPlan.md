
# SSN Validator - Pruebas a realizar

## Indice
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
| Input | 500-25-9291 |
| Steps | <ol><li>Execute the application</li><li>Enter the valid SSN.</li><li>Press ENTER.</li></ol>
| Expected result | Valid SSN. |
| Actual result | True |

## Test 2
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Entered SSN is empty. |
| Input | Empty |
| Steps | <ol><li>Execute the application</li><li>Do not enter any SSN, whether valid or invalid.</li><li>Press ENTER.</li></ol> |
| Expected result | Invalid SSN |
| Actual result | False |

## Test 3
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter social security number (SSN) with incorrect format. |
| Input | 4432-55-335 |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad format.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN |
| Actual result | False |

## Test 4
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter valid social security number (SSN) with 000 in first part. |
| Input | 001-34-0965 |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad first part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN |
| Actual result | False |

## Test 5
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with 00 in second part. |
| Input | 012-01-9876
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad second part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN|
| Actual result | False |

## Test 6
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with 666 in first part. |
| Input | 667-00-9875
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad second part.</li><li>Press ENTER.</li></ol>
| Expected result | Invalid SSN|
| Actual result | False |
