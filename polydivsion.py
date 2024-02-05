def polynomial_division(dividend, divisor):
  """
  Performs polynomial division of `dividend` by `divisor` using long division.

  Args:
    dividend: A list representing the coefficients of the dividend polynomial.
    divisor: A list representing the coefficients of the divisor polynomial.

  Returns:
    A tuple containing the quotient and remainder polynomials as lists.
  """

  # Ensure divisor is not zero
  if not divisor:
    raise ValueError("Divisor cannot be zero")

  # Handle cases where dividend or divisor has only one term
  if len(dividend) == 1:
    return [dividend[0] // divisor[0]], [0]
  elif len(divisor) == 1:
    quotient = []
    remainder = dividend
    while remainder:
      quotient.append(remainder[0] // divisor[0])
      remainder = [remainder[i] - quotient[-1] * divisor[0] for i in range(1, len(remainder))]
    return quotient[::-1], remainder[::-1]

  # Initialize quotient and remainder lists
  quotient = [0] * (len(dividend) - len(divisor) + 1)
  remainder = dividend[:]

  # Perform long division
  for i in range(len(dividend) - len(divisor), -1, -1):
    # Find leading coefficient of quotient term
    quotient[i] = remainder[i] // divisor[0]

    # Subtract product of quotient term and divisor from remainder
    for j in range(len(divisor)):
      remainder[i + j] -= quotient[i] * divisor[j]

    # Remove leading zeros from remainder
    while not remainder and remainder:
      remainder.pop(0)

  return quotient, remainder

# Example usage
dividend = [3, 1, 4, 7]
divisor = [1, 2]
quotient, remainder = polynomial_division(dividend, divisor)

print("Quotient:", quotient)
print("Remainder:", remainder)
